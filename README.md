# 🐳 Docker-AWS-ECR

This repository contains Docker practice examples and deployment steps related to AWS Elastic Container Registry (ECR).

---

## 📦 What is Docker?

Docker is a tool to **build, package, and run applications** inside lightweight, isolated containers.

---

## ❓ Why Docker?

Docker helps you run apps **consistently across environments**, removes **dependency issues**, and is faster than virtual machines.

---

## 🌍 Where is Docker Used?

Used in **development**, **testing**, **CI/CD pipelines**, and **production** for microservices, cloud-native apps, and DevOps automation.

---

## ⚙️ How Docker Works?

You write instructions in a `Dockerfile`, build an image, then run containers using:

```bash
docker build -t my_app .
docker run my_app
```

---

---

## 🐘 What is AWS ECR?

**Amazon Elastic Container Registry (ECR)** is a **secure**, **fully managed** Docker image registry that integrates with **AWS IAM**, **ECS**, **EKS**, and CI/CD tools.

### 🔐 Benefits:

* Access control via IAM
* Image scanning for vulnerabilities
* High availability and scalability

---

## 📁 Repository Structure

```
.
├── docker_exercises/        # Hands-on Docker examples (see its README)
├── ecr/                     # AWS ECR-specific Dockerfiles and scripts
│   ├── Dockerfile
│   ├── index.html
│   └── ecr_push_script.sh
└── README.md                # Project overview
```

---

## 🚀 How to Push to AWS ECR

1. **Authenticate Docker to ECR:**

   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t my_first_ecr .
   ```

3. **Tag the image for ECR:**

   ```bash
   docker tag my_first_ecr:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_first_ecr
   ```

4. **Push the image to ECR:**

   ```bash
   docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my_first_ecr
   ```

---

## 🔒 Security Tip

Do **not** hard-code or share ECR credentials. Use `aws configure`, IAM roles, or environment variables. For Git operations, configure [credential helpers](https://git-scm.com/docs/gitcredentials) securely.
