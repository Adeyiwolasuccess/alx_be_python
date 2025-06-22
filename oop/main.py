# main.py

# Import the Calculator class from the demonstration script
from class_static_methods_demo import Calculator

def main():
    """
    Main function to demonstrate the usage of static and class methods
    of the Calculator class.
    """
    # Using the static method 'add'
    # Static methods are called directly on the class, no instance needed.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method 'multiply'
    # Class methods are also called directly on the class (or an instance),
    # and they have access to class attributes via 'cls'.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
