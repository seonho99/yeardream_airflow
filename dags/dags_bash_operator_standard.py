import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_bash_operator_standard',
    schedule='0 9 1/6 * *',
    start_date=datetime.datetime(2024, 6, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=9))),
    catchup=False
):
    EmptyOperator(tag="homework")
