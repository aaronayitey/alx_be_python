

try:

    number = int(input("Enter a number for pattern drawing: "))

    count = 0
    while count < number:
        print("*"* number, end="\n")
        count += 1
except ValueError:
    print("Enter numbers only!") 