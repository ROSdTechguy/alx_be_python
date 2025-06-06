import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Basic addition 
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)         # Adding zero
        self.assertEqual(self.calc.add(100, 200), 300)   # Larger numbers

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)  # Basic subtraction
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negatie result
        self.assertEqual(self.calc.subtract(-3, -2), -5)  # Negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Subtracting zero

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Basic multiplication
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-1, 5) -5)  # Multiplying negative by positive
        self.assertEqual(self.calc.multiply(-1, -5) 5)  # Multiplying negative by negative

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)      # Basic division
        self.assertEqual(self.calc.divide(5, 2), 2.5)    # Division with float result
        self.assertEqual(self.calc.divide(-6, 3), -2)    # Negative result
        self.assertEqual(self.calc.divide(0, 3), 0)      # Zero divided by non-zero
        self.assertIsNone(self.calc.divide(3, 0))        # Division by zero

    def test_edge_cases(self):
        """Test additional edge cases."""
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)   # Floating-point precision check
        self.assertEqual(self.calc.subtract(1e6, 1), 999999)  # Large number subtraction
        self.assertEqual(self.calc.multiply(1e6, 1e6), 1e12)  # Large number multiplication
        self.assertEqual(self.calc.divide(1e6, 1e3), 1e3)     # Large number division

if __name__ == "__main__":
    unittest.main()