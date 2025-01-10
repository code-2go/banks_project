from src.config import CSV_PATH
import os

def load_file_csv(df, file_name, layer='bronze'):
    path = os.path.join(CSV_PATH, layer, file_name)
    if not os.path.isfile(path):
        df.to_csv(f"{path}.csv")
        print(f'File saved in {layer} layer: {file_name}.')
    else:
        print(f'The file {file_name} already exists in {layer} layer.')