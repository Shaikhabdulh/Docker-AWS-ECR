## 🐳 simple\_lightweight-alpine

A minimal Docker example using the **Alpine Linux** base image — ideal for lightweight container builds and quick experiments.

---

### 📁 Project Structure

```
simple_lightweight-alpine/
├── Dockerfile
```

---

### 📦 What It Does

* Uses a small Alpine base image (`alpine:latest`)
* Installs essential utilities (customize as needed)
* Builds a minimal Docker image for experimentation or base use

---

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/docker_exercises/simple_lightweight-alpine
```

#### 2. Build the Docker image

```bash
docker build -t alpine_demo .
```

#### 3. Run the container

```bash
docker run -it alpine_demo
```

---

### 🔧 Basic Docker Commands

| Command                             | Description                             |
| ----------------------------------- | --------------------------------------- |
| `docker build -t <image_name> .`    | Build Docker image from Dockerfile      |
| `docker images`                     | List all local images                   |
| `docker ps`                         | List running containers                 |
| `docker ps -a`                      | List all containers (running + stopped) |
| `docker run -it <image_name>`       | Run container in interactive mode       |
| `docker stop <container_id>`        | Stop a running container                |
| `docker rm <container_id>`          | Remove a container                      |
| `docker rmi <image_name>`           | Remove an image                         |
| `docker exec -it <container_id> sh` | Execute shell in running container      |
| `docker logs <container_id>`        | View container logs                     |

---

### 🧊 Why Alpine?

* 🔹 Ultra-lightweight (\~5 MB)
* 🔒 Security-focused
* ⚡ Fast startup
* 🧰 Great for microservices or scratch builds

---

### 🎯 Learning Goals

* Write a basic `Dockerfile`
* Understand how to build and run minimal containers
* Use Alpine for performance-focused Docker images
