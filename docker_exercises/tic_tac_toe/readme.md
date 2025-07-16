## 🎮 tic\_tac\_toe (Dockerized Python Game)

A simple **Tic Tac Toe** game written in Python and containerized with Docker. Ideal for beginners learning Docker with Python applications.

---

### 📁 Project Structure

```
tic_tac_toe/
├── Dockerfile
└── tic_tac_toe.py
```

---

### 🐍 Game Description

This is a terminal-based 2-player Tic Tac Toe game. It’s an interactive CLI application written in Python.

---

### 🐳 Docker Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/Shaikhabdulh/Docker-AWS-ECR.git
cd Docker-AWS-ECR/docker_exercises/tic_tac_toe
```

#### 2. Build the Docker image

```bash
docker build -t tic_tac_toe .
```

#### 3. Run the game container

```bash
docker run -it tic_tac_toe
```

> `-it` is used to run in interactive mode so you can play in the terminal.

---

### 🧾 Dockerfile Summary

* **Base Image**: Python (e.g., `python:3.10-slim`)
* **Copy**: Game script into container
* **Run**: Game directly when container starts

---

### 🧠 Learning Goals

* Write a basic Dockerfile for Python apps
* Understand interactive container execution
* Run terminal apps inside Docker containers
