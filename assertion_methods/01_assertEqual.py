import unittest

class TestClass(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("3.9.0".split("."), ["3","9",0])

#dodatkowe informacje na temat błędu w listach
    def test_case2(self):
        self.assertEqual(tuple("3.9.0".split(".")), ("3","9",0))

    def test_case3(self):
        self.assertEqual({3,4}, {4,3,5})
