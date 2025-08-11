import logging
import subprocess
from typing import Annotated
from langchain_core.tools import tool
from src.log import log_io

# Initialize logger
logger = logging.getLogger(__name__)


@tool
@log_io
def bash_tool(
    cmd: Annotated[str, "The bash command to be executed."],
):
    """
    Executes a bash command and captures its output.

    Args:
        cmd (str): The bash command to be executed.

    Returns:
        str: The stdout of the command as a string.

    Raises:
        subprocess.CalledProcessError: If the command fails with a non-zero exit code.

    """
    
    logger.info(f"Executing Bash Command: {cmd}")
    try:
        # Execute the command and capture output
        result = subprocess.run(
            cmd, shell=True, check=True, text=True, capture_output=True
        )
        # Return stdout as the result
        return result.stdout
    except subprocess.CalledProcessError as e:
        # If command fails, return error information
        error_message = f"Command failed with exit code {e.returncode}.\nStdout: {e.stdout}\nStderr: {e.stderr}"
        logger.error(error_message)
        return error_message
    except Exception as e:
        # Catch any other exceptions
        error_message = f"Error executing command: {str(e)}"
        logger.error(error_message)
        return error_message
