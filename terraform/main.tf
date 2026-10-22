

resource "azurerm_resource_group" "dev" {
  name     = var.resource_group_name
  location = var.resource_group_location
  tags = {
    environment = var.environment
  }
}

resource "azurerm_storage_account" "dev" { 
    name =  var.storage_account_name
    resource_group_name = azurerm_resource_group.dev.name
    location            = azurerm_resource_group.dev.location
    account_tier        = "Standard"
    account_replication_type = "LRS"
}
