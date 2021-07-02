from pydantic import UUID4

from grocery_api.data.source import JSON_DIRECTORY

from . import _utils


JSON_FILE = JSON_DIRECTORY / "users.json"


# Using UUID4 doesn't do runtime type-checking here, only static type-checking.
async def read(user_id: str) -> dict:
    """Get a user by their ID.

    Args:
        user_id (str): The user's ID (UUID4).

    Returns:
        dict: A dictionary (the user) with the keys: id, email, username,
            sh_password, salt. For the sake of demonstrating FastAPI filtering data
            based on response_model, let's return all attributes including sensitive
            data such as their salted & hashed password and their salt.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    return _transform_to_user_sensitive_data_dict(json_data[user_id])


def _transform_to_user_sensitive_data_dict(json_data: dict) -> dict:
    """Transforms a JSON dictionary object to `dict`.

    This includes transforming json-compatible data to their proper types.
    E.g. a `str` to a `UUID`

    Args:
        json_data (dict): A dictionary object with json-compatible types.

    Returns:
        dict: A dictionary with values that have
            non-JSON-compatible types like UUID.
    """
    return dict(
        id=UUID4(json_data["id"]),
        email=json_data["email"],
        username=json_data["username"],
        sh_password=json_data["sh_password"],
        salt=json_data["salt"],
    )
