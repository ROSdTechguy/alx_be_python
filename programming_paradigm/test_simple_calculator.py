import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Basic addition
        self.assertEqual(self.calc.add(-1, 1), 0)  # Addition with negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Addition with zero
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)  # Floating-point addition

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Basic subtraction
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Subtraction to negative
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)  # Floating-point subtraction
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Subtraction with zero

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Basic multiplication
        self.assertEqual(self.calc.multiply(-1, 5), -5)  # Multiplication with negative
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Multiplication with zero
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)  # Floating-point multiplication

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2.0)  # Basic division
        self.assertEqual(self.calc.divide(-6, 3), -2.0)  # Division with negative
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Floating-point division
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero divided by a number

if __name__ == "__main__":
    unittest.main()
t
