==============================================================================
Python Concepts Repository
Style Guide
==============================================================================

Purpose
-------
This document defines the coding, documentation, and organizational standards
followed throughout this repository.

The objective is to maintain consistency, readability, scalability, and
production-quality educational content across every Python module.

This repository is intended to be a long-term reference that teaches Python
concepts through clean, professional implementations rather than isolated code
examples.


==============================================================================
1. Repository Philosophy
==============================================================================

• One file = One concept.
• One folder = One topic.
• Every concept should be understandable without opening another file.
• Teach the logic before the syntax.
• Prefer readability over cleverness.
• Progress from beginner concepts to production-quality practices.
• Every file should feel like a chapter in a programming book.


==============================================================================
2. Repository Structure
==============================================================================

Each topic should have its own directory.

Example

Control Statements

    Conditional Statements

        if

        if-else

        if-elif-else

        nested if

        ternary operator

        match-case

    Looping Statements

        for

        while

        nested loops

        break

        continue

        pass

        loop else

        range()

        enumerate()

        zip()


==============================================================================
3. Python Module Structure
==============================================================================

Every Python module should follow this order.

1. Module Documentation
2. Imports
3. Examples
4. Key Takeaways
5. End of File Marker


==============================================================================
4. Module Documentation
==============================================================================

Every module begins with:

• Title
• Module Name
• Overview
• Syntax
• Flow Diagram
• Characteristics
• Time Complexity (where applicable)
• Common Use Cases
• Best Practices
• Common Mistakes
• References


==============================================================================
5. Example Structure
==============================================================================

Every example should follow this format.

# =============================================================================
# Example 1: Example Title
# =============================================================================

Examples should progress naturally.

1. Basic Example
2. Intermediate Example
3. Practical Example
4. Real-world Example
5. Interview-oriented Example


==============================================================================
6. Naming Conventions
==============================================================================

Variables
---------

Use snake_case.

Examples

employee_name

student_marks

matrix_row

candidate_number

salary_amount


Functions
---------

Use snake_case.

Examples

calculate_salary()

merge_sort()

quick_sort()


Classes
-------

Use PascalCase.

Examples

Employee

Student

BankAccount


Constants
---------

Use UPPER_CASE.

Examples

VOTING_AGE

MINIMUM_SALARY

MAXIMUM_RETRIES

DATABASE_PORT

TRIANGLE_ROWS

CHESSBOARD_COLUMNS


==============================================================================
7. Variable Naming Rules
==============================================================================

Variables should clearly describe what they represent.

Good

employee_name

student_marks

matrix_row

matrix_value

candidate_number

prime_candidate

search_numbers

sample_numbers

inventory_items

employee_records

Bad

x

y

temp

item

row

data

number

list1

value


Repository Rule
---------------

Every identifier inside a Python file should be unique unless it intentionally
represents the same object throughout the file.

Do NOT reuse variable names across examples.

Good

sample_numbers

search_numbers

employee_names

matrix_values

inventory_items

Bad

numbers

numbers

numbers

numbers

Reason

• Prevents variable shadowing.
• Eliminates mypy warnings.
• Eliminates Pylance warnings.
• Makes each example independent.
• Improves readability.


==============================================================================
8. Constants
==============================================================================

Constants should always be descriptive.

Good

TRIANGLE_ROWS

CHESSBOARD_ROWS

TABLE_SIZE

MINIMUM_SALARY

MAXIMUM_RETRIES

DATABASE_PORT

Bad

ROWS

LIMIT

SIZE

NUMBER

PORT


Repository Rule
---------------

Constants must never be redefined later in the same file.


==============================================================================
9. Type Hints
==============================================================================

Use type hints wherever practical.

Examples

employee_name: str

salary: float

numbers: list[int]

employees: dict[str, int]


==============================================================================
10. Comments
==============================================================================

Comments should improve understanding.

Prefer section headers.

Example

# =============================================================================
# Example 3: Reverse an Integer
# =============================================================================

Avoid unnecessary inline comments that simply describe obvious code.


==============================================================================
11. Formatting
==============================================================================

• One blank line between logical sections.
• Keep formatting consistent.
• Keep indentation consistent.
• Use descriptive spacing.
• Prefer readability over compact code.


==============================================================================
12. Code Quality
==============================================================================

Prefer readable code over shorter code.

Avoid unnecessary nesting.

Break complex logic into helper functions where appropriate.

Use expressive names instead of abbreviations.

Avoid magic numbers by introducing descriptive constants.


==============================================================================
13. Educational Standards
==============================================================================

Each module should answer one question completely.

Examples

What is a for loop?

What is recursion?

What is break?

What is enumerate()?

A reader should not need another file to understand the current concept.


==============================================================================
14. Key Takeaways
==============================================================================

Every file should conclude with:

# =============================================================================
# Key Takeaways
# =============================================================================

Summarize the most important learning points in bullet form.

This reinforces the concept before the file ends.


==============================================================================
15. Static Analysis Standards
==============================================================================

Every Python module should execute cleanly under modern static analysis tools.

Target Standards

• Zero mypy warnings.
• Zero Pylance warnings.
• No variable shadowing.
• No constant redefinition.
• No incompatible type assignments.
• No unnecessary name reuse.
• Consistent naming throughout the file.


==============================================================================
16. Repository Standards
==============================================================================

This repository prioritizes

• Readability
• Consistency
• Maintainability
• Scalability
• Production-quality practices
• Professional documentation
• Long-term educational value

Every module should look and feel like part of the same book.


==============================================================================
17. Guiding Principle
==============================================================================

"Understand the logic first.

Syntax becomes easy afterwards."


==============================================================================
Last Updated
------------------------------------------------------------------------------

Maintained continuously as the repository evolves.