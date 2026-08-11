"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Negative Start, Negative Stop, and Positive Step

Overview
--------
Python slicing uses three components:

    sequence[start:stop:step]

This module focuses on:

    start < 0
    stop  < 0
    step  > 0

Negative indexes identify positions relative to the end of a sequence.

A positive step moves through the sequence from left to right.

Syntax
------
    sequence[negative_start:negative_stop:positive_step]

Negative Index Reference
------------------------
For:

    values = [10, 20, 30, 40, 50, 60]

the indexes are:

    Positive:   0    1    2    3    4    5
               10   20   30   40   50   60

    Negative:  -6   -5   -4   -3   -2   -1
               10   20   30   40   50   60

Example
-------
    values[-5:-1:2]

The negative boundaries correspond to:

    -5 -> index 1
    -1 -> index 5

The positive step moves:

    1 -> 3

The stop boundary is excluded.

Result:

    [20, 40]

Important
---------
Negative indexes determine WHERE the slice begins and ends.

The positive step determines HOW the slice moves.

Therefore:

    negative start
    negative stop
    positive step

still produces a left-to-right slice.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: Basic Negative Start and Stop
# =============================================================================

negative_boundary_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

basic_negative_boundary_result: list[int] = (
    negative_boundary_values[-5:-1:1]
)

print(
    f"Original values: {negative_boundary_values}"
)

print(
    f"Sliced values:   {basic_negative_boundary_result}"
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
# Slice:
#
# [-5:-1:1]
#
# Corresponding positive indexes:
#
# 1 -> 2 -> 3 -> 4
#
# Index -1 / positive index 5 is excluded.
#
# Result:
#
# [20, 30, 40, 50]


# =============================================================================
# Example 2: Negative Boundaries with a Positive Step of 2
# =============================================================================

step_two_negative_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

step_two_negative_result: list[int] = (
    step_two_negative_boundaries[-6:-1:2]
)

print(
    f"Original values: {step_two_negative_boundaries}"
)

print(
    f"Sliced values:   {step_two_negative_result}"
)


# Negative boundaries:
#
# -6 -> positive index 1
# -1 -> positive index 6
#
# Movement with +2:
#
# 1 -> 3 -> 5
#
# Result:
#
# [20, 40, 60]


# =============================================================================
# Example 3: Negative Boundaries with a Positive Step of 3
# =============================================================================

step_three_negative_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

step_three_negative_result: list[int] = (
    step_three_negative_boundaries[-7:-1:3]
)

print(
    f"Original values: {step_three_negative_boundaries}"
)

print(
    f"Sliced values:   {step_three_negative_result}"
)


# Negative boundaries:
#
# -7 -> positive index 1
# -1 -> positive index 7
#
# Movement:
#
# 1 -> 4
#
# Result:
#
# [20, 50]


# =============================================================================
# Example 4: Changing Only the Step
# =============================================================================

step_comparison_negative_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

negative_boundary_step_one: list[int] = (
    step_comparison_negative_boundaries[-7:-1:1]
)

negative_boundary_step_two: list[int] = (
    step_comparison_negative_boundaries[-7:-1:2]
)

negative_boundary_step_three: list[int] = (
    step_comparison_negative_boundaries[-7:-1:3]
)

print(
    f"Step +1: {negative_boundary_step_one}"
)

print(
    f"Step +2: {negative_boundary_step_two}"
)

print(
    f"Step +3: {negative_boundary_step_three}"
)


# The negative start and stop remain unchanged.
#
# Only the positive step changes the distance between selected indexes.


# =============================================================================
# Example 5: Different Negative Start and Stop
# =============================================================================

different_negative_boundaries: list[int] = [
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800
]

different_negative_result: list[int] = (
    different_negative_boundaries[-7:-2:2]
)

print(
    f"Original values: {different_negative_boundaries}"
)

print(
    f"Sliced values:   {different_negative_result}"
)


# Negative indexes:
#
# -8 -> 100
# -7 -> 200
# -6 -> 300
# -5 -> 400
# -4 -> 500
# -3 -> 600
# -2 -> 700
# -1 -> 800
#
# Slice:
#
# [-7:-2:2]
#
# Corresponding positive indexes:
#
# 1 -> 3 -> 5
#
# Result:
#
# [200, 400, 600]


# =============================================================================
# Example 6: Negative Boundaries with a String
# =============================================================================

negative_boundary_string: str = "PythonProgramming"

negative_string_result: str = (
    negative_boundary_string[-10:-2:2]
)

print(
    f"Original string: {negative_boundary_string}"
)

print(
    f"Sliced string:   {negative_string_result}"
)


# Negative start and stop are interpreted relative to the end.
#
# The positive step still moves from left to right.


# =============================================================================
# Example 7: Negative Boundaries with a Tuple
# =============================================================================

negative_boundary_languages: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
    "Kafka",
    "Docker",
    "Linux"
)

negative_boundary_tuple_result: tuple[str, ...] = (
    negative_boundary_languages[-6:-1:2]
)

print(
    f"Original tuple: {negative_boundary_languages}"
)

print(
    f"Sliced tuple:   {negative_boundary_tuple_result}"
)


# Negative indexes:
#
# -7 -> Python
# -6 -> SQL
# -5 -> Spark
# -4 -> Airflow
# -3 -> Kafka
# -2 -> Docker
# -1 -> Linux
#
# Slice:
#
# [-6:-1:2]
#
# Positive indexes:
#
# 1 -> 3 -> 5
#
# Result:
#
# ("SQL", "Airflow", "Docker")


# =============================================================================
# Example 8: Negative Boundaries Do Not Reverse the Sequence
# =============================================================================

negative_boundary_ordered_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

negative_boundary_forward_result: list[int] = (
    negative_boundary_ordered_values[-5:-1:1]
)

print(
    f"Original values: {negative_boundary_ordered_values}"
)

print(
    f"Sliced values:   {negative_boundary_forward_result}"
)


# Even though start and stop are negative:
#
# -5 -> -4 -> -3 -> -2
#
# the sequence still moves from left to right.
#
# Negative indexes do NOT mean reverse traversal.
#
# The positive step controls the direction.


# =============================================================================
# Example 9: Negative Start Greater Than Negative Stop
# =============================================================================

invalid_negative_boundary_values: list[int] = [
    10,
    20,
    30,
    40,
    50
]

invalid_negative_boundary_result: list[int] = (
    invalid_negative_boundary_values[-2:-4:1]
)

print(
    f"Original values: {invalid_negative_boundary_values}"
)

print(
    f"Result:           {invalid_negative_boundary_result}"
)


# Here:
#
# start = -2
# stop  = -4
# step  = +1
#
# Converted positions:
#
# -2 -> positive index 3
# -4 -> positive index 1
#
# A positive step moves toward larger indexes:
#
# 3 -> 4 -> ...
#
# It cannot move toward index 1.
#
# Therefore the result is empty.


# =============================================================================
# Example 10: Equal Negative Start and Stop
# =============================================================================

equal_negative_boundaries: list[int] = [
    10,
    20,
    30,
    40,
    50
]

equal_negative_result: list[int] = (
    equal_negative_boundaries[-2:-2:1]
)

print(
    f"Original values: {equal_negative_boundaries}"
)

print(
    f"Result:          {equal_negative_result}"
)


# start and stop refer to the same position.
#
# Therefore there is nothing to select.
#
# Result:
#
# []


# =============================================================================
# Example 11: Negative Indexes Identify Boundaries
# =============================================================================

boundary_reference_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

boundary_reference_result: list[int] = (
    boundary_reference_values[-4:-1:1]
)

print(
    f"Original values: {boundary_reference_values}"
)

print(
    f"Sliced values:   {boundary_reference_result}"
)


# Boundary conversion:
#
# -4 -> positive index 2
# -1 -> positive index 5
#
# Positive step:
#
# 2 -> 3 -> 4
#
# Stop index 5 is excluded.
#
# Result:
#
# [30, 40, 50]


# =============================================================================
# Example 12: Comparing Equivalent Positive and Negative Boundaries
# =============================================================================

equivalent_boundary_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60
]

positive_boundary_slice: list[int] = (
    equivalent_boundary_values[1:5:2]
)

negative_boundary_slice: list[int] = (
    equivalent_boundary_values[-5:-1:2]
)

print(
    f"Positive boundaries: {positive_boundary_slice}"
)

print(
    f"Negative boundaries: {negative_boundary_slice}"
)


# These two slices identify the same positions.
#
# Positive boundaries:
#
# [1:5:2]
#
# Negative boundaries:
#
# [-5:-1:2]
#
# Both select:
#
# index 1 -> index 3
#
# Result:
#
# [20, 40]


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ This module uses:

      negative start
      negative stop
      positive step

✓ Negative indexes count positions from the end of the sequence.

✓ A positive step moves from left to right.

✓ Negative indexes do NOT mean that the sequence is reversed.

✓ The stop boundary remains excluded.

✓ Example:

      sequence[-5:-1:2]

  means:

      start at negative index -5
      move forward by +2
      stop before negative index -1

✓ Negative and positive indexes can identify the same positions.

✓ For example:

      sequence[1:5:2]

  and:

      sequence[-5:-1:2]

  select the same elements when the sequence has six elements.

✓ With a positive step, the start boundary must identify a position
  before the stop boundary for a non-empty slice.

✓ Negative-step slicing is covered in the next module.

✓ Negative start and stop with a negative step will be covered separately.
"""
"""
05_negative_start_stop_positive_step
        -       -       +
        │       │       │
      start   stop    step
        │       │       │
        └───────┴───────┴──→
"""

# =============================================================================
# End of File
# =============================================================================