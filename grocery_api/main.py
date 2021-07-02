from fastapi import FastAPI

from grocery_api.data import item as item_data  # noqa
from grocery_api.data import store as store_data  # noqa
from grocery_api.data import user as user_data  # noqa


app = FastAPI()


@app.get("/")
async def get_home():
    return {"message": "Hello World!"}
