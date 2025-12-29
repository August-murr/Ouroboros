import modal


# This script creates and starts a GPU-enabled Modal sandbox preloaded with
# an MLEbench-compatible image and common ML dependencies (e.g., PyTorch,
# transformers). It also installs `openhands` into the image so agents can run
# OpenHands-based workloads without extra manual setup.


# ------------------------- Image definition -------------------------
# Build the runtime image used by the sandbox. We pull an existing registry
# image that already contains typical ML tooling and then make small runtime
# tweaks: install `curl`, install `openhands` via the tool command, and set
# the container entrypoint to `sleep infinity` so the sandbox stays alive.
image = (
    modal.Image.from_registry("cdreetz/mlebench-env:latest")
    .apt_install("curl")
    .run_commands(
        "uv tool install openhands --python 3.12"
    )
    # Keep the container running so you can `modal shell` into it.
    .entrypoint(["sleep", "infinity"])
    # Add a local OpenHands agent config so OpenHands will find it without
    # additional manual steps. See docs.md for details about creating this
    # `agent_settings.json` and where to place it locally.
    .add_local_file(
        local_path="/workspaces/Ouroboros/openhands_agent_config/agent_settings.json",
        remote_path="/root/.openhands/agent_settings.json",
        copy=True
    )
    .add_local_file(
        local_path="/workspaces/Ouroboros/openhands_agent_config/kaggle.json",
        remote_path="/root/.kaggle/kaggle.json",
        copy=True
    )
    .run_commands(
        "mlebench prepare -c dog-breed-identification --data-dir /home/data/"
    )
)


# ------------------------- App & Volume -------------------------
# Look up (or create) a Modal App to host the sandbox and a named Modal
# Volume for persistent storage that is mounted into the sandbox at `/vol`.
app = modal.App.lookup("mlebench-app-GPU", create_if_missing=True)
vol = modal.Volume.from_name("my-volume", create_if_missing=True)


# ------------------------- Sandbox creation -------------------------
# Create the sandbox with the chosen image, attach the volume, and request
# resources (CPU and GPU). `timeout` is how long the sandbox stays active
# before automatic termination (seconds).
with modal.enable_output():
    sb = modal.Sandbox.create(
        app=app,
        image=image,
        volumes={"/vol": vol},
        timeout=30 * 60,
        cpu=4,
        #gpu="T4", # Values range from T4 to B200:8 
    )

# print sandbox id
print(f"Sandbox ID: {sb.object_id}")

#with modal.enable_output():
#    logs = sb.exec("/usr/local/bin/openhands", "--always-approve", "--file", "/home/instructions.txt")



# to run

# To grade a submission (note: output goes to stderr):
# result = sb.exec(
#     "mlebench", 
#     "grade-sample", 
#     "/home/data/dog-breed-identification/prepared/public/sample_submission.csv", 
#     "dog-breed-identification", 
#     "--data-dir", 
#     "/home/data"
# )
# print(result.stderr.read())

# If you want the script to terminate the sandbox at the end of this run,
# call `sb.terminate()` here. The line is left commented so the sandbox stays
# alive for interactive use.
# sb.terminate()