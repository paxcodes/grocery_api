from decimal import Decimal
from typing import Dict, Optional, Set, TypedDict

from fastapi.encoders import jsonable_encoder

from grocery_api.data.source import JSON_DIRECTORY

from . import _utils

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: dict) -> dict:
    """Creates a new item.

    Args:
        item (dict): A dictionary with the keys: name,
            price, is_active, tags.

    Returns:
        dict: A dictionary with the keys: id, name,
            price, is_active, tags.
    """
    json_data = await _utils.read_json_data(JSON_FILE)

    new_id = _utils.get_new_id(json_data)
    json_data[new_id] = jsonable_encoder(dict(id=new_id, **item))

    await _utils.write_json_data(json_data, JSON_FILE)
    return dict(**json_data[new_id])


async def read(item_id: int) -> Optional[dict]:
    """Gets a item based on given {item_id}.

    Args:
        item_id (int): The item ID.

    Returns:
        Optional[dict]: If item exists, returns a dictionary with keys: id, name,
            price, is_active, tags. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None
    serialized_data = _utils.convert_tags_to_set(json_data)
    return dict(**serialized_data[str(item_id)])


async def read_all() -> Dict[int, dict]:
    """Returns all the items.

    Returns:
        Dict[int, dict]: A dictionary with IDs as keys, and each value is an item
            (a dictionary with the keys: id, name, price, is_active, tags.)
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    return {int(id): data for id, data in json_data.items()}


async def update(item_id: int, item: dict) -> Optional[dict]:
    """Updates (replaces) a grocery item given a full representation of the item.

    Args:
        item_id (int): The item ID.
        item (dict): A dictionary (the new data) with the keys: name, price,
            is_active, tags.

    Returns:
        Optional[dict]: If item exists, returns a dictionary (the item with new data)
            with keys: id, name, price, is_active, tags. Otherwise, `None`.
    """

    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    updated_item_data = dict(id=item_id, **item)
    json_data[str(item_id)] = jsonable_encoder(updated_item_data)

    await _utils.write_json_data(json_data, JSON_FILE)
    return updated_item_data


async def update_price(item_id: int, price: Decimal) -> Optional[dict]:
    """Update the price of the item.

    Args:
        item_id (int): The item ID whose price will be updated.
        price (Decimal): The new price.

    Returns:
        Optional[dict]: If item exists, returns a dictionary (the item with new price)
            with keys: id, name, price, is_active, tags. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(item_id) not in json_data:
        return None

    json_data[str(item_id)]["price"] = jsonable_encoder(price)
    await _utils.write_json_data(json_data, JSON_FILE)
    return dict(**json_data[str(item_id)])


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
