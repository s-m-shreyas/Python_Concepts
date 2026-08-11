"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Slice Objects

Overview
--------
Python provides the built-in `slice()` function to create a slice object.

A slice object stores the three components of slicing:

    start
    stop
    step

Instead of writing the slicing expression directly:

    sequence[start:stop:step]

we can create a reusable slice object:

    sequence_slice = slice(start, stop, step)

The slice object can then be applied to one or more compatible sequences.

Syntax
------
    slice(stop)
    slice(start, stop)
    slice(start, stop, step)

Examples
--------
    slice(5)

is equivalent to:

    [:5]

    slice(1, 5)

is equivalent to:

    [1:5]

    slice(1, 5, 2)

is equivalent to:

    [1:5:2]

Key Idea
--------
A slice object stores slicing instructions.

It does not contain the elements being sliced.

The same slice object can therefore be applied to different sequences.

References
----------
Python Official Documentation

https://docs.python.org/3/library/functions.html#slice
"""


# =============================================================================
# Example 1: Creating a Slice Object
# =============================================================================

basic_slice_object: slice = slice(1, 5)

print(
    f"Slice object: {basic_slice_object}"
)


# The slice object represents:
#
# start = 1
# stop  = 5
# step  = None
#
# It can be inspected through its attributes.


# =============================================================================
# Example 2: Inspecting Slice Attributes
# =============================================================================

inspected_slice_object: slice = slice(1, 5, 2)

print(
    f"Start: {inspected_slice_object.start}"
)

print(
    f"Stop:  {inspected_slice_object.stop}"
)

print(
    f"Step:  {inspected_slice_object.step}"
)


# A slice object stores:
#
# .start
# .stop
# .step


# =============================================================================
# Example 3: Applying a Slice Object to a List
# =============================================================================

list_slice_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

list_slice_object: slice = slice(1, 5, 2)

list_slice_result: list[int] = (
    list_slice_values[list_slice_object]
)

print(
    f"Original values: {list_slice_values}"
)

print(
    f"Sliced values:   {list_slice_result}"
)


# The slice object:
#
# slice(1, 5, 2)
#
# behaves like:
#
# [1:5:2]
#
# Therefore:
#
# indexes:
#
# 1 -> 3
#
# values:
#
# 20 -> 40
#
# Result:
#
# [20, 40]


# =============================================================================
# Example 4: Applying the Same Slice Object to Multiple Lists
# =============================================================================

shared_slice_object: slice = slice(1, 6, 2)

first_slice_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

second_slice_values: list[int] = [
    100,
    200,
    300,
    400,
    500,
    600,
]

first_slice_result: list[int] = (
    first_slice_values[shared_slice_object]
)

second_slice_result: list[int] = (
    second_slice_values[shared_slice_object]
)

print(
    f"First result:  {first_slice_result}"
)

print(
    f"Second result: {second_slice_result}"
)


# The same slicing rule is reused:
#
# slice(1, 6, 2)
#
# First list:
#
# [20, 40, 60]
#
# Second list:
#
# [200, 400, 600]


# =============================================================================
# Example 5: Slice Object with Only Stop
# =============================================================================

stop_only_slice: slice = slice(4)

stop_only_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

stop_only_result: list[int] = (
    stop_only_values[stop_only_slice]
)

print(
    f"Original values: {stop_only_values}"
)

print(
    f"Sliced values:   {stop_only_result}"
)


# slice(4)
#
# is equivalent to:
#
# [:4]
#
# start is None.
#
# stop is 4.
#
# step is None.
#
# Result:
#
# [10, 20, 30, 40]


# =============================================================================
# Example 6: Slice Object with Start and Stop
# =============================================================================

start_stop_slice: slice = slice(2, 5)

start_stop_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

start_stop_result: list[int] = (
    start_stop_values[start_stop_slice]
)

print(
    f"Original values: {start_stop_values}"
)

print(
    f"Sliced values:   {start_stop_result}"
)


# slice(2, 5)
#
# is equivalent to:
#
# [2:5]
#
# Result:
#
# [30, 40, 50]


# =============================================================================
# Example 7: Slice Object with a Positive Step
# =============================================================================

positive_step_slice: slice = slice(0, 6, 2)

positive_step_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

positive_step_result: list[int] = (
    positive_step_values[positive_step_slice]
)

print(
    f"Original values: {positive_step_values}"
)

print(
    f"Sliced values:   {positive_step_result}"
)


# Equivalent direct slicing:
#
# positive_step_values[0:6:2]
#
# Result:
#
# [10, 30, 50]


# =============================================================================
# Example 8: Slice Object with a Negative Step
# =============================================================================

negative_step_slice: slice = slice(5, 1, -1)

negative_step_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

negative_step_result: list[int] = (
    negative_step_values[negative_step_slice]
)

print(
    f"Original values: {negative_step_values}"
)

print(
    f"Sliced values:   {negative_step_result}"
)


# Equivalent direct slicing:
#
# negative_step_values[5:1:-1]
#
# Movement:
#
# 5 -> 4 -> 3 -> 2
#
# Stop 1 is excluded.
#
# Result:
#
# [60, 50, 40, 30]


# =============================================================================
# Example 9: Slice Object with Negative Indexes
# =============================================================================

negative_index_slice: slice = slice(-1, -5, -1)

negative_index_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

negative_index_result: list[int] = (
    negative_index_values[negative_index_slice]
)

print(
    f"Original values: {negative_index_values}"
)

print(
    f"Sliced values:   {negative_index_result}"
)


# Equivalent direct slicing:
#
# negative_index_values[-1:-5:-1]
#
# Result:
#
# [60, 50, 40, 30]


# =============================================================================
# Example 10: Applying a Slice Object to a String
# =============================================================================

string_slice_object: slice = slice(0, 6, 2)

sliceable_string: str = "Python"

string_slice_result: str = (
    sliceable_string[string_slice_object]
)

print(
    f"Original string: {sliceable_string}"
)

print(
    f"Sliced string:   {string_slice_result}"
)


# The slice object works with strings because strings support slicing.


# =============================================================================
# Example 11: Applying a Slice Object to a Tuple
# =============================================================================

tuple_slice_object: slice = slice(1, 5, 2)

sliceable_tuple: tuple[int, ...] = (
    10,
    20,
    30,
    40,
    50,
)

tuple_slice_result: tuple[int, ...] = (
    sliceable_tuple[tuple_slice_object]
)

print(
    f"Original tuple: {sliceable_tuple}"
)

print(
    f"Sliced tuple:   {tuple_slice_result}"
)


# Result:
#
# [1:5:2]
#
# -> (20, 40)


# =============================================================================
# Example 12: Using a Slice Object with Bytes
# =============================================================================

bytes_slice_object: slice = slice(1, 5, 2)

sliceable_bytes: bytes = b"Python"

bytes_slice_result: bytes = (
    sliceable_bytes[bytes_slice_object]
)

print(
    f"Original bytes: {sliceable_bytes!r}"
)

print(
    f"Sliced bytes:   {bytes_slice_result!r}"
)

# Bytes are also sliceable sequences.


# =============================================================================
# Example 13: Slice Objects Store Instructions, Not Results
# =============================================================================

stored_slice_object: slice = slice(1, 4)

stored_slice_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
]

stored_slice_result: list[int] = (
    stored_slice_values[stored_slice_object]
)

print(
    f"Slice object: {stored_slice_object}"
)

print(
    f"Slice result: {stored_slice_result}"
)


# The slice object does not store:
#
# [20, 30, 40]
#
# It stores the instructions:
#
# start = 1
# stop  = 4
# step  = None
#
# The sequence provides the actual elements.


# =============================================================================
# Example 14: Reusing a Slice Object
# =============================================================================

reusable_slice: slice = slice(0, 5, 2)

first_reusable_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
]

second_reusable_values: list[int] = [
    100,
    200,
    300,
    400,
    500,
]

first_reusable_result: list[int] = (
    first_reusable_values[reusable_slice]
)

second_reusable_result: list[int] = (
    second_reusable_values[reusable_slice]
)

print(
    f"First reusable result:  {first_reusable_result}"
)

print(
    f"Second reusable result: {second_reusable_result}"
)


# One slice object can describe the same positional operation
# across different compatible sequences.


# =============================================================================
# Example 15: Slice Object with None Values
# =============================================================================

none_based_slice: slice = slice(None, None, -1)

none_based_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
]

none_based_result: list[int] = (
    none_based_values[none_based_slice]
)

print(
    f"Original values: {none_based_values}"
)

print(
    f"Reversed values: {none_based_result}"
)


# slice(None, None, -1)
#
# is equivalent to:
#
# [::-1]
#
# None represents an omitted slicing boundary.


# =============================================================================
# Example 16: Comparing Direct Slicing with a Slice Object
# =============================================================================

comparison_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

direct_slice_result: list[int] = (
    comparison_values[1:6:2]
)

comparison_slice_object: slice = slice(1, 6, 2)

slice_object_result: list[int] = (
    comparison_values[comparison_slice_object]
)

print(
    f"Direct slicing:   {direct_slice_result}"
)

print(
    f"Slice object:     {slice_object_result}"
)


# Both approaches produce the same result:
#
# [20, 40, 60]
#
# Direct:
#
# values[1:6:2]
#
# Slice object:
#
# values[slice(1, 6, 2)]


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `slice()` creates a slice object.

✓ A slice object stores:

      start
      stop
      step

✓ Syntax:

      slice(stop)

      slice(start, stop)

      slice(start, stop, step)

✓ Examples:

      slice(5)
      slice(1, 5)
      slice(1, 5, 2)

✓ A slice object does not store the elements being selected.

✓ It stores the instructions describing how a sequence should be sliced.

✓ A slice object can be reused with multiple compatible sequences.

✓ Slice objects work with sliceable sequence types such as:

      lists
      tuples
      strings
      bytes

✓ Direct slicing:

      values[1:5:2]

  is equivalent to:

      values[slice(1, 5, 2)]

✓ `None` represents an omitted slicing component.

✓ Example:

      slice(None, None, -1)

  is equivalent to:

      [::-1]

✓ Slice objects are useful when slicing logic needs to be stored,
  reused, or passed around as a value.

✓ Copying through slicing is intentionally covered separately.
"""
"""
09_slice_object
        │
        ▼
      slice()
        │
        ├── start
        ├── stop
        └── step
        │
        ▼
sequence[slice_object]
"""

"""
values[1:5:2]
      │
      ▼
values[slice(1, 5, 2)]
"""

# =============================================================================
# End of File
# =============================================================================