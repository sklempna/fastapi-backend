from fastapi import FastAPI, HTTPException, status

from jose import jwt
import httpx
import os

# from fastapi.security import OAuth2Bearer
from msal import ConfidentialClientApplication

app = FastAPI()

# Your Azure app registration details
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_CREDENTIALS = os.getenv("CLIENT_CREDENTIALS")
AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
ISSUER = f"{AUTHORITY_URL}/v2.0"
OPENID_CONFIG_URL = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0/.well-known/openid-configuration"

# MSAL confidential client application
client_app = ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY_URL, client_credential=CLIENT_CREDENTIALS
)


# Dependency to validate access token and extract claims
async def get_current_user(token):
    result = client_app.acquire_token_by_authorization_code(token, scopes=[])
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result.get("id_token_claims")


# Verify and decode the JWT token using the keys
def validate_token(token: str):
    try:
        # Options to validate the claims
        options = {
            "verify_signature": True,
            "verify_aud": True,
            "verify_iat": True,
            "verify_exp": True,
            "verify_nbf": True,
            "verify_iss": True,
            "verify_sub": True,
            "verify_jti": True,
            "verify_at_hash": True,
            "leeway": 0,
        }
        with httpx.Client() as client:
            jwks_uri = client.get(OPENID_CONFIG_URL).json().get("jwks_uri")
            jwks = client.get(jwks_uri).json()["keys"]
        # Decode and validate the token
        decoded_token = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            audience=CLIENT_ID,
            issuer=ISSUER,
            options=options,
        )
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/test")
async def test_endpoint(token):
    decoded = validate_token(token)
    return {"aud": decoded.get("aud")}
