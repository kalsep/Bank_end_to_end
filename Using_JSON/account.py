from Using_JSON.main import *
class BankAccount:
    # get the last account number from the accounts dictionary
    last_account_number = max(accounts.keys(), default=202302)
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = BankAccount.last_account_number + 0
        BankAccount.last_account_number = self.account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def account_info(self):
        return [self.name, self.balance]

    @classmethod
    def create_account(cls, name, initial_deposit):
        account = cls(name, initial_deposit)
        accounts[account.account_number] = account.account_info()
        return account.account_number
