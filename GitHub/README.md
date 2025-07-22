# GitHub Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


Last updated: 2024-12-13

----------------------

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Deleting Your Commit History?](https://xebia.com/blog/deleting-your-commit-history/)
- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [GitHub installation](https://git-scm.com/download/win)
- [Free Password Generator](https://www.lastpass.com/features/password-generator)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [GitHub Commands Glossary](https://www.atlassian.com/git/glossary#commands)
- [MARKDOWN CHEAT SHEET](https://github.com/Kernix13/markdown-cheatsheet?tab=readme-ov-file#block-elements)

</details>

## Why GitHub for DevOps and Azure?

> GitHub is the world’s leading platform for version control and collaboration. Used with Azure, it enables:

- **Continuous Integration/Continuous Deployment (CI/CD)** using GitHub Actions or Azure Pipelines.
- **Infrastructure as Code (IaC)** through integration with tools like Terraform or Bicep.
- **Automation** for testing, security, and delivery.
- **Collaboration** using pull requests, code reviews, and issues—all traceable to Azure Boards.

## How to Commit/Push to GitHub

> This section summarizes the standard workflow for contributing code.

> [!TIP]
> For secure Azure DevOps integration, set up SSH keys ([see reference](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).

1. Clone the repository  
   `git clone <repo-url>`  
   *(Use SSH for better security and automation in CI/CD pipelines.)* `git -c http.sslVerify=false clone <repository-name - ssh>`

2. Change directory and open in VS Code  
   `cd <repo-path>`  
   `code .`

3. Sync with latest changes  
   `git pull`

4. Create a new branch for your feature/bugfix  
   `git checkout -b <branch-name>`

5. Check status, stage, and commit  
   `git status`  
   `git add -A`  
   `git commit -m "Description"`

6. Push your branch  
   `git push origin <branch-name>`

7. (Optional) Pull latest changes from remote  
   `git pull origin <branch-name>`

**Troubleshooting:**  
- If you get SSL or permission errors, verify your SSH key setup and repository access.
- Use `git config --global user.name` and `git config --global user.email` to set your identity.

## GitHub Actions: Automate with Azure

> You can automate builds, tests, and deployments to Azure using [GitHub Actions](https://github.com/Azure/actions):

- Deploy web apps, containers, or functions to Azure.
- Run Terraform/Bicep scripts for infrastructure provisioning.
- Integrate security scans and compliance checks into your CI/CD.


## Good Content List Format 

```
<details><summary> <a href=""> </a></summary><ul>
        <li> <a href=""> </a> </li>
        <li> <a href=""> </a> </li>
        <li> <a href=""> </a> </li>
        <li> <a href=""> </a> </li>
        <li> <a href="" > </a> </li>
        <li> <a href="" > </a> </li>
        <li> <a href="" > </a> </li>
</details></li> <!-- End  -->
```

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->

