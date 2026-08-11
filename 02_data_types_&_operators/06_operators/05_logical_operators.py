# =============================================================================
# 05. Logical Operators
# =============================================================================
# type: ignore

"""
Python Operators

File:
    05_logical_operators.py

Topic:
    Logical Operators

Overview:
    Logical operators are used to combine, reverse, and evaluate conditions.

    Python provides three logical operators:

        and
        or
        not

    Logical operators are commonly used with Boolean expressions.

    Basic behaviour:

        and
            True only when both operands are truthy.

        or
            True when at least one operand is truthy.

        not
            Reverses the truth value of an expression.

    Python's logical operators also use short-circuit evaluation.

    With:

        and

    Python stops evaluating when it encounters a falsy operand.

    With:

        or

    Python stops evaluating when it encounters a truthy operand.

    Important:
        and and or do not necessarily return True or False.

        They return one of their operands.

    This file contains 50 distinct examples covering practical and important
    logical-operator patterns.
"""

# =============================================================================
# 01. Basic and
# =============================================================================

first_condition: bool = True
second_condition: bool = True

result: bool = first_condition and second_condition

print(result)


# =============================================================================
# 02. and With One False Condition
# =============================================================================

first_condition = True
second_condition = False

result = first_condition and second_condition

print(result)


# =============================================================================
# 03. and With Both False
# =============================================================================

first_condition = False
second_condition = False

result = first_condition and second_condition

print(result)


# =============================================================================
# 04. Basic or
# =============================================================================

first_condition = True
second_condition = False

result = first_condition or second_condition

print(result)


# =============================================================================
# 05. or With Both False
# =============================================================================

first_condition = False
second_condition = False

result = first_condition or second_condition

print(result)


# =============================================================================
# 06. or With Both True
# =============================================================================

first_condition = True
second_condition = True

result = first_condition or second_condition

print(result)


# =============================================================================
# 07. Basic not
# =============================================================================

is_active: bool = True

result = not is_active

print(result)


# =============================================================================
# 08. not With False
# =============================================================================

is_completed: bool = False

result = not is_completed

print(result)


# =============================================================================
# 09. Combining and With Comparisons
# =============================================================================

age: int = 25

result = age >= 18 and age <= 60

print(result)


# =============================================================================
# 10. Combining or With Comparisons
# =============================================================================

temperature: float = 35.0

result = temperature < 0 or temperature > 30

print(result)


# =============================================================================
# 11. not With a Comparison
# =============================================================================

number: int = 10

result = not number == 20

print(result)


# =============================================================================
# 12. not With Membership
# =============================================================================

language: str = "Python"

result = not language in {"Java", "C++"}

print(result)


# =============================================================================
# 13. and With Multiple Conditions
# =============================================================================

age = 25
has_id: bool = True
has_ticket: bool = True

can_enter: bool = (
    age >= 18
    and has_id
    and has_ticket
)

print(can_enter)


# =============================================================================
# 14. or With Multiple Conditions
# =============================================================================

is_admin: bool = False
is_manager: bool = True
is_owner: bool = False

has_access: bool = (
    is_admin
    or is_manager
    or is_owner
)

print(has_access)


# =============================================================================
# 15. Combining and and or
# =============================================================================

age = 25
has_permission: bool = True

can_access: bool = (
    age >= 18
    and has_permission
)

print(can_access)


# =============================================================================
# 16. Parentheses With Logical Operators
# =============================================================================

is_weekend: bool = True
is_holiday: bool = False

can_relax: bool = (
    is_weekend
    or is_holiday
)

print(can_relax)


# =============================================================================
# 17. Parentheses Change Logical Meaning
# =============================================================================

age = 25
has_permission = False
is_admin = True

result = (
    (age >= 18 and has_permission)
    or is_admin
)

print(result)


# =============================================================================
# 18. Logical Operator Precedence
# =============================================================================

first: bool = True
second: bool = False
third: bool = True

result = first or second and third

print(result)

# and has higher precedence than or.

# The expression is interpreted as:

# first or (second and third)


# =============================================================================
# 19. Explicit Parentheses for Readability
# =============================================================================

first = True
second = False
third = True

result = first or (second and third)

print(result)


# =============================================================================
# 20. Negating a Compound Condition
# =============================================================================

age = 25
has_permission = True

result = not (
    age >= 18
    and has_permission
)

print(result)


# =============================================================================
# 21. De Morgan's Law With and
# =============================================================================

is_raining: bool = False
is_cold: bool = False

result = not (
    is_raining
    and is_cold
)

print(result)


# =============================================================================
# 22. De Morgan's Law With or
# =============================================================================

is_raining = True
is_cold = False

result = not (
    is_raining
    or is_cold
)

print(result)


# =============================================================================
# 23. Equivalent De Morgan Expression
# =============================================================================

is_raining = True
is_cold = False

result = (
    not is_raining
    and not is_cold
)

print(result)


# =============================================================================
# 24. and Returns an Operand
# =============================================================================

left_value: str = "Hello"
right_value: str = "Python"

result = left_value and right_value

print(result)


# =============================================================================
# 25. and Returns the Falsy Operand
# =============================================================================

left_value = ""
right_value = "Python"

result = left_value and right_value

print(result)


# =============================================================================
# 26. or Returns an Operand
# =============================================================================

first_value: str = ""
second_value: str = "Python"

result = first_value or second_value

print(result)


# =============================================================================
# 27. or Returns the First Truthy Operand
# =============================================================================

first_value = "Hello"
second_value = "Python"

result = first_value or second_value

print(result)


# =============================================================================
# 28. Using or for a Default Value
# =============================================================================

username: str = ""

display_name: str = username or "Guest"

print(display_name)


# =============================================================================
# 29. Using or With a Non-Empty Value
# =============================================================================

username = "Shreyas"

display_name = username or "Guest"

print(display_name)


# =============================================================================
# 30. Using and for Conditional Value Selection
# =============================================================================

is_authenticated: bool = True

message: str = (
    is_authenticated
    and "Welcome"
)

print(message)


# =============================================================================
# 31. and With Numeric Values
# =============================================================================

first_number: int = 10
second_number: int = 20

result = first_number and second_number

print(result)


# =============================================================================
# 32. and With Zero
# =============================================================================

first_number = 0
second_number = 20

result = first_number and second_number

print(result)


# =============================================================================
# 33. or With Zero
# =============================================================================

first_number = 0
second_number = 20

result = first_number or second_number

print(result)


# =============================================================================
# 34. Boolean Conversion With bool
# =============================================================================

value: str = "Python"

truth_value: bool = bool(value)

print(truth_value)


# =============================================================================
# 35. Combining bool With not
# =============================================================================

value = ""

truth_value = not bool(value)

print(truth_value)


# =============================================================================
# 36. Short-Circuit Evaluation With and
# =============================================================================

def get_false() -> bool:
    """Return False."""
    print("get_false() called")

    return False


def get_true() -> bool:
    """Return True."""
    print("get_true() called")

    return True


short_circuit_and: bool = (
    get_false()
    and get_true()
)

print(short_circuit_and)

# get_true() is not called because the left side of and is False.


# =============================================================================
# 37. Short-Circuit Evaluation With or
# =============================================================================

short_circuit_or: bool = (
    get_true()
    or get_false()
)

print(short_circuit_or)

# get_false() is not called because the left side of or is True.


# =============================================================================
# 38. Avoiding Division With Short-Circuit and
# =============================================================================

dividend: int = 10
divisor: int = 0

is_valid_division: bool = (
    divisor != 0
    and dividend / divisor > 2
)

print(is_valid_division)


# =============================================================================
# 39. Safe Attribute Access Pattern
# =============================================================================

user_name: str | None = None

has_user_name: bool = (
    user_name is not None
    and len(user_name) > 0
)

print(has_user_name)


# =============================================================================
# 40. Login Validation
# =============================================================================

entered_username: str = "admin"
entered_password: str = "secret"

valid_username: bool = entered_username == "admin"
valid_password: bool = entered_password == "secret"

login_successful: bool = (
    valid_username
    and valid_password
)

print(login_successful)


# =============================================================================
# 41. Permission Validation
# =============================================================================

is_authenticated = True
is_admin = False
has_permission = True

can_modify: bool = (
    is_authenticated
    and (is_admin or has_permission)
)

print(can_modify)


# =============================================================================
# 42. Age Validation
# =============================================================================

user_age: int = 25

is_valid_age: bool = (
    user_age >= 18
    and user_age <= 65
)

print(is_valid_age)


# =============================================================================
# 43. Range Validation
# =============================================================================

score_value: int = 85

is_valid_score: bool = (
    0 <= score_value <= 100
)

print(is_valid_score)


# =============================================================================
# 44. Multiple Alternative Conditions
# =============================================================================

payment_method: str = "card"

is_supported_payment: bool = (
    payment_method == "cash"
    or payment_method == "card"
    or payment_method == "upi"
)

print(is_supported_payment)


# =============================================================================
# 45. Combining Membership and Logical Operators
# =============================================================================

role: str = "editor"

allowed_roles: set[str] = {
    "admin",
    "editor",
}

is_allowed: bool = (
    role in allowed_roles
    and role != "guest"
)

print(is_allowed)


# =============================================================================
# 46. Logical Operators With None
# =============================================================================

value: str | None = None

has_value: bool = value is not None

print(has_value)


# =============================================================================
# 47. Logical Operators With Empty Collections
# =============================================================================

items: list[str] = []

has_items: bool = bool(items)

print(has_items)


# =============================================================================
# 48. Practical Access-Control Function
# =============================================================================

def can_access_dashboard(
    is_authenticated: bool,
    is_admin: bool,
    is_active: bool,
) -> bool:
    """Return whether a user can access the dashboard."""
    return (
        is_authenticated
        and is_active
        and is_admin
    )


dashboard_access: bool = can_access_dashboard(
    is_authenticated=True,
    is_admin=True,
    is_active=True,
)

print(dashboard_access)


# =============================================================================
# 49. Practical Validation Function
# =============================================================================

def is_valid_registration(
    username: str,
    password: str,
    age: int,
) -> bool:
    """Validate basic registration requirements."""
    valid_username: bool = (
        bool(username)
        and len(username) >= 3
    )

    valid_password: bool = (
        bool(password)
        and len(password) >= 8
    )

    valid_age: bool = (
        age >= 18
        and age <= 100
    )

    return (
        valid_username
        and valid_password
        and valid_age
    )


registration_valid: bool = is_valid_registration(
    username="python_user",
    password="secure123",
    age=25,
)

print(registration_valid)


# =============================================================================
# 50. Practical Combined Logical Expression
# =============================================================================

def can_place_order(
    is_authenticated: bool,
    has_stock: bool,
    payment_confirmed: bool,
    is_admin: bool,
) -> bool:
    """
    Determine whether an order can be placed.

    A normal customer needs authentication, stock, and payment.

    An administrator can place the order when authenticated and stock
    is available, even when payment has not yet been confirmed.
    """
    normal_order: bool = (
        is_authenticated
        and has_stock
        and payment_confirmed
    )

    admin_order: bool = (
        is_authenticated
        and has_stock
        and is_admin
    )

    return normal_order or admin_order


order_allowed: bool = can_place_order(
    is_authenticated=True,
    has_stock=True,
    payment_confirmed=False,
    is_admin=True,
)

print(order_allowed)


# =============================================================================
# Logical Operator Summary
# =============================================================================
"""
Python has three logical operators:

    and
    or
    not


1. and

The and operator evaluates operands from left to right.

Conceptually:

    True and True
        -> True

    True and False
        -> False

    False and True
        -> False

    False and False
        -> False

Important:

    and

does not necessarily return a Boolean.

It returns one of its operands.

Example:

    result = "Hello" and "Python"

The result is:

    "Python"

If the first operand is falsy:

    result = "" and "Python"

the result is:

    ""


2. or

The or operator evaluates operands from left to right.

Conceptually:

    True or True
        -> True

    True or False
        -> True

    False or True
        -> True

    False or False
        -> False

Like and, or does not necessarily return a Boolean.

It returns one of its operands.

Example:

    result = "" or "Python"

The result is:

    "Python"


3. not

The not operator reverses the truth value.

Examples:

    not True
        -> False

    not False
        -> True

    not 0
        -> True

    not 10
        -> False

    not ""
        -> True

    not "Python"
        -> False


Short-circuit evaluation:

    and

stops when a falsy operand is found.

Example:

    False and some_function()

some_function() does not need to be evaluated.

Similarly:

    or

stops when a truthy operand is found.

Example:

    True or some_function()

some_function() does not need to be evaluated.


Truthiness:

Python considers many objects truthy or falsy.

Common falsy values include:

    False
    None
    0
    0.0
    ""
    []
    ()
    {}
    set()

Most other objects are truthy.

Logical operators use this truth-value testing.


Operator precedence:

    not
        ↓
    and
        ↓
    or

Therefore:

    not a and b or c

is conceptually evaluated as:

    ((not a) and b) or c

Use parentheses when the intended logic should be made explicit.


Common patterns:

    condition_a and condition_b

    condition_a or condition_b

    not condition

    username or "Guest"

    is_authenticated and is_active

    is_admin or is_owner

    is_valid and has_permission


Important distinction:

    and
    or

are logical operators.

They are different from:

    &
    |

which are bitwise operators.


Comparison operators can be combined with logical operators.

Example:

    age >= 18 and age <= 65

Membership tests can also be combined:

    username in allowed_users and is_active


Identity tests can be combined:

    value is not None and bool(value)


Core model:

    not
        ↓
    reverses truthiness

    and
        ↓
    requires both sides to continue

    or
        ↓
    accepts the first truthy result


Remember:

    and
        returns the first falsy operand,
        or the last operand if all are truthy.

    or
        returns the first truthy operand,
        or the last operand if all are falsy.

This behaviour is useful for short-circuiting and default-value patterns.
"""

# =============================================================================
# End of 05_logical_operators.py
# =============================================================================