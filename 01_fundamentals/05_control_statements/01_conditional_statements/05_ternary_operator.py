"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
Ternary Operator (Conditional Expression)

Overview
--------
The ternary operator provides a concise way to choose between two values based
on a condition.

It is Python's shorthand alternative to a simple `if-else` statement when only
a single expression needs to be evaluated.

Unlike a regular `if-else` statement, the ternary operator returns a value.

Syntax
------
value_if_true if condition else value_if_false

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
Return  Return
Left    Right
Value   Value

Characteristics
---------------
• Evaluates exactly one condition.
• Returns one of two expressions.
• Produces cleaner code for simple decisions.
• Cannot execute multiple statements.

Common Use Cases
----------------
• Variable assignment
• Display messages
• Choosing default values
• Simple value transformation
• Conditional formatting

Best Practices
--------------
• Use for simple conditions only.
• Keep both expressions short and readable.
• Prefer a regular `if-else` statement for complex logic.
• Avoid deeply nested ternary operators.

When NOT to Use
---------------
• Multiple statements are required.
• Complex business logic is involved.
• Multiple conditions reduce readability.
• Nested ternary operators become difficult to understand.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/expressions.html#conditional-expressions
"""

import random


# =============================================================================
# Example 1
# Voting Eligibility
# =============================================================================

VOTING_AGE: int = 18

person_age: int = random.randint(1, 100)

voting_status: str = (
    "Eligible to vote."
    if person_age >= VOTING_AGE
    else "Not eligible to vote."
)

print(f"Age: {person_age} -> {voting_status}")


# =============================================================================
# Example 2
# Even or Odd Number
# =============================================================================

random_number: int = random.randint(1, 100)

number_type: str = (
    "Even number."
    if random_number % 2 == 0
    else "Odd number."
)

print(f"Number: {random_number} -> {number_type}")


# =============================================================================
# Example 3
# Positive or Negative Number
# =============================================================================

signed_number: int = random.randint(-100, 100)

number_sign: str = (
    "Positive number."
    if signed_number >= 0
    else "Negative number."
)

print(f"Number: {signed_number} -> {number_sign}")


# =============================================================================
# Example 4
# Maximum of Two Numbers
# =============================================================================

first_number: int = random.randint(1, 100)
second_number: int = random.randint(1, 100)

maximum_number: int = (
    first_number
    if first_number > second_number
    else second_number
)

print(
    f"Numbers: ({first_number}, {second_number}) "
    f"-> Maximum: {maximum_number}"
)


# =============================================================================
# Example 5
# User Authentication
# =============================================================================

is_authenticated: bool = random.choice([True, False])

login_message: str = (
    "Login successful."
    if is_authenticated
    else "Login failed."
)

print(
    f"Authentication: {is_authenticated} "
    f"-> {login_message}"
)


# =============================================================================
# Example 6
# Salary Eligibility
# =============================================================================

MINIMUM_SALARY: int = 50_000

employee_salary: int = random.randint(20_000, 100_000)

benefit_status: str = (
    "Eligible for premium benefits."
    if employee_salary >= MINIMUM_SALARY
    else "Not eligible for premium benefits."
)

print(
    f"Salary: ₹{employee_salary:,} "
    f"-> {benefit_status}"
)


# =============================================================================
# Example 7
# Empty vs Non-empty Collection
# =============================================================================

employee_records: list[str] = random.choice(
    [
        [],
        ["Alice", "Bob", "Charlie"]
    ]
)

record_status: str = (
    "Employee records available."
    if employee_records
    else "No employee records found."
)

print(
    f"Employees: {employee_records} "
    f"-> {record_status}"
)


# =============================================================================
# Example 8
# Pass or Fail
# =============================================================================

PASSING_MARKS: int = 35

student_marks: int = random.randint(0, 100)

exam_result: str = (
    "Passed."
    if student_marks >= PASSING_MARKS
    else "Failed."
)

print(
    f"Marks: {student_marks} "
    f"-> {exam_result}"
)


# =============================================================================
# End of Module
# =============================================================================