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


# HOW-TO #1: Implement an endpoint or path that gets all items
#
# We use python's decorator syntax `@`, then the FastAPI instance `app`
# then the method `get` (since this path is for RETRIEVING / GETTING a resource,
# the HTTP method GET is what's appropriate to use),
# then specifying the path we are implementing, "/items"
@app.get("/items")
# Immediately below the decorator is the function that will have
# the logic we want to execute when users (clients) of our API makes
# a request to the path we just defined through the decorator (in this case,
# a GET request to the /items path).
async def get_all_items():
    # Call the read_all() function of our `item_data` module (part of our
    # existing backend). For more info about these modules, see comment on
    # the top section of this file.
    items = await item_data.read_all()
    # We return all the items.
    return items

# Exercise #1: Implement an endpoint or path that gets all stores
@app.get("/stores")
async def get_all_stores():
    stores = await store_data.read_all()
    return stores


# HOW-TO #2: Implement an endpoint or path that gets a specific item
# given an item ID.
#
# Specify "path parameters" (in this case, item_id) using curly braces.
@app.get("/items/{item_id}")
# For a function parameter to be recognized by FastAPI as the path parameter
# we specified in our decorator, it should have the same name. In this case,
# item_id. We also type-hinted it to be an integer.
async def get_item_by_item_id(item_id: int):
    # Call the read() method of our `item_data` module.
    item = await item_data.read(item_id)
    return item
# In your browser, try visiting this path with a string for "item_id"
# (e.g. `http://127.0.0.1:8000/items/foo`) and you'll see that FastAPI
# returns a handy error message out-of-the-box.
#
# Let's also use the generated documentation to interact with our API,
# http://127.0.0.1:8000/docs > Click on the path > Click "Try it out" >
# Specify the Item ID using the form provided.


# Exercise #2: Implement an endpoint or path that gets a specific store
# given a store ID.
@app.get("/stores/{store_id}")
async def get_store_by_store_id(store_id: int):
    store = await store_data.read(store_id)
    return store
