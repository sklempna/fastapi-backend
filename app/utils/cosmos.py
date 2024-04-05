from azure.cosmos import CosmosClient, PartitionKey, exceptions
from pydantic import BaseModel
from fastapi import HTTPException
import os

from app.models import Item


ACCOUNT_HOST = os.getenv("COSMOS_ACCOUNT_HOST")
MASTER_KEY = os.getenv("COSMOS_MASTER_KEY")
DATABASE_ID = os.getenv("COSMOS_DATABASE_ID")
CONTAINER_ID = os.getenv("COSMOS_CONTAINER_ID")


client = CosmosClient(ACCOUNT_HOST, credential=MASTER_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)


def get_item_by_id(item_id: str):
    try:
        # Query the item in the Cosmos DB container by id
        items = list(
            container.query_items(
                query="SELECT * FROM c WHERE c.id = @item_id",
                parameters=[{"name": "@item_id", "value": item_id}],
                enable_cross_partition_query=True,
            )
        )
        if items:
            # Return the first item found
            return items[0]
        else:
            # If no items are found, return a 404 error
            raise HTTPException(status_code=404, detail="Item not found")
    except exceptions.CosmosHttpResponseError as e:
        # If an error occurs with Cosmos DB, return an HTTP exception
        raise HTTPException(status_code=e.status_code, detail=str(e))


def create_item(item: Item):
    try:
        # Try to create the document in Cosmos DB
        response = container.create_item(body=item.model_dump())
        return response
    except exceptions.CosmosHttpResponseError as e:
        # If an error occurs, return an HTTP exception with the error message
        raise HTTPException(status_code=e.status_code, detail=str(e))
