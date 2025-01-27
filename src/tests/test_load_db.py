import os
import unittest
import pandas as pd
from unittest.mock import MagicMock, patch
from src.load.load_db import load_to_database

class TestLoadToDatabase(unittest.TestCase):
    def test_load_to_db(self):
        df = pd.DataFrame({'column1': ['a', 'b', 'c'], 'column2': [1, 2, 3]})

        mock_conn = MagicMock()

        with patch('pandas.DataFrame.to_sql') as mock_to_sql:
            mock_to_sql.return_value = None

            output = load_to_database(df, 'test_table', mock_conn)

            mock_to_sql.assert_called_once_with('test_table', mock_conn, if_exists='replace', index=False)

            self.assertTrue(output)

if __name__ == "__main__":
    unittest.main()