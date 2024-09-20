

try:

    number = int(input("Enter the size of the pattern: "))

    count = 0
    while count < number:
        print("*"* number, end="\n")
        count += 1
except ValueError:
    print("Enter numbers only!") 