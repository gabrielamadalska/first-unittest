import unittest

class TestClass1(unittest.TestCase):
    def test_case1(self):
        self.assertGreater(40, 5.5)

    def test_case2(self):
        self.assertGreaterEqual(5.5, 5.5)

    def test_case3(self):
        self.assertLess(5, 5.5)

    def test_case4(self):
        self.assertLessEqual(5.5, 5.5)


