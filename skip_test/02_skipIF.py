import unittest
from datetime import date

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("aws".upper(), "AWS")


    @unittest.skipIf(date.today().day % 2 == 0, "Skipind even days.")
    def test_something1(self):
        self.assertEqual("aws".upper(), "AWS")


