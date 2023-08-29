# Azure Artifacts Overview

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

# Wiki:
- [Azure Portal - List Azure role assignments](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal)
- [App Service Plan - Introduction](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans)
- [Logic Apps - Stateful vs Stateless](https://martink.me/articles/what-is-new-in-logic-apps-v2)
- [Logic Apps - Monitor run status, review trigger history, and set up alerts](https://learn.microsoft.com/en-us/azure/logic-apps/monitor-logic-apps?tabs=consumption)
- [Logic Apps - Create a Standard logic app workflow in single-tenant Azure Logic Apps using Visual Studio Code](https://learn.microsoft.com/en-us/azure/logic-apps/create-single-tenant-workflows-visual-studio-code#set-up-visual-studio-code)
- [Postman - How to Install and use for API Testing](https://www.guru99.com/postman-tutorial.html)
- [AZ Monitor - Monitor availability with URL ping tests](https://docs.microsoft.com/en-us/azure/azure-monitor/app/monitor-web-app-availability)
- [AZ Monitor - Query Application Insights Telemetry Data using REST API](https://dailydotnettips.com/query-application-insights-telemetry-data-using-rest-api/)
- [AZ Monitor -  Failures and Triggering an Alert from Application Insights](https://pmichaels.net/2022/04/23/azure-monitor-failures-and-triggering-an-alert-from-application-insights/), for MS guide [click here](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-new-alert-rule?tabs=metric)
- [Storage Account - What is Azure Table storage?](https://docs.microsoft.com/en-us/azure/storage/tables/table-storage-overview)
- [Storage Account - Understanding the Table service data model](https://docs.microsoft.com/en-us/rest/api/storageservices/Understanding-the-Table-Service-Data-Model)
- [Storage Account - Create a queue and add a message with the Azure portal](https://learn.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-portal)
- [Storage Account - Samples using v12 Python client libraries](https://learn.microsoft.com/en-us/azure/storage/common/storage-samples-python)
- [Storage Account - Azure Blob Storage client library for Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=connection-string%2Croles-azure-portal%2Csign-in-azure-cli), to understand [how to download specific file under specific path](https://www.educative.io/answers/how-to-download-files-from-azure-blob-storage-using-python). For ["StorageStreamDownloader Class" methods](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.storagestreamdownloader?view=azure-python). How to [read csv from Azure blob Storage and store in a DataFrame](https://stackoverflow.com/questions/62670991/read-csv-from-azure-blob-storage-and-store-in-a-dataframe). The best way to [overwrite Azure Blob in Python](https://stackoverflow.com/questions/61130890/best-way-to-overwrite-azure-blob-in-python)
- [Microsoft Azure Storage Explorer - How to connect](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer?tabs=windows)
- [Microsoft Azure Storage Explorer - Not recognizing PartitionKey in CSV file](https://learn.microsoft.com/en-us/answers/questions/906432/azure-storage-explorer-not-recognizing-partitionke.html)
- [Microsoft Azure Storage Explorer - Browse and manage storage resources](https://learn.microsoft.com/en-us/visualstudio/azure/vs-azure-tools-storage-resources-server-explorer-browse-manage?view=vs-2022)
- [Function Apps - Introduction](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)
- [Function Apps - Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?tabs=in-process&pivots=programming-language-python)
- [Function Apps - Local workspace setup within Vscode](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python), [Azure Functions Core Tools is need](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cmacos%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools), but if vscode automatic instalation fails go [here](https://github.com/Azure/azure-functions-core-tools#installing) to find more information. It's important to consider taht you can open vscode from terminal/command line, go [here](https://stackoverflow.com/questions/30065227/run-open-vscode-from-mac-terminal) to find more. Also, it's better to have [installed Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). If you don't want to use Vscode you can also [create it in Azure Portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal). If error value cannot be null. (Parameter 'provider'), click [here](https://github.com/Azure/azure-functions-core-tools/issues/2232) to understand how to fix it. Downloading and [installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally) to setup the requirements, and any functionality required for the implementation. Configure local.settings.`<extension>` see [how to read local.settings.json configuration in index.js file](https://stackoverflow.com/questions/71127337/how-to-read-local-settings-json-configuration-in-index-js-file) for more perspective on how to do it. Example [Fapps to Storage Account](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?tabs=in-process&pivots=programming-language-python)
- [Function Apps - V2 Python Programming Model](https://techcommunity.microsoft.com/t5/azure-compute-blog/azure-functions-v2-python-programming-model/ba-p/3665168)
- [Function Apps - Running Python Locally on an M1](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python#x86-emulation-on-arm64), if cannot edit default VSCode JSON settings click [here](https://stackoverflow.com/questions/63211082/cannot-edit-default-vscode-json-settings). If error [Microsoft.Azure.WebJobs.Script: Architecture Arm64 is not supported for language python](https://github.com/Azure/azure-functions-python-worker/issues/915#issuecomment-1342319719) try this, and check comments below that one.
- [Function Apps/KeyVault - How to create a secure connection](https://levelup.gitconnected.com/a-secure-way-to-use-credentials-and-secrets-in-azure-functions-7ec91813c807)
- [Function Apps/KeyVault - Troubleshooting Azure Key Vault References in Azure Function Apps](https://medium.com/geekculture/troubleshooting-azure-key-vault-references-in-azure-function-apps-b228c1216f63#:~:text=AccessToKeyVaultDenied%20error%20signifies%20that%20your,Vault's%20firewall%20(under%20Networking).)
- [Function Apps - How to query Azure SQL DB](https://www.sqlshack.com/python-serverless-functions-to-query-azure-sql-db/)
- [Function Apps - how to use SQL update query in azure functions SQL output binding in python](https://stackoverflow.com/questions/76637547/how-to-use-sql-update-query-in-azure-functions-sql-output-binding-in-python), and understand how [commit()](https://www.tutorialspoint.com/what-is-python-commit-method-in-mysql) method works. How to [add df into sql](https://www.dataquest.io/blog/sql-insert-tutorial/)
- [Data Factory - Creating a pipeline with UI](https://learn.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?tabs=data-factory#creating-a-pipeline-with-ui)
- [Data Factory - Need to Copy existing data factory pipelines to new data factory in new resource group](https://learn.microsoft.com/en-us/answers/questions/166820/need-to-copy-existing-data-factory-pipelines-to-ne)
- [Data Factory - How to create and configure Azure Integration Runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-azure-integration-runtime?tabs=data-factory#create-an-azure-ir-via-ui)
- [Data Factory - How to get output parameter from Executed Pipeline in ADF](https://stackoverflow.com/questions/68252383/how-to-get-output-parameter-from-executed-pipeline-in-adf)
- [Data Factory - Roles and permissions for Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/concepts-roles-permissions)
- [Data Factory - Assign a Key Vault access policy (legacy)](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal)
- [Data Factory - How to configure integrationRuntime (also for testing)](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime?tabs=data-factory#create-a-self-hosted-ir-via-ui)
- [Data Factory - Fix DataTypeNotSupported](https://learn.microsoft.com/en-us/azure/data-factory/connector-troubleshoot-synapse-sql#error-code-sqlfailedtoconnect) try to activate runtime, and import schema on sink data for more details click [here](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-schema-and-type-mapping#tabular-source-to-tabular-sink)
- [Data Factory - Managed Private EndPoints](https://blog.baeke.info/2021/06/24/approving-a-private-endpoint-connection-with-azure-cli/)
- [SQL Server/Databases - Configure IP firewall rules](https://www.sqlshack.com/configure-ip-firewall-rules-for-azure-sql-databases/)
- [Data Lake - How To Create it In Azure](https://blog.openbridge.com/how-to-create-data-lake-in-azure-5bce1604c4c8)

