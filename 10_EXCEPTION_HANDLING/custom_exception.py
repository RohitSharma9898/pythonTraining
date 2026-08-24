"""
CUSTOM EXCEPTION

We can create our own exception
by inheriting from Exception.
"""


class InsufficientBalanceError(Exception):

    pass


class BankAccount:

    def __init__(self, balance):

        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:

            raise InsufficientBalanceError(
                "Insufficient balance"
            )

        self.balance -= amount

        print("Withdrawal successful")

        print("Remaining balance:", self.balance)


account = BankAccount(5000)


try:

    account.withdraw(7000)

except InsufficientBalanceError as error:

    print("Error:", error)