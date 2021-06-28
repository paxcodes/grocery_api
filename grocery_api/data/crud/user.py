from typing import TypedDict
from pydantic import UUID4

from grocery_api.data.crud.source import JSON_DIRECTORY

from . import _utils


JSON_FILE = JSON_DIRECTORY / "users.json"


class UserSensitiveDataDict(TypedDict):
    id: UUID4
    email: str
    username: str
    sh_password: str
    salt: str


# Using UUID4 doesn't do runtime type-checking here, only static type-checking.
async def read(user_id: UUID4) -> UserSensitiveDataDict:
    """Get a user by their ID.

    Args:
        user_id (UUID4): The user's ID.

    Returns:
        schemas.UserSensitiveData: For the sake of demonstrating FastAPI filtering data
            based on response_model, let's return all attributes including sensitive
            data such as their salted & hashed password and their salt.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    return _transform_to_user_sensitive_data_dict(json_data[str(user_id)])


def _transform_to_user_sensitive_data_dict(json_data: dict) -> UserSensitiveDataDict:
    """Transforms a JSON dictionary object to `UserSensitiveDataDict`.

    This includes transforming json-compatible data to their proper types. 
    E.g. a `str` to a `UUID`

    Args:
        json_data (dict): A dictionary object with json-compatible types.

    Returns:
        UserSensitiveDataDict: A dictionary with values that have
            non-JSON-compatible types like UUID.
    """
    return UserSensitiveDataDict(
        id=UUID4(json_data["id"]),
        email=json_data["email"],
        username=json_data["username"],
        sh_password=json_data["sh_password"],
        salt=json_data["salt"],
    )
