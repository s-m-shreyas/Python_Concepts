"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Positive Start, Positive Stop, and Negative Step

Overview
--------
Python slicing uses three components:

    sequence[start:stop:step]

This module focuses on:

    start > 0
    stop  > 0
    step  < 0

A negative step moves through the sequence from right to left.

Syntax
------
    sequence[start:stop:negative_step]

Rules
-----
• The start index is included when it lies within the slicing direction.
• The stop index is excluded.
• A negative step moves toward smaller indexes.
• The step determines how far Python moves between selected indexes.
• The start position must normally be greater than the stop position when
  using a negative step.

Important
---------
The sign of the step determines the direction of movement.

For example:

    sequence[5:1:-1]

means:

    Start at index 5.
    Move backward by 1.
    Stop before index 1.

Selected indexes:

    5 -> 4 -> 3 -> 2

The result is therefore:

    [value_at_5, value_at_4, value_at_3, value_at_2]

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: Basic Negative Step
# =============================================================================

positive_boundary_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

basic_negative_step_result: list[int] = (
    positive_boundary_sequence[5:1:-1]
)

print(
    f"Original sequence: {positive_boundary_sequence}"
)

print(
    f"Sliced sequence:   {basic_negative_step_result}"
)


# Index movement:
#
# 5 -> 4 -> 3 -> 2
#
# Index 1 is excluded.
#
# Result:
#
# [60, 50, 40, 30]


# =============================================================================
# Example 2: Negative Step of -2
# =============================================================================

negative_two_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

negative_two_result: list[int] = (
    negative_two_sequence[6:1:-2]
)

print(
    f"Original sequence: {negative_two_sequence}"
)

print(
    f"Sliced sequence:   {negative_two_result}"
)


# Index movement:
#
# 6 -> 4 -> 2
#
# Index 1 is excluded.
#
# Result:
#
# [70, 50, 30]


# =============================================================================
# Example 3: Negative Step of -3
# =============================================================================

negative_three_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

negative_three_result: list[int] = (
    negative_three_sequence[7:1:-3]
)

print(
    f"Original sequence: {negative_three_sequence}"
)

print(
    f"Sliced sequence:   {negative_three_result}"
)


# Index movement:
#
# 7 -> 4
#
# Index 1 is excluded.
#
# Result:
#
# [80, 50]


# =============================================================================
# Example 4: Changing Only the Step
# =============================================================================

step_comparison_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

negative_step_one_result: list[int] = (
    step_comparison_values[6:1:-1]
)

negative_step_two_result: list[int] = (
    step_comparison_values[6:1:-2]
)

negative_step_three_result: list[int] = (
    step_comparison_values[6:1:-3]
)

print(
    f"Step -1: {negative_step_one_result}"
)

print(
    f"Step -2: {negative_step_two_result}"
)

print(
    f"Step -3: {negative_step_three_result}"
)


# The start and stop remain unchanged.
#
# Only the step changes the distance between indexes.


# =============================================================================
# Example 5: Different Positive Start and Stop
# =============================================================================

bounded_reverse_sequence: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

bounded_reverse_result: list[int] = (
    bounded_reverse_sequence[6:2:-1]
)

print(
    f"Original sequence: {bounded_reverse_sequence}"
)

print(
    f"Sliced sequence:   {bounded_reverse_result}"
)


# Index movement:
#
# 6 -> 5 -> 4 -> 3
#
# Index 2 is excluded.
#
# Result:
#
# [70, 60, 50, 40]


# =============================================================================
# Example 6: Negative Step with a String
# =============================================================================

positive_index_string: str = "Python"

positive_index_string_result: str = (
    positive_index_string[5:1:-1]
)

print(
    f"Original string: {positive_index_string}"
)

print(
    f"Sliced string:   {positive_index_string_result}"
)


# Index movement:
#
# 5 -> 4 -> 3 -> 2
#
# Characters:
#
# 5 -> n
# 4 -> o
# 3 -> h
# 2 -> t
#
# Result:
#
# "noht"


# =============================================================================
# Example 7: Negative Step with a Tuple
# =============================================================================

positive_boundary_tuple: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
    "Kafka",
    "Docker"
)

positive_boundary_tuple_result: tuple[str, ...] = (
    positive_boundary_tuple[5:1:-1]
)

print(
    f"Original tuple: {positive_boundary_tuple}"
)

print(
    f"Sliced tuple:   {positive_boundary_tuple_result}"
)


# Index movement:
#
# 5 -> 4 -> 3 -> 2
#
# Result:
#
# ("Docker", "Kafka", "Airflow", "Spark")


# =============================================================================
# Example 8: Start and Stop Determine the Directional Range
# =============================================================================

directional_values: list[int] = [
    100,
    200,
    300,
    400,
    500,
    600,
    700
]

directional_result: list[int] = directional_values[5:2:-1]

print(
    f"Original values: {directional_values}"
)

print(
    f"Directional slice: {directional_result}"
)


# Movement:
#
# 5 -> 4 -> 3
#
# Index 2 is excluded.
#
# Result:
#
# [600, 500, 400]


# =============================================================================
# Example 9: Start Less Than Stop with a Negative Step
# =============================================================================

invalid_direction_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

invalid_direction_result: list[int] = (
    invalid_direction_values[1:5:-1]
)

print(
    f"Original values: {invalid_direction_values}"
)

print(
    f"Result:          {invalid_direction_result}"
)


# start = 1
# stop  = 5
# step  = -1
#
# A negative step moves:
#
# 1 -> 0 -> -1 -> ...
#
# It cannot move toward index 5.
#
# Therefore the result is empty.
#
# The direction of start and stop must agree with the sign of the step.


# =============================================================================
# Example 10: Equal Start and Stop
# =============================================================================

equal_boundary_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

equal_boundary_result: list[int] = (
    equal_boundary_values[3:3:-1]
)

print(
    f"Original values: {equal_boundary_values}"
)

print(
    f"Result:          {equal_boundary_result}"
)


# start = 3
# stop  = 3
#
# There is no movement because the starting and stopping boundaries
# are identical.
#
# Therefore the result is empty.


# =============================================================================
# Example 11: Negative Step Does Not Mean Negative Indexes
# =============================================================================

positive_only_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50
]

negative_step_only_result: list[int] = (
    positive_only_boundaries[4:1:-1]
)

print(
    f"Original values: {positive_only_boundaries}"
)

print(
    f"Result:           {negative_step_only_result}"
)


# Notice:
#
# start = 4  -> positive index
# stop  = 1  -> positive index
# step  = -1 -> negative step
#
# Therefore negative-step slicing does NOT require negative indexes.
#
# Negative indexes are covered separately in the next combinations.


# =============================================================================
# Example 12: Explicit Reverse of a Positive Range
# =============================================================================

ordered_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

explicit_reverse_result: list[int] = (
    ordered_values[5:1:-1]
)

print(
    f"Original values: {ordered_values}"
)

print(
    f"Reversed range:  {explicit_reverse_result}"
)


# This reverses only the selected range:
#
# Indexes:
#
# 5 -> 4 -> 3 -> 2
#
# It does NOT include:
#
# index 1
# index 0


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ This module uses:

      positive start
      positive stop
      negative step

✓ The syntax is:

      sequence[start:stop:negative_step]

✓ A negative step moves from right to left.

✓ The stop index is excluded.

✓ Example:

      sequence[5:1:-1]

  selects:

      5 -> 4 -> 3 -> 2

✓ A negative step does NOT mean that the start and stop indexes must
  themselves be negative.

✓ The direction of start and stop must agree with the direction implied
  by the step.

✓ With a negative step:

      start > stop

  is normally required for a non-empty slice.

✓ A negative step can be -1, -2, -3, and so on.

✓ Negative indexes are intentionally not used in this module.

✓ Negative start and stop indexes are covered in the next modules.
"""
"""
04_positive_start_stop_negative_step
        +       +       -
        │       │       │
      start   stop    step
        │       │       │
        └───────┴───────┴──←
"""

# =============================================================================
# End of File
# =============================================================================