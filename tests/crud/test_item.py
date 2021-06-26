from pytest import mark, fixture

from grocery_api.data import schemas
from grocery_api.data.crud import item as item_crud

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_item_json_is_successfully_mocked():
    assert item_crud.JSON_FILE == TEST_JSON_DIR / "items.json"


@fixture
async def created_item() -> schemas.ItemOut:
    given_new_item_data = {
        "name": "Bananas in Pyjamas",
        "price": 400.1,
        "is_active": True,
        "tags": None,
    }
    actual_new_item = await item_crud.create(schemas.ItemBase(**given_new_item_data))
    yield actual_new_item
    await item_crud.delete(actual_new_item.id)


async def test_it_can_create_item(created_item: schemas.ItemOut):
    actual_new_item = await item_crud.read(created_item.id)
    assert actual_new_item == schemas.ItemOut(
        **{
            "id": 6,
            "name": "Bananas in Pyjamas",
            "price": 400.1,
            "is_active": True,
            "tags": None,
        }
    )


async def test_it_can_read_item_by_id():
    actual_item = await item_crud.read(1)
    expected_item = schemas.ItemOut(
        **{
            "id": 1,
            "name": "Salt & Pax-pper",
            "price": 3.1,
            "is_active": True,
            "tags": None,
        }
    )
    assert actual_item == expected_item


@fixture
async def given_item() -> schemas.ItemOut:
    item_id = 1
    original_item = await item_crud.read(item_id)
    assert original_item
    yield original_item
    await item_crud.update(item_id, original_item)


async def test_it_can_update_item(given_item: schemas.ItemOut):
    given_new_data = {
        "name": "Saltz & Pax-pper",
        "price": 2.5,
        "is_active": True,
    }

    await item_crud.update(given_item.id, schemas.ItemBase(**given_new_data))
    actual_item = await item_crud.read(given_item.id)

    expected_item = schemas.ItemOut(
        **{
            "id": given_item.id,
            "name": "Saltz & Pax-pper",
            "price": 2.5,
            "is_active": True,
            "tags": None,
        }
    )
    assert actual_item == expected_item


async def test_it_can_update_item_tags(given_item: schemas.ItemOut):
    given_new_tags = {"pantry"}

    await item_crud.update_tags(given_item.id, given_new_tags)
    actual_item = await item_crud.read(given_item.id)

    expected_item = given_item.copy(update={"tags": given_new_tags})
    assert actual_item == expected_item


async def test_it_can_delete_item_by_id(given_item: schemas.ItemOut):
    await item_crud.delete(given_item.id)
    actual_item = await item_crud.read(given_item.id)

    assert actual_item is None
