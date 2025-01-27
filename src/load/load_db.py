import os

def load_to_database(df, table_name, conn):
    try: 
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f'The dataframe has been export to {table_name}.db')
        return True
    except Exception:
        print("")
        raise