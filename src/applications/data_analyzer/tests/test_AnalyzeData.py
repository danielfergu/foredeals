import unittest
from unittest.mock import MagicMock, patch
from data_analyzer.AnalyzeData import AnalyzeData

class TestAnalyzeData(unittest.TestCase):
    def setUp(self):
        self.analyzer = AnalyzeData()
        self.analyzer.csv = 'src/applications/data_analyzer/sqft_price.csv'

    def tearDown(self):
        pass

    def test_calculate_sqft_price(self):
        self.analyzer.auction_sqft = 5
        self.analyzer.auction_price = 50
        self.analyzer.calculate_sqft_price()
        self.assertEqual(self.analyzer.sqft_price, 10.0)

        self.analyzer.auction_sqft = 0
        self.analyzer.calculate_sqft_price()
        self.assertEqual(self.analyzer.sqft_price, 0.0)

    def test_get_csv_prices(self):
        result = self.analyzer.get_csv_prices()
        first_two_zip_codes = dict(list(result.items())[:2])
        expected_result = {'10025': 1270, '60657': 295}
        self.assertEqual(first_two_zip_codes, expected_result)

    def test_get_market_price(self):
        self.analyzer.auction_zip_code = '10025'
        self.analyzer.get_market_price()
        self.assertEqual(self.analyzer.market_price, 1270)

if __name__ == '__main__':
    unittest.main()
