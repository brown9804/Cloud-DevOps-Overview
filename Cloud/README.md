# Cloud Principles Overview

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

# Content:

<details>
<summary><b>Table of Contents</b> (click to open)</summary>
<!-- MarkdownTOC -->
  
- [0. API Currency Exchange Example](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/0-api_curr_exchange_eg)
- [1. Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform)
  - [Installing Terraform and Working with Terraform Providers](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab0)
  - [Using Terraform CLI Commands (workspace and state) to Manipulate a Terraform Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab1)
  - [Building and Testing a Basic Terraform Module](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab2)
  - [Exploring Terraform State Functionality](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab3)
  - [Deploy an Azure Storage Account with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab4)
  - [Deploy an Azure File Share and Blob Storage with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab5)
  - [Deploy Azure VNETs and Subnets with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab6)
  - [Create Azure NSGs with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab7)
  - [Deploying an Azure VM with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab8)
  - [Deploy a Web Application with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab9)
  - [Deploy a MySQL Database with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_10)
  - [Migrating Terraform State to Terraform Cloud](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_11)
  - [Using Terraform Provisioners to Set Up an Apache Web Server on AWS](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_12)
  - [Make Changes to AWS Infrastructure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_13)
  - [Use Output Variables to Query Data in AWS Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_14)
  - [Make Changes to Azure Infrastructure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_15)
  - [Use Output Variables to Query Data in Azure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_16)
  - [Use Terraform to Create a Kubernetes Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_17)
  - [Manage Kubernetes Resources with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_18)
  - [Use Terraform to Create an EKS Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_19)
  - [Troubleshooting a Terraform Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_20)
- [2. Linux](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux)
  - [Working with Users and Permissions](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab0)
  - [System Service Management, Runlevels and Boot Targets](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab1)
  - [Securely Accessing Your System](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab2)
  - [Package Management and Troubleshooting](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab3)
  - [File Management, Permissions and Backup](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab4)
  - [Working with Text Files and Streams](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab5)
  - [Linux Device Management](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab6)
  - [The Linux Shell](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab7)
  - [Networking](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab8)
  - [Processes Management](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab9)

<!-- /MarkdownTOC -->
</details>

# Wiki:
- [Terraform Environment Variables - export log files](https://www.terraform.io/cli/config/environment-variables)
- [Terraform - How to enable debug logging](https://www.suse.com/support/kb/doc/?id=000020022)
- [Terraform - Custom Condition Checks](https://www.terraform.io/language/expressions/custom-conditions#input-variable-validation)
- ['export' is not recognized as an internal or external command](https://stackoverflow.com/questions/26368306/export-is-not-recognized-as-an-internal-or-external-command)
- [Terraform - Add Disk Bursting for VM Scale Sets](https://github.com/hashicorp/terraform-provider-azurerm/issues/15392)
- [Terraform - Azure managed disks general information](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview), see disk types, and disk redundancy options as well. The structure related to the [azurerm_managed_disk](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/managed_disk), and you can find more references of which VM are able to enable this property [here](https://github.com/hashicorp/terraform-provider-azurerm/pull/14137)
- [GitHub - How to solve the Filename too long error when using `git clone` in windows](https://www.bswen.com/2021/12/how-to-solve-filename-too-long-error-when-using-git-clone-in-windows.html). Solution 2.2.2 might be us)eful, if not go to [How to Make Windows 10 Accept File Paths Over 260 Characters](https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/). And, if that does not fix this try using Git Bash, WSL, or the Command Prompt.
- [GitHub - Useful Git Configuration Items, like better compression](https://wildlyinaccurate.com/useful-git-configuration-items/)
- [GitHub - REST API Search](https://docs.github.com/en/rest/search#text-match-metadata)
- [Azure Bastion - What is?](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview)
- [PuTTY (a free SSH and Telnet client) Donwload](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- [SQL Server Management Studio (SSMS) – how to save results with headers](https://solutioncenter.apexsql.com/sql-server-management-studio-ssms-how-to-save-results-with-headers/)
- [SQL - Replacing one value with another](https://stackoverflow.com/questions/14212814/sql-replacing-one-value-with-another)
- [SQL - Difference between COMMIT and ROLLBACK](https://www.geeksforgeeks.org/difference-between-commit-and-rollback-in-sql/)
- [SQL - GROUP BY Statement](https://www.w3schools.com/sql/sql_groupby.asp)
- [SQL - join tables with group by and order by](https://www.w3resource.com/sql/joins/joining-with-group-by-and-order-by.php)
- [SQL - How to Find Records with NULL in a Column](https://learnsql.com/cookbook/how-to-find-records-with-null-in-a-column/)
- [SQL - Commenting and Uncommenting Code](https://zarez.net/?p=1581#:~:text=SQL%20Server%20Startup-,Commenting%20and%20Uncommenting%20Code%20in%20SQL%20Server%20Management%20Studio,by%20'CTRL%2BC'.)
- [SQL - Comparison Operators (Equal, Not Equal, Less than, Grater than)](https://www.tutlane.com/tutorial/sql-server/sql-comparison-operators)
- [SQL - Delete](https://www.w3schools.com/sql/sql_delete.asp)
- [SQL - INSERT INTO Syntax](https://www.w3schools.com/sql/sql_insert.asp)
- [SQL - Writing Loops](https://www.wiseowl.co.uk/blog/s348/loops-in-sql.htm)
- [SQL - Iterate Through Array Of Data In SQL Query](https://www.c-sharpcorner.com/article/iterate-through-array-of-data-in-sql-query/)
- [SQL - Getting the current system date and time](https://docs.microsoft.com/en-us/sql/t-sql/functions/getdate-transact-sql?view=sql-server-ver16)
- [SQL - Set Operators - EXCEPT and INTERSECT](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/set-operators-except-and-intersect-transact-sql?view=sql-server-ver16)
- [SQL - COUNT() function with distinct clause](https://www.w3resource.com/sql/aggregate-functions/count-with-distinct.php)
- [SQL - Server PRINT and SQL Server RAISERROR statements](https://www.sqlshack.com/sql-server-print-and-sql-server-raiserror-statements/)
- [SQL- COUNT rows with user defined column heading](https://www.w3resource.com/sql/aggregate-functions/count-function.php)
- [SQL - Select Top N or Top N Random Rows](https://www.kodyaz.com/articles/sql-select-top-query.aspx)
- [SQL - How to Join 3 Tables (or More)](https://learnsql.com/blog/how-to-join-3-tables-or-more-in-sql/)
- [SSMS - Database Diagram](https://www.mssqltips.com/sqlservertip/6269/sql-server-database-diagram-tool-in-management-studio/)
- [SSMS - Script objects](https://docs.microsoft.com/en-us/sql/ssms/tutorials/scripting-ssms?view=sql-server-ver16)
- [SSMS - How to Export Tables from a Database](https://documentation.alphasoftware.com/pages/HowTo/Databases/Export%20Tables%20from%20a%20Database.xml)
- [Nodejs - Install Windows](https://www.guru99.com/download-install-node-js.html)
- [Nodejs vs JavaScript](https://www.knowledgehut.com/blog/web-development/node-js-vs-javasript)
- [Python - Implementation HMAC-SHA1](https://gist.github.com/heskyji/5167567b64cb92a910a3), you can find more functions definitions [here](https://gist.github.com/binaryatrocity/7079332cab038da1394d) or [Cryptographic signature and verification of messages](http://pymotw.com/2/hmac/)
- [Python - encode()](https://stackoverflow.com/questions/2340319/python-3-1-1-string-to-hex)
- [Python - Asynchronous HTTP Requests](https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp), [example of post request](https://stackoverflow.com/questions/55250420/aiohttp-async-session-requests), [request Post with param data](https://stackoverflow.com/questions/15900338/python-request-post-with-param-data)


