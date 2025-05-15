import re
from typing import Any

from tools.enum.filetype import SyntaxFormat, FileType
from tools.utils.file_util import strip_wrapper

THINK_TAG_REGEX = re.compile(r'<think>.*?</think>', flags=re.DOTALL)

def get_input_text(tool_parameters: dict[str, Any]) -> str:
    input_text = tool_parameters.get("input_text", "")
    input_filetype = tool_parameters.get("input_filetype", "")
    if not input_text:
        raise ValueError(f"Empty input text")
    remove_think_prompt = tool_parameters.get("remove_think_prompt", True)
    if remove_think_prompt:
        input_text = THINK_TAG_REGEX.sub('', input_text)

    if input_filetype:
        # Remove the wrapper from the input text
        input_text = strip_wrapper(input_text, input_filetype)
    if input_filetype == SyntaxFormat.MARKDOWN:
        input_text = input_text.replace("\\\\", "\\")

    input_text = input_text.replace("\\n", "\n")
    if not input_text:
        raise ValueError(f"Empty input text")
    return input_text

def get_input_filetype(tool_parameters: dict[str, Any]) -> str:
    input_filetype = tool_parameters.get("input_filetype", "")
    if not input_filetype:
        raise ValueError(f"Empty input filetype")
    
    try:
        # Case-insensitive lookup by key name
        return SyntaxFormat[input_filetype.upper()]
    except KeyError:
        raise ValueError(f"Invalid input filetype: {input_filetype}. Must be a valid SyntaxFormat key.")


def get_output_filetype(tool_parameters: dict[str, Any]) -> str:
    output_filetype = tool_parameters.get("output_filetype", "")
    if not output_filetype:
        raise ValueError(f"Empty output filetype")
    
    try:
        # Case-insensitive lookup by key name
        return FileType[output_filetype.upper()]
    except KeyError:
        raise ValueError(f"Invalid input filetype: {output_filetype}. Must be a valid SyntaxFormat key.")



