from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from test_airflow import greeting
from test_airflow import yourname

with DAG (
    dag_id = 'my-dag',
    start_date = datetime(2025, 1, 1),
    schedule_interval = "@daily",
    catchup = False
) as dag:
    
    hello_task = PythonOperator(
        task_id = 'hello_task',
        python_callable = greeting
    )

    task_yourname = PythonOperator(
        task_id = 'task_yourname',
        python_callable = yourname
    )

    hello_task >> task_yourname