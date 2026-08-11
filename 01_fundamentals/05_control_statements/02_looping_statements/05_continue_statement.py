"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
Continue Statement

Overview
--------
The `continue` statement skips the remaining statements in the current
iteration of a loop and immediately proceeds to the next iteration.

Unlike the `break` statement, which completely terminates the loop,
`continue` only skips the current iteration while allowing the loop to
continue executing.

The `continue` statement can be used inside both `for` and `while` loops.

Syntax
------
for item in iterable:

    if condition:

        continue

while condition:

    if condition:

        continue

Flow
----
Loop Starts
     │
     ▼
Execute Current Iteration
     │
     ▼
Continue Condition Met?
     │
 ┌───┴───┐
 │       │
No      Yes
 │       │
 ▼       ▼
Execute  Skip Remaining
Remaining Statements
Statements     │
      │        │
      └────────┘
           │
           ▼
Next Iteration

Characteristics
---------------
• Skips only the current iteration.
• Loop execution continues normally.
• Works with both `for` and `while` loops.
• Improves readability by avoiding deeply nested conditions.

Time Complexity
---------------
Worst Case:
O(n)

The loop still iterates over every element, although some iterations may
skip part of the loop body.

Common Use Cases
----------------
• Skip invalid records.
• Ignore unwanted values.
• Filter data during iteration.
• Skip specific menu options.
• Data cleaning.

Best Practices
--------------
• Use `continue` only when it improves readability.
• Keep the continue condition simple.
• Ensure loop variables are updated correctly in `while` loops.

Common Mistakes
---------------
• Forgetting to update loop variables before `continue` in a while loop,
  resulting in infinite loops.
• Overusing `continue`, making loop logic difficult to follow.

References
----------
Python Official Documentation

https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
"""


# =============================================================================
# Example 1: Skip Even Numbers
# =============================================================================

numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6
]

for current_number in numbers:

    if current_number % 2 == 0:

        continue

    print(f"Odd Number -> {current_number}")


# =============================================================================
# Example 2: Skip Empty Strings
# =============================================================================

employee_names: list[str] = [
    "Alice",
    "",
    "Bob",
    "",
    "Charlie"
]

for employee_name in employee_names:

    if employee_name == "":

        continue

    print(f"Employee -> {employee_name}")


# =============================================================================
# Example 3: Skip Negative Numbers
# =============================================================================

measurements: list[int] = [
    25,
    -1,
    18,
    -8,
    32
]

for measurement in measurements:

    if measurement < 0:

        continue

    print(f"Valid Measurement -> {measurement}")


# =============================================================================
# Example 4: Continue Inside While Loop
# =============================================================================

counter: int = 0

while counter < 6:

    counter += 1

    if counter == 3:

        continue

    print(f"Counter -> {counter}")


# =============================================================================
# Example 5: Skip Reserved Usernames
# =============================================================================

RESERVED_USERNAMES: set[str] = {
    "admin",
    "root"
}

usernames: list[str] = [
    "Alice",
    "admin",
    "Charlie",
    "root",
    "David"
]

for username in usernames:

    if username.lower() in RESERVED_USERNAMES:

        continue

    print(f"Valid Username -> {username}")


# =============================================================================
# End of File
# =============================================================================