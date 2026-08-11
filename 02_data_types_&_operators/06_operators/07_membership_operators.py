# type: ignore
# =============================================================================
# 07. Membership Operators
# =============================================================================
"""
Python Operators

File:
07_membership_operators.py

Topic:
Membership Operators

Overview:
Membership operators are used to test whether a value exists inside
another object.

Python provides two membership operators:

    in
    not in

Examples:

    value in collection
    value not in collection

Membership operators are commonly used with:

    - Strings
    - Lists
    - Tuples
    - Sets
    - Dictionaries
    - Ranges
    - Other iterable or membership-aware objects

The result of a membership operation is always a boolean:

    True
    False
"""

# =============================================================================
# 01. Basic Membership With A List
# =============================================================================

numbers: list[int] = [
    10,
    20,
    30,
]

result: bool = 20 in numbers

print(result)

# 20 exists inside numbers.
#
# Result:
#
# True

# =============================================================================
# 02. Value Not Present In A List
# =============================================================================

numbers = [
    10,
    20,
    30,
]

result = 40 in numbers

print(result)

# 40 does not exist inside numbers.
#
# Result:
#
# False

# =============================================================================
# 03. Using not in
# =============================================================================

numbers = [
    10,
    20,
    30,
]

result = 40 not in numbers

print(result)

# 40 does not exist inside numbers.
#
# Therefore:
#
# 40 not in numbers
#
# is:
#
# True

# =============================================================================
# 04. Membership In A Tuple
# =============================================================================

colors: tuple[str, ...] = (
    "red",
    "green",
    "blue",
)

is_present: bool = "green" in colors

print(is_present)

# Result:
#
# True

# =============================================================================
# 05. Membership Not In A Tuple
# =============================================================================

colors = (
    "red",
    "green",
    "blue",
)

is_missing: bool = "yellow" not in colors

print(is_missing)

# Result:
#
# True

# =============================================================================
# 06. Membership In A Set
# =============================================================================

languages: set[str] = {
    "Python",
    "Java",
    "Go",
}

is_present = "Python" in languages

print(is_present)

# Sets are commonly used when efficient membership testing is important.

# =============================================================================
# 07. Membership Not In A Set
# =============================================================================

languages = {
    "Python",
    "Java",
    "Go",
}

is_missing = "Rust" not in languages

print(is_missing)

# Result:
#
# True

# =============================================================================
# 08. Membership In A String
# =============================================================================

text: str = "Python programming"

result = "Python" in text

print(result)

# Strings support membership testing.
#
# "Python" occurs inside the string.

# =============================================================================
# 09. Substring Membership
# =============================================================================

text = "Python programming"

result = "program" in text

print(result)

# Membership on strings checks whether the left-hand string occurs as
# a substring of the right-hand string.

# =============================================================================
# 10. Substring Not Present
# =============================================================================

text = "Python programming"

result = "Java" not in text

print(result)

# "Java" does not occur inside the string.

# =============================================================================
# 11. String Membership Is Case-Sensitive
# =============================================================================

language = "Python"

lowercase_result: bool = "python" in language
uppercase_result: bool = "Python" in language

print(lowercase_result)
print(uppercase_result)

# String membership is case-sensitive.
#
# "python" != "Python"

# =============================================================================
# 12. Case-Insensitive Membership
# =============================================================================

language = "Python Programming"

search_text: str = "python"

result = search_text.lower() in language.lower()

print(result)

# Both strings are converted to lowercase before the membership test.

# =============================================================================
# 13. Membership In A Range
# =============================================================================

numbers_range: range = range(
    1,
    11,
)

result = 5 in numbers_range

print(result)

# range(1, 11) contains:
#
# 1, 2, 3, ..., 10

# =============================================================================
# 14. Value Outside A Range
# =============================================================================

numbers_range = range(
    1,
    11,
)

result = 20 in numbers_range

print(result)

# 20 is outside the range.

# =============================================================================
# 15. not in With A Range
# =============================================================================

numbers_range = range(
    1,
    11,
)

result = 20 not in numbers_range

print(result)

# Result:
#
# True

# =============================================================================
# 16. Membership With A Step
# =============================================================================

even_numbers: range = range(
    0,
    11,
    2,
)

result = 6 in even_numbers

print(result)

# even_numbers contains:
#
# 0, 2, 4, 6, 8, 10

# =============================================================================
# 17. Number Not Matching A Range Step
# =============================================================================

even_numbers = range(
    0,
    11,
    2,
)

result = 7 in even_numbers

print(result)

# 7 is inside the numeric boundaries but is not produced by the range
# because the step is 2.

# =============================================================================
# 18. Membership In A Dictionary
# =============================================================================

user: dict[str, str] = {
    "name": "Alex",
    "role": "Developer",
    "language": "Python",
}

result = "name" in user

print(result)

# Dictionary membership checks keys by default.

# =============================================================================
# 19. Dictionary Key Not Present
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
    "language": "Python",
}

result = "age" not in user

print(result)

# "age" is not a key in the dictionary.

# =============================================================================
# 20. Dictionary Membership Checks Keys
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
}

key_result: bool = "name" in user
value_result: bool = "Alex" in user

print(key_result)
print(value_result)

# "name" is a key:
#
# True
#
# "Alex" is a value, not a key:
#
# False

# =============================================================================
# 21. Explicit Dictionary Key Membership
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
}

result = "name" in user.keys()

print(result)

# This explicitly checks dictionary keys.

# =============================================================================
# 22. Dictionary Value Membership
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
}

result = "Developer" in user.values()

print(result)

# Use .values() when you specifically want to search dictionary values.

# =============================================================================
# 23. Dictionary Item Membership
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
}

result = ("name", "Alex") in user.items()

print(result)

# .items() exposes key-value pairs.
#
# Therefore a tuple containing the key and value can be tested.

# =============================================================================
# 24. Membership In Dictionary Items
# =============================================================================

user = {
    "name": "Alex",
    "role": "Developer",
}

result = ("role", "Admin") not in user.items()

print(result)

# The exact key-value pair does not exist.

# =============================================================================
# 25. Membership In A List Of Strings
# =============================================================================

supported_languages: list[str] = [
    "Python",
    "Java",
    "Go",
    "Rust",
]

language = "Python"

is_supported: bool = language in supported_languages

print(is_supported)

# Membership testing is often useful for validation.

# =============================================================================
# 26. Membership Validation Function
# =============================================================================

def is_supported_language(
    language: str,
) -> bool:
    """
    Return whether a language is supported.
    """
    supported_languages: set[str] = {
        "Python",
        "Java",
        "Go",
        "Rust",
    }

    return language in supported_languages


result = is_supported_language(
    "Python",
)

print(result)

# A set is a useful choice when the primary operation is membership testing.

# =============================================================================
# 27. not in For Validation
# =============================================================================

blocked_users: set[str] = {
    "admin",
    "guest",
    "anonymous",
}

username: str = "developer"

is_allowed: bool = username not in blocked_users

print(is_allowed)

# not in can make validation conditions easy to read.

# =============================================================================
# 28. Membership In A Tuple Of Choices
# =============================================================================

status: str = "active"

valid_statuses: tuple[str, ...] = (
    "active",
    "inactive",
    "pending",
)

is_valid: bool = status in valid_statuses

print(is_valid)

# This is useful when a value must belong to a known set of choices.

# =============================================================================
# 29. Membership In A Set Of Choices
# =============================================================================

status = "active"

valid_statuses: set[str] = {
    "active",
    "inactive",
    "pending",
}

is_valid = status in valid_statuses

print(is_valid)

# A set is especially useful when the collection represents unique choices.

# =============================================================================
# 30. Membership Inside An if Statement
# =============================================================================

username = "admin"

administrators: set[str] = {
    "admin",
    "root",
    "superuser",
}

if username in administrators:
    print("Administrator access")

# Membership expressions return booleans and can be used directly in
# conditional statements.

# =============================================================================
# 31. not in Inside An if Statement
# =============================================================================

username = "developer"

blocked_users = {
    "admin",
    "guest",
}

if username not in blocked_users:
    print("Access allowed")

# =============================================================================
# 32. Membership In A Nested List
# =============================================================================

rows: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

result = [4, 5, 6] in rows

print(result)

# Membership checks each complete inner list as an element.

# =============================================================================
# 33. Nested Membership Does Not Search Recursively
# =============================================================================

rows = [
    [1, 2, 3],
    [4, 5, 6],
]

result = 4 in rows

print(result)

# 4 is inside an inner list, but it is not directly an element of rows.
#
# Therefore:
#
# False

# =============================================================================
# 34. Nested Membership With any()
# =============================================================================

rows = [
    [1, 2, 3],
    [4, 5, 6],
]

target: int = 5

result = any(
    target in row
    for row in rows
)

print(result)

# any() can be combined with membership testing when searching nested
# collections.

# =============================================================================
# 35. Membership In A List Of Tuples
# =============================================================================

coordinates: list[tuple[int, int]] = [
    (0, 0),
    (1, 2),
    (3, 4),
]

result = (1, 2) in coordinates

print(result)

# Membership compares the complete tuple.

# =============================================================================
# 36. Membership In A List Of Dictionaries
# =============================================================================

users: list[dict[str, str]] = [
    {
        "name": "Alex",
        "role": "Developer",
    },
    {
        "name": "Sam",
        "role": "Designer",
    },
]

target_user: dict[str, str] = {
    "name": "Alex",
    "role": "Developer",
}

result = target_user in users

print(result)

# Dictionary membership inside the list uses equality between dictionary
# objects.

# =============================================================================
# 37. Membership With None
# =============================================================================

value: str | None = None

result = None in [
    "Python",
    None,
    "Go",
]

print(result)

# None can be an element of a collection.

# =============================================================================
# 38. Membership With Boolean Values
# =============================================================================

values: list[bool] = [
    True,
    False,
]

result = True in values

print(result)

# Boolean values can be tested like other values.

# =============================================================================
# 39. Membership With Integers
# =============================================================================

values: set[int] = {
    10,
    20,
    30,
}

result = 20 in values

print(result)

# =============================================================================
# 40. Membership With Floating-Point Values
# =============================================================================

values: list[float] = [
    1.5,
    2.5,
    3.5,
]

result = 2.5 in values

print(result)

# Floating-point membership uses equality semantics, so be careful when
# comparing calculated floating-point values.

# =============================================================================
# 41. Membership And Floating-Point Precision
# =============================================================================

values: list[float] = [
    0.1 + 0.2,
]

result = 0.3 in values

print(result)

# Floating-point calculations can contain representation differences.
#
# Therefore exact membership checks on calculated floating-point values
# may not behave as mathematically expected.

# =============================================================================
# 42. Membership With Bytes
# =============================================================================

data: bytes = b"Python"

result = b"Py" in data

print(result)

# bytes supports membership testing.

# =============================================================================
# 43. Membership With Byte Values
# =============================================================================

data = b"Python"

result = 80 in data

print(result)

# Integer membership in bytes checks whether the byte value occurs.
#
# ASCII:
#
# P -> 80

# =============================================================================
# 44. Membership With A Generator
# =============================================================================

def generate_numbers():
    """
    Generate a sequence of numbers.
    """
    yield 1
    yield 2
    yield 3


numbers_generator = generate_numbers()

result = 2 in numbers_generator

print(result)

# Membership testing can consume values from an iterator or generator
# until the requested value is found or the iterator is exhausted.

# =============================================================================
# 45. Membership Can Consume An Iterator
# =============================================================================

def generate_values():
    """
    Generate three values.
    """
    yield 1
    yield 2
    yield 3


values_generator = generate_values()

first_result: bool = 2 in values_generator
second_result: bool = 2 in values_generator

print(first_result)
print(second_result)

# The first membership test consumes values until it finds 2.
#
# The generator is now positioned after 2.
#
# A second search may therefore produce a different result.

# =============================================================================
# 46. Membership With A Custom Class
# =============================================================================

class NumberCollection:
    """
    Demonstrate custom membership behaviour.
    """

    def __init__(
        self,
        numbers: list[int],
    ) -> None:
        self.numbers: list[int] = numbers

    def __contains__(
        self,
        value: object,
    ) -> bool:
        return value in self.numbers


collection = NumberCollection(
    [10, 20, 30],
)

result = 20 in collection

print(result)

# __contains__ allows a class to define custom behaviour for:
#
#     value in object

# =============================================================================
# 47. Custom Membership With not in
# =============================================================================

class UsernameCollection:
    """
    Demonstrate custom membership testing.
    """

    def __init__(
        self,
        usernames: set[str],
    ) -> None:
        self.usernames: set[str] = usernames

    def __contains__(
        self,
        username: object,
    ) -> bool:
        return username in self.usernames


usernames = UsernameCollection(
    {
        "alex",
        "sam",
    },
)

result = "john" not in usernames

print(result)

# not in uses the membership protocol as well.

# =============================================================================
# 48. Membership And any()
# =============================================================================

words: list[str] = [
    "Python",
    "programming",
    "language",
]

search_terms: tuple[str, ...] = (
    "Python",
    "Java",
)

found: bool = any(
    term in words
    for term in search_terms
)

print(found)

# any() returns True when at least one membership condition is True.

# =============================================================================
# 49. Membership And all()
# =============================================================================

required_permissions: tuple[str, ...] = (
    "read",
    "write",
)

user_permissions: set[str] = {
    "read",
    "write",
    "execute",
}

has_all_permissions: bool = all(
    permission in user_permissions
    for permission in required_permissions
)

print(has_all_permissions)

# all() returns True only when every requested permission exists.

# =============================================================================
# 50. Practical Membership Validation
# =============================================================================

def validate_role(
    role: str,
) -> str:
    """
    Validate a role using membership operators.
    """
    valid_roles: set[str] = {
        "admin",
        "developer",
        "designer",
        "manager",
    }

    if role not in valid_roles:
        return "Invalid role"

    return "Valid role"


valid_role_result: str = validate_role(
    "developer",
)

invalid_role_result: str = validate_role(
    "guest",
)

print(valid_role_result)
print(invalid_role_result)

# This is one of the most common practical uses of membership operators:
#
#     if value not in allowed_values:
#         ...
#
# or:
#
#     if value in allowed_values:
#         ...

# =============================================================================
# Membership Operators Summary
# =============================================================================

"""
The two membership operators are:

    in
    not in

Examples:

    value in collection

    value not in collection

The result is always:

    True
    False

Common collections supporting membership testing include:

    - str
    - list
    - tuple
    - set
    - dict
    - range
    - bytes
    - generators
    - custom objects implementing membership behaviour

Important dictionary rule:

    value in dictionary

checks dictionary keys.

For dictionary values:

    value in dictionary.values()

For dictionary key-value pairs:

    (key, value) in dictionary.items()

Important string rule:

    substring in string

checks whether the substring occurs inside the string.

String membership is case-sensitive:

    "Python" in "Python programming"
    -> True

    "python" in "Python programming"
    -> False

Important set rule:

Sets are commonly useful when membership testing is a primary operation.

Bitwise operators and membership operators are different:

    bitwise:
        value & mask

    membership:
        value in collection
"""

# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Python has two membership operators:

    in
    not in

✓ Membership operators return boolean values.

✓ Use in to check whether a value exists in a collection.

✓ Use not in to check whether a value does not exist in a collection.

✓ Strings support substring membership.

✓ String membership is case-sensitive.

✓ Lists support membership testing.

✓ Tuples support membership testing.

✓ Sets support membership testing.

✓ Dictionaries check keys by default.

✓ Use dictionary.values() to check values.

✓ Use dictionary.items() to check key-value pairs.

✓ range objects support membership testing.

✓ Membership can be used directly in if statements.

✓ Membership is commonly used for validation.

✓ Sets are often a good choice for collections whose main purpose is
  membership testing.

✓ Nested collections are not searched recursively by in.

✓ any() can combine multiple membership checks.

✓ all() can verify that multiple values are members of a collection.

✓ Generators and iterators can be consumed by membership tests.

✓ Custom classes can implement __contains__() to define membership
  behaviour.

Core model:

    VALUE
      ↓
    in / not in
      ↓
    COLLECTION
      ↓
    True / False

Common patterns:

    if value in allowed_values:
        ...

    if value not in blocked_values:
        ...

    key in dictionary

    value in dictionary.values()

    (key, value) in dictionary.items()

    substring in text

    all(
        value in collection
        for value in required_values
    )

    any(
        value in collection
        for value in candidate_values
    )

The main idea:

    MEMBERSHIP OPERATOR
          ↓
    "Does this value exist here?"
          ↓
       in / not in
          ↓
       True / False
"""

# =============================================================================
# End of 07_membership_operators.py
# =============================================================================