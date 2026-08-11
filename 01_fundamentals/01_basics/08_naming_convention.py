"""
==============================================================================
Python Basics
==============================================================================

File
----
07_naming_conventions.py

Topic
-----
Naming Conventions

Overview
--------
Names are used for variables, functions, classes, constants, modules,
and other Python objects.

Good names make code easier to read, understand, maintain, and modify.

This file covers:

    - Valid identifiers
    - Invalid identifiers
    - Case sensitivity
    - snake_case
    - UPPER_CASE
    - PascalCase
    - Leading underscores
    - Trailing underscores
    - Double underscores
    - Naming functions
    - Naming classes
    - Naming constants
    - Naming modules
    - Naming boolean variables
    - Descriptive names
    - Avoiding ambiguous names
    - Python naming conventions
"""


# =============================================================================
# 01. Basic Identifier
# =============================================================================

user_name: str = "Alex"

print(
    user_name
)


# An identifier is a name used to identify something in Python.


# =============================================================================
# 02. Letters, Numbers, and Underscores
# =============================================================================

student_name_1: str = "Alex"

student_name_2: str = "Sam"

print(
    student_name_1,
    student_name_2,
)


# Identifiers can contain:
#
#     letters
#     digits
#     underscores
#
# A digit cannot be the first character.


# =============================================================================
# 03. Valid Names
# =============================================================================

valid_variable_name: int = 100

another_valid_name: str = "Python"

_private_style_name: str = "Internal"

print(
    valid_variable_name
)

print(
    another_valid_name
)

print(
    _private_style_name
)


# =============================================================================
# 04. Invalid Names
# =============================================================================

"""
The following names would be invalid:

    1student = 100
    user-name = "Alex"
    user name = "Alex"
    class = "Python"

They are intentionally not executed here because they would
produce syntax errors.
"""


# =============================================================================
# 05. Names Cannot Start With a Number
# =============================================================================

valid_numbered_name: str = "Python"

print(
    valid_numbered_name
)


# Correct:

data_2026 = "Python"


# Incorrect:

# 2026_data = "Python"


# =============================================================================
# 06. Underscores Are Allowed
# =============================================================================

user_first_name: str = "Alex"

database_connection_string: str = "example"

print(
    user_first_name
)

print(
    database_connection_string
)


# Underscores are commonly used to separate words.


# =============================================================================
# 07. Python Is Case-Sensitive
# =============================================================================

case_sensitive_name: str = "Alex"

CASE_SENSITIVE_NAME: str = "Sam"

print(
    case_sensitive_name
)

print(
    CASE_SENSITIVE_NAME
)


# These are different identifiers.


# =============================================================================
# 08. snake_case
# =============================================================================

first_name: str = "Alex"

last_name: str = "Smith"

employee_id: int = 1001

database_name: str = "production"

print(
    first_name,
    last_name,
    employee_id,
    database_name,
)


# snake_case is the standard convention for:
#
#     variables
#     functions
#     methods


# =============================================================================
# 09. UPPER_CASE
# =============================================================================

MAX_USERS: int = 100

DEFAULT_TIMEOUT: int = 30

DATABASE_PORT: int = 5432

print(
    MAX_USERS,
    DEFAULT_TIMEOUT,
    DATABASE_PORT,
)


# UPPER_CASE is conventionally used for constants.


# =============================================================================
# 10. PascalCase
# =============================================================================

class DataProcessor:
    """
    Example class using PascalCase.
    """

    pass


processor_object: DataProcessor = DataProcessor()

print(
    processor_object
)


# PascalCase is conventionally used for class names.


# =============================================================================
# 11. Function Naming
# =============================================================================

def calculate_total(
    first_value: int,
    second_value: int,
) -> int:
    return first_value + second_value


total_result: int = calculate_total(
    10,
    20,
)

print(
    total_result
)


# Functions normally use snake_case.


# =============================================================================
# 12. Boolean Naming
# =============================================================================

is_active: bool = True

has_permission: bool = False

can_execute: bool = True

should_retry: bool = False

print(
    is_active,
    has_permission,
    can_execute,
    should_retry,
)


# Boolean names are often written as questions or conditions:
#
#     is_
#     has_
#     can_
#     should_


# =============================================================================
# 13. Descriptive Names
# =============================================================================

customer_age: int = 30

monthly_salary: float = 50000.0

account_balance: float = 15000.0

print(
    customer_age
)

print(
    monthly_salary
)

print(
    account_balance
)


# Descriptive names communicate meaning.


# =============================================================================
# 14. Avoid Single-Letter Names When Meaning Is Unclear
# =============================================================================

total_price: float = 1000.0

print(
    total_price
)


# Prefer:

total_price = 1000.0


# over ambiguous names such as:

# x = 1000.0


# Single-letter names can be appropriate in limited contexts,
# such as mathematical formulas or loop variables.


# =============================================================================
# 15. Common Short Names in Loops
# =============================================================================

numbers: list[int] = [
    10,
    20,
    30,
]

for number in numbers:
    print(
        number
    )


# A short loop variable can be perfectly readable when its meaning
# is obvious from the surrounding context.


# =============================================================================
# 16. Avoid Ambiguous Abbreviations
# =============================================================================

customer_address: str = "Bengaluru"

print(
    customer_address
)


# Prefer:

customer_address # pyright: ignore[reportUnusedExpression]


# instead of unclear names such as:

# cust_addr


# Abbreviations should be used only when they are widely understood
# within the project's context.


# =============================================================================
# 17. Avoid Built-in Names
# =============================================================================

"""
Avoid using names such as:

    list
    str
    int
    type
    id
    input
    print
    sum

for your own variables.

Doing so can hide the built-in name inside the current scope.
"""


# Example of a safe name:

user_list: list[int] = [
    10,
    20,
]

print(
    user_list
)


# =============================================================================
# 18. Avoid Shadowing Built-ins
# =============================================================================

shadowing_example_value: int = 100

print(
    shadowing_example_value
)


# Avoid:

# list = [10, 20]
#
# str = "Python"
#
# type = "Example"


# These names are valid identifiers but can cause confusion
# because they shadow Python built-ins.


# =============================================================================
# 19. Trailing Underscore
# =============================================================================

class_name_: str = "Example"

print(
    class_name_
)


# A trailing underscore can be used when a desirable name conflicts
# with a Python keyword or another important name.


# Example:

# class = "Example"       # invalid
# class_ = "Example"      # valid


# =============================================================================
# 20. Leading Underscore
# =============================================================================

_internal_value: int = 100

print(
    _internal_value
)


# A single leading underscore conventionally indicates:
#
#     "This is intended for internal use."


# It does not create a strict access restriction.


# =============================================================================
# 21. Double Leading Underscore
# =============================================================================

class EmployeeRecord:
    """
    Demonstrate a double-leading-underscore attribute.
    """

    def __init__(
        self,
        employee_name: str,
    ) -> None:
        self.__employee_name = employee_name

    def get_employee_name(self) -> str:
        return self.__employee_name


employee_record: EmployeeRecord = (
    EmployeeRecord(
        "Alex"
    )
)

print(
    employee_record.get_employee_name()
)


# A double leading underscore inside a class triggers name mangling.


# =============================================================================
# 22. Double Leading and Trailing Underscores
# =============================================================================

class ExampleObject:
    """
    Demonstrate a special method name.
    """

    def __init__(self) -> None:
        pass


example_object: ExampleObject = ExampleObject()

print(
    example_object
)


# Names such as __init__ are reserved for special Python behaviour.
#
# These are often called "dunder" names:
#
#     double underscore + name + double underscore


# =============================================================================
# 23. Module Naming
# =============================================================================

"""
Python module filenames normally use:

    lowercase
    snake_case

Examples:

    data_processing.py
    file_reader.py
    database_utils.py
"""


# =============================================================================
# 24. Package Naming
# =============================================================================

"""
Python package names are normally:

    lowercase
    short
    simple

Examples:

    utilities
    data_processing
    algorithms
"""


# =============================================================================
# 25. Class Naming
# =============================================================================

class CustomerRecord:
    """
    Example class using PascalCase.
    """

    pass


class DatabaseConnection:
    """
    Example class using PascalCase.
    """

    pass


# =============================================================================
# 26. Method Naming
# =============================================================================

class UserAccount:
    """
    Demonstrate method naming.
    """

    def get_user_name(
        self,
    ) -> str:
        return "Alex"


user_account: UserAccount = UserAccount()

print(
    user_account.get_user_name()
)


# Methods normally use snake_case.


# =============================================================================
# 27. Constant Naming
# =============================================================================

MAX_RETRY_COUNT: int = 3

DEFAULT_PAGE_SIZE: int = 25

API_TIMEOUT_SECONDS: int = 30

print(
    MAX_RETRY_COUNT
)

print(
    DEFAULT_PAGE_SIZE
)

print(
    API_TIMEOUT_SECONDS
)


# Constants conventionally use UPPER_CASE_WITH_UNDERSCORES.


# =============================================================================
# 28. Avoid Excessively Short Names
# =============================================================================

customer_transaction_count: int = 25

print(
    customer_transaction_count
)


# This is more informative than:

# ctc = 25


# =============================================================================
# 29. Avoid Excessively Long Names
# =============================================================================

employee_count: int = 100

print(
    employee_count
)


# Names should be descriptive without becoming unnecessarily verbose.


# =============================================================================
# 30. Naming Should Reflect Meaning
# =============================================================================

maximum_retry_count: int = 3

current_retry_count: int = 1

print(
    maximum_retry_count
)

print(
    current_retry_count
)


# The names communicate different concepts clearly.


# =============================================================================
# 31. Avoid Generic Names
# =============================================================================

customer_email_address: str = (
    "alex@example.com"
)

print(
    customer_email_address
)


# Prefer a meaningful name over something generic such as:

# value = "alex@example.com"


# =============================================================================
# 32. Naming Temporary Values
# =============================================================================

temporary_calculation_result: int = (
    100
    + 200
)

print(
    temporary_calculation_result
)


# Temporary names can still be descriptive.


# =============================================================================
# 33. Naming Private-Looking Members
# =============================================================================

class DataStore:
    """
    Example internal attribute.
    """

    def __init__(self) -> None:
        self._internal_cache: dict[str, int] = {}


data_store: DataStore = DataStore()

print(
    data_store._internal_cache)# pyright: ignore[reportPrivateUsage]


# A single leading underscore communicates intended internal usage.
#
# It is a convention, not strict privacy.


# =============================================================================
# 34. Naming With Acronyms
# =============================================================================

api_url: str = "https://example.com"

http_status_code: int = 200

database_api_client: str = "Client"

print(
    api_url
)

print(
    http_status_code
)

print(
    database_api_client
)


# In normal variable and function names, lowercase snake_case is preferred.


# =============================================================================
# 35. Naming Consistency
# =============================================================================

employee_first_name: str = "Alex"
employee_last_name: str = "Smith"

employee_department: str = "Engineering"

print(
    employee_first_name,
    employee_last_name,
    employee_department,
)


# Consistent naming makes related variables easier to recognize.


# =============================================================================
# 36. Naming Conventions Are Mostly Conventions
# =============================================================================

"""
Python generally does not enforce most naming conventions.

For example:

    employee_name
    EmployeeName
    EMPLOYEE_NAME

can all be syntactically valid identifiers.

Their conventional meanings are different:

    employee_name
        -> variable / function / method

    EmployeeName
        -> usually class

    EMPLOYEE_NAME
        -> usually constant
"""


# =============================================================================
# 37. Python Keywords Cannot Be Used Normally
# =============================================================================

"""
Python keywords include names such as:

    if
    else
    for
    while
    class
    def
    return
    import
    True
    False
    None

These cannot normally be used as identifiers.
"""


# =============================================================================
# 38. Use Trailing Underscore for Keyword Conflicts
# =============================================================================

class_: str = "Python"

from_: str = "database"

print(
    class_
)

print(
    from_
)


# =============================================================================
# 39. Naming Convention Summary
# =============================================================================

"""
Variables:

    user_name
    account_balance
    employee_count


Functions:

    calculate_total()
    get_user_name()
    process_data()


Classes:

    DataProcessor
    CustomerRecord
    DatabaseConnection


Constants:

    MAX_USERS
    DEFAULT_TIMEOUT
    DATABASE_PORT


Internal names:

    _internal_value


Special Python names:

    __init__
    __name__
    __doc__
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Python identifiers can contain letters, digits, and underscores.

✓ An identifier cannot normally begin with a digit.

✓ Python is case-sensitive.

✓ Standard variable naming:

      snake_case

✓ Standard function naming:

      snake_case

✓ Standard method naming:

      snake_case

✓ Standard class naming:

      PascalCase

✓ Standard constant naming:

      UPPER_CASE

✓ A single leading underscore generally means:

      "intended for internal use"

✓ A trailing underscore can avoid keyword/name conflicts:

      class_

      from_

✓ Double leading underscores inside classes trigger name mangling.

✓ Names such as __init__ and __name__ are special Python names.

✓ Avoid shadowing built-ins such as:

      list
      str
      int
      type
      id
      print
      input
      sum

✓ Prefer descriptive names.

✓ Avoid unnecessary abbreviations.

✓ Keep naming consistent across a project.

The main principle:

    Good name
        ↓
    Clear meaning
        ↓
    Easier code reading
        ↓
    Easier maintenance
"""