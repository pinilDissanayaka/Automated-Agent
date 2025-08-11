import os
from typing import Annotated
from langchain_core.tools import tool
from src.log import log_io


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
    file_path = os.path.join(os.getcwd(), "output.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)