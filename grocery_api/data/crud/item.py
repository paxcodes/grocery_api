from typing import Optional, Set

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: schemas.ItemBase) -> schemas.ItemOut:
    """Creates a grocery item.

    Args:
        item (ItemBase): A pydantic schema with the properties: name, price,
            is_active, tags.

    Returns:
        ItemOut: The item created with properties: id, name, price, is_active, tags
    """
    pass


async def read(item_id: int) -> schemas.ItemOut:
    pass


async def update(item: schemas.ItemBase) -> schemas.ItemOut:
    """Updates a grocery item given a full representation of the item.

    Args:
        item (ItemBase): A pydantic schema with the properties: name, price,
            is_active, tags

    Returns:
        ItemOut: The item, including the `id` with updated attributes: name, price,
            is_active, tags
    """
    pass


async def update_tags(item_id: int, tags: Optional[Set[str]]) -> schemas.ItemOut:
    pass


async def delete(item_id: int) -> None:
    pass
