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
docker run -it -p 8000:8000 -e TENANT_ID=my-tenant-id -e CLIENT_ID=my-client_id -e CLIENT_CREDENTIALS=my-client-credential -e PORT=8000
        -e COSMOS_ACCOUNT_HOST=https://my-cosmosdb-account.documents.azure.com:443/
        -e COSMOS_MASTER_KEY=my-cosmos-master-key
        -e COSMOS_DATABASE_ID=my-cosmosdb-database
        -e COSMOS_CONTAINER_ID=my-cosmosdb-container
        backend
```

## Setting up the cloud environment

Necessary project infrastructure can be set-up on azure using the terraform project in the folder terraform.

Steps:

- log into the azure portal and open a cloud shell
- clone this repository `git clone https://github.com/sklempna/fastapi-backend`
- go into the terraform project `cd fastapi-backend/terraform`
- initialize terraform state `terraform init`
- run terraform `terraform apply`
