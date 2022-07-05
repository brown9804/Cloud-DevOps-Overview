# Deploy a Web Application

provider "azurerm" {
    version = 1.38
    }

resource "azurerm_app_service_plan" "svcplan" {
  name                = "Enter App Service Plan name"
  location            = "eastus"
  resource_group_name = "Enter Resource Group Name"

  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "appsvc" {
  name                = "Enter Web App Service Name"
  location            = "eastus"
  resource_group_name = "Enter Resource Group Name"
  app_service_plan_id = azurerm_app_service_plan.svcplan.id


  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
  }
}