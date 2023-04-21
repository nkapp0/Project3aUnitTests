#Unit Tests
import unittest
from app import app

class TestInputValidation(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_symbol_valid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='1',
            time_series='1',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_symbol_invalid(self):
        response = self.app.post('/', data=dict(
            symbol='aapl',
            chart_type='1',
            time_series='1',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertIn(b'Symbol must be capitalized and contain 1-7 alphabetical characters', response.data)

    def test_chart_type_valid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='2',
            time_series='1',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_chart_type_invalid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='3',
            time_series='1',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertIn(b'Chart type must be 1 or 2', response.data)

    def test_time_series_valid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='1',
            time_series='3',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_time_series_invalid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='1',
            time_series='5',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertIn(b'Time series must be a numeric character between 1 and 4', response.data)

    def test_start_date_valid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='1',
            time_series='1',
            start_date='2022-01-01',
            end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_start_date_invalid(self):
        response = self.app.post('/', data=dict(
            symbol='AAPL',
            chart_type='1',
            time_series='1',
            start_date='2022-01-31',
            end_date='2022-01-20'
        ), follow_redirects=True)
        self.assertIn(b'Start date must be in the format YYYY-MM-DD', response.data)

    def test_end_date_valid(self):
        response = self.app.post('/', data=dict(
        symbol='AAPL',
        chart_type='1',
        time_series='1',
        start_date='2022-01-01',
        end_date='2022-01-31'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
