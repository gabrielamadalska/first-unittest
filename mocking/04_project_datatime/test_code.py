import unittest
from unittest.mock import patch
from code_generator import get_code_with_day, get_code


class TestGetCoode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_should_return_3(self, mocked_random):
        mocked_random.return_value = 3
        actual = get_code()
        expected = 'XC-3'
        self.assertEqual(actual, expected)

class TestGetCodeWithDay(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_with_today_date(self, mocked_int):
        mocked_int.return_value = 5
        actual = get_code_with_day()
        expected = 'XC-5-FRI'
        self.assertEqual(actual, expected)

    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_date_monday(self, mocked_int, mocked_day):
        mocked_int.return_value = 5
        mocked_day.return_value = "MON"
        expected = 'XC-5-MON'
        actual = get_code_with_day()
        self.assertEqual(actual, expected)




