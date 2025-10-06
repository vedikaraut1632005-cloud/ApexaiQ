"""This program creates a BankAccount class with deposit, withdraw, and check_balance methods.
It also handles insufficient balance using exceptions."""

class InsufficientBalanceError(Exception):
    """This exception is raised when someone tries to withdraw more money than available."""
    pass


class BankAccount:
    """A simple class that represents a bank account."""

    def __init__(self, account_holder, balance=0):
        """Initialize the account with account holder name and initial balance."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit a given amount into the account."""
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        """Withdraw a given amount if balance is sufficient, else raise an exception."""
        if amount > self.balance:
            raise InsufficientBalanceError("Withdrawal failed: Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def check_balance(self):
        """Check and print the current account balance."""
        print(f"{self.account_holder}, your current balance is: {self.balance}")



try:
    acc = BankAccount("Vedika", 1000)   
    acc.check_balance()

    acc.deposit(500)   
    acc.check_balance()

    acc.withdraw(2000)  
    acc.check_balance()

except InsufficientBalanceError as e:
    print(e)

