from typing import Optional, TypedDict

from grocery_api.data.crud.source import JSON_DIRECTORY

from . import _utils


JSON_FILE = JSON_DIRECTORY / "stores.json"


class StoreDict(TypedDict):
    name: str
    founding_year: int
    is_active: bool
    parent_company: Optional[str]


class StoreOutDict(StoreDict):
    id: int


async def create(store: StoreDict) -> StoreOutDict:
    json_data = await _utils.read_json_data(JSON_FILE)
    
    new_id = _utils.get_new_id(json_data)
    json_data[new_id] = StoreOutDict(id=new_id, **store)
    
    await _utils.write_json_data(json_data, JSON_FILE)
    return StoreOutDict(**json_data[new_id])


async def read(store_id: int) -> Optional[StoreOutDict]:
    """Gets a store based on given {store_id}.

    Args:
        store_id (int): The Store ID.

    Returns:
        Optional[StoreOutDict]: If store exists, returns a dictionary with keys: id, name,
            founding_year, is_active, parent_company. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(store_id) not in json_data:
        return None
    return json_data[str(store_id)]


async def update(store_id: int, store: StoreDict) -> Optional[StoreOutDict]:
    """Updates (replaces) a grocery store given a full representation of the store.
    
    Args:
        store_id (int): The Store ID.
        store (StoreDict): A dictionary containing new data that has the keys:
            name, founding_year, is_active, parent_company

    Returns:
        Optional[StoreOutDict]: If store exists, returns a dictionary with the
            updated data. It will contain keys: id, name, founding_year,
            is_active, parent_company. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(store_id) not in json_data:
        return None
    json_data[str(store_id)] = StoreOutDict(id=store_id, **store)
    await _utils.write_json_data(json_data, JSON_FILE)
    return json_data[str(store_id)]



async def update_parent_company(
    store_id: int, new_parent_company: Optional[str]
) -> Optional[StoreOutDict]:
    """Updates parent company of store.

    Args:
        store_id (int): The store ID.
        new_parent_company (Optional[str]): The new parent company.

    Returns:
        Optional[StoreOutDict]: If store exists, returns a dictionary with the
            updated data. It will contain keys: id, name, founding_year,
            is_active, parent_company. Otherwise, `None`.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(store_id) not in json_data:
        return None
    json_data[str(store_id)]["parent_company"] = new_parent_company
    await _utils.write_json_data(json_data, JSON_FILE)
    return json_data[str(store_id)]


async def delete(store_id: int) -> None:
    """Deletes a store with the given {store_id}.

    Args:
        store_id (int): The ID of the store.

    Raises:
        ValueError - If {store_id} does not exist.
    """
    json_data = await _utils.read_json_data(JSON_FILE)
    if str(store_id) not in json_data:
        raise ValueError(f"Store {store_id} does not exist.")
    
    del json_data[str(store_id)]
    await _utils.write_json_data(json_data, JSON_FILE)
