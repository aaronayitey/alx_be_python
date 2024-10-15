# Define the Calculator class
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method
    @staticmethod
    def add(a, b):
        """This method adds two numbers and returns the result."""
        return a + b

    # Class method
    @classmethod
    def multiply(cls, a, b):
        """This method multiplies two numbers and prints the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
