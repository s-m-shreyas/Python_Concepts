"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
While Loop

Overview
--------
The `while` loop repeatedly executes a block of code as long as a specified
condition evaluates to True.

Unlike the `for` loop, which iterates over an iterable object, the `while`
loop is condition-controlled. It is commonly used when the number of
iterations is not known beforehand.

Syntax
------
while condition:
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
Execute Exit Loop
 Block
   │
   ▼
Return to Condition

Characteristics
---------------
• Condition-controlled loop.
• Executes while the condition remains True.
• Number of iterations is determined at runtime.
• Requires manual modification of the loop condition.
• Can produce infinite loops if not handled carefully.

Time Complexity
---------------
O(n)

where n is the number of loop iterations.

Common Use Cases
----------------
• Unknown number of iterations.
• Waiting for user input.
• Reading data until a condition is met.
• Retry mechanisms.
• Simulation problems.

Best Practices
--------------
• Always ensure the loop condition eventually becomes False.
• Update the loop variable inside the loop body.
• Avoid unnecessary infinite loops.
• Keep loop conditions simple and readable.

References
----------
Python Official Documentation

https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
"""


# =============================================================================
# Example 1
# Basic Counter
# =============================================================================

counter: int = 1

while counter <= 5:

    print(f"Counter -> {counter}")

    counter += 1


# =============================================================================
# Example 2
# Countdown
# =============================================================================

countdown: int = 5

while countdown > 0:

    print(f"Countdown -> {countdown}")

    countdown -= 1


# =============================================================================
# Example 3
# Multiplication Table
# =============================================================================

TABLE_NUMBER: int = 7

multiplier: int = 1

while multiplier <= 10:

    print(
        f"{TABLE_NUMBER} × {multiplier}"
        f" = {TABLE_NUMBER * multiplier}"
    )

    multiplier += 1


# =============================================================================
# Example 4
# Sum of Natural Numbers
# =============================================================================

LIMIT: int = 10

current_number: int = 1
total_sum: int = 0

while current_number <= LIMIT:

    total_sum += current_number

    current_number += 1

print(f"Sum of first {LIMIT} natural numbers -> {total_sum}")


# =============================================================================
# Example 5
# Reverse Digits of an Integer
# =============================================================================

original_number: int = 12_345

remaining_number: int = original_number
reversed_number: int = 0

while remaining_number > 0:

    digit: int = remaining_number % 10

    reversed_number = (reversed_number * 10) + digit

    remaining_number //= 10

print(f"Original Number -> {original_number}")

print(f"Reversed Number -> {reversed_number}")


# =============================================================================
# Example 6
# Infinite Loop (Demonstration Only)
# =============================================================================

"""
while True:

    print("This loop never terminates.")

Use Ctrl + C to stop execution.

Infinite loops are commonly used in:

• Servers
• Game loops
• Event listeners
• Background services
"""

# =============================================================================
# End of Module
# =============================================================================