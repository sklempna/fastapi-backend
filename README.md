# fastapi-backend

## azure app config

In the manifest file of the app registration set
`"accessTokenAcceptedVersion": 2`
to make sure the frontend will get an oauth v2 token. Otherwise this will mess up signature validation.

## run in docker

build with

```bash
docker build -t backend .
```

run with

```bash
docker run -p 8000:8000 -e TENANT_ID=my-tenant-id -e CLIENT_ID=my-client_id -e CLIENT_CREDENTIALS=my-client-credential -e PORT=8000 backend
```
