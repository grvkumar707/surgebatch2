output "resource_group_name" {
  value = data.azurerm_resource_group.example.name
}

output "resource_group_location" {
  value = data.azurerm_resource_group.example.location
}

# output "storage_account_name" {
#   value = module.storage_account.storage_account_name
# }
# output "storage_account_id" {
#   value = module.storage_account.storage_account_id
# }