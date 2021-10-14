import unittest

def setUpModule():
    print("Works before all methods in test modul")

def tearDownModule():
    print("Works after all methods in test modul")

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'Before {cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        print(f'After ...{cls.__name__}')

    def test_case_1(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

    def test_case_2(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)

    def test_case_2(self):
        self.assertAlmostEqual(0.12345678, 0.12345679)

class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(0.1234567, 0.1234566, 6)


