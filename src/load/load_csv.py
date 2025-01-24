from src.config import CSV_PATH
import os

def load_file_csv(df, file_name, layer='_raw'):
    path = os.path.join(CSV_PATH, layer, f"{file_name}.csv")

    try:
        # check the existence of the directory
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # check if the file exists
        if not os.path.isfile(path):
            df.to_csv(f"{path}.csv")
            print(f'File saved in {layer} layer: {file_name}.')
        else:
            print(f'The file {file_name} already exists in {layer} layer.')
        return True
    
    except FileNotFoundError as e:
        print(f'The directory was not found')
        return False
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return False