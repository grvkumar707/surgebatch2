resource "azurerm_resource_group" "dev" {
  name     = var.resource_group_name
  location = var.resource_group_location
  tags = {
    environment = var.environment
  }
}