from pathlib import Path

from pytest import mark, fixture

from grocery_api.data import schemas
from grocery_api.data.crud import item

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_item_json_is_successfully_mocked():
    assert item.JSON_FILE == TEST_JSON_DIR / "items.json"


async def test_get_item_by_id():
    actual_item = await item.read(1)
    expected_item = schemas.Item(
        **{
            "id": 1,
            "name": "Salt & Pax-pper",
            "price": 3.1,
            "is_active": True,
            "tags": None,
        }
    )
    assert actual_item == expected_item
