# =============================================================================
#
# Python Functions
#
# File
#
# 08_return_statement.py
#
# Topic
#
# Return Statement
#
# =============================================================================

# """

# Overview

# The return statement is used to send a value from a function back to the
# code that called the function.

# A function can:

# - return a value
# - return multiple values
# - return None
# - return early
# - return different values from different branches
# - return the result of an expression
# - return another function's result
# - return collections
# - return tuples
# - return dictionaries
# - return objects
# - use return inside conditional statements
# - use return inside loops
# - use return to stop function execution
# - use return without an expression
# - assign a returned value to a variable
# - pass a returned value directly to another function
# - unpack multiple returned values
# - understand the difference between print() and return
# - understand unreachable code after return
# - understand that return exits only the current function
# - understand how return interacts with nested functions
# - understand return annotations
# - understand returning mutable objects
# - understand returning newly created objects
# - understand returning None explicitly
# - understand implicit None
# - understand return in recursive functions
# - understand return in exception handling
# - understand return inside try/finally
# - understand the importance of consistent return behaviour

# """


# =============================================================================
#
# 01. Basic Return Statement
#
# =============================================================================

def greet_user(
    user_name: str,
) -> str:
    """
    Return a greeting for a user.
    """
    return (
        f"Hello, {user_name}!"
    )


greeting: str = greet_user(
    "Shreyas"
)

print(
    greeting
)

# The return statement sends a value back to the caller.

#

# Therefore:

#

# greet_user(
#     "Shreyas"
# )

#

# returns:

#

# "Hello, Shreyas!"

#

# The returned value can then be stored in a variable.


# =============================================================================
#
# 02. Return Ends Function Execution
#
# =============================================================================

def get_message() -> str:
    """
    Return a message and stop function execution.
    """
    return (
        "Process completed"
    )

    # This code is never reached.

    print(
        "This will never execute"
    )


message: str = get_message()

print(
    message
)

# Once Python executes return:

#

# return value

#

# the current function immediately ends.

#

# Any code written after that return statement in the same execution path
# cannot be reached.


# =============================================================================
#
# 03. Return Can Return a Number
#
# =============================================================================

def calculate_square(
    number: int,
) -> int:
    """
    Return the square of a number.
    """
    return (
        number
        ** 2
    )


square: int = calculate_square(
    5
)

print(
    square
)

# return can return numeric values.

#

# Here:

#

# return number ** 2

#

# sends the calculated integer back to the caller.


# =============================================================================
#
# 04. Return Can Return a String
#
# =============================================================================

def create_username(
    first_name: str,
    last_name: str,
) -> str:
    """
    Return a username.
    """
    return (
        f"{first_name.lower()}."
        f"{last_name.lower()}"
    )


username: str = create_username(
    "Alex",
    "Morgan",
)

print(
    username
)

# A function can return strings just like it can return numbers.


# =============================================================================
#
# 05. Return Can Return a Boolean
#
# =============================================================================

def is_even(
    number: int,
) -> bool:
    """
    Return whether a number is even.
    """
    return (
        number % 2 == 0
    )


even_result: bool = is_even(
    10
)

print(
    even_result
)

# The expression:

#

# number % 2 == 0

#

# produces a boolean value.

#

# return sends that boolean value back to the caller.


# =============================================================================
#
# 06. Return Can Return a List
#
# =============================================================================

def create_numbers(
    count: int,
) -> list[int]:
    """
    Return a list of numbers.
    """
    return (
        list(
            range(
                1,
                count + 1,
            )
        )
    )


numbers: list[int] = create_numbers(
    5
)

print(
    numbers
)

# return can return any Python object.

#

# Here the returned object is a list.


# =============================================================================
#
# 07. Return Can Return a Dictionary
#
# =============================================================================

def create_profile() -> dict[str, object]:
    """
    Return a profile dictionary.
    """
    return {
        "name": "Alex",
        "age": 30,
        "city": "Bengaluru",
    }


profile: dict[str, object] = create_profile()

print(
    profile
)

# Dictionaries can also be returned directly.


# =============================================================================
#
# 08. Return Can Return a Tuple
#
# =============================================================================

def get_coordinates() -> tuple[int, int]:
    """
    Return coordinates as a tuple.
    """
    return (
        12,
        77,
    )


coordinates: tuple[int, int] = get_coordinates()

print(
    coordinates
)

# The returned value is a tuple:

#

# (
#     12,
#     77,
# )


# =============================================================================
#
# 09. Return Multiple Values
#
# =============================================================================

def calculate_values(
    first: int,
    second: int,
) -> tuple[int, int, int]:
    """
    Return sum, difference, and product.
    """
    return (
        first + second,
        first - second,
        first * second,
    )


calculated_values: tuple[int, int, int] = calculate_values(
    10,
    5,
)

print(
    calculated_values
)

# Python does not technically return several separate values.

#

# The expression:

#

# return (
#     first + second,
#     first - second,
#     first * second,
# )

#

# returns one tuple containing three values.

#

# Therefore the result is:

#

# (
#     15,
#     5,
#     50,
# )


# =============================================================================
#
# 10. Unpacking Multiple Returned Values
#
# =============================================================================

def get_user_data() -> tuple[str, int, str]:
    """
    Return multiple pieces of user information.
    """
    return (
        "Alex",
        30,
        "Bengaluru",
    )


user_name, user_age, user_city = get_user_data()

print(
    user_name
)

print(
    user_age
)

print(
    user_city
)

# The returned tuple can be unpacked directly.

#

# Therefore:

#

# user_name, user_age, user_city

#

# receives:

#

# "Alex"

# 30

# "Bengaluru"


# =============================================================================
#
# 11. Return Without Storing the Result
#
# =============================================================================

def get_status() -> str:
    """
    Return a status message.
    """
    return (
        "OK"
    )


print(
    get_status()
)

# The returned value does not have to be stored in a variable.

#

# It can be passed directly to another function.


# =============================================================================
#
# 12. Return Value Can Be Passed to Another Function
#
# =============================================================================

def get_number() -> int:
    """
    Return a number.
    """
    return (
        10
    )


def double_number(
    number: int,
) -> int:
    """
    Return double the supplied number.
    """
    return (
        number
        * 2
    )


doubled_number: int = double_number(
    get_number()
)

print(
    doubled_number
)

# The result of one function can become the argument of another function.

#

# First:

#

# get_number()

# ↓

# 10

#

# Then:

#

# double_number(
#     10
# )

# ↓

# 20


# =============================================================================
#
# 13. Return Expression
#
# =============================================================================

def calculate_total(
    price: float,
    quantity: int,
) -> float:
    """
    Return the calculated total.
    """
    return (
        price
        * quantity
    )


total: float = calculate_total(
    1500.0,
    3,
)

print(
    total
)

# return can contain an expression.

#

# Python evaluates the expression first.

#

# Then the resulting value is returned.


# =============================================================================
#
# 14. Return a Variable
#
# =============================================================================

def calculate_discount(
    price: float,
    discount_percentage: float,
) -> float:
    """
    Calculate and return the discount amount.
    """
    discount_amount: float = (
        price
        * discount_percentage
        / 100
    )

    return (
        discount_amount
    )


discount: float = calculate_discount(
    1000.0,
    10.0,
)

print(
    discount
)

# The return statement can return an existing variable.

#

# Here:

#

# discount_amount

#

# is returned.


# =============================================================================
#
# 15. Return an Expression Directly
#
# =============================================================================

def calculate_discount_directly(
    price: float,
    discount_percentage: float,
) -> float:
    """
    Return the discount amount directly.
    """
    return (
        price
        * discount_percentage
        / 100
    )


discount_direct: float = calculate_discount_directly(
    1000.0,
    10.0,
)

print(
    discount_direct
)

# These two styles can produce the same result:

#

# calculate a variable first

#

# or:

#

# return the expression directly


# =============================================================================
#
# 16. Return None Explicitly
#
# =============================================================================

# mypy: ignore-errors

def perform_task() -> None:
    """
    Perform a task and explicitly return None.
    """
    print(
        "Task completed"
    )

    return None


task_result: None = perform_task()

print(
    task_result
)

# A function can explicitly return None.

#

# None represents the absence of a meaningful value.


# =============================================================================
#
# 17. Return Without a Value
#
# =============================================================================

def stop_process(
    should_stop: bool,
) -> None:
    """
    Stop execution when requested.
    """
    if should_stop:
        return

    print(
        "Process continues"
    )


stop_process(
    True
)

stop_process(
    False
)

# A bare return:

#

# return

#

# immediately exits the function.

#

# It behaves as though:

#

# return None

#

# had been used.


# =============================================================================
#
# 18. Function Without Return
#
# =============================================================================

def print_message() -> None:
    """
    Print a message without returning a value.
    """
    print(
        "Hello from the function"
    )


result: None = print_message()

print(
    result
)

# If a function reaches the end without executing return:

#

# Python implicitly returns:

#

# None


# =============================================================================
#
# 19. Explicit None vs Implicit None
#
# =============================================================================

def explicit_none() -> None:
    """
    Explicitly return None.
    """
    return None


def implicit_none() -> None:
    """
    Reach the end without a return statement.
    """
    pass


explicit_result: None = explicit_none()

implicit_result: None = implicit_none()

print(
    explicit_result
)

print(
    implicit_result
)

# Both functions return None.

#

# The difference is only how the result is produced.

#

# Explicit:

#

# return None

#

# Implicit:

#

# function reaches the end


# =============================================================================
#
# 20. Return With if
#
# =============================================================================

def classify_number(
    number: int,
) -> str:
    """
    Return a classification based on a number.
    """
    if number > 0:
        return (
            "positive"
        )

    if number < 0:
        return (
            "negative"
        )

    return (
        "zero"
    )


positive: str = classify_number(
    10
)

negative: str = classify_number(
    -10
)

zero: str = classify_number(
    0
)

print(
    positive
)

print(
    negative
)

print(
    zero
)

# Different return statements can execute depending on the condition.


# =============================================================================
#
# 21. Return With if and else
#
# =============================================================================

def get_access_status(
    age: int,
) -> str:
    """
    Return access status based on age.
    """
    if age >= 18:
        return (
            "Access granted"
        )
    else:
        return (
            "Access denied"
        )


adult_status: str = get_access_status(
    25
)

minor_status: str = get_access_status(
    15
)

print(
    adult_status
)

print(
    minor_status
)

# Each branch returns a different value.


# =============================================================================
#
# 22. Return Can Make else Unnecessary
#
# =============================================================================

def get_access_status_early(
    age: int,
) -> str:
    """
    Return access status using an early return.
    """
    if age < 18:
        return (
            "Access denied"
        )

    return (
        "Access granted"
    )


access_status: str = get_access_status_early(
    25
)

print(
    access_status
)

# Because return immediately exits the function:

#

# if age < 18:
#     return "Access denied"

#

# the remaining code only executes when the condition is false.

#

# Therefore an else block is not required.


# =============================================================================
#
# 23. Multiple Return Statements
#
# =============================================================================

def get_grade(
    score: int,
) -> str:
    """
    Return a grade based on the score.
    """
    if score >= 90:
        return (
            "A"
        )

    if score >= 80:
        return (
            "B"
        )

    if score >= 70:
        return (
            "C"
        )

    if score >= 60:
        return (
            "D"
        )

    return (
        "F"
    )


grade_a: str = get_grade(
    95
)

grade_b: str = get_grade(
    85
)

grade_f: str = get_grade(
    45
)

print(
    grade_a
)

print(
    grade_b
)

print(
    grade_f
)

# A function may contain multiple return statements.

#

# Only the first return statement reached during execution is executed.


# =============================================================================
#
# 24. Return Inside a Loop
#
# =============================================================================

def find_first_even(
    numbers: list[int],
) -> int | None:
    """
    Return the first even number.
    """
    for number in numbers:
        if number % 2 == 0:
            return (
                number
            )

    return None


first_even: int | None = find_first_even(
    [1, 3, 7, 8, 11]
)

print(
    first_even
)

# return inside a loop immediately exits the entire function.

#

# It does not merely skip the current loop iteration.

#

# Once an even number is found:

#

# return number

#

# ends the function.


# =============================================================================
#
# 25. Return None When No Result Exists
#
# =============================================================================

def find_user(
    user_id: int,
) -> str | None:
    """
    Return a user name if the ID is known.
    """
    users: dict[int, str] = {
        1: "Alex",
        2: "Sam",
    }

    if user_id in users:
        return (
            users[user_id]
        )

    return None


existing_user: str | None = find_user(
    1
)

missing_user: str | None = find_user(
    99
)

print(
    existing_user
)

print(
    missing_user
)

# None is often used to represent:

#

# no result

# not found

# unavailable value

# absence of data


# =============================================================================
#
# 26. Checking a Returned None
#
# =============================================================================

found_user: str | None = find_user(
    99
)

if found_user is None:
    print(
        "User not found"
    )
else:
    print(
        found_user
    )

# When a function can return either a value or None, the caller can check:

#

# if value is None:

#

# or:

#

# if value is not None:


# =============================================================================
#
# 27. Return a List Created Inside the Function
#
# =============================================================================

def create_even_numbers(
    limit: int,
) -> list[int]:
    """
    Return all even numbers up to the limit.
    """
    numbers: list[int] = []

    for number in range(
        1,
        limit + 1,
    ):
        if number % 2 == 0:
            numbers.append(
                number
            )

    return (
        numbers
    )


even_numbers: list[int] = create_even_numbers(
    10
)

print(
    even_numbers
)

# A function can create an object and return that object to the caller.


# =============================================================================
#
# 28. Returned Mutable Objects Can Be Modified
#
# =============================================================================

def create_items() -> list[str]:
    """
    Return a list of items.
    """
    return [
        "Python",
        "SQL",
    ]


items: list[str] = create_items()

items.append(
    "Docker"
)

print(
    items
)

# The returned list is a normal mutable list.

#

# Therefore the caller can modify it after receiving it.


# =============================================================================
#
# 29. Returning the Same Object
#
# =============================================================================

def return_list(
    items: list[str],
) -> list[str]:
    """
    Return the supplied list.
    """
    return (
        items
    )


original_items: list[str] = [
    "Python",
    "SQL",
]

returned_items: list[str] = return_list(
    original_items
)

returned_items.append(
    "Docker"
)

print(
    original_items
)

print(
    returned_items
)

# The function returns the same list object that it received.

#

# Therefore modifying returned_items also affects original_items.

#

# return does not automatically create a copy.


# =============================================================================
#
# 30. Returning a Copy
#
# =============================================================================

def return_list_copy(
    items: list[str],
) -> list[str]:
    """
    Return a shallow copy of the supplied list.
    """
    return (
        items.copy()
    )


original_items_copy: list[str] = [
    "Python",
    "SQL",
]

copied_items: list[str] = return_list_copy(
    original_items_copy
)

copied_items.append(
    "Docker"
)

print(
    original_items_copy
)

print(
    copied_items
)

# If independent list objects are required:

#

# items.copy()

#

# can be returned instead.


# =============================================================================
#
# 31. Return a Dictionary
#
# =============================================================================

def calculate_statistics(
    first: float,
    second: float,
) -> dict[str, float]:
    """
    Return multiple calculated values in a dictionary.
    """
    return {
        "sum": first + second,
        "difference": first - second,
        "average": (
            first + second
        ) / 2,
    }


statistics: dict[str, float] = calculate_statistics(
    20.0,
    10.0,
)

print(
    statistics
)

# A dictionary can make multiple returned values self-describing.

#

# Instead of:

#

# (
#     30,
#     10,
#     15,
# )

#

# the caller receives named values:

#

# {
#     "sum": 30,
#     "difference": 10,
#     "average": 15,
# }


# =============================================================================
#
# 32. Returning a Boolean Condition Directly
#
# =============================================================================

def is_adult(
    age: int,
) -> bool:
    """
    Return whether the age represents an adult.
    """
    return (
        age >= 18
    )


adult: bool = is_adult(
    25
)

print(
    adult
)

# There is no need to write:

#

# if age >= 18:
#     return True
# else:
#     return False

#

# The condition itself already produces a boolean.


# =============================================================================
#
# 33. Returning a Conditional Expression
#
# =============================================================================

def get_status_text(
    is_active: bool,
) -> str:
    """
    Return status text using a conditional expression.
    """
    return (
        "Active"
        if is_active
        else
        "Inactive"
    )


active_status: str = get_status_text(
    True
)

inactive_status: str = get_status_text(
    False
)

print(
    active_status
)

print(
    inactive_status
)

# A conditional expression can also be returned directly.


# =============================================================================
#
# 34. Return and print() Are Different
#
# =============================================================================

def calculate_value() -> int:
    """
    Return a calculated value.
    """
    return (
        100
    )


returned_value: int = calculate_value()

print(
    returned_value
)

# return:

#

# sends a value back to the caller.

#

# print():

#

# displays a value on the output.

#

# They solve different problems.

#

# A returned value can be:

#

# stored

# reused

# passed to another function

# compared

# transformed

#

# A printed value is primarily output for display.


# =============================================================================
#
# 35. Function With print() But No return
#
# =============================================================================

def print_square(
    number: int,
) -> None:
    """
    Print the square instead of returning it.
    """
    print(
        number
        ** 2
    )

# since the var does not get anything in return it always return None.

# printed_result: None = print_square(
#     5
# )

# so printing None will give None.

# print(
#     printed_result
# )

# so

print_square(5)

# The function displays:

#

# 25

#

# but returns:

#

# None

#

# Therefore:

#

# print(square)

#

# is not the same as:

#

# return square


# =============================================================================
#
# 36. Return Allows Reuse
#
# =============================================================================

def calculate_square_for_reuse(
    number: int,
) -> int:
    """
    Return a square for reuse.
    """
    return (
        number
        ** 2
    )


square_value: int = calculate_square_for_reuse(
    5
)

doubled_square: int = (
    square_value
    * 2
)

formatted_square: str = (
    f"Square->{square_value}"
)

print(
    doubled_square
)

print(
    formatted_square
)

# Because the function returns a value, that value can be reused in
# additional operations.


# =============================================================================
#
# 37. Return From Nested Conditional Logic
#
# =============================================================================

def validate_age(
    age: int,
) -> str:
    """
    Return a validation result.
    """
    if age < 0:
        return (
            "Invalid age"
        )

    if age > 120:
        return (
            "Unrealistic age"
        )

    return (
        "Valid age"
    )


valid_age: str = validate_age(
    30
)

invalid_age: str = validate_age(
    -5
)

unrealistic_age: str = validate_age(
    150
)

print(
    valid_age
)

print(
    invalid_age
)

print(
    unrealistic_age
)

# Multiple early returns can make validation logic straightforward.

#

# Each invalid condition exits immediately.


# =============================================================================
#
# 38. Return From a for Loop
#
# =============================================================================

def find_name(
    names: list[str],
    target: str,
) -> str | None:
    """
    Return the first matching name.
    """
    for name in names:
        if name == target:
            return (
                name
            )

    return None


names: list[str] = [
    "Alex",
    "Sam",
    "Jordan",
]

found_name: str | None = find_name(
    names,
    "Sam",
)

print(
    found_name
)

# return can be used to stop searching as soon as the desired result
# is found.


# =============================================================================
#
# 39. Return Inside Nested Loops
#
# =============================================================================

def find_pair(
    numbers: list[int],
    target: int,
) -> tuple[int, int] | None:
    """
    Return the first pair whose sum matches the target.
    """
    for first in numbers:
        for second in numbers:
            if first + second == target:
                return (
                    first,
                    second,
                )

    return None


pair: tuple[int, int] | None = find_pair(
    [1, 2, 3, 4],
    5,
)

print(
    pair
)

# return exits the entire function.

#

# Therefore when the pair is found:

#

# both loops

# ↓

# stop

#

# and the function returns the pair.


# =============================================================================
#
# 40. Return Does Not Exit the Program
#
# =============================================================================

def get_value() -> int:
    """
    Return a value from the current function.
    """
    return (
        10
    )


value: int = get_value()

print(
    "Function finished"
)

print(
    value
)

# return exits the current function.

#

# It does NOT automatically terminate the entire Python program.


# =============================================================================
#
# 41. Return From a Nested Function
#
# =============================================================================

def outer_function() -> str:
    """
    Demonstrate return from a nested function.
    """
    def inner_function() -> str:
        return (
            "Inner result"
        )

    inner_result: str = inner_function()

    return (
        f"Outer received: {inner_result}"
    )


nested_result: str = outer_function()

print(
    nested_result
)

# return inside inner_function():

#

# exits inner_function().

#

# It does not directly return from outer_function().

#

# The inner function returns its value to the code that called it.


# =============================================================================
#
# 42. Returning Another Function
#
# =============================================================================

def create_greeting_function():
    """
    Return a function.
    """
    def greet(
        name: str,
    ) -> str:
        return (
            f"Hello, {name}!"
        )

    return (
        greet
    )


greeting_function = create_greeting_function()

greeting_result: str = greeting_function(
    "Alex"
)

print(
    greeting_result
)

# Functions are objects in Python.

#

# Therefore a function can return another function.


# =============================================================================
#
# 43. Returning a Lambda Function
#
# =============================================================================

from collections.abc import Callable


def create_multiplier(
    multiplier: float,
) -> Callable[[float], float]:
    """
    Return a function that multiplies a number
    by the supplied multiplier.
    """
    return (
        lambda number:
        number * multiplier
    )

# internally: double = lambda number: number * 2

double: Callable[[float], float] = create_multiplier(
    2
)

triple: Callable[[float], float] = create_multiplier(
    3
)

print(
    double(10)
)

print(
    triple(10)
)

# A function can return a callable object.

#

# This is an example of higher-order function behaviour.


# =============================================================================
#
# 44. Return Type Annotation
#
# =============================================================================

def add_numbers(
    first: int,
    second: int,
) -> int:
    """
    Return the sum of two integers.
    """
    return (
        first
        + second
    )


sum_result: int = add_numbers(
    10,
    20,
)

print(
    sum_result
)

# The annotation:

#

# -> int

#

# documents the expected return type.

#

# It does not itself perform runtime type enforcement.


# =============================================================================
#
# 45. Return Annotation With None
#
# =============================================================================

def log_message(
    message: str,
) -> None:
    """
    Log a message without returning a meaningful value.
    """
    print(
        message
    )


log_message(
    "Application started"
)

# -> None

#

# communicates that the function is intended not to return a meaningful
# value.


# =============================================================================
#
# 46. Return Annotation With Union
#
# =============================================================================

def find_score(
    user_id: int,
) -> int | None:
    """
    Return a score or None if no score exists.
    """
    scores: dict[int, int] = {
        1: 95,
        2: 88,
    }

    return (
        scores.get(
            user_id
        )
    )


existing_score: int | None = find_score(
    1
)

missing_score: int | None = find_score(
    99
)

print(
    existing_score
)

print(
    missing_score
)

# The annotation:

#

# int | None

#

# communicates that the function can return either:

#

# int

#

# or:

#

# None


# =============================================================================
#
# 47. Return Annotation With a Collection
#
# =============================================================================

def get_names() -> list[str]:
    """
    Return a list of names.
    """
    return [
        "Alex",
        "Sam",
        "Jordan",
    ]


names_result: list[str] = get_names()

print(
    names_result
)

# Return annotations can describe collection types.


# =============================================================================
#
# 48. Return a Tuple With Named Meaning
#
# =============================================================================

def get_dimensions() -> tuple[int, int]:
    """
    Return width and height.
    """
    width: int = 1920
    height: int = 1080

    return (
        width,
        height,
    )


width, height = get_dimensions()

print(
    width
)

print(
    height
)

# Returning a tuple is useful when several related values must be returned
# together.


# =============================================================================
#
# 49. Return a Dictionary for Named Results
#
# =============================================================================

def get_dimensions_as_dictionary() -> dict[str, int]:
    """
    Return dimensions using named dictionary keys.
    """
    return {
        "width": 1920,
        "height": 1080,
    }


dimensions: dict[str, int] = (
    get_dimensions_as_dictionary()
)

print(
    dimensions
)

# A dictionary can be useful when the returned values need explicit names.


# =============================================================================
#
# 50. Return in try
#
# =============================================================================

def divide_numbers(
    numerator: float,
    denominator: float,
) -> float | None:
    """
    Return the division result or None when division is invalid.
    """
    try:
        return (
            numerator
            / denominator
        )
    except ZeroDivisionError:
        return None


valid_division: float | None = divide_numbers(
    10.0,
    2.0,
)

invalid_division: float | None = divide_numbers(
    10.0,
    0.0,
)

print(
    valid_division
)

print(
    invalid_division
)

# return can be used inside a try block.

#

# If the return executes successfully, the function prepares to leave.


# =============================================================================
#
# 51. Return in except
#
# =============================================================================

def safe_integer(
    value: str,
) -> int | None:
    """
    Return an integer or None when conversion fails.
    """
    try:
        return (
            int(value)
        )
    except ValueError:
        return None


valid_integer: int | None = safe_integer(
    "100"
)

invalid_integer: int | None = safe_integer(
    "Python"
)

print(
    valid_integer
)

print(
    invalid_integer
)

# return can also be used inside an except block.


# =============================================================================
#
# 52. Return and finally
#
# =============================================================================

def return_with_finally() -> str:
    """
    Demonstrate return together with finally.
    """
    try:
        return (
            "try result"
        )
    finally:
        print(
            "finally executes"
        )


finally_result: str = return_with_finally()

print(
    finally_result
)

# A finally block executes even when the try block contains a return.

#

# The return is prepared, but finally still executes before the function
# actually completes.


# =============================================================================
#
# 53. Avoid Returning From finally
#
# =============================================================================

def dangerous_finally_return() -> str:
    """
    Demonstrate why returning from finally can be dangerous.
    """
    try:
        return (
            "try result"
        )
    finally:
        return (
            "finally result"
        )


dangerous_result: str = dangerous_finally_return()

print(
    dangerous_result
)

# A return inside finally can override an earlier return.

#

# Therefore returning from finally should generally be avoided unless
# that behaviour is explicitly intended.


# =============================================================================
#
# 54. Return in Recursive Functions
#
# =============================================================================

def factorial(
    number: int,
) -> int:
    """
    Return the factorial of a number recursively.
    """
    if number <= 1:
        return (
            1
        )

    return (
        number
        * factorial(
            number - 1
        )
    )


factorial_result: int = factorial(
    5
)

print(
    factorial_result
)

# Recursive functions depend on return values.

#

# The recursive call returns a value to the previous call.

#

# For:

#

# factorial(5)

#

# the calls eventually reach:

#

# factorial(1)

#

# which returns:

#

# 1

#

# The previous calls then use those returned values.


# =============================================================================
#
# 55. Return From a Recursive Search
#
# =============================================================================

def recursive_sum(
    numbers: list[int],
    index: int = 0,
) -> int:
    """
    Return the sum of a list recursively.
    """
    if index == len(numbers):
        return (
            0
        )

    return (
        numbers[index]
        +
        recursive_sum(
            numbers,
            index + 1,
        )
    )


recursive_total: int = recursive_sum(
    [10, 20, 30]
)

print(
    recursive_total
)

# return allows each recursive call to send its result back to the caller.


# =============================================================================
#
# 56. Return Can Be Used for Guard Clauses
#
# =============================================================================

def process_user(
    user_name: str | None,
) -> str:
    """
    Process a user only when a valid name exists.
    """
    if user_name is None:
        return (
            "No user provided"
        )

    if user_name == "":
        return (
            "Empty user name"
        )

    return (
        f"Processing {user_name}"
    )


valid_user: str = process_user(
    "Alex"
)

missing_user_name: str = process_user(
    None
)

empty_user_name: str = process_user(
    ""
)

print(
    valid_user
)

print(
    missing_user_name
)

print(
    empty_user_name
)

# Guard clauses use early return to handle invalid or special cases first.

#

# This often keeps the main logic less deeply nested.


# =============================================================================
#
# 57. Return Should Represent the Function's Result
#
# =============================================================================

def calculate_area(
    width: float,
    height: float,
) -> float:
    """
    Return the area of a rectangle.
    """
    return (
        width
        * height
    )


area: float = calculate_area(
    10.0,
    5.0,
)

print(
    area
)

# A useful function generally returns the result that its caller needs.

#

# The caller can then decide what to do with that result.


# =============================================================================
#
# 58. Returning a Computed Result Instead of Printing It
#
# =============================================================================

def calculate_total_price(
    price: float,
    quantity: int,
) -> float:
    """
    Return the total price.
    """
    return (
        price
        * quantity
    )


total_price: float = calculate_total_price(
    1500.0,
    3,
)

print(
    f"Total: {total_price}"
)

# Returning the value gives the caller control over presentation.

#

# The function calculates.

#

# The caller decides how to display or use the result.


# =============================================================================
#
# 59. Return Value Can Be Compared
#
# =============================================================================

def is_valid_password(
    password: str,
) -> bool:
    """
    Return whether a password meets a simple requirement.
    """
    return (
        len(password) >= 8
    )


if is_valid_password(
    "python123"
):
    print(
        "Password is valid"
    )
else:
    print(
        "Password is invalid"
    )

# A returned value can be used directly in a condition.


# =============================================================================
#
# 60. Return Value Can Be Used in an Expression
#
# =============================================================================

def get_price() -> float:
    """
    Return a price.
    """
    return (
        100.0
    )


final_price: float = (
    get_price()
    * 1.18
)

print(
    final_price
)

# Function calls that return values can participate in larger expressions.


# =============================================================================
#
# 61. Return Value Can Be Passed to a Method
#
# =============================================================================

def get_message_text() -> str:
    """
    Return message text.
    """
    return (
        "python programming"
    )


uppercase_message: str = (
    get_message_text().upper()
)

print(
    uppercase_message
)

# A returned string can immediately be used with string methods.


# =============================================================================
#
# 62. Return Value Can Be Used as a Dictionary Value
#
# =============================================================================

def get_application_version() -> str:
    """
    Return an application version.
    """
    return (
        "1.0.0"
    )


application_info: dict[str, str] = {
    "name": "DataPipeline",
    "version": get_application_version(),
}

print(
    application_info
)

# A function call can be used anywhere an expression is accepted.


# =============================================================================
#
# 63. Return Value Can Be Used in a List
#
# =============================================================================

def get_score() -> int:
    """
    Return a score.
    """
    return (
        95
    )


scores: list[int] = [
    get_score(),
    88,
    76,
]

print(
    scores
)

# Returned values can be inserted directly into collections.


# =============================================================================
#
# 64. Return a New Object Each Time
#
# =============================================================================

def create_empty_list() -> list[str]:
    """
    Return a newly created empty list.
    """
    return []


first_list: list[str] = create_empty_list()

second_list: list[str] = create_empty_list()

first_list.append(
    "Python"
)

print(
    first_list
)

print(
    second_list
)

# Each function call creates a new list.

#

# Therefore the returned lists are independent objects.


# =============================================================================
#
# 65. Return and Object Identity
#
# =============================================================================

def create_object() -> list[str]:
    """
    Return a new list object.
    """
    return []


object_a: list[str] = create_object()

object_b: list[str] = create_object()

print(
    object_a is object_b
)

# Each call creates a separate list object.

#

# Therefore:

#

# object_a is object_b

#

# is False.


# =============================================================================
#
# 66. Returning an Existing Global Object
#
# =============================================================================

shared_configuration: dict[str, object] = {
    "debug": True,
}


def get_shared_configuration() -> dict[str, object]:
    """
    Return the shared configuration object.
    """
    return (
        shared_configuration
    )


configuration_reference: dict[str, object] = (
    get_shared_configuration()
)

configuration_reference["timeout"] = 30

print(
    shared_configuration
)

# Returning an existing object returns a reference to that object.

#

# The function does not automatically copy it.


# =============================================================================
#
# 67. Return and Variable Scope
#
# =============================================================================

def create_local_value() -> int:
    """
    Return a local variable.
    """
    local_value: int = 100

    return (
        local_value
    )


returned_local_value: int = create_local_value()

print(
    returned_local_value
)

# A local variable normally exists only inside the function.

#

# But its value can be returned to the caller.

#

# The caller receives the returned object/value, not direct access to the
# function's local variable.


# =============================================================================
#
# 68. Return Does Not Return Local Variable Scope
#
# =============================================================================

def create_local_name() -> str:
    """
    Return a local string.
    """
    local_name: str = "Alex"

    return (
        local_name
    )


name_from_function: str = create_local_name()

print(
    name_from_function
)

# The returned value is available to the caller.

#

# The local variable itself is not transferred into the caller's scope.


# =============================================================================
#
# 69. Return From a Function With No Arguments
#
# =============================================================================

def get_application_name() -> str:
    """
    Return the application name.
    """
    return (
        "DataPipeline"
    )


application_name: str = get_application_name()

print(
    application_name
)

# A function does not need parameters in order to return a value.


# =============================================================================
#
# 70. Return From a Function With Default Arguments
#
# =============================================================================

def calculate_power(
    base: int,
    exponent: int = 2,
) -> int:
    """
    Return a calculated power.
    """
    return (
        base
        ** exponent
    )


default_power: int = calculate_power(
    5
)

custom_power: int = calculate_power(
    5,
    3,
)

print(
    default_power
)

print(
    custom_power
)

# Return behaviour is independent of whether the function parameters have
# default values.


# =============================================================================
#
# 71. Return and *args
#
# =============================================================================

def sum_values(
    *numbers: int,
) -> int:
    """
    Return the sum of variable-length positional arguments.
    """
    total: int = 0

    for number in numbers:
        total += number

    return (
        total
    )


sum_result_71: int = sum_values(
    10,
    20,
    30,
)

print(
    sum_result
)

# A function using *args can return a normal result.

#

# *args controls how values enter the function.

#

# return controls what leaves the function.


# =============================================================================
#
# 72. Return and **kwargs
#
# =============================================================================

def count_options(
    **options: object,
) -> int:
    """
    Return the number of supplied options.
    """
    return (
        len(options)
    )


option_count: int = count_options(
    debug=True,
    timeout=30,
    environment="production",
)

print(
    option_count
)

# **kwargs controls how keyword arguments enter the function.

#

# return controls the value sent back to the caller.


# =============================================================================
#
# 73. Returning an Empty Collection
#
# =============================================================================

def find_matching_items(
    items: list[str],
    target: str,
) -> list[str]:
    """
    Return matching items.
    """
    return [
        item
        for item in items
        if item == target
    ]


matches: list[str] = find_matching_items(
    ["Python", "SQL", "Python"],
    "Java",
)

print(
    matches
)

# A function can return an empty collection when there are no matches.

#

# This is different from returning None.

#

# [] means:

# a valid list containing zero items.

#

# None means:

# no value / absence of a result.


# =============================================================================
#
# 74. Empty List vs None
#
# =============================================================================

def find_items(
    target: str,
) -> list[str] | None:
    """
    Demonstrate the distinction between empty results and None.
    """
    items: dict[str, list[str]] = {
        "python": ["Python"],
        "java": [],
    }

    if target not in items:
        return None

    return (
        items[target]
    )


python_items: list[str] | None = find_items(
    "python"
)

java_items: list[str] | None = find_items(
    "java"
)

unknown_items: list[str] | None = find_items(
    "rust"
)

print(
    python_items
)

print(
    java_items
)

print(
    unknown_items
)

# The results represent different meanings:

#

# ["Python"]

# ↓

# matching items exist

#

# []

# ↓

# the known category has no items

#

# None

# ↓

# the requested category does not exist


# =============================================================================
#
# 75. Consistent Return Types
#
# =============================================================================

def get_discount(
    is_member: bool,
) -> float:
    """
    Return a discount percentage consistently.
    """
    if is_member:
        return (
            20.0
        )

    return (
        0.0
    )


member_discount: float = get_discount(
    True
)

regular_discount: float = get_discount(
    False
)

print(
    member_discount
)

print(
    regular_discount
)

# Both execution paths return float values.

#

# Consistent return types make functions easier to understand and use.


# =============================================================================
#
# 76. Inconsistent Return Types
#
# =============================================================================

def get_optional_discount(
    is_member: bool,
) -> float | None:
    """
    Return a discount or None.
    """
    if is_member:
        return (
            20.0
        )

    return None


member_optional_discount: float | None = (
    get_optional_discount(
        True
    )
)

non_member_optional_discount: float | None = (
    get_optional_discount(
        False
    )
)

print(
    member_optional_discount
)

print(
    non_member_optional_discount
)

# Sometimes different return types are intentional.

#

# In such cases the return annotation should communicate the possible types.


# =============================================================================
#
# 77. Return Inside try Does Not Skip finally
#
# =============================================================================

def get_result() -> str:
    """
    Demonstrate return and finally execution order.
    """
    try:
        return (
            "result"
        )
    finally:
        print(
            "Cleanup executed"
        )


result_from_try: str = get_result()

print(
    result_from_try
)

# Even though return is inside try:

#

# finally

#

# still executes before the function completes.


# =============================================================================
#
# 78. Return Should Usually Be the Final Result of a Branch
#
# =============================================================================

def classify_temperature(
    temperature: float,
) -> str:
    """
    Classify a temperature.
    """
    if temperature < 0:
        return (
            "Freezing"
        )

    if temperature < 20:
        return (
            "Cold"
        )

    if temperature < 30:
        return (
            "Moderate"
        )

    return (
        "Hot"
    )


freezing: str = classify_temperature(
    -5
)

cold: str = classify_temperature(
    10
)

moderate: str = classify_temperature(
    25
)

hot: str = classify_temperature(
    35
)

print(
    freezing
)

print(
    cold
)

print(
    moderate
)

print(
    hot
)

# Each branch has a clear result.

#

# Once a return executes, no later branch is evaluated.


# =============================================================================
#
# 79. Return Statement Core Model
#
# =============================================================================

"""
The return statement has two major responsibilities:

1. Stop the current function.

2. Send a value back to the caller.

Example:

def add(
    first: int,
    second: int,
) -> int:
    return first + second

Call:

result = add(
    10,
    20,
)

Flow:

caller
  ↓
add(10, 20)
  ↓
first + second
  ↓
30
  ↓
return
  ↓
caller receives 30

Therefore:

RETURN
   ↓
stop current function
   +
send value to caller
"""


# =============================================================================
#
# 80. Return Statement Summary
#
# =============================================================================

"""
The return statement:
"""