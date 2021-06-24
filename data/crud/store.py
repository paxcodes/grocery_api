from .. import schemas
from .source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "stores.json"


async def create(store: schemas.Store):
    pass


async def read(store_id: int):
    pass


async def update(store: schemas.Store):
    pass


async def delete(store_id: int):
    pass
