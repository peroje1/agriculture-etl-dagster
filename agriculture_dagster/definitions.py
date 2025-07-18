from dagster import Definitions
from agriculture_dagster.sensors import new_csv_sensor
from agriculture_dagster.schedules import weekly_agriculture_schedule
from agriculture_dagster.jobs import agriculture_etl_job

defs = Definitions(
    jobs=[agriculture_etl_job],
    schedules=[weekly_agriculture_schedule],
    sensors=[new_csv_sensor],
)
