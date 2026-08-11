# type: ignore
# =============================================================================
# 12. Short-Circuit Evaluation
# =============================================================================
"""
Python Operators

File:
    12_short_circuit_evaluation.py

Topic:
    Short-Circuit Evaluation

Overview:
    Short-circuit evaluation means Python may stop evaluating a logical
    expression as soon as the final result is already known.

    Python short-circuits these operators:

        and
        or

    With and:

        False and anything

    is always False, so Python does not need to evaluate the right side.

    With or:

        True or anything

    is always True, so Python does not need to evaluate the right side.

    Short-circuit evaluation is useful for:

        - Avoiding unnecessary work
        - Preventing errors
        - Guarding function calls
        - Checking values before using them
        - Improving readability
        - Implementing fallback logic
        - Handling optional values
        - Protecting operations from invalid input

Topics covered:

    - Basic and short-circuiting
    - Basic or short-circuiting
    - False and expression
    - True and expression
    - True or expression
    - False or expression
    - Function-call short-circuiting
    - Preventing division by zero
    - None checks
    - Empty collections
    - Membership checks
    - Permission checks
    - Validation guards
    - Expensive operation guards
    - Lazy fallback evaluation
    - Boolean return values
    - Truthy values
    - Falsy values
    - Operand return values
    - Evaluation order
    - Practical validation
"""

# =============================================================================
# 01. Basic and Short-Circuit
# =============================================================================

first_condition: bool = False
second_condition: bool = True

and_result: bool = first_condition and second_condition

print(and_result)

# Because the first operand is False, Python already knows that the entire
# and expression must be False.


# =============================================================================
# 02. Basic or Short-Circuit
# =============================================================================

first_condition_02: bool = True
second_condition_02: bool = False

or_result: bool = first_condition_02 or second_condition_02

print(or_result)

# Because the first operand is True, Python already knows that the entire
# or expression must be True.


# =============================================================================
# 03. False and Expression
# =============================================================================

result_03: bool = False and True

print(result_03)

# The right-hand expression is unnecessary because False and anything
# always produces False.


# =============================================================================
# 04. True and Expression
# =============================================================================

result_04: bool = True and True

print(result_04)

# Because the left side is True, Python must evaluate the right side.


# =============================================================================
# 05. True or Expression
# =============================================================================

result_05: bool = True or False

print(result_05)

# The right side is not evaluated because True or anything is True.


# =============================================================================
# 06. False or Expression
# =============================================================================

result_06: bool = False or True

print(result_06)

# Because the left side is False, Python must evaluate the right side.


# =============================================================================
# 07. Function Used With and
# =============================================================================

def check_permission() -> bool:
    """
    Return whether a user has permission.
    """
    print("Permission check executed.")
    return True


permission_result: bool = True and check_permission()

print(permission_result)


# =============================================================================
# 08. Function Skipped With and
# =============================================================================

def perform_operation() -> bool:
    """
    Represent an operation that should not run.
    """
    print("Operation executed.")
    return True


operation_result: bool = False and perform_operation()

print(operation_result)

# perform_operation() is never called because the left side is False.


# =============================================================================
# 09. Function Skipped With or
# =============================================================================

def load_default_value() -> str:
    """
    Return a fallback value.
    """
    print("Fallback executed.")
    return "default"


fallback_result: str = "existing" or load_default_value()

print(fallback_result)

# load_default_value() is not called because "existing" is truthy.


# =============================================================================
# 10. Function Executed With or
# =============================================================================

empty_value: str = ""

fallback_result_10: str = empty_value or load_default_value()

print(fallback_result_10)

# The empty string is falsy, so Python evaluates the right side.


# =============================================================================
# 11. Prevent Division By Zero
# =============================================================================

divisor: int = 0

safe_division_check: bool = (
    divisor != 0
    and 100 / divisor > 2
)

print(safe_division_check)

# Because divisor != 0 is False, Python does not evaluate 100 / divisor.


# =============================================================================
# 12. Safe Division Function
# =============================================================================

def can_divide(
    numerator: float,
    denominator: float,
) -> bool:
    """
    Return whether a division operation is safe.
    """
    return denominator != 0 and numerator / denominator >= 0


division_is_safe: bool = can_divide(
    10.0,
    2.0,
)

print(division_is_safe)


# =============================================================================
# 13. Prevent Invalid List Access
# =============================================================================

numbers: list[int] = []

has_items: bool = bool(numbers)

safe_first_access: bool = (
    has_items
    and numbers[0] > 0
)

print(safe_first_access)

# numbers[0] is not evaluated when the list is empty.


# =============================================================================
# 14. Safe List Access
# =============================================================================

values: list[int] = [10, 20, 30]

has_values: bool = bool(values)

first_value_is_positive: bool = (
    has_values
    and values[0] > 0
)

print(first_value_is_positive)


# =============================================================================
# 15. None Guard
# =============================================================================

username: str | None = None

has_username: bool = (
    username is not None
    and len(username) > 3
)

print(has_username)

# len(username) is not evaluated when username is None.


# =============================================================================
# 16. None Guard With a Valid String
# =============================================================================

username_16: str | None = "Shreyas"

valid_username: bool = (
    username_16 is not None
    and len(username_16) >= 3
)

print(valid_username)


# =============================================================================
# 17. Empty String With or
# =============================================================================

display_name: str = ""

name_to_display: str = display_name or "Guest"

print(name_to_display)


# =============================================================================
# 18. Existing String With or
# =============================================================================

display_name_18: str = "Alex"

name_to_display_18: str = display_name_18 or "Guest"

print(name_to_display_18)


# =============================================================================
# 19. Empty List With or
# =============================================================================

items: list[str] = []

items_to_use: list[str] = items or ["Default"]

print(items_to_use)


# =============================================================================
# 20. Existing List With or
# =============================================================================

items_20: list[str] = ["Python", "SQL"]

items_to_use_20: list[str] = (
    items_20
    or ["Default"]
)

print(items_to_use_20)


# =============================================================================
# 21. Empty Dictionary With or
# =============================================================================

configuration: dict[str, str] = {}

configuration_to_use: dict[str, str] = (
    configuration
    or {"mode": "development"}
)

print(configuration_to_use)


# =============================================================================
# 22. Existing Dictionary With or
# =============================================================================

configuration_22: dict[str, str] = {
    "mode": "production",
}

configuration_to_use_22: dict[str, str] = (
    configuration_22
    or {"mode": "development"}
)

print(configuration_to_use_22)


# =============================================================================
# 23. Permission Guard
# =============================================================================

is_authenticated: bool = True
is_admin: bool = False

can_delete: bool = (
    is_authenticated
    and is_admin
)

print(can_delete)


# =============================================================================
# 24. Authentication Guard
# =============================================================================

is_logged_in: bool = False

can_access_dashboard: bool = (
    is_logged_in
    and check_permission()
)

print(can_access_dashboard)

# check_permission() is skipped because is_logged_in is False.


# =============================================================================
# 25. Multiple and Conditions
# =============================================================================

account_active: bool = True
email_verified: bool = True
has_permission: bool = True

can_access: bool = (
    account_active
    and email_verified
    and has_permission
)

print(can_access)

# Python evaluates from left to right and stops when it encounters a falsy
# operand.


# =============================================================================
# 26. Multiple or Conditions
# =============================================================================

primary_value: str = ""
secondary_value: str = ""
tertiary_value: str = "Fallback"

selected_value: str = (
    primary_value
    or secondary_value
    or tertiary_value
)

print(selected_value)

# Python continues until it finds the first truthy operand.


# =============================================================================
# 27. First Truthy Value
# =============================================================================

first_option: str = ""
second_option: str = "Python"
third_option: str = "SQL"

selected_option: str = (
    first_option
    or second_option
    or third_option
)

print(selected_option)


# =============================================================================
# 28. All Falsy Values With or
# =============================================================================

first_value_28: str = ""
second_value_28: str = ""
third_value_28: str = ""

fallback_28: str = (
    first_value_28
    or second_value_28
    or third_value_28
    or "Default"
)

print(fallback_28)


# =============================================================================
# 29. First Falsy Value With and
# =============================================================================

first_value_29: bool = True
second_value_29: bool = True
third_value_29: bool = False

and_chain_29: bool = (
    first_value_29
    and second_value_29
    and third_value_29
)

print(and_chain_29)


# =============================================================================
# 30. First Falsy Value Stops Evaluation
# =============================================================================

def first_check() -> bool:
    """
    Return False and demonstrate evaluation order.
    """
    print("First check executed.")
    return False


def second_check() -> bool:
    """
    Return True.
    """
    print("Second check executed.")
    return True


check_result: bool = (
    first_check()
    and second_check()
)

print(check_result)

# second_check() is skipped because first_check() returned False.


# =============================================================================
# 31. First Truthy Value Stops or Evaluation
# =============================================================================

def primary_check() -> bool:
    """
    Return True and demonstrate short-circuiting.
    """
    print("Primary check executed.")
    return True


def secondary_check() -> bool:
    """
    Return True.
    """
    print("Secondary check executed.")
    return True


or_check_result: bool = (
    primary_check()
    or secondary_check()
)

print(or_check_result)

# secondary_check() is skipped because primary_check() returned True.


# =============================================================================
# 32. Evaluation Order With Three Functions
# =============================================================================

def check_one() -> bool:
    """
    Return True.
    """
    print("check_one")
    return True


def check_two() -> bool:
    """
    Return False.
    """
    print("check_two")
    return False


def check_three() -> bool:
    """
    Return True.
    """
    print("check_three")
    return True


three_check_result: bool = (
    check_one()
    and check_two()
    and check_three()
)

print(three_check_result)

# check_three() is skipped because check_two() returned False.


# =============================================================================
# 33. Short-Circuit With Membership
# =============================================================================

allowed_roles: list[str] = [
    "admin",
    "manager",
]

role: str = "guest"

has_allowed_role: bool = (
    role in allowed_roles
    and role == "admin"
)

print(has_allowed_role)


# =============================================================================
# 34. Short-Circuit With Dictionary Access
# =============================================================================

user_data: dict[str, str] = {}

has_email: bool = (
    "email" in user_data
    and user_data["email"].endswith("@example.com")
)

print(has_email)

# The dictionary value is accessed only when the key exists.


# =============================================================================
# 35. Safe Dictionary Access
# =============================================================================

user_data_35: dict[str, str] = {
    "email": "alex@example.com",
}

valid_email: bool = (
    "email" in user_data_35
    and user_data_35["email"].endswith("@example.com")
)

print(valid_email)


# =============================================================================
# 36. Short-Circuit With String Operations
# =============================================================================

email: str = ""

valid_email_format: bool = (
    bool(email)
    and "@" in email
    and "." in email
)

print(valid_email_format)

# Later checks are skipped when email is empty.


# =============================================================================
# 37. Short-Circuit With Collection Length
# =============================================================================

records: list[int] = []

has_records: bool = (
    len(records) > 0
    and records[0] > 10
)

print(has_records)


# =============================================================================
# 38. Short-Circuit With Expensive Operation
# =============================================================================

def expensive_calculation() -> bool:
    """
    Represent a calculation that should run only when necessary.
    """
    print("Expensive calculation executed.")
    return True


feature_enabled: bool = False

calculation_allowed: bool = (
    feature_enabled
    and expensive_calculation()
)

print(calculation_allowed)

# expensive_calculation() is skipped.


# =============================================================================
# 39. Expensive Operation Allowed
# =============================================================================

feature_enabled_39: bool = True

calculation_allowed_39: bool = (
    feature_enabled_39
    and expensive_calculation()
)

print(calculation_allowed_39)


# =============================================================================
# 40. or as a Fallback
# =============================================================================

def get_primary_value() -> str:
    """
    Return an empty value.
    """
    return ""


def get_backup_value() -> str:
    """
    Return a backup value.
    """
    return "Backup"


selected_value_40: str = (
    get_primary_value()
    or get_backup_value()
)

print(selected_value_40)


# =============================================================================
# 41. or Does Not Always Return bool
# =============================================================================

value_41: str = "Python"

result_41: str = value_41 or "Default"

print(result_41)

# The or operator returns an operand, not necessarily True or False.


# =============================================================================
# 42. and Does Not Always Return bool
# =============================================================================

value_42: str = "Python"

result_42: str = value_42 and "Programming"

print(result_42)

# The and operator also returns an operand.


# =============================================================================
# 43. and With a Falsy Operand
# =============================================================================

value_43: str = ""

result_43: str = value_43 and "Programming"

print(result_43)

# Because value_43 is falsy, Python returns it without evaluating the
# right-hand operand.


# =============================================================================
# 44. or With a Truthy Operand
# =============================================================================

value_44: str = "Python"

result_44: str = value_44 or "Programming"

print(result_44)

# Because value_44 is truthy, Python returns it immediately.


# =============================================================================
# 45. Boolean Conversion With bool
# =============================================================================

value_45: str = ""

boolean_result_45: bool = bool(
    value_45
)

print(boolean_result_45)

# bool() explicitly converts the value to True or False.


# =============================================================================
# 46. Guarding an Attribute Access
# =============================================================================

class User:
    """
    Represent a simple user object.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name


user: User | None = User("Alex")

has_long_name: bool = (
    user is not None
    and len(user.name) > 3
)

print(has_long_name)


# =============================================================================
# 47. Guarding a Method Call
# =============================================================================

user_47: User | None = None

user_name_valid: bool = (
    user_47 is not None
    and user_47.name.startswith("A")
)

print(user_name_valid)

# The method call is skipped because user_47 is None.


# =============================================================================
# 48. Practical Validation Guard
# =============================================================================

def validate_username(
    username: str | None,
) -> bool:
    """
    Validate a username safely.
    """
    return (
        username is not None
        and bool(username)
        and 3 <= len(username) <= 20
    )


username_result: bool = validate_username(
    "python_user",
)

print(username_result)


# =============================================================================
# 49. Practical Configuration Fallback
# =============================================================================

def get_configuration(
    configured_value: str | None,
) -> str:
    """
    Return configured value or a default.
    """
    return configured_value or "development"


configuration_result: str = get_configuration(
    None,
)

print(configuration_result)


# =============================================================================
# 50. Practical Authentication Guard
# =============================================================================

def can_view_profile(
    is_authenticated: bool,
    user: User | None,
) -> bool:
    """
    Return whether a profile can be viewed.
    """
    return (
        is_authenticated
        and user is not None
        and bool(user.name)
    )


profile_access: bool = can_view_profile(
    is_authenticated=True,
    user=User("Alex"),
)

print(profile_access)


# =============================================================================
# Short-Circuit Evaluation Summary
# =============================================================================
"""
Short-circuit evaluation allows Python to stop evaluating a logical
expression when the final result is already known.

For and:

    False and anything
        ↓
    False

Python does not need to evaluate anything after the first falsy operand.

For or:

    True or anything
        ↓
    True

Python does not need to evaluate anything after the first truthy operand.

Examples:

    is_valid and process()

    is_authenticated and is_admin

    username is not None and len(username) > 3

    configured_value or default_value

    primary_value or secondary_value or fallback_value

Important:

    and and or return operands, not necessarily bool values.

Example:

    "Python" and "Programming"

returns:

    "Programming"

Example:

    "" or "Default"

returns:

    "Default"

Short-circuiting is especially useful for guards:

    denominator != 0 and numerator / denominator > 0

    user is not None and user.name.startswith("A")

    "email" in data and data["email"].endswith("@example.com")

    is_authenticated and check_permission()

The general evaluation model is:

    LEFT SIDE
        ↓
    CHECK TRUTHINESS
        ↓
    RESULT ALREADY KNOWN?
       / \
     YES  NO
      ↓    ↓
    STOP  EVALUATE RIGHT SIDE

For and:

    First falsy operand stops evaluation.

For or:

    First truthy operand stops evaluation.

Core idea:

    and
        ↓
    stop at first falsy value

    or
        ↓
    stop at first truthy value

Short-circuit evaluation is both a logical behaviour and a practical
technique for writing safe, efficient, and readable Python code.
"""

# =============================================================================
# End of 12_short_circuit_evaluation.py
# =============================================================================