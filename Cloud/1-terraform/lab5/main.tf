provider "azurerm" {
    version = 1.38
    }
    
resource "azurerm_storage_account" "lab" {
  name                     = "unique storage account name"
  resource_group_name      = "Enter Resource Group Name"
  location                 = "[Use the same location as your lab provided resource group]"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "lab" {
  name                  = "blobcontainer4lab"
  storage_account_name  = azurerm_storage_account.lab.name
  container_access_type = "private"
}

resource "azurerm_storage_blob" "lab" {
  name                   = "TerraformBlob"
  storage_account_name   = azurerm_storage_account.lab.name
  storage_container_name = azurerm_storage_container.lab.name
  type                   = "Block"
}
resource "azurerm_storage_share" "lab" {
  name                 = "terraformshare"  
  storage_account_name = azurerm_storage_account.lab.name
  quota                = 50
}