# This script accepts a number input from a user and
# outputs a multiplication table for that number from 1 to 10
try:
    number = int(input("Enter a number to see its multiplication table: "))
    
    for num in range(1, 11):
        print(f"{number} * {num} = {number * num}")

except ValueError:
    print("Enter a number only!")