import modal

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
    .run_commands(
        "git clone https://github.com/August-murr/Ouroboros.git /home/Ouroboros"
    )
)

app = modal.App.lookup("mlebench-app-GPU", create_if_missing=True)

with modal.enable_output():
    sb = modal.Sandbox.create(
        app=app,
        image=image,
        timeout=30 * 60,
        cpu=4,
        #gpu="T4", # Values range from T4 to B200:8 
    )