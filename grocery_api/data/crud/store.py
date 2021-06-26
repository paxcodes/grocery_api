from typing import Optional

from grocery_api.data import schemas
from grocery_api.data.crud.source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "stores.json"


async def create(store: schemas.StoreBase) -> schemas.StoreOut:
    pass


async def read(store_id: int) -> Optional[schemas.StoreOut]:
    pass


async def update(store_id: int, store: schemas.StoreBase) -> Optional[schemas.StoreOut]:
    """Updates (replaces) a grocery store given a full representation of the store."""
    pass


async def update_parent_company(
    store_id: int, parent_company: str
) -> Optional[schemas.StoreOut]:
    pass


async def delete(store_id: int) -> None:
    """Deletes a store with the given {store_id}.

    Args:
        store_id (int): The ID of the store.

    Raises:
        ValueError - If {store_id} does not exist.
    """
    pass
