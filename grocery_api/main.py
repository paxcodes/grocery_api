from fastapi import FastAPI

# These are the "helper modules" to retrieve data. We will use these
# inside our paths' functions.
#
# Example, to get all the store data:
#   stores = await store_data.read_all()
# To get a specific store given a store ID, store_id,
#   store = await store_data.read(store_id)
#
# `item_data` and `store_data` will have very similar functions so when you
# see me use one in `item_data` it is very likely a similar function exists
# in `store_data`.
#
# You can also think of these modules as our existing "backend" or
# "functionalities" which we will make accessible via the web using
# the API we will be creating with the FastAPI framework.
from grocery_api.data import item as item_data  # noqa
from grocery_api.data import store as store_data  # noqa
from grocery_api.data import user as user_data  # noqa


app = FastAPI()


@app.get("/")
async def get_home():
    return {"message": "Hello World!"}
