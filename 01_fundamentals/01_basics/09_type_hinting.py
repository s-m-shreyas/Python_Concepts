"""
==============================================================================
Python Basics
==============================================================================

File
----
08_type_hints.py

Topic
-----
Type Hints / Type Annotations

Overview
--------
Type hints are annotations that describe the expected types of values,
variables, function parameters, and return values.

Python does not normally enforce type hints at runtime.

Type hints primarily help:

    - Developers
    - IDEs
    - Static type checkers
    - Linters
    - Documentation
    - Code readability

Runtime type checking with type() and isinstance() is covered separately
in the data_types section.

This file covers:

    - Variable annotations
    - Function parameter annotations
    - Return annotations
    - Built-in collection annotations
    - Optional values
    - Union types
    - Any
    - Type aliases
    - Generic collections
    - Nested type hints
    - Type hints for functions
    - Type hints and runtime behaviour
"""


# =============================================================================
# 01. Basic Variable Annotation
# =============================================================================

hint_user_name: str = "Alex"

print(
    hint_user_name
)


# The annotation says:
#
#     hint_user_name is intended to refer to a str.


# =============================================================================
# 02. Integer Annotation
# =============================================================================

hint_user_age: int = 30

print(
    hint_user_age
)


# =============================================================================
# 03. Float Annotation
# =============================================================================

hint_account_balance: float = 15000.50

print(
    hint_account_balance
)


# =============================================================================
# 04. Boolean Annotation
# =============================================================================

hint_is_active: bool = True

print(
    hint_is_active
)


# =============================================================================
# 05. None Annotation
# =============================================================================

hint_missing_value: None = None

print(
    hint_missing_value
)


# `None` can be used directly as a type annotation when the only
# permitted value is None.


# =============================================================================
# 06. Function Parameter Annotation
# =============================================================================

def add_numbers(
    first_number: int,
    second_number: int,
) -> int:
    return first_number + second_number


hint_sum_result: int = add_numbers(
    10,
    20,
)

print(
    hint_sum_result
)


# Parameter annotations describe the intended parameter types.
#
# -> int describes the intended return type.


# =============================================================================
# 07. Function With String Parameters
# =============================================================================

def create_full_name(
    first_name: str,
    last_name: str,
) -> str:
    return f"{first_name} {last_name}"


hint_full_name: str = create_full_name(
    "Alex",
    "Smith",
)

print(
    hint_full_name
)


# =============================================================================
# 08. Function Returning None
# =============================================================================

def display_message(
    message_text: str,
) -> None:
    print(
        message_text
    )


display_message(
    "Hello, Python!"
)


# `-> None` means the function is intended to return None.


# =============================================================================
# 09. List Annotation
# =============================================================================

hint_numbers_list: list[int] = [
    10,
    20,
    30,
]

print(
    hint_numbers_list
)


# list[int] means:
#
#     a list whose elements are intended to be int values.


# =============================================================================
# 10. List of Strings
# =============================================================================

hint_languages_list: list[str] = [
    "Python",
    "SQL",
    "Java",
]

print(
    hint_languages_list
)


# =============================================================================
# 11. Tuple Annotation
# =============================================================================

hint_coordinates: tuple[int, int] = (
    10,
    20,
)

print(
    hint_coordinates
)


# tuple[int, int] describes a tuple containing exactly two int values.


# =============================================================================
# 12. Variable-Length Tuple
# =============================================================================

hint_scores: tuple[int, ...] = (
    80,
    90,
    95,
    88,
)

print(
    hint_scores
)


# tuple[int, ...] means:
#
#     any number of int elements.


# =============================================================================
# 13. Set Annotation
# =============================================================================

hint_unique_numbers: set[int] = {
    10,
    20,
    30,
}

print(
    hint_unique_numbers
)


# =============================================================================
# 14. Frozen Set Annotation
# =============================================================================

hint_fixed_numbers: frozenset[int] = frozenset(
    {
        10,
        20,
        30,
    }
)

print(
    hint_fixed_numbers
)


# =============================================================================
# 15. Dictionary Annotation
# =============================================================================

hint_employee_ages: dict[str, int] = {
    "Alex": 30,
    "Sam": 28,
}

print(
    hint_employee_ages
)


# dict[str, int] means:
#
#     keys   -> str
#     values -> int


# =============================================================================
# 16. Nested Collection Annotation
# =============================================================================

hint_department_employees: dict[str, list[str]] = {
    "Engineering": [
        "Alex",
        "Sam",
    ],
    "Finance": [
        "John",
        "Mike",
    ],
}

print(
    hint_department_employees
)


# Type hints can describe nested structures.


# =============================================================================
# 17. List of Dictionaries
# =============================================================================

hint_employee_records: list[dict[str, str]] = [
    {
        "name": "Alex",
        "department": "Engineering",
    },
    {
        "name": "Sam",
        "department": "Finance",
    },
]

print(
    hint_employee_records
)


# =============================================================================
# 18. Union Type
# =============================================================================

hint_identifier: int | str = 100

print(
    hint_identifier
)

hint_identifier = "EMP100"

print(
    hint_identifier
)


# `int | str` means the value is intended to be either int or str.


# =============================================================================
# 19. Optional Value
# =============================================================================

hint_optional_name: str | None = None

print(
    hint_optional_name
)

hint_optional_name = "Alex"

print(
    hint_optional_name
)


# str | None means:
#
#     either str
#     or None


# =============================================================================
# 20. Optional Function Parameter
# =============================================================================

def greet_user(
    user_name: str | None,
) -> str:
    if user_name is None:
        return "Hello, Guest!"

    return f"Hello, {user_name}!"


hint_guest_message: str = greet_user(
    None
)

hint_named_message: str = greet_user(
    "Alex"
)

print(
    hint_guest_message
)

print(
    hint_named_message
)


# =============================================================================
# 21. Any
# =============================================================================

from typing import Any

hint_any_value: Any = 100

print(
    hint_any_value
)

hint_any_value = "Python"

print(
    hint_any_value
)

hint_any_value = [
    10,
    20,
]

print(
    hint_any_value
)


# Any means that the value is intentionally not restricted
# to a particular type by static typing.


# =============================================================================
# 22. Any in a Dictionary
# =============================================================================

hint_mixed_record: dict[str, Any] = {
    "name": "Alex",
    "age": 30,
    "active": True,
    "scores": [
        80,
        90,
    ],
}

print(
    hint_mixed_record
)


# Any is useful when dictionary values may legitimately have
# different types.


# =============================================================================
# 23. Any as a Function Parameter
# =============================================================================

def display_any_value(
    arbitrary_value: Any,
) -> None:
    print(
        arbitrary_value
    )


display_any_value(
    "Python"
)

display_any_value(
    100
)

display_any_value(
    [10, 20]
)


# =============================================================================
# 24. Type Alias
# =============================================================================

EmployeeId = int

hint_employee_id: EmployeeId = 1001

print(
    hint_employee_id
)


# A type alias gives a descriptive name to an existing type.


# =============================================================================
# 25. Type Alias for a Collection
# =============================================================================

EmployeeScores = dict[str, list[int]]

hint_employee_scores: EmployeeScores = {
    "Alex": [
        80,
        90,
    ],
    "Sam": [
        75,
        85,
    ],
}

print(
    hint_employee_scores
)


# Type aliases can make complex annotations easier to read.


# =============================================================================
# 26. Function Type Alias
# =============================================================================

from collections.abc import Callable

NumberOperation = Callable[
    [int, int],
    int,
]


def multiply_numbers(
    first_value: int,
    second_value: int,
) -> int:
    return first_value * second_value


hint_operation: NumberOperation = multiply_numbers

print(
    hint_operation(
        5,
        4,
    )
)


# Callable describes a callable object.
#
# Here:
#
#     [int, int]
#         -> parameter types
#
#     int
#         -> return type


# =============================================================================
# 27. Type Hint for a Function Parameter
# =============================================================================

def apply_operation(
    operation: NumberOperation,
    first_operand: int,
    second_operand: int,
) -> int:
    return operation(
        first_operand,
        second_operand,
    )


hint_operation_result: int = apply_operation(
    multiply_numbers,
    6,
    7,
)

print(
    hint_operation_result
)


# =============================================================================
# 28. Type Hints Do Not Automatically Convert Values
# =============================================================================

hint_number_text: str = "100"

print(
    hint_number_text
)


# An annotation does not automatically convert:
#
#     "100"
#
# into:
#
#     100
#
# Conversion must be explicit.


# =============================================================================
# 29. Annotation Does Not Perform Runtime Conversion
# =============================================================================

hint_runtime_value: int = int(
    "100"
)

print(
    hint_runtime_value
)


# int() performs the conversion.
#
# The annotation only describes the intended resulting type.


# =============================================================================
# 30. Type Hints Are Not Runtime Type Checking
# =============================================================================

hint_runtime_text: str = "Python"

print(
    hint_runtime_text
)


# The annotation itself does not perform a runtime check.
#
# Runtime checking with:
#
#     type()
#     isinstance()
#
# is covered separately in the data_types section.


# =============================================================================
# 31. Function Annotations Are Available at Runtime
# =============================================================================

def annotated_function(
    first_value: int,
    second_value: str,
) -> bool:
    return bool(
        first_value
        and second_value
    )


print(
    annotated_function.__annotations__
)


# Function annotations are stored as metadata.
#
# They can be inspected at runtime.


# =============================================================================
# 32. Variable Annotations
# =============================================================================

hint_documented_value: int = 100

print(
    hint_documented_value
)


# Variable annotations primarily provide information for
# developers and static analysis tools.


# =============================================================================
# 33. Generic Dictionary With Any Values
# =============================================================================

hint_configuration: dict[str, Any] = {
    "host": "localhost",
    "port": 5432,
    "debug": True,
}

print(
    hint_configuration
)


# =============================================================================
# 34. Generic List of Optional Values
# =============================================================================

hint_optional_scores: list[int | None] = [
    90,
    None,
    85,
]

print(
    hint_optional_scores
)


# Every element is intended to be either int or None.


# =============================================================================
# 35. Dictionary With Optional Values
# =============================================================================

hint_optional_fields: dict[str, str | None] = {
    "name": "Alex",
    "email": None,
}

print(
    hint_optional_fields
)


# =============================================================================
# 36. Nested Union Types
# =============================================================================

hint_mixed_values: list[int | str | None] = [
    100,
    "Python",
    None,
]

print(
    hint_mixed_values
)


# =============================================================================
# 37. Type Hint for a Constant
# =============================================================================

HINT_MAX_RETRIES: int = 3

print(
    HINT_MAX_RETRIES
)


# Type annotations can also be used with constants.


# =============================================================================
# 38. Type Hints and Mutable Collections
# =============================================================================

hint_mutable_values: list[int] = [
    10,
    20,
]

hint_mutable_values.append(
    30
)

print(
    hint_mutable_values
)


# A type hint does not make a mutable object immutable.


# =============================================================================
# 39. Type Hints and Immutable Collections
# =============================================================================

hint_immutable_values: tuple[int, ...] = (
    10,
    20,
    30,
)

print(
    hint_immutable_values
)


# The tuple's immutability comes from the tuple object itself,
# not from the type annotation.


# =============================================================================
# 40. Type Hints for Nested Functions
# =============================================================================

def calculate_average(
    values: list[float],
) -> float:
    return sum(values) / len(values)


hint_average_result: float = calculate_average(
    [
        10.0,
        20.0,
        30.0,
    ]
)

print(
    hint_average_result
)


# =============================================================================
# 41. Type Hints for Empty Collections
# =============================================================================

hint_empty_numbers: list[int] = []

hint_empty_records: dict[str, int] = {}

hint_empty_names: set[str] = set()

print(
    hint_empty_numbers
)

print(
    hint_empty_records
)

print(
    hint_empty_names
)


# Annotations are particularly useful for empty collections because
# the intended element types cannot be inferred from existing values.


# =============================================================================
# 42. Type Hinting a Variable Before Assignment
# =============================================================================

hint_future_value: int

hint_future_value = 100

print(
    hint_future_value
)


# This separates annotation from assignment.


# =============================================================================
# 43. Multiple Variable Annotations
# =============================================================================

hint_first_count: int = 10
hint_second_count: int = 20
hint_third_count: int = 30

print(
    hint_first_count,
    hint_second_count,
    hint_third_count,
)


# =============================================================================
# 44. Type Hints and Default Values
# =============================================================================

DEFAULT_BATCH_SIZE: int = 100


def process_batch(
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> int:
    return batch_size


hint_default_batch: int = process_batch()

hint_custom_batch: int = process_batch(
    500
)

print(
    hint_default_batch
)

print(
    hint_custom_batch
)


# The annotation describes the parameter type.
#
# The default value supplies the value used when no argument is provided.


# =============================================================================
# 45. Type Hints Do Not Change Python's Dynamic Nature
# =============================================================================

dynamic_hint_value: int = 100

print(
    dynamic_hint_value
)


# Python remains dynamically typed.
#
# Type hints add information for humans and development tools.


# =============================================================================
# 46. Static Type Checking
# =============================================================================

"""
Tools such as:

    Pyright
    Pylance
    mypy

can inspect type annotations and report possible inconsistencies.

Example:

    expected_count: int = 100

    expected_count = "Python"

A static type checker may report this as a type problem.

Python itself does not automatically stop the assignment merely because
the variable was annotated as int.
"""


# =============================================================================
# 47. Type Hints vs Runtime Types
# =============================================================================

"""
Important distinction:

    Type annotation
        ↓
    Developer / static-analysis information


    Runtime type
        ↓
    Actual type of the object currently referenced


Example:

    value: int = 100

The annotation says:

    value is intended to refer to int.


At runtime:

    100

is an int object.

The concepts are related but not identical.
"""


# =============================================================================
# 48. Type Hints Do Not Create Objects
# =============================================================================

hint_annotation_only: int

print(
    "Annotation exists without assigning a value."
)


# An annotation without an assignment does not create a new value object.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Type hints describe intended types.

✓ Variable annotation:

      name: str = "Alex"

✓ Function parameter annotation:

      def greet(name: str) -> str:

✓ Return annotation:

      -> str

✓ None return annotation:

      -> None

✓ Collection annotations:

      list[int]
      tuple[str, int]
      set[str]
      frozenset[int]
      dict[str, float]

✓ Variable-length tuple:

      tuple[int, ...]

✓ Union:

      int | str

✓ Optional value:

      str | None

✓ Any:

      Any

✓ Type aliases can simplify complicated annotations.

✓ Callable can describe function signatures.

✓ Type hints do not automatically convert values.

✓ Type hints do not normally enforce runtime types.

✓ Runtime checking is a separate concept.

✓ Static analysis tools such as Pyright and mypy can use annotations.

✓ Annotations improve:

      readability
      documentation
      IDE assistance
      static analysis
      maintainability

Core distinction:

    TYPE ANNOTATION
          ↓
    intended type information

    RUNTIME TYPE
          ↓
    actual type of the object

    RUNTIME TYPE CHECKING
          ↓
    type() / isinstance()

These are separate concepts.
"""