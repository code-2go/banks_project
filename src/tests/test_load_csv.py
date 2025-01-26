import os
import unittest
import pandas as pd
import tempfile
from src.load.load_csv import load_file_csv
from unittest.mock import patch

class TestLoadCSV(unittest.TestCase):
    def test_load_success(self):
        # Check if the file will be loaded
        with tempfile.TemporaryDirectory() as temp_dir:
            df = pd.DataFrame({'column1': ['a', 'b', 'c'], 'column2': [1, 2, 3]})
            file = load_file_csv(df, "test_data", layer="test", base_path=temp_dir)
            self.assertTrue(file)

    def test_load_file_exists(self):
        # Check if the file will be subscribed if it already exists
        with tempfile.TemporaryDirectory() as temp_dir:
            df = pd.DataFrame({'column1': ['a', 'b', 'c'], 'column2': [1, 2, 3]})
            file_path = load_file_csv(df, "test_data", layer="test", base_path=temp_dir)
            with open(file_path, 'w') as f:
                f.write("test")
            output = load_file_csv(df, "test_data", layer="test", base_path=temp_dir)
            self.assertFalse(output)

    def test_load_exceptions(self):
        # Check if the function is raising generic exceptions 
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("builtins.print") as mock_print:
                with patch('builtins.open', side_effect=PermissionError):
                    df = pd.DataFrame({'column1': ['a', 'b', 'c'], 'column2': [1, 2, 3]})
                    with self.assertRaises(PermissionError):
                        load_file_csv(df, "test_data", layer="test", base_path=temp_dir)
                    mock_print.assert_called_once_with("An error occurred: ")

if __name__ == "__main__":
    unittest.main()
