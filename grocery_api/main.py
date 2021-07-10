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

# PART 3 OF HOW-TO #3 CREATE A NEW ITEM: Import the pydantic schema we created
from grocery_api.schemas.item import Item
# For PART 4: Go back to the decorator / function for the path "POST /items"

# PART 3 OF EXERCISE #3 CREATE A NEW STORE: Import the pydantic schema we created
from grocery_api.schemas.store import Store
# For PART 4: Go back to the decorator / function for the path "POST /stores"

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

# HOW-TO #3: Implement an endpoint that CREATES AN ITEM
#
# PART 1: Defining the endpoint
#
# The appropriate HTTP method to use when _creating_ a new resource
# (in this case, creating a new item) is POST.
@app.post("/items")
# The data for the new item will be in the "request body". As explained in
# the slides, "request body" is where clients will put the data needed for the
# request. In this case, the data that's needed for creating a new item is the
# new item's properties like "name", "price", etc.
#
# To validate this incoming data, we will create a "pydantic schema."
# Go to grocery_api/schemas/item.py for "PART 2: Create the schema"
#
# PART 4: Use the schema to type-hint `item` and complete the function.
#
# FastAPI recognizes that the function parameter, `item` is referring to
# data in the "request body" because it is type-hinted as a "pydantic schema."
async def create_an_item(item: Item):
    # Call item_data.create(). Since the create() method is asking for a
    # dictionary, we use pydantic.BaseModel's built-in method dict() to
    # export the schema `item` into a regular python dictionary.
    new_item = await item_data.create(item.dict())
    return new_item
# Use the generated documentation to interact with our API,
# http://127.0.0.1:8000/docs > Click on "POST /items" > Click "Try it out" >
# Fill out the request body. E.g.,
#
# {
#   "name": "Bananas",
#   "price": 10,
#   "is_active": true
# }
#
# Press "Execute". "Server Response" should be "Code 200" and the
# "Response Body" is the new item created.


# EXERCISE #3: CREATE A STORE
# PART 1: Define the path and the path's function
@app.post("/stores")
# Go to grocery_api/schemas/store.py for "PART 2: Create the schema"
#
# PART 4: Use the schema to type-hint `store` and complete the function.
async def create_a_store(store: Store):
    new_store = await store_data.create(store.dict())
    return new_store
# Use the generated documentation to interact with our API,
# http://127.0.0.1:8000/docs > Click on POST /stores > Click "Try it out" >
# Fill out the request body. E.g.,
#
# {
#   "name": "My Company",
#   "founding_year": 1990,
#   "is_active": true
# }
#