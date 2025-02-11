# Test the crew.py 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from reportcrew.crew import generate_analysis_reports, generate_investment_reports

class TestCrew(unittest.TestCase):
    def test_generate_analysis_reports(self):
        stock_symbol = "AAPL"
        result = generate_analysis_reports(stock_symbol)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_generate_investment_reports(self):
        stock_symbol = "AAPL"
        result = generate_investment_reports(stock_symbol)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
    
if __name__ == "__main__":
    unittest.main()