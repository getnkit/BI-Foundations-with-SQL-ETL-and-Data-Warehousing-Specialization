# Task 1.1 - Define DAG arguments
from datetime import datetime, timedelta
from airflow import DAG

default_args = {
    'owner': 'dummy_name',
    'start_date': datetime.today(),
    'email': ['dummy_email@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 1.2 - Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval='@daily',
)

# Task 1.3 - Create a task to unzip data
from airflow.operators.bash import BashOperator

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags',
    dag=dag,
)

# Task 1.4 - Create a task to extract data from csv file
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="""
    cut -d',' -f1,2,3,4 /home/project/airflow/dags/vehicle-data.csv > /home/project/airflow/dags/csv_data.csv
    """,
    dag=dag,
)

# Task 1.5 - Create a task to extract data from tsv file
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="""
    cut -d$'\t' -f5,6,7 /home/project/airflow/dags/tollplaza-data.tsv > /home/project/airflow/dags/tsv_data.csv
    """,
    dag=dag,
)

# Task 1.6 - Create a task to extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="""
    awk '{print substr($0, 10, 5), substr($0, 15, 5)}' /home/project/airflow/dags/payment-data.txt > /home/project/airflow/dags/fixed_width_data.csv
    """,
    dag=dag,
)

# Task 1.7 - Create a task to consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="""
    paste -d ',' /home/project/airflow/dags/csv_data.csv /home/project/airflow/dags/tsv_data.csv /home/project/airflow/dags/fixed_width_data.csv > /home/project/airflow/dags/extracted_data.csv
    """,
    dag=dag,
)

# Task 1.8 - Transform and load the data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="""
    awk -F',' '{OFS=","; $4=toupper($4); print $0}' /home/project/airflow/dags/extracted_data.csv > /home/project/airflow/dags/transformed_data.csv
    """,
    dag=dag,
)

# Task 1.9 - Define the task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data






