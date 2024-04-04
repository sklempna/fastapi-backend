from azure.cosmos import CosmosClient, PartitionKey, exceptions
import os


ACCOUNT_HOST = os.getenv("COSMOS_ACCOUNT_HOST")
MASTER_KEY = os.getenv("COSMOS_MASTER_KEY")
DATABASE_ID = os.getenv("COSMOS_DATABASE_ID")
CONTAINER_ID = os.getenv("COSMOS_CONTAINER_ID")


client = CosmosClient(ACCOUNT_HOST, credential=MASTER_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

query = "SELECT * FROM c"
items = list(container.query_items(query=query, enable_cross_partition_query=True))


def cosmos_test():
    return str(items)
