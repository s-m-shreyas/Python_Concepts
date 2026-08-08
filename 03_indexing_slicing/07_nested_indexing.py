"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Nested Indexing

Overview
--------
Nested indexing is the process of using multiple indexes to access an element
inside a nested collection.

A nested collection contains another collection as one or more of its
elements.

For example:

    values = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

The first index selects an inner collection.

The second index selects an element from that inner collection.

Syntax
------
    sequence[outer_index][inner_index]

Example
-------
    values[1][2]

Execution:

    values[1]
        ↓
    [40, 50, 60]

Then:

    [40, 50, 60][2]
        ↓
    60

Therefore:

    values[1][2] → 60

Key Idea
--------
Nested indexing is simply indexing performed in multiple stages.

The first index selects the nested object.

The next index operates on the object returned by the previous index.

Nested indexing can therefore be extended to deeper structures:

    sequence[index_1][index_2][index_3]

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html
"""


# =============================================================================
# Example 1: Basic Nested List Indexing
# =============================================================================

basic_nested_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

basic_nested_element: int = basic_nested_values[1][2]

print(
    f"Nested values: {basic_nested_values}"
)

print(
    f"Selected element: {basic_nested_element}"
)


# Execution:
#
# basic_nested_values[1]
#
# -> [40, 50, 60]
#
# Then:
#
# basic_nested_values[1][2]
#
# -> 60


# =============================================================================
# Example 2: Selecting Different Inner Lists
# =============================================================================

row_selection_values: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

first_row_element: int = row_selection_values[0][1]
second_row_element: int = row_selection_values[1][1]
third_row_element: int = row_selection_values[2][1]

print(
    f"First row element:  {first_row_element}"
)

print(
    f"Second row element: {second_row_element}"
)

print(
    f"Third row element:  {third_row_element}"
)


# First:
#
# row_selection_values[0]
# -> [1, 2, 3]
#
# [1, 2, 3][1]
# -> 2
#
#
# Second:
#
# row_selection_values[1]
# -> [4, 5, 6]
#
# [4, 5, 6][1]
# -> 5
#
#
# Third:
#
# row_selection_values[2]
# -> [7, 8, 9]
#
# [7, 8, 9][1]
# -> 8


# =============================================================================
# Example 3: Nested Indexing with Different Inner Indexes
# =============================================================================

coordinate_matrix: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

top_left_value: int = coordinate_matrix[0][0]
center_value: int = coordinate_matrix[1][1]
bottom_right_value: int = coordinate_matrix[2][2]

print(
    f"Top-left value:     {top_left_value}"
)

print(
    f"Center value:       {center_value}"
)

print(
    f"Bottom-right value: {bottom_right_value}"
)


# The two indexes represent:
#
# coordinate_matrix[row][column]
#
# First index:
#
# row
#
# Second index:
#
# column


# =============================================================================
# Example 4: Nested Indexing with Strings
# =============================================================================

nested_words: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

first_word_character: str = nested_words[0][2]
second_word_character: str = nested_words[1][1]
third_word_character: str = nested_words[2][3]

print(
    f"First word character:  {first_word_character}"
)

print(
    f"Second word character: {second_word_character}"
)

print(
    f"Third word character:  {third_word_character}"
)


# Execution:
#
# nested_words[0]
# -> "Python"
#
# "Python"[2]
# -> "t"
#
#
# nested_words[1]
# -> "SQL"
#
# "SQL"[1]
# -> "Q"


# =============================================================================
# Example 5: Nested List Containing Tuples
# =============================================================================

employee_records: list[tuple[str, int]] = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),
]

first_employee_name: str = employee_records[0][0]
second_employee_age: int = employee_records[1][1]
third_employee_name: str = employee_records[2][0]

print(
    f"First employee:  {first_employee_name}"
)

print(
    f"Second age:      {second_employee_age}"
)

print(
    f"Third employee:  {third_employee_name}"
)


# Nested indexing does not require every nested object to be a list.
#
# Here:
#
# employee_records[1]
# -> ("Bob", 30)
#
# employee_records[1][1]
# -> 30


# =============================================================================
# Example 6: Nested Tuple
# =============================================================================

nested_tuple_values: tuple[tuple[int, ...], ...] = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90),
)

nested_tuple_element: int = nested_tuple_values[2][1]

print(
    f"Nested tuple: {nested_tuple_values}"
)

print(
    f"Selected element: {nested_tuple_element}"
)


# The same indexing concept applies to tuples.
#
# nested_tuple_values[2]
# -> (70, 80, 90)
#
# nested_tuple_values[2][1]
# -> 80


# =============================================================================
# Example 7: Negative Indexing at the Outer Level
# =============================================================================

outer_negative_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

outer_negative_element: int = outer_negative_values[-1][0]

print(
    f"Nested values: {outer_negative_values}"
)

print(
    f"Selected element: {outer_negative_element}"
)


# First index:
#
# -1
#
# selects the last inner list:
#
# [70, 80, 90]
#
# Second index:
#
# 0
#
# selects:
#
# 70


# =============================================================================
# Example 8: Negative Indexing at the Inner Level
# =============================================================================

inner_negative_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

inner_negative_element: int = inner_negative_values[1][-1]

print(
    f"Nested values: {inner_negative_values}"
)

print(
    f"Selected element: {inner_negative_element}"
)


# First index:
#
# 1
#
# selects:
#
# [40, 50, 60]
#
# Second index:
#
# -1
#
# selects the last element:
#
# 60


# =============================================================================
# Example 9: Negative Indexing at Both Levels
# =============================================================================

both_negative_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

both_negative_element: int = both_negative_values[-1][-1]

print(
    f"Nested values: {both_negative_values}"
)

print(
    f"Selected element: {both_negative_element}"
)


# First -1:
#
# selects the last inner list:
#
# [70, 80, 90]
#
# Second -1:
#
# selects the last element:
#
# 90


# =============================================================================
# Example 10: Three-Level Nested Indexing
# =============================================================================

three_level_values: list[list[list[int]]] = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
]

three_level_element: int = three_level_values[1][0][1]

print(
    f"Three-level structure: {three_level_values}"
)

print(
    f"Selected element:      {three_level_element}"
)


# Execution:
#
# three_level_values[1]
# -> [
#      [5, 6],
#      [7, 8]
#    ]
#
# Then:
#
# three_level_values[1][0]
# -> [5, 6]
#
# Finally:
#
# three_level_values[1][0][1]
# -> 6


# =============================================================================
# Example 11: Modifying a Nested Element
# =============================================================================

modifiable_nested_values: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

modifiable_nested_values[1][2] = 600

print(
    f"Modified nested values: {modifiable_nested_values}"
)


# The indexes identify the exact element being modified:
#
# [1]
# -> second inner list
#
# [2]
# -> third element inside that list
#
# Therefore:
#
# modifiable_nested_values[1][2] = 600
#
# changes:
#
# 60 -> 600


# =============================================================================
# Example 12: Nested Indexing as Sequential Operations
# =============================================================================

sequential_index_values: list[list[int]] = [
    [100, 200, 300],
    [400, 500, 600],
]

selected_inner_collection: list[int] = sequential_index_values[1]

selected_nested_value: int = selected_inner_collection[2]

direct_nested_value: int = sequential_index_values[1][2]

print(
    f"Selected inner collection: {selected_inner_collection}"
)

print(
    f"Sequential result:          {selected_nested_value}"
)

print(
    f"Direct nested result:       {direct_nested_value}"
)


# These two approaches are equivalent:
#
# Sequential:
#
# selected_inner_collection = sequential_index_values[1]
# selected_nested_value = selected_inner_collection[2]
#
#
# Direct:
#
# direct_nested_value = sequential_index_values[1][2]
#
#
# Nested indexing is therefore simply multiple indexing operations
# performed from left to right.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Nested indexing accesses elements inside nested collections.

✓ The basic syntax is:

      sequence[outer_index][inner_index]

✓ The first index selects the nested object.

✓ The second index selects an element from that object.

✓ Nested indexing can be extended:

      sequence[index_1][index_2][index_3]

✓ Negative indexes can be used at any indexing level.

✓ Negative indexes identify positions from the end of the corresponding
  sequence.

✓ Nested indexing can be used with lists, tuples, strings, and combinations
  of these sequence types.

✓ Nested indexing can also be used to modify mutable nested objects.

✓ Nested indexing is a sequence of indexing operations performed from
  left to right.

✓ Slicing nested collections is intentionally covered separately in:

      08_nested_slicing.py
"""
"""
nested_values[1][2]
       │      │
       │      └── index the object returned by [1]
       │
       └── first indexing operation
"""
"""
For the value inside nested list of some list.

values[1][0][1]
   │    │   │
   │    │   └── element
   │    └────── nested collection
   └─────────── outer collection
"""
# =============================================================================
# End of File
# =============================================================================