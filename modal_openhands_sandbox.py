"""
Modal Sandbox Setup for OpenHands Agent

This script sets up and manages a Modal sandbox environment for running OpenHands.
It defines a containerized image, creates a Modal app, instantiates a sandbox,
and provides cleanup functionality.
"""

import modal


def setup_image():
    """
    Define the Modal image for the OpenHands sandbox.
    
    This image:
    - Starts from a minimal Debian base
    - Installs curl (needed for uv installer)
    - Uses uv to install OpenHands with Python 3.12
    - Adds a preconfigured agent_settings.json file to ~/.openhands/
      (this directory is the standard OpenHands configuration location)
    
    The local agent_settings.json is copied from the workspace to the container
    at /root/.openhands/agent_settings.json where OpenHands expects to find it.
    """
    image = (
        modal.Image.debian_slim()
        .apt_install("curl")
        .run_commands(
            "uv tool install openhands --python 3.12"
        )
        .add_local_file(
            local_path="/path/to/local/agent_settings.json",  # Placeholder: path to your config file
            remote_path="/root/.openhands/agent_settings.json"  # Standard OpenHands config location
        )
    )
    return image


def create_app():
    """
    Lookup or create a Modal app instance.
    
    The app acts as a container for all Modal resources and functions.
    If an app with this name already exists, it will be reused.
    """
    app = modal.App.lookup("my-app", create_if_missing=True)
    return app


def create_sandbox(app, image):
    """
    Create and start a Modal sandbox with the specified image.
    
    Parameters:
    - app: Modal app instance
    - image: Modal image definition
    
    Configuration:
    - timeout: 30 minutes (1800 seconds) for the sandbox to run
    - cpu: 4 CPU cores allocated
    - gpu: Commented out - uncomment "T4" to enable GPU support if needed
    """
    with modal.enable_output():
        sb = modal.Sandbox.create(
            app=app,
            image=image,
            timeout=30 * 60,  # 30 minutes
            # gpu="T4",  # Uncomment to enable GPU support
            cpu=4
        )
    return sb


def terminate_sandbox(sandbox):
    """
    Terminate the sandbox and clean up resources.
    
    This should be called when you're done with the sandbox to avoid
    unnecessary resource consumption.
    """
    sandbox.terminate()


# Main execution
if __name__ == "__main__":
    # Setup the image
    image = setup_image()
    print("✓ Modal image configured")
    
    # Create or lookup the app
    app = create_app()
    print("✓ Modal app created/retrieved")
    
    # Create the sandbox
    sandbox = create_sandbox(app, image)
    print("✓ Sandbox created and running")
    
    # When done, clean up
    # Uncomment the line below to terminate the sandbox
    # terminate_sandbox(sandbox)
