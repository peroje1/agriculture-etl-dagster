import pandas as pd
from pandas_transformation import transform_agriculture_data

file_path = r"D:\agriculture\data\sample_crop_yield.csv"
df = pd.read_csv(file_path)

aggregated_results = transform_agriculture_data(df)

print(aggregated_results['avg_yield_by_crop'])
print(aggregated_results['yield_pivot_region_crop'])
