import pandas as pd

file_path = "D:/etl_agriculture/sample_crop_yield.csv"
df = pd.read_csv(file_path)

df.info()

df.describe(include='all')

#checking for nulls and duplicates
print(df.isnull().sum())
print((df == '').sum())
print("Duplicate rows:", df.duplicated().sum())

#fertilizer and irrigation used to bool
df["Fertilizer_Used"] = df["Fertilizer_Used"].astype(bool)
df["Irrigation_Used"] = df["Irrigation_Used"].astype(bool)

#nulls
df.isnull().sum()
df.dropna(inplace=True)

#duplicates
df = df.drop_duplicates()

#checking unique values
print("Regions:", df["Region"].unique())
print("Soil Types:", df["Soil_Type"].unique())
print("Crops:", df["Crop"].unique())
print("Weather Conditions:", df["Weather_Condition"].unique())

#clean data
df.to_csv("D:/etl_agriculture/sample_crop_yield_clean.csv", index=False)