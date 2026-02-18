def task_d():
    print("All done")

with DAG(
    dag_id="day1_simple_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    a = PythonOperator(
        task_id="task_a",
        python_callable=task_a,
    )

    b = PythonOperator(
        task_id="task_b",
        python_callable=task_b,
    )

    c = PythonOperator(
        task_id="task_c",
        python_callable=task_c,
    )

    d = PythonOperator(
        task_id="task_d",
        python_callable=task_d,
    )

    a >> [b, c]
    [b, c] >> d
