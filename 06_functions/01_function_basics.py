"""
==============================================================================
Python Functions
==============================================================================

File
----
01_function_basics.py

Topic
-----
Function Basics

Overview
--------
A function is a reusable block of code designed to perform a specific task.

Functions allow us to:

    - Organize code
    - Reuse logic
    - Reduce duplication
    - Improve readability
    - Separate responsibilities
    - Build larger programs from smaller components

This file introduces the fundamental structure and behaviour of functions.

Topics covered:

    - Function definition
    - def keyword
    - Function name
    - Function body
    - Function call
    - Function execution
    - Reusing a function
    - Functions without parameters
    - Functions with simple parameters
    - Function return values
    - Function calls inside expressions
    - Function execution order
    - Function objects
    - Calling functions multiple times

Parameter-specific concepts are covered in later files.
"""


# =============================================================================
# 01. Basic Function Definition
# =============================================================================

def display_welcome() -> None:
    """
    Display a welcome message.
    """
    print(
        "Welcome to Python functions!"
    )


# A function is defined using the `def` keyword.
#
# Structure:
#
#     def function_name():
#         function body
#
# Defining a function does not execute its body.


# =============================================================================
# 02. Calling a Function
# =============================================================================

display_welcome()


# Parentheses are used to call the function.
#
# The function body executes when the function is called.


# =============================================================================
# 03. Defining a Function Before Calling It
# =============================================================================

def show_python_message() -> None:
    """
    Display a message about Python.
    """
    print(
        "Python is a general-purpose programming language."
    )


show_python_message()


# Python executes the program from top to bottom.
#
# The function must normally be defined before the point where
# the function is called during execution.


# =============================================================================
# 04. Function Can Be Called More Than Once
# =============================================================================

def display_separator() -> None:
    """
    Display a separator line.
    """
    print(
        "-" * 40
    )


display_separator()
display_separator()
display_separator()


# The same function can be reused multiple times.


# =============================================================================
# 05. Function With Multiple Statements
# =============================================================================

def display_profile() -> None:
    """
    Display multiple pieces of information.
    """
    print(
        "Name: Alex"
    )

    print(
        "Role: Data Engineer"
    )

    print(
        "Language: Python"
    )


display_profile()


# A function body can contain multiple statements.
#
# All statements belonging to the function must be indented.


# =============================================================================
# 06. Function Execution Happens When Called
# =============================================================================

def display_execution_message() -> None:
    """
    Display a message when the function executes.
    """
    print(
        "The function body is now executing."
    )


print(
    "Before function call."
)

display_execution_message()

print(
    "After function call."
)


# This demonstrates the execution sequence:
#
#     Before function call
#             ↓
#     Function call
#             ↓
#     Function body
#             ↓
#     After function call


# =============================================================================
# 07. Function Without a Return Statement
# =============================================================================

def display_status() -> None:
    """
    Display a status message.
    """
    print(
        "System status: Ready"
    )


display_status()


# A function does not need to explicitly contain a return statement.
#
# Such a function commonly performs an action rather than producing
# a result for the caller.


# =============================================================================
# 08. Function Returning a Value
# =============================================================================

def get_application_name() -> str:
    """
    Return the application name.
    """
    return "Python Learning Repository"


application_name_result: str = get_application_name()

print(
    application_name_result
)


# `return` sends a value back to the code that called the function.


# =============================================================================
# 09. Using a Returned Value in an Expression
# =============================================================================

def get_base_number() -> int:
    """
    Return a base number.
    """
    return 25


base_number_result: int = get_base_number()

doubled_base_number: int = base_number_result * 2

print(
    doubled_base_number
)


# A returned value can be stored in a variable and used in later expressions.


# =============================================================================
# 10. Directly Using a Returned Value
# =============================================================================

def get_message_length() -> int:
    """
    Return the length of a fixed message.
    """
    message_text: str = "Python"

    return len(
        message_text
    )


print(
    get_message_length()
)


# A function call that returns a value can be used directly
# wherever an expression is allowed.


# =============================================================================
# 11. Function With a Parameter
# =============================================================================

def display_language(
    language_name: str,
) -> None:
    """
    Display the supplied language name.
    """
    print(
        f"Language: {language_name}"
    )


display_language(
    "Python"
)


# A parameter allows a function to receive information from its caller.
#
# Detailed parameter and argument behaviour is covered in later files.


# =============================================================================
# 12. Reusing a Parameterized Function
# =============================================================================

display_language(
    "SQL"
)

display_language(
    "Java"
)

display_language(
    "C++"
)


# The same function can operate on different values.


# =============================================================================
# 13. Function Performing a Calculation
# =============================================================================

def calculate_square_value(
    number_value: int,
) -> int:
    """
    Return the square of an integer.
    """
    return number_value * number_value


square_result_value: int = calculate_square_value(
    12
)

print(
    square_result_value
)


# Functions are useful for encapsulating reusable calculations.


# =============================================================================
# 14. Function Returning a Boolean
# =============================================================================

def is_even_number(
    candidate_number: int,
) -> bool:
    """
    Return True when the supplied number is even.
    """
    return candidate_number % 2 == 0


even_number_result: bool = is_even_number(
    24
)

print(
    even_number_result
)


# The return annotation describes the intended type of the result.


# =============================================================================
# 15. Function Returning a String
# =============================================================================

def build_greeting(
    person_name: str,
) -> str:
    """
    Build and return a greeting message.
    """
    return f"Hello, {person_name}!"


greeting_message_result: str = build_greeting(
    "Sam"
)

print(
    greeting_message_result
)


# =============================================================================
# 16. Function Calls Can Be Nested
# =============================================================================

def get_uppercase_text() -> str:
    """
    Return an uppercase text value.
    """
    return "python"


def display_uppercase_text() -> None:
    """
    Display the uppercase text returned by another function.
    """
    print(
        get_uppercase_text().upper()
    )


display_uppercase_text()


# A function can call another function.
#
# This allows larger operations to be divided into smaller responsibilities.


# =============================================================================
# 17. Function Calls Can Be Used as Arguments
# =============================================================================

def get_reference_value() -> int:
    """
    Return a reference integer.
    """
    return 50


def display_numeric_value(
    numeric_value: int,
) -> None:
    """
    Display an integer value.
    """
    print(
        numeric_value
    )


display_numeric_value(
    get_reference_value()
)


# The returned value from one function becomes the argument
# supplied to another function.


# =============================================================================
# 18. Function Execution Order
# =============================================================================

def first_operation() -> None:
    """
    Display the first operation.
    """
    print(
        "First operation"
    )


def second_operation() -> None:
    """
    Display the second operation.
    """
    print(
        "Second operation"
    )


def third_operation() -> None:
    """
    Display the third operation.
    """
    print(
        "Third operation"
    )


first_operation()
second_operation()
third_operation()


# The calls determine the execution order.
#
# The order of function definitions does not determine the order
# in which their bodies execute.


# =============================================================================
# 19. Function Can Be Stored in a Variable
# =============================================================================

def display_repository_message() -> None:
    """
    Display a repository message.
    """
    print(
        "Learning Python step by step."
    )


repository_message_function = display_repository_message

repository_message_function()


# Functions are objects in Python.
#
# A function can therefore be referenced by another variable.
#
# Advanced first-class function behaviour is covered later.


# =============================================================================
# 20. Function Object vs Function Call
# =============================================================================

def display_function_reference() -> None:
    """
    Display a function reference message.
    """
    print(
        "This function demonstrates function references."
    )


function_reference_value = display_function_reference

print(
    function_reference_value
)

function_reference_value()


# Without parentheses:
#
#     display_function_reference
#
# we refer to the function object.
#
# With parentheses:
#
#     display_function_reference()
#
# we call the function.


# =============================================================================
# 21. Functions Can Be Used to Separate Responsibilities
# =============================================================================

def display_application_header() -> None:
    """
    Display an application header.
    """
    print(
        "=" * 40
    )

    print(
        "DATA PROCESSING APPLICATION"
    )

    print(
        "=" * 40
    )


def display_application_status() -> None:
    """
    Display application status.
    """
    print(
        "Status: Running"
    )


display_application_header()
display_application_status()


# Separating responsibilities into functions makes code easier to understand.


# =============================================================================
# 22. Small Functions
# =============================================================================

def get_supported_language() -> str:
    """
    Return the primary supported language.
    """
    return "Python"


supported_language_result: str = get_supported_language()

print(
    supported_language_result
)


# A function can be very small.
#
# Small functions are not automatically bad.
#
# The important question is whether the function has a clear purpose.


# =============================================================================
# 23. Function With a Single Responsibility
# =============================================================================

def calculate_total_price(
    item_price: float,
) -> float:
    """
    Return the supplied item price.
    """
    return item_price


product_price_result: float = calculate_total_price(
    1499.50
)

print(
    product_price_result
)


# A function should generally have a clear and understandable responsibility.


# =============================================================================
# 24. Function Return Value Can Be Assigned
# =============================================================================

def get_record_count() -> int:
    """
    Return a sample record count.
    """
    return 250


record_count_result: int = get_record_count()

print(
    record_count_result
)


# The caller decides what to do with the returned value.


# =============================================================================
# 25. Function Return Value Can Be Ignored
# =============================================================================

def get_processing_status() -> str:
    """
    Return a processing status.
    """
    return "Completed"


get_processing_status()


# Python allows a returned value to be ignored when the caller
# does not need the result.


# =============================================================================
# 26. Functions Can Be Called From Other Functions
# =============================================================================

def get_system_name() -> str:
    """
    Return the system name.
    """
    return "Data Pipeline"


def display_system_information() -> None:
    """
    Display system information.
    """
    system_name_result: str = get_system_name()

    print(
        f"System: {system_name_result}"
    )


display_system_information()


# Functions can be composed together to build larger operations.


# =============================================================================
# 27. Function Calls and Return Flow
# =============================================================================

def get_initial_value() -> int:
    """
    Return an initial value.
    """
    return 10


def increase_value(
    original_value: int,
) -> int:
    """
    Increase the supplied value.
    """
    return original_value + 5


initial_value_result: int = get_initial_value()

updated_value_result: int = increase_value(
    initial_value_result
)

print(
    updated_value_result
)


# Conceptually:
#
#     get_initial_value()
#             ↓
#          10
#             ↓
#     increase_value(10)
#             ↓
#          15


# =============================================================================
# 28. Function Definition Does Not Mean Immediate Execution
# =============================================================================

def delayed_execution_example() -> None:
    """
    Display a message when eventually called.
    """
    print(
        "This message appears only when the function is called."
    )


print(
    "Function has been defined."
)

print(
    "Function has not executed yet."
)

delayed_execution_example()


# Defining the function creates the function object.
#
# Calling the function executes its body.


# =============================================================================
# 29. Function Names Should Describe Their Purpose
# =============================================================================

def calculate_average_value(
    first_score: float,
    second_score: float,
) -> float:
    """
    Return the average of two scores.
    """
    return (
        first_score
        + second_score
    ) / 2


average_score_result: float = calculate_average_value(
    80.0,
    90.0,
)

print(
    average_score_result
)


# Good function names communicate what the function does.


# =============================================================================
# 30. Function Naming Convention
# =============================================================================

def process_customer_record() -> None:
    """
    Demonstrate standard Python function naming.
    """
    print(
        "Processing customer record."
    )


process_customer_record()


# Python conventionally uses snake_case for function names.
#
# Examples:
#
#     calculate_total()
#     process_data()
#     get_user_name()
#     display_result()


# =============================================================================
# 31. Function Documentation
# =============================================================================

def calculate_cube_value(
    cube_input: int,
) -> int:
    """
    Return the cube of an integer.
    """
    return cube_input ** 3


cube_result_value: int = calculate_cube_value(
    5
)

print(
    cube_result_value
)


# Docstrings provide documentation for functions.
#
# More detailed docstring conventions are covered separately.


# =============================================================================
# 32. Function Basics Summary
# =============================================================================

"""
Basic function flow:

    1. Define the function
            ↓
    2. Give it a name
            ↓
    3. Write the function body
            ↓
    4. Call the function
            ↓
    5. Function body executes
            ↓
    6. Function may return a value


Basic syntax:

    def function_name():
        statements


Function with a parameter:

    def function_name(value: int) -> None:
        statements


Function with a return value:

    def function_name(value: int) -> int:
        return value


Important distinction:

    Function definition
        ↓
    Creates the function object


    Function call
        ↓
    Executes the function body
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Functions are reusable blocks of code.

✓ Functions are defined using the `def` keyword.

✓ Defining a function does not execute its body.

✓ Calling a function executes its body.

✓ Functions can be called multiple times.

✓ Functions can receive information through parameters.

✓ Functions can return values using `return`.

✓ A function can return None.

✓ Returned values can be stored in variables.

✓ Returned values can be used directly in expressions.

✓ Functions can call other functions.

✓ Functions are Python objects.

✓ A function reference and a function call are different:

      function_name
          ↓
      function object

      function_name()
          ↓
      function call

✓ Functions should generally have clear responsibilities.

✓ Function names conventionally use snake_case.

✓ Type annotations improve readability and static analysis.

✓ Docstrings provide documentation.

Core idea:

    Define
      ↓
    Call
      ↓
    Execute
      ↓
    Return
      ↓
    Reuse
"""