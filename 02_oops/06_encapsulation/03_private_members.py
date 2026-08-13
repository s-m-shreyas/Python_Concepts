# type: ignore

"""
03_private_members.py

Demonstrates private members in Python classes.

A double underscore prefix, such as __password, tells Python
that the attribute should be name-mangled to avoid accidental
collision with attributes in other classes.

This is not "true" privacy in the same sense as some other
programming languages, but it is a stronger convention than a
single underscore.
"""


# ============================================================
# 1. PRIVATE ATTRIBUTE
# ============================================================

class UserAccount:
    """Represent a user account with a private password."""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.__password = password

    def check_password(self, entered_password: str) -> bool:
        """Validate the account password."""
        return entered_password == self.__password


user = UserAccount("sanjay", "secret123")

print(user.username)
print(user.check_password("secret123"))

# Direct access raises AttributeError because Python mangles the name.
# print(user.__password)


# ============================================================
# 2. NAME MANGLING
# ============================================================

# Behind the scenes, Python stores the attribute as:
# _UserAccount__password
# This is why the name is technically still accessible through
# the mangled form, although this is discouraged.

print(user._UserAccount__password)


# ============================================================
# 3. WHY PRIVATE MEMBERS ARE USEFUL
# ============================================================

# - reduce accidental name collisions
# - hide implementation details
# - encourage access through methods

# However, this is still not a complete security mechanism.
# A determined programmer can still access the mangled name.


# ============================================================
# INTERVIEW NOTE
# ============================================================

# __attribute is not a truly private variable in Python.
# It is a convention with runtime name-mangling support.
# Use private members to avoid accidental cross-class conflicts,
# not to secure sensitive data.
