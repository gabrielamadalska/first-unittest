import unittest
import sys

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("aws".upper(), "AWS")


    @unittest.skipUnless(sys.platform.startswith("win"), "Skip uneless Windows")
    def test_something1(self):
        self.assertEqual("aws".upper(), "AWS")

    @unittest.skipUnless(sys.platform.startswith("linux"), "Skip uneless Windows")
    def test_something2(self):
        self.assertEqual("aws".upper(), "AWS")


