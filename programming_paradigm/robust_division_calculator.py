# robust_division_calculator.py

def safe_divide(numerator, denominator):
    # Attempt to convert numerator and denominator to floats
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    # Attempt division and handle division by zero
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    # Return the result if no exceptions occurred
    return f"The result of the division is {result}"
