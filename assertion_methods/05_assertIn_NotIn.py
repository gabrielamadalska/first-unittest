import unittest


class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertIn("@", "sample@gmail.com")

    def test_case2(self):
        tech_stack = ["java", "python", "c++"]
        self.assertIn("java", tech_stack)

    def test_case3(self):
        tech_stack = ["java", "python", "c++"]
        self.assertNotIn("excel", tech_stack)

