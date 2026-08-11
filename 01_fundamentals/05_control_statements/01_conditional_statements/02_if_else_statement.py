"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
If-Else Statement

Overview
--------
The `if-else` statement extends the basic `if` statement by providing an
alternative execution path when the specified condition evaluates to False.

Unlike a standalone `if` statement, exactly one block of code is executed.

Syntax
------
if condition:
    statement(s)
else:
    statement(s)

Flow
----
Condition
    │
    ▼
Is condition True?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
 ▼      ▼
if      else
Block   Block

Characteristics
---------------
• Executes exactly one code block.
• Supports two-way decision making.
• Improves readability over multiple independent `if` statements.
• Commonly used for binary outcomes.

Common Use Cases
----------------
• Authentication
• Eligibility checking
• Positive / Negative validation
• Even / Odd identification
• Access control
• Data validation

Best Practices
--------------
• Keep conditions concise and meaningful.
• Use descriptive constant names instead of magic numbers.
• Avoid deeply nested conditions.
• Write clear logic for both the True and False paths.
• Prefer expressive variable names.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/compound_stmts.html#if
"""

import random


# =============================================================================
# Example 1
# Voting Eligibility
# =============================================================================

VOTING_AGE: int = 18

person_age: int = random.randint(1, 100)

if person_age >= VOTING_AGE:
    print(f"Age: {person_age} -> Eligible to vote.")
else:
    print(f"Age: {person_age} -> Not eligible to vote.")


# =============================================================================
# Example 2
# Positive or Negative Number
# =============================================================================

ZERO: int = 0

signed_number: int = random.randint(-100, 100)

if signed_number >= ZERO:
    print(f"Number: {signed_number} -> Positive number.")
else:
    print(f"Number: {signed_number} -> Negative number.")


# =============================================================================
# Example 3
# User Authentication
# =============================================================================

is_authenticated: bool = random.choice([True, False])

if is_authenticated:
    print(
        f"Authentication: {is_authenticated}"
        " -> Login successful."
    )
else:
    print(
        f"Authentication: {is_authenticated}"
        " -> Invalid credentials."
    )


# =============================================================================
# Example 4
# Even or Odd Number
# =============================================================================

random_number: int = random.randint(1, 100)

if random_number % 2 == 0:
    print(f"Number: {random_number} -> Even number.")
else:
    print(f"Number: {random_number} -> Odd number.")


# =============================================================================
# Example 5
# User Role Validation
# =============================================================================

ADMIN_ROLE: str = "Admin"

user_role: str = random.choice(
    [
        "Admin",
        "User"
    ]
)

if user_role == ADMIN_ROLE:
    print(f"Role: {user_role} -> Administrative privileges granted.")
else:
    print(f"Role: {user_role} -> Standard user privileges granted.")


# =============================================================================
# Example 6
# Empty vs Non-empty Collection
# =============================================================================

employee_records: list[str] = random.choice(
    [
        [],
        ["Alice", "Bob", "Charlie"]
    ]
)

if employee_records:
    print(
        f"Employees: {employee_records}"
        " -> Employee records available."
    )
else:
    print(
        f"Employees: {employee_records}"
        " -> No employee records found."
    )


# =============================================================================
# Example 7
# Salary Eligibility
# =============================================================================

MINIMUM_SALARY: int = 50_000

employee_salary: int = random.randint(20_000, 100_000)

if employee_salary >= MINIMUM_SALARY:
    print(
        f"Salary: ₹{employee_salary:,}"
        " -> Eligible for premium benefits."
    )
else:
    print(
        f"Salary: ₹{employee_salary:,}"
        " -> Not eligible for premium benefits."
    )