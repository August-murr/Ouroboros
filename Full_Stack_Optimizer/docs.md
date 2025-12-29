# Modal Sandbox Builder — Documentation

Purpose
- This folder contains `Modal_Sandbox_builder.py`, a small script that
  creates a GPU-enabled Modal sandbox using an MLEbench-friendly image and
  installs `openhands` so agent processes can run ML workloads.

OpenHands configuration
- OpenHands requires an `agent_settings.json` file for provider/model/API
  configuration. This script expects a local copy at
  `/workspaces/Ouroboros/openhands_agent_config/agent_settings.json` which
  is copied into the sandbox at `/root/.openhands/agent_settings.json`.
- To create this file locally:
  1. Configure OpenHands once in an interactive environment (or create the
     JSON manually) with your chosen provider and model name.
  2. Save the resulting JSON to the folder `openhands_agent_config` in the
     repo root.
- Alternative: instead of copying the config, change the `local_path` in
  `Modal_Sandbox_builder.py` to wherever you prefer to keep your local
  `agent_settings.json`.

Modal Volume (persistent storage)
- The script attaches a named Modal Volume (`my-volume`) and mounts it at
  `/vol` inside the sandbox. This is useful to persist datasets, logs,
  model checkpoints, or other artifacts.
- To download files from the volume to your local machine:

```bash
modal volume get my-volume path/in/volume/file.tar.gz ./local-destination/
```

Connecting to the sandbox
- After creating the sandbox, you can connect with a shell using the
  sandbox id shown in the Modal dashboard:

```bash
modal shell <sandbox-id>
```

Running OpenHands inside the sandbox
- OpenHands may be installed at a system path like `/usr/local/bin/openhands`.
  Run it directly if needed. Example:

```bash
/usr/local/bin/openhands --always-approve
```

- Note: `--always-approve` gives the agent autonomy to act without
  interactive confirmation.

Termination
- You can terminate the sandbox programmatically by calling `sb.terminate()`
  in the script or from the Modal dashboard. `Modal_Sandbox_builder.py` leaves
  termination commented out so the sandbox remains available for manual use.

Summary
- `Modal_Sandbox_builder.py` creates a sandboxed environment where an
  autonomous coding agent can access GPUs and ML packages. The `openhands`
  config file enables OpenHands to run without further manual configuration.
