


module "storage_account" {
  source = "./storageaccount"

  storage_account_name    = var.storage_account_name
  resource_group_name     = data.azurerm_resource_group.example.name
  resource_group_location = data.azurerm_resource_group.example.location
}


module "resource_group" {
  source = "./resourcegroup"
  resource_group_name     = var.resource_group_name
  resource_group_location = var.resource_group_location
  environment             = var.environment
}

