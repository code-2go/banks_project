import pandas as pd
import os
from pandas.errors import EmptyDataError
from src.config import BASE_PATH


def currency_converter(df):

    if not isinstance(df, pd.DataFrame):
        raise TypeError('ERROR: the input df is not a pandas DataFrame.')

    path = os.path.join(BASE_PATH, "data", "_raw","exchange_rate.csv")

    # Read file phase
    try:
        fx_rate = pd.read_csv(path)

    except FileNotFoundError:
        print(f'ERROR: Exchange rate file not found at {path}.')
        raise
    
    except Exception as e:
        print(f'ERROR reading exchange rate file: {e}')
        raise 

    if fx_rate.empty:
            raise EmptyDataError('ERROR: Exchange rate file at {path} is empty.')

    # Transform phase
    try:
        conversion_dict = {}

        for i, row in fx_rate.iterrows():
            conversion_dict[row['Currency']] = row['Rate']

        for currency, rate in conversion_dict.items():
            column_name = f'MC_{currency}_Billion'
            df[column_name] = round((df['MC_USD_Billion'] * rate), 2)

    except KeyError as e:
        print(f'ERROR: Missing required column {e} in exchange_rate file.')
        raise
    
    except Exception as e:
        print(f'ERROR during transformation process: {e}')
        raise

    if df.empty:
        print('WARNING: The input DataFrame is empty. Returning an empty DataFrame.')
    
    return df    
 