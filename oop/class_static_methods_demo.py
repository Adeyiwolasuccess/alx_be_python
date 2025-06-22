class Calculator:
    """
    A class demonstrating the use of static and class methods.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
