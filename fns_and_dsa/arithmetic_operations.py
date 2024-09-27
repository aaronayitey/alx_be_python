def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform.

    Returns:
        float: The result of the operation.
    """
    
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return 'Cannot divide by zero'
            return num1 / num2
        case _:
            return "Invalid operation! Please select from \
                (add, subtract, multiply, divide) only!"
