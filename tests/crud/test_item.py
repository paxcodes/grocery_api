from pathlib import Path

from pytest import mark, fixture

from data import schemas
from data.crud import item

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_item_json_is_successfully_mocked():
    assert item.JSON_FILE == TEST_JSON_DIR / "items.json"
