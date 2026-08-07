"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
range() Function

Overview
--------
The `range()` function generates an immutable sequence of integers.

It is most commonly used with `for` loops when a block of code needs to
execute a fixed number of times.

Unlike lists, a `range` object generates values lazily (on demand), making
it memory efficient even for very large ranges.

Syntax
------
range(stop)

range(start, stop)

range(start, stop, step)

Flow
----
Create range Object
        │
        ▼
Generate Next Value
        │
        ▼
Value Available?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
 ▼      ▼
Execute End Loop
Iteration

Characteristics
---------------
• Generates integer sequences.
• Start value is inclusive.
• Stop value is exclusive.
• Supports positive and negative step values.
• Memory efficient (lazy evaluation).
• Frequently used with `for` loops.

Time Complexity
---------------
Creating a range object:
O(1)

Iterating through n values:
O(n)

Common Use Cases
----------------
• Repeating tasks a fixed number of times.
• Iterating over indexes.
• Counting.
• Reverse iteration.
• Numerical sequence generation.

Best Practices
--------------
• Prefer `range()` over manually incrementing counters.
• Use descriptive constants instead of magic numbers.
• Remember that the stop value is excluded.

Common Mistakes
---------------
• Forgetting that the stop value is not included.
• Using a step value of zero (raises ValueError).
• Confusing a range object with a list.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#range
"""


# =============================================================================
# Example 1: range(stop)
# =============================================================================

STOP_VALUE: int = 5

for generated_number in range(STOP_VALUE):

    print(generated_number)


# =============================================================================
# Example 2: range(start, stop)
# =============================================================================

START_VALUE: int = 5
END_VALUE: int = 10

for current_number in range(START_VALUE, END_VALUE):

    print(current_number)


# =============================================================================
# Example 3: range(start, stop, step)
# =============================================================================

EVEN_NUMBER_START: int = 2
EVEN_NUMBER_STOP: int = 12
EVEN_NUMBER_STEP: int = 2

for even_number in range(
    EVEN_NUMBER_START,
    EVEN_NUMBER_STOP,
    EVEN_NUMBER_STEP
):

    print(even_number)


# =============================================================================
# Example 4: Reverse Iteration
# =============================================================================

COUNTDOWN_START: int = 5
COUNTDOWN_STOP: int = 0
COUNTDOWN_STEP: int = -1

for countdown_value in range(
    COUNTDOWN_START,
    COUNTDOWN_STOP,
    COUNTDOWN_STEP
):

    print(countdown_value)


# =============================================================================
# Example 5: Multiplication Table
# =============================================================================

TABLE_NUMBER: int = 7
TABLE_LIMIT: int = 10

for multiplier in range(1, TABLE_LIMIT + 1):

    print(
        f"{TABLE_NUMBER} × {multiplier}"
        f" = {TABLE_NUMBER * multiplier}"
    )


# =============================================================================
# Example 6: Convert range to List
# =============================================================================

LIST_RANGE_START: int = 1
LIST_RANGE_STOP: int = 6

generated_numbers: list[int] = list(
    range(
        LIST_RANGE_START,
        LIST_RANGE_STOP
    )
)

print(generated_numbers)


# =============================================================================
# Example 7: Character Positions
# =============================================================================

sample_text: str = "Python"

for character_index in range(len(sample_text)):

    print(
        f"Index: {character_index}"
        f" -> Character: {sample_text[character_index]}"
    )


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ range() generates integer sequences.

✓ The stop value is excluded.

✓ Supports start, stop and step parameters.

✓ A range object is memory efficient.

✓ Commonly used with for loops.

✓ Can iterate forwards or backwards.

✓ Can be converted into a list when needed.
"""


# =============================================================================
# End of File
# =============================================================================