# type: ignore
# =============================================================================
# 08. Identity Operators
# =============================================================================
"""
Python Operators

File:
    08_identity_operators.py

Topic:
    Identity Operators

Overview:
    Identity operators are used to determine whether two names refer to
    the same object in memory.

Python provides two identity operators:

    is
        Returns True when two references point to the same object.

    is not
        Returns True when two references do not point to the same object.

Identity comparison is different from equality comparison.

Equality:
    ==
        Checks whether two objects have equivalent values.

Identity:
    is
        Checks whether two references point to the same object.

General rule:

    ==  -> same value
    is  -> same object

Identity operators are especially useful when checking against None.

Recommended:

    if value is None:
        ...

Avoid:

    if value == None:
        ...

This file contains practical examples of identity operators.
"""

# =============================================================================
# 01. Basic `is` Operator
# =============================================================================

first_number: int = 100
second_number: int = first_number

same_object: bool = first_number is second_number

print(same_object)


# =============================================================================
# 02. Basic `is not` Operator
# =============================================================================

first_list: list[int] = [1, 2, 3]
second_list: list[int] = [1, 2, 3]

different_objects: bool = first_list is not second_list

print(different_objects)


# =============================================================================
# 03. `is` Versus `==`
# =============================================================================

first_values: list[int] = [10, 20, 30]
second_values: list[int] = [10, 20, 30]

print(first_values == second_values)
print(first_values is second_values)

# `==` checks value equality.
# `is` checks object identity.


# =============================================================================
# 04. Two Variables Referencing the Same List
# =============================================================================

original_list: list[str] = ["Python", "SQL"]
alias_list: list[str] = original_list

print(original_list == alias_list)
print(original_list is alias_list)


# =============================================================================
# 05. Two Separate Lists With the Same Values
# =============================================================================

list_one: list[str] = ["Python", "SQL"]
list_two: list[str] = ["Python", "SQL"]

print(list_one == list_two)
print(list_one is list_two)


# =============================================================================
# 06. Identity After Assignment
# =============================================================================

source: list[int] = [1, 2, 3]
reference: list[int] = source

print(source is reference)


# =============================================================================
# 07. Identity After Mutation
# =============================================================================

numbers: list[int] = [1, 2, 3]
same_numbers: list[int] = numbers

numbers.append(4)

print(numbers)
print(same_numbers)
print(numbers is same_numbers)


# =============================================================================
# 08. Mutation Does Not Change Identity
# =============================================================================

items: list[str] = ["Python"]
items_reference: list[str] = items

before_identity: bool = items is items_reference

items.append("SQL")

after_identity: bool = items is items_reference

print(before_identity)
print(after_identity)


# =============================================================================
# 09. Rebinding Changes the Reference
# =============================================================================

first_items: list[str] = ["Python"]
second_items: list[str] = first_items

print(first_items is second_items)

second_items = ["SQL"]

print(first_items is second_items)


# =============================================================================
# 10. Identity With None
# =============================================================================

value: str | None = None

if value is None:
    print("Value is None.")


# =============================================================================
# 11. `is not None`
# =============================================================================

username: str | None = "Shreyas"

if username is not None:
    print(username)


# =============================================================================
# 12. Function Returning None
# =============================================================================

def perform_action() -> None:
    """Perform an action without returning a value."""
    print("Action completed.")


result: None = perform_action()

if result is None:
    print("The function returned None.")


# =============================================================================
# 13. Checking Optional Values
# =============================================================================

def get_username() -> str | None:
    """Return a username or None."""
    return "Alex"


user: str | None = get_username()

if user is not None:
    print(f"Username: {user}")


# =============================================================================
# 14. Identity With Empty Lists
# =============================================================================

empty_list_one: list[int] = []
empty_list_two: list[int] = []

print(empty_list_one == empty_list_two)
print(empty_list_one is empty_list_two)


# =============================================================================
# 15. Identity With Empty Dictionaries
# =============================================================================

empty_dict_one: dict[str, int] = {}
empty_dict_two: dict[str, int] = {}

print(empty_dict_one == empty_dict_two)
print(empty_dict_one is empty_dict_two)


# =============================================================================
# 16. Identity With Empty Sets
# =============================================================================

empty_set_one: set[int] = set()
empty_set_two: set[int] = set()

print(empty_set_one == empty_set_two)
print(empty_set_one is empty_set_two)


# =============================================================================
# 17. Same Dictionary Object
# =============================================================================

user_data: dict[str, str] = {
    "name": "Alex",
}

user_data_reference: dict[str, str] = user_data

print(user_data is user_data_reference)


# =============================================================================
# 18. Different Dictionary Objects
# =============================================================================

first_user: dict[str, str] = {
    "name": "Alex",
}

second_user: dict[str, str] = {
    "name": "Alex",
}

print(first_user == second_user)
print(first_user is second_user)


# =============================================================================
# 19. Same Set Object
# =============================================================================

first_set: set[int] = {1, 2, 3}
second_set: set[int] = first_set

print(first_set is second_set)


# =============================================================================
# 20. Different Set Objects
# =============================================================================

set_one: set[int] = {1, 2, 3}
set_two: set[int] = {1, 2, 3}

print(set_one == set_two)
print(set_one is set_two)


# =============================================================================
# 21. Tuple Identity
# =============================================================================

first_tuple: tuple[int, int] = (1, 2)
second_tuple: tuple[int, int] = first_tuple

print(first_tuple is second_tuple)


# =============================================================================
# 22. Separate Tuple Objects
# =============================================================================

tuple_one: tuple[int, int] = (1, 2)
tuple_two: tuple[int, int] = (1, 2)

print(tuple_one == tuple_two)

# Identity of immutable objects should not be inferred from value equality.
# Use == when comparing values.


# =============================================================================
# 23. String Identity
# =============================================================================

first_name: str = "Python"
second_name: str = first_name

print(first_name is second_name)


# =============================================================================
# 24. String Equality Versus Identity
# =============================================================================

language_one: str = "Python"
language_two: str = "".join(["Py", "thon"])

print(language_one == language_two)
print(language_one is language_two)


# =============================================================================
# 25. Integer Equality Versus Identity
# =============================================================================

number_one: int = 1000
number_two: int = 1000

print(number_one == number_two)

# Do not use `is` to compare ordinary numeric values.
print(number_one is number_two)


# =============================================================================
# 26. Correct Numeric Comparison
# =============================================================================

score_one: int = 1000
score_two: int = 1000

if score_one == score_two:
    print("Scores are equal.")


# =============================================================================
# 27. Identity With a Sentinel Object
# =============================================================================

NOT_FOUND: object = object()

result_value: object = NOT_FOUND

if result_value is NOT_FOUND:
    print("Result was not found.")


# =============================================================================
# 28. Sentinel Object With Different Objects
# =============================================================================

MISSING: object = object()

actual_value: object = object()

print(actual_value is MISSING)
print(actual_value is not MISSING)


# =============================================================================
# 29. Function Using a Sentinel
# =============================================================================

DEFAULT_SENTINEL: object = object()


def find_value(
    value: str | None = None,
) -> str:
    """Return a supplied value or a default message."""
    if value is None:
        return "Default value."

    return value


print(find_value())
print(find_value("Python"))


# =============================================================================
# 30. Identity With Custom Objects
# =============================================================================

class User:
    """Represent a simple user object."""

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name


user_one: User = User("Alex")
user_two: User = user_one

print(user_one is user_two)


# =============================================================================
# 31. Two Separate Custom Objects
# =============================================================================

customer_one: User = User("Alex")
customer_two: User = User("Alex")

print(customer_one is customer_two)


# =============================================================================
# 32. Custom Objects Can Have Equal Data But Different Identity
# =============================================================================

person_one: User = User("Alex")
person_two: User = User("Alex")

print(person_one.name == person_two.name)
print(person_one is person_two)


# =============================================================================
# 33. Identity After Reassignment
# =============================================================================

object_one: User = User("Alex")
object_two: User = object_one

print(object_one is object_two)

object_two = User("Alex")

print(object_one is object_two)


# =============================================================================
# 34. Identity With Function Results
# =============================================================================

def create_user() -> User:
    """Create and return a new User object."""
    return User("Alex")


created_user_one: User = create_user()
created_user_two: User = create_user()

print(created_user_one is created_user_two)


# =============================================================================
# 35. Function Returning the Same Object
# =============================================================================

shared_user: User = User("Alex")


def get_shared_user() -> User:
    """Return the existing shared user object."""
    return shared_user


returned_user_one: User = get_shared_user()
returned_user_two: User = get_shared_user()

print(returned_user_one is returned_user_two)


# =============================================================================
# 36. Identity Through Function Parameters
# =============================================================================

def check_identity(
    first: list[int],
    second: list[int],
) -> bool:
    """Return whether two parameters reference the same object."""
    return first is second


shared_numbers: list[int] = [1, 2, 3]

print(check_identity(shared_numbers, shared_numbers))


# =============================================================================
# 37. Same Object Passed Twice
# =============================================================================

values: list[int] = [10, 20, 30]

same_reference_result: bool = check_identity(
    values,
    values,
)

print(same_reference_result)


# =============================================================================
# 38. Different Objects Passed to a Function
# =============================================================================

values_one: list[int] = [10, 20, 30]
values_two: list[int] = [10, 20, 30]

different_reference_result: bool = check_identity(
    values_one,
    values_two,
)

print(different_reference_result)


# =============================================================================
# 39. Identity Check Inside a Function
# =============================================================================

def describe_identity(
    first: object,
    second: object,
) -> str:
    """Describe whether two references point to the same object."""
    if first is second:
        return "Same object."

    return "Different objects."


first_object: list[int] = [1, 2]
second_object: list[int] = first_object

print(describe_identity(first_object, second_object))


# =============================================================================
# 40. `is not` With Separate Objects
# =============================================================================

first_object = [1, 2, 3]
second_object = [1, 2, 3]

if first_object is not second_object:
    print("These are different objects.")


# =============================================================================
# 41. Identity and Aliasing
# =============================================================================

original: dict[str, int] = {
    "python": 1,
}

alias: dict[str, int] = original

print(original is alias)

alias["sql"] = 2

print(original)


# =============================================================================
# 42. Identity and Copying
# =============================================================================

import copy

original_data: list[int] = [1, 2, 3]
copied_data: list[int] = copy.copy(original_data)

print(original_data == copied_data)
print(original_data is copied_data)


# =============================================================================
# 43. Shallow Copy Creates a Different Outer Object
# =============================================================================

source_data: list[int] = [10, 20]
shallow_copy: list[int] = source_data.copy()

print(source_data == shallow_copy)
print(source_data is shallow_copy)


# =============================================================================
# 44. Deep Copy Creates a Different Object
# =============================================================================

nested_data: list[list[int]] = [
    [1, 2],
    [3, 4],
]

deep_copied_data: list[list[int]] = copy.deepcopy(nested_data)

print(nested_data == deep_copied_data)
print(nested_data is deep_copied_data)


# =============================================================================
# 45. Identity of Nested Objects After Shallow Copy
# =============================================================================

nested_source: list[list[int]] = [
    [1, 2],
]

nested_shallow_copy: list[list[int]] = nested_source.copy()

print(nested_source is nested_shallow_copy)
print(nested_source[0] is nested_shallow_copy[0])


# =============================================================================
# 46. Identity of Nested Objects After Deep Copy
# =============================================================================

nested_original: list[list[int]] = [
    [1, 2],
]

nested_deep_copy: list[list[int]] = copy.deepcopy(nested_original)

print(nested_original is nested_deep_copy)
print(nested_original[0] is nested_deep_copy[0])


# =============================================================================
# 47. Identity Is Not Equality
# =============================================================================

first_data: list[str] = ["A", "B"]
second_data: list[str] = ["A", "B"]

if first_data == second_data:
    print("The objects contain equal values.")

if first_data is not second_data:
    print("The objects are different objects.")


# =============================================================================
# 48. Correct None Checking
# =============================================================================

def process_value(
    value: str | None,
) -> str:
    """Process a value using an identity check for None."""
    if value is None:
        return "No value provided."

    return f"Value: {value}"


print(process_value(None))
print(process_value("Python"))


# =============================================================================
# 49. `is not None` in a Function
# =============================================================================

def display_value(
    value: int | None,
) -> None:
    """Display a value when it is not None."""
    if value is not None:
        print(f"Value: {value}")
        return

    print("Value is None.")


display_value(100)
display_value(None)


# =============================================================================
# 50. Practical Identity Comparison
# =============================================================================

def compare_objects(
    first: object,
    second: object,
) -> None:
    """Demonstrate the difference between equality and identity."""
    print(f"Equal values: {first == second}")
    print(f"Same object: {first is second}")


first_list: list[int] = [1, 2, 3]
second_list: list[int] = [1, 2, 3]
third_list: list[int] = first_list

compare_objects(
    first_list,
    second_list,
)

compare_objects(
    first_list,
    third_list,
)


# =============================================================================
# Identity Operators Summary
# =============================================================================
"""
Identity operators:

    is
        Checks whether two references point to the same object.

    is not
        Checks whether two references point to different objects.

Equality operators:

    ==
        Checks whether two objects have equal values.

    !=
        Checks whether two objects have different values.

Important:

    a == b
        Does not mean that a and b are the same object.

    a is b
        Means that a and b refer to the same object.

Examples:

    first = [1, 2, 3]
    second = [1, 2, 3]

    first == second
        True

    first is second
        False

But:

    first = [1, 2, 3]
    second = first

    first == second
        True

    first is second
        True

Best practice:

    Use == when comparing values.

    Use is when checking object identity.

    Use is None when checking for None.

    Use is not None when checking that a value is not None.

Avoid using `is` for ordinary value comparisons such as:

    number is 100
    string is "Python"

Those comparisons are about values, not object identity.

Core model:

    ==      -> equality
    !=      -> inequality

    is      -> same object
    is not  -> different object

Most important practical pattern:

    if value is None:
        ...

    if value is not None:
        ...

Identity is about references to objects, not merely whether two objects
contain the same data.
"""

# =============================================================================
# End of 08_identity_operators.py
# =============================================================================