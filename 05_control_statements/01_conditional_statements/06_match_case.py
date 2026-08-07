"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
Match-Case Statement (Structural Pattern Matching)

Overview
--------
The `match-case` statement provides a cleaner and more readable alternative
to long `if-elif-else` chains when comparing a single value against multiple
possible cases.

Introduced in Python 3.10, it performs structural pattern matching and selects
the first matching case.

Syntax
------
match expression:
    case pattern_1:
        statement(s)
    case pattern_2:
        statement(s)
    case _:
        statement(s)

Flow
----
Expression
     │
     ▼
Match Case 1?
     │
 ┌───┴───┐
 │       │
Yes      No
 │        │
 ▼        ▼
Execute  Check Next Case
 Block
             │
             ▼
       ...
             │
             ▼
      Execute Default (_)

Characteristics
---------------
• Introduced in Python 3.10.
• Evaluates a single expression.
• Executes only the first matching case.
• Improves readability over long if-elif chains.
• Supports advanced structural pattern matching.

Common Use Cases
----------------
• Menu-driven applications
• Command interpreters
• Status code handling
• User role management
• API response processing
• State machines

Best Practices
--------------
• Use for multiple discrete values.
• Keep each case independent.
• Always include a default (`case _`) when appropriate.
• Prefer `if-elif-else` for complex Boolean expressions.

When NOT to Use
---------------
• Only two possible outcomes exist.
• Conditions involve comparison operators (<, >, <=, >=).
• Logic depends on multiple unrelated variables.
• Complex Boolean expressions are required.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
"""

import random


# =============================================================================
# Example 1
# Day of the Week
# =============================================================================

day_name: str = random.choice(
    [
        "Monday",
        "Tuesday",
        "Sunday"
    ]
)

match day_name:

    case "Monday":
        print(f"Day: {day_name} -> Start of the work week.")

    case "Tuesday":
        print(f"Day: {day_name} -> Regular working day.")

    case "Sunday":
        print(f"Day: {day_name} -> Weekend.")

    case _:
        print(f"Day: {day_name} -> Unknown day.")


# =============================================================================
# Example 2
# User Role
# =============================================================================

user_role: str = random.choice(
    [
        "Admin",
        "Manager",
        "Employee",
        "Guest"
    ]
)

match user_role:

    case "Admin":
        print(f"Role: {user_role} -> Full system access.")

    case "Manager":
        print(f"Role: {user_role} -> Department access.")

    case "Employee":
        print(f"Role: {user_role} -> Standard employee access.")

    case _:
        print(f"Role: {user_role} -> Read-only access.")


# =============================================================================
# Example 3
# HTTP Status Code
# =============================================================================

http_status_code: int = random.choice(
    [
        200,
        400,
        404,
        500
    ]
)

match http_status_code:

    case 200:
        print(f"HTTP Status: {http_status_code} -> OK")

    case 400:
        print(f"HTTP Status: {http_status_code} -> Bad Request")

    case 404:
        print(f"HTTP Status: {http_status_code} -> Not Found")

    case 500:
        print(f"HTTP Status: {http_status_code} -> Internal Server Error")

    case _:
        print(f"HTTP Status: {http_status_code} -> Unknown Status")


# =============================================================================
# Example 4
# Calculator Operator
# =============================================================================

operator_symbol: str = random.choice(
    [
        "+",
        "-",
        "*",
        "/"
    ]
)

match operator_symbol:

    case "+":
        print(f"Operator: {operator_symbol} -> Addition")

    case "-":
        print(f"Operator: {operator_symbol} -> Subtraction")

    case "*":
        print(f"Operator: {operator_symbol} -> Multiplication")

    case "/":
        print(f"Operator: {operator_symbol} -> Division")

    case _:
        print(f"Operator: {operator_symbol} -> Unsupported operator")


# =============================================================================
# Example 5
# File Extension
# =============================================================================

file_extension: str = random.choice(
    [
        ".py",
        ".txt",
        ".csv",
        ".pdf"
    ]
)

match file_extension:

    case ".py":
        print(f"Extension: {file_extension} -> Python Source File")

    case ".txt":
        print(f"Extension: {file_extension} -> Text File")

    case ".csv":
        print(f"Extension: {file_extension} -> CSV File")

    case _:
        print(f"Extension: {file_extension} -> Other File Type")


# =============================================================================
# Example 6
# Traffic Signal
# =============================================================================

traffic_signal: str = random.choice(
    [
        "Red",
        "Yellow",
        "Green"
    ]
)

match traffic_signal:

    case "Red":
        print(f"Signal: {traffic_signal} -> Stop")

    case "Yellow":
        print(f"Signal: {traffic_signal} -> Prepare to Stop")

    case "Green":
        print(f"Signal: {traffic_signal} -> Go")

    case _:
        print(f"Signal: {traffic_signal} -> Invalid Signal")


# =============================================================================
# Example 7
# Menu Selection
# =============================================================================

menu_option: int = random.randint(1, 5)

match menu_option:

    case 1:
        print(f"Option: {menu_option} -> View Profile")

    case 2:
        print(f"Option: {menu_option} -> Edit Profile")

    case 3:
        print(f"Option: {menu_option} -> Settings")

    case 4:
        print(f"Option: {menu_option} -> Logout")

    case _:
        print(f"Option: {menu_option} -> Invalid Selection")


# =============================================================================
# End of Module
# =============================================================================