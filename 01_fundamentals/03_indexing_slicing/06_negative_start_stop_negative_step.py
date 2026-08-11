"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Negative Start, Negative Stop, and Negative Step

Overview
--------
Python slicing uses three components:

    sequence[start:stop:step]

This module focuses on:

    start < 0
    stop  < 0
    step  < 0

Negative indexes identify positions relative to the end of a sequence.

A negative step moves through the sequence from right to left.

Syntax
------
    sequence[negative_start:negative_stop:negative_step]

Example
-------
For:

    values = [10, 20, 30, 40, 50, 60]

the indexes are:

    Positive:   0    1    2    3    4    5
               10   20   30   40   50   60

    Negative:  -6   -5   -4   -3   -2   -1
               10   20   30   40   50   60

Consider:

    values[-1:-5:-2]

The corresponding positions are:

    -1 -> index 5
    -3 -> index 3

Therefore:

    [60, 40]

Rules
-----
• Negative indexes count from the end of the sequence.
• A negative step moves from right to left.
• The stop index remains excluded.
• The start position normally needs to be after the stop position in the
  direction of movement.
• Negative indexes and negative steps are separate concepts.

Important
---------
The sign of an index determines how the position is identified.

The sign of the step determines the direction of traversal.

Therefore:

    negative start
    negative stop
    negative step

means:

    identify boundaries from the end
    and move backward through the sequence.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: Basic Negative Start, Stop, and Step
# =============================================================================

negative_slice_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

basic_negative_slice_result: list[int] = (
    negative_slice_values[-1:-5:-1]
)

print(
    f"Original values: {negative_slice_values}"
)

print(
    f"Sliced values:   {basic_negative_slice_result}"
)


# Negative indexes:
#
# -6 -> 10
# -5 -> 20
# -4 -> 30
# -3 -> 40
# -2 -> 50
# -1 -> 60
#
# Movement:
#
# -1 -> -2 -> -3 -> -4
#
# Stop -5 is excluded.
#
# Result:
#
# [60, 50, 40, 30]


# =============================================================================
# Example 2: Negative Step of -2
# =============================================================================

negative_step_two_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

negative_step_two_result: list[int] = (
    negative_step_two_values[-1:-7:-2]
)

print(
    f"Original values: {negative_step_two_values}"
)

print(
    f"Sliced values:   {negative_step_two_result}"
)


# Movement:
#
# -1 -> -3 -> -5
#
# Stop -7 is excluded.
#
# Result:
#
# [70, 50, 30]


# =============================================================================
# Example 3: Negative Step of -3
# =============================================================================

negative_step_three_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

negative_step_three_result: list[int] = (
    negative_step_three_values[-1:-8:-3]
)

print(
    f"Original values: {negative_step_three_values}"
)

print(
    f"Sliced values:   {negative_step_three_result}"
)


# Movement:
#
# -1 -> -4 -> -7
#
# Result:
#
# [80, 50, 20]


# =============================================================================
# Example 4: Different Negative Boundaries
# =============================================================================

different_negative_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

different_negative_result: list[int] = (
    different_negative_boundaries[-2:-7:-1]
)

print(
    f"Original values: {different_negative_boundaries}"
)

print(
    f"Sliced values:   {different_negative_result}"
)


# Movement:
#
# -2 -> -3 -> -4 -> -5 -> -6
#
# Stop -7 is excluded.
#
# Result:
#
# [70, 60, 50, 40, 30]


# =============================================================================
# Example 5: Negative Boundaries with a String
# =============================================================================

negative_slice_word: str = "PythonProgramming"

negative_slice_word_result: str = (
    negative_slice_word[-1:-8:-1]
)

print(
    f"Original string: {negative_slice_word}"
)

print(
    f"Sliced string:   {negative_slice_word_result}"
)


# The slice begins at the final character and moves backward.
#
# The same slicing rules apply to strings.


# =============================================================================
# Example 6: Negative Boundaries with a Tuple
# =============================================================================

negative_slice_languages: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
    "Kafka",
    "Docker",
    "Linux"
)

negative_slice_tuple_result: tuple[str, ...] = (
    negative_slice_languages[-1:-6:-2]
)

print(
    f"Original tuple: {negative_slice_languages}"
)

print(
    f"Sliced tuple:   {negative_slice_tuple_result}"
)


# Movement:
#
# -1 -> -3 -> -5
#
# Result:
#
# ("Linux", "Kafka", "Spark")


# =============================================================================
# Example 7: Negative Start and Stop Do Not Automatically Reverse Anything
# =============================================================================

negative_boundary_direction_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

negative_boundary_direction_result: list[int] = (
    negative_boundary_direction_values[-5:-1:-1]
)

print(
    f"Original values: {negative_boundary_direction_values}"
)

print(
    f"Result:           {negative_boundary_direction_result}"
)


# Here:
#
# start = -5 -> positive index 1
# stop  = -1 -> positive index 5
# step  = -1
#
# A negative step moves toward smaller indexes.
#
# Starting at index 1, Python cannot move toward index 5.
#
# Therefore:
#
# []


# =============================================================================
# Example 8: Equal Negative Boundaries
# =============================================================================

equal_negative_slice_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

equal_negative_slice_result: list[int] = (
    equal_negative_slice_values[-2:-2:-1]
)

print(
    f"Original values: {equal_negative_slice_values}"
)

print(
    f"Result:           {equal_negative_slice_result}"
)


# start and stop identify the same position.
#
# Therefore no elements are selected.
#
# Result:
#
# []


# =============================================================================
# Example 9: Complete Reverse with Negative Indexes
# =============================================================================

reverse_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

complete_reverse_result: list[int] = (
    reverse_values[-1:-6:-1]
)

print(
    f"Original values: {reverse_values}"
)

print(
    f"Reversed values: {complete_reverse_result}"
)


# Movement:
#
# -1 -> -2 -> -3 -> -4 -> -5
#
# Stop -6 is excluded.
#
# Result:
#
# [50, 40, 30, 20, 10]


# =============================================================================
# Example 10: The [::-1] Reverse Shortcut
# =============================================================================

reverse_shortcut_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

reverse_shortcut_result: list[int] = (
    reverse_shortcut_values[::-1]
)

print(
    f"Original values: {reverse_shortcut_values}"
)

print(
    f"Reversed values: {reverse_shortcut_result}"
)


# [::-1] means:
#
# start -> omitted
# stop  -> omitted
# step  -> -1
#
# For a negative step:
#
# omitted start -> beginning from the end
# omitted stop  -> continue toward the beginning
#
# Result:
#
# [50, 40, 30, 20, 10]


# =============================================================================
# Example 11: Explicit Negative Boundaries vs Reverse Shortcut
# =============================================================================

comparison_reverse_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

explicit_negative_reverse: list[int] = (
    comparison_reverse_values[-1:-6:-1]
)

shortcut_negative_reverse: list[int] = (
    comparison_reverse_values[::-1]
)

print(
    f"Explicit reverse: {explicit_negative_reverse}"
)

print(
    f"Shortcut reverse: {shortcut_negative_reverse}"
)


# Both produce:
#
# [50, 40, 30, 20, 10]
#
# The explicit form provides negative start and stop boundaries.
#
# The shortcut omits both boundaries and specifies only a negative step.


# =============================================================================
# Example 12: Negative Step with Different Negative Boundaries
# =============================================================================

final_negative_slice_values: list[int] = [
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800
]

final_negative_slice_result: list[int] = (
    final_negative_slice_values[-2:-7:-2]
)

print(
    f"Original values: {final_negative_slice_values}"
)

print(
    f"Sliced values:   {final_negative_slice_result}"
)


# Movement:
#
# -2 -> -4 -> -6
#
# Corresponding values:
#
# 700 -> 500 -> 300
#
# Result:
#
# [700, 500, 300]


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ This module uses:

      negative start
      negative stop
      negative step

✓ Negative indexes identify positions from the end.

✓ A negative step moves from right to left.

✓ The stop index remains excluded.

✓ Example:

      sequence[-1:-5:-1]

  selects:

      -1 -> -2 -> -3 -> -4

✓ Negative indexes do not control direction.

✓ The negative step controls direction.

✓ Example:

      sequence[-5:-1:-1]

  is empty because the starting position is to the left of the stopping
  position while the step requires movement toward the left.

✓ `[::-1]` is the standard Python slicing expression for reversing a
  sequence.

✓ `sequence[-1:-6:-1]` explicitly specifies negative start and stop
  boundaries for a complete reverse.

✓ `sequence[::-1]` achieves the same reverse by omitting both boundaries.

✓ This completes the four fundamental start/stop/step combinations.
"""
"""
06_negative_start_stop_negative_step
        -       -       -
        │       │       │
      start   stop    step
        │       │       │
        └───────┴───────┴──←
"""

# =============================================================================
# End of File
# =============================================================================