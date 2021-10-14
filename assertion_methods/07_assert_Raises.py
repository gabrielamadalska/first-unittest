import unittest

def get_value(index, container):
    return container[index]


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertRaises(IndexError, get_value, 3, "aws")

    def test_case2(self):
        with self.assertRaises(IndexError):
            get_value(3, "aws")
