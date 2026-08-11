"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
Nested If Statement

Overview
--------
A nested `if` statement is an `if` statement placed inside another `if`
statement.

The inner condition is evaluated only when the outer condition evaluates
to True.

Nested conditions are useful when a decision depends on another decision
being satisfied first.

Syntax
------
if condition_1:
    statement(s)

    if condition_2:
        statement(s)

Flow
----
Condition 1
      │
      ▼
True?
 │
 ├────► Evaluate Condition 2
 │              │
 │              ▼
 │          True?
 │          │
 │          ├────► Execute Inner Block
 │          │
 │          ▼
 │      Skip Inner Block
 │
 ▼
Continue Program

Characteristics
---------------
• Allows hierarchical decision making.
• Inner conditions execute only if outer conditions are satisfied.
• Useful for validating prerequisites before further checks.
• Can improve readability when decisions naturally depend on one another.

Common Use Cases
----------------
• User authentication and authorization
• Multi-level input validation
• Banking transactions
• Employee access control
• Academic eligibility
• Business rule validation

Best Practices
--------------
• Keep nesting levels minimal.
• Avoid deeply nested structures.
• Use meaningful variable names.
• Consider using logical operators when nesting becomes excessive.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/compound_stmts.html#if
"""

import random


# =============================================================================
# Example 1
# Authentication and Authorization
# =============================================================================

ADMIN_ROLE: str = "Admin"

is_authenticated: bool = random.choice([True, False])
user_role: str = random.choice(
    [
        ADMIN_ROLE,
        "Manager",
        "User"
    ]
)

if is_authenticated:

    if user_role == ADMIN_ROLE:
        print(
            f"Authentication: {is_authenticated}, "
            f"Role: {user_role} "
            "-> Administrative access granted."
        )


# =============================================================================
# Example 2
# Student Scholarship Eligibility
# =============================================================================

MINIMUM_MARKS: int = 85
MAXIMUM_FAMILY_INCOME: int = 500_000

marks: int = random.randint(40, 100)
family_income: int = random.randint(100_000, 1_000_000)

if marks >= MINIMUM_MARKS:

    if family_income <= MAXIMUM_FAMILY_INCOME:
        print(
            f"Marks: {marks}, "
            f"Family Income: ₹{family_income:,} "
            "-> Scholarship approved."
        )


# =============================================================================
# Example 3
# Employee Promotion Eligibility
# =============================================================================

MINIMUM_EXPERIENCE: int = 5
MINIMUM_RATING: int = 4

experience: int = random.randint(1, 10)
performance_rating: int = random.randint(1, 5)

if experience >= MINIMUM_EXPERIENCE:

    if performance_rating >= MINIMUM_RATING:
        print(
            f"Experience: {experience} years, "
            f"Rating: {performance_rating} "
            "-> Eligible for promotion."
        )


# =============================================================================
# Example 4
# Bank Loan Approval
# =============================================================================

MINIMUM_SALARY: int = 60_000
MINIMUM_CREDIT_SCORE: int = 700

salary: int = random.randint(20_000, 120_000)
credit_score: int = random.randint(500, 850)

if salary >= MINIMUM_SALARY:

    if credit_score >= MINIMUM_CREDIT_SCORE:
        print(
            f"Salary: ₹{salary:,}, "
            f"Credit Score: {credit_score} "
            "-> Loan approved."
        )


# =============================================================================
# Example 5
# Inventory Validation
# =============================================================================

MINIMUM_STOCK: int = 10

product_exists: bool = random.choice([True, False])
stock_quantity: int = random.randint(0, 25)

if product_exists:

    if stock_quantity >= MINIMUM_STOCK:
        print(
            f"Product Exists: {product_exists}, "
            f"Stock: {stock_quantity} "
            "-> Ready for dispatch."
        )


# =============================================================================
# Example 6
# Exam Eligibility
# =============================================================================

MINIMUM_ATTENDANCE: int = 75
MINIMUM_ASSIGNMENTS: int = 5

attendance: int = random.randint(50, 100)
assignments_completed: int = random.randint(0, 6)

if attendance >= MINIMUM_ATTENDANCE:

    if assignments_completed >= MINIMUM_ASSIGNMENTS:
        print(
            f"Attendance: {attendance}%, "
            f"Assignments: {assignments_completed} "
            "-> Eligible for final examination."
        )


# =============================================================================
# End of Module
# =============================================================================