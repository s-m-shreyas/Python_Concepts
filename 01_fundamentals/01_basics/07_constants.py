"""
==============================================================================
Python Basics
==============================================================================

File
----
06_constants.py

Topic
-----
Constants

Overview
--------
A constant is a value that is intended to remain unchanged during
the execution of a program.

Python does not provide a dedicated constant keyword.

Instead, Python programmers follow naming conventions to indicate that
a variable should be treated as a constant.

This file covers:

    - What is a constant?
    - Constant naming convention
    - Module-level constants
    - Multiple constants
    - Constants used in calculations
    - Constants used in functions
    - Constants inside classes
    - Constant naming with multiple words
    - Constants are conventions in Python
    - Difference between constants and immutable objects
"""


# =============================================================================
# 01. Basic Constant
# =============================================================================

PI_VALUE: float = 3.141592653589793

print(
    PI_VALUE
)


# By convention, constants are written using uppercase letters.


# =============================================================================
# 02. Constant Naming
# =============================================================================

MAX_USERS: int = 100

MIN_PASSWORD_LENGTH: int = 8

DEFAULT_TIMEOUT: int = 30

print(
    MAX_USERS
)

print(
    MIN_PASSWORD_LENGTH
)

print(
    DEFAULT_TIMEOUT
)


# =============================================================================
# 03. Multiple-Word Constant
# =============================================================================

APPLICATION_NAME: str = "Data Pipeline"

DATABASE_PORT: int = 5432

MAX_RETRY_COUNT: int = 3

print(
    APPLICATION_NAME
)

print(
    DATABASE_PORT
)

print(
    MAX_RETRY_COUNT
)


# Constants with multiple words use uppercase letters
# separated by underscores.


# =============================================================================
# 04. Boolean Constants
# =============================================================================

DEBUG_MODE: bool = False

ENABLE_LOGGING: bool = True

print(
    DEBUG_MODE
)

print(
    ENABLE_LOGGING
)


# =============================================================================
# 05. String Constant
# =============================================================================

DEFAULT_LANGUAGE: str = "Python"

print(
    DEFAULT_LANGUAGE
)


# =============================================================================
# 06. Constants Used in Calculations
# =============================================================================

TAX_RATE: float = 0.18

PRODUCT_PRICE: float = 1000.0

TAX_AMOUNT: float = (
    PRODUCT_PRICE
    * TAX_RATE
)

FINAL_PRICE: float = (
    PRODUCT_PRICE
    + TAX_AMOUNT
)

print(
    f"Tax: {TAX_AMOUNT!r}"
)

print(
    f"Final price: {FINAL_PRICE!r}"
)


# Constants can be used as fixed configuration values
# throughout a program.


# =============================================================================
# 07. Mathematical Constant
# =============================================================================

GRAVITY_ACCELERATION: float = 9.81

OBJECT_MASS: float = 10.0

WEIGHT_FORCE: float = (
    OBJECT_MASS
    * GRAVITY_ACCELERATION
)

print(
    f"Weight: {WEIGHT_FORCE!r}"
)


# =============================================================================
# 08. Constant Used in a Function
# =============================================================================

DEFAULT_DISCOUNT_RATE: float = 0.10


def calculate_discount(
    original_price: float,
) -> float:
    return (
        original_price
        * DEFAULT_DISCOUNT_RATE
    )


discount_result: float = calculate_discount(
    1000.0
)

print(
    f"Discount: {discount_result!r}"
)


# A module-level constant can be accessed by functions in the module.


# =============================================================================
# 09. Multiple Constants Used Together
# =============================================================================

BASE_SALARY: float = 50000.0

BONUS_RATE: float = 0.10

BONUS_AMOUNT: float = (
    BASE_SALARY
    * BONUS_RATE
)

TOTAL_COMPENSATION: float = (
    BASE_SALARY
    + BONUS_AMOUNT
)

print(
    f"Bonus: {BONUS_AMOUNT!r}"
)

print(
    f"Total: {TOTAL_COMPENSATION!r}"
)





# =============================================================================
# 11. Convention vs Enforcement
# =============================================================================

CONVENTIONAL_CONSTANT: str = "Python"

print(
    CONVENTIONAL_CONSTANT
)

CONVENTIONAL_CONSTANT  = "SQL"  # pyright: ignore[reportConstantRedefinition]

print(
    CONVENTIONAL_CONSTANT
)


"""
Python does not stop the reassignment.

Therefore:

    CONSTANT_NAME = value

means:

    "Please treat this as a constant."

It does not mean:

    "Python will prevent reassignment."
"""


# =============================================================================
# 12. Constants Are Usually Defined at Module Level
# =============================================================================

APPLICATION_VERSION: str = "1.0.0"

MAX_CONNECTIONS: int = 10

CACHE_TIMEOUT_SECONDS: int = 300

print(
    APPLICATION_VERSION
)

print(
    MAX_CONNECTIONS
)

print(
    CACHE_TIMEOUT_SECONDS
)


# Module-level constants are available throughout the module.


# =============================================================================
# 13. Constant Inside a Class
# =============================================================================

class ApplicationConfig:
    """
    Store application-level configuration values.
    """

    DEFAULT_PORT: int = 8080
    DEFAULT_HOST: str = "localhost"


print(
    ApplicationConfig.DEFAULT_PORT
)

print(
    ApplicationConfig.DEFAULT_HOST
)


# Uppercase class attributes can also represent constants by convention.


# =============================================================================
# 14. Class Constants Accessed Through an Instance
# =============================================================================

class ServerConfig:
    """
    Store server configuration.
    """

    SERVER_PORT: int = 8000


server_config_instance: ServerConfig = ServerConfig()

print(
    server_config_instance.SERVER_PORT
)


# The class attribute can be accessed through an instance,
# although class-level access is generally clearer for constants.


# =============================================================================
# 15. Constant Tuple
# =============================================================================

SUPPORTED_DATABASES: tuple[str, ...] = (
    "PostgreSQL",
    "MySQL",
    "Oracle",
)

print(
    SUPPORTED_DATABASES
)


# The uppercase naming communicates that the collection
# is intended to remain unchanged.


# =============================================================================
# 16. Constant Set
# =============================================================================

SUPPORTED_FORMATS: frozenset[str] = frozenset(
    {
        "CSV",
        "JSON",
        "XML",
    }
)

print(
    SUPPORTED_FORMATS
)


# An immutable collection can be useful when the collection itself
# should not be modified.


# =============================================================================
# 17. Constant Dictionary
# =============================================================================

HTTP_STATUS_CODES: dict[str, int] = {
    "OK": 200,
    "NOT_FOUND": 404,
    "SERVER_ERROR": 500,
}

print(
    HTTP_STATUS_CODES
)


# The uppercase name communicates intended constant usage.
#
# However, the dictionary itself is still mutable.


# =============================================================================
# 18. Constant and Mutability
# =============================================================================

CONSTANT_LIST: list[str] = [
    "Python",
    "SQL",
]

print(
    CONSTANT_LIST
)

CONSTANT_LIST.append(
    "Airflow"
)

print(
    CONSTANT_LIST
)


# Important:
#
# The uppercase naming convention does not make an object immutable.
#
# CONSTANT_LIST is still a mutable list.


# =============================================================================
# 19. Constant Name vs Immutable Object
# =============================================================================

CONSTANT_TEXT: str = "Python"

print(
    CONSTANT_TEXT
)




# The name can still be rebound.
#
# String immutability does not make the variable name constant.


# =============================================================================
# 20. Constants and Configuration
# =============================================================================

API_BASE_URL: str = "https://example.com"

API_TIMEOUT_SECONDS: int = 30

API_MAX_RETRIES: int = 3

print(
    f"URL: {API_BASE_URL}"
)

print(
    f"Timeout: {API_TIMEOUT_SECONDS}"
)

print(
    f"Retries: {API_MAX_RETRIES}"
)


# Constants are commonly used for configuration values.


# =============================================================================
# 21. Constant Used as a Default
# =============================================================================

DEFAULT_PAGE_SIZE: int = 25


def get_page_size() -> int:
    return DEFAULT_PAGE_SIZE


page_size_result: int = get_page_size()

print(
    page_size_result
)


# Constants can centralize values that are reused throughout a program.


# =============================================================================
# 22. Constants Reduce Magic Numbers
# =============================================================================

MAGIC_NUMBER_EXAMPLE: int = 60


def is_passing_score(
    student_score: int,
) -> bool:
    return student_score >= MAGIC_NUMBER_EXAMPLE


print(
    is_passing_score(75)
)

print(
    is_passing_score(45)
)


# A named constant makes the meaning of the value clearer.


# =============================================================================
# 23. Avoiding Magic Values
# =============================================================================

PASSING_SCORE: int = 60


def evaluate_score(
    exam_score: int,
) -> str:
    if exam_score >= PASSING_SCORE:
        return "Pass"

    return "Fail"


print(
    evaluate_score(80)
)

print(
    evaluate_score(50)
)


# Named constants make code easier to understand and maintain.


# =============================================================================
# 24. Constant Naming Convention
# =============================================================================

"""
Recommended convention:

    CONSTANT_NAME

Examples:

    MAX_USERS
    DEFAULT_TIMEOUT
    DATABASE_PORT
    API_BASE_URL
    TAX_RATE
    MIN_PASSWORD_LENGTH


Avoid:

    max_users
    defaultTimeout
    DatabasePort

when the value is intended to be a constant.
"""


# =============================================================================
# 25. Constants Are Not Read-Only Variables
# =============================================================================

READ_ONLY_STYLE_VALUE: int = 100

print(
    READ_ONLY_STYLE_VALUE
)




# Python has no built-in read-only variable keyword.


# =============================================================================
# 26. Constant Concept
# =============================================================================

"""
A useful mental model:

    CONSTANT

        =
    
    normal Python variable
        +
    uppercase naming convention
        +
    programmer intention


It does NOT mean:

    Python-enforced immutability
"""


# =============================================================================
# 27. Constant vs Immutable Object
# =============================================================================

CONSTANT_CONCEPT_VALUE: tuple[int, ...] = (
    10,
    20,
    30,
)

print(
    CONSTANT_CONCEPT_VALUE
)


"""
Two different concepts:

    Constant
        ↓
    The name is intended not to be reassigned.

    Immutable object
        ↓
    The object itself cannot be changed after creation.

A constant can refer to a mutable object.

An immutable object can be referenced by a non-constant name.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Python does not have a dedicated `const` keyword.

✓ Constants are represented by convention.

✓ The standard naming convention is:

      UPPERCASE_WITH_UNDERSCORES

✓ Common examples:

      MAX_USERS
      DEFAULT_TIMEOUT
      DATABASE_PORT
      TAX_RATE

✓ Constants are commonly defined at module level.

✓ Constants can also exist as class attributes.

✓ Constants can improve readability.

✓ Constants can replace unexplained magic numbers.

✓ Python does NOT prevent reassignment:

      MAX_USERS = 100
      MAX_USERS = 200

✓ Uppercase naming communicates programmer intention.

✓ Uppercase naming does NOT make an object immutable.

✓ A constant may refer to a mutable object:

      CONSTANT_LIST = []

✓ Immutability and constant naming are different concepts.

Core distinction:

    CONSTANT
        ↓
    "Do not intentionally reassign this name."

    IMMUTABLE OBJECT
        ↓
    "This object cannot be modified."

    PYTHON
        ↓
    Does not enforce the constant convention.
"""