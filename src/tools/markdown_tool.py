import os
import logging
from typing import Annotated
from langchain_core.tools import tool
from src.log import log_io

logger = logging.getLogger(__name__)

@tool
@log_io
def write_markdown_file(
    content:Annotated[str, "The content to write to the markdown file."],
) -> None:
    """
    Writes the given content to a markdown file named "output.md" in the current directory.
    
    Args:
        content (str): The content to write to the markdown file.
    """
    logger.info("Preparing to write content to markdown file.")

    file_path = os.path.join(os.getcwd(), "output.md")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        logger.error(f"Error writing markdown file: {e}")
        return e
