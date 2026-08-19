# Jenkins — Complete CI/CD Guide

## 1. What is Jenkins?

If you're learning CI/CD, think of **Jenkins as an automation engine**.

> Jenkins watches for a trigger, runs a sequence of automated steps, and reports whether those steps succeeded or failed.

For example:

```text
Developer
    ↓
git push
    ↓
Jenkins detects change
    ↓
Checkout code
    ↓
Install dependencies
    ↓
Run tests
    ↓
Build application
    ↓
Create Docker image
    ↓
Deploy
```

Jenkins doesn't replace Git, Docker, Azure, etc. It **coordinates them**.

---

# 2. Why Use Jenkins?

Jenkins is an open-source automation server commonly used for:

- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Automated testing
- Build automation
- Deployment automation

Without Jenkins, you might manually run:

```bash
git pull
pip install -r requirements.txt
pytest
docker build -t myapp .
docker push ...
```

With Jenkins, you define these steps once and Jenkins can run them automatically.

```text
git push
   ↓
Jenkins
   ↓
Runs everything automatically
```

---

# 3. Real-Life Example

Imagine a factory.

Instead of an employee manually checking every product, you create an automated production line:

```text
Raw Material
     ↓
Machine 1
     ↓
Machine 2
     ↓
Quality Check
     ↓
Packaging
     ↓
Shipping
```

Jenkins is similar.

Your **code is the raw material**, and your CI/CD pipeline is the production line.

```text
Code
 ↓
Build
 ↓
Test
 ↓
Security Check
 ↓
Package
 ↓
Deploy
```

---

# 4. Jenkins Architecture

A basic Jenkins setup has a **controller** and one or more **agents**.

```text
                 Jenkins Controller
                       │
              ┌────────┴────────┐
              │                 │
          Agent 1           Agent 2
              │                 │
           Build/Test       Build/Test
```

## Jenkins Controller

The controller manages things like:

- Jobs/pipelines
- Configuration
- Credentials
- Scheduling
- Build coordination
- Pipeline orchestration

## Jenkins Agent

An agent actually performs the work.

For example:

```text
Agent
 ├── Git
 ├── Python
 ├── Docker
 └── Testing tools
```

The controller tells the agent:

> "Checkout this repository and run the tests."

The agent performs the commands and reports the result.

For learning, Jenkins and the build workload can run on the same machine. In production, controller and agents are often separated.

---

# 5. How Jenkins Works

A common flow is:

```text
GitHub Repository
       │
       │ git push
       ↓
    Jenkins
       │
       ↓
  Checkout Code
       │
       ↓
Install Dependencies
       │
       ↓
    Run Tests
       │
       ↓
      Build
       │
       ↓
      Deploy
```

The five important concepts are:

```text
Trigger
   ↓
Pipeline
   ↓
Stage
   ↓
Step
   ↓
Result
```

---

# 6. What is a Jenkins Job?

A **job** is a task configured in Jenkins.

For example:

```text
Python-CI
```

could:

```text
1. Clone repository
2. Install dependencies
3. Run pytest
```

Another job:

```text
Deploy-Application
```

could:

```text
1. Build Docker image
2. Push image
3. Deploy application
```

Modern Jenkins usage commonly favors **Pipeline jobs**, where the pipeline is defined as code.

---

# 7. What is a Jenkins Pipeline?

A Jenkins Pipeline defines your CI/CD workflow.

For example:

```text
Pipeline
   │
   ├── Checkout
   ├── Build
   ├── Test
   ├── Security Scan
   └── Deploy
```

Or:

```text
Build
  ↓
Test
  ↓
Deploy
```

If `Test` fails:

```text
Build
  ↓
Test ❌
  ↓
STOP
```

Deployment doesn't happen.

---

# 8. Declarative vs Scripted Pipeline

Jenkins has two major pipeline styles.

## Declarative Pipeline

More structured and easier to learn.

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
    }
}
```

## Scripted Pipeline

More flexible and Groovy-based.

```groovy
node {
    stage('Build') {
        echo 'Building'
    }

    stage('Test') {
        echo 'Testing'
    }
}
```

For learning CI/CD, **start with Declarative Pipeline**.

---

# 9. What is a Jenkinsfile?

A **Jenkinsfile** is a text file that defines your Jenkins pipeline.

You usually put it in the root of your Git repository:

```text
my-project/
│
├── src/
├── tests/
├── requirements.txt
├── Dockerfile
└── Jenkinsfile
```

Example:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

    }
}
```

Now your pipeline is stored alongside your application code.

This is called **Pipeline as Code**.

---

# 10. Understanding the Jenkinsfile

## Pipeline

```groovy
pipeline {
```

Defines a Declarative Jenkins pipeline.

## Agent

```groovy
agent any
```

Means:

> Run this pipeline on any available Jenkins agent.

## Stages

```groovy
stages {
```

Contains the major parts of your pipeline.

## Stage

```groovy
stage('Test') {
```

Defines one stage.

## Steps

```groovy
steps {
    sh 'pytest'
}
```

Defines the commands Jenkins should execute.

On Linux:

```groovy
sh 'command'
```

On Windows:

```groovy
bat 'command'
```

---

# 11. Creating Your First Jenkins CI Pipeline

Suppose you have a Python project:

```text
my-python-app/
│
├── app.py
├── test_app.py
├── requirements.txt
└── Jenkinsfile
```

Your `Jenkinsfile`:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

    }
}
```

The flow becomes:

```text
Git Repository
      ↓
Checkout
      ↓
Install
      ↓
pytest
      ↓
Success / Failure
```

---

# 12. How Jenkins Gets Your Code

A common setup is:

```text
GitHub
   ↓
Jenkins
   ↓
Git clone / checkout
```

You configure the repository in Jenkins.

For example:

```text
Repository:
https://github.com/username/my-python-app.git
```

Jenkins then checks out the code when the pipeline runs.

For private repositories, you'll need appropriate Git credentials.

---

# 13. How Do We Trigger Jenkins?

There are several ways.

## Manual Trigger

You click:

```text
Build Now
```

Useful when learning.

## Polling SCM

Jenkins periodically checks whether the repository changed.

```text
Jenkins
   ↓
Check Git
   ↓
Changes?
   ↓
Yes → Build
```

This works, but webhook-based triggers are generally preferable for prompt CI.

## Webhook

A better approach is:

```text
Developer
   ↓
git push
   ↓
GitHub
   ↓
Webhook
   ↓
Jenkins
   ↓
Pipeline
```

The Git hosting platform tells Jenkins:

> "A change happened. Start the pipeline."

---

# 14. Jenkins CI Pipeline

A proper CI pipeline might look like:

```text
             Git Push
                ↓
             Jenkins
                ↓
             Checkout
                ↓
          Install Dependencies
                ↓
              Linting
                ↓
               Tests
                ↓
           Security Scan
                ↓
              Build
                ↓
              SUCCESS
```

This is **Continuous Integration**.

---

# 15. Creating a CD Pipeline

Suppose your application is packaged as a Docker image.

Pipeline:

```text
Git Push
   ↓
Jenkins
   ↓
Checkout
   ↓
Test
   ↓
Docker Build
   ↓
Docker Push
   ↓
Deploy
```

Example:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push myregistry/myapp:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }

    }
}
```

Conceptually:

```text
                 Jenkins
                   │
         ┌─────────┴─────────┐
         ↓                   ↓
       Build                Test
         │                   │
         └─────────┬─────────┘
                   ↓
              Docker Image
                   ↓
             Container Registry
                   ↓
                 Deploy
```

---

# 16. Jenkins + Docker

Jenkins and Docker are commonly used together.

```text
Jenkins
   ↓
docker build
   ↓
Docker Image
   ↓
docker push
   ↓
Container Registry
   ↓
Deployment
```

For example, your pipeline might create:

```text
myapp:1.0.0
```

and push it to a registry.

For Azure:

```text
GitHub
   ↓
Jenkins
   ↓
Docker Build
   ↓
Azure Container Registry
   ↓
Azure App Service / Azure Kubernetes Service
```

---

# 17. Jenkins + Azure

A possible Azure-based architecture:

```text
                  GitHub
                    │
                    │ Push
                    ↓
                  Jenkins
                    │
              ┌─────┴─────┐
              ↓           ↓
            Build        Test
              │           │
              └─────┬─────┘
                    ↓
              Docker Build
                    ↓
         Azure Container Registry
                    ↓
              Azure Deployment
                    ↓
        App Service / AKS / VM
```

Jenkins can authenticate to Azure using appropriate credentials and Azure tooling.

---

# 18. Jenkins Credentials

Never hard-code secrets into your Jenkinsfile.

Bad:

```groovy
sh 'docker login -u myuser -p mypassword'
```

Don't put secrets directly into your Jenkinsfile.

Instead:

```text
Jenkins
  ↓
Credentials
  ↓
Username / Password / Token / Secret
  ↓
Pipeline
```

Jenkins provides a **Credentials** system for storing secrets.

Your Jenkinsfile can reference a credential without hardcoding its value.

---

# 19. Environment Variables

You can define environment variables:

```groovy
pipeline {
    agent any

    environment {
        APP_NAME = 'myapp'
        ENVIRONMENT = 'production'
    }

    stages {

        stage('Build') {
            steps {
                sh 'echo Building $APP_NAME'
            }
        }
    }
}
```

For secrets, use Jenkins credentials rather than plain environment values in the Jenkinsfile.

---

# 20. Pipeline with Multiple Environments

A more realistic CD pipeline:

```text
             Build
               ↓
             Test
               ↓
          Deploy Dev
               ↓
        Integration Tests
               ↓
         Deploy Staging
               ↓
            Approval
               ↓
       Deploy Production
```

Jenkins can represent this with stages:

```groovy
stage('Deploy Dev') {
    steps {
        // deployment
    }
}

stage('Deploy Staging') {
    steps {
        // deployment
    }
}

stage('Deploy Production') {
    steps {
        input message: 'Deploy to production?'
    }
}
```

The `input` step can provide a manual approval point.

---

# 21. Complete Example

A simplified production-style structure:

```groovy
pipeline {

    agent any

    environment {
        IMAGE_NAME = 'myapp'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'ruff check .'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Security Scan') {
            steps {
                sh "trivy image ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
```

The flow:

```text
Checkout
   ↓
Install
   ↓
Lint
   ↓
Test
   ↓
Docker Build
   ↓
Security Scan
   ↓
Deploy
   ↓
Success / Failure
```

---

# 22. What is `post`?

The `post` section defines actions that happen after the pipeline or stage finishes.

Example:

```groovy
post {

    success {
        echo 'Success'
    }

    failure {
        echo 'Failed'
    }

    always {
        echo 'Pipeline finished'
    }
}
```

You can use this for:

- Notifications
- Cleanup
- Reports
- Test artifacts

---

# 23. Jenkins Plugins

Jenkins has a large plugin ecosystem.

Plugins allow Jenkins to integrate with other technologies.

For example:

```text
Jenkins
 ├── Git Plugin
 ├── Docker Plugin
 ├── GitHub integration
 ├── Credentials Plugin
 ├── Pipeline Plugin
 └── Azure-related plugins
```

You don't need to install hundreds of plugins.

Install only what your pipeline actually needs and keep them maintained.

---

# 24. Jenkins Pipeline vs GitHub Actions

| Feature | Jenkins | GitHub Actions |
|---|---|---|
| Type | Automation server | CI/CD platform |
| Open source | Yes | GitHub-hosted platform |
| Self-hosting | Common | Possible with self-hosted runners |
| Configuration | Jenkinsfile | YAML workflow |
| Plugins | Huge ecosystem | Actions marketplace |
| GitHub integration | Via integrations/plugins | Native |
| Infrastructure control | High | Depends on runner setup |

### Jenkins

```text
You manage Jenkins
      ↓
Jenkins server
      ↓
Agents
      ↓
Pipeline
```

### GitHub Actions

```text
GitHub Repository
      ↓
GitHub Actions
      ↓
Runner
      ↓
Workflow
```

---

# 25. Jenkins Mental Model

Don't try to memorize all the Jenkins syntax yet.

Remember:

```text
                  JENKINS

                   Trigger
                      ↓
                 Jenkins Job
                      ↓
                   Pipeline
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      Build          Test        Security
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                   Package
                      ↓
                    Deploy
                      ↓
                  Production
```

And:

```text
Jenkinsfile
     ↓
Defines Pipeline
     ↓
Pipeline contains Stages
     ↓
Stages contain Steps
```

---

# 26. Practical Learning Path

A useful hands-on sequence is:

## Step 1 — Run Jenkins locally or on an Azure VM

```text
Azure VM
   ↓
Ubuntu
   ↓
Jenkins
```

## Step 2 — Create a simple Jenkins job

```text
Build Now
   ↓
echo "Hello Jenkins"
```

## Step 3 — Connect Jenkins to GitHub

```text
GitHub
   ↓
Jenkins
```

## Step 4 — Create your first Jenkinsfile

```text
Checkout
   ↓
Install
   ↓
Test
```

## Step 5 — Add a GitHub webhook

```text
git push
   ↓
GitHub webhook
   ↓
Jenkins
   ↓
Pipeline automatically runs
```

## Step 6 — Add Docker

```text
Test
 ↓
Docker Build
 ↓
Docker Image
```

## Step 7 — Push to Azure Container Registry

```text
Jenkins
   ↓
Docker Build
   ↓
Azure Container Registry
```

## Step 8 — Deploy to an Azure service

```text
ACR
 ↓
Azure App Service / AKS
```

At that point, you'll have built a real CI/CD pipeline rather than only learning Jenkins syntax.

---

# 27. Jenkins with Docker Desktop — Local Setup

If you're running Jenkins locally using **Docker Desktop**, the most important concept is **port mapping**.

The Jenkins web interface normally listens on port `8080` inside the container.

You need to map your computer's port `8080` to the container's port `8080`.

```text
Browser
   ↓
http://localhost:8080
   ↓
Windows
   ↓
Docker port mapping
   ↓
Jenkins container :8080
   ↓
Jenkins
```

The mapping should look like:

```text
Host port       Container port
    8080   →        8080
```

---

# 28. Check Port Mapping in Docker Desktop

Open:

**Docker Desktop → Containers → Jenkins container**

Look under **Ports**.

You want something similar to:

```text
0.0.0.0:8080 → 8080/tcp
```

or:

```text
localhost:8080 → 8080
```

If you only see:

```text
8080/tcp
```

without a host port, Jenkins' port is not exposed to your computer.

That is why:

```text
http://localhost:8080
```

will not work.

---

# 29. Run Jenkins with Docker

If the container was created without port mapping, stop and remove it and create it again with the required ports.

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts
```

The important part is:

```text
-p 8080:8080
```

It means:

```text
Your computer's port 8080
          ↓
Docker container's port 8080
          ↓
        Jenkins
```

---

# 30. Recommended Jenkins Docker Command

For learning Jenkins locally, use a Docker volume so Jenkins data persists:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

The volume:

```text
-v jenkins_home:/var/jenkins_home
```

provides persistent Jenkins storage.

Without persistent storage, deleting the container can cause you to lose Jenkins configuration, jobs, plugins, and other data.

Architecture:

```text
Docker Container
       │
       ↓
/var/jenkins_home
       │
       ↓
Docker Volume
       │
       ↓
Persistent Jenkins data
```

---

# 31. Check Whether the Jenkins Container Is Running

Run:

```bash
docker ps
```

You should see something similar to:

```text
CONTAINER ID   IMAGE                 PORTS
abc123         jenkins/jenkins:lts  0.0.0.0:8080->8080/tcp
```

The important part is:

```text
0.0.0.0:8080->8080/tcp
```

If it is present, Docker is forwarding your computer's port `8080` to Jenkins.

Then open:

```text
http://localhost:8080
```

---

# 32. Check Jenkins Logs

If port mapping looks correct but the page still doesn't load:

```bash
docker logs jenkins
```

You can also follow the logs:

```bash
docker logs -f jenkins
```

Wait until Jenkins has finished starting.

You should eventually see a message indicating that Jenkins is fully running.

Then try:

```text
http://localhost:8080
```

---

# 33. Get the Initial Jenkins Admin Password

The first time Jenkins starts, it asks for an initial administrator password.

Get it with:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

You'll receive a password similar to:

```text
a8f7c2......
```

Copy it into the Jenkins setup page.

---

# 34. Jenkins Docker Ports

There are two ports you may commonly see:

## Port 8080

Used for the Jenkins web UI.

```text
Browser
   ↓
localhost:8080
   ↓
Jenkins
```

## Port 50000

Historically used for Jenkins controller/agent communication.

For initial local learning, the most important port is:

```text
8080
```

---

# 35. Troubleshooting `localhost:8080`

If Jenkins is running but `localhost:8080` doesn't open, check these in order:

### Check 1 — Is the container running?

```bash
docker ps
```

### Check 2 — Is port 8080 mapped?

```bash
docker port jenkins
```

You should see a mapping for container port `8080`.

### Check 3 — Check Jenkins logs

```bash
docker logs jenkins
```

### Check 4 — Check Docker Desktop

Verify:

```text
Host:      8080
Container: 8080
```

### Check 5 — Open the correct address

```text
http://localhost:8080
```

---

# 36. Final Jenkins + Docker Architecture

Your local learning setup can look like:

```text
                    Windows
                       │
                       │ localhost:8080
                       ↓
                 Docker Desktop
                       │
                       ↓
              ┌──────────────────┐
              │ Jenkins Container │
              │                  │
              │ Jenkins :8080    │
              │                  │
              └────────┬─────────┘
                       │
                       ↓
                jenkins_home
                 Docker Volume
```

Then:

```text
Browser
   ↓
http://localhost:8080
   ↓
Jenkins Dashboard
```

---

# 37. Overall Jenkins Learning Architecture

Once the local setup is working, the full learning path becomes:

```text
                       GitHub
                          │
                          │ git push
                          ↓
                    GitHub Webhook
                          │
                          ↓
                       Jenkins
                          │
              ┌───────────┴───────────┐
              ↓                       ↓
            Build                    Test
              │                       │
              └───────────┬───────────┘
                          ↓
                    Docker Build
                          ↓
                     Docker Image
                          ↓
             Azure Container Registry
                          ↓
                 Azure Deployment
                          ↓
             App Service / AKS / VM
```

This is the complete mental model to keep in mind while learning Jenkins.
