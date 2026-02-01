# Docker Lab: Multi-Container Application

## Overview

This project demonstrates the basics of Docker and Docker Compose by deploying
a multi-container application consisting of a web backend, reverse proxy, and database.

The goal of this lab is to practice containerization, service orchestration,
and inter-container communication in a production-like setup.

---

## Architecture
```text
Client
|
v
Nginx (Reverse Proxy)
|
v
Flask Backend
|
v
PostgreSQL Database
```
---

## Technologies Used

- Docker
- Docker Compose
- Python (Flask)
- PostgreSQL
- Nginx

---

## Project Structure
```text
docker-lab/
├── docker-compose.yml
├── README.md
├── .env
├── .dockerignore
├── backend/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── nginx/
│ ├── Dockerfile
│ └── nginx.conf
└── db/
└── init.sql
```
---

## How to Run

From the project root directory:

```bash
docker-compose up --build
```
Or with newer Docker versions:

```bash
docker compose up --build
```

---

## Available Endpoints

- `/` – returns data from PostgreSQL
- `/health` – service health check

Access the application via:
```text
http://localhost
```
---

## Key Features

- Multi-container setup using Docker Compose
- Reverse proxy with Nginx
- Backend service isolated from external access
- Persistent PostgreSQL storage using volumes
- Environment-based configuration
- Health checks for service monitoring


