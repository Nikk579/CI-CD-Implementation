# Kubernetes — Complete Beginner-to-Industry Guide

> A practical guide to understanding Kubernetes from the basics to real-world usage, with examples, YAML files, commands, architecture, advantages, limitations, and industry practices.

---

## Table of Contents

1. [What is Kubernetes?](#1-what-is-kubernetes)
2. [Why Do We Need Kubernetes?](#2-why-do-we-need-kubernetes)
3. [Containers vs Kubernetes](#3-containers-vs-kubernetes)
4. [Kubernetes Architecture](#4-kubernetes-architecture)
5. [Important Kubernetes Components](#5-important-kubernetes-components)
6. [Kubernetes Objects](#6-kubernetes-objects)
7. [Installing Kubernetes Locally](#7-installing-kubernetes-locally)
8. [kubectl](#8-kubectl)
9. [Your First Kubernetes Deployment](#9-your-first-kubernetes-deployment)
10. [Pods](#10-pods)
11. [Deployments](#11-deployments)
12. [Services](#12-services)
13. [Labels and Selectors](#13-labels-and-selectors)
14. [Namespaces](#14-namespaces)
15. [ConfigMaps](#15-configmaps)
16. [Secrets](#16-secrets)
17. [Environment Variables](#17-environment-variables)
18. [Volumes and Persistent Storage](#18-volumes-and-persistent-storage)
19. [Scaling](#19-scaling)
20. [Rolling Updates](#20-rolling-updates)
21. [Rollback](#21-rollback)
22. [Health Checks](#22-health-checks)
23. [Resource Requests and Limits](#23-resource-requests-and-limits)
24. [Jobs and CronJobs](#24-jobs-and-cronjobs)
25. [Ingress](#25-ingress)
26. [Networking Basics](#26-networking-basics)
27. [Kubernetes Security Basics](#27-kubernetes-security-basics)
28. [Kubernetes on Azure](#28-kubernetes-on-azure)
29. [Kubernetes in AI/ML Applications](#29-kubernetes-in-aiml-applications)
30. [CI/CD with Kubernetes](#30-cicd-with-kubernetes)
31. [How Kubernetes Is Used in Industry](#31-how-kubernetes-is-used-in-industry)
32. [Advantages](#32-advantages)
33. [Limitations](#33-limitations)
34. [Docker vs Kubernetes](#34-docker-vs-kubernetes)
35. [Virtual Machines vs Kubernetes](#35-virtual-machines-vs-kubernetes)
36. [Typical Production Architecture](#36-typical-production-architecture)
37. [Important Commands Cheat Sheet](#37-important-commands-cheat-sheet)
38. [Recommended Learning Path](#38-recommended-learning-path)
39. [Mini Project](#39-mini-project)

---

# 1. What is Kubernetes?

Kubernetes, commonly called **K8s**, is an open-source platform used to **deploy, manage, scale, and maintain containerized applications**.

Suppose you have a Python FastAPI application.

You create a Docker image:

```text
FastAPI Application
        ↓
     Docker
        ↓
   Docker Image
```

You can run that image using Docker:

```bash
docker run -p 8000:8000 my-api
```

This works well for one or a few containers.

But imagine your application grows.

You now have:

```text
Frontend
Backend API
Authentication Service
Payment Service
Database
Redis
Worker
ML Inference Service
```

And you need:

- Multiple instances
- Automatic restart
- Load balancing
- Scaling
- Service discovery
- Rolling deployments
- Health checks
- Resource management
- High availability

Managing all of this manually becomes difficult.

This is where Kubernetes comes in.

```text
                  Kubernetes
                      |
       +--------------+--------------+
       |              |              |
    Backend         Worker        ML Service
       |              |              |
    3 Pods          2 Pods         4 Pods
```

Kubernetes continuously tries to make the actual state of your infrastructure match the desired state you specify.

---

# 2. Why Do We Need Kubernetes?

Without Kubernetes, you might manually manage containers:

```text
Server
 ├── Container 1
 ├── Container 2
 ├── Container 3
 └── Container 4
```

If Container 2 crashes:

```text
Container 2 → CRASHED
```

You need something to restart it.

If traffic increases:

```text
100 requests/sec
       ↓
Application overloaded
```

You may need to manually start additional containers.

Kubernetes can automate these tasks.

For example:

```yaml
replicas: 3
```

This tells Kubernetes:

> I want 3 running instances of this application.

If one crashes:

```text
Before:

Pod 1   Pod 2   Pod 3
 ↓       ↓       ↓
Running Running Crashed
```

Kubernetes creates another:

```text
Pod 1   Pod 2   Pod 3
 ↓       ↓       ↓
Running Running Running
```

---

# 3. Containers vs Kubernetes

Docker and Kubernetes are **not competitors**.

They solve different problems.

## Docker

Docker is primarily used to:

- Build container images
- Run containers
- Package applications

Example:

```bash
docker build -t my-api .
docker run my-api
```

## Kubernetes

Kubernetes manages containerized applications across infrastructure.

It handles:

- Deployment
- Scaling
- Networking
- Service discovery
- Health checks
- Self-healing
- Configuration
- Rolling updates

A simplified relationship:

```text
Application
     ↓
 Docker Image
     ↓
Container
     ↓
Kubernetes
     ↓
Pods / Services / Deployments
```

---

# 4. Kubernetes Architecture

A Kubernetes cluster consists primarily of:

```text
                 Kubernetes Cluster
                        |
              +---------+---------+
              |                   |
        Control Plane          Worker Nodes
              |                   |
       +------+-----+       +-----+-----+
       |            |       |           |
   API Server   Scheduler   Pod        Pod
       |                    Pod        Pod
 Controller Manager
       |
    etcd
```

---

# 5. Important Kubernetes Components

## 5.1 Control Plane

The Control Plane manages the Kubernetes cluster.

Important components:

```text
API Server
Scheduler
Controller Manager
etcd
```

---

## 5.2 API Server

The API Server is the main entry point into Kubernetes.

When you run:

```bash
kubectl get pods
```

`kubectl` communicates with the Kubernetes API Server.

```text
kubectl
   ↓
API Server
   ↓
Kubernetes Cluster
```

---

## 5.3 etcd

`etcd` is the key-value database used by Kubernetes to store cluster state.

It contains information such as:

```text
Deployments
Pods
Services
Configurations
Cluster state
```

Think of it as Kubernetes' source of truth for cluster state.

---

## 5.4 Scheduler

The Scheduler decides **which worker node should run a Pod**.

For example:

```text
Pod requested
     ↓
Scheduler
     ↓
Node 1 has enough resources?
     ↓
YES
     ↓
Pod scheduled on Node 1
```

---

## 5.5 Controller Manager

Controllers continuously monitor the cluster.

Suppose:

```text
Desired Pods = 3
Current Pods = 2
```

The controller notices the difference and creates another Pod.

```text
Desired State
      ↓
   3 Pods
      ↑
Controller
      ↑
Current State
   2 Pods
```

---

# 6. Kubernetes Objects

Kubernetes uses objects to describe desired infrastructure.

Common objects include:

```text
Pod
Deployment
Service
ConfigMap
Secret
Namespace
Job
CronJob
Ingress
PersistentVolume
PersistentVolumeClaim
StatefulSet
DaemonSet
```

You define these objects using YAML.

Example:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-api

spec:
  replicas: 3
```

This describes the desired state.

---

# 7. Installing Kubernetes Locally

For learning Kubernetes locally, common options include:

### Minikube

Runs a Kubernetes cluster locally.

### Docker Desktop Kubernetes

Docker Desktop can provide a local Kubernetes cluster.

### kind

`kind` runs Kubernetes nodes using containers.

For beginners, Minikube or Docker Desktop Kubernetes are convenient.

---

# 8. kubectl

`kubectl` is the command-line tool used to communicate with Kubernetes.

Check the cluster:

```bash
kubectl cluster-info
```

Check nodes:

```bash
kubectl get nodes
```

Check Pods:

```bash
kubectl get pods
```

Check deployments:

```bash
kubectl get deployments
```

Check services:

```bash
kubectl get services
```

Get more information:

```bash
kubectl describe pod <pod-name>
```

View logs:

```bash
kubectl logs <pod-name>
```

Execute a command inside a Pod:

```bash
kubectl exec -it <pod-name> -- /bin/bash
```

---

# 9. Your First Kubernetes Deployment

Let's deploy an Nginx application.

Create:

```text
deployment.yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx-deployment

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

Apply it:

```bash
kubectl apply -f deployment.yaml
```

Check:

```bash
kubectl get deployments
```

Check Pods:

```bash
kubectl get pods
```

You should see something similar to:

```text
NAME                                READY
nginx-deployment-xxxxxx-xxxxx      1/1
nginx-deployment-xxxxxx-yyyyy      1/1
nginx-deployment-xxxxxx-zzzzz      1/1
```

Because:

```yaml
replicas: 3
```

---

# 10. Pods

A **Pod** is the smallest deployable unit in Kubernetes.

Usually:

```text
Pod
 └── Container
```

But a Pod can contain multiple tightly coupled containers:

```text
Pod
 ├── Application Container
 └── Sidecar Container
```

Most beginner applications use one container per Pod.

Example:

```yaml
apiVersion: v1
kind: Pod

metadata:
  name: nginx-pod

spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

Create:

```bash
kubectl apply -f pod.yaml
```

Check:

```bash
kubectl get pods
```

---

# 11. Deployments

You generally don't create individual Pods manually for production applications.

Instead, use a Deployment.

A Deployment manages Pods.

```text
Deployment
     |
     +---- Pod
     |
     +---- Pod
     |
     +---- Pod
```

Example:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: backend

spec:
  replicas: 3

  selector:
    matchLabels:
      app: backend

  template:
    metadata:
      labels:
        app: backend

    spec:
      containers:
        - name: backend
          image: my-backend:1.0
          ports:
            - containerPort: 8000
```

---

# 12. Services

Pods are temporary.

A Pod can be deleted and recreated with a different IP address.

Therefore, applications should not directly depend on Pod IPs.

Kubernetes provides **Services**.

```text
                 Service
                    |
          +---------+---------+
          |         |         |
         Pod       Pod       Pod
```

The Service provides a stable network endpoint.

---

## ClusterIP

Default Service type.

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  selector:
    app: backend

  ports:
    - port: 80
      targetPort: 8000
```

Apply:

```bash
kubectl apply -f service.yaml
```

---

## NodePort

Exposes a service through a port on the node.

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  type: NodePort

  selector:
    app: backend

  ports:
    - port: 8000
      targetPort: 8000
      nodePort: 30080
```

---

## LoadBalancer

Cloud providers can provision an external load balancer.

```yaml
apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  type: LoadBalancer

  selector:
    app: backend

  ports:
    - port: 80
      targetPort: 8000
```

---

# 13. Labels and Selectors

Labels are key-value metadata.

Example:

```yaml
labels:
  app: backend
  environment: production
```

A Service can select Pods:

```yaml
selector:
  app: backend
```

This means:

> Send traffic to Pods with `app=backend`.

Labels are extremely important in Kubernetes.

---

# 14. Namespaces

Namespaces logically separate resources.

Example:

```text
Cluster
 |
 +-- development
 |
 +-- staging
 |
 +-- production
```

Create:

```bash
kubectl create namespace development
```

Deploy into it:

```bash
kubectl apply -f deployment.yaml -n development
```

View:

```bash
kubectl get pods -n development
```

Namespaces are commonly used to separate environments or teams.

---

# 15. ConfigMaps

A ConfigMap stores non-sensitive configuration.

Example:

```yaml
apiVersion: v1
kind: ConfigMap

metadata:
  name: backend-config

data:
  APP_ENV: production
  LOG_LEVEL: info
```

Use it in a Deployment:

```yaml
envFrom:
  - configMapRef:
      name: backend-config
```

This allows configuration to be separated from the application image.

---

# 16. Secrets

Secrets are intended for sensitive configuration such as:

```text
API keys
Passwords
Tokens
Credentials
```

Example:

```yaml
apiVersion: v1
kind: Secret

metadata:
  name: backend-secret

type: Opaque

stringData:
  API_KEY: example-key
  DB_PASSWORD: example-password
```

Then:

```yaml
envFrom:
  - secretRef:
      name: backend-secret
```

Important:

> Kubernetes Secrets are not automatically equivalent to a fully secure secrets-management system. In production, consider cloud secret-management solutions and appropriate encryption/access controls.

---

# 17. Environment Variables

Example:

```yaml
containers:
  - name: backend
    image: my-backend:1.0

    env:
      - name: APP_ENV
        value: production

      - name: PORT
        value: "8000"
```

You can also load values from ConfigMaps and Secrets.

---

# 18. Volumes and Persistent Storage

Containers are generally treated as ephemeral.

If a container writes:

```text
/data/file.txt
```

that data may disappear when the container is replaced unless persistent storage is used.

Kubernetes provides storage abstractions.

Important concepts:

```text
PersistentVolume (PV)
PersistentVolumeClaim (PVC)
StorageClass
```

A PVC requests storage:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim

metadata:
  name: app-storage

spec:
  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 5Gi
```

Application:

```yaml
volumes:
  - name: app-data
    persistentVolumeClaim:
      claimName: app-storage
```

---

# 19. Scaling

One of Kubernetes' major advantages is scaling.

Current:

```text
3 Pods
```

Scale to 5:

```bash
kubectl scale deployment backend --replicas=5
```

Check:

```bash
kubectl get pods
```

---

## Horizontal Pod Autoscaler

Kubernetes can automatically adjust the number of Pods based on metrics.

Conceptually:

```text
Low Traffic
    ↓
2 Pods

High Traffic
    ↓
5 Pods

Very High Traffic
    ↓
10 Pods
```

Example:

```bash
kubectl autoscale deployment backend \
  --cpu-percent=70 \
  --min=2 \
  --max=10
```

---

# 20. Rolling Updates

Suppose production currently runs:

```text
backend:1.0
```

You create:

```text
backend:2.0
```

A Deployment can gradually replace old Pods.

```text
Old Pods
1.0
1.0
1.0

        ↓

1.0
1.0
2.0

        ↓

1.0
2.0
2.0

        ↓

2.0
2.0
2.0
```

Update:

```bash
kubectl set image deployment/backend \
  backend=my-backend:2.0
```

Check:

```bash
kubectl rollout status deployment/backend
```

---

# 21. Rollback

If version 2.0 has a problem:

```bash
kubectl rollout undo deployment/backend
```

Check:

```bash
kubectl rollout history deployment/backend
```

This is extremely useful for production deployments.

---

# 22. Health Checks

Applications can fail without the container itself crashing.

Kubernetes supports probes.

## Liveness Probe

Checks whether the application is alive.

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000

  initialDelaySeconds: 10
  periodSeconds: 10
```

If the application becomes unhealthy, Kubernetes can restart the container.

---

## Readiness Probe

Checks whether the application is ready to receive traffic.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8000

  initialDelaySeconds: 5
  periodSeconds: 5
```

This is important during deployments.

---

# 23. Resource Requests and Limits

Each container can define resource requirements.

```yaml
resources:

  requests:
    cpu: "250m"
    memory: "256Mi"

  limits:
    cpu: "500m"
    memory: "512Mi"
```

### Request

The amount Kubernetes uses when scheduling the Pod.

### Limit

The maximum resource allocation allowed for the container.

Example:

```text
Application

CPU request: 250m
CPU limit:   500m

Memory request: 256Mi
Memory limit:   512Mi
```

Resource management becomes especially important in production.

---

# 24. Jobs and CronJobs

Not every application runs continuously.

## Job

A Job runs a task to completion.

Example:

```yaml
apiVersion: batch/v1
kind: Job

metadata:
  name: data-processing

spec:
  template:

    spec:
      restartPolicy: Never

      containers:
        - name: processor
          image: my-data-processor:1.0
```

---

## CronJob

A CronJob runs periodically.

Example:

```yaml
apiVersion: batch/v1
kind: CronJob

metadata:
  name: daily-task

spec:
  schedule: "0 7 * * *"

  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never

          containers:
            - name: task
              image: my-task:1.0
```

This runs approximately every day at 7:00 according to the cluster's configured time basis.

Useful for:

```text
Data processing
Reports
Cleanup
Scheduled ML jobs
ETL
Backups
```

---

# 25. Ingress

Ingress manages external HTTP/HTTPS access to services.

Example:

```text
                    Internet
                       |
                    Ingress
                       |
          +------------+------------+
          |                         |
       frontend                  backend
          |                         |
        Pods                      Pods
```

Example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress

metadata:
  name: application-ingress

spec:
  rules:

    - host: example.com

      http:
        paths:

          - path: /
            pathType: Prefix

            backend:
              service:
                name: frontend
                port:
                  number: 80

          - path: /api
            pathType: Prefix

            backend:
              service:
                name: backend
                port:
                  number: 8000
```

Ingress requires an appropriate ingress controller in the cluster.

---

# 26. Networking Basics

Kubernetes networking allows:

```text
Pod → Pod
Pod → Service
Pod → Internet
External → Service
```

A common flow is:

```text
User
 ↓
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Pods
 ↓
Application
```

Kubernetes networking is one of the more advanced areas to learn after the fundamentals.

---

# 27. Kubernetes Security Basics

Important security concepts include:

```text
RBAC
Service Accounts
Network Policies
Secrets
Pod Security
Namespaces
Resource Limits
Image Security
```

---

## RBAC

RBAC means:

**Role-Based Access Control**

It controls:

> Who can perform which actions on which resources.

For example:

```text
Developer
  ↓
Can read Pods

Production Admin
  ↓
Can create/delete Deployments

Viewer
  ↓
Read-only access
```

---

# 28. Kubernetes on Azure

Since you're learning **Microsoft Azure**, an important Kubernetes service to learn is:

## Azure Kubernetes Service (AKS)

AKS is Microsoft's managed Kubernetes service.

Instead of manually managing an entire Kubernetes cluster, Azure manages much of the underlying Kubernetes infrastructure for you.

Conceptually:

```text
Azure
 |
 +-- AKS Cluster
      |
      +-- Control Plane
      |
      +-- Worker Nodes
           |
           +-- Pods
           +-- Services
           +-- Deployments
```

Typical architecture:

```text
User
 |
Internet
 |
Azure Load Balancer
 |
AKS
 |
Ingress
 |
Services
 |
Pods
 |
Applications
```

Common Azure services used with AKS include:

```text
Azure Container Registry
Azure Load Balancer
Azure Monitor
Azure Key Vault
Azure Storage
Azure Managed Identity
Azure Virtual Network
```

A common production flow is:

```text
Developer
    |
    ↓
GitHub
    |
    ↓
CI/CD Pipeline
    |
    ↓
Build Docker Image
    |
    ↓
Azure Container Registry
    |
    ↓
AKS
    |
    ↓
Pods
```

---

# 29. Kubernetes in AI/ML Applications

Kubernetes is particularly useful for large AI/ML systems.

Consider an AI platform:

```text
                 API Gateway
                     |
                  Ingress
                     |
             +-------+-------+
             |               |
         Backend API     ML Service
             |               |
             |          +----+----+
             |          |         |
             |        GPU Pod   GPU Pod
             |
        Database
```

Possible workloads:

```text
LLM inference
Computer vision
OCR
Model serving
Batch inference
Training jobs
Embedding generation
RAG pipelines
Agentic AI services
```

For example, your FastAPI ML application could be packaged into Docker:

```text
FastAPI
YOLO
OpenCV
Python
```

Build:

```bash
docker build -t vision-api:1.0 .
```

Push the image to a container registry.

Then Kubernetes can run multiple instances:

```text
vision-api:1.0

       ↓

+-------------+
| Kubernetes  |
+-------------+
      |
  +---+---+---+
  |   |   |   |
 Pod Pod Pod Pod
```

This can be useful when many inference requests arrive simultaneously.

For GPU workloads, Kubernetes can also schedule workloads onto nodes with available GPUs, provided the cluster is configured with the appropriate GPU support.

---

# 30. CI/CD with Kubernetes

Kubernetes is commonly part of a CI/CD pipeline.

Example:

```text
Developer
    |
    ↓
Git Push
    |
    ↓
GitHub
    |
    ↓
CI Pipeline
    |
    +-- Run Tests
    |
    +-- Build Docker Image
    |
    +-- Security Checks
    |
    ↓
Container Registry
    |
    ↓
CD Pipeline
    |
    ↓
Kubernetes
    |
    ↓
Deployment
```

Example deployment command:

```bash
kubectl apply -f deployment.yaml
```

Or the pipeline can update the image:

```bash
kubectl set image deployment/backend \
  backend=myregistry/backend:1.2.0
```

A more mature approach may use:

```text
Helm
GitOps
Argo CD
Flux
```

---

# 31. How Kubernetes Is Used in Industry

Companies commonly use Kubernetes when applications need reliable container orchestration at scale.

Typical architecture:

```text
                  Users
                    |
                    ↓
              Load Balancer
                    |
                    ↓
                 Ingress
                    |
        +-----------+-----------+
        |           |           |
     Service     Service     Service
        |           |           |
       Pods        Pods        Pods
        |           |           |
    Backend      Worker      ML API
        |
   +----+----+
   |         |
Database    Cache
```

Kubernetes can manage:

- Microservices
- APIs
- Background workers
- Batch processing
- ML inference
- Web applications
- Event processing
- Internal platforms

---

# 32. Advantages

## 32.1 Automatic Scaling

Applications can scale based on demand.

```text
Traffic ↑
   ↓
Pods ↑
```

---

## 32.2 Self-Healing

If a Pod crashes:

```text
Pod crashes
     ↓
Kubernetes detects it
     ↓
New Pod created
```

---

## 32.3 High Availability

Applications can run multiple replicas.

```text
Pod 1
Pod 2
Pod 3
```

If one fails:

```text
Pod 1 ❌
Pod 2 ✅
Pod 3 ✅
```

The remaining instances can continue serving traffic while Kubernetes replaces the failed Pod.

---

## 32.4 Rolling Deployments

New application versions can be deployed gradually.

---

## 32.5 Service Discovery

Services provide stable endpoints for communicating applications.

---

## 32.6 Resource Management

You can define CPU and memory requirements.

---

## 32.7 Portability

Kubernetes concepts are available across many environments:

```text
On-premises
Azure
AWS
Google Cloud
Local environments
```

---

# 33. Limitations

Kubernetes is powerful, but it is not always the right choice.

## 33.1 Complexity

Kubernetes has many concepts:

```text
Pods
Deployments
Services
Ingress
Namespaces
Volumes
RBAC
Networking
Operators
Helm
```

It can take time to learn.

---

## 33.2 Operational Overhead

Running Kubernetes introduces additional infrastructure and operational responsibilities.

---

## 33.3 Debugging Can Be Difficult

A request may travel through:

```text
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Container
 ↓
Application
```

A problem anywhere can cause failures.

---

## 33.4 Overkill for Small Applications

For a simple application:

```text
One VM
   ↓
One Docker Container
```

Kubernetes may provide more complexity than value.

---

## 33.5 Cost

Running multiple nodes, load balancers, storage, monitoring, and other components can increase costs.

---

# 34. Docker vs Kubernetes

| Feature | Docker | Kubernetes |
|---|---|---|
| Build images | Yes | No |
| Run containers | Yes | Yes, through container runtime |
| Container orchestration | Limited | Yes |
| Auto scaling | Limited/manual | Yes |
| Self healing | Limited | Yes |
| Service discovery | Limited | Yes |
| Rolling deployment | Limited | Yes |
| Cluster management | No | Yes |
| Production orchestration | Limited | Yes |

Think:

```text
Docker
=
Containerization

Kubernetes
=
Container Orchestration
```

---

# 35. Virtual Machines vs Kubernetes

A VM gives you a complete operating system environment.

```text
VM
 |
OS
 |
Application
```

Kubernetes manages containerized workloads.

```text
Kubernetes Node
 |
Container Runtime
 |
Pod
 |
Container
 |
Application
```

They are not necessarily alternatives.

Kubernetes itself commonly runs workloads on virtual machines or equivalent compute nodes.

---

# 36. Typical Production Architecture

A realistic cloud architecture might look like:

```text
                        Internet
                           |
                           ↓
                    DNS / CDN / WAF
                           |
                           ↓
                    Load Balancer
                           |
                           ↓
                       Ingress
                           |
             +-------------+-------------+
             |             |             |
          Frontend      Backend       ML API
             |             |             |
           Pods          Pods          Pods
                           |
              +------------+------------+
              |            |            |
           Database      Redis       Storage
```

For Azure:

```text
                         Azure
                           |
        +------------------+------------------+
        |                                     |
   Azure Container                       Azure AKS
     Registry                               |
        |                              Kubernetes
        |                                   |
        |                          +--------+--------+
        |                          |        |        |
        +----------------------> Backend  Worker   ML API
```

---

# 37. Important Commands Cheat Sheet

## Cluster

```bash
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
```

## Pods

```bash
kubectl get pods
kubectl get pods -A
kubectl describe pod <pod>
kubectl logs <pod>
kubectl delete pod <pod>
```

## Deployments

```bash
kubectl get deployments
kubectl describe deployment <deployment>
kubectl scale deployment <deployment> --replicas=5
kubectl rollout status deployment/<deployment>
kubectl rollout history deployment/<deployment>
kubectl rollout undo deployment/<deployment>
```

## Services

```bash
kubectl get services
kubectl describe service <service>
```

## Apply configuration

```bash
kubectl apply -f file.yaml
```

## Delete configuration

```bash
kubectl delete -f file.yaml
```

## Get everything

```bash
kubectl get all
```

## Debugging

```bash
kubectl describe pod <pod>
kubectl logs <pod>
kubectl exec -it <pod> -- /bin/bash
```

---

# 38. Recommended Learning Path

Don't try to learn every Kubernetes feature at once.

Follow this order.

## Level 1 — Containers

Learn:

```text
Docker
Dockerfile
Images
Containers
Docker Compose
```

---

## Level 2 — Kubernetes Fundamentals

Learn:

```text
Cluster
Node
Pod
Deployment
Service
Labels
Selectors
Namespace
kubectl
YAML
```

---

## Level 3 — Application Configuration

Learn:

```text
ConfigMap
Secret
Environment Variables
Volumes
PersistentVolume
PersistentVolumeClaim
```

---

## Level 4 — Production Concepts

Learn:

```text
Scaling
HPA
Rolling Updates
Rollback
Readiness Probe
Liveness Probe
Resource Requests
Resource Limits
```

---

## Level 5 — Networking

Learn:

```text
ClusterIP
NodePort
LoadBalancer
Ingress
DNS
Network Policies
```

---

## Level 6 — Security

Learn:

```text
RBAC
Service Accounts
Secrets
Pod Security
Network Policies
Identity
```

---

## Level 7 — Cloud Kubernetes

Since you're learning Azure:

```text
Azure Kubernetes Service (AKS)
Azure Container Registry
Azure Load Balancer
Azure Monitor
Azure Key Vault
Azure Storage
Managed Identity
Azure Virtual Network
```

---

## Level 8 — Advanced Industry Topics

Eventually learn:

```text
Helm
Kustomize
Operators
GitOps
Argo CD
Prometheus
Grafana
Distributed tracing
Service mesh
GPU workloads
Cluster autoscaling
```

---

# 39. Mini Project

A great beginner project is to deploy a simple FastAPI application.

## Project Architecture

```text
FastAPI
   |
Docker
   |
Docker Image
   |
Kubernetes
   |
Deployment
   |
+---+---+
|   |   |
Pod Pod Pod
    |
 Service
    |
External Access
```

---

## Step 1 — Create FastAPI Application

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from Kubernetes"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
```

---

## Step 2 — Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Step 3 — Requirements

`requirements.txt`

```text
fastapi
uvicorn
```

---

## Step 4 — Build Image

```bash
docker build -t fastapi-k8s:1.0 .
```

---

## Step 5 — Run with Docker

```bash
docker run -p 8000:8000 fastapi-k8s:1.0
```

Test:

```text
http://localhost:8000
```

---

## Step 6 — Create Kubernetes Deployment

`deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: fastapi-deployment

spec:
  replicas: 3

  selector:
    matchLabels:
      app: fastapi

  template:

    metadata:
      labels:
        app: fastapi

    spec:

      containers:

        - name: fastapi
          image: fastapi-k8s:1.0

          ports:
            - containerPort: 8000

          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"

            limits:
              cpu: "500m"
              memory: "256Mi"

          readinessProbe:
            httpGet:
              path: /health
              port: 8000

            initialDelaySeconds: 5
            periodSeconds: 10
```

---

## Step 7 — Create Service

`service.yaml`

```yaml
apiVersion: v1
kind: Service

metadata:
  name: fastapi-service

spec:
  selector:
    app: fastapi

  ports:
    - port: 80
      targetPort: 8000

  type: NodePort
```

---

## Step 8 — Deploy

```bash
kubectl apply -f deployment.yaml
```

```bash
kubectl apply -f service.yaml
```

Check:

```bash
kubectl get pods
```

```bash
kubectl get services
```

---

# 40. Understand the Complete Flow

After deploying the application:

```text
                  Kubernetes Cluster
                         |
                  Deployment
                         |
             +-----------+-----------+
             |           |           |
            Pod         Pod         Pod
             |           |           |
          FastAPI     FastAPI     FastAPI
             \           |           /
              \          |          /
                  Service
                     |
                  Client
```

If a Pod crashes:

```text
Pod crashes
     ↓
Deployment notices
     ↓
Replacement Pod
     ↓
Application continues
```

If traffic increases:

```text
Traffic
   ↓
HPA
   ↓
More Pods
   ↓
More capacity
```

If a new version is deployed:

```text
v1 Pods
   ↓
Rolling Update
   ↓
v2 Pods
```

If v2 fails:

```text
Rollback
   ↓
v1
```

This is the core idea behind Kubernetes.

---

# 41. Kubernetes Mental Model

The most important concept to remember is:

> **You tell Kubernetes what you want, and Kubernetes continuously works to make the cluster match that desired state.**

For example:

```yaml
replicas: 3
```

means:

```text
Desired State:
3 Pods
```

Kubernetes continuously checks:

```text
Desired = 3
Current = 3

Everything OK
```

If:

```text
Desired = 3
Current = 2
```

Kubernetes attempts to create another Pod.

This is the fundamental idea behind Kubernetes' declarative model.

---

# 42. What You Should Know Before Calling Yourself Kubernetes-Ready

You don't need to memorize every Kubernetes object.

You should be comfortable with:

```text
✓ Docker
✓ Containers
✓ Kubernetes architecture
✓ Pods
✓ Deployments
✓ Services
✓ Labels and Selectors
✓ Namespaces
✓ ConfigMaps
✓ Secrets
✓ Volumes
✓ kubectl
✓ YAML
✓ Scaling
✓ Rolling Updates
✓ Rollbacks
✓ Health Checks
✓ Resource Requests/Limits
✓ Jobs/CronJobs
✓ Ingress
✓ Basic Networking
✓ Basic RBAC
✓ AKS
✓ Container Registry
✓ CI/CD
```

For an AI/ML Engineer, additionally understand:

```text
✓ Dockerizing ML applications
✓ Model serving
✓ Kubernetes Deployments
✓ GPU workloads
✓ Batch inference
✓ Autoscaling
✓ Monitoring
✓ CI/CD for ML services
✓ Azure AKS
✓ Azure Container Registry
```

---

# 43. Final Summary

Kubernetes is a **container orchestration platform**.

Docker helps you package and run applications as containers.

Kubernetes helps you manage those containers reliably at scale.

The core flow to remember is:

```text
Code
 ↓
Dockerfile
 ↓
Docker Image
 ↓
Container Registry
 ↓
Kubernetes Deployment
 ↓
Pods
 ↓
Service
 ↓
Users
```

And the production mindset is:

```text
                         Kubernetes
                             |
       +---------------------+---------------------+
       |                     |                     |
   Deployment             Service              Config
       |                     |                     |
      Pods                Networking          ConfigMap
       |                                         |
   Containers                                  Secret
       |
   Application
```

For your Azure learning path, the natural progression is:

```text
Docker
   ↓
Kubernetes Basics
   ↓
kubectl + YAML
   ↓
Deploy FastAPI
   ↓
Services + Ingress
   ↓
Scaling + Health Checks
   ↓
Azure Container Registry
   ↓
Azure Kubernetes Service (AKS)
   ↓
CI/CD
   ↓
Production AI/ML Deployment
```

The goal is not simply to memorize Kubernetes commands. The goal is to understand **why each Kubernetes component exists, how the components communicate, and how Kubernetes turns containerized applications into reliable production services.**