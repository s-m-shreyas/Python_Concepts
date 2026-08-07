"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
Break Statement

Overview
--------
The `break` statement immediately terminates the nearest enclosing loop,
regardless of whether the loop condition is still True.

Program execution resumes with the first statement immediately following
the terminated loop.

The `break` statement can be used inside both `for` and `while` loops.

Syntax
------
for item in iterable:

    if condition:

        break

while condition:

    if condition:

        break

Flow
----
Loop Starts
     │
     ▼
Execute Current Iteration
     │
     ▼
Break Condition Met?
     │
 ┌───┴───┐
 │       │
No      Yes
 │       │
 ▼       ▼
Next    Exit Loop
Iteration

Characteristics
---------------
• Immediately exits the nearest enclosing loop.
• Remaining loop iterations are skipped.
• Works with both `for` and `while` loops.
• Commonly used for searching and early termination.

Time Complexity
---------------
Worst Case:
O(n)

Best Case:
O(1)

The loop may terminate early depending on when the break condition is met.

Common Use Cases
----------------
• Searching for an element.
• Input validation.
• Menu-driven programs.
• Infinite loop termination.
• Optimization by avoiding unnecessary iterations.

Best Practices
--------------
• Use `break` only when early termination improves readability.
• Keep the break condition clear and obvious.
• Avoid multiple unrelated break statements inside the same loop.

Common Mistakes
---------------
• Forgetting that only the nearest loop is terminated.
• Using `break` where `return` is more appropriate.
• Creating overly complex loop logic with many break statements.

References
----------
Python Official Documentation

https://docs.python.org/3/reference/simple_stmts.html#break
"""


# =============================================================================
# Example 1
# Stop When a Target Number is Found
# =============================================================================

numbers: list[int] = [
    5,
    18,
    27,
    41,
    56
]

TARGET_NUMBER: int = 27

for current_number in numbers:

    print(f"Checking {current_number}")

    if current_number == TARGET_NUMBER:

        print(f"Found {TARGET_NUMBER}.")
        break


# =============================================================================
# Example 2
# Exit a While Loop
# =============================================================================

counter: int = 1

while True:

    print(f"Counter -> {counter}")

    if counter == 5:

        print("Stopping loop.")
        break

    counter += 1


# =============================================================================
# Example 3
# Find First Even Number
# =============================================================================

random_numbers: list[int] = [
    11,
    15,
    19,
    24,
    28
]

for candidate_number in random_numbers:

    if candidate_number % 2 == 0:

        print(f"First even number -> {candidate_number}")
        break


# =============================================================================
# Example 4
# Search for an Employee
# =============================================================================

employee_names: list[str] = [
    "Alice",
    "Bob",
    "Charlie",
    "David"
]

TARGET_EMPLOYEE: str = "Charlie"

for employee_name in employee_names:

    if employee_name == TARGET_EMPLOYEE:

        print(f"Employee found -> {employee_name}")
        break


# =============================================================================
# Example 5
# Menu Exit Simulation
# =============================================================================

menu_options: list[str] = [
    "View Profile",
    "Settings",
    "Logout"
]

for menu_option in menu_options:

    print(menu_option)

    if menu_option == "Logout":

        print("Exiting menu.")
        break


# =============================================================================
# End of File
# =============================================================================