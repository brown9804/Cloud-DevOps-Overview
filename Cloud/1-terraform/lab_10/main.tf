# Deploy a MySQL Database with Terraform
## Deploy a MySQL Database Instance

provider "azurerm" {
    version = 1.38
    }

resource "azurerm_mysql_server" "example" {
  name                = "tflab-mysqlserver-1-[some unique characters]"
  location            = "The location of your lab provided resource group"
  resource_group_name = "Enter Resource Group Name"

  sku {
    name     = "B_Gen5_2"
    capacity = 2
    tier     = "Basic"
    family   = "Gen5"
  }

  storage_profile {
    storage_mb            = 5120
    backup_retention_days = 7
    geo_redundant_backup  = "Disabled"
  }

  administrator_login          = "mysqladminun"
  administrator_login_password = "easytologin4once!"
  version                      = "5.7"
  ssl_enforcement              = "Enabled"
}

resource "azurerm_mysql_database" "example" {
  name                = "exampledb"
  resource_group_name = "Enter Resource Group Name"
  server_name         = azurerm_mysql_server.example.name
  charset             = "utf8"
  collation           = "utf8_unicode_ci"
}