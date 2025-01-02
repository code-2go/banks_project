import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime 

URL = r"https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
FX = r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"

BASE_PATH = r"C:\Users\b_gur\OneDrive\Documentos\IBM\banks_project"
LOG_PATH = rf"{BASE_PATH}\log\code_log.txt"
CSV_PATH = rf"{BASE_PATH}\csv_files"
DB_NAME = 'Banks.db'
TABLE_NAME = 'Largest_banks'
TABLE_SCHEMA = ['Name', 'MC_USD_Billion']
CONN_SQL = sqlite3.Connection(rf"{BASE_PATH}\db_files\{DB_NAME}")

def log(message):
    timestamp_format = '%Y-%b-%d | %H:%M:%S '
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(LOG_PATH, 'a') as log_file:
        log_file.write(f'{timestamp} - {message} \n')
    

def donwload_file(path, file_name):
    response = requests.get(FX)
    if response.status_code == 200:
        with open(f"{CSV_PATH}{file_name}", 'wb') as file:
            file.write(response.content)
            print(f'Download was a Success.')
    else:
        print(f'Download Fail. Status Code: {response.status_code}')

def extract(url):
    content = requests.get(url).text
    object_soup = BeautifulSoup(content, 'html.parser')
    tables = object_soup.find_all('tbody')
    rows = tables[0].find_all('tr')
    data = []
    for row in rows:
        cell = row.find_all('td')
        if len(cell) != 0:
            if cell[1].find('a') is not None:
                cell = row.find_all('td')
                data.append({
                    'Name': cell[1].text.strip(),
                    'MC_USD_Billion': cell[2].contents[0].strip()
                })       
    df = pd.DataFrame(data, columns=TABLE_SCHEMA)
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)
    return df

def load_file_csv(df, file_name):
    df.to_csv(rf"{BASE_PATH}\csv_files\{file_name}.csv")
    print('File Saved as success.')
    
def currency_converter(df):
    fx_rate = pd.read_csv(rf"{BASE_PATH}\csv_files\FX_rate.csv")
    conversion_dict = {}
    for i, row in fx_rate.iterrows():
        conversion_dict[row['Currency']] = row['Rate']
    for currency, rate in conversion_dict.items():
        column_name = f'MC_{currency}_Billion'
        df[column_name] = round((df['MC_USD_Billion'] * rate), 2)
    return df


# log('Download Files Process Started')
# donwload_file(FX, '\FX_rate.csv')
# log('Download Files Process Ended')

# log('Extraction Process Started')
Largest_banks = extract(URL)
# log('Extraction Process Ended')

# log('Load file.csv Process Started')
# load_file_csv(banks_data, r'\banks_data_raw.csv')
# log('Load file.csv Process Ended')

# log('Transform Phase Started')
Largest_banks = currency_converter(Largest_banks)
# log('Transform Phase Ended')

# log('Load file.csv Process Started')
load_file_csv(Largest_banks, TABLE_NAME)
# log('Load file.csv Process Ended')
