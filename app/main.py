from fastapi import FastAPI

from app.utils.cosmos import create_item, get_item_by_id, update_item_with_id
from app.utils.auth import validate_token
from app.models import Item


app = FastAPI()


@app.get("/health")
async def get_health():
    return {"status": "online"}


# @app.get("/test")
# async def test_endpoint(token):
#     decoded = validate_token(token)
#     return {"aud": decoded.get("aud")}


@app.get("/items/{item_id}", response_model=Item)
async def get_item_by_id_endpoint(item_id: str):
    response = get_item_by_id(item_id)
    return response


@app.post("/items/")
async def post_item_endpoint(item: Item):
    response = create_item(item)
    return response


@app.put("/items/{item_id}", response_model=Item)
async def put_item_endpoint(item_id: str, update_item: Item):
    response = update_item_with_id(item_id, update_item)
    return response
