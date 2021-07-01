from pytest import mark

from pydantic import UUID4

from grocery_api.data.crud import user as user_crud

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_user_json_is_successfully_mocked():
    assert user_crud.JSON_FILE == TEST_JSON_DIR / "users.json"


async def test_it_can_get_user_by_id():
    actual_user = await user_crud.read(UUID4("c6fce069-4748-499d-a85d-bf310bfd534b"))
    expected_user = dict(
        id=UUID4("c6fce069-4748-499d-a85d-bf310bfd534b"),
        username="sons_code_not_pax",
        email="alphonse_jack@paxmargret.33mail.com",
        sh_password="07dbb6e6832da0841dd79701200e4b179f1a94a7b3dd26f612817f3c03117434",
        salt="et52edye5sf8",
    )
    assert actual_user == expected_user
