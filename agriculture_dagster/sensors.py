import os
from dagster import sensor, RunRequest
from agriculture_dagster.jobs import agriculture_etl_job

WATCH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))

seen_files = set()

@sensor(job=agriculture_etl_job)
def new_csv_sensor(context):
    new_runs = []
    if not os.path.exists(WATCH_DIR):
        context.log.info(f"Directory not found: {WATCH_DIR}")
        return []

    for filename in os.listdir(WATCH_DIR):
        if filename.endswith(".csv") and filename not in seen_files:
            seen_files.add(filename)
            context.log.info(f"New file detected: {filename}")
            new_runs.append(RunRequest(run_key=filename, run_config={}))

    return new_runs
