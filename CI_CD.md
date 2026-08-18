# CI/CD Basics

## 1. What is CI/CD?

**CI/CD** stands for:

- **CI** → Continuous Integration
- **CD** → Continuous Delivery / Continuous Deployment

CI/CD is a software development practice that automates the process of:

```text
Write Code
    ↓
Commit Code
    ↓
Build
    ↓
Test
    ↓
Package
    ↓
Deploy
    ↓
Monitor
```

Instead of developers manually performing these steps every time they make a change, CI/CD tools automate them.

---

# 2. Why Do We Need CI/CD?

Imagine a team of 10 developers working on the same application.

Every developer is making changes:

```text
Developer A → Authentication
Developer B → Payment
Developer C → Dashboard
Developer D → API
Developer E → Database
```

Without CI/CD, someone may have to manually:

1. Pull the latest code
2. Install dependencies
3. Run tests
4. Build the application
5. Deploy it to the server

This becomes slow and error-prone.

With CI/CD:

```text
Developer
    ↓
git push
    ↓
CI/CD Pipeline
    ↓
Build
    ↓
Tests
    ↓
Deploy
```

The process becomes automated and repeatable.

---

# 3. Continuous Integration (CI)

## What is CI?

**Continuous Integration** means developers frequently integrate their code into a shared repository and automatically verify that the new code works.

For example:

```text
Developer writes code
        ↓
git push
        ↓
CI starts
        ↓
Install dependencies
        ↓
Run linting
        ↓
Run tests
        ↓
Build application
```

If something fails:

```text
❌ CI Failed
```

The developer can fix the issue before it reaches production.

---

# 4. Simple CI Example

Suppose you have a Python application.

A developer pushes:

```bash
git push origin main
```

The CI system automatically executes:

```bash
pip install -r requirements.txt
pytest
```

If all tests pass:

```text
✅ Build Successful
✅ Tests Passed
```

If tests fail:

```text
❌ Build Failed
```

---

# 5. Continuous Delivery

**Continuous Delivery** means the application is automatically prepared and made ready for deployment.

A typical pipeline:

```text
Code
 ↓
Build
 ↓
Test
 ↓
Package
 ↓
Ready for Deployment
```

The important point is:

> The software is always kept in a deployable state.

The final production deployment may still require manual approval.

Example:

```text
Developer
    ↓
Push Code
    ↓
CI
    ↓
Build
    ↓
Test
    ↓
Staging
    ↓
Manual Approval
    ↓
Production
```

---

# 6. Continuous Deployment

**Continuous Deployment** goes one step further.

After the code successfully passes all automated checks, it is automatically deployed to production.

```text
Code
 ↓
Build
 ↓
Test
 ↓
Security Scan
 ↓
Deploy
 ↓
Production
```

No manual approval is required for the production deployment.

Example:

```text
git push
   ↓
CI/CD Pipeline
   ↓
Tests pass
   ↓
Automatic deployment
   ↓
Production
```

---

# 7. Continuous Delivery vs Continuous Deployment

| Feature                           | Continuous Delivery | Continuous Deployment |
| --------------------------------- | ------------------- | --------------------- |
| Build automatically               | ✅                  | ✅                    |
| Test automatically                | ✅                  | ✅                    |
| Deployment prepared automatically | ✅                  | ✅                    |
| Production deployment             | Manual approval     | Automatic             |
| Automation level                  | High                | Very high             |

### Easy way to remember

**Continuous Delivery:**

> "The application is ready to deploy."

**Continuous Deployment:**

> "The application is automatically deployed."

---

# 8. CI/CD Pipeline

A **pipeline** is a sequence of automated steps used to build, test, and deploy an application.

Example:

```text
                 CI/CD PIPELINE

Developer
    │
    ▼
Git Push
    │
    ▼
Checkout Code
    │
    ▼
Install Dependencies
    │
    ▼
Lint
    │
    ▼
Run Tests
    │
    ▼
Build Application
    │
    ▼
Security Scan
    │
    ▼
Deploy to Staging
    │
    ▼
Integration Tests
    │
    ▼
Deploy to Production
```

Each step is often called a:

- Stage
- Job
- Step
- Task

The exact terminology depends on the CI/CD platform.

---

# 9. CI/CD Pipeline Stages

A common pipeline looks like this:

## Stage 1 — Source

Get the latest code.

```text
GitHub
GitLab
Bitbucket
Azure Repos
```

---

## Stage 2 — Build

Install dependencies and build the application.

Python:

```bash
pip install -r requirements.txt
```

Node.js:

```bash
npm install
npm run build
```

Java:

```bash
mvn package
```

---

## Stage 3 — Test

Run automated tests.

Example:

```bash
pytest
```

Possible testing levels:

```text
Unit Tests
Integration Tests
API Tests
End-to-End Tests
```

---

## Stage 4 — Code Quality

Check code quality.

Examples:

```text
Ruff
Flake8
Pylint
SonarQube
ESLint
```

---

## Stage 5 — Security

Scan the application and dependencies.

Examples:

```text
Trivy
Snyk
Dependabot
SonarQube
OWASP tools
```

---

## Stage 6 — Package

Create a deployable artifact.

Examples:

```text
Docker Image
Python Package
JAR
ZIP
Executable
```

For Docker:

```bash
docker build -t my-app .
```

---

## Stage 7 — Deploy

Deploy the application.

For example:

```text
Development
     ↓
Staging
     ↓
Production
```

---

# 10. CI/CD Environments

Most real-world applications have multiple environments.

```text
Development
     ↓
Testing
     ↓
Staging
     ↓
Production
```

### Development

Used by developers.

### Testing

Used for automated testing.

### Staging

A production-like environment used for final verification.

### Production

The environment used by real users.

---

# 11. Types of CI/CD Pipelines

There are several ways to classify CI/CD pipelines.

## 11.1 CI Pipeline

Focuses mainly on integrating and testing code.

```text
Code
 ↓
Build
 ↓
Test
 ↓
Quality Check
```

---

## 11.2 Continuous Delivery Pipeline

```text
Code
 ↓
Build
 ↓
Test
 ↓
Package
 ↓
Staging
 ↓
Manual Approval
 ↓
Production
```

---

## 11.3 Continuous Deployment Pipeline

```text
Code
 ↓
Build
 ↓
Test
 ↓
Security
 ↓
Staging
 ↓
Production
```

Production deployment happens automatically.

---

# 12. CI/CD Trigger Types

A pipeline needs a way to know when it should run.

## Push Trigger

Runs when code is pushed.

```text
git push
   ↓
Pipeline starts
```

---

## Pull Request Trigger

Runs when a pull request is created or updated.

```text
Developer
    ↓
Pull Request
    ↓
CI
    ↓
Tests
```

This is very common.

---

## Scheduled Trigger

Runs at a specific time.

Example:

```text
Every night at 2 AM
```

Useful for:

- Security scans
- Regression tests
- Dependency checks

---

## Manual Trigger

A developer manually starts the pipeline.

---

# 13. CI/CD Tools and Technologies

There are many CI/CD platforms.

## GitHub Actions

CI/CD integrated with GitHub.

Example:

```text
GitHub Repository
       ↓
GitHub Actions
       ↓
Build
       ↓
Test
       ↓
Deploy
```

Configuration is commonly stored in:

```text
.github/workflows/
```

---

## GitLab CI/CD

GitLab has built-in CI/CD functionality.

Configuration:

```text
.gitlab-ci.yml
```

---

## Jenkins

Jenkins is a popular automation server.

It can be used for:

- CI
- CD
- Build automation
- Testing
- Deployment

Jenkins pipelines can be defined using a `Jenkinsfile`.

---

## Azure DevOps

Microsoft's DevOps platform provides:

- Azure Repos
- Azure Pipelines
- Azure Boards
- Azure Test Plans
- Azure Artifacts

For Azure-based learning, **Azure Pipelines** is particularly important.

---

## CircleCI

Cloud-based CI/CD platform.

---

## Travis CI

Another CI service that can run automated builds and tests.

---

# 14. Common CI/CD Tools

CI/CD is not just one tool.

A real pipeline may use multiple technologies.

Example:

```text
GitHub
   ↓
GitHub Actions
   ↓
Python
   ↓
Pytest
   ↓
Docker
   ↓
Trivy
   ↓
Azure
```

Different tools perform different jobs.

---

# 15. Source Control Tools

Used to store and manage source code.

Common options:

```text
Git
GitHub
GitLab
Bitbucket
Azure Repos
```

The most fundamental technology is:

```text
Git
```

---

# 16. Build Tools

Build tools create the application/package.

Examples:

### Python

```text
pip
poetry
uv
```

### Java

```text
Maven
Gradle
```

### JavaScript

```text
npm
yarn
pnpm
```

### .NET

```text
dotnet CLI
```

---

# 17. Testing Tools

Testing is a major part of CI.

Python:

```text
pytest
unittest
```

JavaScript:

```text
Jest
Mocha
```

Java:

```text
JUnit
```

---

# 18. Code Quality Tools

Examples:

```text
SonarQube
Ruff
Flake8
Pylint
ESLint
```

They can detect:

- Bugs
- Code smells
- Formatting problems
- Security issues
- Maintainability problems

---

# 19. Containerization

Docker is commonly used in CI/CD.

Example:

```text
Source Code
    ↓
Docker Build
    ↓
Docker Image
    ↓
Container Registry
    ↓
Deployment
```

Common container registries:

```text
Docker Hub
Azure Container Registry
Amazon ECR
Google Artifact Registry
GitHub Container Registry
```

For Azure:

```text
Azure Container Registry (ACR)
```

is commonly used.

---

# 20. Infrastructure and Deployment Tools

CI/CD pipelines can deploy infrastructure as well as applications.

Common tools:

```text
Terraform
Bicep
Ansible
Pulumi
```

For Azure specifically:

```text
Azure CLI
Bicep
Terraform
```

---

# 21. CI/CD with Azure

A typical Azure-based setup could look like:

```text
Developer
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Build
    ↓
Test
    ↓
Docker Build
    ↓
Azure Container Registry
    ↓
Azure App Service
```

Or using Azure DevOps:

```text
Developer
    ↓
Azure Repos
    ↓
Azure Pipelines
    ↓
Build
    ↓
Test
    ↓
Docker
    ↓
Azure Container Registry
    ↓
Azure App Service
```

---

# 22. How to Write a CI/CD Pipeline

A CI/CD pipeline is usually written as a configuration file.

The exact syntax depends on the platform.

For example, GitHub Actions uses YAML.

Typical structure:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

---

# 23. Understanding the YAML

The first part:

```yaml
name: CI Pipeline
```

gives the workflow a name.

---

The trigger:

```yaml
on:
  push:
    branches:
      - main
```

means:

```text
When code is pushed to main
        ↓
Start pipeline
```

---

The job:

```yaml
jobs:
  test:
```

defines a job called `test`.

---

The runner:

```yaml
runs-on: ubuntu-latest
```

means the job runs on an Ubuntu environment provided by the CI platform.

---

The steps:

```yaml
steps:
```

contain the commands/actions that should execute.

---

Checkout:

```yaml
uses: actions/checkout@v4
```

gets your repository code.

---

Install dependencies:

```yaml
run: |
  pip install -r requirements.txt
```

executes a shell command.

---

Run tests:

```yaml
run: |
  pytest
```

runs the test suite.

---

# 24. Example Complete CI/CD Flow

Suppose you have a FastAPI application.

Repository:

```text
my-fastapi-app/
│
├── src/
├── tests/
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

Developer:

```bash
git add .
git commit -m "Add prediction endpoint"
git push
```

Then:

```text
GitHub
   ↓
GitHub Actions
   ↓
Checkout
   ↓
Install dependencies
   ↓
Run tests
   ↓
Build Docker image
   ↓
Security scan
   ↓
Push image to registry
   ↓
Deploy
```

---

# 25. CI/CD with Docker

A common production architecture:

```text
              Developer
                  │
                  ▼
              Git Push
                  │
                  ▼
             CI Pipeline
                  │
       ┌──────────┴──────────┐
       │                     │
       ▼                     ▼
     Build                  Test
       │                     │
       └──────────┬──────────┘
                  ▼
            Docker Build
                  │
                  ▼
          Docker Image
                  │
                  ▼
       Container Registry
                  │
                  ▼
             Deployment
                  │
                  ▼
             Production
```

---

# 26. CI/CD Secrets

Never hard-code credentials inside your repository.

Bad:

```yaml
API_KEY: "my-secret-key"
```

Instead, use secret management provided by your CI/CD platform.

For example:

```text
GitHub Secrets
Azure DevOps secret variables
Azure Key Vault
```

Pipeline:

```text
CI/CD
  ↓
Retrieve secret securely
  ↓
Use secret
  ↓
Deploy
```

---

# 27. Environment Variables

Applications commonly use environment variables for configuration.

Example:

```text
DATABASE_URL
API_KEY
MODEL_NAME
ENVIRONMENT
```

Instead of:

```python
API_KEY = "actual-secret"
```

use:

```python
import os

API_KEY = os.getenv("API_KEY")
```

The CI/CD system can provide the value during deployment.

---

# 28. Artifacts

An **artifact** is a file/package produced by a pipeline.

Examples:

```text
Docker image
JAR file
ZIP file
Python package
Test report
Build output
```

Example:

```text
Source Code
    ↓
Build
    ↓
my-app.zip
```

The pipeline can store the artifact and use it later for deployment.

---

# 29. Pipeline Failure

A major advantage of CI/CD is that a failed step stops the pipeline.

Example:

```text
Build
  ↓
✅
  ↓
Tests
  ↓
❌ FAILED
  ↓
STOP
```

The application doesn't continue to production.

This prevents many broken deployments.

---

# 30. Deployment Strategies

CI/CD also includes different deployment strategies.

## Rolling Deployment

Gradually replace old instances with new ones.

```text
Old Version
Old Version
Old Version

       ↓

New Version
Old Version
Old Version

       ↓

New Version
New Version
Old Version

       ↓

New Version
New Version
New Version
```

---

## Blue-Green Deployment

Maintain two environments.

```text
Blue → Current Production

Green → New Version
```

After testing:

```text
Traffic
   ↓
Green
```

If something goes wrong, traffic can be switched back.

---

## Canary Deployment

Release the new version to a small percentage of users first.

```text
Users
 │
 ├── 95% → Old Version
 │
 └── 5%  → New Version
```

If everything works:

```text
50% → New
50% → Old
```

Eventually:

```text
100% → New
```

---

# 31. CI/CD Best Practices

### Keep builds reproducible

The same source code should produce the same build as much as possible.

### Run tests automatically

Don't depend only on manual testing.

### Keep pipelines fast

Slow pipelines discourage developers from using them effectively.

### Secure secrets

Never commit:

```text
API keys
Passwords
Tokens
Private keys
```

### Use separate environments

```text
Development
Staging
Production
```

### Add security scanning

Scan:

```text
Code
Dependencies
Docker images
Infrastructure
```

### Use approvals where appropriate

Production deployments may require approval depending on the organization's risk level.

### Monitor deployments

CI/CD doesn't end at deployment.

After deployment:

```text
Deploy
  ↓
Monitor
  ↓
Detect problems
  ↓
Rollback if necessary
```

---

# 32. CI/CD vs DevOps

These terms are related but not identical.

### DevOps

A broader culture and set of practices combining:

```text
Development
+
Operations
+
Automation
+
Monitoring
+
Collaboration
```

### CI/CD

A major part of DevOps focused on:

```text
Build
Test
Release
Deploy
```

Think:

```text
                 DevOps
                    │
       ┌────────────┼────────────┐
       │            │            │
      CI/CD      Monitoring   Infrastructure
       │
   ┌───┴───┐
   CI      CD
```

---

# 33. Common CI/CD Technology Stack

A modern project might use:

```text
Version Control
      ↓
GitHub
      ↓
CI/CD
      ↓
GitHub Actions
      ↓
Testing
      ↓
Pytest
      ↓
Code Quality
      ↓
Ruff / SonarQube
      ↓
Containerization
      ↓
Docker
      ↓
Registry
      ↓
Azure Container Registry
      ↓
Deployment
      ↓
Azure App Service / Azure Kubernetes Service
      ↓
Monitoring
      ↓
Azure Monitor / Application Insights
```

---

# 34. CI/CD Tools Cheat Sheet

| Category           | Tools                                                            |
| ------------------ | ---------------------------------------------------------------- |
| Version Control    | Git, GitHub, GitLab, Azure Repos                                 |
| CI/CD              | GitHub Actions, GitLab CI/CD, Jenkins, Azure Pipelines, CircleCI |
| Build              | Maven, Gradle, npm, pip, Poetry                                  |
| Testing            | Pytest, JUnit, Jest                                              |
| Code Quality       | SonarQube, Ruff, ESLint, Pylint                                  |
| Security           | Trivy, Snyk, Dependabot                                          |
| Containers         | Docker                                                           |
| Container Registry | Docker Hub, Azure Container Registry, GitHub Container Registry  |
| IaC                | Terraform, Bicep, Pulumi, Ansible                                |
| Cloud              | Azure, AWS, GCP                                                  |
| Monitoring         | Azure Monitor, Application Insights, Prometheus, Grafana         |

---

# 35. CI/CD Mental Model

Remember this:

```text
             CI/CD
                │
                ▼
        "Automate software
         delivery process"
                │
                ▼
           Git Push
                │
                ▼
             Build
                │
                ▼
             Test
                │
                ▼
          Quality/Security
                │
                ▼
             Package
                │
                ▼
             Deploy
                │
                ▼
           Production
                │
                ▼
            Monitor
```

### CI

> **Integrate code frequently and automatically build/test it.**

### Continuous Delivery

> **Keep software continuously ready for deployment, with production release potentially requiring approval.**

### Continuous Deployment

> **Automatically deploy successfully validated changes to production.**

### Pipeline

> **An automated sequence of steps that moves code from source control to a deployable/running application.**

### Tools

> **Git manages source code, CI/CD platforms automate pipelines, testing tools verify code, Docker packages applications, registries store artifacts/images, and cloud platforms host the application.**
