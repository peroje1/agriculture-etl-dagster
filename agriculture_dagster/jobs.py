from agriculture_dagster.extract import extract_data
from agriculture_dagster.clean import clean_data
from agriculture_dagster.transform import transform_data
from agriculture_dagster.load import load_to_mysql
from dagster import job

@job
def agriculture_etl_job():
    raw = extract_data()
    cleaned = clean_data(raw)
    transformed = transform_data(cleaned)
    load_to_mysql(transformed)
