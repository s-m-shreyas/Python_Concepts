# type: ignore

"""
01_public_members.py

Demonstrates public members in Python classes.

Public members are attributes and methods that are accessible
from outside the class without any restriction.

In Python, members are public by default unless we use a
special naming convention such as a leading underscore or
double underscore.
"""


# ============================================================
# 1. PUBLIC ATTRIBUTES
# ============================================================

class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """Remove money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            raise ValueError("Invalid withdrawal amount.")


account = BankAccount("Alice", 1500.0)

print(account.owner)
print(account.balance)

account.deposit(250.0)
account.withdraw(100.0)


# ============================================================
# 2. PUBLIC MEMBERS ARE ACCESSIBLE OUTSIDE THE CLASS
# ============================================================

# This is the default behavior in Python.
# Anyone can access or change a public attribute directly.

account.balance = 5000
print(f"Updated balance: {account.balance}")


# ============================================================
# 3. WHY THIS IS NOT STRONG ENCAPSULATION
# ============================================================

# Public members do not restrict direct access.
# This is convenient for simple programs, but it can allow
# accidental misuse if the object state is modified without
# validation.

# For better control, we usually use methods to manage access.

# ============================================================
# INTERVIEW NOTE
# ============================================================

# In Python, public means "no underscore prefix".
# The language does not prevent direct access by default.
# A design with careful methods is usually preferred over
# direct attribute modification.
