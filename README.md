# Onboardi

This repository contains the source code for Onboardi, a web application with a backend, frontend, and an agent component.

## Project Structure

The repository is a monorepo with the following structure:

- `src/backend`: A Django project providing the backend API.
- `src/frontend`: A Next.js project for the frontend user interface.
- `src/agent`: A Python-based agent.
- `docker-compose.yml`: Docker Compose file for running the application stack.
- `k8s`: Kubernetes deployment files.

## Getting Started

To get started with Onboardi, you can use Docker Compose to build and run the entire application.

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1.  Clone the repository:
    ```bash
    git clone https://github.com/ZEZE1020/onboardi.git
    cd onboardi-repo
    ```
2.  Build and run the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```

This will start the backend, frontend, and any other services defined in the `docker-compose.yml` file.

- The frontend will be accessible at `http://localhost:3000`.
- The backend API will be accessible at `http://localhost:8000`.

## Kubernetes

The `k8s` directory contains Kubernetes deployment files for deploying the application to a Kubernetes cluster.