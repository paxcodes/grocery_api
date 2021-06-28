from pytest import fixture, raises, mark

from grocery_api.data.crud import store as store_crud

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_store_json_is_successfully_mocked():
    assert store_crud.JSON_FILE == TEST_JSON_DIR / "stores.json"


@fixture
async def created_store() -> store_crud.StoreOutDict:
    given_new_store_data = {
        "name": "The Real Canadian Superstore",
        "founding_year": 1801,
        "is_active": True,
        "parent_company": None
    }
    actual_new_store = await store_crud.create(
        given_new_store_data
    )
    yield actual_new_store
    await store_crud.delete(actual_new_store.id)


async def test_it_can_create_store(created_store: store_crud.StoreOutDict):
    actual_new_store = await store_crud.read(created_store.id)
    assert actual_new_store == store_crud.StoreOutDict(
        **{
            "id": 2,
            "name": "The Real Canadian Superstore",
            "founding_year": 1801,
            "is_active": True,
            "parent_company": None,
        }
    )


async def test_it_can_read_store_by_id():
    actual_store = await store_crud.read(1)
    expected_store = store_crud.StoreOutDict(
        **{
            "id": 1,
            "name": "Sean, Pax, and Sons",
            "founding_year": 2018,
            "is_active": True,
            "parent_company": None,
        }
    )
    assert actual_store == expected_store


async def test_read_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.read(100)
    assert actual_store is None


@fixture
async def given_store() -> store_crud.StoreOutDict:
    store_id = 1
    original_store = await store_crud.read(store_id)
    assert original_store
    yield original_store
    await store_crud.update(store_id, original_store)


async def test_it_can_update_store(given_store: store_crud.StoreOutDict):
    given_new_data = {
        "name": "Sean, Pax, and Sons",
        "founding_year": 2021,
        "is_active": True,
        "parent_company": str
    }

    await store_crud.update(given_store.id, given_new_data)
    actual_store = await store_crud.read(given_store.id)
    expected_store = store_crud.StoreOutDict(
        **{
            "id": given_store.id,
            "name": "Sean, Pax, and Sons",
            "founding_year": 2021,
            "is_active": True,
            "parent_company": None,
        }
    )
    assert actual_store == expected_store


async def test_update_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.update(
        100,
        {
            "name": "Sean, Pax, and Sons",
            "price": 2021,
            "is_active": True,
            "parent_company": None
        },
    )
    assert actual_store is None


async def test_it_can_update_store_parent_company(given_store: store_crud.StoreOutDict):
    given_new_company = "Lwaxana Dax"

    await store_crud.update_parent_company(given_store.id, given_new_company)
    actual_store = await store_crud.read(given_store.id)

    expected_store = given_store.copy(update={"parent_company": given_new_company})
    assert actual_store == expected_store


async def test_update_parent_company_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.update_parent_company(
        100,
        "Lwaxana Dax",
    )
    assert actual_store is None


async def test_it_can_delete_store_by_id(given_store: store_crud.StoreOutDict):
    await store_crud.delete(given_store.id)
    actual_store = await store_crud.read(given_store.id)

    assert actual_store is None


async def test_delete_raises_an_exception_when_store_does_not_exist():
    given_store_id = 100

    with raises(ValueError) as exc_info:
        await store_crud.delete(given_store_id)
        exc_msg = str(exc_info.value)

    assert f"Store {given_store_id} does not exist" in exc_msg
