import keyword


"""
Variable Identifier Rules:

1 - The varibale name must not be a keyword.
2 - The variable must not start with any digit or number.
3 - The varibale name must not contain any space.
4 - The varibale name must not contain any special character except '_'.
5 - A variable is alphanumeric entity, that too starting with alphabet only.
"""


"""
A varibale name cannot be same as any element in the below list ->
Run the print statement to see the list.
"""
print(keyword.kwlist)

# Valid variable names.

"""
'str' is datatype of the object, that will be store to this variable inside memory.
This method is called type hinting or type annotation.
"""

some_var: str = ''
some_var_2: str = ''
some_var_3, some_var_4 = '', ''

"""
==============================================================================
Python Basics
==============================================================================

File
----
01_hello_world.py

Topic
-----
Hello World

Overview
--------
This file introduces the simplest Python program:

    print("Hello, World!")

It covers:

    - Python source code
    - Statements
    - String literals
    - The print() function
    - Program execution
    - Multiple statements
    - Basic output
"""


# =============================================================================
# 01. First Python Statement
# =============================================================================

print("Hello, World!")


# Python executes the statement from top to bottom.


# =============================================================================
# 02. Simple Text Output
# =============================================================================

print("Hello")

print("Python")


# Each print() statement produces output on a separate line.


# =============================================================================
# 03. Multiple Words
# =============================================================================

print("Hello Python")


# Text enclosed inside quotes is a string literal.


# =============================================================================
# 04. Different Quote Styles
# =============================================================================

print("Hello Python")

print('Hello Python')


# Both single and double quotes can be used for strings.


# =============================================================================
# 05. Output With Numbers
# =============================================================================

print(100)

print(25.5)


# Numbers do not need quotation marks when they are written as numeric literals.


# =============================================================================
# 06. Text and Numbers
# =============================================================================

print("Age:", 30)

print("Score:", 95)


# print() can display multiple values.


# =============================================================================
# 07. Multiple Values
# =============================================================================

print(
    "Python",
    "SQL",
    "ETL",
)


# By default, print() separates multiple arguments with a space.


# =============================================================================
# 08. Empty print()
# =============================================================================

print()

print("After empty line")


# print() without arguments produces a blank line.


# =============================================================================
# 09. Printing Expressions
# =============================================================================

print(10 + 20)

print(100 - 25)

print(10 * 5)


# Python evaluates the expressions before displaying their results.


# =============================================================================
# 10. Printing Variables
# =============================================================================

hello_user_name: str = "Alex"

print(hello_user_name)


# print() can display the value referenced by a variable.


# =============================================================================
# 11. Text With a Variable
# =============================================================================

hello_person_name: str = "Alex"

print("Hello", hello_person_name)


# =============================================================================
# 12. Formatted Output
# =============================================================================

formatted_person_name: str = "Alex"
formatted_person_age: int = 30

print(
    f"Name: {formatted_person_name}"
)

print(
    f"Age: {formatted_person_age}"
)


# f-strings allow expressions and variables to be embedded inside strings.


# =============================================================================
# 13. Basic Program Flow
# =============================================================================

print("Program started")

print("Processing")

print("Program finished")


# Python normally executes statements from top to bottom.


# =============================================================================
# 14. Statement Per Line
# =============================================================================

first_message: str = "First"
second_message: str = "Second"
third_message: str = "Third"

print(first_message)
print(second_message)
print(third_message)


# Each statement is executed in sequence.


# =============================================================================
# 15. Hello World With a Function
# =============================================================================

def display_hello_world() -> None:
    print("Hello, World!")


display_hello_world()


# A function groups reusable instructions.
#
# Functions are covered in greater detail later.


# =============================================================================
# 16. Special Characters
# =============================================================================

print("Hello\nPython")

print("Python\tSQL")


# \n -> new line
# \t -> tab


# =============================================================================
# 17. Quotes Inside Text
# =============================================================================

print('Python is called "Python".')

print("Python's syntax is readable.")


# Different quote styles can be useful when the text itself contains quotes.


# =============================================================================
# 18. Basic Unicode Output
# =============================================================================

print("Python 🐍")

print("Hello 世界")


# Python source code supports Unicode text.


# =============================================================================
# 19. Simple Complete Program
# =============================================================================

program_language: str = "Python"
program_creator: str = "Guido van Rossum"

print(
    f"Language: {program_language}"
)

print(
    f"Creator: {program_creator}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Python programs consist of executable statements.

✓ Python normally executes statements from top to bottom.

✓ print() displays output.

✓ Text is written using string literals:

      "Hello"

      'Hello'

✓ Numeric literals can be printed directly:

      print(100)

✓ print() can accept multiple values:

      print("Age:", 30)

✓ print() separates multiple arguments with spaces by default.

✓ print() without arguments produces a blank line.

✓ Expressions are evaluated before their results are printed:

      print(10 + 20)

✓ Variables can be printed:

      print(user_name)

✓ f-strings can combine text and variable values.

✓ Python supports Unicode text.

The fundamental pattern is:

    Python code
        ↓
    Python interpreter
        ↓
    Statement execution
        ↓
    Output
"""
