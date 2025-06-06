class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to calculate the sum of two numbers.
        :param a: int or float, the first number
        :param b: int or float, the second number
        :return: int or float, the sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to calculate the product of two numbers.
        Prints the class attribute 'calculation_type' before performing the operation.
        :param a: int or float, the first number
        :param b: int or float, the second number
        :return: int or float, the product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

