# polymorphism_demo.py
import math

class Shape:
    """
    Base class representing a generic shape.
    """
    def area(self):
        """
        Calculates the area of the shape. This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a new Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
