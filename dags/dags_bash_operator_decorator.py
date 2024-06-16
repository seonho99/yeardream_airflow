import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_bash_operator_decorator',
    schedule='0 13 6 * 0#2',
    start_date=datetime.datetime(2024, 5, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=9))),
    catchup=False
):
    EmptyOperator(tag="homework")