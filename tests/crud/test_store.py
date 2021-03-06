from pytest import fixture, raises, mark

from grocery_api.data import store as store_crud

from .json_dir import TEST_JSON_DIR

pytestmark = mark.asyncio


def test_store_json_is_successfully_mocked():
    assert store_crud.JSON_FILE == TEST_JSON_DIR / "stores.json"


@fixture
async def created_store() -> dict:
    actual_new_store = await store_crud.create(
        dict(
            name="The Real Canadian Superstore",
            founding_year=1801,
            is_active=True,
            parent_company=None,
        )
    )
    yield actual_new_store
    await store_crud.delete(actual_new_store["id"])


async def test_it_can_create_store(created_store: dict):
    actual_new_store = await store_crud.read(created_store["id"])
    assert actual_new_store == dict(
        id=2,
        name="The Real Canadian Superstore",
        founding_year=1801,
        is_active=True,
        parent_company=None,
    )


async def test_it_can_read_all_stores():
    actual_stores = await store_crud.read_all()
    assert list(actual_stores.keys()) == [1]
    assert actual_stores[1] == {
        "id": 1,
        "name": "Sean, Pax, and Sans",
        "founding_year": 2018,
        "is_active": True,
        "parent_company": None,
    }


async def test_it_can_read_store_by_id():
    actual_store = await store_crud.read(1)
    expected_store = dict(
        id=1,
        name="Sean, Pax, and Sans",
        founding_year=2018,
        is_active=True,
        parent_company=None,
    )
    assert actual_store == expected_store


async def test_read_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.read(100)
    assert actual_store is None


@fixture
async def given_store() -> dict:
    store_id = 1
    original_store = await store_crud.read(store_id)
    assert original_store
    yield original_store
    await store_crud.update(
        store_id,
        dict(
            name=original_store["name"],
            founding_year=original_store["founding_year"],
            is_active=original_store["is_active"],
            parent_company=original_store["parent_company"],
        ),
    )


async def test_it_can_update_store(given_store: dict):
    given_new_data = dict(
        name="Sean, Pax, and Sons",
        founding_year=2021,
        is_active=True,
        parent_company=None,
    )

    await store_crud.update(given_store["id"], given_new_data)
    actual_store = await store_crud.read(given_store["id"])
    expected_store = dict(
        id=given_store["id"],
        name="Sean, Pax, and Sons",
        founding_year=2021,
        is_active=True,
        parent_company=None,
    )
    assert actual_store == expected_store


async def test_update_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.update(
        100,
        dict(
            name="Sean, Pax, and Sons",
            founding_year=2021,
            is_active=True,
            parent_company=None,
        ),
    )
    assert actual_store is None


async def test_it_can_update_store_parent_company(given_store: dict):
    given_new_company = "Lwaxana Dax"

    await store_crud.update_parent_company(given_store["id"], given_new_company)
    actual_store = await store_crud.read(given_store["id"])

    expected_store = given_store.copy()
    expected_store["parent_company"] = given_new_company
    assert actual_store == expected_store


async def test_update_parent_company_returns_none_when_store_does_not_exist():
    actual_store = await store_crud.update_parent_company(
        100,
        "Lwaxana Dax",
    )
    assert actual_store is None


@fixture
async def given_store_to_be_deleted() -> dict:
    store_id = 1
    original_store = await store_crud.read(store_id)
    assert original_store
    yield original_store
    await store_crud.create(
        dict(
            name=original_store["name"],
            founding_year=original_store["founding_year"],
            is_active=original_store["is_active"],
            parent_company=original_store["parent_company"],
        )
    )


async def test_it_can_delete_store_by_id(given_store_to_be_deleted: dict):
    await store_crud.delete(given_store_to_be_deleted["id"])
    actual_store = await store_crud.read(given_store_to_be_deleted["id"])
    assert actual_store is None


async def test_delete_raises_an_exception_when_store_does_not_exist():
    given_store_id = 100

    with raises(ValueError) as exc_info:
        await store_crud.delete(given_store_id)

    exc_msg = str(exc_info.value)
    assert f"Store {given_store_id} does not exist" in exc_msg
