from src.config import BASE_PATH
import pandas as pd
import os


def currency_converter(df):
    path = os.path.join(BASE_PATH, "csv_files", "bronze", "exchange_rate.csv")
    fx_rate = pd.read_csv(path)
    conversion_dict = {}
    for i, row in fx_rate.iterrows():
        conversion_dict[row['Currency']] = row['Rate']
    for currency, rate in conversion_dict.items():
        column_name = f'MC_{currency}_Billion'
        df[column_name] = round((df['MC_USD_Billion'] * rate), 2)
    return df