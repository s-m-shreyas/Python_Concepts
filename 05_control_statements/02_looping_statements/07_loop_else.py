"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
Loop Else

Overview
--------
The `else` clause in Python loops executes only when the loop completes
normally without encountering a `break` statement.

It can be used with both `for` and `while` loops.

Many beginners mistakenly believe that the `else` block executes whenever
the loop condition becomes False. In reality, the `else` block executes
only if the loop was **not terminated by a break statement**.

Syntax
------
for item in iterable:

    ...

else:

    ...

while condition:

    ...

else:

    ...

Flow
----
Loop Starts
      │
      ▼
Execute Current Iteration
      │
      ▼
Was break Executed?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Exit      Execute
Loop      else Block

Characteristics
---------------
• Can be used with both `for` and `while` loops.
• Executes only if the loop finishes normally.
• Skipped whenever a `break` statement executes.
• Commonly used when searching for an item.

Time Complexity
---------------
Depends entirely on the loop itself.

The `else` clause adds no additional computational complexity.

Common Use Cases
----------------
• Searching for an element.
• User authentication.
• Prime number checking.
• Data validation.
• Lookup operations.

Best Practices
--------------
• Use loop else only when it naturally improves readability.
• It is most useful when paired with searching logic.
• Avoid forcing loop else into situations where a normal `if` statement
  would be clearer.

Common Mistakes
---------------
• Thinking the else block executes after every loop.
• Assuming else executes because the loop condition becomes False.
• Forgetting that executing `break` skips the else block.

References
----------
Python Official Documentation

https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""


# =============================================================================
# Example 1: for-else Without break
# =============================================================================

sample_numbers: list[int] = [
    10,
    20,
    30
]

for sample_number in sample_numbers:

    print(sample_number)

else:

    print("Loop completed successfully.")


# =============================================================================
# Example 2: Search for a Number
# =============================================================================

search_numbers: list[int] = [
    10,
    20,
    30,
    40
]

SEARCH_TARGET_NUMBER: int = 30

for candidate_number in search_numbers:

    if candidate_number == SEARCH_TARGET_NUMBER:

        print(f"Found {SEARCH_TARGET_NUMBER}.")
        break

else:

    print("Target number not found.")


# =============================================================================
# Example 3: Search for an Employee
# =============================================================================

employee_directory: list[str] = [
    "Alice",
    "Bob",
    "Charlie"
]

SEARCH_TARGET_EMPLOYEE: str = "David"

for employee_name in employee_directory:

    if employee_name == SEARCH_TARGET_EMPLOYEE:

        print(f"Employee found -> {employee_name}")
        break

else:

    print("Employee not found.")


# =============================================================================
# Example 4: while-else Without break
# =============================================================================

while_counter: int = 1

WHILE_LOOP_LIMIT: int = 5

while while_counter <= WHILE_LOOP_LIMIT:

    print(f"Counter -> {while_counter}")

    while_counter += 1

else:

    print("While loop completed successfully.")


# =============================================================================
# Example 5: Prime Number Check
# =============================================================================

PRIME_CANDIDATE_NUMBER: int = 17

for possible_divisor in range(2, PRIME_CANDIDATE_NUMBER):

    if PRIME_CANDIDATE_NUMBER % possible_divisor == 0:

        print(f"{PRIME_CANDIDATE_NUMBER} is not a prime number.")
        break

else:

    print(f"{PRIME_CANDIDATE_NUMBER} is a prime number.")


# =============================================================================
# Example 6: User Authentication Search
# =============================================================================

registered_users: list[str] = [
    "Alice",
    "Bob",
    "Charlie"
]

LOGIN_USERNAME: str = "Eve"

for registered_user in registered_users:

    if registered_user == LOGIN_USERNAME:

        print("Login successful.")
        break

else:

    print("User account not found.")


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Loop else executes only when the loop completes normally.

✓ Executing `break` prevents the else block from running.

✓ Works with both `for` and `while` loops.

✓ Most commonly used for searching operations.

✓ Improves readability by removing the need for additional flags.

✓ Loop else is unique to Python and is often overlooked by beginners.
"""


# =============================================================================
# End of File
# =============================================================================