"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Frozen Set (`frozenset`)

Overview
--------
A frozenset is an unordered, immutable collection of unique hashable objects.

A frozenset is similar to a set, but unlike a set, its contents cannot be
changed after creation.

Frozensets are:

    - Unordered
    - Immutable
    - Iterable
    - Not indexable
    - Not sliceable
    - Capable of storing only hashable elements
    - Capable of containing unique values
    - Hashable themselves

Examples:

    frozenset()
    frozenset({1, 2, 3})
    frozenset([1, 2, 3])
    frozenset("Python")

This module covers:

    - Frozenset literals
    - Default and non-default values
    - Empty frozensets
    - Duplicate removal
    - Type identification
    - Runtime type checking
    - Length
    - Membership testing
    - Iteration
    - Set operations
    - Subsets
    - Supersets
    - Disjoint sets
    - Frozenset methods
    - Conversion between set and frozenset
    - Hashability
    - Immutability
    - Frozenset as dictionary key
    - Frozenset as set element

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Frozenset Creation
# =============================================================================

empty_frozenset_value: frozenset[int] = frozenset()

numeric_frozenset_value: frozenset[int] = frozenset({
    10,
    20,
    30,
})

text_frozenset_value: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Airflow",
})

mixed_frozenset_value: frozenset[object] = frozenset({
    10,
    "Python",
    3.14,
    True,
})

print(
    f"Empty frozenset:   {empty_frozenset_value}"
)

print(
    f"Numeric frozenset: {numeric_frozenset_value}"
)

print(
    f"Text frozenset:    {text_frozenset_value}"
)

print(
    f"Mixed frozenset:   {mixed_frozenset_value}"
)


# =============================================================================
# Example 2: Default and Non-Default Frozenset Values
# =============================================================================

default_like_frozenset: frozenset[int] = frozenset()

non_default_frozenset_primary: frozenset[int] = frozenset({
    1,
    2,
    3,
})

non_default_frozenset_secondary: frozenset[str] = frozenset({
    "Python",
    "SQL",
})

print(
    f"Default-like frozenset: "
    f"{default_like_frozenset}"
)

print(
    f"First frozenset:        "
    f"{non_default_frozenset_primary}"
)

print(
    f"Second frozenset:       "
    f"{non_default_frozenset_secondary}"
)


# Python does NOT automatically assign frozenset() to an annotated variable.
#
# This:
#
#     values: frozenset[int]
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: frozenset[int] = frozenset()


# =============================================================================
# Example 3: Empty Set vs Empty Frozenset
# =============================================================================

empty_mutable_set: set[object] = set()

empty_immutable_set: frozenset[object] = frozenset()

print(
    f"Empty set:       {empty_mutable_set}"
)

print(
    f"Empty frozenset: {empty_immutable_set}"
)

print(
    f"Empty set type:       "
    f"{type(empty_mutable_set)}"
)

print(
    f"Empty frozenset type: "
    f"{type(empty_immutable_set)}"
)


# `set()` creates an empty mutable set.
#
# `frozenset()` creates an empty immutable frozenset.


# =============================================================================
# Example 4: Duplicate Values
# =============================================================================

duplicate_frozenset_values: frozenset[int] = frozenset([
    10,
    20,
    10,
    30,
    20,
])

print(
    f"Frozenset with duplicates: "
    f"{duplicate_frozenset_values}"
)


# Like a set, a frozenset stores only unique values.


# =============================================================================
# Example 5: Creating a Frozenset From a String
# =============================================================================

string_source_for_frozenset: str = "banana"

character_frozenset_value: frozenset[str] = frozenset(
    string_source_for_frozenset
)

print(
    f"Source string:      "
    f"{string_source_for_frozenset}"
)

print(
    f"Character frozenset:"
    f" {character_frozenset_value}"
)


# `frozenset()` accepts an iterable.
#
# A string is iterable character by character.
#
# Duplicate characters are removed.


# =============================================================================
# Example 6: Type Identification
# =============================================================================

frozenset_type_sample: frozenset[int] = frozenset({
    5,
    10,
    15,
})

print(
    f"Value: {frozenset_type_sample}"
)

print(
    f"Type:  {type(frozenset_type_sample)}"
)


# Expected:
#
#     <class 'frozenset'>


# =============================================================================
# Example 7: Runtime Frozenset Type Checking
# =============================================================================

frozenset_runtime_candidate: object = frozenset({
    1,
    2,
    3,
})

set_runtime_candidate_for_frozenset: object = {
    1,
    2,
    3,
}

frozenset_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    frozenset_runtime_candidate,
    frozenset,
)

set_frozenset_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    set_runtime_candidate_for_frozenset,
    frozenset,
)

print(
    f"frozenset({{1, 2, 3}}) is a frozenset: "
    f"{frozenset_runtime_check}"
)

print(
    f"{{1, 2, 3}} is a frozenset: "
    f"{set_frozenset_check}"
)


# The candidates are intentionally typed as `object`.
#
# The Pyright suppression is used because this example intentionally
# demonstrates runtime isinstance() behaviour.


# =============================================================================
# Example 8: Frozenset Length
# =============================================================================

frozenset_length_sample: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Spark",
    "Airflow",
})

frozenset_length_result: int = len(
    frozenset_length_sample
)

print(
    f"Frozenset length: {frozenset_length_result}"
)


# =============================================================================
# Example 9: Membership Testing
# =============================================================================

frozenset_membership_values: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Spark",
})

python_frozenset_present: bool = (
    "Python" in frozenset_membership_values
)

java_frozenset_present: bool = (
    "Java" in frozenset_membership_values
)

print(
    f"Python present: {python_frozenset_present}"
)

print(
    f"Java present:   {java_frozenset_present}"
)


# `in` and `not in` can be used for membership testing.


# =============================================================================
# Example 10: Frozenset Iteration
# =============================================================================

frozenset_iteration_values: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Airflow",
})

for frozenset_iteration_item in (
    frozenset_iteration_values
):
    print(frozenset_iteration_item)


# Frozensets are iterable.
#
# They do not provide positional indexing.


# =============================================================================
# Example 11: Frozensets Do Not Support Indexing
# =============================================================================

non_indexable_frozenset: frozenset[int] = frozenset({
    10,
    20,
    30,
})

# The following operation is invalid:
#
#     non_indexable_frozenset[0]
#
# Frozensets are not sequence types.


# =============================================================================
# Example 12: Frozensets Do Not Support Slicing
# =============================================================================

non_sliceable_frozenset: frozenset[int] = frozenset({
    10,
    20,
    30,
})

# The following operation is invalid:
#
#     non_sliceable_frozenset[0:2]
#
# Frozensets do not support slicing.


# =============================================================================
# Example 13: Frozenset Immutability
# =============================================================================

immutable_frozenset_sample: frozenset[int] = frozenset({
    10,
    20,
    30,
})

print(
    f"Original frozenset: "
    f"{immutable_frozenset_sample}"
)


# The following operations are invalid:
#
#     immutable_frozenset_sample.add(40)
#
#     immutable_frozenset_sample.remove(10)
#
#     immutable_frozenset_sample.clear()
#
# Frozensets do not provide methods that modify their contents.


# =============================================================================
# Example 14: add() Is Not Available
# =============================================================================

add_unsupported_frozenset: frozenset[int] = frozenset({
    10,
    20,
})

# The following operation is invalid:
#
#     add_unsupported_frozenset.add(30)
#
# Unlike `set`, `frozenset` does not have `add()`.


# =============================================================================
# Example 15: Set Union
# =============================================================================

frozenset_union_left: frozenset[str] = frozenset({
    "Python",
    "SQL",
})

frozenset_union_right: frozenset[str] = frozenset({
    "SQL",
    "Airflow",
})

frozenset_union_result: frozenset[str] = (
    frozenset_union_left
    | frozenset_union_right
)

print(
    f"Union: {frozenset_union_result}"
)


# Frozensets support set operations.
#
# The result of operations between frozensets is generally a frozenset.


# =============================================================================
# Example 16: union()
# =============================================================================

frozenset_union_method_left: frozenset[int] = frozenset({
    1,
    2,
    3,
})

frozenset_union_method_right: frozenset[int] = frozenset({
    3,
    4,
    5,
})

frozenset_union_method_result: frozenset[int] = (
    frozenset_union_method_left.union(
        frozenset_union_method_right
    )
)

print(
    f"Union result: {frozenset_union_method_result}"
)


# =============================================================================
# Example 17: Intersection
# =============================================================================

frozenset_intersection_left: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Pandas",
})

frozenset_intersection_right: frozenset[str] = frozenset({
    "SQL",
    "Airflow",
    "Pandas",
})

frozenset_intersection_result: frozenset[str] = (
    frozenset_intersection_left
    & frozenset_intersection_right
)

print(
    f"Intersection: {frozenset_intersection_result}"
)


# =============================================================================
# Example 18: Difference
# =============================================================================

frozenset_difference_left: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Pandas",
})

frozenset_difference_right: frozenset[str] = frozenset({
    "SQL",
    "Airflow",
})

frozenset_difference_result: frozenset[str] = (
    frozenset_difference_left
    - frozenset_difference_right
)

print(
    f"Difference: {frozenset_difference_result}"
)


# =============================================================================
# Example 19: Symmetric Difference
# =============================================================================

frozenset_symmetric_left: frozenset[str] = frozenset({
    "Python",
    "SQL",
    "Pandas",
})

frozenset_symmetric_right: frozenset[str] = frozenset({
    "SQL",
    "Airflow",
    "Spark",
})

frozenset_symmetric_result: frozenset[str] = (
    frozenset_symmetric_left
    ^ frozenset_symmetric_right
)

print(
    f"Symmetric difference: "
    f"{frozenset_symmetric_result}"
)


# =============================================================================
# Example 20: Subset
# =============================================================================

frozenset_subset_small: frozenset[int] = frozenset({
    1,
    2,
})

frozenset_subset_large: frozenset[int] = frozenset({
    1,
    2,
    3,
    4,
})

frozenset_subset_result: bool = (
    frozenset_subset_small
    <= frozenset_subset_large
)

print(
    f"Is subset: {frozenset_subset_result}"
)


# =============================================================================
# Example 21: Proper Subset
# =============================================================================

frozenset_proper_subset_small: frozenset[int] = frozenset({
    1,
    2,
})

frozenset_proper_subset_large: frozenset[int] = frozenset({
    1,
    2,
    3,
})

frozenset_proper_subset_result: bool = (
    frozenset_proper_subset_small
    < frozenset_proper_subset_large
)

print(
    f"Is proper subset: "
    f"{frozenset_proper_subset_result}"
)


# =============================================================================
# Example 22: Superset
# =============================================================================

frozenset_superset_large: frozenset[int] = frozenset({
    1,
    2,
    3,
    4,
})

frozenset_superset_small: frozenset[int] = frozenset({
    1,
    2,
})

frozenset_superset_result: bool = (
    frozenset_superset_large
    >= frozenset_superset_small
)

print(
    f"Is superset: {frozenset_superset_result}"
)


# =============================================================================
# Example 23: Disjoint Sets
# =============================================================================

frozenset_disjoint_left: frozenset[int] = frozenset({
    1,
    2,
    3,
})

frozenset_disjoint_right: frozenset[int] = frozenset({
    4,
    5,
    6,
})

frozenset_disjoint_result: bool = (
    frozenset_disjoint_left.isdisjoint(
        frozenset_disjoint_right
    )
)

print(
    f"Are sets disjoint: "
    f"{frozenset_disjoint_result}"
)


# =============================================================================
# Example 24: Frozenset Conversion From Set
# =============================================================================

mutable_source_set: set[int] = {
    10,
    20,
    30,
}

converted_immutable_set: frozenset[int] = (
    frozenset(mutable_source_set)
)

print(
    f"Set:       {mutable_source_set}"
)

print(
    f"Frozenset: {converted_immutable_set}"
)


# `frozenset()` can create an immutable set from another iterable.


# =============================================================================
# Example 25: Set Conversion From Frozenset
# =============================================================================

immutable_source_set: frozenset[int] = frozenset({
    100,
    200,
    300,
})

converted_mutable_set: set[int] = set(
    immutable_source_set
)

print(
    f"Frozenset: {immutable_source_set}"
)

print(
    f"Set:       {converted_mutable_set}"
)


# `set()` creates a mutable set from a frozenset.


# =============================================================================
# Example 26: Frozenset as a Dictionary Key
# =============================================================================

permissions_frozenset: frozenset[str] = frozenset({
    "read",
    "write",
})

permission_mapping: dict[
    frozenset[str],
    str,
] = {
    permissions_frozenset: "Read/write access",
}

print(
    permission_mapping
)


# A frozenset is hashable.
#
# Therefore, it can be used as a dictionary key.


# =============================================================================
# Example 27: Frozenset as a Set Element
# =============================================================================

nested_frozenset_value: frozenset[int] = frozenset({
    1,
    2,
})

set_containing_frozenset: set[frozenset[int]] = {
    nested_frozenset_value,
}

print(
    f"Set containing frozenset: "
    f"{set_containing_frozenset}"
)


# A frozenset can be stored inside a set because it is hashable.
#
# A normal mutable set cannot be a set element.


# =============================================================================
# Example 28: Frozenset Equality
# =============================================================================

frozenset_equality_left: frozenset[int] = frozenset({
    1,
    2,
    3,
})

frozenset_equality_right: frozenset[int] = frozenset({
    3,
    2,
    1,
})

frozenset_equality_result: bool = (
    frozenset_equality_left
    == frozenset_equality_right
)

print(
    f"Equal frozensets: "
    f"{frozenset_equality_result}"
)


# Frozenset equality is based on membership.
#
# Element order does not matter.


# =============================================================================
# Example 29: Frozenset Identity
# =============================================================================

frozenset_identity_source: frozenset[int] = frozenset({
    1,
    2,
    3,
})

frozenset_identity_copy: frozenset[int] = frozenset(
    set(frozenset_identity_source)
)

frozenset_identity_result: bool = (
    frozenset_identity_source
    is frozenset_identity_copy
)

print(
    f"Same frozenset object: "
    f"{frozenset_identity_result}"
)


# `==` compares values.
#
# `is` compares object identity.


# =============================================================================
# Example 30: Frozenset vs Set
# =============================================================================

comparison_mutable_set: set[int] = {
    1,
    2,
    3,
}

comparison_immutable_set: frozenset[int] = frozenset({
    1,
    2,
    3,
})

print(
    f"Set:       {comparison_mutable_set}"
)

print(
    f"Frozenset: {comparison_immutable_set}"
)

print(
    f"Set type:       {type(comparison_mutable_set)}"
)

print(
    f"Frozenset type: {type(comparison_immutable_set)}"
)


# Main difference:
#
#     set       -> mutable
#     frozenset -> immutable
#
# Both support mathematical set operations.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `frozenset` represents an unordered, immutable collection of unique
  hashable objects.

✓ `frozenset()` creates an empty frozenset.

✓ A type annotation alone does not initialize a variable.

✓ Frozensets automatically remove duplicate values.

✓ Frozensets are immutable.

✓ Frozensets are iterable.

✓ Frozensets do not support indexing.

✓ Frozensets do not support slicing.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of unique elements.

✓ `in` and `not in` perform membership testing.

✓ Frozensets do not provide mutating methods such as:
      add()
      remove()
      discard()
      pop()
      clear()

✓ Frozensets support:
      union()
      intersection()
      difference()
      symmetric_difference()
      issubset()
      issuperset()
      isdisjoint()

✓ Frozensets support set operators:
      |
      &
      -
      ^

✓ Frozensets can be compared using subset and superset operators.

✓ Frozensets can be converted from sets and other iterables.

✓ Sets can be created from frozensets.

✓ Frozensets are hashable.

✓ A frozenset can be used as a dictionary key.

✓ A frozenset can be an element of another set.

✓ A normal mutable set cannot be a dictionary key or set element.

✓ `==` compares frozenset contents.

✓ `is` compares object identity.

✓ The major distinction is:

      set       -> mutable + unhashable
      frozenset -> immutable + hashable

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================