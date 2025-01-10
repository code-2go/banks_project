from src.config import LOG_PATH
from datetime import datetime

def log(message):
    timestamp_format = '%Y-%b-%d | %H:%M:%S '
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(LOG_PATH, 'a') as log_file:
        log_file.write(f'{timestamp} - {message} \n')