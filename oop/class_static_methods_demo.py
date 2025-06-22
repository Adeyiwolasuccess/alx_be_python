# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the use of static and class methods.
    """
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method that returns the sum of two numbers.
        Static methods do not have access to the class (cls) or instance (self).

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method that returns the product of two numbers.
        Class methods receive the class itself (cls) as the first argument,
        allowing them to access class attributes or call other class methods.

        Args:
            cls: The class itself (conventionally named 'cls').
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
