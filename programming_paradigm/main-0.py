# main-0.py

import sys  # Import system module to handle command-line arguments
from bank_account import BankAccount  # Import the BankAccount class

def main():
    # Main function to handle command-line input and perform bank operations
    account = BankAccount(100)  # Create an account with an initial balance of $100

    if len(sys.argv) < 2:  # Check if any command-line arguments are provided
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)  # Exit if no valid arguments are provided

    # Split the command and parameters from the command-line argument
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None  # Convert amount to float if provided

    # Perform deposit operation
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    
    # Perform withdrawal operation
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    
    # Display the account balance
    elif command == "display":
        account.display_balance()
    
    # Handle invalid commands
    else:
        print("Invalid command. Please use 'deposit', 'withdraw', or 'display'.")

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
