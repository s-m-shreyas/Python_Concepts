"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Tuple (`tuple`)

Overview
--------
A tuple is an ordered, immutable collection of objects.

Tuples can contain:

    - Integers
    - Floats
    - Complex numbers
    - Strings
    - Booleans
    - Other tuples
    - Lists
    - Dictionaries
    - Objects of different types

Examples:

    ()
    (1, 2, 3)
    ("Python", "SQL", "Airflow")
    (1, "Python", 3.14, True)

Tuples are:

    - Ordered
    - Indexable
    - Sliceable
    - Iterable
    - Immutable
    - Capable of containing duplicate values
    - Capable of storing heterogeneous objects

This module covers:

    - Tuple literals
    - Default and non-default values
    - Empty tuples
    - Single-element tuples
    - Tuple packing
    - Tuple unpacking
    - Type identification
    - Runtime type checking
    - Length
    - Positive indexing
    - Negative indexing
    - Slicing
    - Nested tuples
    - Iteration
    - Membership testing
    - Concatenation
    - Repetition
    - Tuple methods
    - Built-in functions applicable to tuples
    - Heterogeneous tuples
    - Tuple immutability
    - Conversion between tuples and lists

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Tuple Literals
# =============================================================================

empty_tuple_value: tuple[()] = ()

numeric_tuple_value: tuple[int, ...] = (
    10,
    20,
    30,
)

text_tuple_value: tuple[str, ...] = (
    "Python",
    "SQL",
    "Airflow",
)

mixed_tuple_value: tuple[object, ...] = (
    10,
    "Python",
    3.14,
    True,
)

print(f"Empty tuple:   {empty_tuple_value}")
print(f"Numeric tuple: {numeric_tuple_value}")
print(f"Text tuple:    {text_tuple_value}")
print(f"Mixed tuple:   {mixed_tuple_value}")


# =============================================================================
# Example 2: Default and Non-Default Tuple Values
# =============================================================================

default_like_tuple_value: tuple[()] = ()

non_default_tuple_primary: tuple[int, ...] = (
    1,
    2,
    3,
)

non_default_tuple_secondary: tuple[str, ...] = (
    "Python",
    "SQL",
)

print(
    f"Default-like tuple: {default_like_tuple_value}"
)

print(
    f"First tuple:        {non_default_tuple_primary}"
)

print(
    f"Second tuple:       {non_default_tuple_secondary}"
)


# Python does NOT automatically assign () to an annotated tuple variable.
#
# This:
#
#     values: tuple[int, ...]
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: tuple[int, ...] = ()
#
# Therefore, () is a commonly used default-like tuple value, not Python's
# automatic default.


# =============================================================================
# Example 3: Single-Element Tuple
# =============================================================================

single_element_tuple_value: tuple[int] = (
    100,
)

print(
    f"Single-element tuple: {single_element_tuple_value}"
)

print(
    f"Type: {type(single_element_tuple_value)}"
)


# The comma creates a tuple.
#
#     (100,) -> tuple
#     (100)  -> int


# =============================================================================
# Example 4: Tuple Packing
# =============================================================================

packed_tuple_value: tuple[str, ...] = (
    "Python",
    "SQL",
    "Airflow",
)

print(
    f"Packed tuple: {packed_tuple_value}"
)


# Multiple values can be packed into a tuple.


# =============================================================================
# Example 5: Tuple Unpacking
# =============================================================================

unpacking_source_tuple: tuple[str, str, str] = (
    "Python",
    "SQL",
    "Airflow",
)

unpacked_language_name: str
unpacked_database_name: str
unpacked_workflow_name: str

(
    unpacked_language_name,
    unpacked_database_name,
    unpacked_workflow_name,
) = unpacking_source_tuple

print(unpacked_language_name)
print(unpacked_database_name)
print(unpacked_workflow_name)


# =============================================================================
# Example 6: Extended Tuple Unpacking
# =============================================================================

extended_unpacking_source: tuple[int, int, int, int, int] = (
    10,
    20,
    30,
    40,
    50,
)



(   extended_first_value,
    *extended_middle_values,
    extended_last_value,) = extended_unpacking_source

print(
    f"First:  {extended_first_value}"
)

print(
    f"Middle: {extended_middle_values}"
)

print(
    f"Last:   {extended_last_value}"
)


# =============================================================================
# Example 7: Type Identification
# =============================================================================

tuple_type_sample: tuple[int, ...] = (
    5,
    10,
    15,
)

print(
    f"Value: {tuple_type_sample}"
)

print(
    f"Type:  {type(tuple_type_sample)}"
)


# Expected:
#
#     <class 'tuple'>


# =============================================================================
# Example 8: Runtime Tuple Type Checking
# =============================================================================

tuple_runtime_candidate: object = (
    1,
    2,
    3,
)

list_runtime_candidate_for_tuple: object = [
    1,
    2,
    3,
]

tuple_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    tuple_runtime_candidate,
    tuple,
)

list_tuple_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    list_runtime_candidate_for_tuple,
    tuple,
)

print(
    f"(1, 2, 3) is a tuple: "
    f"{tuple_runtime_check}"
)

print(
    f"[1, 2, 3] is a tuple: "
    f"{list_tuple_check}"
)


# The candidates are intentionally typed as `object`.
#
# The Pyright suppression is used because this example intentionally
# demonstrates runtime isinstance() behaviour.


# =============================================================================
# Example 9: Tuple Length
# =============================================================================

tuple_length_sample: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
)

tuple_length_result: int = len(
    tuple_length_sample
)

print(
    f"Tuple length: {tuple_length_result}"
)


# =============================================================================
# Example 10: Positive Indexing
# =============================================================================

positive_tuple_index_sample: tuple[str, ...] = (
    "zero",
    "one",
    "two",
    "three",
)

tuple_first_element: str = (
    positive_tuple_index_sample[0]
)

tuple_third_element: str = (
    positive_tuple_index_sample[2]
)

print(
    f"First element: {tuple_first_element}"
)

print(
    f"Third element: {tuple_third_element}"
)


# =============================================================================
# Example 11: Negative Indexing
# =============================================================================

negative_tuple_index_sample: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
    "Airflow",
)

tuple_last_element: str = (
    negative_tuple_index_sample[-1]
)

tuple_second_last_element: str = (
    negative_tuple_index_sample[-2]
)

print(
    f"Last element:        {tuple_last_element}"
)

print(
    f"Second-last element: {tuple_second_last_element}"
)


# =============================================================================
# Example 12: Tuple Slicing
# =============================================================================

tuple_slice_source: tuple[int, ...] = (
    10,
    20,
    30,
    40,
    50,
)

tuple_first_slice: tuple[int, ...] = (
    tuple_slice_source[0:3]
)

tuple_second_slice: tuple[int, ...] = (
    tuple_slice_source[2:5]
)

print(
    f"First slice:  {tuple_first_slice}"
)

print(
    f"Second slice: {tuple_second_slice}"
)


# =============================================================================
# Example 13: Nested Tuples
# =============================================================================

nested_tuple_structure: tuple[
    tuple[int, int],
    tuple[int, int],
] = (
    (10, 20),
    (30, 40),
)

nested_tuple_row: tuple[int, int] = (
    nested_tuple_structure[1]
)

nested_tuple_value: int = (
    nested_tuple_structure[1][0]
)

print(
    f"Nested tuple: {nested_tuple_row}"
)

print(
    f"Nested value: {nested_tuple_value}"
)


# =============================================================================
# Example 14: Heterogeneous Tuple
# =============================================================================

heterogeneous_tuple_values: tuple[object, ...] = (
    25,
    3.14,
    "Python",
    True,
)

print(
    heterogeneous_tuple_values
)


# =============================================================================
# Example 15: Tuple Iteration
# =============================================================================

tuple_iteration_values: tuple[str, ...] = (
    "Python",
    "SQL",
    "Airflow",
)

for tuple_iteration_item in tuple_iteration_values:
    print(tuple_iteration_item)


# =============================================================================
# Example 16: Iteration With enumerate()
# =============================================================================

tuple_enumeration_values: tuple[str, ...] = (
    "Python",
    "SQL",
    "Airflow",
)

for tuple_enumeration_index, tuple_enumeration_item in enumerate(
    tuple_enumeration_values
):
    print(
        f"Index: {tuple_enumeration_index}, "
        f"Value: {tuple_enumeration_item}"
    )


# =============================================================================
# Example 17: Membership Testing
# =============================================================================

tuple_membership_values: tuple[str, ...] = (
    "Python",
    "SQL",
    "Spark",
)

tuple_python_present: bool = (
    "Python" in tuple_membership_values
)

tuple_java_present: bool = (
    "Java" in tuple_membership_values
) # pyright: ignore[reportUnnecessaryContains]

print(
    f"Python present: {tuple_python_present}"
)

print(
    f"Java present:   {tuple_java_present}"
)


# =============================================================================
# Example 18: Tuple Concatenation
# =============================================================================

tuple_first_group: tuple[str, ...] = (
    "Python",
    "SQL",
)

tuple_second_group: tuple[str, ...] = (
    "Spark",
    "Airflow",
)

combined_tuple_groups: tuple[str, ...] = (
    tuple_first_group
    + tuple_second_group
)

print(
    f"Combined tuple: {combined_tuple_groups}"
)


# =============================================================================
# Example 19: Tuple Repetition
# =============================================================================

repeated_tuple_values: tuple[int, ...] = (
    0,
) * 5

print(
    f"Repeated tuple: {repeated_tuple_values}"
)


# =============================================================================
# Example 20: Tuple Immutability
# =============================================================================

immutable_tuple_sample: tuple[int, ...] = (
    10,
    20,
    30,
)

print(
    f"Original tuple: {immutable_tuple_sample}"
)


# The following operation is invalid:
#
#     immutable_tuple_sample[0] = 100
#
# A tuple does not support item assignment because tuples are immutable.


# =============================================================================
# Example 21: Tuple Methods
# =============================================================================

tuple_method_values: tuple[int, ...] = (
    10,
    20,
    10,
    30,
    10,
)

tuple_count_result: int = (
    tuple_method_values.count(10)
)

tuple_index_result: int = (
    tuple_method_values.index(30)
)

print(
    f"10 occurs: {tuple_count_result} times"
)

print(
    f"30 index: {tuple_index_result}"
)


# =============================================================================
# Example 22: min(), max(), and sum()
# =============================================================================

tuple_numeric_summary: tuple[int, ...] = (
    10,
    20,
    30,
    40,
)

tuple_minimum_value: int = min(
    tuple_numeric_summary
)

tuple_maximum_value: int = max(
    tuple_numeric_summary
)

tuple_sum_value: int = sum(
    tuple_numeric_summary
)

print(
    f"Minimum: {tuple_minimum_value}"
)

print(
    f"Maximum: {tuple_maximum_value}"
)

print(
    f"Sum:     {tuple_sum_value}"
)


# =============================================================================
# Example 23: sorted() With a Tuple
# =============================================================================

unsorted_tuple_values: tuple[int, ...] = (
    40,
    10,
    30,
    20,
)

sorted_tuple_result: list[int] = sorted(
    unsorted_tuple_values
)

print(
    f"Original tuple: {unsorted_tuple_values}"
)

print(
    f"Sorted result:  {sorted_tuple_result}"
)


# `sorted()` returns a list even when the input is a tuple.


# =============================================================================
# Example 24: Tuple Conversion From a List
# =============================================================================

source_conversion_list: list[int] = [
    10,
    20,
    30,
]

converted_tuple_value: tuple[int, ...] = tuple(
    source_conversion_list
)

print(
    f"List:  {source_conversion_list}"
)

print(
    f"Tuple: {converted_tuple_value}"
)


# =============================================================================
# Example 25: List Conversion From a Tuple
# =============================================================================

source_conversion_tuple: tuple[int, ...] = (
    100,
    200,
    300,
)

converted_list_value: list[int] = list(
    source_conversion_tuple
)

print(
    f"Tuple: {source_conversion_tuple}"
)

print(
    f"List:  {converted_list_value}"
)


# =============================================================================
# Example 26: Equality
# =============================================================================

tuple_equality_left: tuple[int, ...] = (
    1,
    2,
    3,
)

tuple_equality_right: tuple[int, ...] = (
    1,
    2,
    3,
)

tuple_equality_result: bool = (
    tuple_equality_left
    == tuple_equality_right
)

print(
    f"Equal tuple values: {tuple_equality_result}"
)


# =============================================================================
# Example 27: Identity
# =============================================================================

tuple_identity_source: tuple[int, ...] = (
    1,
    2,
    3,
)

tuple_identity_copy: tuple[int, ...] = tuple(
    list(tuple_identity_source)
)

tuple_identity_result: bool = (
    tuple_identity_source
    is tuple_identity_copy
)

print(
    f"Same tuple object: {tuple_identity_result}"
)


# =============================================================================
# Example 28: Tuple Containing a Mutable Object
# =============================================================================

tuple_with_nested_list: tuple[list[int], ...] = (
    [10, 20, 30],
)

tuple_nested_list: list[int] = (
    tuple_with_nested_list[0]
)

tuple_nested_list.append(40)

print(
    f"Tuple: {tuple_with_nested_list}"
)


# The tuple itself is immutable.
#
# However, the tuple can contain a mutable object.
#
# Therefore, the nested list can still be modified.
#
# This distinction is important:
#
#     tuple[0] = another_value
#
# is not allowed.
#
# But:
#
#     tuple[0].append(...)
#
# can be allowed when tuple[0] is a mutable list.


# =============================================================================
# Example 29: Tuple as a Dictionary Key
# =============================================================================

coordinate_key_tuple: tuple[int, int] = (
    10,
    20,
)

coordinate_mapping: dict[
    tuple[int, int],
    str,
] = {
    coordinate_key_tuple: "Point A",
}

print(
    coordinate_mapping
)


# Tuples containing only hashable elements can themselves be hashable.
#
# This allows them to be used as dictionary keys.


# =============================================================================
# Example 30: Tuple as a Set Element
# =============================================================================

tuple_set_member: tuple[str, str] = (
    "Python",
    "SQL",
)

tuple_container_set: set[tuple[str, str]] = {
    tuple_set_member,
}

print(
    tuple_container_set
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `tuple` represents an ordered, immutable collection of objects.

✓ `()` is a commonly used default-like tuple value.

✓ A type annotation alone does not initialize a variable.

✓ A single-element tuple requires a trailing comma:
      (100,)

✓ Tuples support:
      - indexing
      - negative indexing
      - slicing
      - iteration
      - membership testing

✓ Tuples can contain nested tuples and other Python objects.

✓ Tuples can be heterogeneous.

✓ Tuple packing groups multiple values into one tuple.

✓ Tuple unpacking assigns tuple elements to separate variables.

✓ Extended unpacking uses `*` to collect multiple values.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of elements.

✓ `+` concatenates tuples.

✓ `*` repeats tuples.

✓ Tuples cannot have their elements directly reassigned.

✓ Tuples provide:
      count()
      index()

✓ `min()`, `max()`, and `sum()` work with suitable tuples.

✓ `sorted()` accepts a tuple but returns a list.

✓ `tuple()` converts an iterable into a tuple.

✓ `list()` converts an iterable into a list.

✓ `==` compares tuple values.

✓ `is` compares object identity.

✓ A tuple can contain mutable objects such as lists.

✓ A tuple containing a mutable object is immutable at the tuple level, but
  the nested mutable object can still be modified.

✓ Tuples containing only hashable elements can be used as dictionary keys
  or set elements.

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================