from src.extract.extract import extract, download_file
from src.load.load_db import load_to_database
from src.load.load_csv import load_file_csv
from src.transform.transform import currency_converter
from src.utils.log import log
from src.config import URL, TABLE_NAME, DOWNLOAD

log('Download Files Process Started')
download_file(DOWNLOAD, 'exchange_rate')
log('Download Files Process Ended')

log('Extraction Process Started')
Largest_banks = extract(URL)
log('Extraction Process Ended')

log('Load file.csv Process Started')
load_file_csv(Largest_banks, 'banks_data_raw')
log('Load file.csv Process Ended')

log('Transform Phase Started')
Largest_banks = currency_converter(Largest_banks)
log('Transform Phase Ended')

log('Load file.csv Process Started')
load_file_csv(Largest_banks, TABLE_NAME, "final")
log('Load file.csv Process Ended')

log('Load to Database Process Started')
load_to_database(Largest_banks)
log('Load to Database Process Ended')