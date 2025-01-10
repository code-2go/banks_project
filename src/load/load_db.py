from src.config import TABLE_NAME, CONN_SQL
import os

def load_to_database(df):
    df.to_sql(TABLE_NAME, CONN_SQL, if_exists="replace", index=False)
    print(f'The dataframe has been export to {TABLE_NAME}.db')
