from dagster import op, In, Out, Output
import pandas as pd
import os

@op(
    out=Out(description="Raw DataFrame from the CSV file"),
    description="Loads the latest weekly crop yield CSV from the data folder"
)
def extract_data() -> pd.DataFrame:
    data_dir = "data"
    filename = "sample_crop_yield.csv"
    file_path = os.path.join(data_dir, filename)

    df = pd.read_csv(file_path)
    return df
