import asyncio
import json

import aiofiles
from pydantic import UUID4

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "users.json"


# Using UUID4 doesn't do runtime type-checking here, only static type-checking.
async def read(user_id: UUID4) -> schemas.UserSensitiveData:
    """Get a user by their ID.

    Args:
        user_id (UUID4): The user's ID.

    Returns:
        schemas.UserSensitiveData: For the sake of demonstrating FastAPI filtering data
            based on response_model, let's return all attributes including sensitive
            data such as their salted & hashed password and their salt.
    """
    async with aiofiles.open(JSON_FILE) as f:
        file_data = await f.read()
    json_data = json.loads(file_data)
    return schemas.UserSensitiveData(**json_data[str(user_id)])
