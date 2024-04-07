from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os

service_endpoint = os.getenv("SEARCH_SERVICE_ENDPOINT")
index_name = os.getenv("SEARCH_INDEX_NAME")
key = os.getenv("SEARCH_API_KEY")

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

# Examples on how to use the python lib for azure ai search
#
# https://learn.microsoft.com/en-us/python/api/overview/azure/search-documents-readme?view=azure-python
