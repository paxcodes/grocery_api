from pytest import fixture

from grocery_api.data.crud import store

from .json_dir import TEST_JSON_DIR


def test_store_json_is_successfully_mocked():
    assert store.JSON_FILE == TEST_JSON_DIR / "stores.json"
