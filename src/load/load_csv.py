from src.config import CSV_PATH
import os

def load_file_csv(df, file_name, layer='_raw', base_path=CSV_PATH):

    if not file_name.endswith(".csv"):
        file_name += ".csv"

    path = os.path.join(base_path, layer, file_name)
    
    if os.path.exists(path):
        print(f'The file {file_name}.csv already exists in {layer} layer.')
        return False 

    try:
        # check the existence of the directory
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(f"{path}")
        print(f'File saved in {layer} layer: {file_name}.')
        return True
    
    except FileNotFoundError as e:
        print(f'Required file not found: {e}. Check if the path is correct')
        raise
    
    except Exception as e:
        print(f'An error occurred: {e}')
        raise