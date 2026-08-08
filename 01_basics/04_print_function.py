"""
==============================================================================
Python Basics
==============================================================================

File
----
03_print_function.py

Topic
-----
print() Function

Overview
--------
The print() function displays values on standard output.

This file covers:

    - Basic print()
    - Printing different data types
    - Multiple arguments
    - sep
    - end
    - New lines
    - Tabs
    - Printing expressions
    - Printing variables
    - flush
    - file
    - Return value of print()
"""


# =============================================================================
# 01. Basic print()
# =============================================================================

print("Hello, Python")


# print() displays the supplied value.


# =============================================================================
# 02. Printing Text
# =============================================================================

print("Python")
print("SQL")
print("Data Engineering")


# =============================================================================
# 03. Printing Integers
# =============================================================================

print(100)
print(250)
print(-50)


# =============================================================================
# 04. Printing Floating-Point Values
# =============================================================================

print(25.5)
print(3.14)
print(-10.75)


# =============================================================================
# 05. Printing Boolean Values
# =============================================================================

print(True)
print(False)


# =============================================================================
# 06. Printing None
# =============================================================================

print(None)


# print() can display None as output.


# =============================================================================
# 07. Printing Collections
# =============================================================================

print([10, 20, 30])

print((10, 20, 30))

print({10, 20, 30})

print(
    {
        "Python": 100,
        "SQL": 90,
    }
)


# =============================================================================
# 08. Printing Multiple Arguments
# =============================================================================

print(
    "Name:",
    "Alex",
)

print(
    "Age:",
    30,
)

print(
    "Score:",
    95,
)


# Multiple arguments are separated by a space by default.


# =============================================================================
# 09. Default sep
# =============================================================================

print(
    "Python",
    "SQL",
    "ETL",
)


# Default:
#
#     sep = " "


# =============================================================================
# 10. Custom sep
# =============================================================================

print(
    "2026",
    "08",
    "08",
    sep="-",
)


# =============================================================================
# 11. Another sep Example
# =============================================================================

print(
    "Python",
    "SQL",
    "Airflow",
    sep=" | ",
)


# =============================================================================
# 12. Empty sep
# =============================================================================

print(
    "Python",
    "SQL",
    "ETL",
    sep="",
)


# sep controls what is placed between arguments.


# =============================================================================
# 13. Default end
# =============================================================================

print("Hello")
print("Python")


# Default:
#
#     end = "\n"
#
# Therefore each print() normally moves to the next line.


# =============================================================================
# 14. Custom end
# =============================================================================

print(
    "Hello",
    end=" ",
)

print(
    "Python"
)


# The first print() does not create a new line.


# =============================================================================
# 15. Custom end With Separator
# =============================================================================

print(
    "Loading",
    end="..."
)

print(
    "Done"
)


# =============================================================================
# 16. Empty end
# =============================================================================

print(
    "Python",
    end="",
)

print(
    " continues"
)


# =============================================================================
# 17. New Line Character
# =============================================================================

print(
    "Hello\nPython"
)


# \n represents a new line.


# =============================================================================
# 18. Tab Character
# =============================================================================

print(
    "Python\tSQL"
)


# \t represents a tab.


# =============================================================================
# 19. Multiple New Lines
# =============================================================================

print(
    "First\nSecond\nThird"
)


# =============================================================================
# 20. sep and end Together
# =============================================================================

print(
    "2026",
    "08",
    "08",
    sep="/",
    end=" -> ",
)

print(
    "Today"
)


# sep controls the space between arguments.
#
# end controls what comes after the final argument.


# =============================================================================
# 21. Printing Expressions
# =============================================================================

print(
    10 + 20
)

print(
    100 - 25
)

print(
    10 * 5
)

print(
    100 / 4
)


# Expressions are evaluated before print() displays the result.


# =============================================================================
# 22. Printing Variables
# =============================================================================

print_user_name: str = "Alex"

print(
    print_user_name
)


# =============================================================================
# 23. Printing Multiple Variables
# =============================================================================

print_first_name: str = "Alex"
print_last_name: str = "Smith"

print(
    print_first_name,
    print_last_name,
)


# =============================================================================
# 24. Printing With Labels
# =============================================================================

print_user_age: int = 30

print(
    "Age:",
    print_user_age,
)


# =============================================================================
# 25. Printing an Empty Line
# =============================================================================

print(
    "Before"
)

print()

print(
    "After"
)


# print() with no arguments produces a blank line.


# =============================================================================
# 26. Printing repr() Representation
# =============================================================================

print_repr_text: str = "Python\nSQL"

print(
    print_repr_text
)

print(
    repr(print_repr_text)
)


# repr() displays an escaped representation of the string.


# =============================================================================
# 27. Using !r With print Formatting
# =============================================================================

print_format_text: str = "Python\nSQL"

print(
    f"Value: {print_format_text!r}"
)


# !r requests the repr representation inside an f-string.


# =============================================================================
# 28. Printing Different Values Together
# =============================================================================

print_value_name: str = "Alex"
print_value_age: int = 30
print_value_score: float = 95.5

print(
    print_value_name,
    print_value_age,
    print_value_score,
)


# =============================================================================
# 29. print() Return Value
# =============================================================================

print_return_result: None = print(
    "Hello"
)

print(
    f"Return value: {print_return_result!r}"
)


# print() returns None.


# =============================================================================
# 30. Assignment From print()
# =============================================================================

print_assignment_result: None = print(
    "Python"
)

print(
    print_assignment_result is None
)


# print() is used for output, not for producing a useful return value.


# =============================================================================
# 31. Nested print()
# =============================================================================

print(
    "Outer:",
    print(
        "Inner"
    ),
)


# The inner print() executes first.
#
# Its return value is None.
#
# Therefore the outer print() displays None as one of its arguments.


# =============================================================================
# 32. Using sep With Collections of Values
# =============================================================================

print(
    10,
    20,
    30,
    40,
    sep=", ",
)


# =============================================================================
# 33. Using end for Progress-Style Output
# =============================================================================

print(
    "Step 1",
    end=" -> ",
)

print(
    "Step 2",
    end=" -> ",
)

print(
    "Step 3"
)


# =============================================================================
# 34. Printing a Simple Table
# =============================================================================

print(
    "Name",
    "Age",
    "Score",
    sep=" | ",
)

print(
    "Alex",
    30,
    95,
    sep=" | ",
)

print(
    "Sam",
    28,
    90,
    sep=" | ",
)


# =============================================================================
# 35. file Parameter
# =============================================================================

import sys

print(
    "Output through standard output",
    file=sys.stdout,
)


# `file` determines where print() sends its output.
#
# By default:
#
#     file = sys.stdout


# =============================================================================
# 36. Printing to Standard Error
# =============================================================================

print(
    "Example error message",
    file=sys.stderr,
)


# sys.stderr is commonly used for error-related output.


# =============================================================================
# 37. flush Parameter
# =============================================================================

print(
    "Immediate output",
    flush=True,
)


# flush=True asks Python to flush the output stream immediately.


# =============================================================================
# 38. Default print() Parameters
# =============================================================================

"""
The basic signature is conceptually:

    print(
        *objects,
        sep=" ",
        end="\\n",
        file=None,
        flush=False,
    )


Important parameters:

    *objects
        Values to print.

    sep
        Separator between multiple values.

    end
        Text printed after the final value.

    file
        Output stream.

    flush
        Whether to flush the stream immediately.
"""


# =============================================================================
# 39. sep Does Not Affect a Single Argument
# =============================================================================

print(
    "Python",
    sep="---",
)


# sep matters when multiple arguments are supplied.


# =============================================================================
# 40. end Does Not Add Extra Text Automatically
# =============================================================================

print(
    "Python",
    end="END\n",
)


# Whatever is supplied to end is written after the final argument.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ print() displays values.

✓ print() can accept multiple arguments.

✓ Multiple arguments are separated by a space by default.

      print("Python", "SQL")

      -> Python SQL

✓ `sep` controls the separator between arguments.

      print("Python", "SQL", sep=" | ")

      -> Python | SQL

✓ `end` controls what is printed after the final argument.

      print("Python", end=" ")

✓ The default separator is:

      sep=" "

✓ The default ending is:

      end="\\n"

✓ print() without arguments creates a blank line.

✓ print() evaluates expressions before displaying them.

✓ print() can display variables and collections.

✓ print() returns:

      None

✓ `file` controls the output stream.

✓ `flush=True` requests immediate flushing of the output stream.

✓ `repr()` or `!r` can display a representation useful for
  understanding values such as strings containing escape characters.

Core model:

    print(
        values,
        sep=separator,
        end=ending,
        file=stream,
        flush=flush_setting,
    )
"""