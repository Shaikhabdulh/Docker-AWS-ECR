

### 📁 `docker_exercises`

This repository contains hands-on Docker exercises to understand image creation, containerization, and deployment using minimal and real-world apps.

---

## 📂 Folder Structure

```
docker_exercises/
│
├── simple_lightweight-alpine/   # Minimal Alpine-based image
└── tic_tac_toe/                  # Python Tic Tac Toe game in Docker
```

---

## 🚀 Projects

### 1. `simple_lightweight-alpine`

**📌 Description:**
A simple Dockerfile using the Alpine Linux base image. Great for learning how to create lightweight containers.

**🛠️ Contents:**

* `Dockerfile` — installs basic utilities and runs a minimal command.

**📦 How to Use:**

```bash
cd simple_lightweight-alpine
docker build -t alpine_app .
docker run alpine_app
```

---

### 2. `tic_tac_toe`

**📌 Description:**
A CLI-based Python Tic Tac Toe game containerized using Docker.

**🛠️ Contents:**

* `app.py` — Python script for the game
* `Dockerfile` — defines Python runtime environment

**📦 How to Use:**

```bash
cd tic_tac_toe
docker build -t tic_tac_toe .
docker run -it tic_tac_toe
```

---

## 🧾 Prerequisites

* Docker installed and running
* Basic knowledge of CLI and Python (for `tic_tac_toe`)

---

## 📘 Why This Repo?

This repo is designed to:

* Teach Docker basics hands-on
* Showcase real examples from scratch
* Improve containerization and image optimization understanding

---

Let me know if you'd like to add a `.gitignore`, license, or CI workflow!
