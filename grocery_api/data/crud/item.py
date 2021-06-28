from decimal import Decimal
from typing import Dict, List, Optional, Set, TypedDict

from fastapi.encoders import jsonable_encoder

from grocery_api.data.crud.source import JSON_DIRECTORY

from . import _utils

JSON_FILE = JSON_DIRECTORY / "items.json"

class ItemDict(TypedDict):
    name: str
    price: Decimal
    is_active: bool
    tags: Optional[Set[str]]



class ItemOutDict(ItemDict):
    id: int


async def create(item: ItemDict) -> ItemOutDict:
    json_data = await _utils.read_json_data(JSON_FILE)

    new_id = _utils.get_new_id(json_data)
    json_data[new_id] = ItemOutDict(id=new_id, **item)

    await _utils.write_json_data(json_data, JSON_FILE)
    return ItemOutDict(**json_data[new_id])

async def read(item_id: int) -> Optional[ItemOutDict]:
    """Gets a item based on given {item_id}.

    Args:
        item_id (int): The item ID.

    Returns:
        Optional[ItemOutDict]: If item exists, returns a dictionary with keys: id, name,
            price, is_active, tags. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None
    serialized_data = _utils.convert_tags_to_set(json_data)
    return ItemOutDict(**serialized_data[str(item_id)])


async def read_all() -> Dict[int, dict]:
    json_data = await _utils.read_json_data(JSON_FILE)
    return {
        int(id): data
        for id, data in json_data.items()
    }


async def update(item_id: int, item: ItemDict) -> Optional[ItemOutDict]:
    """Updates (replaces) a grocery item given a full representation of the item."""
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    updated_item_data = ItemOutDict(id=item_id, **item)
    json_data[str(item_id)] = updated_item_data

    await _utils.write_json_data(json_data, JSON_FILE)
    return ItemOutDict(**updated_item_data)


async def update_tags(
    item_id: int, tags: Optional[Set[str]]
) -> Optional[ItemOutDict]:
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    json_data[str(item_id)]["tags"] = jsonable_encoder(tags)
    await _utils.write_json_data(json_data, JSON_FILE)
    return ItemOutDict(**json_data[str(item_id)])


async def delete(item_id: int) -> None:
    """Deletes an item with the given {item_id}.

    Args:
        item_id (int): The ID of the item.

    Raises:
        ValueError - If {item_id} does not exist.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        raise ValueError(f"Item {item_id} does not exist.")

    del json_data[str(item_id)]
    await _utils.write_json_data(json_data, JSON_FILE)
