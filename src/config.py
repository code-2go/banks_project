import os
from sqlite3 import Connection

# URLs
URL = r"https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
DOWNLOAD = r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"

# Paths
BASE_PATH = r"C:\Users\b_gur\OneDrive\Documentos\IBM\banks_project"
CSV_PATH = os.path.join(BASE_PATH, "csv_files")
LOG_PATH = os.path.join(BASE_PATH, "src", "utils", "code_log.txt")
DB_PATH = os.path.join(BASE_PATH, "db_files", "Banks.db")


# Database
DB_NAME = 'Banks.db'
TABLE_NAME = 'Largest_banks'
TABLE_SCHEMA = ['Name', 'MC_USD_Billion']
CONN_SQL = Connection(DB_PATH)