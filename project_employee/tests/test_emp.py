import unittest
from employee.emp import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp = Employee("Anna", "Kowalska", 80000)
        self.assertEqual(emp.email, "anna.kowalska@mail.com")

    def test_email_after_name_changing(self):
        emp = Employee("Anna", "Kowalska", 80000)
        emp.first_name = "Barbara"
        self.assertEqual(emp.email, "barbara.kowalska@mail.com")

    def test_email_after_last_name_changing(self):
        emp = Employee("Anna", "Kowalska", 80000)
        emp.last_name = "Nowak"
        self.assertEqual(emp.email, "anna.nowak@mail.com")

    def test_tax(self):
        emp = Employee("Anna", "Kowalska", 80000)
        self.assertEqual(emp.tax(), 13600)

    def test_apply_bonu(self):
        emp = Employee("Anna", "Kowalska", 80000)
        emp.apply_bonus()
        self.assertEqual(emp.salary, 88000)



