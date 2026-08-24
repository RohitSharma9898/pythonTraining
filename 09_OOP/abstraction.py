"""
ABSTRACTION

Abstraction means hiding unnecessary
implementation details and showing
only important functionality.

Example:

When we use an ATM, we only see
the required options.
We don't see the internal implementation.
"""


class ATM:

    def withdraw(self, amount):

        print("Processing withdrawal...")


atm = ATM()

atm.withdraw(500)