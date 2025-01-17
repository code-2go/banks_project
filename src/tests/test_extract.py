import os
from src.extract.extract import extract, download_file
import unittest
from unittest.mock import patch, MagicMock


# def test_extract():
#     mock_html = "<table><tr><td>Name</td></tr></table>"
#     with unittest.patch('requests.get') as mock_get:
#         mock_response = unittest.MagicMock()
#         mock_response.text = mock_html
#         mock_get.return_value = mock_response
#         df = extract("mock_url")
#         assert not df.empty, "A extração deve retornar um DataFrame não vazio."

class TestExtract(unittest.TestCase):
    @patch("src.extract.extract.requests.get")
    def test_extract(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = "<table><tr><td>Name</td></tr></table>"
        mock_get.return_value = mock_response

        df = extract("mock_url")
        self.assertFalse(df.empty, "O Dataframe não deve estar vazio.")

if __name__ == "__main__":
    unittest.main()

class TestDownload(unittest.TestCase):
    def test_dowload(self, tmp_path, mock_get):
        mock_response = MagicMock()
        mock_response.content = b"currency,rate\nUSD,1.0\nEUR,0.85"
        mock_get.return_value = mock_response
        download_file("mock_path", "sample.csv")
        self.assertFalse(os.path.isfile(tmp_path / "sample.csv")), "O arquivo deve ser baixado e salvo."

if __name__ == "__main__":
    unittest.main()
        



   

# def test_download(tmp_path):
#     mock_content = b"currency,rate\nUSD,1.0\nEUR,0.85"
#     with patch('request.get') as mock_get:
#         mock_response = MagickMock()
#         mock_response.content = mock_content
#         mock_get.return_value = mock_response
#         download_file("mock_path", "sample.csv")
#         assert os.path.isfile(tmp_path / "sample.csv"),"O arquivo deve ser baixado e salvo."
