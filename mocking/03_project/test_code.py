import unittest
from unittest.mock import patch
from code_generator import get_code


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_should_return_3(self, mocked_random):
        mocked_random.return_value = 3
        actual = get_code()
        expected = 'XC-3'
        self.assertEqual(actual, expected)

    @patch('random.randint')
    def test_get_code_should_return_7(self, mocked_random):
        mocked_random.return_value = 7
        actual = get_code()
        expected = 'XC-7'
        self.assertEqual(actual, expected)
