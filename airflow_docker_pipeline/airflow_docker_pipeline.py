from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data into BigQuery...")

with DAG("simple_etl_dag", start_date=datetime(2025, 3, 7), schedule_interval="@daily", catchup=False) as dag:

    task1 = PythonOperator(task_id="extract", python_callable=extract)
    task2 = PythonOperator(task_id="transform", python_callable=transform)
    task3 = PythonOperator(task_id="load", python_callable=load)

    task1 >> task2 >> task3
