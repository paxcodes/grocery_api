from pydantic import UUID4

from .. import schemas
from .source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "users.json"


async def read_user(user_id: UUID4) -> schemas.UserSensitiveData:
    # For the sake of demonstrating FastAPI filtering data based on response_model,
    # let's return all attributes here.
    pass
