import unittest
from tax import calc_tax

class TestCalcTax(unittest.TestCase):
    def test_calc_tax_negative_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.23, -5)

    def test_calc_tax_wrong_type_age_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, 0.23, "text")

    def test_calc_tax_tweenty_percent_eighteen_age(self):
        self.assertAlmostEqual(calc_tax(60000, .2, 18), 5000)

    def test_calc_tax_tweenty_percent_sixty_six_age(self):
        self.assertAlmostEqual(calc_tax(60000, .2, 66), 8000)

    def test_calc_tax_tweenty_percent_nineteen_age(self):
        self.assertAlmostEqual(calc_tax(60000, .2, 19), 12000)

    def test_calc_tax_tweenty_percent_sixty_five_age(self):
        self.assertAlmostEqual(calc_tax(60000, .2, 65), 12000)
