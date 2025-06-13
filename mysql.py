from sqlalchemy import create_engine
import pandas as pd
from pandas_transformation import transform_agriculture_data

file_path = r"D:\agriculture\data\sample_crop_yield.csv"
df = pd.read_csv(file_path)

mysql_user = 'root'
mysql_password = 'ejodrp96'
mysql_host = 'localhost'
mysql_port = '3306'
mysql_db = 'agriculture'

connection_string = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
engine = create_engine(connection_string)
aggregated_results = transform_agriculture_data(df)

for name, df_agg in aggregated_results.items():
    table_name = f"agri_{name}"  # prefix for consistency

    if isinstance(df_agg, pd.DataFrame):
        #check for multiindex collumns
        if isinstance(df_agg.columns, pd.MultiIndex):
            df_agg.columns = ['_'.join(map(str, col)).strip() for col in df_agg.columns.values]

        #reset index
        df_agg = df_agg.reset_index()

        #save to MySQL table
        df_agg.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print(f"Saved {name} to table {table_name}")
    else:
        print(f"Skipping {name}: Not a DataFrame")
