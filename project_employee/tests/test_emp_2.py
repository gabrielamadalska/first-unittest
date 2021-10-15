import unittest
from employee.emp import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("setting up")
        self.emp = Employee("Anna", "Kowalska", 80000)

    def tearDown(self):
        print("tearing down...")
        del self.emp

    def test_email(self):
        self.assertEqual(self.emp.email, "anna.kowalska@mail.com")

    def test_email_after_name_changing(self):
        self.emp.first_name = "Barbara"
        self.assertEqual(self.emp.email, "barbara.kowalska@mail.com")

    def test_email_after_last_name_changing(self):
        self.emp.last_name = "Nowak"
        self.assertEqual(self.emp.email, "anna.nowak@mail.com")

    def test_tax(self):
        self.assertEqual(self.emp.tax(), 13600)

    def test_apply_bonu(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)



