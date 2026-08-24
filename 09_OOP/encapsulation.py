"""
ENCAPSULATION

Encapsulation means keeping data and methods
together inside a class.

It also helps control access to data.
"""


class BankAccount:

    def __init__(self, balance):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def show_balance(self):

        print("Balance:", self.balance)


account = BankAccount(1000)

account.deposit(500)

account.show_balance()