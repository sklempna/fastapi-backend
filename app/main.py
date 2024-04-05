from fastapi import FastAPI

from .cosmos import cosmos_test
from .auth import validate_token

app = FastAPI()


@app.get("/test")
async def test_endpoint(token):
    decoded = validate_token(token)
    return {"aud": decoded.get("aud")}


@app.get("/cosmostest")
async def cosmostest_endpoint():
    return {"answer": cosmos_test()}
