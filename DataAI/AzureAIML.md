# Azure Artifitial Intelligence + ML Overview

----------

Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Aug, 2022

----------

## Content 
- [AI Search](#ai-search)
  

## Wiki 

All Azure services as for now:

| Area | Category | Service | Overview |
| ---- | ---- | ---- | ---- | 
| Artifitial Intelligence | Platform | Azure AI Studio | TBD |
| Machine Learning | Platform | Azure Machine Learning | TBD |
| AI + APIs | Service | [AI Search](#ai-search) (formerly known as "Azure Cognitive Search") | Azure AI Search, a powerful information retrieval platform by Microsoft, enables developers to create rich search experiences and generative AI applications. For more information click [here](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | 
| AI + APIs | Service | AI Services | TBD | 
| AI + APIs | Service | AI Services multi-service account | TBD | 
| AI + APIs | Service | AI Video Indexer | TBD | 
| AI + APIs | Service | Anomaly detectors | TBD | 
| AI + APIs | Service | Bot Services | TBD | 
| AI + APIs | Service | Computer Vision | TBD | 
| AI + APIs | Service | Custom Vision | TBD | 
| AI + APIs | Service | Content moderators | TBD | 
| AI + APIs | Service | Document intelligences | TBD | 
| AI + APIs | Service | Face APIs | TBD | 
| AI + APIs | Service | Immersive readers | TBD | 
| AI + APIs | Service | Language | TBD | 
| AI + APIs | Service | Metrics Advisors | TBD | 
| AI + APIs | Service |  | TBD | 

## AI Search 

> Built-in indexers are available for `Azure Cosmos DB, Azure SQL Database, Azure Blob Storage, and Microsoft SQL Server hosted in Azure Virtual Machines`. Use Azure `Data Factory`, with more than 80 connectors, or `Azure Logic Apps` to connect to your data source. Alternatively, push data into an Azure AI Search index, which has no restrictions on data source type.

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/bdaebc61-162f-4c0f-855f-6dc74de38397)

### Use Cases for Azure AI Search

1. **E-commerce and Retail**:
   - Enhance product search experiences on e-commerce websites by providing relevant results, filters, and facets.
   - Implement personalized recommendations based on user behavior and preferences.
   - Enable faceted navigation for efficient product discovery.

> [!NOTE]
> Azure AI Search is an AI-powered information retrieval platform that helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data. It can implement search functionality for any mobile or search application within your organization or as part of software as a service (SaaS) apps. 

> Here's a general architecture of how Azure AI Search can be used in an e-commerce solution:

> 1. **Customers** go to the e-commerce web application from any device.
> 2. The **product catalog** is maintained in an **Azure SQL database** for transactional processing.
> 3. **Azure AI Search** uses a search indexer to automatically keep its search index up to date through integrated change tracking.
> 4. Customer's search queries are offloaded to the AI Search service, which processes the query and returns the most relevant results.
> 5. As an alternative to a web-based search experience, customers can also use a conversational bot in social media or straight from digital assistants to search for products and incrementally refine their search query and results.
> 6. Optionally, customers can use the skillset feature to apply artificial intelligence for even smarter processing.

> Key Azure services involved in this architecture include:

> - **Azure App Service - Web Apps**: Hosts web applications allowing autoscale and high availability without having to manage infrastructure.
> - **Azure SQL Database**: A general-purpose relational database-managed service in Microsoft Azure that supports structures such as relational data, JSON, spatial, and XML.
> - **Azure AI Search**: A cloud solution that provides a rich search experience over private, heterogeneous content in web, mobile, and enterprise applications.
> - **Azure AI Bot Service**: Provides tools to build, test, deploy, and manage intelligent bots.
> - **Azure AI services**: Lets you use intelligent algorithms to see, hear, speak, understand, and interpret your user needs through natural methods of communication.



2. **Content and Document Management**:
   - Index and search through large document repositories, intranets, and knowledge bases.
   - Implement full-text search, highlighting, and document previews.
   - Facilitate content discovery and retrieval for employees and customers.

3. **Enterprise Search**:
   - Create a unified search experience across various enterprise data sources (files, databases, APIs).
   - Enable users to find information quickly within their organization.
   - Support natural language queries and relevance tuning.

4. **Healthcare and Life Sciences**:
   - Build medical knowledge bases for clinicians and researchers.
   - Enable semantic search for medical literature, clinical trials, and patient records.
   - Facilitate drug discovery and research.

5. **Media and Entertainment**:
   - Enhance video and audio content discovery by indexing metadata and transcripts.
   - Implement search for news articles, blogs, podcasts, and multimedia content.
   - Enable personalized recommendations for movies, music, and TV shows.

6. **Travel and Hospitality**:
   - Power hotel booking platforms with efficient search capabilities.
   - Enable location-based search for restaurants, attractions, and events.
   - Implement geospatial search for travel planning.

7. **Financial Services**:
   - Create powerful search interfaces for financial data, stock market information, and investment research.
   - Enable users to find relevant financial documents, reports, and news articles.
   - Implement secure search for sensitive data.

