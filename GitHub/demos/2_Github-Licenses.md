# Github Licenses - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)

Last updated: 2025-08-04

----------------------

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [What is GitHub Copilot?](https://docs.github.com/en/copilot/get-started/what-is-github-copilot)
- [Choosing your enterprise's plan for GitHub Copilot](https://docs.github.com/en/copilot/get-started/choose-enterprise-plan#about-the-plans)
- [Use GitHub Copilot for free in Visual Studio](https://learn.microsoft.com/en-gb/visualstudio/ide/copilot-free-plan?view=vs-2022)
- [Deploy GitHub Copilot to existing Visual Studio instances](https://learn.microsoft.com/en-gb/visualstudio/ide/deploy-copilot-to-enterprise?view=vs-2022)
- [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access)
- [About individual Copilot plans and benefits](https://docs.github.com/en/copilot/concepts/billing/individual-plans)
- [Github Copilot](https://github.com/features/copilot/plans) - features and plans
- [GitHub Enterprise pricing](https://azure.microsoft.com/en-us/pricing/details/githubenterprise/?msockid=38ec3806873362243e122ce086486339) - Table
- [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/?service=githubenterprise)

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


> [!NOTE]
> - Free Copilot = personal use only + code may be used for training.
> - Org use requires paid plans (Business or Enterprise) = code is **not** used for training.
> - Pricing varies, but expect \$19–\$39 per user/month, with possible discounts for Visual Studio subscribers.
> - For privacy-sensitive environments, confirm data policies when integrating custom LLMs.

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1405-limegreen" alt="Total views">
  <p>Refresh Date: 2025-08-04</p>
</div>
<!-- END BADGE -->

