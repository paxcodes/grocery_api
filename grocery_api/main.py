from fastapi import FastAPI

from grocery_api.data.crud import item as item_data     # noqa
from grocery_api.data.crud import store as store_data   # noqa
from grocery_api.data.crud import user as user_data     # noqa


app = FastAPI()


@app.get("/")
async def get_home():
    return {"message": "Hello World!"}
