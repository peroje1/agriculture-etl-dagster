from dagster import op
import pandas as pd
from sqlalchemy import create_engine

@op
def load_to_mysql(aggregated_results: dict) -> None:
    mysql_user = 'root'
    mysql_password = 'ejodrp96'
    mysql_host = 'localhost'
    mysql_port = '3306'
    mysql_db = 'agriculture'

    connection_string = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
    engine = create_engine(connection_string)

    for name, df_agg in aggregated_results.items():
        table_name = f"agri_{name.lower()}"

        if isinstance(df_agg, pd.DataFrame):

            if isinstance(df_agg.columns, pd.MultiIndex):
                df_agg.columns = ['_'.join(map(str, col)).strip() for col in df_agg.columns.values]

            df_agg = df_agg.reset_index()

            df_agg.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
            print(f"Saved to table: {table_name}")
        else:
            print(f"Skipped {name}: Not a DataFrame")
