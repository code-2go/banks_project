from src.config import TABLE_SCHEMA, CSV_PATH
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

def donwload_file(url, file_name):
    response = requests.get(url)
    path = os.path.join(CSV_PATH, "bronze", file_name)
    if response.status_code == 200:
        if not os.path.isfile(path):
            with open(f"{path}.csv", 'wb') as file:
                file.write(response.content)
                print('Download was a Success.')
        else: 
            print(f'The file {file_name} already exists.')
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