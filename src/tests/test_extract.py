import os
from src.extract.extract import extract, download_file
import unittest
from unittest.mock import patch, MagicMock

class TestExtract(unittest.TestCase):
    @patch("src.extract.extract.requests.get")
    def test_extract(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = """
        <html>
            <body>
                <table>
                    <tbody>
                        <tr>
                            [<td>1
                            </td>, <td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/web/20230908091635/https://en.wikipedia.org/wiki/United_States" title="United States"><img alt="United States" class="mw-file-element" data-file-height="650" data-file-width="1235" decoding="async" height="12" src="//web.archive.org/web/20230908091635im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png" srcset="//web.archive.org/web/20230908091635im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/35px-Flag_of_the_United_States.svg.png 1.5x, //web.archive.org/web/20230908091635im_/https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/46px-Flag_of_the_United_States.svg.png 2x" width="23"/></a></span></span> <a href="/web/20230908091635/https://en.wikipedia.org/wiki/JPMorgan_Chase" title="JPMorgan Chase">JPMorgan Chase</a>
                            </td>, <td>432.92
                            </td>]
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        df = extract("mock_url")
        self.assertFalse(df.empty, "O DataFrame não deve estar vazio.")
        self.assertEqual(df.loc[0, "Name"], "JPMorgan Chase", "O nome do primeiro banco deve ser 'JPMorgan Chase'.")
        self.assertEqual(df.loc[0, "MC_USD_Billion"], 432.92, "O valor esperado para MC_USD_Billion deve ser '432.92'.")
     
if __name__ == "__main__":
    unittest.main()

# class TestDownload(unittest.TestCase):
#     def test_dowload(self, tmp_path, mock_get):
#         mock_response = MagicMock()
#         mock_response.content = b"currency,rate\nUSD,1.0\nEUR,0.85"
#         mock_get.return_value = mock_response
#         download_file("mock_path", "sample.csv")
#         self.assertFalse(os.path.isfile(tmp_path / "sample.csv")), "O arquivo deve ser baixado e salvo."

# if __name__ == "__main__":
#     unittest.main()
        



   

# def test_download(tmp_path):
#     mock_content = b"currency,rate\nUSD,1.0\nEUR,0.85"
#     with patch('request.get') as mock_get:
#         mock_response = MagickMock()
#         mock_response.content = mock_content
#         mock_get.return_value = mock_response
#         download_file("mock_path", "sample.csv")
#         assert os.path.isfile(tmp_path / "sample.csv"),"O arquivo deve ser baixado e salvo."
