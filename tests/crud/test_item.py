from decimal import Decimal

from pytest import mark, fixture, raises

from grocery_api.data import item as item_crud

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_item_json_is_successfully_mocked():
    assert item_crud.JSON_FILE == TEST_JSON_DIR / "items.json"


@fixture
async def created_item() -> dict:
    given_new_item_data = dict(
        name="Bananas in Pyjamas", price=Decimal(400.1), is_active=True, tags=None
    )
    actual_new_item = await item_crud.create(given_new_item_data)
    yield actual_new_item
    await item_crud.delete(actual_new_item["id"])


async def test_it_can_create_item(created_item: dict):
    actual_new_item = await item_crud.read(created_item["id"])
    assert actual_new_item == dict(
        id=6,
        name="Bananas in Pyjamas",
        price=Decimal(400.1),
        is_active=True,
        tags=None,
    )


async def test_it_can_read_all_items():
    actual_items = await item_crud.read_all()
    assert list(actual_items.keys()) == [1, 2, 3, 4, 5]
    assert actual_items[1] == {
        "id": 1,
        "name": "Salt & Pax-pper",
        "price": 3.1,
        "is_active": True,
        "tags": None,
    }


async def test_it_can_read_item_by_id():
    actual_item = await item_crud.read(1)
    expected_item = dict(
        id=1,
        name="Salt & Pax-pper",
        price=Decimal(3.1),
        is_active=True,
        tags=None,
    )
    assert actual_item == expected_item


async def test_read_returns_none_when_item_does_not_exist():
    actual_item = await item_crud.read(100)
    assert actual_item is None


@fixture
async def given_item() -> dict:
    item_id = 1
    original_item = await item_crud.read(item_id)
    assert original_item
    yield original_item
    await item_crud.update(
        item_id,
        dict(
            name=original_item["name"],
            price=original_item["price"],
            is_active=original_item["is_active"],
            tags=original_item["tags"],
        ),
    )


async def test_it_can_update_item(given_item: dict):
    given_new_data = dict(
        name="Saltz & Pax-pper",
        price=Decimal(2.5),
        is_active=True,
        tags=None,
    )

    await item_crud.update(given_item["id"], given_new_data)
    actual_item = await item_crud.read(given_item["id"])

    expected_item = dict(
        id=given_item["id"],
        name="Saltz & Pax-pper",
        price=Decimal(2.5),
        is_active=True,
        tags=None,
    )
    assert actual_item == expected_item


async def test_update_returns_none_when_item_does_not_exist():
    actual_item = await item_crud.update(
        100,
        dict(name="Saltz & Pax-pper", price=Decimal(2.5), is_active=True, tags=None),
    )
    assert actual_item is None


async def test_it_can_update_item_price(given_item: dict):
    given_new_price = Decimal(540.99)

    await item_crud.update_price(given_item["id"], given_new_price)
    actual_item = await item_crud.read(given_item["id"])

    expected_item = given_item.copy()
    expected_item["price"] = given_new_price
    assert actual_item == expected_item


async def test_update_price_returns_none_when_item_does_not_exist():
    actual_item = await item_crud.update_price(
        100,
        Decimal(10_000),
    )
    assert actual_item is None


@fixture
async def given_item_to_be_deleted() -> dict:
    item_id = 5
    original_item = await item_crud.read(item_id)
    assert original_item
    yield original_item
    await item_crud.create(
        dict(
            name=original_item["name"],
            price=original_item["price"],
            is_active=original_item["is_active"],
            tags=original_item["tags"],
        )
    )


async def test_it_can_delete_item_by_id(given_item_to_be_deleted: dict):
    await item_crud.delete(given_item_to_be_deleted["id"])
    actual_item = await item_crud.read(given_item_to_be_deleted["id"])

    assert actual_item is None


async def test_delete_raises_an_exception_when_item_does_not_exist():
    given_item_id = 100

    with raises(ValueError) as exc_info:
        await item_crud.delete(given_item_id)

    exc_msg = str(exc_info.value)
    assert f"Item {given_item_id} does not exist" in exc_msg
