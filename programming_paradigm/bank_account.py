# bank_account.py

class BankAccount:
    # Initialize the bank account with an optional initial balance
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    # Deposit a specified amount into the bank account
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    # Withdraw a specified amount from the bank account if sufficient funds are available
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    # Display the current balance of the bank account
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")


