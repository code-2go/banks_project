import os
import unittest
import pandas as pd
from pandas.errors import EmptyDataError
from unittest.mock import patch
from src.transform.transform import currency_converter

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'MC_USD_Billion': [100, 200, 300]})
        self.fx_rate = pd.DataFrame({'Currency': ['EUR', 'GBP'], 'Rate': [0.85, 0.95]})

    def test_currency_converter(self):
        with patch("pandas.read_csv", return_value=self.fx_rate):
            converted_df = currency_converter(self.df)

            self.assertIn("MC_EUR_Billion", converted_df.columns)
            self.assertIn("MC_GBP_Billion", converted_df.columns)
            self.assertEqual(converted_df.loc[0, "MC_EUR_Billion"], 85)

    def test_currency_converter_file_not_found(self):
        with patch("pandas.read_csv", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                currency_converter(self.df)
    
    def test_currency_converter_empty_fx_rate_file(self):
        empty_fx_rate = pd.DataFrame()

        with patch("pandas.read_csv", return_value=empty_fx_rate):
            with self.assertRaises(EmptyDataError):
                currency_converter(self.df)

    def test_currency_converter_invalid_types(self):
        invalid_inputs = [None, 'string', [1, 2 ,3], {'key': 'value'}]
        
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError) as context:
                    currency_converter(invalid_input)
            
                self.assertEqual(str(context.exception), 'ERROR: the input df is not a pandas DataFrame.')

    def test_currency_converter_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=['MC_USD_Billion'])

        with patch("pandas.read_csv", return_value=self.fx_rate):
            converted_df = currency_converter(empty_df)
            self.assertTrue(converted_df.empty)

    def test_currency_converter_missing_columns(self):
        cases =  [ 
            pd.DataFrame({'wrongColumn': ['EUR', 'GBP'], 'Rate': [0.85, 0.95]}), 
            pd.DataFrame({'Currency': ['EUR', 'GBP'], 'wrongColumn': [0.85, 0.95]})
        ] 

        for case in cases:
            with self.subTest(case=case):
                with patch("pandas.read_csv", return_value=case):
                    with self.assertRaises(KeyError):
                        currency_converter(self.df)

    def test_currency_converter_negative_or_zero_rates(self):
        negative_or_zero_fx_rate = pd.DataFrame({'Currency': ['EUR', 'GBP'], 'Rate': [0, -0.95]})

        with patch("pandas.read_csv", return_value=negative_or_zero_fx_rate):
            converted_df = currency_converter(self.df)

            self.assertEqual(converted_df.loc[0, "MC_EUR_Billion"], 0)
            self.assertEqual(converted_df.loc[1, "MC_GBP_Billion"], -190)
                
if __name__ == "__main__":
    unittest.main()