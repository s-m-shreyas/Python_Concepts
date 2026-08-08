"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Nested Slicing

Overview
--------
Nested slicing is the process of applying slicing to a sequence contained
inside another sequence.

A nested structure can first be indexed to select an inner sequence and then
sliced to select a range of elements from that inner sequence.

Syntax
------
    sequence[outer_index][start:stop:step]

Example
-------
    values = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120]
    ]

    values[1][1:3]

Execution:

    values[1]
        ↓
    [50, 60, 70, 80]

    [50, 60, 70, 80][1:3]
        ↓
    [60, 70]

Therefore:

    values[1][1:3] → [60, 70]

Key Idea
--------
Nested slicing consists of two separate operations:

    1. Select the nested sequence.
    2. Apply slicing to the selected sequence.

The outer index identifies WHICH nested sequence is being sliced.

The slice identifies WHICH RANGE of elements is selected from it.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html
"""


# =============================================================================
# Example 1: Basic Nested Slicing
# =============================================================================

basic_nested_sequences: list[list[int]] = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

basic_nested_slice: list[int] = (
    basic_nested_sequences[1][1:3]
)

print(
    f"Original structure: {basic_nested_sequences}"
)

print(
    f"Nested slice:       {basic_nested_slice}"
)


# Execution:
#
# basic_nested_sequences[1]
# -> [50, 60, 70, 80]
#
# [50, 60, 70, 80][1:3]
# -> [60, 70]


# =============================================================================
# Example 2: Slicing the First Inner Sequence
# =============================================================================

first_inner_sequences: list[list[int]] = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
]

first_inner_slice: list[int] = (
    first_inner_sequences[0][1:4]
)

print(
    f"First inner sequence: {first_inner_sequences[0]}"
)

print(
    f"Sliced result:        {first_inner_slice}"
)


# The outer index [0] selects the first inner sequence.
#
# The slice [1:4] then selects:
#
# index 1 -> 20
# index 2 -> 30
# index 3 -> 40
#
# Result:
#
# [20, 30, 40]


# =============================================================================
# Example 3: Slicing the Last Inner Sequence
# =============================================================================

last_inner_sequences: list[list[int]] = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

last_inner_slice: list[int] = (
    last_inner_sequences[2][0:3]
)

print(
    f"Last inner sequence: {last_inner_sequences[2]}"
)

print(
    f"Sliced result:      {last_inner_slice}"
)


# The outer index [2] selects:
#
# [90, 100, 110, 120]
#
# The slice [0:3] selects:
#
# [90, 100, 110]
#
# Result:
#
# [90, 100, 110]


# =============================================================================
# Example 4: Nested Slicing with a Positive Step
# =============================================================================

positive_step_nested_values: list[list[int]] = [
    [10, 20, 30, 40, 50, 60],
    [70, 80, 90, 100, 110, 120],
]

positive_step_nested_slice: list[int] = (
    positive_step_nested_values[1][0:6:2]
)

print(
    f"Selected inner sequence: {positive_step_nested_values[1]}"
)

print(
    f"Sliced result:            {positive_step_nested_slice}"
)


# The outer index selects:
#
# [70, 80, 90, 100, 110, 120]
#
# The slice:
#
# [0:6:2]
#
# selects indexes:
#
# 0 -> 2 -> 4
#
# Result:
#
# [70, 90, 110]


# =============================================================================
# Example 5: Nested Slicing with a Negative Step
# =============================================================================

negative_step_nested_values: list[list[int]] = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
]

negative_step_nested_slice: list[int] = (
    negative_step_nested_values[1][4:1:-1]
)

print(
    f"Selected inner sequence: {negative_step_nested_values[1]}"
)

print(
    f"Sliced result:            {negative_step_nested_slice}"
)


# The outer index selects:
#
# [60, 70, 80, 90, 100]
#
# The slice:
#
# [4:1:-1]
#
# selects indexes:
#
# 4 -> 3 -> 2
#
# Result:
#
# [100, 90, 80]


# =============================================================================
# Example 6: Negative Index with Nested Slicing
# =============================================================================

negative_outer_index_values: list[list[int]] = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

negative_outer_index_slice: list[int] = (
    negative_outer_index_values[-1][1:3]
)

print(
    f"Selected inner sequence: {negative_outer_index_values[-1]}"
)

print(
    f"Sliced result:            {negative_outer_index_slice}"
)


# Outer index:
#
# -1
#
# selects the last inner sequence:
#
# [90, 100, 110, 120]
#
# Then:
#
# [1:3]
#
# selects:
#
# [100, 110]


# =============================================================================
# Example 7: Negative Inner Index with Slicing
# =============================================================================

negative_inner_index_values: list[list[int]] = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
]

negative_inner_index_slice: list[int] = (
    negative_inner_index_values[0][-4:-1]
)

print(
    f"Selected inner sequence: {negative_inner_index_values[0]}"
)

print(
    f"Sliced result:            {negative_inner_index_slice}"
)


# Inner negative boundaries:
#
# -4 -> 20
# -3 -> 30
# -2 -> 40
# -1 -> 50
#
# Stop -1 is excluded.
#
# Result:
#
# [20, 30, 40]


# =============================================================================
# Example 8: Slicing Every Inner Sequence Separately
# =============================================================================

multiple_inner_sequences: list[list[int]] = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

first_sequence_slice: list[int] = (
    multiple_inner_sequences[0][1:3]
)

second_sequence_slice: list[int] = (
    multiple_inner_sequences[1][1:3]
)

third_sequence_slice: list[int] = (
    multiple_inner_sequences[2][1:3]
)

print(
    f"First slice:  {first_sequence_slice}"
)

print(
    f"Second slice: {second_sequence_slice}"
)

print(
    f"Third slice:  {third_sequence_slice}"
)


# Each outer index selects a different inner sequence.
#
# The same slice can then be applied independently.


# =============================================================================
# Example 9: Nested String Slicing
# =============================================================================

nested_string_values: list[str] = [
    "Python",
    "Programming",
    "Database",
]

first_string_slice: str = nested_string_values[0][1:4]
second_string_slice: str = nested_string_values[1][0:6:2]
third_string_slice: str = nested_string_values[2][::-1]

print(
    f"First string slice:  {first_string_slice}"
)

print(
    f"Second string slice: {second_string_slice}"
)

print(
    f"Third string slice:  {third_string_slice}"
)


# The same concept works when the nested object is a string.
#
# First:
#
# nested_string_values[0]
# -> "Python"
#
# Then:
#
# "Python"[1:4]
# -> "yth"


# =============================================================================
# Example 10: Nested Tuple Slicing
# =============================================================================

nested_tuple_sequences: tuple[tuple[int, ...], ...] = (
    (10, 20, 30, 40),
    (50, 60, 70, 80),
    (90, 100, 110, 120),
)

nested_tuple_slice: tuple[int, ...] = (
    nested_tuple_sequences[1][1:4]
)

print(
    f"Selected tuple: {nested_tuple_sequences[1]}"
)

print(
    f"Sliced tuple:   {nested_tuple_slice}"
)


# The inner tuple is immutable, but slicing still creates a new tuple
# containing the selected elements.


# =============================================================================
# Example 11: Nested Slicing Is Not the Same as Outer Slicing
# =============================================================================

comparison_nested_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

outer_slice_result: list[list[int]] = (
    comparison_nested_values[0:2]
)

inner_slice_result: list[int] = (
    comparison_nested_values[0][0:2]
)

print(
    f"Outer slice: {outer_slice_result}"
)

print(
    f"Inner slice: {inner_slice_result}"
)


# Outer slicing:
#
# comparison_nested_values[0:2]
#
# selects INNER COLLECTIONS:
#
# [[10, 20, 30], [40, 50, 60]]
#
#
# Inner slicing:
#
# comparison_nested_values[0][0:2]
#
# first selects:
#
# [10, 20, 30]
#
# and then slices it:
#
# [10, 20]
#
# These are two different operations.


# =============================================================================
# Example 12: Nested Slicing as Sequential Operations
# =============================================================================

sequential_nested_values: list[list[int]] = [
    [100, 200, 300, 400],
    [500, 600, 700, 800],
]

selected_inner_sequence: list[int] = (
    sequential_nested_values[1]
)

selected_inner_slice: list[int] = (
    selected_inner_sequence[1:3]
)

direct_nested_slice: list[int] = (
    sequential_nested_values[1][1:3]
)

print(
    f"Selected inner sequence: {selected_inner_sequence}"
)

print(
    f"Sequential slice:         {selected_inner_slice}"
)

print(
    f"Direct nested slice:      {direct_nested_slice}"
)


# These are equivalent:
#
# Sequential:
#
# selected_inner_sequence = sequential_nested_values[1]
# selected_inner_slice = selected_inner_sequence[1:3]
#
#
# Direct:
#
# direct_nested_slice = sequential_nested_values[1][1:3]
#
#
# Nested slicing is therefore indexing followed by slicing.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Nested slicing applies slicing to a sequence contained inside another
  sequence.

✓ The basic syntax is:

      sequence[outer_index][start:stop:step]

✓ The outer index selects the nested sequence.

✓ The slice then selects a range from that nested sequence.

✓ The outer operation and inner slicing operation are separate.

✓ Nested slicing can use positive or negative indexes.

✓ Nested slicing can use positive or negative steps.

✓ Nested slicing works with nested lists, tuples, strings, and combinations
  of sequence types.

✓ Outer slicing and inner slicing are different operations.

✓ Example:

      values[0:2]

  slices the OUTER sequence.

✓ Example:

      values[0][0:2]

  selects the first inner sequence and then slices that INNER sequence.

✓ Nested slicing is effectively:

      1. Select the nested sequence.
      2. Apply slicing to the selected sequence.

✓ `slice()` objects are intentionally covered separately in:

      09_slice_object.py
"""
"""
nested_values[1][1:3]
       │       │
       │       └── slice the selected inner sequence
       │
       └── select the inner sequence
"""
"""
Outer slicing                    Inner slicing

values[0:2]                      values[0][0:2]
     │                                  │
     ▼                                  ▼
select inner lists              select first inner list
     │                                  │
     ▼                                  ▼
[[...], [...]]                  then slice its elements
                                        │
                                        ▼
                                    [...]
"""

# =============================================================================
# End of File
# =============================================================================