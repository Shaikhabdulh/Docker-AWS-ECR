# 🐳 docker_exercises

This repository contains hands-on Docker exercises to understand image creation, containerization, and deployment using minimal and real-world applications.

---

## 📂 Folder Structure

```

docker\_exercises/
│
├── simple\_lightweight-alpine/   # Minimal Alpine-based image
├── tic\_tac\_toe/                 # Python Tic Tac Toe game in Docker
└── custom\_nginx\_site/          # Serve custom static HTML via Nginx container

````

---

## 🚀 Projects

### 1. `simple_lightweight-alpine`

**📌 Description:**
A basic Dockerfile using the Alpine Linux image. Ideal for learning lightweight image creation.

**🛠️ Contents:**
- `Dockerfile` — Installs basic utilities and runs a minimal command.

**📦 How to Use:**
```bash
cd simple_lightweight-alpine
docker build -t alpine_app .
docker run alpine_app
````

---

### 2. `tic_tac_toe`

**📌 Description:**
A CLI-based Python Tic Tac Toe game containerized with Docker.

**🛠️ Contents:**

* `tic_tac_toe.py` — Python game script
* `Dockerfile` — Defines Python environment

**📦 How to Use:**

```bash
cd tic_tac_toe
docker build -t tic_tac_toe .
docker run -it tic_tac_toe
```

---

### 3. `custom_nginx_site`

**📌 Description:**
A project to build a Docker image using Nginx to serve a custom static HTML page.

**🛠️ Contents:**

* `Dockerfile` — Based on `nginx:alpine`, replaces default content
* `index.html` — Custom static webpage

**📦 How to Use:**

```bash
cd custom_nginx_site
docker build -t custom-nginx-site .
docker run -d -p 8080:80 custom-nginx-site
```

---

## 🧾 Prerequisites

* Docker installed and running
* Basic terminal usage
* Python knowledge for `tic_tac_toe` project
* Browser access for testing `custom_nginx_site`

---

## 🐳 What, Why, Where & How of Docker

---

### ✅ What is Docker?

Docker is a tool that lets you **package applications and dependencies** into lightweight containers that run consistently across environments.

---

### 🔍 Why Docker?

| Benefit            | Explanation                                        |
| ------------------ | -------------------------------------------------- |
| 🧩 Isolation       | Keeps apps in separate containers, no interference |
| 🧱 Consistency     | Works the same in dev, test, and prod              |
| ⚡ Lightweight      | Less overhead than full VMs                        |
| 🚀 Speed           | Fast startup and execution                         |
| 🔁 Reproducibility | Ensures same result every time via Dockerfiles     |
| ☁️ Cloud-Ready     | Designed for microservices and distributed apps    |

---

### 🌍 Where Docker is Used?

* **Development**: Clean dev environments
* **Testing**: Test different versions/OS easily
* **Production**: Scale services using Kubernetes or Docker Swarm
* **DevOps/MLOps**: CI/CD, model deployment, container orchestration
* **Training/Labs**: Isolated safe environments

---

### 🛠️ How Docker Works (Basic Flow)

1. Create a `Dockerfile` to define environment and app
2. Build the Docker image:

   ```bash
   docker build -t my_app .
   ```
3. Run a container from the image:

   ```bash
   docker run -it my_app
   ```

Each container runs in isolation but uses the host OS kernel.

---

### 🆚 Docker vs Traditional Setup

| Feature              | Docker (Containers)            | Traditional (VMs/Host Setup)  |
| -------------------- | ------------------------------ | ----------------------------- |
| Startup Time         | Seconds                        | Minutes                       |
| Resource Usage       | Low (shares kernel)            | High (full OS in each VM)     |
| Portability          | Runs anywhere Docker runs      | Depends on OS/environment     |
| Dependency Conflicts | Avoided via isolation          | Common when shared OS is used |
| Ease of Maintenance  | Easy rebuilds, version control | Manual fixes and patches      |

---

## 📥 Clone This Repository

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/docker_exercises
```
## 📌 Takeaways from this Exercise

This exercise introduces practical usage of Docker to build images, run containers, serve static websites, and containerize Python applications — all in lightweight and reproducible ways.

---

# 🧰 Basic Docker Commands

These commands help manage Docker images, containers, and interactions effectively.

### 📦 Image Management

| Command                           | Description                          |
| --------------------------------- | ------------------------------------ |
| `docker --version`                | Show Docker version                  |
| `docker images`                   | List all local Docker images         |
| `docker build -t <image_name> .`  | Build Docker image from Dockerfile   |
| `docker rmi <image_id>`           | Remove an image                      |
| `docker pull <image>`             | Download image from Docker Hub       |
| `docker tag <image> <repo>:<tag>` | Tag image before pushing             |
| `docker push <repo>:<tag>`        | Push image to Docker Hub or registry |

---

### 🧪 Container Lifecycle

| Command                            | Description                                  |
| ---------------------------------- | -------------------------------------------- |
| `docker ps`                        | List running containers                      |
| `docker ps -a`                     | List all containers (including stopped ones) |
| `docker run <image>`               | Run container from image                     |
| `docker run -it <image>`           | Run with interactive shell                   |
| `docker run -d -p 8080:80 <image>` | Run in detached mode with port mapping       |
| `docker stop <container_id>`       | Stop a running container                     |
| `docker rm <container_id>`         | Remove a container                           |

---

### 🔧 Debug & Inspection

| Command                             | Description                   |
| ----------------------------------- | ----------------------------- |
| `docker exec -it <container_id> sh` | Access shell inside container |
| `docker logs <container_id>`        | View logs from a container    |
| `docker inspect <container_id>`     | View container details        |

---

### 💡 Pro Tips

* 🧹 `docker system prune -a`: Remove all unused containers/images/networks
* 📄 `docker network ls`, `docker volume ls`: Manage networks and volumes
* 📁 Use `.dockerignore` to speed up builds by ignoring unnecessary files
