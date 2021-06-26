from typing import Optional, Set

from fastapi.encoders import jsonable_encoder

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

from . import _utils

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: schemas.ItemBase) -> schemas.ItemOut:
    json_data = await _utils.read_json_data(JSON_FILE)

    new_id = _utils.get_new_id(json_data)
    json_data[new_id] = {**{"id": new_id}, **jsonable_encoder(item)}

    await _utils.write_json_data(json_data, JSON_FILE)
    return schemas.ItemOut(**json_data[new_id])


async def read(item_id: int) -> Optional[schemas.ItemOut]:
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None
    return schemas.ItemOut(**json_data[str(item_id)])


async def update(item_id: int, item: schemas.ItemBase) -> Optional[schemas.ItemOut]:
    """Updates (replaces) a grocery item given a full representation of the item."""
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    updated_item_data = {**{"id": item_id}, **jsonable_encoder(item)}
    json_data[str(item_id)] = updated_item_data

    await _utils.write_json_data(json_data, JSON_FILE)
    return schemas.ItemOut(**updated_item_data)


async def update_tags(
    item_id: int, tags: Optional[Set[str]]
) -> Optional[schemas.ItemOut]:
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    json_data[str(item_id)]["tags"] = jsonable_encoder(tags)
    await _utils.write_json_data(json_data, JSON_FILE)
    return schemas.ItemOut(**json_data[str(item_id)])


async def delete(item_id: int) -> None:
    """Deletes an item with the given {item_id}.

    Args:
        item_id (int): The ID of the item.

    Raises:
        ValueError - If {item_id} does not exist.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    del json_data[str(item_id)]
    await _utils.write_json_data(json_data, JSON_FILE)
