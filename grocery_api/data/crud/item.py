from typing import Optional, Set

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: schemas.ItemBase) -> schemas.ItemOut:
    pass


async def read(item_id: int) -> Optional[schemas.ItemOut]:
    pass


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
    pass
