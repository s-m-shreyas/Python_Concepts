"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Positive Start, Positive Stop, and Positive Step

Overview
--------
Python slicing allows a sequence to be accessed using three boundaries:

    sequence[start:stop:step]

This module focuses on the combination where:

    start > 0
    stop  > 0
    step  > 0

A positive step moves through the sequence from left to right.

Syntax
------
    sequence[start:stop:step]

Rules
-----
• The start index is included.
• The stop index is excluded.
• A positive step moves toward larger indexes.
• The step determines the distance between selected indexes.
• All three slicing components are explicitly specified in this module.

Example
-------
    numbers = [10, 20, 30, 40, 50, 60]

    numbers[1:5:2]

Selected indexes:

    1 -> 3

Result:

    [20, 40]

Index Representation
--------------------
For:

    values = [10, 20, 30, 40, 50, 60]

the indexes are:

    Index:      0    1    2    3    4    5
    Value:     10   20   30   40   50   60

The expression:

    values[1:5:2]

means:

    Start at index 1
    Move by +2
    Stop before index 5

Therefore:

    1 -> 3

Result:

    [20, 40]

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: Basic Positive Slicing
# =============================================================================

positive_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

positive_slice_result: list[int] = positive_sequence[1:5:1]

print(
    f"Original sequence: {positive_sequence}"
)

print(
    f"Sliced sequence:   {positive_slice_result}"
)


# Index movement:
#
# 1 -> 2 -> 3 -> 4
#
# Index 5 is excluded.
#
# Result:
#
# [20, 30, 40, 50]


# =============================================================================
# Example 2: Positive Step of 2
# =============================================================================

step_two_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

step_two_result: list[int] = step_two_sequence[1:5:2]

print(
    f"Original sequence: {step_two_sequence}"
)

print(
    f"Step of +2:        {step_two_result}"
)


# Index movement:
#
# 1 -> 3
#
# Index 5 is excluded.
#
# Result:
#
# [20, 40]


# =============================================================================
# Example 3: Positive Step of 3
# =============================================================================

step_three_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

step_three_result: list[int] = step_three_sequence[1:8:3]

print(
    f"Original sequence: {step_three_sequence}"
)

print(
    f"Step of +3:        {step_three_result}"
)


# Index movement:
#
# 1 -> 4 -> 7
#
# Result:
#
# [20, 50, 80]


# =============================================================================
# Example 4: Start at a Different Positive Index
# =============================================================================

different_start_sequence: list[int] = [
    100,
    200,
    300,
    400,
    500,
    600,
    700
]

different_start_result: list[int] = (
    different_start_sequence[2:7:2]
)

print(
    f"Original sequence: {different_start_sequence}"
)

print(
    f"Different start:   {different_start_result}"
)


# Index movement:
#
# 2 -> 4 -> 6
#
# Result:
#
# [300, 500, 700]


# =============================================================================
# Example 5: Changing the Stop Boundary
# =============================================================================

stop_boundary_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

short_stop_result: list[int] = (
    stop_boundary_sequence[1:5:1]
)

long_stop_result: list[int] = (
    stop_boundary_sequence[1:8:1]
)

print(
    f"Stop at index 5: {short_stop_result}"
)

print(
    f"Stop at index 8: {long_stop_result}"
)


# The start remains the same.
#
# Only the stop boundary changes.


# =============================================================================
# Example 6: Start and Stop Determine the Range
# =============================================================================

range_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

range_result: list[int] = range_sequence[2:6:1]

print(
    f"Original sequence: {range_sequence}"
)

print(
    f"Selected range:    {range_result}"
)


# Index movement:
#
# 2 -> 3 -> 4 -> 5
#
# Index 6 is excluded.
#
# Result:
#
# [30, 40, 50, 60]


# =============================================================================
# Example 7: Step Controls the Distance Between Indexes
# =============================================================================

step_comparison_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

step_one_comparison: list[int] = (
    step_comparison_sequence[1:7:1]
)

step_two_comparison: list[int] = (
    step_comparison_sequence[1:7:2]
)

step_three_comparison: list[int] = (
    step_comparison_sequence[1:7:3]
)

print(
    f"Step +1: {step_one_comparison}"
)

print(
    f"Step +2: {step_two_comparison}"
)

print(
    f"Step +3: {step_three_comparison}"
)


# Notice that the start and stop remain unchanged.
#
# Only the step changes the distance between selected indexes.


# =============================================================================
# Example 8: Positive Slicing with a String
# =============================================================================

python_word: str = "PythonProgramming"

python_word_slice: str = python_word[1:10:2]

print(
    f"Original string: {python_word}"
)

print(
    f"Sliced string:   {python_word_slice}"
)


# The same slicing rules apply to strings:
#
# start  -> positive
# stop   -> positive
# step   -> positive


# =============================================================================
# Example 9: Positive Slicing with a Tuple
# =============================================================================

language_sequence: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
    "Kafka",
    "Docker"
)

language_slice: tuple[str, ...] = language_sequence[1:6:2]

print(
    f"Original tuple: {language_sequence}"
)

print(
    f"Sliced tuple:   {language_slice}"
)


# Index movement:
#
# 1 -> 3 -> 5
#
# Result:
#
# ("SQL", "Airflow", "Docker")


# =============================================================================
# Example 10: Start Greater Than Zero but Stop Before the End
# =============================================================================

partial_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90
]

partial_result: list[int] = partial_sequence[3:8:2]

print(
    f"Original sequence: {partial_sequence}"
)

print(
    f"Partial slice:     {partial_result}"
)


# Index movement:
#
# 3 -> 5 -> 7
#
# Result:
#
# [40, 60, 80]


# =============================================================================
# Example 11: Start and Stop Can Produce an Empty Slice
# =============================================================================

empty_range_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50
]

empty_range_result: list[int] = empty_range_sequence[3:3:1]

print(
    f"Original sequence: {empty_range_sequence}"
)

print(
    f"Empty slice:       {empty_range_result}"
)


# start = 3
# stop  = 3
#
# Since the stop boundary is excluded and both boundaries are identical,
# there are no indexes to select.
#
# Result:
#
# []


# =============================================================================
# Example 12: Start Greater Than Stop with a Positive Step
# =============================================================================

invalid_direction_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50
]

invalid_direction_result: list[int] = (
    invalid_direction_sequence[4:1:1]
)

print(
    f"Original sequence: {invalid_direction_sequence}"
)

print(
    f"Result:            {invalid_direction_result}"
)


# start = 4
# stop  = 1
# step  = +1
#
# A positive step moves:
#
# 4 -> 5 -> 6 -> ...
#
# It cannot move toward index 1.
#
# Therefore the result is empty.
#
# A negative step is required to move from a higher index toward
# a lower index.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ This module uses positive start, positive stop, and positive step.

✓ The syntax is:

      sequence[start:stop:step]

✓ Positive step means movement from left to right.

✓ The start index is included.

✓ The stop index is excluded.

✓ The step controls the distance between selected indexes.

✓ Example:

      sequence[1:6:2]

  selects:

      1 -> 3 -> 5

✓ A positive step cannot move from a higher start index toward a lower
  stop index.

✓ Negative step combinations are covered in the next modules.

✓ Negative indexes are intentionally not used in this module.
"""
"""
03_positive_start_stop_positive_step
        +       +       +
        │       │       │
      start   stop    step
        │       │       │
        └───────┴───────┴──→
"""


# =============================================================================
# End of File
# =============================================================================