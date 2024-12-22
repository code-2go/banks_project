import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime 

url = r'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
FX = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'

base_path = r'C:\Users\b_gur\OneDrive\Documentos\IBM\banks_project'
log_path = rf'{base_path}\log\code_log.txt'
csv_path = rf'{base_path}\csv_files'
db_name = 'Banks.db'
table_name = 'Largest_banks'
table_schema = ['Name', 'MC_USD_Billion']
conn_sql = sqlite3.Connection(rf'{base_path}\db_files\{db_name}')

def log(message):
    timestamp_format = '%Y-%b-%d | %H:%M:%S '
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_path, 'a') as log_file:
        log_file.write(f'{timestamp} - {message} \n')
    

def donwload_file(path, file_name):
    response = requests.get(FX)
    if response.status_code == 200:
        with open(f'{csv_path}{file_name}', 'wb') as file:
            file.write(response.content)
            print(f'Download was a Success.')
    else:
        print(f'Download Fail. Status Code: {response.status_code}')

log('Download Files Process')
donwload_file(FX, '\FX_data.csv')