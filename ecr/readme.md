# 📦 AWS ECR (Elastic Container Registry)

This section provides hands-on guidance to **build, tag, push, pull, and run Docker images using AWS Elastic Container Registry (ECR)**. It is designed for cloud-native DevOps workflows and integration with services like EC2, ECS, and CI/CD pipelines.

---

## 🐘 What is AWS ECR?

**Amazon Elastic Container Registry (ECR)** is a fully managed Docker-compatible image registry service by AWS. It allows you to:

* Store and manage Docker container images securely
* Integrate with AWS services (ECS, EC2, Lambda, CodeBuild, etc.)
* Control access using **fine-grained IAM policies**
* Avoid dependency on public registries

---

## ❓ Why Use ECR?

| ✅ Reason             | 🌐 Benefit                                              |
| -------------------- | ------------------------------------------------------- |
| Secure Hosting       | Private container image storage with encryption at rest |
| AWS Integration      | Seamless with ECS, EC2, CodePipeline, CodeBuild, etc.   |
| Fine-Grained Control | Manage access using IAM users, roles, and permissions   |
| Cost-Effective       | Free 500MB/month storage in Free Tier                   |
| Region-Specific      | Faster access within same AWS region                    |

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

| Feature              | Docker Hub (Free)      | AWS ECR (Free Tier)                       |
| -------------------- | ---------------------- | ----------------------------------------- |
| Private Repositories | 1 repo                 | Unlimited (up to 500MB total/month)       |
| Region Scope         | Global                 | Region-specific                           |
| Access Control       | Basic (team-based)     | IAM-based (fine-grained)                  |
| Native Integration   | Limited                | Native AWS services                       |
| Pricing After Limits | \$7/month for Pro plan | Pay-as-you-go per GB stored & transferred |

---

## 📁 Folder Structure

```
ecr/
├── README.md            # This documentation file
├── Dockerfile           # Sample Dockerfile (e.g. for Nginx)
├── index.html           # Sample static webpage to serve via Nginx
├── ecr_push_script.sh   # (Optional) Bash script to automate login/tag/push
└── notes.md             # Optional: notes, screenshots or manual steps
```

---

## ✅ GitHub Clone & Get Started

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/ecr
```
