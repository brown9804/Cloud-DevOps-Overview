# Github Licenses - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)

Last updated: 2025-08-27

----------------------

> [!NOTE]
> GitHub areas:
> - GitHub Enterprise Cloud
> - GitHub Enterprise Server
> - GitHub Advanced Security (Code Scanning, Secret Scanning)
> - GitHub Copilot For Business
> - GitHub Copilot for Enterprise
> - GitHub Actions
> - GitHub Code Quality (coming soon) 

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [What is GitHub Copilot?](https://docs.github.com/en/copilot/get-started/what-is-github-copilot)
- [Choosing your enterprise's plan for GitHub Copilot](https://docs.github.com/en/copilot/get-started/choose-enterprise-plan#about-the-plans)
- [Use GitHub Copilot for free in Visual Studio](https://learn.microsoft.com/en-gb/visualstudio/ide/copilot-free-plan?view=vs-2022)
- [Deploy GitHub Copilot to existing Visual Studio instances](https://learn.microsoft.com/en-gb/visualstudio/ide/deploy-copilot-to-enterprise?view=vs-2022)
- [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access)
- [About individual Copilot plans and benefits](https://docs.github.com/en/copilot/concepts/billing/individual-plans)
- [Github Copilot](https://github.com/features/copilot/plans) - features and plans
- [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans)
- [GitHub Enterprise pricing](https://azure.microsoft.com/en-us/pricing/details/githubenterprise/?msockid=38ec3806873362243e122ce086486339) - Table
- [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/?service=githubenterprise)
- [Start your premium free trial by choosing an enterprise type](https://github.com/account/enterprises/new?ref_cta=GHEC+trial&ref_loc=setting+up+a+trial+of+github+enterprise+cloud&ref_page=docs) - Enterprise trial first
- [GitHub Enterprise Cloud Enterprise Managed Users - Microsoft Entra ID / Azure AD Single Sign-On (SSO) Integration Guide](https://se-resource-library.octodemo.com/Azure_SSO_EMU)
- [GitHub Copilot Business - Setup Guide](https://se-resource-library.octodemo.com/GitHub_Copilot_Business)
- [How to link Azure subscription to your GitHub's enterprise account](https://se-resource-library.octodemo.com/Link_Azure_Subscription)
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/) -FAQs
- [Accessing compliance reports for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/accessing-compliance-reports-for-your-organization)
- [STAR Registry Listing for GitHub](https://cloudsecurityalliance.org/star/registry/github-inc/services/github)

</details>

<details>
<summary><b>Table of Content</b> (Click to expand)</summary>

- [GitHub Copilot Personal vs. Businesses Use](#github-copilot-personal-vs-businesses-use)
- [Pricing Details](#pricing-details)
- [Custom LLM Scenario](#custom-llm-scenario)
- [VS code vs Visual Studio](#vs-code-vs-visual-studio)
- [How to setup GitHub Copilot](#how-to-setup-github-copilot)
- [GitHub Copilot with GitHub Enterprise – Setup Procedure](#github-copilot-with-github-enterprise--setup-procedure)

</details>

> [!IMPORTANT]
> The information provided and any document (such as scripts, sample codes, etc.) is provided `AS-IS` and `WITH ALL FAULTS`. Pricing estimates are for `demonstration purposes only and do not reflect final pricing`. `Microsoft assumes no liability` for your use of this information and makes no guarantees or warranties, expressed or implied, regarding its accuracy or completeness, including any pricing details. `Please note that these demos are intended as a guide and are based on my personal experiences. For official guidance, support, or more detailed information, please refer to Microsoft's official documentation or contact Microsoft directly`: [Microsoft Sales and Support](https://support.microsoft.com/contactus?ContactUsExperienceEntryPointAssetId=S.HP.SMC-HOME)

## GitHub Copilot Personal vs. Businesses Use

| Section                                   | Details|
|-------------------------------------------|-----------------|
| **Free Version (Personal Use Only)**   | - GitHub Copilot Free is designed **only for individual developers**.<br>- It **cannot** be enabled on a managed organization account.<br>- When using the free version, **your code may be used to train GitHub’s AI models**. This is a key privacy consideration for anyone working with sensitive or proprietary code. |
| **Organization Use (Paid Plans)**      | - For companies or teams, GitHub offers **Copilot for Business** and **Copilot for Enterprise**.<br>- These plans are built for enterprise compliance and **do not use your code for training**.<br>- They include additional features like policy controls, audit logs, and enterprise-grade security.                                         |

## Pricing Details

> [!IMPORTANT]
> These are the prices as of today. Please make sure to check the current prices here in case anything has changed.
> - [Github Copilot](https://github.com/features/copilot/plans) - features and plans
> - [GitHub Enterprise pricing](https://azure.microsoft.com/en-us/pricing/details/githubenterprise/?msockid=38ec3806873362243e122ce086486339) - Table
> - [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/?service=githubenterprise)

- **Copilot for Business**: \$19 per user/month.  
- **Copilot for Enterprise**: \$39 per user/month.  

    https://github.com/user-attachments/assets/a80d8ab6-e9d0-4ef6-9352-30098bbcbbb3

> [!TIP]
> - To use these, each user typically needs a **GitHub Enterprise license** (around \$20 per user/month).  
> - `Visual Studio subscribers can often add GitHub Enterprise for $0.12 per user/month, then add Copilot for $19.`
> - For large deals, GitHub sometimes offers a `1-month free trial`.

## Custom LLM Scenario

- If an organization deploys its own LLM (e.g., in Azure AI Foundry) and integrates it with GitHub Copilot, the assumption is that `code would not be sent to GitHub for training`.  
- However, this depends on the integration method and data flow, so it’s important to `verify GitHub’s documentation and your LLM’s data-handling policies`.

> e.g How to deploy an AI Foundry instance:

https://github.com/user-attachments/assets/3e47ad50-5ccf-491a-a4c8-1703a219d36e

> e.g How to deploy an LLM within AI Foundry:

https://github.com/user-attachments/assets/b341cc70-f79b-4878-8f9d-7dcfb9255723

> e.g How to integrate LLMs from AI Foundry within GitHub Copilot

https://github.com/user-attachments/assets/3c993648-8a8d-4b5d-be79-19850aeef593

> [!NOTE]
> - Free Copilot = personal use only + code may be used for training.
> - Org use requires paid plans (Business or Enterprise) = code is **not** used for training.
> - Pricing varies, but expect \$19–\$39 per user/month, with possible discounts for Visual Studio subscribers.
> - For privacy-sensitive environments, confirm data policies when integrating custom LLMs.

## VS code vs Visual Studio 

| **Aspect**                     | **Visual Studio Code (VS Code)** | **Visual Studio (IDE)** |
|--------------------------------|---------------------------------------------------------------|--------------------------------------------------------|
| **Product Type**              | Lightweight, cross-platform **code editor** (Windows, macOS, Linux) | Full-featured **Integrated Development Environment** (Windows, Mac version available)                    |
| **Primary Use Cases**         | Web development, scripting, multi-language projects (JavaScript, Python, Go, etc.)                                  | Enterprise development, .NET, C#, C++, large-scale applications |
| **Copilot Installation**      | Install **GitHub Copilot** extension from VS Code Marketplace (Ctrl+Shift+X → search “GitHub Copilot”)              | Enable **GitHub Copilot** via Visual Studio Installer → Modify → Individual Components → GitHub Copilot |
| **Supported Features**        | - Inline code completions<br>- Chat view & Quick Chat<br>- Slash commands<br>- MCP (Model Context Protocol)<br>- Agent Mode | - Inline completions<br>- Copilot Chat integrated into IDE<br>- Agent Mode<br>- Deep .NET/C++ integration |
| **Customization**             | Highly extensible with extensions and custom tool sets | Limited to built-in .NET productivity tools and Copilot defaults |
| **Language Focus**            | Multi-language (JS, TS, Python, Go, PHP, etc.) | Primarily .NET, C#, C++, with strong debugging and refactoring tools|
| **Platform Support**          | Windows, macOS, Linux | Windows (full), macOS (Visual Studio for Mac – different feature set)|
| **Pricing**                   | Requires GitHub Copilot Pro/Business/Enterprise subscription (\$19–\$39 per user/month)                              | `Visual Studio subscribers can often add GitHub Enterprise for $0.12 per user/month, then add Copilot for $19.` |

## How to setup GitHub Copilot

1. Install Visual Studio Code:
    - Download and install VS Code from: https://code.visualstudio.com/
    - Open VS Code once installation is complete.
2. Create a GitHub account (if you don’t have one yet):
    - Visit: https://github.com/join
    - Sign up for a free account and verify your email address.
3. Subscribe to GitHub Copilot Pro:
    - Log in at https://github.com
    - Go to: https://github.com/features/copilot
    - Click `Start my free trial` or subscribe to Copilot Paid Plan. `Choose the appropriate plan for individual or business use.`
4. Add the GitHub Copilot extension in VS Code:
    - Open VS Code.
    - Search for the Extensions view (Ctrl+Shift+X or Cmd+Shift+X).
    - Search for GitHub Copilot and select Install.
5. Sign in to GitHub within VS Code:
    - After installing the extension, sign in when prompted.
    - Authorize VS Code to access your GitHub account through your browser.
    - You’re now ready to use GitHub Copilot in VS Code.

## GitHub Copilot with GitHub Enterprise – Setup Procedure 

> This process enables secure, enterprise-managed deployment of GitHub Copilot

1. Create a GitHub account for your organization. 
2. Please go here [Start your premium free trial by choosing an enterprise type](https://github.com/account/enterprises/new?ref_cta=GHEC+trial&ref_loc=setting+up+a+trial+of+github+enterprise+cloud&ref_page=docs), and start a GitHub Enterprise trial (includes Copilot and advanced security). 
3. Select the `Enterprise Managed Users` option.
4. Enter required organization details and a short code for user management.
5. Set up Single Sign-On (SSO) with your identity provider. Click here to read the steps: [GitHub Enterprise Cloud Enterprise Managed Users - Microsoft Entra ID / Azure AD Single Sign-On (SSO) Integration Guide](https://se-resource-library.octodemo.com/Azure_SSO_EMU)
6. Link your Azure subscription for billing (optional during trial). Click here to read the steps: [How to link Azure subscription to your GitHub's enterprise account](https://se-resource-library.octodemo.com/Link_Azure_Subscription)
7. Add users to the enterprise and assign Copilot seats. Click here to read how: [GitHub Copilot Business - Setup Guide](https://se-resource-library.octodemo.com/GitHub_Copilot_Business)
8. Users install the Copilot extension in their IDE.
9. Users activate their accounts and Copilot access is enabled automatically.

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1312-limegreen" alt="Total views">
  <p>Refresh Date: 2025-08-27</p>
</div>
<!-- END BADGE -->

