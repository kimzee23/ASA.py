import unittest
import expenseTR

class Test_Expense_TR(unittest.TestCase):
    def test_add_expense_success(self):
        expenses = []
        result = expenseTR.add_expense(expenses, "20250223", "Groceries", "5000")
        self.assertEqual(result, "Expense added successfully!")
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0], [20250223, "Groceries", 5000])
    
    def test_add_expense_invalid_amount(self):
        expenses = []
        result = expenseTR.add_expense(expenses, "20250223", "Groceries", "kolajo")
        self.assertEqual(result, "Invalid amount and Date entered . Please enter a number.")
        self.assertEqual(len(expenses), 0)
    
    def test_view_expenses_empty(self):
        expenses = []
        result = expenseTR.view_expenses(expenses)
        self.assertEqual(result, "No expenses recorded.")
    
    def test_view_expenses_is_not_empty(self):
        expenses = [[20250225, "Groceries", 5000], [20250223, "Bokku", 1700.50]]
        result = expenseTR.view_expenses(expenses)
        self.assertIn("Groceries", result)
        self.assertIn("Bokku", result)
        self.assertIn("5000", result)
        self.assertIn("1700.50", result)
    
    def test_calculate_total_expenses(self):
        expenses = [[20250223, "Groceries", 5000], [20250223, "Bokku", 1700.50]]
        result = expenseTR.calculate_total_expenses(expenses)
        self.assertEqual(result, "Your total expenses is #6700.50")
    
    def test_calculate_total_expenses_empty(self):
        expenses = []
        result = expenseTR.calculate_total_expenses(expenses)
        self.assertEqual(result, "Your total expenses is #0.00 You did not spend anything ode :")


if __name__ == "__main__":
    unittest.main()
