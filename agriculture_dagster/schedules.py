from dagster import schedule
from datetime import time
from agriculture_dagster.jobs import agriculture_etl_job

@schedule(
    cron_schedule="0 8 * * 1", #monday at 8:00
    job=agriculture_etl_job,
    execution_timezone="Europe/Belgrade"
)
def weekly_agriculture_schedule(_context):
    return {}
