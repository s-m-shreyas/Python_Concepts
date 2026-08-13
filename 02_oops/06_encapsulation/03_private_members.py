# type: ignore

"""
03_private_members.py

Demonstrates private members in Python.

A private member is typically written with a double underscore
prefix, such as __password or __balance.

Python does not make it totally inaccessible, but it applies
name mangling to prevent accidental naming conflicts.
"""


# ============================================================
# 1. PRIVATE ATTRIBUTE
# ============================================================

class UserAccount:
    """Represent a user account."""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.__password = password

    def check_password(self, entered_password: str) -> bool:
        """Validate the provided password."""
        return entered_password == self.__password


user = UserAccount("sanjay", "secret123")
print(user.username)
print(user.check_password("secret123"))

"""
The password is private, so it is not intended for direct access.
We provide a method to check if the input matches.
"""


# ============================================================
# 2. DIRECT ACCESS IS BLOCKED BY NORMAL NAME
# ============================================================

# This would raise AttributeError:
# print(user.__password)

"""
In normal usage, Python does not allow access to the attribute
using the original name.
The attribute name is internally transformed.
"""


# ============================================================
# 3. NAME MANGLING IN ACTION
# ============================================================

print(user._UserAccount__password)

"""
Python stores the private attribute under a mangled name such as:

    _UserAccount__password

This is why the attribute is still technically accessible via
its mangled form, though this is discouraged.
"""


# ============================================================
# 4. PRIVATE METHODS
# ============================================================

class AuthSystem:
    """Example of a private method."""

    def __init__(self, secret_key: str) -> None:
        self.__secret_key = secret_key

    def validate(self, key: str) -> bool:
        return self.__check_key(key)

    def __check_key(self, key: str) -> bool:
        return key == self.__secret_key


auth = AuthSystem("abc123")
print(auth.validate("abc123"))

"""
The __check_key() method is private. It supports the public
validate() method and hides the internal logic.
"""


# ============================================================
# 5. WHY PRIVATE MEMBERS ARE USEFUL
# ============================================================

# - reduce accidental collisions
# - separate internal implementation from public interface
# - discourage direct modification from outside the class
# - support safer, clearer class design

# However, they are not a security feature in the strict sense.
# Names can still be accessed through mangled names.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __name is a private-style member.
# - Python renames it via name mangling.
# - It prevents accidental clash with other classes.
# - It is not a strict security barrier.
# - It helps create a cleaner public interface.
