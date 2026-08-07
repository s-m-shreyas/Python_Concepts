"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
Nested Loops

Overview
--------
A nested loop is a loop placed inside another loop. For each iteration of the
outer loop, the inner loop executes completely.

Nested loops are commonly used when working with two-dimensional data,
matrices, coordinate systems, tables, grids, and pattern generation.

Syntax
------
for outer_variable in iterable:

    for inner_variable in iterable:

        statement(s)

Flow
----
Outer Loop
     │
     ▼
Execute Outer Iteration
     │
     ▼
Execute Inner Loop Completely
     │
     ▼
Next Outer Iteration
     │
     ▼
Repeat Until Outer Loop Ends

Characteristics
---------------
• A loop inside another loop.
• Inner loop completes for every outer iteration.
• Can combine different loop types (for + for, while + while, etc.).
• Useful for multi-dimensional traversal.
• Time complexity often increases multiplicatively.

Time Complexity
---------------
Typically O(n × m)

where:

• n = outer loop iterations
• m = inner loop iterations

If both loops iterate n times:

O(n²)

Common Use Cases
----------------
• Matrix traversal
• Pattern printing
• Multiplication tables
• Grid-based problems
• Coordinate generation
• Comparing two collections

Best Practices
--------------
• Keep nesting depth as small as possible.
• Avoid unnecessary nested loops for performance reasons.
• Use meaningful loop variable names.
• Break large nested logic into helper functions when appropriate.

References
----------
Python Official Documentation

https://docs.python.org/3/tutorial/controlflow.html
"""


# =============================================================================
# Example 1
# Matrix Traversal
# =============================================================================

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for matrix_row in matrix:

    for matrix_value in matrix_row:

        print(matrix_value, end=" ")

    print()


# =============================================================================
# Example 2
# Multiplication Table (1 to 5)
# =============================================================================

for multiplicand in range(1, 6):

    for multiplier in range(1, 6):

        print(
            f"{multiplicand * multiplier:2}",
            end=" "
        )

    print()


# =============================================================================
# Example 3
# Coordinate Generation
# =============================================================================

for x_coordinate in range(3):

    for y_coordinate in range(3):

        print(f"({x_coordinate}, {y_coordinate})")

    print()


# =============================================================================
# Example 4
# Compare Two Collections
# =============================================================================

employee_names: list[str] = [
    "Alice",
    "Bob"
]

project_names: list[str] = [
    "Payroll",
    "Inventory"
]

for employee_name in employee_names:

    for project_name in project_names:

        print(
            f"{employee_name} -> {project_name}"
        )

    print()


# =============================================================================
# Example 5
# Right-Angled Triangle Pattern
# =============================================================================

TRIANGLE_ROWS: int = 5

for row_number in range(1, TRIANGLE_ROWS + 1):

    for _ in range(row_number):

        print("*", end=" ")

    print()


# =============================================================================
# Example 6
# Chessboard Coordinates
# =============================================================================

CHESSBOARD_ROWS: int = 8
CHESSBOARD_COLUMNS: int = 8

for chessboard_row in range(1, CHESSBOARD_ROWS + 1):

    for chessboard_column in range(1, CHESSBOARD_COLUMNS + 1):

        print(
            f"({chessboard_row}, {chessboard_column})",
            end=" "
        )

    print()


# =============================================================================
# End of Module
# =============================================================================