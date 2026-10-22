provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "dev" {
  count = 2
  name     = "bhalla${count.index == 0 ? "dev" : "uat"}"
  location = "East US"
  tags = {
    environment = "${count.index == 0 ? "dev" : "uat"}"
  }
}

