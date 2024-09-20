# This script asks user input of two number and perform calculations

# Handle ValueError for inputs other than numbers
try:

    # Take user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Select the operation for calculation
    operation = input("Choose the operation (+, -, *, /): ")

    if operation == "/" and num2 == 0:
        print("Cannot divide by zero.")

    else:
        match operation:
            case "+":
                calculation = num1 + num2
            case "-":
                calculation = num1 - num2
            case "*":
                calculation = num1 * num2
            case "/":
                calculation = num1 / num2
            case _:
                print("Please select from (+,-,*,/) only!")


        print(f"The result is {calculation}.")
except ValueError:
    print("Enter numbers only!")

