# main.py

import sys  # Import the sys module to handle command-line arguments
from robust_division_calculator import safe_divide  # Import the division function

def main():
    # Ensure exactly 3 arguments are provided: the script name, numerator, and denominator
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)  # Exit if the wrong number of arguments are provided

    # Get the numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division and display the result or error message
    result = safe_divide(numerator, denominator)
    print(result)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
