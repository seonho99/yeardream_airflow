import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_bash_operator_standard',
    schedule='0 9 1/6 * *'
    start_date=datetime(2024, 6, 1, tz='Asia/Seoul'),
    catchup=False
):
    EmptyOperator(task_id="task")