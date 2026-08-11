"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
If Statement

Overview
--------
The `if` statement is Python's fundamental decision-making construct.

It evaluates a Boolean expression and executes a block of code only when
the specified condition evaluates to True.

If the condition evaluates to False, the associated block is skipped and
program execution continues with the next statement.

Syntax
------
if condition:
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
Execute Skip
 Block   Block

Characteristics
---------------
• Simplest conditional statement.
• Executes code only when the condition is True.
• Does not provide an alternative execution path.
• Forms the foundation of all decision-making constructs in Python.

Common Use Cases
----------------
• Input validation
• Permission checking
• Value comparisons
• Error handling
• Business rules
• Feature toggles

Best Practices
--------------
• Keep conditions simple and readable.
• Use meaningful variable names.
• Avoid deeply nested conditions.
• Prefer descriptive constants instead of magic numbers.
• Write expressive Boolean conditions.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/compound_stmts.html#if
"""

import random


# =============================================================================
# Example 1
# Eligibility Check
# =============================================================================

VOTING_AGE: int = 18

age: int = random.randint(1, 100)

if age >= VOTING_AGE:
    print(f"Age: {age} -> Eligible to vote.")


# =============================================================================
# Example 2
# Boolean Variable
# =============================================================================

is_logged_in: bool = random.choice([True, False])

if is_logged_in:
    print(f"Authentication: {is_logged_in} -> Login successful.")


# =============================================================================
# Example 3
# Comparison Operator
# =============================================================================

HIGH_TEMPERATURE: int = 30

temperature: int = random.randint(-10, 45)

if temperature > HIGH_TEMPERATURE:
    print(f"Temperature: {temperature}°C -> High temperature detected.")


# =============================================================================
# Example 4
# String Comparison
# =============================================================================

ADMIN_ROLE: str = "Admin"

user_role: str = random.choice(
    [
        "Admin",
        "Manager",
        "User"
    ]
)

if user_role == ADMIN_ROLE:
    print(f"Role: {user_role} -> Administrative privileges enabled.")


# =============================================================================
# Example 5
# Membership Operator
# =============================================================================

AVAILABLE_FRUITS: list[str] = [
    "Apple",
    "Banana",
    "Orange"
]

fruit_name: str = random.choice(
    [
        "Banana",
        "Mango",
        "Grapes"
    ]
)

if fruit_name in AVAILABLE_FRUITS:
    print(f"Fruit: {fruit_name} -> Available in inventory.")


# =============================================================================
# Example 6
# Truthy Values
# =============================================================================

employees: list[str] = random.choice(
    [
        [],
        ["Alice", "Bob", "Charlie"]
    ]
)

if employees:
    print(f"Employees: {employees} -> Employee records available.")


# =============================================================================
# Example 7
# Multiple Conditions using Logical Operators
# =============================================================================

MINIMUM_SALARY: int = 50_000
MINIMUM_EXPERIENCE: int = 3

salary: int = random.randint(20_000, 100_000)
experience: int = random.randint(0, 10)

if (
    salary >= MINIMUM_SALARY
    and experience >= MINIMUM_EXPERIENCE
):
    print(
        f"Salary: ₹{salary}, Experience: {experience} years "
        "-> Candidate shortlisted."
    )


# =============================================================================
# End of Module
# =============================================================================