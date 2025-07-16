# 🌐 Custom Nginx Site with Docker

This project demonstrates how to build a **custom Nginx Docker container** that serves a personalized HTML web page.

---

## 📘 What Is This?

This is a Docker-based project that:
- Uses the official lightweight `nginx:alpine` image
- Replaces Nginx's default content with your own HTML file
- Runs an HTTP web server inside a container

---

## ❓ Why We Do This?

- 🧱 To understand how to customize Docker images
- 🧪 Learn to serve static content via Nginx in containers
- 🚀 Practice containerization for front-end/static sites
- 🔁 Gain confidence working with Dockerfile basics

---

## 🌍 Where It’s Used

- Hosting static websites or landing pages
- Web app frontends inside Docker containers
- Dev/test environments for UI preview
- Nginx reverse proxy or frontend with custom assets

---

## ⚙️ How It Works

### Folder Structure

```

custom\_nginx\_site/
├── Dockerfile
└── index.html

````

---

### Dockerfile

```Dockerfile
# Use official Nginx image based on Alpine Linux
FROM nginx:alpine

# Optional: Clean default web files
RUN rm -rf /usr/share/nginx/html/*

# Copy your custom HTML into Nginx's web root
COPY index.html /usr/share/nginx/html/

# Expose port 80 for HTTP traffic
EXPOSE 80

# CMD is already defined in nginx:alpine: "nginx -g 'daemon off;'"
````

---

### index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Custom Nginx Site</title>
</head>
<body>
    <h1>🚀 Welcome to My Dockerized Nginx Site!</h1>
    <p>Task: Day 17 - Create Dockerfile for custom Nginx site</p>
    <p>By: Shaikh Abdul Hamid</p>
</body>
</html>
```

---

## 🚀 How to Run

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/docker_exercises/custom_nginx_site
```

### 🛠️ Step 2: Build the Docker Image

```bash
docker build -t custom-nginx-site .
```

### ▶️ Step 3: Run the Docker Container

```bash
docker run -d -p 8080:80 custom-nginx-site
```

### 🌐 Step 4: Access in Browser

Open your browser and go to:

```
http://localhost:8080
```

You should see a welcome message from your custom Nginx Docker container.

---

## 📚 Summary

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| Base Image     | `nginx:alpine` (lightweight and fast)         |
| Port Exposed   | `80` (mapped to `8080` on host)               |
| Purpose        | Serve a custom HTML page using Nginx + Docker |
| Author         | Shaikh Abdul Hamid                            |
| Task Reference | Day 17 Task 2 - Dockerfile for custom Nginx   |

---

Feel free to extend this with CSS, JS, or host it on AWS using ECR + ECS!
