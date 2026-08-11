"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
List (`list`)

Overview
--------
A list is an ordered, mutable collection of objects.

Lists can contain:

    - Integers
    - Floats
    - Complex numbers
    - Strings
    - Booleans
    - Other lists
    - Tuples
    - Sets
    - Dictionaries
    - Objects of different types

Examples:

    []
    [1, 2, 3]
    ["Python", "SQL", "Airflow"]
    [1, "Python", 3.14, True]

Lists are:

    - Ordered
    - Indexable
    - Sliceable
    - Iterable
    - Mutable
    - Capable of containing duplicate values
    - Capable of storing heterogeneous objects

This module covers:

    - List literals
    - Default and non-default values
    - Type identification
    - Runtime type checking
    - List length
    - Positive indexing
    - Negative indexing
    - Slicing
    - Nested lists
    - Iteration
    - Membership testing
    - Concatenation
    - Repetition
    - Adding elements
    - Removing elements
    - Updating elements
    - Sorting
    - Reversing
    - Copying
    - List methods
    - Built-in functions applicable to lists
    - Heterogeneous lists
    - List mutability

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


from typing import cast


# =============================================================================
# Example 1: List Literals
# =============================================================================

empty_collection_list: list[int] = []

numeric_collection_list: list[int] = [
    10,
    20,
    30,
]

text_collection_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

mixed_collection_list: list[object] = [
    10,
    "Python",
    3.14,
    True,
]

print(f"Empty list:   {empty_collection_list}")
print(f"Numeric list: {numeric_collection_list}")
print(f"Text list:    {text_collection_list}")
print(f"Mixed list:   {mixed_collection_list}")


# A list is created using square brackets:
#
#     [element1, element2, element3]
#
# An empty list is:
#
#     []


# =============================================================================
# Example 2: Default and Non-Default List Values
# =============================================================================

default_like_collection: list[int] = []

non_default_collection_primary: list[int] = [
    1,
    2,
    3,
]

non_default_collection_secondary: list[str] = [
    "Python",
    "SQL",
]

print(
    f"Default-like list: {default_like_collection}"
)

print(
    f"First list:        {non_default_collection_primary}"
)

print(
    f"Second list:       {non_default_collection_secondary}"
)


# Python does NOT automatically assign [] to an annotated list variable.
#
# This:
#
#     values: list[int]
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: list[int] = []
#
# Therefore, [] is a commonly used default-like list value, not Python's
# automatic default.


# =============================================================================
# Example 3: Type Identification
# =============================================================================

list_type_sample: list[int] = [
    5,
    10,
    15,
]

print(f"Value: {list_type_sample}")
print(f"Type:  {type(list_type_sample)}")


# Expected:
#
#     <class 'list'>


# =============================================================================
# Example 4: Runtime List Type Checking
# =============================================================================

list_runtime_candidate: object = [
    1,
    2,
    3,
]

tuple_runtime_candidate: object = (
    1,
    2,
    3,
)

list_runtime_check: bool = isinstance(
    list_runtime_candidate,
    list,
) # pyright: ignore[reportUnnecessaryIsInstance]

tuple_list_check: bool = isinstance(
    tuple_runtime_candidate,
    list,
)

print(
    f"[1, 2, 3] is a list: "
    f"{list_runtime_check}"
)

print(
    f"(1, 2, 3) is a list: "
    f"{tuple_list_check}"
)


# The candidates are intentionally typed as `object`.
#
# This keeps `isinstance()` meaningful to static type checkers.


# =============================================================================
# Example 5: List Length
# =============================================================================

length_demo_list: list[str] = [
    "Python",
    "SQL",
    "Spark",
    "Airflow",
]

length_demo_result: int = len(
    length_demo_list
)

print(
    f"List length: {length_demo_result}"
)


# `len()` returns the number of elements in the list.


# =============================================================================
# Example 6: Positive Indexing
# =============================================================================

positive_index_list: list[str] = [
    "zero",
    "one",
    "two",
    "three",
]

first_list_element: str = positive_index_list[0]
third_list_element: str = positive_index_list[2]

print(
    f"First element: {first_list_element}"
)

print(
    f"Third element: {third_list_element}"
)


# Lists use zero-based indexing.
#
#     element -> index
#
#     zero    -> 0
#     one     -> 1
#     two     -> 2
#     three   -> 3


# =============================================================================
# Example 7: Negative Indexing
# =============================================================================

negative_index_list: list[str] = [
    "Python",
    "SQL",
    "Spark",
    "Airflow",
]

last_list_element: str = negative_index_list[-1]
second_last_list_element: str = negative_index_list[-2]

print(
    f"Last element:        {last_list_element}"
)

print(
    f"Second-last element: {second_last_list_element}"
)


# Negative indexing starts from the end:
#
#     Python  SQL  Spark  Airflow
#      -4     -3    -2      -1


# =============================================================================
# Example 8: List Slicing
# =============================================================================

slice_demo_list: list[int] = [
    10,
    20,
    30,
    40,
    50,
]

first_slice_result: list[int] = slice_demo_list[0:3]
second_slice_result: list[int] = slice_demo_list[2:5]

print(
    f"First slice:  {first_slice_result}"
)

print(
    f"Second slice: {second_slice_result}"
)


# General syntax:
#
#     list[start:stop]
#
# The `stop` index is excluded.


# =============================================================================
# Example 9: Nested Lists
# =============================================================================

nested_numbers_list: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

nested_row_value: list[int] = nested_numbers_list[1]

print(
    f"Nested row: {nested_row_value}"
)

print(
    f"Nested value: {nested_numbers_list[1][2]}"
)


# A list can contain other lists.
#
# Each nested list has its own indexing.


# =============================================================================
# Example 10: Heterogeneous List
# =============================================================================

heterogeneous_values_list: list[object] = [
    25,
    3.14,
    "Python",
    True,
]

print(
    heterogeneous_values_list
)


# Python lists can contain objects of different types.
#
# When static typing is important, `list[object]` can explicitly represent
# a list whose elements may have different concrete types.


# =============================================================================
# Example 11: Iterating Through a List
# =============================================================================

iteration_values_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

for iteration_item_value in iteration_values_list:
    print(iteration_item_value)


# Lists are iterable.
#
# Iteration produces one element at a time.


# =============================================================================
# Example 12: Iteration With enumerate()
# =============================================================================

enumeration_values_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

for enumeration_index, enumeration_item in enumerate(
    enumeration_values_list
):
    print(
        f"Index: {enumeration_index}, "
        f"Value: {enumeration_item}"
    )


# `enumerate()` provides both:
#
#     index
#     value


# =============================================================================
# Example 13: Membership Testing
# =============================================================================

membership_values_list: list[str] = [
    "Python",
    "SQL",
    "Spark",
]

python_membership_check: bool = (
    "Python" in membership_values_list
)

java_membership_check: bool = (
    "Java" in membership_values_list
)

print(
    f"Python present: {python_membership_check}"
)

print(
    f"Java present:   {java_membership_check}"
)


# `in` checks whether an element exists in the list.
#
# `not in` checks whether an element does not exist.


# =============================================================================
# Example 14: List Concatenation
# =============================================================================

first_tool_group: list[str] = [
    "Python",
    "SQL",
]

second_tool_group: list[str] = [
    "Spark",
    "Airflow",
]

combined_tool_group: list[str] = (
    first_tool_group
    + second_tool_group
)

print(
    f"Combined list: {combined_tool_group}"
)


# `+` creates a new list containing the elements of both lists.


# =============================================================================
# Example 15: List Repetition
# =============================================================================

repeated_value_list: list[int] = [
    0
] * 5

print(
    f"Repeated list: {repeated_value_list}"
)


# `*` repeats the elements of a list.


# =============================================================================
# Example 16: Updating an Element
# =============================================================================

mutable_update_list: list[str] = [
    "Python",
    "Java",
    "SQL",
]

mutable_update_list[1] = "C++"

print(
    f"Updated list: {mutable_update_list}"
)


# Lists are mutable.
#
# Individual elements can be replaced after the list is created.


# =============================================================================
# Example 17: append()
# =============================================================================

append_demo_list: list[str] = [
    "Python",
    "SQL",
]

append_demo_list.append(
    "Airflow"
)

print(
    f"After append(): {append_demo_list}"
)


# `append()` adds one element to the end of the list.


# =============================================================================
# Example 18: extend()
# =============================================================================

extend_demo_list: list[str] = [
    "Python",
]

extend_demo_list.extend(
    [
        "SQL",
        "Airflow",
    ]
)

print(
    f"After extend(): {extend_demo_list}"
)


# `extend()` adds each element from another iterable individually.


# =============================================================================
# Example 19: insert()
# =============================================================================

insert_demo_list: list[str] = [
    "Python",
    "Airflow",
]

insert_demo_list.insert(
    1,
    "SQL",
)

print(
    f"After insert(): {insert_demo_list}"
)


# `insert(index, value)` inserts an element at a specified position.


# =============================================================================
# Example 20: remove()
# =============================================================================

remove_demo_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

remove_demo_list.remove(
    "SQL"
)

print(
    f"After remove(): {remove_demo_list}"
)


# `remove()` deletes the first matching value.
#
# If the value does not exist, ValueError is raised.


# =============================================================================
# Example 21: pop()
# =============================================================================

pop_demo_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

removed_tool_name: str = pop_demo_list.pop()

print(
    f"Removed value: {removed_tool_name}"
)

print(
    f"Remaining list: {pop_demo_list}"
)


# `pop()` removes and returns an element.
#
# Without an index:
#
#     pop()
#
# removes the last element.
#
# With an index:
#
#     pop(index)
#
# removes the element at that position.


# =============================================================================
# Example 22: clear()
# =============================================================================

clear_demo_list: list[int] = [
    10,
    20,
    30,
]

clear_demo_list.clear()

print(
    f"After clear(): {clear_demo_list}"
)


# `clear()` removes all elements from the list.


# =============================================================================
# Example 23: index()
# =============================================================================

index_search_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

sql_position_index: int = (
    index_search_list.index("SQL")
)

print(
    f"SQL index: {sql_position_index}"
)


# `index()` returns the position of the first matching element.


# =============================================================================
# Example 24: count()
# =============================================================================

duplicate_values_list: list[int] = [
    10,
    20,
    10,
    30,
    10,
]

ten_occurrence_count: int = (
    duplicate_values_list.count(10)
)

print(
    f"10 occurs {ten_occurrence_count} times."
)


# `count()` returns the number of occurrences of a value.


# =============================================================================
# Example 25: sort()
# =============================================================================

unsorted_numbers_list: list[int] = [
    40,
    10,
    30,
    20,
]

unsorted_numbers_list.sort()

print(
    f"Sorted list: {unsorted_numbers_list}"
)


# `sort()` modifies the existing list in place.


# =============================================================================
# Example 26: reverse()
# =============================================================================

forward_order_list: list[str] = [
    "one",
    "two",
    "three",
]

forward_order_list.reverse()

print(
    f"Reversed list: {forward_order_list}"
)


# `reverse()` modifies the existing list in place.


# =============================================================================
# Example 27: sorted() vs sort()
# =============================================================================

source_sort_values: list[int] = [
    50,
    20,
    40,
    10,
]

sorted_copy_values: list[int] = sorted(
    source_sort_values
)

print(
    f"Original: {source_sort_values}"
)

print(
    f"Sorted:   {sorted_copy_values}"
)


# `sort()`:
#
#     modifies the original list
#
# `sorted()`:
#
#     creates and returns a new sorted list


# =============================================================================
# Example 28: min(), max(), and sum()
# =============================================================================

numeric_summary_list: list[int] = [
    10,
    20,
    30,
    40,
]

minimum_list_value: int = min(
    numeric_summary_list
)

maximum_list_value: int = max(
    numeric_summary_list
)

sum_list_value: int = sum(
    numeric_summary_list
)

print(
    f"Minimum: {minimum_list_value}"
)

print(
    f"Maximum: {maximum_list_value}"
)

print(
    f"Sum:     {sum_list_value}"
)


# `min()` returns the smallest element.
#
# `max()` returns the largest element.
#
# `sum()` adds numeric elements.


# =============================================================================
# Example 29: Shallow Copy
# =============================================================================

shallow_original_list: list[int | list[int]] = [
    1,
    2,
    3,
    [4, 5, 6],
]

shallow_copied_list: list[int | list[int]] = (
    shallow_original_list.copy()
)

print(
    f"Same parent object: "
    f"{shallow_original_list is shallow_copied_list}"
)


# `.copy()` creates a new outer list.
#
# Therefore:
#
#     shallow_original_list is shallow_copied_list
#
# is False.
#
# However, nested mutable objects are still shared.
#
# This topic is covered in detail in the dedicated copying concepts.


# =============================================================================
# Example 30: Nested Object Sharing in a Shallow Copy
# =============================================================================

shared_nested_original: list[int] = cast(
    list[int],
    shallow_original_list[-1],
)

shared_nested_copy: list[int] = cast(
    list[int],
    shallow_copied_list[-1],
)

print(
    f"Same nested object: "
    f"{shared_nested_original is shared_nested_copy}"
)


# `cast()` is used here only to provide the static type checker with the
# information that these specific list elements are nested `list[int]`
# objects.
#
# It does NOT perform a runtime conversion.
#
# The nested list remains the same object in both parent lists.


# =============================================================================
# Example 31: List Mutability
# =============================================================================

mutable_example_list: list[int] = [
    10,
    20,
    30,
]

mutable_example_list[0] = 100

print(
    f"Modified list: {mutable_example_list}"
)


# Lists are mutable.
#
# Their contents can be changed without creating a completely new list object.
#
# Detailed mutability behaviour is covered under:
#
#     17_type_behaviour/01_mutability.py


# =============================================================================
# Example 32: List Equality
# =============================================================================

equal_content_list_left: list[int] = [
    1,
    2,
    3,
]

equal_content_list_right: list[int] = [
    1,
    2,
    3,
]

list_equality_result: bool = (
    equal_content_list_left
    == equal_content_list_right
)

print(
    f"Equal list values: {list_equality_result}"
)


# `==` compares the contents of lists element by element.


# =============================================================================
# Example 33: List Identity
# =============================================================================

identity_list_source: list[int] = [
    1,
    2,
    3,
]

identity_list_copy: list[int] = (
    identity_list_source.copy()
)

list_identity_result: bool = (
    identity_list_source
    is identity_list_copy
)

print(
    f"Same list object: {list_identity_result}"
)


# `.copy()` creates a different outer list object.
#
# Therefore:
#
#     == -> True
#     is -> False
#
# This is an important example of the difference between equality and
# identity.


# =============================================================================
# Example 34: List Comprehension
# =============================================================================

source_numbers_for_comprehension: list[int] = [
    1,
    2,
    3,
    4,
    5,
]

squared_numbers_result: list[int] = [
    comprehension_number ** 2
    for comprehension_number
    in source_numbers_for_comprehension
]

print(
    f"Squared values: {squared_numbers_result}"
)


# A list comprehension provides a compact way to construct a new list from
# an iterable.


# =============================================================================
# Example 35: List Conversion From Another Iterable
# =============================================================================

tuple_for_list_conversion: tuple[int, ...] = (
    10,
    20,
    30,
)

converted_from_tuple_list: list[int] = list(
    tuple_for_list_conversion
)

print(
    f"Tuple: {tuple_for_list_conversion}"
)

print(
    f"List:  {converted_from_tuple_list}"
)


# `list()` can construct a list from an iterable.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `list` represents an ordered, mutable collection of objects.

✓ `[]` is a commonly used default-like list value, but Python does not
  automatically initialize an annotated list with [].

✓ A type annotation alone does not initialize a variable.

✓ Lists can contain:
      - numbers
      - strings
      - booleans
      - other lists
      - other Python objects

✓ Lists can be heterogeneous.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of elements.

✓ Lists use zero-based positive indexing.

✓ Lists support negative indexing.

✓ Lists support slicing.

✓ Lists can contain nested lists.

✓ Lists are iterable.

✓ `enumerate()` provides indexes together with values.

✓ `in` and `not in` perform membership testing.

✓ `+` concatenates lists.

✓ `*` repeats list elements.

✓ Lists are mutable.

✓ Individual elements can be updated.

✓ `append()` adds one element.

✓ `extend()` adds elements from an iterable.

✓ `insert()` inserts an element at a specific position.

✓ `remove()` removes the first matching value.

✓ `pop()` removes and returns an element.

✓ `clear()` removes all elements.

✓ `index()` finds the position of a value.

✓ `count()` counts occurrences.

✓ `sort()` modifies a list in place.

✓ `reverse()` modifies a list in place.

✓ `sorted()` returns a new sorted list.

✓ `min()`, `max()`, and `sum()` can operate on suitable lists.

✓ `.copy()` creates a shallow copy.

✓ A shallow copy creates a new outer list but can still share nested mutable
  objects.

✓ `cast()` can communicate more precise static type information to a type
  checker without performing a runtime conversion.

✓ `==` compares list contents.

✓ `is` compares list identity.

✓ List comprehensions provide a concise way to construct lists.

✓ `list()` can create a list from another iterable.

✓ Detailed mutability, copying, equality, and identity behaviour is covered
  separately.
"""


# =============================================================================
# End of File
# =============================================================================