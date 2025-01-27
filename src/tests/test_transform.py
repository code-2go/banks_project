import os
import unittest
import pandas as pd
from unittest.mock import patch
from src.transform.transform import currency_converter

class TestCurrencyConverter(unittest.TestCase):
    def test_currency_converter(self):
        df = pd.DataFrame({'MC_USD_Billion': [100, 200, 300]})
        fx_rate = pd.DataFrame({'Currency': ['EUR', 'GBP'], 'Rate': [0.85, 0.95]})

        with patch("pandas.read_csv", return_value=fx_rate):
            converted_df = currency_converter(df)

            self.assertIn("MC_EUR_Billion", converted_df.columns)
            self.assertIn("MC_GBP_Billion", converted_df.columns)
            self.assertEqual(converted_df.loc[0, "MC_EUR_Billion"], 85)

if __name__ == "__main__":
    unittest.main()