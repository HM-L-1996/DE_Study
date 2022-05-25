#pip3 install apache-airflow-providers-apache-spark
from airflow import DAG

from datetime import datetime
# from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
default_args={
    'start_date':datetime(2021,1,1)
}

with DAG(dag_id="spark-example",
        schedule_interval="@daily",
        default_args=default_args,
        tags=['spark'],
        catchup=False) as dag:

    submit_job = SparkSubmitOperator(
        application="/Users/ihyeonmin/Desktop/study/data-engineering/01-spark/count_trips_sql.py",
        task_id="submit_job",
        conn_id="spark_local"
    )
    # submit_job = BashOperator(
    #     task_id='submit_job',
    #     bash_command='spark-submit --master local --name arrow-spark /Users/ihyeonmin/Desktop/study/data-engineering/01-spark/count_trips_sql.py'
    # )