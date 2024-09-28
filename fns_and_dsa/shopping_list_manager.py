def display_menu():
    """
    Displays the main menu of the Shopping List Manager program.
    
    This function does not take any parameters and does not return any values.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    The main function that controls the shopping list manager program.
    
    It repeatedly displays a menu to the user and performs actions based on the user's choice.
    
    The function does not take any parameters and does not return any values.
    """
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item name: ")
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()