"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
Pass Statement

Overview
--------
The `pass` statement is a null operation in Python. When executed, it performs
no action.

It is commonly used as a placeholder where Python syntax requires a statement,
but no implementation is currently needed.

Unlike `break` and `continue`, the `pass` statement does not affect loop
execution. Control simply moves to the next statement.

Syntax
------
pass

Flow
----
Execute pass
      │
      ▼
Do Nothing
      │
      ▼
Continue Program Execution

Characteristics
---------------
• Performs no operation.
• Used as a placeholder.
• Does not terminate a loop.
• Does not skip an iteration.
• Commonly used during development.

Time Complexity
---------------
O(1)

Common Use Cases
----------------
• Creating placeholder functions.
• Creating placeholder classes.
• Placeholder loop bodies.
• Placeholder conditional blocks.
• Incremental software development.

Best Practices
--------------
• Use `pass` only temporarily unless intentionally creating an empty block.
• Replace placeholder implementations as development progresses.
• Prefer meaningful implementations whenever possible.

Common Mistakes
---------------
• Confusing `pass` with `continue`.
• Assuming `pass` skips an iteration.
• Leaving unnecessary `pass` statements in completed code.

References
----------
Python Official Documentation

https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement
"""


# =============================================================================
# Example 1: Empty Loop Body
# =============================================================================

for number in range(5):

    pass

print("Loop completed.")


# =============================================================================
# Example 2: Empty Conditional Block
# =============================================================================

temperature: int = 35

if temperature > 40:

    pass

print("Program continues normally.")


# =============================================================================
# Example 3: Placeholder Function
# =============================================================================

def calculate_salary() -> None:

    pass


print("Function declared successfully.")


# =============================================================================
# Example 4: Placeholder Class
# =============================================================================

class Employee:

    pass


employee: Employee = Employee()

print(f"Object Created -> {employee}")


# =============================================================================
# Example 5: pass Does NOT Skip an Iteration
# =============================================================================

for number in range(1, 6):

    if number == 3:

        pass

    print(number)


# =============================================================================
# Example 6: pass Inside a While Loop
# =============================================================================

counter: int = 1

while counter <= 3:

    pass

    print(counter)

    counter += 1


# =============================================================================
# End of File
# =============================================================================