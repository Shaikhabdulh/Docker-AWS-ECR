# 📦 AWS ECR (Elastic Container Registry)

This section provides hands-on guidance to **build, tag, push, pull, and run Docker images using AWS Elastic Container Registry (ECR)**. It is designed for cloud-native DevOps workflows and integration with services like EC2, ECS, and CI/CD pipelines.

---

## 🐘 What is AWS ECR?

**Amazon Elastic Container Registry (ECR)** is a fully managed Docker-compatible image registry service by AWS. It allows you to:

- Store and manage Docker container images securely
- Integrate with AWS services (ECS, EC2, Lambda, CodeBuild, etc.)
- Control access using **fine-grained IAM policies**
- Avoid dependency on public registries

---

## ❓ Why Use ECR?

| ✅ Reason           | 🌐 Benefit                                                                 |
|---------------------|---------------------------------------------------------------------------|
| Secure Hosting       | Private container image storage with encryption at rest                  |
| AWS Integration      | Seamless with ECS, EC2, CodePipeline, CodeBuild, etc.                    |
| Fine-Grained Control | Manage access using IAM users, roles, and permissions                    |
| Cost-Effective       | Free 500MB/month storage in Free Tier                                    |
| Region-Specific      | Faster access within same AWS region                                     |

---

## ⚙️ How AWS ECR Works (Step-by-Step)

```bash
# Step 1: Authenticate Docker to your AWS account
aws ecr get-login-password --region <region> | \
docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

# Step 2: Tag your image with the ECR repository URI
docker tag my_app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_app:latest

# Step 3: Push the Docker image to your ECR repository
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_app:latest

# Step 4: Pull the image on any other host
docker pull <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_app:latest

# Step 5: Run the image
docker run -d -p 8080:80 <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_app:latest
```

---

## 🔁 Docker Hub vs AWS ECR (Free Tier Comparison)

| Feature               | Docker Hub (Free)               | AWS ECR (Free Tier)                         |
|-----------------------|----------------------------------|---------------------------------------------|
| Private Repositories  | 1 repo                          | Unlimited (up to 500MB total/month)         |
| Region Scope          | Global                          | Region-specific                             |
| Access Control        | Basic (team-based)              | IAM-based (fine-grained)                    |
| Native Integration    | Limited                         | Native AWS services                         |
| Pricing After Limits  | $7/month for Pro plan           | Pay-as-you-go per GB stored & transferred   |

---

## 📁 Folder Structure

```
ecr/
├── Dockerfile           # Sample Dockerfile (e.g. for Nginx)
├── index.html           # Sample static webpage to serve via Nginx
├── ecr_push_script.sh   # (Optional) Bash script to automate login/tag/push
```

---

## ✅ GitHub Clone & Get Started

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/ecr
```

---

## 🔧 File Contents

### `Dockerfile`
```dockerfile
# Use official Nginx image as the base
FROM nginx:alpine

# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy our custom static page
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for web traffic
EXPOSE 80
```

### `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello from ECR</title>
</head>
<body>
    <h1>Welcome to Nginx served via Docker and AWS ECR!</h1>
    <p>This static site is containerized and stored in ECR.</p>
</body>
</html>
```

### `ecr_push_script.sh`
```bash
#!/bin/bash

# CONFIGURATION
REGION="us-east-1"
ACCOUNT_ID="123456789012"
REPO_NAME="my_nginx_ecr"
IMAGE_TAG="latest"

# Step 1: Authenticate Docker to ECR
aws ecr get-login-password --region $REGION | \
docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Step 2: Build Docker image
docker build -t $REPO_NAME .

# Step 3: Tag Docker image for ECR
docker tag $REPO_NAME:$IMAGE_TAG $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG

# Step 4: Push to ECR
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG
```

> 🔐 Ensure that your AWS CLI is configured properly with `aws configure`.

## Useful Links:
- AWS ECR Docs: https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html
- AWS CLI ECR Auth: https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html
```
