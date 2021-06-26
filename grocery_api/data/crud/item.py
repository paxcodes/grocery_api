import json
from typing import Optional, Set

import aiofiles
from fastapi.encoders import jsonable_encoder

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

from ._utils import get_new_id

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: schemas.ItemBase) -> schemas.ItemOut:
    async with aiofiles.open(JSON_FILE) as f:
        file_data = await f.read()
    json_data = json.loads(file_data)

    new_id = get_new_id(json_data)
    json_data[new_id] = {**{"id": new_id}, **jsonable_encoder(item)}

    # Save the JSON data back to the JSON file
    async with aiofiles.open(JSON_FILE, mode="w") as f:
        await f.write(json.dumps(json_data, indent=4))

    return schemas.ItemOut(**json_data[new_id])


async def read(item_id: int) -> Optional[schemas.ItemOut]:
    async with aiofiles.open(JSON_FILE) as f:
        file_data = await f.read()
    json_data = json.loads(file_data)

    return schemas.ItemOut(**json_data[str(item_id)])


async def update(item_id: int, item: schemas.ItemBase) -> Optional[schemas.ItemOut]:
    """Updates (replaces) a grocery item given a full representation of the item."""
    pass


async def update_tags(
    item_id: int, tags: Optional[Set[str]]
) -> Optional[schemas.ItemOut]:
    pass


async def delete(item_id: int) -> None:
    """Deletes an item with the given {item_id}.

    Args:
        item_id (int): The ID of the item.

    Raises:
        ValueError - If {item_id} does not exist.
    """
    async with aiofiles.open(JSON_FILE) as f:
        file_data = await f.read()
    json_data = json.loads(file_data)

    del json_data[str(item_id)]

    async with aiofiles.open(JSON_FILE, mode="w") as f:
        await f.write(json.dumps(json_data, indent=4))
