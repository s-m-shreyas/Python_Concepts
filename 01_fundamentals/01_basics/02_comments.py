"""
==============================================================================
Python Basics
==============================================================================

File
----
02_comments.py

Topic
-----
Comments

Overview
--------
Comments are notes written inside source code for humans.

Python ignores comments during normal program execution.

This file covers:

    - Single-line comments
    - Comments after code
    - Multiple comments
    - Commenting out code
    - Multi-line explanatory comments
    - Docstrings
    - Module docstrings
    - Function docstrings
    - Class docstrings
    - Comments vs docstrings
"""


# =============================================================================
# 01. Basic Comment
# =============================================================================

# This is a comment.

print("Python")


# Everything after # on the line is treated as a comment.


# =============================================================================
# 02. Comment Before Code
# =============================================================================

# Display a greeting.
print("Hello, Python")


# Comments can explain what the following statement does.


# =============================================================================
# 03. Comment After Code
# =============================================================================

print("Hello")  # Display a greeting.


# A comment can appear after executable code.


# =============================================================================
# 04. Multiple Comments
# =============================================================================

# Python is a programming language.
# Python supports multiple programming paradigms.
# Python has dynamic typing.

print("Python")


# Each line beginning with # is a separate comment.


# =============================================================================
# 05. Commenting Out Code
# =============================================================================

commented_example_value: int = 100

# commented_example_value = 200

print(
    commented_example_value
)


# The second assignment is disabled because it is commented out.


# =============================================================================
# 06. Temporarily Commenting Code
# =============================================================================

temporary_first_value: int = 10
temporary_second_value: int = 20

# temporary_result_value: int = (
#     temporary_first_value
#     + temporary_second_value
# )

print(
    temporary_first_value
)

print(
    temporary_second_value
)


# Commenting code can temporarily disable a block during development.


# =============================================================================
# 07. Comments Do Not Affect Execution
# =============================================================================

execution_comment_value: int = 100

# This comment does not change the value.
# The next statement still uses the original value.

print(
    execution_comment_value
)


# =============================================================================
# 08. Comments Can Explain Why
# =============================================================================

temperature_value: int = 25

# Store the temperature in Celsius.
print(
    temperature_value
)


# Good comments can explain the purpose or reasoning behind code.


# =============================================================================
# 09. Comments Can Explain Non-Obvious Logic
# =============================================================================

total_amount: int = 100
discount_amount: int = 20

# Apply the discount before displaying the final amount.
final_amount: int = (
    total_amount
    - discount_amount
)

print(
    final_amount
)


# A useful comment explains something that may not be immediately obvious.


# =============================================================================
# 10. Comments Should Not Explain Obvious Code
# =============================================================================

user_name: str = "Alex"

print(
    user_name
)


# Avoid unnecessary comments such as:
#
#     user_name = "Alex"  # Assign Alex to user_name
#
# when the code is already self-explanatory.


# =============================================================================
# 11. Commenting a Block
# =============================================================================

block_first_value: int = 10
block_second_value: int = 20

# block_total_value: int = (
#     block_first_value
#     + block_second_value
# )
#
# print(
#     block_total_value
# )


# Each line of a commented block needs its own # marker.


# =============================================================================
# 12. Module Docstring
# =============================================================================

"""
The string at the beginning of this file is a module docstring.

It describes the purpose of the module.
"""


# The module docstring is different from an ordinary comment.


# =============================================================================
# 13. Function Docstring
# =============================================================================

def calculate_square(
    square_input_value: int,
) -> int:
    """
    Return the square of an integer.
    """
    return square_input_value ** 2


square_result_value: int = calculate_square(
    5
)

print(
    square_result_value
)


# A function docstring describes what the function does.


# =============================================================================
# 14. Class Docstring
# =============================================================================

class StudentRecord:
    """
    Represent a simple student record.
    """

    def __init__(
        self,
        student_name_value: str,
    ) -> None:
        self.student_name_value = student_name_value


student_record_object: StudentRecord = (
    StudentRecord(
        "Alex"
    )
)

print(
    student_record_object.student_name_value
)


# A class docstring describes the purpose of the class.


# =============================================================================
# 15. Docstrings Can Be Accessed
# =============================================================================

def generate_message(
    message_text_value: str,
) -> str:
    """
    Return the supplied message.
    """
    return message_text_value


print(
    generate_message.__doc__
)


# Function docstrings are stored as metadata and can be accessed through
# the __doc__ attribute.


# =============================================================================
# 16. Comment vs Docstring
# =============================================================================

# This is a comment.


def comment_vs_docstring_example() -> None:
    """
    This is a docstring.
    """
    print("Example")


comment_vs_docstring_example()


# Comment:
#
#     Intended mainly for source-code explanation.
#
# Docstring:
#
#     Documentation associated with a module, function, class,
#     or other supported Python object.


# =============================================================================
# 17. Documentation-Style Docstring
# =============================================================================

def calculate_total_price(
    item_price_value: float,
    item_quantity_value: int,
) -> float:
    """
    Calculate the total price of an item.

    Parameters
    ----------
    item_price_value:
        Price of one item.

    item_quantity_value:
        Number of items.

    Returns
    -------
    float
        Total price.
    """
    return (
        item_price_value
        * item_quantity_value
    )


total_price_result: float = (
    calculate_total_price(
        25.5,
        3,
    )
)

print(
    total_price_result
)


# Docstrings can contain structured documentation.


# =============================================================================
# 18. Comments Inside Functions
# =============================================================================

def calculate_difference(
    minuend_value: int,
    subtrahend_value: int,
) -> int:
    # Subtract the second value from the first.
    return (
        minuend_value
        - subtrahend_value
    )


difference_result: int = calculate_difference(
    100,
    40,
)

print(
    difference_result
)


# Comments can appear anywhere Python allows a comment.


# =============================================================================
# 19. Comments With Type Annotations
# =============================================================================

annotated_comment_value: int = 100  # Integer value.


print(
    annotated_comment_value
)


# Comments do not change the annotation or runtime value.


# =============================================================================
# 20. Comments and Strings Are Different
# =============================================================================

string_comment_example: str = "# This is not a comment"

print(
    string_comment_example
)


# A # character inside a string is part of the string.
#
# It becomes a comment only when Python encounters it outside a string.


# =============================================================================
# 21. Comment After a String
# =============================================================================

comment_after_string: str = (
    "Python"
)  # This part is a comment.

print(
    comment_after_string
)


# The string and the comment are separate.


# =============================================================================
# 22. Comments Are Ignored by Python
# =============================================================================

ignored_comment_value: int = 50

# ignored_comment_value = 999

print(
    ignored_comment_value
)


# The commented assignment never executes.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A comment begins with #.

✓ Python ignores comments during normal execution.

✓ Comments can appear:

      before code

      after code

      between statements

✓ Comments can temporarily disable code.

✓ Good comments explain purpose, reasoning, or non-obvious behaviour.

✓ Avoid comments that merely repeat obvious code.

✓ A docstring is documentation associated with a Python object.

✓ Common docstring locations include:

      module
      function
      class

✓ Function docstrings can be accessed using:

      function_name.__doc__

✓ Comments and docstrings are different.

      # comment
          -> source-code comment

      '''
      documentation
      '''
          -> docstring when used in the appropriate position

✓ A # inside a string is not a comment.

Core distinction:

    COMMENT
        ↓
    Explain source code to developers.

    DOCSTRING
        ↓
    Document a Python object.

    CODE
        ↓
    Executed by Python.
"""