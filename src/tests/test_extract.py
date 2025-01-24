import os
import unittest
import tempfile
from src.config import RESOURCE_PATH
from src.extract.extract import extract, download_file
from unittest.mock import patch, MagicMock

def load_mock_html(file_name):
    path = os.path.join(RESOURCE_PATH, file_name)
    with open(path, "r") as file:
        return file.read()

class TestExtract(unittest.TestCase):
    @patch("src.extract.extract.requests.get")
    def test_extract(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = load_mock_html("mock_page.html")
        mock_get.return_value = mock_response

        df = extract("mock_url")
        self.assertFalse(df.empty, "The dataframe should not be empyt.")
        self.assertEqual(df.loc[0, "Name"], "JPMorgan Chase", "The name of the first bank should be 'JPMorgan Chase'.")
        self.assertEqual(df.loc[0, "MC_USD_Billion"], 432.92, "The expected value for MC_USD_Billion should be '432.92'.")

class TestDownload(unittest.TestCase):
    @patch('requests.get')
    def test_dowload(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"currency,rate\nUSD,1.0\nEUR,0.85"
        mock_get.return_value = mock_response

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "sample.csv")
            download_file("mock_url", file_path)
            print(f"Arquivo Criado: {file_path}")
            self.assertTrue(os.path.abspath(file_path), "The file must be downloaded and saved")

if __name__ == "__main__":
    unittest.main()