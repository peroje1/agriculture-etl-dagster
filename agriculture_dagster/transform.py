from dagster import op, Out, Output
import pandas as pd
import numpy as np

@op(out=Out(description="Aggregated metrics as a dictionary of DataFrames"))
def transform_data(df: pd.DataFrame) -> dict:
    df['Rainfall_mm'] = df['Rainfall_mm'].astype(float)
    df['Fertilizer_Used'] = df['Fertilizer_Used'].astype(float)
    df['Irrigation_Used'] = df['Irrigation_Used'].astype(float)
    df['Temperature_Celsius'] = df['Temperature_Celsius'].astype(float)
    df['Days_to_Harvest'] = df['Days_to_Harvest'].astype(float)

    df['Rainfall_Level'] = pd.cut(df['Rainfall_mm'], bins=[-np.inf, 300, 600, np.inf], labels=['Low', 'Medium', 'High'])
    df['Fertilizer_Level'] = pd.cut(df['Fertilizer_Used'], bins=[-np.inf, 100, 200, np.inf], labels=['Low', 'Medium', 'High'])
    df['Harvest_Duration'] = pd.cut(df['Days_to_Harvest'], bins=[-np.inf, 90, 150, np.inf], labels=['Short', 'Medium', 'Long'])
    df['Temperature_Level'] = pd.cut(df['Temperature_Celsius'], bins=[-np.inf, 15, 25, np.inf], labels=['Low', 'Medium', 'High'])
    df['Irrigation_Flag'] = np.where(df['Irrigation_Used'] > 0, 'Yes', 'No')
    df['Drought_Flag'] = np.where(df['Rainfall_mm'] < 150, 'Yes', 'No')
    df['Heat_Stress_Flag'] = np.where(df['Temperature_Celsius'] > 30, 'Yes', 'No')

    df['Yield_per_kg_fertilizer'] = df['Yield_tons_per_hectare'] / df['Fertilizer_Used'].replace(0, np.nan)
    df['Yield_per_irrigation'] = df['Yield_tons_per_hectare'] / df['Irrigation_Used'].replace(0, np.nan)
    df['Yield_Rank_by_Region'] = df.groupby('Region')['Yield_tons_per_hectare'].rank(ascending=False)

    results = {
        'avg_yield_by_crop': df.groupby('Crop')['Yield_tons_per_hectare'].mean().reset_index(),
        'avg_yield_by_region': df.groupby('Region')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_rainfall_level': df.groupby('Rainfall_Level')['Yield_tons_per_hectare'].mean().reset_index(),
        'avg_yield_by_crop_weather': df.groupby(['Crop', 'Weather_Condition'])['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_soil_type': df.groupby('Soil_Type')['Yield_tons_per_hectare'].mean().reset_index(),
        'fertilizer_vs_yield': df.groupby('Fertilizer_Level')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_crop_region': df.groupby(['Crop', 'Region'])['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_harvest_duration': df.groupby('Harvest_Duration')['Yield_tons_per_hectare'].mean().reset_index(),
        'rainfall_fert_yield': df.groupby(['Rainfall_Level', 'Fertilizer_Level'])['Yield_tons_per_hectare'].mean().reset_index(),
        'avg_yield_by_temperature_level': df.groupby('Temperature_Level')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_irrigation_flag': df.groupby('Irrigation_Flag')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_drought_flag': df.groupby('Drought_Flag')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_by_heat_stress_flag': df.groupby('Heat_Stress_Flag')['Yield_tons_per_hectare'].mean().reset_index(),
        'yield_pivot_region_crop': df.pivot_table(index='Region', columns='Crop', values='Yield_tons_per_hectare', aggfunc='mean')
    }

    return results
