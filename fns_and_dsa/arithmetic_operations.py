# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the operation or a specific error message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # 1. Handle the division by zero scenario specifically
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        # 2. Handle any other invalid operation string
        return "Invalid operation."