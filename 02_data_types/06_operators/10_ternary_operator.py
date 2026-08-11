# type: ignore
# =============================================================================
# 10. Ternary Operator
# =============================================================================
"""
Python Operators

File:
    10_ternary_operator.py

Topic:
    Ternary Operator

Overview:
    The ternary operator is a compact way to choose between two expressions
    based on a condition.

Syntax:

    value_if_true if condition else value_if_false

Example:

    age = 20
    status = "adult" if age >= 18 else "minor"

The condition is evaluated first.

If the condition is True:
    the expression before else is returned.

If the condition is False:
    the expression after else is returned.

Topics covered:

    - Basic ternary expressions
    - Boolean conditions
    - Numeric conditions
    - String conditions
    - Comparison operators
    - Equality checks
    - Membership checks
    - None checks
    - Truthy and falsy values
    - Function return values
    - Function calls
    - Assigning ternary results
    - Printing ternary results
    - Ternary expressions with calculations
    - Ternary expressions with strings
    - Ternary expressions with lists
    - Ternary expressions with dictionaries
    - Nested ternary expressions
    - Ternary expressions inside f-strings
    - Ternary expressions in function arguments
    - Ternary expressions in return statements
    - Ternary expressions with boolean operators
    - Ternary expressions with membership operators
    - Ternary expressions with identity operators
    - Ternary expressions with comparisons
    - Practical examples
    - Readability considerations
"""

# =============================================================================
# 01. Basic Ternary Operator
# =============================================================================

age: int = 20

status: str = "adult" if age >= 18 else "minor"

print(status)


# =============================================================================
# 02. Basic Boolean Ternary
# =============================================================================

is_logged_in: bool = True

message: str = "Welcome" if is_logged_in else "Please log in"

print(message)


# =============================================================================
# 03. Ternary With a False Condition
# =============================================================================

is_available: bool = False

availability: str = "Available" if is_available else "Unavailable"

print(availability)


# =============================================================================
# 04. Ternary With Equality
# =============================================================================

role: str = "admin"

access_level: str = "Full access" if role == "admin" else "Limited access"

print(access_level)


# =============================================================================
# 05. Ternary With Inequality
# =============================================================================

status_code: int = 404

response_type: str = "Success" if status_code != 404 else "Not found"

print(response_type)


# =============================================================================
# 06. Ternary With Greater Than
# =============================================================================

score: int = 85

result: str = "High score" if score > 80 else "Normal score"

print(result)


# =============================================================================
# 07. Ternary With Less Than
# =============================================================================

temperature: float = 15.0

weather: str = "Cold" if temperature < 20 else "Warm"

print(weather)


# =============================================================================
# 08. Ternary With Greater Than or Equal To
# =============================================================================

marks: int = 75

grade_status: str = "Passed" if marks >= 40 else "Failed"

print(grade_status)


# =============================================================================
# 09. Ternary With Less Than or Equal To
# =============================================================================

age_limit: int = 18

eligibility: str = "Eligible" if age_limit <= 18 else "Not eligible"

print(eligibility)


# =============================================================================
# 10. Ternary With Even and Odd Numbers
# =============================================================================

number: int = 12

parity: str = "Even" if number % 2 == 0 else "Odd"

print(parity)


# =============================================================================
# 11. Ternary With Positive and Negative Numbers
# =============================================================================

number: int = -10

sign: str = "Positive" if number >= 0 else "Negative"

print(sign)


# =============================================================================
# 12. Ternary With Zero
# =============================================================================

number: int = 0

zero_status: str = "Zero" if number == 0 else "Non-zero"

print(zero_status)


# =============================================================================
# 13. Ternary With an Empty String
# =============================================================================

username: str = ""

display_name: str = username if username else "Guest"

print(display_name)


# =============================================================================
# 14. Ternary With a Non-empty String
# =============================================================================

username: str = "Shreyas"

display_name: str = username if username else "Guest"

print(display_name)


# =============================================================================
# 15. Ternary With a List
# =============================================================================

numbers: list[int] = [10, 20, 30]

message: str = "List has values" if numbers else "List is empty"

print(message)


# =============================================================================
# 16. Ternary With an Empty List
# =============================================================================

numbers: list[int] = []

message: str = "List has values" if numbers else "List is empty"

print(message)


# =============================================================================
# 17. Ternary With a Dictionary
# =============================================================================

user: dict[str, str] = {
    "name": "Alex",
}

user_status: str = "User exists" if user else "User is empty"

print(user_status)


# =============================================================================
# 18. Ternary With an Empty Dictionary
# =============================================================================

user: dict[str, str] = {}

user_status: str = "User exists" if user else "User is empty"

print(user_status)


# =============================================================================
# 19. Ternary With None
# =============================================================================

value: str | None = None

result: str = value if value is not None else "Default value"

print(result)


# =============================================================================
# 20. Ternary With a Non-None Value
# =============================================================================

value: str | None = "Python"

result: str = value if value is not None else "Default value"

print(result)


# =============================================================================
# 21. Ternary With Function Return Value
# =============================================================================

def get_score() -> int:
    """Return a sample score."""
    return 90


score: int = get_score()

result: str = "Passed" if score >= 40 else "Failed"

print(result)


# =============================================================================
# 22. Ternary Inside a Function Return
# =============================================================================

def get_status(score: int) -> str:
    """Return pass or fail based on the score."""
    return "Passed" if score >= 40 else "Failed"


print(get_status(75))
print(get_status(25))


# =============================================================================
# 23. Ternary With a Function Call
# =============================================================================

def is_even(number: int) -> bool:
    """Return whether a number is even."""
    return number % 2 == 0


number: int = 8

message: str = "Even" if is_even(number) else "Odd"

print(message)


# =============================================================================
# 24. Ternary Inside a Function Argument
# =============================================================================

age: int = 25

print("Adult" if age >= 18 else "Minor")


# =============================================================================
# 25. Ternary Inside an f-string
# =============================================================================

score: int = 85

print(f"Result: {'Passed' if score >= 40 else 'Failed'}")


# =============================================================================
# 26. Ternary With Arithmetic
# =============================================================================

first_number: int = 10
second_number: int = 20

larger_number: int = (
    first_number
    if first_number > second_number
    else second_number
)

print(larger_number)


# =============================================================================
# 27. Find the Smaller Number
# =============================================================================

first_number: int = 10
second_number: int = 20

smaller_number: int = (
    first_number
    if first_number < second_number
    else second_number
)

print(smaller_number)


# =============================================================================
# 28. Calculate Absolute Value
# =============================================================================

number: int = -25

absolute_value: int = number if number >= 0 else -number

print(absolute_value)


# =============================================================================
# 29. Select a Default Port
# =============================================================================

configured_port: int | None = None

port: int = configured_port if configured_port is not None else 8000

print(port)


# =============================================================================
# 30. Select a Default Username
# =============================================================================

username: str = ""

user_label: str = username if username else "Anonymous"

print(user_label)


# =============================================================================
# 31. Ternary With and
# =============================================================================

age: int = 25
has_license: bool = True

can_drive: str = (
    "Can drive"
    if age >= 18 and has_license
    else "Cannot drive"
)

print(can_drive)


# =============================================================================
# 32. Ternary With or
# =============================================================================

has_username: bool = False
has_email: bool = True

identifier: str = (
    "User identified"
    if has_username or has_email
    else "Unknown user"
)

print(identifier)


# =============================================================================
# 33. Ternary With not
# =============================================================================

is_blocked: bool = False

account_status: str = (
    "Active"
    if not is_blocked
    else "Blocked"
)

print(account_status)


# =============================================================================
# 34. Ternary With Membership
# =============================================================================

role: str = "admin"
allowed_roles: list[str] = ["admin", "manager"]

permission: str = (
    "Allowed"
    if role in allowed_roles
    else "Denied"
)

print(permission)


# =============================================================================
# 35. Ternary With Not in
# =============================================================================

username: str = "alex"
blocked_users: list[str] = ["john", "mike"]

status: str = (
    "Allowed"
    if username not in blocked_users
    else "Blocked"
)

print(status)


# =============================================================================
# 36. Ternary With Identity
# =============================================================================

value: str | None = None

result: str = (
    "No value"
    if value is None
    else "Value exists"
)

print(result)


# =============================================================================
# 37. Ternary With Boolean Values
# =============================================================================

is_admin: bool = True

access_granted: bool = True if is_admin else False

print(access_granted)


# =============================================================================
# 38. Boolean Ternary Simplification
# =============================================================================

is_admin: bool = True

access_granted: bool = is_admin

print(access_granted)

# When both branches are simply True and False, the ternary expression
# is often unnecessary.


# =============================================================================
# 39. Ternary With String Selection
# =============================================================================

language: str = "python"

language_name: str = (
    "Python"
    if language == "python"
    else "Other"
)

print(language_name)


# =============================================================================
# 40. Ternary With Multiple Conditions
# =============================================================================

age: int = 25
is_employed: bool = True

category: str = (
    "Working adult"
    if age >= 18 and is_employed
    else "Other"
)

print(category)


# =============================================================================
# 41. Nested Ternary Operator
# =============================================================================

score: int = 85

grade: str = (
    "A"
    if score >= 90
    else "B"
    if score >= 80
    else "C"
)

print(grade)


# =============================================================================
# 42. Nested Ternary With Three Categories
# =============================================================================

temperature: float = 30.0

weather_status: str = (
    "Cold"
    if temperature < 15
    else "Warm"
    if temperature < 30
    else "Hot"
)

print(weather_status)


# =============================================================================
# 43. Nested Ternary With Four Categories
# =============================================================================

score: int = 92

grade: str = (
    "A"
    if score >= 90
    else "B"
    if score >= 80
    else "C"
    if score >= 70
    else "D"
)

print(grade)


# =============================================================================
# 44. Ternary For Absolute Difference
# =============================================================================

first_number: int = 25
second_number: int = 40

difference: int = (
    first_number - second_number
    if first_number >= second_number
    else second_number - first_number
)

print(difference)


# =============================================================================
# 45. Ternary For Minimum Value
# =============================================================================

first_number: int = 15
second_number: int = 10

minimum: int = (
    first_number
    if first_number < second_number
    else second_number
)

print(minimum)


# =============================================================================
# 46. Ternary For Maximum Value
# =============================================================================

first_number: int = 15
second_number: int = 10

maximum: int = (
    first_number
    if first_number > second_number
    else second_number
)

print(maximum)


# =============================================================================
# 47. Ternary With Tuple Selection
# =============================================================================

is_development: bool = True

configuration: tuple[str, int] = (
    ("development", 8000)
    if is_development
    else ("production", 80)
)

print(configuration)


# =============================================================================
# 48. Ternary With List Selection
# =============================================================================

use_extended_list: bool = True

values: list[int] = (
    [1, 2, 3, 4, 5]
    if use_extended_list
    else [1, 2, 3]
)

print(values)


# =============================================================================
# 49. Ternary With Dictionary Selection
# =============================================================================

is_production: bool = True

configuration: dict[str, int] = (
    {"workers": 4, "port": 80}
    if is_production
    else {"workers": 1, "port": 8000}
)

print(configuration)


# =============================================================================
# 50. Ternary With Type Selection
# =============================================================================

use_float: bool = True

number: int | float = 10.5 if use_float else 10

print(number)


# =============================================================================
# 51. Ternary With String Formatting
# =============================================================================

name: str = "Alex"
age: int = 30

profile: str = (
    f"{name} is an adult"
    if age >= 18
    else f"{name} is a minor"
)

print(profile)


# =============================================================================
# 52. Ternary With Collection Length
# =============================================================================

items: list[str] = ["Python", "SQL", "Go"]

collection_status: str = (
    "Has items"
    if len(items) > 0
    else "Empty"
)

print(collection_status)


# =============================================================================
# 53. Ternary With Multiple Comparisons
# =============================================================================

score: int = 75

score_range: str = (
    "Excellent"
    if score >= 90
    else "Good"
    if score >= 70
    else "Needs improvement"
)

print(score_range)


# =============================================================================
# 54. Ternary With a Function Parameter
# =============================================================================

def format_name(name: str) -> str:
    """Return a formatted name using a ternary expression."""
    return name.strip() if name.strip() else "Unknown"


print(format_name("Alex"))
print(format_name("   "))


# =============================================================================
# 55. Ternary With String Length
# =============================================================================

password: str = "python123"

password_status: str = (
    "Strong enough"
    if len(password) >= 8
    else "Too short"
)

print(password_status)


# =============================================================================
# 56. Ternary With Numeric Calculation
# =============================================================================

price: float = 100.0
discount_available: bool = True

final_price: float = (
    price * 0.90
    if discount_available
    else price
)

print(final_price)


# =============================================================================
# 57. Ternary With a Boolean Function
# =============================================================================

def is_positive(number: int) -> bool:
    """Return True when number is positive."""
    return number > 0


number: int = 10

description: str = (
    "Positive"
    if is_positive(number)
    else "Not positive"
)

print(description)


# =============================================================================
# 58. Ternary With None and a Function
# =============================================================================

def get_username() -> str | None:
    """Return a username or None."""
    return None


username: str | None = get_username()

display_name: str = (
    username
    if username is not None
    else "Guest"
)

print(display_name)


# =============================================================================
# 59. Ternary With a Dictionary Lookup
# =============================================================================

users: dict[int, str] = {
    1: "Alex",
    2: "Sam",
}

user_id: int = 1

user_name: str = (
    users[user_id]
    if user_id in users
    else "Unknown"
)

print(user_name)


# =============================================================================
# 60. Practical User Access Example
# =============================================================================

user_role: str = "admin"
is_active: bool = True

access_message: str = (
    "Access granted"
    if user_role == "admin" and is_active
    else "Access denied"
)

print(access_message)


# =============================================================================
# 61. Ternary Expression Versus Traditional if Statement
# =============================================================================

score: int = 80

result: str

if score >= 40:
    result = "Passed"
else:
    result = "Failed"

print(result)


# Equivalent ternary version:

score: int = 80

result = "Passed" if score >= 40 else "Failed"

print(result)


# =============================================================================
# 62. Ternary With Parentheses
# =============================================================================

age: int = 21

message: str = (
    "Adult"
    if age >= 18
    else "Minor"
)

print(message)


# Parentheses can improve readability when the expression spans multiple
# lines.


# =============================================================================
# 63. Ternary Inside a Calculation
# =============================================================================

number: int = 10
multiplier: int = 2 if number > 5 else 1

result: int = number * multiplier

print(result)


# =============================================================================
# 64. Ternary For Selecting a Function Result
# =============================================================================

def development_port() -> int:
    """Return the development port."""
    return 8000


def production_port() -> int:
    """Return the production port."""
    return 80


is_production: bool = False

port: int = (
    production_port()
    if is_production
    else development_port()
)

print(port)


# =============================================================================
# 65. Ternary With Boolean Expression
# =============================================================================

age: int = 25
has_permission: bool = True

can_access: bool = (
    age >= 18 and has_permission
)

print(can_access)


# A ternary is unnecessary when the desired result is exactly the Boolean
# condition itself.


# =============================================================================
# 66. Ternary Returning Different Types
# =============================================================================

use_number: bool = True

value: int | str = 100 if use_number else "one hundred"

print(value)


# Although Python allows different result types, keeping both branches
# conceptually compatible usually makes code easier to understand.


# =============================================================================
# 67. Ternary With Object Selection
# =============================================================================

primary_items: list[str] = ["Python", "Go"]
backup_items: list[str] = ["Java", "C++"]

use_primary: bool = True

selected_items: list[str] = (
    primary_items
    if use_primary
    else backup_items
)

print(selected_items)


# =============================================================================
# 68. Ternary With Environment Selection
# =============================================================================

environment: str = "development"

debug_enabled: bool = (
    True
    if environment == "development"
    else False
)

print(debug_enabled)


# =============================================================================
# 69. Ternary With Port Selection
# =============================================================================

environment: str = "production"

port: int = (
    80
    if environment == "production"
    else 8000
)

print(port)


# =============================================================================
# 70. Ternary With Logging Level
# =============================================================================

is_production: bool = True

log_level: str = (
    "WARNING"
    if is_production
    else "DEBUG"
)

print(log_level)


# =============================================================================
# 71. Ternary With Access Control
# =============================================================================

is_admin: bool = False
is_owner: bool = True

access: str = (
    "Allowed"
    if is_admin or is_owner
    else "Denied"
)

print(access)


# =============================================================================
# 72. Ternary With Validation
# =============================================================================

email: str = "user@example.com"

validation_message: str = (
    "Valid"
    if "@" in email
    else "Invalid"
)

print(validation_message)


# =============================================================================
# 73. Ternary With a File Extension
# =============================================================================

filename: str = "report.py"

file_type: str = (
    "Python file"
    if filename.endswith(".py")
    else "Other file"
)

print(file_type)


# =============================================================================
# 74. Ternary With a Dictionary Value
# =============================================================================

user: dict[str, str] = {
    "name": "Alex",
}

name: str = (
    user["name"]
    if "name" in user
    else "Unknown"
)

print(name)


# =============================================================================
# 75. Ternary With List Indexing
# =============================================================================

numbers: list[int] = [10, 20, 30]

index: int = 1

selected_number: int = (
    numbers[index]
    if 0 <= index < len(numbers)
    else -1
)

print(selected_number)


# =============================================================================
# 76. Ternary With Division Safety
# =============================================================================

numerator: float = 100.0
denominator: float = 5.0

result: float = (
    numerator / denominator
    if denominator != 0
    else 0.0
)

print(result)


# =============================================================================
# 77. Ternary With Percentage Calculation
# =============================================================================

total_marks: int = 500
obtained_marks: int = 425

percentage: float = (
    obtained_marks / total_marks * 100
    if total_marks > 0
    else 0.0
)

print(percentage)


# =============================================================================
# 78. Ternary With Temperature Conversion
# =============================================================================

temperature_celsius: float = 25.0

temperature_label: str = (
    "Freezing"
    if temperature_celsius <= 0
    else "Above freezing"
)

print(temperature_label)


# =============================================================================
# 79. Ternary With List Selection Based on Length
# =============================================================================

primary_values: list[int] = [1, 2, 3]
backup_values: list[int] = [100, 200]

selected_values: list[int] = (
    primary_values
    if primary_values
    else backup_values
)

print(selected_values)


# =============================================================================
# 80. Ternary With Configuration Selection
# =============================================================================

is_debug: bool = True

configuration_name: str = (
    "development"
    if is_debug
    else "production"
)

print(configuration_name)


# =============================================================================
# 81. Ternary With Object State
# =============================================================================

class User:
    """Represent a simple user."""

    def __init__(
        self,
        active: bool,
    ) -> None:
        self.active: bool = active


user = User(active=True)

status: str = (
    "Active"
    if user.active
    else "Inactive"
)

print(status)


# =============================================================================
# 82. Ternary With Attribute Existence
# =============================================================================

class Account:
    """Represent a simple account."""

    def __init__(
        self,
        username: str,
    ) -> None:
        self.username: str = username


account = Account("alex")

username: str = (
    account.username
    if hasattr(account, "username")
    else "Unknown"
)

print(username)


# =============================================================================
# 83. Ternary With Type Checking
# =============================================================================

value: object = 100

value_type: str = (
    "Integer"
    if isinstance(value, int)
    else "Other"
)

print(value_type)


# =============================================================================
# 84. Ternary With Multiple Conditions
# =============================================================================

age: int = 30
country: str = "India"

eligibility: str = (
    "Eligible"
    if age >= 18 and country == "India"
    else "Not eligible"
)

print(eligibility)


# =============================================================================
# 85. Ternary With Membership and Comparison
# =============================================================================

role: str = "manager"
minimum_age: int = 21
allowed_roles: list[str] = ["admin", "manager"]

result: str = (
    "Approved"
    if role in allowed_roles and minimum_age >= 18
    else "Rejected"
)

print(result)


# =============================================================================
# 86. Ternary With Nested Function Calls
# =============================================================================

def get_number() -> int:
    """Return a number."""
    return 10


number: int = get_number()

result: str = (
    "Large"
    if abs(number) > 5
    else "Small"
)

print(result)


# =============================================================================
# 87. Ternary With abs()
# =============================================================================

number: int = -15

description: str = (
    "Large absolute value"
    if abs(number) >= 10
    else "Small absolute value"
)

print(description)


# =============================================================================
# 88. Ternary With max()
# =============================================================================

first_number: int = 20
second_number: int = 30

maximum: int = (
    max(first_number, second_number)
    if first_number != second_number
    else first_number
)

print(maximum)


# =============================================================================
# 89. Ternary With min()
# =============================================================================

first_number: int = 20
second_number: int = 30

minimum: int = (
    min(first_number, second_number)
    if first_number != second_number
    else first_number
)

print(minimum)


# =============================================================================
# 90. Practical Grade Function
# =============================================================================

def get_grade(score: int) -> str:
    """Return a grade using nested ternary expressions."""
    return (
        "A"
        if score >= 90
        else "B"
        if score >= 80
        else "C"
        if score >= 70
        else "D"
        if score >= 60
        else "F"
    )


print(get_grade(95))
print(get_grade(82))
print(get_grade(72))
print(get_grade(65))
print(get_grade(40))


# =============================================================================
# 91. Practical Temperature Function
# =============================================================================

def describe_temperature(
    temperature: float,
) -> str:
    """Return a temperature description."""
    return (
        "Cold"
        if temperature < 15
        else "Moderate"
        if temperature < 30
        else "Hot"
    )


print(describe_temperature(10.0))
print(describe_temperature(25.0))
print(describe_temperature(35.0))


# =============================================================================
# 92. Practical Login Function
# =============================================================================

def login_message(
    username: str,
    password_valid: bool,
) -> str:
    """Return a login result."""
    return (
        f"Welcome, {username}"
        if password_valid
        else "Invalid credentials"
    )


print(login_message("Alex", True))
print(login_message("Alex", False))


# =============================================================================
# 93. Practical Discount Function
# =============================================================================

def calculate_price(
    price: float,
    is_member: bool,
) -> float:
    """Apply a member discount when applicable."""
    return price * 0.90 if is_member else price


print(calculate_price(100.0, True))
print(calculate_price(100.0, False))


# =============================================================================
# 94. Practical Shipping Function
# =============================================================================

def shipping_cost(
    order_total: float,
) -> float:
    """Return free shipping for qualifying orders."""
    return 0.0 if order_total >= 500.0 else 50.0


print(shipping_cost(750.0))
print(shipping_cost(250.0))


# =============================================================================
# 95. Practical Even/Odd Function
# =============================================================================

def describe_number(
    number: int,
) -> str:
    """Return whether a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"


print(describe_number(10))
print(describe_number(11))


# =============================================================================
# 96. Practical Positive/Negative/Zero Function
# =============================================================================

def describe_sign(
    number: int,
) -> str:
    """Describe the sign of a number."""
    return (
        "Positive"
        if number > 0
        else "Negative"
        if number < 0
        else "Zero"
    )


print(describe_sign(10))
print(describe_sign(-10))
print(describe_sign(0))


# =============================================================================
# 97. Practical Largest-of-Three Example
# =============================================================================

def largest_of_three(
    first: int,
    second: int,
    third: int,
) -> int:
    """Return the largest of three numbers."""
    largest_first_second: int = (
        first
        if first > second
        else second
    )

    return (
        largest_first_second
        if largest_first_second > third
        else third
    )


print(largest_of_three(10, 20, 15))


# =============================================================================
# 98. Practical Default Value Function
# =============================================================================

def get_display_name(
    name: str | None,
) -> str:
    """Return a name or a default value."""
    return name if name is not None else "Guest"


print(get_display_name("Alex"))
print(get_display_name(None))


# =============================================================================
# 99. Practical Environment Configuration
# =============================================================================

def get_server_port(
    environment: str,
) -> int:
    """Return a server port based on the environment."""
    return (
        80
        if environment == "production"
        else 8000
    )


print(get_server_port("production"))
print(get_server_port("development"))


# =============================================================================
# 100. Practical Permission Function
# =============================================================================

def get_permission(
    role: str,
    is_active: bool,
) -> str:
    """Return whether a user can access the system."""
    return (
        "Access granted"
        if role in {"admin", "manager"} and is_active
        else "Access denied"
    )


print(get_permission("admin", True))
print(get_permission("manager", True))
print(get_permission("user", True))
print(get_permission("admin", False))


# =============================================================================
# 101. Ternary Operator Core Pattern
# =============================================================================

"""
The fundamental syntax is:

    value_if_true if condition else value_if_false

Example:

    status = "adult" if age >= 18 else "minor"

Equivalent traditional if/else:

    if age >= 18:
        status = "adult"
    else:
        status = "minor"

The ternary operator is useful when the selected values are simple and
the condition is easy to understand.
"""


# =============================================================================
# 102. Ternary Operator Evaluation
# =============================================================================

"""
Conceptually:

    result = true_value if condition else false_value

Python evaluates the condition.

If the condition is truthy:

    true_value

is selected.

Otherwise:

    false_value

is selected.

Only the selected branch needs to be evaluated.

For example:

    value = 10

    result = "positive" if value > 0 else "negative"

The result is:

    "positive"
"""


# =============================================================================
# 103. Ternary Operator and Truthiness
# =============================================================================

"""
The condition does not have to explicitly produce True or False.

Python uses truth-value testing.

Examples:

    empty list       -> False
    non-empty list   -> True
    empty string     -> False
    non-empty string -> True
    zero             -> False
    non-zero number  -> True
    None             -> False

Example:

    items = []

    message = "Has data" if items else "No data"
"""


# =============================================================================
# 104. Ternary Operator and Readability
# =============================================================================

"""
Good use:

    status = "Passed" if score >= 40 else "Failed"

This is short and easy to understand.

Avoid excessively complicated nested ternaries when a normal if/elif/else
statement would be clearer.

For example, instead of deeply nesting conditions:

    result = (
        "A"
        if score >= 90
        else "B"
        if score >= 80
        else "C"
        if score >= 70
        else "D"
    )

a normal conditional may sometimes be easier to maintain:

    if score >= 90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    else:
        result = "D"

The ternary operator should improve concise expressions, not make code
harder to understand.
"""


# =============================================================================
# 105. Ternary Operator Best Practices
# =============================================================================

"""
Best practices:

1. Use ternary expressions for simple two-way decisions.

2. Keep the condition easy to understand.

3. Keep both result expressions reasonably short.

4. Use parentheses when a multi-line ternary improves readability.

5. Avoid deeply nested ternary expressions.

6. Prefer normal if/elif/else when there are many branches.

7. Avoid using a ternary when a direct Boolean expression is enough.

8. Keep the two possible results conceptually related.

9. Use descriptive variable names.

10. Remember that the syntax is:

       value_if_true if condition else value_if_false

11. Do not confuse the ternary expression with C-style:

       condition ? true_value : false_value

    Python does not use that syntax.

"""


# =============================================================================
# 106. Ternary Operator Versus if/else
# =============================================================================

score: int = 85

# Ternary version:

result_ternary: str = "Passed" if score >= 40 else "Failed"

print(result_ternary)


# Traditional version:

result_if_else: str

if score >= 40:
    result_if_else = "Passed"
else:
    result_if_else = "Failed"

print(result_if_else)


# Both produce the same logical result.


# =============================================================================
# 107. Ternary Operator With Assignment
# =============================================================================

is_admin: bool = True

role_name: str = "Administrator" if is_admin else "User"

print(role_name)


# The result of the ternary expression is assigned to role_name.


# =============================================================================
# 108. Ternary Operator With Return
# =============================================================================

def get_access(
    is_authenticated: bool,
) -> str:
    """Return access status."""
    return "Authenticated" if is_authenticated else "Unauthenticated"


print(get_access(True))
print(get_access(False))


# =============================================================================
# 109. Ternary Operator With Printing
# =============================================================================

is_ready: bool = True

print("Ready" if is_ready else "Not ready")


# =============================================================================
# 110. Final Practical Example
# =============================================================================

def process_user(
    username: str | None,
    age: int,
    is_active: bool,
) -> str:
    """
    Return a user status using several simple conditions.

    The function demonstrates how ternary expressions can be used for
    straightforward two-way decisions while keeping the data flow explicit.
    """
    display_name: str = (
        username
        if username is not None
        else "Guest"
    )

    account_status: str = (
        "Active"
        if is_active
        else "Inactive"
    )

    age_status: str = (
        "Adult"
        if age >= 18
        else "Minor"
    )

    return (
        f"User: {display_name}; "
        f"Account: {account_status}; "
        f"Age group: {age_status}"
    )


print(
    process_user(
        username="Alex",
        age=25,
        is_active=True,
    )
)

print(
    process_user(
        username=None,
        age=16,
        is_active=False,
    )
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Python's ternary expression provides a concise two-way conditional.

✓ The syntax is:

    value_if_true if condition else value_if_false

✓ The condition is evaluated first.

✓ If the condition is truthy, the first expression is selected.

✓ If the condition is falsy, the expression after else is selected.

✓ Ternary expressions can be assigned to variables.

✓ Ternary expressions can be returned from functions.

✓ Ternary expressions can be passed as function arguments.

✓ Ternary expressions can appear inside f-strings.

✓ Ternary expressions can use comparisons.

✓ Ternary expressions can use boolean operators.

✓ Ternary expressions can use membership operators.

✓ Ternary expressions can use identity checks.

✓ Ternary expressions work with strings, numbers, lists, dictionaries,
  tuples, and other objects.

✓ Python uses truthiness when evaluating the condition.

✓ Nested ternary expressions are possible.

✓ Deeply nested ternaries can reduce readability.

✓ Use normal if/elif/else statements when the logic becomes complicated.

✓ A ternary expression should usually represent a simple two-way decision.

Core syntax:

    result = value_if_true if condition else value_if_false

Traditional equivalent:

    if condition:
        result = value_if_true
    else:
        result = value_if_false

Common patterns:

    status = "Passed" if score >= 40 else "Failed"

    name = username if username else "Guest"

    value = default if value is None else value

    maximum = first if first > second else second

    parity = "Even" if number % 2 == 0 else "Odd"

    access = "Allowed" if is_authenticated else "Denied"

The main idea:

    CONDITION
        ↓
    ┌───────────────┐
    │               │
  True            False
    ↓               ↓
value_if_true   value_if_false
    │               │
    └───────┬───────┘
            ↓
          RESULT
"""


# =============================================================================
# End of 10_ternary_operator.py
# =============================================================================