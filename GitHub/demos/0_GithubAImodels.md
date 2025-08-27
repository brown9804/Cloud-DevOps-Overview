# Prototyping with AI Models on GitHub

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)

Last updated: 2025-08-04

----------------------

> GitHub provides a platform for developers to `prototype, experiment with, and integrate AI models into their projects`. This process involves several key steps and tools that facilitate the development and deployment of AI-powered applications.

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Prototyping with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models)
- [GitHub Models](https://docs.github.com/en/github-models)
- [Github Marketplace Models Catalog](https://github.com/marketplace/models/catalog)

</details>


<details>
<summary><b>Table of Content</b> (Click to expand)</summary>

- [Overview](#overview)
- [Demo](#demo)
    - [Set Up Your Environment](#set-up-your-environment)
    - [Find and Select an AI Model](#find-and-select-an-ai-model)
    - [Experiment in the Playground](#experiment-in-the-playground)
    - [Integrate with Visual Studio Code](#integrate-with-visual-studio-code)
    - [Make API Requests](#make-api-requests)
    - [Process and Use Responses](#process-and-use-responses)
    - [Transition to Production](#transition-to-production)

</details>

## Overview 

| **Component**                  | **Description**                                                                                                                                                                                                 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Finding AI Models**          | You can find various AI models on the GitHub Marketplace. Navigate to the `Models` section to explore available models and view their details.                                                                  |
| **Experimenting with AI Models**| GitHub offers a playground where you can test different models by adjusting parameters and submitting prompts. You can experiment with AI models using the API provided by GitHub.                             |
| **Saving and Sharing Experiments** | You can save your playground experiments and share them with others. This is useful for collaboration and getting feedback on your prototypes.                                                                |
| **Integration with Visual Studio Code** | GitHub models can be integrated into Visual Studio Code, allowing you to experiment with AI models directly within your development environment.                                                             |
| **Going to Production**        | Once you are ready to move from prototyping to production, you can switch to using a token from a paid Azure account. This provides more robust and scalable options for deploying your AI models.                |
| **Rate Limits**                | There are rate limits in place to ensure fair usage of the AI models. These limits vary depending on the model and usage scenario. Monitoring your usage and optimizing requests can help you stay within these limits. The rate limits for the playground and free API usage are intended to help you experiment with models and prototype your AI application. For use beyond those limits, and to bring your application to scale, you must provision resources from an Azure account, and authenticate from there instead of your GitHub personal access token.   |

## Demo 
### Set Up Your Environment
  
  1. **Create a GitHub Repository**:
     - Go to GitHub and sign in to your account.
     - Click on the **+** icon in the top right corner and select **New repository**.

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/9a9e85b8-0976-4c5a-9102-9802b8ca864b" />

     - Name your repository and choose its visibility (public or private).
     - Click **Create repository**.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/c37e8637-3a25-439e-8276-9ffe7edfcca4" />

  2. **Generate a Personal Access Token (PAT)**:
     - Click on your profile picture in the top right corner and select **Settings**.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/58182b98-1903-4c67-baf6-737bd6db2b5a" />

     - In the left sidebar, click **Developer settings**.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/45151b34-c8ba-416d-823c-9c0e53b6f77a" />

     - Click **Personal access tokens** and then **Generate new token**.

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/57478e3f-51ee-4271-945e-761630da9936" />

     - Select the scopes you need (e.g., `repo`, `workflow`, `copilot`) and click **Generate token**.
     - Copy the token and store it securely.

          <table>
            <tr>
              <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/28dbaab1-e855-4d3b-8fa7-4b732c9d65e4" /></td>
              <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/d647dec3-9a5d-41d8-8449-cacf11031512" /></td>
            </tr>
          </table>

### Find and Select an AI Model

1. **Navigate to GitHub Marketplace**:
   - Go to the GitHub Marketplace.
   - Click on the **Models** section to explore available AI models.

        <table>
          <tr>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/4d1fda24-f87e-4b19-a92b-6f056768cdb0" /></td>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/5ef8ee5f-0ff7-4cb3-a09f-c9782dabc22f" /></td>
          </tr>
        </table>

2. **Select a Model**:
   - Browse through the models and select one that fits your needs, such as **OpenAI GPT-4**.
   - Review the model’s details, capabilities, and usage instructions.

        <table>
          <tr>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/2e6063c4-ff13-48bf-b879-59d64f1333fb" /></td>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/ea65e7ed-26c5-49af-9c31-7d01a098f2b2" /></td>
          </tr>
        </table>
        
### Experiment in the Playground
1. **Access the Playground**:
   - Go to the playground section for the selected model.
   - You can find this in the model’s details page on GitHub Marketplace.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/9038b2ae-eb72-49a4-bc40-54f41d8feef6" />

2. **Test the Model**:
   - Adjust parameters such as prompt, temperature, and max tokens.
   - Submit prompts to see how the model responds.
   - Example prompt: `Explain the basics of machine learning`

        <table>
          <tr>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/b1e1d229-e7ad-47eb-83e9-5ed3213537b8" /></td>
            <td><img width="400" alt="image" src="" /></td>
          </tr>
        </table>

   -  You can compare the performance between models:

        <table>
          <tr>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/a512c5e9-4021-4db8-95ec-959c43749d23" /></td>
            <td><img width="400" alt="image" src="https://github.com/user-attachments/assets/22fe2804-cd2a-41e1-a391-5e93eb16f17e" /></td>
          </tr>
        </table>

3. **Save Experiments**:
   - Save your experiments by clicking on the `Save` button.
   - Share the saved experiments with collaborators for feedback.
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/04939a90-6bc6-4146-be1a-12b1b4dd7968" />

### Integrate with Visual Studio Code
1. **Install Extensions**:
   - Open Visual Studio Code.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar.
   - Search for and install the `GitHub Copilot` extension.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/2160aff7-0589-4b33-bbeb-71b1235b58b8" />

2. **Set Up API Key**:
   - Open a terminal in Visual Studio Code.
   - Set your API key by running:
     ```bash
     export OPENAI_API_KEY="your-api-key"
     ```

### Make API Requests
1. **Write a Script**:
   - Create a new file in your repository, e.g., `ai_model_test.py`.
   - Write a script to make API requests to the AI model. For example:
     ```python
     import openai

     openai.api_key = "your-api-key"

     response = openai.Completion.create(
         model="gpt-4",
         prompt="Explain the basics of machine learning.",
         max_tokens=100
     )

     print(response.choices[0].text)
     ```

2. **Run the Script**: Run your script in the terminal to see the model’s response.

### Process and Use Responses

| **Step**                | **Description**                                                                                                                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Integrate Responses** | - Use the responses from the AI model in your application. <br> - For example, display the generated text in a web app or use it to automate a task.                                                            |
| **Optimize and Iterate**| - Continuously optimize your prompts and code based on the responses. <br> - Iterate to improve the performance and relevance of the AI model.                                                                  |

### Transition to Production

| **Step**                  | **Description**                                                                                                                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Provision Azure Resources** | - Sign in to your Azure account. <br> - Provision the necessary resources, such as Azure Cognitive Services.                                                                                                  |
| **Update Authentication** | - Switch from using your GitHub PAT to an Azure production key. <br> - Update your environment variable: <br> ``` export OPENAI_API_KEY="your-azure-api-key"```   
| **Monitor and Scale** | Monitor your usage and scale your application as needed using Azure’s infrastructure |


<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1312-limegreen" alt="Total views">
  <p>Refresh Date: 2025-08-27</p>
</div>
<!-- END BADGE -->

