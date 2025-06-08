def perform_operation(num1, num2, operation):
    """
    perfoms basic arithmetic operations

    Args:
        num1 (float): first number
        num2 (float): second number
        operation (str): The operation to perform ('add', 'subtract', 'multiplication', 'divide'.)

        Returns: 
            The result of the operation or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation"
    
    
