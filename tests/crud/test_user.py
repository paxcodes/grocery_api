from data.schemas import user as user_schema
from pytest import fixture

from data.crud import user as user_crud

from .json_dir import TEST_JSON_DIR


def test_user_json_is_successfully_mocked():
    assert user_crud.JSON_FILE == TEST_JSON_DIR / "users.json"
