variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "resource_group_location" {
  description = "The location of the resource group"
  type        = string
}

variable "cosmosdb_account_name" {
  description = "The name of the Cosmos DB account"
  type        = string
}

variable "cosmosdb_database_name" {
  description = "The name of the Cosmos DB database"
  type        = string
}

variable "cosmosdb_container_name" {
  description = "The name of the Cosmos DB container"
  type        = string
}