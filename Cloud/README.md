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
- [How to connect to Microsoft Azure Storage Explorer](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer?tabs=windows)
- [Terraform Environment Variables - export log files](https://www.terraform.io/cli/config/environment-variables)
- [How to enable debug logging when using Terraform](https://www.suse.com/support/kb/doc/?id=000020022)
- ['export' is not recognized as an internal or external command](https://stackoverflow.com/questions/26368306/export-is-not-recognized-as-an-internal-or-external-command)
- [List Azure role assignments using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal)
- [How to solve the Filename too long error when using `git clone` in windows](https://www.bswen.com/2021/12/how-to-solve-filename-too-long-error-when-using-git-clone-in-windows.html). Solution 2.2.2 might be useful, if not go to [How to Make Windows 10 Accept File Paths Over 260 Characters](https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/). And, if that does not fix this try using Git Bash, WSL, or the Command Prompt.
- [Useful Git Configuration Items, like better compression](https://wildlyinaccurate.com/useful-git-configuration-items/)
- [What is Azure Bastion?](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview)
- [SQL Server Management Studio (SSMS) – how to save results with headers](https://solutioncenter.apexsql.com/sql-server-management-studio-ssms-how-to-save-results-with-headers/)
- [SQL replacing one value with another](https://stackoverflow.com/questions/14212814/sql-replacing-one-value-with-another)
- [SQL - Difference between COMMIT and ROLLBACK](https://www.geeksforgeeks.org/difference-between-commit-and-rollback-in-sql/)
- [SQL - GROUP BY Statement](https://www.w3schools.com/sql/sql_groupby.asp)
- [SQL - join tables with group by and order by](https://www.w3resource.com/sql/joins/joining-with-group-by-and-order-by.php)

