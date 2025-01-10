import json

from src.core.logging_utils import get_logger

logger = get_logger(__name__)


def str_to_bool(value: str, default: bool = None) -> bool:
    """
    Convert a string to a boolean with a default value for invalid inputs.

    Args:
        value (str): The input string.
        default (bool): The default value to return for invalid inputs.

    Returns:
        bool: The boolean representation of the string or the default value.
    """
    value = value.strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    elif default is not None:
        return default
    else:
        raise ValueError(f"Failed to convert str to bool. value: ${value}")


def parse_json_beautifully(json_value: str):
    try:
        parsed_json = json.loads(json_value)
        return json.dumps(parsed_json, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.warning(f"Failed to parse json beautifully. error: {e}")
        return json_value
