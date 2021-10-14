import unittest

class TestClass1(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual( 'aws'.upper(), 'AWS')

    def test_case_2(self):
        self.assertTrue('Apple'.islower())

class TestClass2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, '1')