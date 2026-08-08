"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Set (`set`)

Overview
--------
A set is an unordered, mutable collection of unique hashable objects.

Sets are useful when:

    - Duplicate values need to be removed.
    - Membership testing is important.
    - Mathematical set operations are required.
    - The order of elements is not important.

Sets are:

    - Unordered
    - Mutable
    - Iterable
    - Not indexable
    - Not sliceable
    - Capable of storing only hashable elements
    - Unable to contain duplicate elements

Examples:

    set()
    {1, 2, 3}
    {"Python", "SQL", "Airflow"}

Important:
    {} creates an empty dictionary, NOT an empty set.

This module covers:

    - Set literals
    - Default and non-default values
    - Empty sets
    - Duplicate removal
    - Type identification
    - Runtime type checking
    - Length
    - Membership testing
    - Iteration
    - Adding elements
    - Removing elements
    - Set union
    - Set intersection
    - Set difference
    - Symmetric difference
    - Subsets
    - Supersets
    - Disjoint sets
    - Set methods
    - Set conversion
    - Set immutability of elements
    - Hashable element requirement

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Set Literals
# =============================================================================

empty_set_value: set[int] = set()

numeric_set_value: set[int] = {
    10,
    20,
    30,
}

text_set_value: set[str] = {
    "Python",
    "SQL",
    "Airflow",
}

mixed_set_value: set[object] = {
    10,
    "Python",
    3.14,
    True,
}

print(f"Empty set:   {empty_set_value}")
print(f"Numeric set: {numeric_set_value}")
print(f"Text set:    {text_set_value}")
print(f"Mixed set:   {mixed_set_value}")


# =============================================================================
# Example 2: Default and Non-Default Set Values
# =============================================================================

default_like_set_value: set[int] = set()

non_default_set_primary: set[int] = {
    1,
    2,
    3,
}

non_default_set_secondary: set[str] = {
    "Python",
    "SQL",
}

print(
    f"Default-like set: {default_like_set_value}"
)

print(
    f"First set:        {non_default_set_primary}"
)

print(
    f"Second set:       {non_default_set_secondary}"
)


# Python does NOT automatically assign set() to an annotated set variable.
#
# This:
#
#     values: set[int]
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: set[int] = set()


# =============================================================================
# Example 3: Empty Set vs Empty Dictionary
# =============================================================================

empty_set_literal: set[object] = set()

empty_dictionary_literal: dict[object, object] = {}

print(
    f"Empty set:        {empty_set_literal}"
)

print(
    f"Empty dictionary: {empty_dictionary_literal}"
)

print(
    f"Empty set type:        {type(empty_set_literal)}"
)

print(
    f"Empty dictionary type: {type(empty_dictionary_literal)}"
)


# Important:
#
#     {}
#
# creates an empty dictionary.
#
# To create an empty set:
#
#     set()


# =============================================================================
# Example 4: Duplicate Values
# =============================================================================

duplicate_number_set: set[int] = {
    10,
    20,
    10,
    30,
    20,
}

print(
    f"Set with duplicates: {duplicate_number_set}"
)


# Sets automatically keep only unique values.
#
# Therefore, duplicate values are discarded when the set is created.


# =============================================================================
# Example 5: Type Identification
# =============================================================================

set_type_sample: set[int] = {
    5,
    10,
    15,
}

print(
    f"Value: {set_type_sample}"
)

print(
    f"Type:  {type(set_type_sample)}"
)


# Expected:
#
#     <class 'set'>


# =============================================================================
# Example 6: Runtime Set Type Checking
# =============================================================================

set_runtime_candidate: object = {
    1,
    2,
    3,
}

list_runtime_candidate_for_set: object = [
    1,
    2,
    3,
]

set_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    set_runtime_candidate,
    set,
)

list_set_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    list_runtime_candidate_for_set,
    set,
)

print(
    f"{{1, 2, 3}} is a set: "
    f"{set_runtime_check}"
)

print(
    f"[1, 2, 3] is a set: "
    f"{list_set_check}"
)


# The candidates are intentionally typed as `object`.
#
# The Pyright suppression is used because this example intentionally
# demonstrates runtime isinstance() behaviour.


# =============================================================================
# Example 7: Set Length
# =============================================================================

set_length_sample: set[str] = {
    "Python",
    "SQL",
    "Spark",
    "Airflow",
}

set_length_result: int = len(
    set_length_sample
)

print(
    f"Set length: {set_length_result}"
)


# `len()` returns the number of unique elements in the set.


# =============================================================================
# Example 8: Membership Testing
# =============================================================================

set_membership_values: set[str] = {
    "Python",
    "SQL",
    "Spark",
}

python_set_membership: bool = (
    "Python" in set_membership_values
)

java_set_membership: bool = (
    "Java" in set_membership_values
)

print(
    f"Python present: {python_set_membership}"
)

print(
    f"Java present:   {java_set_membership}"
)


# `in` and `not in` are particularly useful with sets.
#
# Set membership testing is generally efficient because sets are hash-based.


# =============================================================================
# Example 9: Set Iteration
# =============================================================================

set_iteration_values: set[str] = {
    "Python",
    "SQL",
    "Airflow",
}

for set_iteration_item in set_iteration_values:
    print(set_iteration_item)


# Sets are iterable.
#
# However, sets do not provide positional indexing.


# =============================================================================
# Example 10: Sets Do Not Support Indexing
# =============================================================================

non_indexable_set: set[int] = {
    10,
    20,
    30,
}

# The following operation is invalid:
#
#     non_indexable_set[0]
#
# Sets are not sequence types and therefore do not support indexing.


# =============================================================================
# Example 11: Sets Do Not Support Slicing
# =============================================================================

non_sliceable_set: set[int] = {
    10,
    20,
    30,
}

# The following operation is invalid:
#
#     non_sliceable_set[0:2]
#
# Sets do not support slicing.


# =============================================================================
# Example 12: add()
# =============================================================================

add_demo_set: set[str] = {
    "Python",
    "SQL",
}

add_demo_set.add(
    "Airflow"
)

print(
    f"After add(): {add_demo_set}"
)


# `add()` inserts one element into the set.


# =============================================================================
# Example 13: Adding an Existing Element
# =============================================================================

existing_element_set: set[int] = {
    10,
    20,
    30,
}

existing_element_set.add(
    20
)

print(
    f"After adding existing value: "
    f"{existing_element_set}"
)


# Adding an element that already exists does not create a duplicate.


# =============================================================================
# Example 14: update()
# =============================================================================

update_demo_set: set[str] = {
    "Python",
}

update_demo_set.update(
    {
        "SQL",
        "Airflow",
    }
)

print(
    f"After update(): {update_demo_set}"
)


# `update()` adds elements from one or more iterables.


# =============================================================================
# Example 15: remove()
# =============================================================================

remove_demo_set: set[str] = {
    "Python",
    "SQL",
    "Airflow",
}

remove_demo_set.remove(
    "SQL"
)

print(
    f"After remove(): {remove_demo_set}"
)


# `remove()` deletes the specified element.
#
# If the element does not exist, KeyError is raised.


# =============================================================================
# Example 16: discard()
# =============================================================================

discard_demo_set: set[str] = {
    "Python",
    "SQL",
    "Airflow",
}

discard_demo_set.discard(
    "Java"
)

print(
    f"After discard(): {discard_demo_set}"
)


# `discard()` removes an element if it exists.
#
# If the element does not exist, no error is raised.


# =============================================================================
# Example 17: pop()
# =============================================================================

pop_demo_set: set[str] = {
    "Python",
    "SQL",
    "Airflow",
}

removed_set_value: str = pop_demo_set.pop()

print(
    f"Removed value: {removed_set_value}"
)

print(
    f"Remaining set: {pop_demo_set}"
)


# `pop()` removes and returns an arbitrary element.
#
# Because sets are unordered, you should not rely on which element is removed.


# =============================================================================
# Example 18: clear()
# =============================================================================

clear_demo_set: set[int] = {
    10,
    20,
    30,
}

clear_demo_set.clear()

print(
    f"After clear(): {clear_demo_set}"
)


# `clear()` removes all elements from the set.


# =============================================================================
# Example 19: Set Union
# =============================================================================

python_tools_group: set[str] = {
    "Python",
    "Pandas",
    "SQL",
}

data_engineering_tools_group: set[str] = {
    "SQL",
    "Airflow",
    "Spark",
}

combined_tools_union: set[str] = (
    python_tools_group
    | data_engineering_tools_group
)

print(
    f"Union: {combined_tools_union}"
)


# Union contains all unique elements from both sets.
#
# Operator:
#
#     |


# =============================================================================
# Example 20: union()
# =============================================================================

union_method_left: set[int] = {
    1,
    2,
    3,
}

union_method_right: set[int] = {
    3,
    4,
    5,
}

union_method_result: set[int] = (
    union_method_left.union(
        union_method_right
    )
)

print(
    f"Union result: {union_method_result}"
)


# `union()` performs the same conceptual operation as `|`.


# =============================================================================
# Example 21: Set Intersection
# =============================================================================

intersection_left_set: set[str] = {
    "Python",
    "SQL",
    "Pandas",
}

intersection_right_set: set[str] = {
    "SQL",
    "Airflow",
    "Pandas",
}

intersection_result_set: set[str] = (
    intersection_left_set
    & intersection_right_set
)

print(
    f"Intersection: {intersection_result_set}"
)


# Intersection contains only elements common to both sets.
#
# Operator:
#
#     &


# =============================================================================
# Example 22: intersection()
# =============================================================================

intersection_method_left: set[int] = {
    1,
    2,
    3,
}

intersection_method_right: set[int] = {
    2,
    3,
    4,
}

intersection_method_result: set[int] = (
    intersection_method_left.intersection(
        intersection_method_right
    )
)

print(
    f"Intersection result: {intersection_method_result}"
)


# =============================================================================
# Example 23: Set Difference
# =============================================================================

difference_left_set: set[str] = {
    "Python",
    "SQL",
    "Pandas",
}

difference_right_set: set[str] = {
    "SQL",
    "Airflow",
}

difference_result_set: set[str] = (
    difference_left_set
    - difference_right_set
)

print(
    f"Difference: {difference_result_set}"
)


# Difference contains elements present in the left set but not the right set.
#
# Operator:
#
#     -


# =============================================================================
# Example 24: difference()
# =============================================================================

difference_method_left: set[int] = {
    1,
    2,
    3,
}

difference_method_right: set[int] = {
    2,
    3,
    4,
}

difference_method_result: set[int] = (
    difference_method_left.difference(
        difference_method_right
    )
)

print(
    f"Difference result: {difference_method_result}"
)


# =============================================================================
# Example 25: Symmetric Difference
# =============================================================================

symmetric_difference_left: set[str] = {
    "Python",
    "SQL",
    "Pandas",
}

symmetric_difference_right: set[str] = {
    "SQL",
    "Airflow",
    "Spark",
}

symmetric_difference_result: set[str] = (
    symmetric_difference_left
    ^ symmetric_difference_right
)

print(
    f"Symmetric difference: "
    f"{symmetric_difference_result}"
)


# Symmetric difference contains elements that belong to either set,
# but not to both.
#
# Operator:
#
#     ^


# =============================================================================
# Example 26: symmetric_difference()
# =============================================================================

symmetric_method_left: set[int] = {
    1,
    2,
    3,
}

symmetric_method_right: set[int] = {
    3,
    4,
    5,
}

symmetric_method_result: set[int] = (
    symmetric_method_left.symmetric_difference(
        symmetric_method_right
    )
)

print(
    f"Symmetric result: {symmetric_method_result}"
)


# =============================================================================
# Example 27: Subset
# =============================================================================

subset_small_set: set[int] = {
    1,
    2,
}

subset_large_set: set[int] = {
    1,
    2,
    3,
    4,
}

subset_check_result: bool = (
    subset_small_set
    <= subset_large_set
)

print(
    f"Is subset: {subset_check_result}"
)


# `<=` checks whether every element of the left set exists in the right set.


# =============================================================================
# Example 28: Proper Subset
# =============================================================================

proper_subset_small: set[int] = {
    1,
    2,
}

proper_subset_large: set[int] = {
    1,
    2,
    3,
}

proper_subset_result: bool = (
    proper_subset_small
    < proper_subset_large
)

print(
    f"Is proper subset: {proper_subset_result}"
)


# `<` checks for a proper subset.
#
# The two sets must not be equal.


# =============================================================================
# Example 29: Superset
# =============================================================================

superset_large_set: set[int] = {
    1,
    2,
    3,
    4,
}

superset_small_set: set[int] = {
    1,
    2,
}

superset_check_result: bool = (
    superset_large_set
    >= superset_small_set
)

print(
    f"Is superset: {superset_check_result}"
)


# `>=` checks whether the left set contains every element of the right set.


# =============================================================================
# Example 30: Proper Superset
# =============================================================================

proper_superset_large: set[int] = {
    1,
    2,
    3,
}

proper_superset_small: set[int] = {
    1,
    2,
}

proper_superset_result: bool = (
    proper_superset_large
    > proper_superset_small
)

print(
    f"Is proper superset: {proper_superset_result}"
)


# =============================================================================
# Example 31: isdisjoint()
# =============================================================================

first_disjoint_set: set[int] = {
    1,
    2,
    3,
}

second_disjoint_set: set[int] = {
    4,
    5,
    6,
}

disjoint_check_result: bool = (
    first_disjoint_set.isdisjoint(
        second_disjoint_set
    )
)

print(
    f"Are sets disjoint: {disjoint_check_result}"
)


# `isdisjoint()` returns True when the sets have no common elements.


# =============================================================================
# Example 32: Set Conversion
# =============================================================================

duplicate_source_list: list[int] = [
    10,
    20,
    10,
    30,
    20,
]

unique_values_from_list: set[int] = set(
    duplicate_source_list
)

print(
    f"Original list: {duplicate_source_list}"
)

print(
    f"Unique values: {unique_values_from_list}"
)


# Converting a sequence to a set is a common way to remove duplicate values.
#
# However, the original ordering should not be relied upon after conversion
# to a set.


# =============================================================================
# Example 33: Set Conversion Back to List
# =============================================================================

unique_number_set: set[int] = {
    10,
    20,
    30,
}

converted_set_list: list[int] = list(
    unique_number_set
)

print(
    f"Set:  {unique_number_set}"
)

print(
    f"List: {converted_set_list}"
)


# Converting a set to a list creates a list of the set's elements.
#
# The original set ordering should not be assumed.


# =============================================================================
# Example 34: Heterogeneous Set
# =============================================================================

heterogeneous_set_values: set[object] = {
    10,
    3.14,
    "Python",
    True,
}

print(
    heterogeneous_set_values
)


# Sets can contain different types as long as every element is hashable.


# =============================================================================
# Example 35: Hashable Elements
# =============================================================================

hashable_element_set: set[object] = {
    10,
    "Python",
    (1, 2),
}

print(
    f"Hashable elements: {hashable_element_set}"
)


# Integers, strings, and tuples containing hashable elements can be members
# of a set.


# =============================================================================
# Example 36: Mutable Elements Are Not Allowed
# =============================================================================

invalid_list_element_set: set[object] = set()

# The following operation is invalid:
#
#     invalid_list_element_set.add([1, 2, 3])
#
# A list is mutable and therefore unhashable.
#
# Set elements must be hashable.


# =============================================================================
# Example 37: Tuple vs List as Set Elements
# =============================================================================

tuple_set_element: tuple[int, int] = (
    10,
    20,
)

valid_nested_set: set[tuple[int, int]] = {
    tuple_set_element,
}

print(
    f"Set containing tuple: {valid_nested_set}"
)


# A tuple containing only hashable elements can be a set element.
#
# A list cannot be a set element because lists are unhashable.


# =============================================================================
# Example 38: Set Equality
# =============================================================================

set_equality_left: set[int] = {
    1,
    2,
    3,
}

set_equality_right: set[int] = {
    3,
    2,
    1,
}

set_equality_result: bool = (
    set_equality_left
    == set_equality_right
)

print(
    f"Equal sets: {set_equality_result}"
)


# Set equality is based on membership, not element order.


# =============================================================================
# Example 39: Set Identity
# =============================================================================

set_identity_source: set[int] = {
    1,
    2,
    3,
}

set_identity_copy: set[int] = set(
    set_identity_source
)

set_identity_result: bool = (
    set_identity_source
    is set_identity_copy
)

print(
    f"Same set object: {set_identity_result}"
)


# `==` checks whether the sets contain the same elements.
#
# `is` checks whether both variables refer to the exact same object.


# =============================================================================
# Example 40: Set Mutability
# =============================================================================

mutable_set_example: set[int] = {
    10,
    20,
    30,
}

mutable_set_example.add(
    40
)

print(
    f"Modified set: {mutable_set_example}"
)


# Sets are mutable.
#
# Elements can be added or removed after the set is created.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `set` represents an unordered collection of unique hashable objects.

✓ `set()` creates an empty set.

✓ `{}` creates an empty dictionary, not an empty set.

✓ Sets automatically remove duplicate values.

✓ Sets are mutable.

✓ Sets are iterable.

✓ Sets do not support indexing.

✓ Sets do not support slicing.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of unique elements.

✓ `in` and `not in` perform membership testing.

✓ `add()` adds one element.

✓ `update()` adds elements from one or more iterables.

✓ `remove()` raises KeyError when the requested element does not exist.

✓ `discard()` does not raise an error when the requested element is absent.

✓ `pop()` removes and returns an arbitrary element.

✓ `clear()` removes all elements.

✓ Union combines unique elements from sets.

✓ Intersection returns common elements.

✓ Difference returns elements present only in the left set.

✓ Symmetric difference returns elements present in either set, but not both.

✓ `<=` checks subset relationships.

✓ `<` checks proper subset relationships.

✓ `>=` checks superset relationships.

✓ `>` checks proper superset relationships.

✓ `isdisjoint()` checks whether two sets have no common elements.

✓ Sets can contain heterogeneous values when those values are hashable.

✓ Mutable objects such as lists cannot be set elements.

✓ Tuples containing only hashable elements can be set elements.

✓ `set()` can convert an iterable into a set and remove duplicates.

✓ Converting to a set means element order should not be relied upon.

✓ `==` compares set contents.

✓ `is` compares object identity.

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================