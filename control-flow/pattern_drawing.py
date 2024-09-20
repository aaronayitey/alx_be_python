

try:

    size = int(input("Enter the size of the pattern: "))

    row = 0
    while row < size:
        for a in range(size):
            print("*", end="")
        
        print()

        row += 1
except ValueError:
    print("Enter numbers only!") 
