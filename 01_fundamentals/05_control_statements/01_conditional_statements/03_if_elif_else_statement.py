"""
==============================================================================
Python Control Statements
==============================================================================

Module
------
If-Elif-Else Statement

Overview
--------
The `if-elif-else` statement extends the basic `if-else` construct by allowing
multiple conditions to be evaluated sequentially.

Python evaluates each condition from top to bottom. As soon as one condition
evaluates to True, its corresponding block is executed and the remaining
conditions are skipped.

If none of the conditions evaluate to True, the optional `else` block is
executed.

Syntax
------
if condition_1:
    statement(s)
elif condition_2:
    statement(s)
elif condition_3:
    statement(s)
else:
    statement(s)

Flow
----
Condition 1
      │
      ▼
True?
 │
 ├────► Execute Block 1
 │
 ▼
Condition 2
      │
      ▼
True?
 │
 ├────► Execute Block 2
 │
 ▼
Condition 3
      │
      ▼
True?
 │
 ├────► Execute Block 3
 │
 ▼
Execute Else Block

Characteristics
---------------
• Supports multiple decision branches.
• Conditions are evaluated sequentially.
• Only the first matching condition is executed.
• Remaining conditions are skipped after the first successful match.
• Improves readability compared to multiple independent `if` statements.

Common Use Cases
----------------
• Grade classification
• Age categorization
• Salary bands
• Tax calculation
• Access level management
• Business rule evaluation

Best Practices
--------------
• Arrange conditions from most specific to most general.
• Use descriptive constants instead of magic numbers.
• Avoid overlapping conditions.
• Keep branching logic simple and readable.
• Use the `else` block as the default or fallback case.

References
----------
Python Official Documentation
https://docs.python.org/3/reference/compound_stmts.html#if
"""

import random


# =============================================================================
# Example 1
# Student Grade Classification
# =============================================================================

GRADE_A_MIN: int = 90
GRADE_B_MIN: int = 75
GRADE_C_MIN: int = 60
PASSING_MARKS: int = 35

marks: int = random.randint(0, 100)

if marks >= GRADE_A_MIN:
    print(f"Marks: {marks} -> Grade A")

elif marks >= GRADE_B_MIN:
    print(f"Marks: {marks} -> Grade B")

elif marks >= GRADE_C_MIN:
    print(f"Marks: {marks} -> Grade C")

elif marks >= PASSING_MARKS:
    print(f"Marks: {marks} -> Grade D")

else:
    print(f"Marks: {marks} -> Failed")


# =============================================================================
# Example 2
# Age Classification
# =============================================================================

CHILD_MAX_AGE: int = 12
TEENAGER_MAX_AGE: int = 19
ADULT_MAX_AGE: int = 59

age: int = random.randint(1, 90)

if age <= CHILD_MAX_AGE:
    print(f"Age: {age} -> Child")

elif age <= TEENAGER_MAX_AGE:
    print(f"Age: {age} -> Teenager")

elif age <= ADULT_MAX_AGE:
    print(f"Age: {age} -> Adult")

else:
    print(f"Age: {age} -> Senior Citizen")


# =============================================================================
# Example 3
# Temperature Classification
# =============================================================================

FREEZING_POINT: int = 0
COLD_MAX_TEMPERATURE: int = 15
PLEASANT_MAX_TEMPERATURE: int = 30

temperature: int = random.randint(-10, 45)

if temperature <= FREEZING_POINT:
    print(f"Temperature: {temperature}°C -> Freezing")

elif temperature <= COLD_MAX_TEMPERATURE:
    print(f"Temperature: {temperature}°C -> Cold")

elif temperature <= PLEASANT_MAX_TEMPERATURE:
    print(f"Temperature: {temperature}°C -> Pleasant")

else:
    print(f"Temperature: {temperature}°C -> Hot")


# =============================================================================
# Example 4
# Employee Experience Classification
# =============================================================================

JUNIOR_MAX_YEARS: int = 2
MID_LEVEL_MAX_YEARS: int = 5
SENIOR_MAX_YEARS: int = 10

experience: int = random.randint(0, 20)

if experience < JUNIOR_MAX_YEARS:
    print(f"Experience: {experience} years -> Junior")

elif experience < MID_LEVEL_MAX_YEARS:
    print(f"Experience: {experience} years -> Mid-Level")

elif experience < SENIOR_MAX_YEARS:
    print(f"Experience: {experience} years -> Senior")

else:
    print(f"Experience: {experience} years -> Expert")


# =============================================================================
# Example 5
# User Access Level
# =============================================================================

ADMIN_ROLE: str = "Admin"
MANAGER_ROLE: str = "Manager"
EMPLOYEE_ROLE: str = "Employee"

role: str = random.choice(
    [
        ADMIN_ROLE,
        MANAGER_ROLE,
        EMPLOYEE_ROLE,
        "Guest"
    ]
)

if role == ADMIN_ROLE:
    print(f"Role: {role} -> Full system access.")

elif role == MANAGER_ROLE:
    print(f"Role: {role} -> Department access.")

elif role == EMPLOYEE_ROLE:
    print(f"Role: {role} -> Standard employee access.")

else:
    print(f"Role: {role} -> Read-only access.")


# =============================================================================
# Example 6
# Body Mass Index (BMI) Classification
# =============================================================================

UNDERWEIGHT_MAX_BMI: float = 18.5
NORMAL_MAX_BMI: float = 25.0
OVERWEIGHT_MAX_BMI: float = 30.0

bmi: float = round(random.uniform(15.0, 40.0), 1)

if bmi < UNDERWEIGHT_MAX_BMI:
    print(f"BMI: {bmi} -> Underweight")

elif bmi < NORMAL_MAX_BMI:
    print(f"BMI: {bmi} -> Normal")

elif bmi < OVERWEIGHT_MAX_BMI:
    print(f"BMI: {bmi} -> Overweight")

else:
    print(f"BMI: {bmi} -> Obese")


# =============================================================================
# Example 7
# Income Tax Slab Classification
# =============================================================================

NO_TAX_LIMIT: int = 300_000
LOWER_TAX_LIMIT: int = 700_000
MIDDLE_TAX_LIMIT: int = 1_500_000

annual_income: int = random.randint(100_000, 2_000_000)

if annual_income <= NO_TAX_LIMIT:
    print(f"Annual Income: ₹{annual_income:,} -> No Tax")

elif annual_income <= LOWER_TAX_LIMIT:
    print(f"Annual Income: ₹{annual_income:,} -> 5% Tax Slab")

elif annual_income <= MIDDLE_TAX_LIMIT:
    print(f"Annual Income: ₹{annual_income:,} -> 20% Tax Slab")

else:
    print(f"Annual Income: ₹{annual_income:,} -> 30% Tax Slab")


# =============================================================================
# End of Module
# =============================================================================