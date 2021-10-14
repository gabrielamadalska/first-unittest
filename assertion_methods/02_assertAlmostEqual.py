import unittest

class TestClass1(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(0.1 + 0.2, 0.3)

    def test_case_2(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

    def test_case_3(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)

    def test_case_4(self):
        self.assertAlmostEqual(0.12345678, 0.12345679)

        #True, bo metoda odejmuje wartości i zaokrągla różnicę do 7 miejsca po przecinku

    def test_case_5(self):
        self.assertAlmostEqual(0.1234567, 0.1234566, 6)

        # ostatnia pozycja pozwala zmienić liczbę po przecinku do której metoda zaokrągla

