import unittest

from calculator.calc_math import SimpleMathCalculator


def setUpModule():
    print("setting up")
    global calc #instancja naszej klasy, kalkulator
    calc = SimpleMathCalculator()

def tearDownModule():
    print("tearing")
    global calc
    calc = SimpleMathCalculator()

class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3,4), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(3,4), -1)
