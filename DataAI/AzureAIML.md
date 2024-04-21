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
| AI + APIs | Service | AI Services | Azure AI services are a collection of cloud-based services provided by Microsoft Azure to help developers build applications with artificial intelligence capabilities. <br/> <br/> Here’s an overview: <br/> 1. **Azure Machine Learning**: A cloud-based environment you can use to train, deploy, automate, manage, and track ML models. <br/> 2. **Azure Cognitive Services**: A collection of APIs, SDKs, and services available to help developers build intelligent applications without having direct AI or data science skills or knowledge. It includes services for vision, speech, language, decision, and web search. <br/> 3. **Azure Bot Service**: Enables developers to create conversational interfaces on multiple channels. <br/> 4. **Azure Databricks**: An Apache Spark-based analytics platform optimized for Azure. It's integrated with Azure to provide one-click setup, streamlined workflows, and an interactive workspace. <br/> 5. **Azure Search**: A search-as-a-service cloud solution that gives developers APIs and tools for adding a rich search experience over private, heterogeneous content in web, mobile, and enterprise applications. <br/> 6. **Azure Data Lake Analytics**: An on-demand analytics job service that simplifies big data. Instead of deploying, configuring, and tuning hardware, you write queries to transform your data and extract valuable insights. <br/> <br/> These services are designed to work together to help developers and data scientists build end-to-end AI applications. They can be used individually or in combination, depending on the specific application requirements. They are all built on the robust Azure cloud platform, ensuring scalability, reliability, and security. <br/> <br/> Remember, the use of these services requires an Azure subscription. If you don't have one, you can create a free account to get started. <br/> To see the list of Available Azure AI services, click [here](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#available-azure-ai-services) | 
| AI + APIs | Service | AI Services multi-service account | 1. **AI Services** offer prebuilt and customizable APIs and models for creating intelligent applications. [reference](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services) <br/> 2. A **multi-service account** allows access to multiple Azure AI services with a single key and endpoint, consolidating billing. [reference](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?tabs=windows&pivots=azportal) and [here](https://stackoverflow.com/questions/77407269/how-to-create-azure-ai-services-multi-service-account-using-terraform) <br/> 3. In contrast, a **single-service account** provides access to a specific AI service with a unique key and endpoint. [refenrece](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/ai-services/multi-service-resource.md) | 
| AI + APIs | AI Service | Anomaly detectors $${\color{red}Retired}$$ | Azure Anomaly Detector was an AI service provided by Microsoft Azure. It offered a set of APIs that allowed users to monitor and detect anomalies in their time series data with little machine learning (ML) knowledge. This could be done either through batch validation or real-time inference. For reference click [here](https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview) | 
| AI + APIs | AI Service | Content moderators $${\color{red}Retired}$$ | Azure Content Moderator was an AI service provided by Microsoft Azure. It was designed to handle content that could be potentially offensive, risky, or otherwise undesirable. The service included AI-powered content moderation which scanned text, images, and videos, and automatically applied content flags. However, Azure Content Moderator was deprecated in February 2024 and was retired by February 2027. It was replaced by Azure AI Content Safety, which offered advanced AI features and enhanced performance. Click [here](https://learn.microsoft.com/en-us/azure/ai-services/content-moderator/overview) for reference. | 
| AI + APIs | AI Service | Language  $${\color{red}Retired}$$ | Azure AI Language was a cloud-based service provided by Microsoft Azure. It offered Natural Language Processing (NLP) features for understanding and analyzing text. This service was used to build intelligent applications using the web-based Language Studio, REST APIs, and client libraries. <br/>  <br/> The Azure AI Language service unified the following previously available Azure AI services: Text Analytics, QnA Maker, and LUIS. It also provided several new features. <br/> <br/> Here are some of the key features of the Azure AI Language service: <br/> 1. **Named Entity Recognition (NER)**: This preconfigured feature categorized entities (words or phrases) in unstructured text across several predefined category groups. <br/> 2. **Personally Identifying (PII) and Health (PHI) Information Detection**: This preconfigured feature identified, categorized, and redacted sensitive information in both unstructured text documents, and conversation transcripts. <br/> 3. **Language Detection**: This preconfigured feature detected the language a document was written in, and returned a language code for a wide range of languages, variants, dialects, and some regional/cultural languages. <br/> 4. **Sentiment Analysis and Opinion Mining**: These preconfigured features helped find out what people think of a brand or topic by mining text for clues about positive or negative sentiment, and could associate them with specific aspects of the text. <br/> 5. **Summarization**: This preconfigured feature used extractive text summarization to produce a summary of documents and conversation transcriptions. <br/> <br/> However, please note that as of July 2023, Azure AI services encompassed all of what were previously known as Cognitive Services and Azure Applied AI Services. Click [here](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview) for reference, and [2](https://language.cognitive.azure.com/), [3](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview), [4](https://azure.microsoft.com/en-us/products/ai-services/ai-language) | 
| AI + APIs | AI Service | Metrics Advisors  $${\color{red}Retired}$$ | Azure AI Metrics Advisor was a part of Azure AI services that used AI to perform data monitoring and anomaly detection in time series data. The service automated the process of applying models to your data, and provided a set of APIs and a web-based workspace for data ingestion, anomaly detection, and diagnostics. Developers could build AIOps, predictive maintenance, and business monitor applications on top of the service. <br/> <br/> Here are some of the key features of the Azure AI Metrics Advisor service: <br/> 1. **Connect to a variety of data sources**: Metrics Advisor could connect to, and ingest multi-dimensional metric data from many data stores, including SQL Server, Azure Blob Storage, MongoDB and more. <br/> 2. **Easy-to-use and customizable anomaly detection**: Metrics Advisor automatically selected the best model for your data, without needing to know any machine learning. It could automatically monitor every time series within multi-dimensional metrics. Users could use parameter tuning and interactive feedback to customize the model applied on their data, and future anomaly detection results. <br/> 3. **Real-time notification through multiple channels**: Whenever anomalies were detected, Metrics Advisor was able to send real time notification through multiple channels using hooks, such as email hooks, web hooks, Teams hooks and Azure DevOps hooks. Flexible alert configuration let users customize when and where to send a notification. <br/> 4. **Smart diagnostic insights by analyzing anomalies**: Metrics Advisor combined anomalies detected on the same multi-dimensional metric into a diagnostic tree to help users analyze root cause into specific dimension. <br/> <br/> However, please note that starting from the 20th of September, 2023, creation of new Metrics Advisor resources was discontinued, and the Metrics Advisor service was retired on the 1st of October, 2026. Click [here](https://learn.microsoft.com/en-us/azure/ai-services/metrics-advisor/overview) | 
| AI + APIs | AI Service | Personalizers  $${\color{red}Retired}$$ | Azure AI Personalizer was an AI service provided by Microsoft Azure. It used reinforcement learning to help applications make smarter decisions at scale. Personalizer processed information about the state of your application, scenario, and/or users (contexts), and a set of possible decisions and related attributes (actions) to determine the best decision to make. <br/> <br/> Here are some of the key features of the Azure AI Personalizer service: <br/> - Real-time Learning: Personalizer could improve over time based on user behavior, and discover what maximizes results to stay on top of changing trends. <br/> - Quick Integration: Personalizer could be embedded by adding two lines of code. It worked with your data in any form. <br/> - Apprentice Mode: When turned on, Personalizer learned alongside your existing solution without being exposed to users until it met your performance threshold. <br/> - Evaluation: Users could interpret and evaluate Personalizer through the interface. <br/> <br/> However, please note that starting from the 0th of September, 03, creation of new Personalizer resources was discontinued, and the Personalizer service was retired on the st of October, 06.  Click [here](https://learn.microsoft.com/en-us/azure/ai-services/personalizer/what-is-personalizer) for reference. | 
| AI + APIs | AI Service | [AI Search](#ai-search) (formerly known as "Azure AI Search") | Azure AI Search, a powerful information retrieval platform by Microsoft, enables developers to create rich search experiences and generative AI applications. For more information click [here](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | 
| AI + APIs | AI Service | AI Video Indexer | Azure AI Video Indexer is a cloud and edge video analytics service that uses artificial intelligence to extract actionable insights from stored videos, for more information click [here](https://azure.microsoft.com/en-us/products/ai-video-indexer/)| 
| AI + APIs | AI Service | AI Content Safety | The service was used in various scenarios such as online marketplaces that moderate product catalogs and other user-generated content, and gaming companies that moderate user-generated game artifacts and chat rooms. <br/> <br/> The service offered several APIs: <br/> - Image Moderation API: This API scanned images and detected potential adult and racy content. <br/> - Text Moderation API: This API scanned text content and returned profanity terms and personal data. <br/> - Video Moderation API: This API scanned videos and detected potential adult and racy content. <br/> - List Management API: This API allowed users to create and manage custom exclusion or inclusion lists of images and text. <br/> Click [here](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) for reference. | 
| AI + APIs | AI Service | Bot Services | Azure AI Bot Service was a part of Azure AI services that provided a comprehensive environment for building, testing, hosting, and deploying bots. It was designed to apply AI features and could be used to build intelligent applications. <br/> <br/> Here are some of the key features of the Azure AI Bot Service: <br/> 1. **Integrated Development Environment**: Azure AI Bot Service provided an integrated development environment for bot building. Its integration with Power Virtual Agents, a fully hosted low-code platform, enabled developers of all technical abilities to build conversational AI bots. <br/> 2. **Build Bots Quickly**: Users could make, test, and publish bots using a low-code graphical interface. They could also improve their bot applications over time. <br/> 3. **Real-Time Notification**: Whenever anomalies were detected, Azure AI Bot Service was able to send real-time notifications through multiple channels using hooks. <br/> 4. **Smart Diagnostic Insights**: Azure AI Bot Service combined anomalies detected on the same multi-dimensional metric into a diagnostic tree to help users analyze root cause into specific dimensions. <br/> <br/> Click [here](https://learn.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) for reference, and [2](https://chatbotbusinessframework.com/azure-bot-service-explained-simply/), [3](https://www.devopsschool.com/blog/what-is-azure-bot-service/), [4](https://www.trustradius.com/products/azure-bot-service/reviews?qs=pros-and-cons#reviews). | 
| AI + APIs | Service | Computer Vision | Azure AI Vision, also known as Azure Computer Vision, was a cloud-based service provided by Microsoft Azure. It offered advanced algorithms that processed images and returned information based on the visual features you’re interested in. This service could be used to build intelligent applications. <br/> <br/> Here are some of the key features of the Azure AI Vision service: <br/> - Optical Character Recognition (OCR): The OCR service extracted text from images. It used deep-learning-based models and worked with text on various surfaces and backgrounds. - Image Analysis: The Image Analysis service extracted many visual features from images, such as objects, faces, adult content, and auto-generated text descriptions. <br/> - Face: The Face service provided AI algorithms that detected, recognized, and analyzed human faces in images. <br/> - Video Analysis: Video Analysis included video-related features like Spatial Analysis and Video Retrieval.  <br/> <br/> For more information click [here](https://azure.microsoft.com/en-us/products/ai-services/ai-vision), [2](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview), [3](https://www.rinf.tech/why-and-when-to-use-azure-computer-vision-and-cognitive-services/), [4](https://www.pluralsight.com/resources/blog/cloud/a-visual-guide-to-computer-vision-in-azure). | 
| AI + APIs | AI Service | Custom Vision | Azure AI Custom Vision was an image recognition service provided by Microsoft Azure. It allowed users to build, deploy, and improve their own image identifier models. An image identifier applied labels to images, according to their visual characteristics. Each label represented a classification or object. <br/> <br/> Here are some of the key features of the Azure AI Custom Vision service: <br/> <br/> 1. **Customization to your scenario**: Users could set their model to perceive a particular object for their use case. <br/> 2. **Intuitive model creation**: Users could easily build their image identifier model using the simple interface. <br/> 3. **Flexible deployment**: Users could run AI Custom Vision in the cloud or on the edge in containers. <br/> 4. **Built-in security**: Users could rely on enterprise-grade security and privacy for their data and any trained models. <br/> <br/> Click [here](https://azure.microsoft.com/en-us/products/ai-services/ai-custom-vision) for more information, [2](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview), [3](https://azure.microsoft.com/ja-jp/products/ai-services/ai-custom-vision), [4](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/custom-vision-service/). | 
| AI + APIs | AI Service | Document intelligences | Azure AI Document Intelligence is a service provided by Microsoft Azure. It is an automated data processing system that uses AI and OCR to quickly extract text and structure from documents. <br/> <br/> Key Features: <br/> - **Text Extraction**: Easily pull data and organize information with prebuilt and custom features. <br/> - **Customized Results**: Get output tailored to your layouts with automatic custom extraction and improve it with human feedback. <br/> - **Flexible Deployment**: Ingest data from the cloud or at the edge and apply to search indexes, business automation workflows, and more. <br/> - **Built-in Security**: Rely on enterprise-grade security and privacy applied to both your data and any trained models. <br/> <br/> Capabilities: <br/> - **Document Analysis**: Detects and extracts text and layout of documents, like tables, check boxes, and objects <br/> - **Prebuilt Models**: These are pretrained models for common scenarios such as IDs, receipts, and invoices, that extract text, key-value pairs, and line items from documents <br/> - **Custom Models**: This custom form service lets you train on your own data to learn the structure of your documents in an intelligent way. <br/> <br/> Applications: <br/> Azure AI Document Intelligence can be used to automate your data processing in applications and workflows, enhance data-driven strategies, and enrich document search capabilities. <br/> Click [here](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence) for reference, [2](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/?view=doc-intel-4.0.0). | 
| AI + APIs | AI Service | Face APIs | TBD | 
| AI + APIs | AI Service | Immersive readers | TBD | 
| AI + APIs | AI Service | Azure OpenAI  | TBD | 
| AI + APIs | AI Service | Speech Services  | TBD | 
| AI + APIs | AI Service | Translators  | TBD | 
| Industry Machine Learning solutions | Solution | Intelligent Recommendations Accounts  | TBD | 
| Industry Machine Learning solutions | Solution | Azure Synapse Analytics  | TBD | 

## AI Search 

> Built-in indexers are available for `Azure Cosmos DB, Azure SQL Database, Azure Blob Storage, and Microsoft SQL Server hosted in Azure Virtual Machines`. Use Azure `Data Factory`, with more than 80 connectors, or `Azure Logic Apps` to connect to your data source. Alternatively, push data into an Azure AI Search index, which has no restrictions on data source type.

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/bdaebc61-162f-4c0f-855f-6dc74de38397)

### Use Cases for Azure AI Search

#### 1. E-commerce and Retail:
   - Enhance product search experiences on e-commerce websites by providing relevant results, filters, and facets.
   - Implement personalized recommendations based on user behavior and preferences.
   - Enable faceted navigation for efficient product discovery.

> [!IMPORTANT]
> Here's an general architecture example of how Azure AI Search can be used in an e-commerce solution: <br/>

> Azure AI Search is an AI-powered information retrieval platform that helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data. It can implement search functionality for any mobile or search application within your organization or as part of software as a service (SaaS) apps. <br/>

> 1. **Customers** go to the e-commerce web application from any device. <br/>
> 2. The **product catalog** is maintained in an **Azure SQL database** for transactional processing. <br/>
> 3. **Azure AI Search** uses a search indexer to automatically keep its search index up to date through integrated change tracking. <br/>
> 4. Customer's search queries are offloaded to the AI Search service, which processes the query and returns the most relevant results. <br/>
> 5. As an alternative to a web-based search experience, customers can also use a conversational bot in social media or straight from digital assistants to search for products and incrementally refine their search query and results. <br/>
> 6. Optionally, customers can use the skillset feature to apply artificial intelligence for even smarter processing. <br/>

> Key Azure services involved in this architecture include: <br/>
> - **Azure App Service - Web Apps**: Hosts web applications allowing autoscale and high availability without having to manage infrastructure. <br/>
> - **Azure SQL Database**: A general-purpose relational database-managed service in Microsoft Azure that supports structures such as relational data, JSON, spatial, and XML. <br/>
> - **Azure AI Search**: A cloud solution that provides a rich search experience over private, heterogeneous content in web, mobile, and enterprise applications. <br/>
> - **Azure AI Bot Service**: Provides tools to build, test, deploy, and manage intelligent bots. <br/>
> - **Azure AI services**: Lets you use intelligent algorithms to see, hear, speak, understand, and interpret your user needs through natural methods of communication. <br/>

####  2. Content and Document Management:
   - Index and search through large document repositories, intranets, and knowledge bases.
   - Implement full-text search, highlighting, and document previews.
   - Facilitate content discovery and retrieval for employees and customers.

> [!IMPORTANT]
> An example of **Use Case: Employee Knowledge Base Search**  <br/>

> **Scenario:** A multinational corporation has a vast internal knowledge base for its employees. This knowledge base includes a variety of documents such as policy documents, training materials, project reports, and more. The company wants to make it easier for employees to find relevant information quickly and efficiently. <br/>

> **Solution with Azure AI Search:** <br/>
> 1. **Azure Blob Storage:** All the documents are stored in Azure Blob Storage. This provides a scalable and secure place for storing all the company's documents. <br/>
> 2. **Azure AI Search:** This is the core service that enables the search functionality. It creates an index of all the documents stored in the Blob Storage. <br/>
> 3. **AI Enrichment:** Azure AI Search uses built-in AI capabilities to extract more insights from the documents. It can extract key phrases, recognize entities, and more. This enriched data is also stored in the search index. <br/>
> 4. **Search Application:** The company builds a search application that uses the Azure AI Search service. Employees can use this application to search the knowledge base. They can perform full-text search, get highlighted results, and even see document previews. <br/>
> 5. **Azure Active Directory:** To ensure secure access to the documents, the search application integrates with Azure Active Directory. This way, only authorized employees can search and view the documents. <br/>
> 6. **Azure Monitor and Azure Application Insights:** These services are used to monitor the performance of the search application and to get insights about its usage. This helps the company to continuously improve the search experience for its employees. <br/>

> This setup allows the company to facilitate content discovery and retrieval for its employees, enhancing productivity and efficiency. It's a great example of how Azure AI Search can be used in the context of content and document management. <br/>

####  3. Enterprise Search:
   - Create a unified search experience across various enterprise data sources (files, databases, APIs).
   - Enable users to find information quickly within their organization.
   - Support natural language queries and relevance tuning.

> [!IMPORTANT]
>  An example of how you can create a unified search experience across various enterprise data sources using Azure resources and Azure AI Search.

> 1. **Data Ingestion**: The first step is to ingest data from various sources. Azure provides several connectors for popular data sources such as Azure SQL Database, Azure Cosmos DB, Azure Blob Storage, and more. You can also use Azure Functions or Logic Apps to pull data from APIs and other sources not directly supported by Azure AI Search.
```python
# Example of using Azure Function to pull data from an API
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    response = requests.get('https://api.example.com/data')
    data = response.json()
    # Code to push data to Azure AI Search
```
> 2. **Indexing**: Once the data is ingested, it needs to be indexed. Azure AI Search provides powerful capabilities to define custom indexes.
```json
// Example of creating an index in Azure AI Search 
{
  "name": "my-index",
  "fields": [
    {"name": "id", "type": "Edm.String", "key": true},
    {"name": "description", "type": "Edm.String", "searchable": true},
    // Other fields...
  ]
}
```
> 3. **Search**: With the data indexed, you can now implement the search experience. Azure AI Search provides a robust REST API and SDKs for popular programming languages.
```python
# Example of using the Python SDK to search
from azure.search.documents import SearchClient

client = SearchClient("<endpoint>", "<index name>", "<api key>")
results = client.search(search_text="example query")
```
> 4. **User Interface**: Finally, you need a user interface for users to interact with. This could be a web application, a mobile app, or even a chatbot. The UI sends queries to Azure AI Search and displays the results. <br/> 
> This is a simplified example, and a real-world implementation would likely involve additional considerations such as security, scalability, and performance optimization. 

####  4. Healthcare and Life Sciences:
   - Build medical knowledge bases for clinicians and researchers.
   - Enable semantic search for medical literature, clinical trials, and patient records.
   - Facilitate drug discovery and research.

> [!IMPORTANT]
> Here’s a general example of a high-level architecture for a solution in the Healthcare and Life Sciences domain using Azure resources, specifically Azure AI Search.

> 1. Data Sources:
>    - Medical Literature
>    - Clinical Trials Data
>    - Patient Records
>    - Research Data
> 
> 2. Azure Data Lake Storage:
>    - Store all the raw data in Azure Data Lake Storage which is a secure, scalable and cost-effective storage.
> 
> 3. Azure Databricks:
>    - Use Azure Databricks for data preparation and transformation. It can handle large amounts of data and perform operations like cleaning, normalization, and aggregation.
> 
> 4. Azure AI Search:
>    - Index the transformed data from Azure Databricks into Azure AI Search. Azure AI Search provides capabilities for advanced content understanding through AI that can help in semantic search.
> 
> 5. Azure Cognitive Services:
>    - Use Azure Cognitive Services for additional AI capabilities like entity recognition, sentiment analysis, etc. This can enhance the search experience by providing more context.
> 
> 6. Azure Web Apps or Azure API Management:
>    - Expose the search capabilities through a Web App or API for clinicians, researchers, and other users to use.
> 
> 7. Azure Active Directory:
>    - Use Azure Active Directory for identity management and securing access to the data and services.
> 
> 8. Azure Monitor and Azure Log Analytics:
>    - Use these services for monitoring the health of the system, diagnosing issues and understanding usage patterns.
>
> This architecture allows you to build a robust medical knowledge base and enables semantic search for medical literature, clinical trials, and patient records. It also facilitates drug discovery and research by providing easy access to relevant information. Please note that this is a high-level architecture and the actual implementation may require additional components or steps based on specific requirements. Always follow data privacy and compliance requirements when dealing with sensitive data like patient records. <br/>
> Remember, Azure AI Search was formerly known as “Cognitive Search”, but the functionality remains the same, providing powerful search capabilities over your data using AI.

####  5. Media and Entertainment:
   - Enhance video and audio content discovery by indexing metadata and transcripts.
   - Implement search for news articles, blogs, podcasts, and multimedia content.
   - Enable personalized recommendations for movies, music, and TV shows.
     
> [!IMPORTANT]
> A high-level example of a solution architecture using Azure AI Search (formerly known as Cognitive Search) for the Media and Entertainment industry. This solution can enhance content discovery, implement search for various types of content, and enable personalized recommendations.

> Solution Architecture for Media and Entertainment using Azure AI Search
> 
> 1. Content Ingestion
> - **Azure Blob Storage**: Store raw multimedia content such as videos, audio files, news articles, blogs, and podcasts.
> 
> 2. Content Processing
> - **Azure Media Services**: Extract metadata and transcripts from video and audio files.
> - **Azure Cognitive Services**: Extract key phrases, entities, and sentiment from news articles and blogs.
> 
> 3. Indexing
> - **Azure AI Search**: Index the metadata and transcripts for efficient search.
> 
> 4. Search and Discovery
> - **Azure AI Search**: Implement full-text search over the indexed content. It supports faceted navigation, filters, and sorting to enhance content discovery.
> 
> 5. Personalized Recommendations
> - **Azure Personalizer**: Use reinforcement learning to provide personalized recommendations for movies, music, and TV shows based on user behavior.
> 
> 6. User Interface
> - **Web App / Mobile App**: A user-friendly interface where users can search for and discover content, and receive personalized recommendations.
>
> Please note that this is a high-level architecture and the actual implementation may vary based on specific requirements and constraints. You might need to consider additional aspects such as security, scalability, and cost optimization when designing the solution.

####  6. Travel and Hospitality:
   - Power hotel booking platforms with efficient search capabilities.
   - Enable location-based search for restaurants, attractions, and events.
   - Implement geospatial search for travel planning.

> [!IMPORTANT]
> An example of an architecture using Azure resources, specifically with Azure AI Search (formerly known as “Cognitive Search”) for the Travel and Hospitality industry. This architecture powers hotel booking platforms with efficient search capabilities, enables location-based search for restaurants, attractions, and events, and implements geospatial search for travel planning.

> Azure Architecture for Travel and Hospitality <br/>
>
> Components:
> 1. **Azure AI Search**: This is the core component that powers the search capabilities. It indexes data from various sources and provides powerful search capabilities.
> 2. **Azure Maps**: This service is used to implement geospatial search for travel planning. It provides location-based services like maps, search, routing, traffic, and time zones.
> 3. **Azure Cosmos DB**: This is the globally distributed, multi-model database service used for managing data at scale.
> 4. **Azure Functions**: This is used for running event-driven serverless compute that can scale on demand.
> 5. **Azure Blob Storage**: This is used for storing unstructured data like images, videos, etc.
> 
> Workflow:
> 1. Data from various sources like hotel details, restaurant details, event details, etc., are stored in Azure Blob Storage.
> 2. Azure Functions are triggered whenever there is new data in Blob Storage. These functions process the data and store it in Cosmos DB.
> 3. Azure AI Search indexes the data from Cosmos DB. It uses cognitive skills for extracting more information from the data.
> 4. Users interact with a front-end application. Whenever they perform a search, the application queries Azure AI Search and presents the results to the user.
> 5. If the user performs a location-based search, the application uses Azure Maps to provide geospatial search capabilities.
> 
> This architecture provides a robust and scalable solution for travel and hospitality platforms.

####  7. Financial Services:
   - Create powerful search interfaces for financial data, stock market information, and investment research.
   - Enable users to find relevant financial documents, reports, and news articles.
   - Implement secure search for sensitive data.
     
> [!IMPORTANT]
> An example of an architecture using Azure resources, specifically with Azure AI Search (formerly known as “Cognitive Search”) for the Financial Services industry. This architecture creates powerful search interfaces for financial data, stock market information, and investment research, enables users to find relevant financial documents, reports, and news articles, and implements secure search for sensitive data.

> Azure Architecture for Financial Services
>
> Components:
>
> 1. **Azure AI Search**: This is the core component that powers the search capabilities. It indexes data from various sources and provides powerful search capabilities.
> 2. **Azure Cosmos DB**: This is the globally distributed, multi-model database service used for managing data at scale.
> 3. **Azure Functions**: This is used for running event-driven serverless compute that can scale on demand.
> 4. **Azure Blob Storage**: This is used for storing unstructured data like financial documents, reports, etc.
> 5. **Azure Key Vault**: This is used for safeguarding cryptographic keys and other secrets used by cloud apps and services.
> 
> Workflow:
> 
> 1. Data from various sources like financial data, stock market information, investment research, etc., are stored in Azure Blob Storage.
> 2. Azure Functions are triggered whenever there is new data in Blob Storage. These functions process the data and store it in Cosmos DB.
> 3. Azure AI Search indexes the data from Cosmos DB. It uses cognitive skills for extracting more information from the data.
> 4. Users interact with a front-end application. Whenever they perform a search, the application queries Azure AI Search and presents the results to the user.
> 5. If the user performs a search for sensitive data, the application uses Azure Key Vault to ensure the search is secure.
>
> This architecture provides a robust and scalable solution for financial services platforms.

