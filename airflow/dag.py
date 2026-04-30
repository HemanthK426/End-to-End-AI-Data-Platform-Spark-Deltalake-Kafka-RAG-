from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG("spark_delta_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@daily")

bronze = BashOperator(
    task_id="bronze_ingestion",
    bash_command="python notebooks/01_bronze_ingestion.py",
    dag=dag
)

silver = BashOperator(
    task_id="silver_transformation",
    bash_command="python notebooks/02_silver_transformation.py",
    dag=dag
)

gold = BashOperator(
    task_id="gold_aggregation",
    bash_command="python notebooks/03_gold_aggregation.py",
    dag=dag
)

bronze >> silver >> gold