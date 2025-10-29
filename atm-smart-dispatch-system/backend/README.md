# ATM Smart Dispatch System Backend

This repository contains the backend for the AI-powered ATM Smart Dispatch System. It is built with FastAPI and uses Elasticsearch as its core data and intelligence engine.

## ⚙️ Tech Stack

- **FastAPI**: For the web framework.
- **Elasticsearch**: For data storage, search, and analytics.
- **Redis**: For caching and real-time messaging (placeholder).
- **APScheduler**: For running scheduled background jobs.
- **Docker & Docker Compose**: For containerization and local setup.

## 🚀 Getting Started

Follow these instructions to get the backend running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following software installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd atm-smart-dispatch-system/backend
    ```

2.  **Create an environment file**:
    Copy the example environment file to a new `.env` file. The default values are configured for the `docker-compose` setup and should work out of the box.
    ```bash
    cp .env.example .env
    ```

3.  **Build and run the application with Docker Compose**:
    This command will build the Docker images for the backend, Elasticsearch, and Redis, and then start the services.
    ```bash
    docker-compose up --build
    ```
    - The `--build` flag ensures that the image is rebuilt if there are any changes.
    - It might take a minute for Elasticsearch to start up. You can monitor the logs in your terminal.

4.  **Access the application**:
    Once the containers are running, the FastAPI application will be available at `http://localhost:8000`.

## 📚 API Documentation

FastAPI automatically generates interactive API documentation. Once the application is running, you can access it at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

From the Swagger UI, you can interact with the API endpoints, send requests, and see the responses.

## ✅ How to Test the Endpoints

Here are a few `curl` examples to test the key endpoints from your terminal.

### 1. Create a new Engineer

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/engineers/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "engineer_id": "eng99",
  "name": "Test Engineer",
  "skills": [
    "Cash Dispenser"
  ],
  "location": [
    40.7128,
    -74.0060
  ],
  "is_available": true
}'
```

### 2. Ingest an ATM Log

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/logs/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "atm_id": "atm123",
  "timestamp": "2023-10-27T10:00:00Z",
  "event_type": "Error",
  "details": {
    "error_code": "E-45-2",
    "description": "Cash dispenser jam"
  }
}'
```

### 3. Create a Dispatch to get an Engineer assigned

This will create a dispatch request for an ATM that needs a "Cash Dispenser" skill. The system will find an available engineer (like Alice or the Test Engineer you created) and assign them.

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/dispatches/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "atm_id": "atm123",
  "description": "The cash dispenser is jammed and requires an expert.",
  "required_skill": "Cash Dispenser"
}'
```

You will get a response that includes the details of the engineer who was assigned.
