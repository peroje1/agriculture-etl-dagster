from dagster import op, Out, Output
import pandas as pd

@op(out=Out(description="Cleaned DataFrame with no nulls or duplicates"))
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df["Fertilizer_Used"] = df["Fertilizer_Used"].astype(bool)
    df["Irrigation_Used"] = df["Irrigation_Used"].astype(bool)
    df = df.dropna()
    df = df.drop_duplicates()

    print("Regions:", df["Region"].unique())
    print("Soil Types:", df["Soil_Type"].unique())
    print("Crops:", df["Crop"].unique())
    print("Weather Conditions:", df["Weather_Condition"].unique())

    return df
