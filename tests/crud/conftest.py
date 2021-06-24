from pytest import fixture

from data.crud import user, store, item
from .json_dir import TEST_JSON_DIR


@fixture(autouse=True)
def mock_json_directory(mocker):
    mocker.patch.object(user, "JSON_FILE", new=TEST_JSON_DIR / "users.json")
    mocker.patch.object(store, "JSON_FILE", new=TEST_JSON_DIR / "stores.json")
    mocker.patch.object(item, "JSON_FILE", new=TEST_JSON_DIR / "items.json")
