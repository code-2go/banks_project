from src.config import TABLE_SCHEMA, CSV_PATH
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

def download_file(url, file_name):
    try:
        response = requests.get(url, timeout=10)
        path = os.path.join(CSV_PATH, "_raw", file_name)
        if response.status_code == 200:
            if not os.path.isfile(path):
                with open(f"{path}.csv", 'wb') as file:
                    file.write(response.content)
                print('Download was a Success.')
            else: 
                print(f'The file {file_name} already exists.')

    except requests.exceptions.RequestException as e:
        print(f'{file_name} download failed')
        return False
    
    except Exception as e:
        print(f'{file_name} download had an unexpected error: {e}')
        return False
    
    return True


def extract(url):
    try:
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
                        'MC_USD_Billion': float(cell[2].text.strip().replace(',', ''))
                    })       
        df = pd.DataFrame(data, columns=TABLE_SCHEMA)
        return df
    
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
        return pd.DataFrame()
