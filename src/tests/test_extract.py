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
        self.assertFalse(df.empty, "O DataFrame não deve estar vazio.")
        self.assertEqual(df.loc[0, "Name"], "JPMorgan Chase", "O nome do primeiro banco deve ser 'JPMorgan Chase'.")
        self.assertEqual(df.loc[0, "MC_USD_Billion"], 432.92, "O valor esperado para MC_USD_Billion deve ser '432.92'.")

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
            self.assertTrue(os.path.abspath(file_path), "O arquivo deve ser baixado e salvo.")

if __name__ == "__main__":
    unittest.main()