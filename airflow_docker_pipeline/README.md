# Airflow ETL Pipeline - Docker
This project sets up a simple Airflow pipeline using Docker to manage ETL tasks.

## Technologies
- Apache Airflow
- Docker
- Python

## DAG Process
- Dummy extract, transform, and load steps.
- Triggered daily.
- Logs success or failure.

## Setup
- Install Docker and Docker Compose.
- Start Airflow: `docker-compose up`
- Access Airflow UI at `http://localhost:8080`.
