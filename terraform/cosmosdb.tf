resource "azurerm_cosmosdb_account" "cdba" {
  name                = var.cosmosdb_account_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB" # This is required for SQL API

  enable_automatic_failover = false

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_sql_database" "cdbdb" {
  name                = var.cosmosdb_database_name
  resource_group_name = azurerm_resource_group.example.name
  account_name        = azurerm_cosmosdb_account.example.name
  throughput          = 400 # Minimum throughput for SQL API
}

resource "azurerm_cosmosdb_sql_container" "cdbcont" {
  name                = var.cosmosdb_container_name
  resource_group_name = azurerm_resource_group.example.name
  account_name        = azurerm_cosmosdb_account.example.name
  database_name       = azurerm_cosmosdb_sql_database.example.name
  partition_key_path  = "/examplePartitionKey"

  throughput          = 400 # Minimum throughput for SQL API
}