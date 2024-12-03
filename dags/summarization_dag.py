from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks.scraper import scrape_and_clean_text
from tasks.model_summarize import summarize_text
from tasks.save_to_sql import save_to_sql
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 1),
    'retries': 1, 
}

# def scrape():
    # os.system("python /PROJECT-PEMROG/tasks/scraper.py")
# 
# def summarize():
    # os.system("python /PROJECT-PEMROG/tasks/model_summarixe.py")
# 
# def save():
    # os.system("python /PROJECT-PEMROG/tasks/save_to_sql.py")

with DAG(
    'daily_text_summarization',
    default_args=default_args, 
    schedule_interval='@daily',
    catchup=False  
) as dag:

    scrape_task = PythonOperator(
        task_id='scrape_data',
        python_callable=scrape_and_clean_text  
    )

    summarize_task = PythonOperator(
        task_id='summarize_texts',
        python_callable=summarize_text
    )

    save_task = PythonOperator(
        task_id='save_to_sql',
        python_callable=save_to_sql
    )

    scrape_task >> summarize_task >> save_task
