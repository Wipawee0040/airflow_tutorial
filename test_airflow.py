def greeting():
    return "Hello, Airflow!"

def yourname(**kwargs):
    ti = kwargs['ti']
    name = ti.xcom_pull(task_ids='hello_task')
    print(f"I'am Choco, your Airflow assistant! {name}!")

