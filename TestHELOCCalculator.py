import unittest
import hashlib
from HELOCCalculator import calculate_monthly_payment, hash_name, get_positive_float, get_positive_int

class TestBankFunctions(unittest.TestCase):
    def test_calculate_monthly_payment(self):
        self.assertAlmostEqual(calculate_monthly_payment(1000, 5, 1), 85.61, places=2)
        self.assertAlmostEqual(calculate_monthly_payment(5000, 10, 5), 106.24, places=2)

    def test_hash_name(self):
        self.assertEqual(hash_name("John Doe"), hashlib.sha256("John Doe".encode()).hexdigest())

    def test_get_positive_float(self):
        with self.assertRaises(ValueError):
            get_positive_float("-10")

    def test_get_positive_int(self):
        with self.assertRaises(ValueError):
            get_positive_int("-5")

if __name__ == "__main__":
    unittest.main()
