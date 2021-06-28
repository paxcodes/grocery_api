from typing import Optional, TypedDict

from grocery_api.data.crud.source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "stores.json"

StoreDict = TypedDict("StoreDict", {
    'name': str,
    'founding_year': int,
    'is_active': bool,
    'parent_company': Optional[str]
})

class StoreOutDict(StoreDict):
    id: int


async def create(store: StoreDict) -> StoreOutDict:
    pass


async def read(store_id: int) -> Optional[StoreOutDict]:
    pass


async def update(store_id: int, store: StoreDict) -> Optional[StoreOutDict]:
    """Updates (replaces) a grocery store given a full representation of the store."""
    pass


async def update_parent_company(
    store_id: int, parent_company: str
) -> Optional[StoreOutDict]:
    pass


async def delete(store_id: int) -> None:
    """Deletes a store with the given {store_id}.

    Args:
        store_id (int): The ID of the store.

    Raises:
        ValueError - If {store_id} does not exist.
    """
    pass
