from .. import schemas
from .source import JSON_DIRECTORY

JSON_FILE = JSON_DIRECTORY / "items.json"


async def create(item: schemas.Item):
    pass


async def read(item_id: int):
    pass


async def update(item: schemas.Item):
    pass


async def delete(item_id: int):
    pass
