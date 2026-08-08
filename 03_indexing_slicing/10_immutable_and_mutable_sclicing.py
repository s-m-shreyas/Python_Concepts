"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Mutability and Immutability

Overview
--------
Mutability describes whether an object can be changed after it has been
created.

Mutable objects can be modified in place.

Immutable objects cannot be modified after creation. When a different value
is required, a new value must be produced and the variable can then refer to
that value.

Common examples:

    Mutable:
        list

    Immutable:
        str
        tuple
        int
        float
        bool

This distinction is especially important when working with indexing,
slicing, and copy operations.

Key Idea
--------
Indexing and slicing are operations.

Mutability is a property of the object being operated on.

Therefore:

    indexing/slicing
            +
    object mutability
            ↓
    determines what can happen next

Object identity can be inspected with:

    id(object)

Object identity can be compared with:

    object_a is object_b

Important
---------
`id()` shows object identity, not value equality.

Two objects can contain the same value while being different objects.

Also, Python may reuse immutable objects internally, so `id()` should not be
used as the definition of immutability.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html
"""


# =============================================================================
# Example 1: A List Is Mutable
# =============================================================================

mutable_numbers: list[int] = [
    10,
    20,
    30,
]

mutable_numbers_id_before: int = id(mutable_numbers)

print(
    f"Before modification: {mutable_numbers}"
)

print(
    f"Object ID:           {mutable_numbers_id_before}"
)

mutable_numbers[0] = 100

mutable_numbers_id_after: int = id(mutable_numbers)

print(
    f"After modification:  {mutable_numbers}"
)

print(
    f"Object ID:           {mutable_numbers_id_after}"
)

print(
    f"Same object:         "
    f"{mutable_numbers_id_before == mutable_numbers_id_after}"
)


# The list was modified in place.
#
# The values changed:
#
# [10, 20, 30]
#       ↓
# [100, 20, 30]
#
# The object itself remained the same object.


# =============================================================================
# Example 2: A String Is Immutable
# =============================================================================

immutable_text: str = "Python"

immutable_text_id_before: int = id(immutable_text)

print(
    f"Original string: {immutable_text}"
)

print(
    f"Object ID:       {immutable_text_id_before}"
)


# The following operation is invalid:
#
# immutable_text[0] = "J"
#
# Strings do not allow item assignment because they are immutable.
#
# Attempting it raises:
#
# TypeError


# =============================================================================
# Example 3: Producing a Different String Value
# =============================================================================

original_text_value: str = "Python"

original_text_id: int = id(original_text_value)

modified_text_value: str = (
    "J" + original_text_value[1:]
)

modified_text_id: int = id(modified_text_value)

print(
    f"Original value: {original_text_value}"
)

print(
    f"Original ID:    {original_text_id}"
)

print(
    f"New value:      {modified_text_value}"
)

print(
    f"New ID:         {modified_text_id}"
)

print(
    f"Same object:    "
    f"{original_text_value is modified_text_value}"
)


# We did not modify the original string.
#
# Instead:
#
# "Python"
#    ↓
# "Jython"
#
# A different string value is produced.
#
# The `is` comparison demonstrates whether the two variables refer to the
# same object in this particular execution.


# =============================================================================
# Example 4: Reassigning a Variable to a Different String
# =============================================================================

reassigned_text: str = "Python"

reassigned_text_id_before: int = id(reassigned_text)

print(
    f"Before reassignment: {reassigned_text}"
)

print(
    f"Object ID:           {reassigned_text_id_before}"
)

reassigned_text = "Jython"

reassigned_text_id_after: int = id(reassigned_text)

print(
    f"After reassignment:  {reassigned_text}"
)

print(
    f"Object ID:           {reassigned_text_id_after}"
)

print(
    f"ID changed:          "
    f"{reassigned_text_id_before != reassigned_text_id_after}"
)


# The variable was reassigned.
#
# It is important to distinguish:
#
# modification:
#
#     changing the existing object
#
# from:
#
#     reassignment
#
#     making the variable refer to another value/object
#
# Strings cannot be modified in place, so a different value is assigned to
# the variable instead.


# =============================================================================
# Example 5: List Slicing Produces a New List
# =============================================================================

original_list_values: list[int] = [
    10,
    20,
    30,
    40,
]

original_list_id: int = id(original_list_values)

sliced_list_values: list[int] = (
    original_list_values[1:3]
)

sliced_list_id: int = id(sliced_list_values)

print(
    f"Original list: {original_list_values}"
)

print(
    f"Original ID:   {original_list_id}"
)

print(
    f"Sliced list:   {sliced_list_values}"
)

print(
    f"Sliced ID:     {sliced_list_id}"
)

print(
    f"Same object:   "
    f"{original_list_values is sliced_list_values}"
)


# The slice:
#
# original_list_values[1:3]
#
# creates another list object.
#
# Therefore:
#
# original_list_values is sliced_list_values
#
# -> False


# =============================================================================
# Example 6: Modifying the Sliced List
# =============================================================================

source_list_values: list[int] = [
    10,
    20,
    30,
    40,
]

copied_slice_values: list[int] = (
    source_list_values[:]
)

source_list_id: int = id(source_list_values)
copied_slice_id: int = id(copied_slice_values)

copied_slice_values[0] = 200

print(
    f"Original list: {source_list_values}"
)

print(
    f"Sliced list:   {copied_slice_values}"
)

print(
    f"Original ID:   {source_list_id}"
)

print(
    f"Sliced ID:     {copied_slice_id}"
)

print(
    f"Same object:   "
    f"{source_list_values is copied_slice_values}"
)


# The slice created a separate list.
#
# Therefore changing copied_slice_values does not modify source_list_values.


# =============================================================================
# Example 7: Tuple Is Immutable
# =============================================================================

immutable_coordinates: tuple[int, int, int] = (
    10,
    20,
    30,
)

immutable_coordinates_id: int = id(
    immutable_coordinates
)

print(
    f"Original tuple: {immutable_coordinates}"
)

print(
    f"Object ID:      {immutable_coordinates_id}"
)


# The following operation is invalid:
#
# immutable_coordinates[0] = 100
#
# Tuples do not support item assignment because they are immutable.


# =============================================================================
# Example 8: Slicing an Immutable Sequence
# =============================================================================

source_tuple_values: tuple[int, ...] = (
    10,
    20,
    30,
    40,
    50,
)

source_tuple_id: int = id(source_tuple_values)

sliced_tuple_values: tuple[int, ...] = (
    source_tuple_values[1:4]
)

sliced_tuple_id: int = id(sliced_tuple_values)

print(
    f"Original tuple: {source_tuple_values}"
)

print(
    f"Original ID:    {source_tuple_id}"
)

print(
    f"Sliced tuple:   {sliced_tuple_values}"
)

print(
    f"Sliced ID:      {sliced_tuple_id}"
)

print(
    f"Same object:    "
    f"{source_tuple_values is sliced_tuple_values}"
)


# The tuple itself is immutable.
#
# The slice produces another tuple containing the selected values.


# =============================================================================
# Example 9: Indexing Does Not Determine Mutability
# =============================================================================

indexed_list_values: list[int] = [
    10,
    20,
    30,
]

indexed_string_value: str = "ABC"

print(
    f"List element:   {indexed_list_values[0]}"
)

print(
    f"String element: {indexed_string_value[0]}"
)


# Both objects support indexing.
#
# However:
#
# list -> supports item assignment
# str  -> does not support item assignment
#
# The sequence type determines mutability.


# =============================================================================
# Example 10: Slicing Does Not Make an Object Mutable
# =============================================================================

immutable_source_text: str = "Python"

immutable_text_slice: str = (
    immutable_source_text[1:4]
)

immutable_source_id: int = id(immutable_source_text)
immutable_slice_id: int = id(immutable_text_slice)

print(
    f"Original text: {immutable_source_text}"
)

print(
    f"Original ID:   {immutable_source_id}"
)

print(
    f"Sliced text:   {immutable_text_slice}"
)

print(
    f"Sliced ID:     {immutable_slice_id}"
)

print(
    f"Same object:   "
    f"{immutable_source_text is immutable_text_slice}"
)


# The resulting object is still a string.
#
# Therefore it remains immutable.
#
# Slicing does not change:
#
# str -> immutable


# =============================================================================
# Example 11: Mutable Object Can Change Its Contents
# =============================================================================

mutable_values_example: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

mutable_values_example_id: int = id(
    mutable_values_example
)

mutable_values_example[1] = "Snowflake"

print(
    f"Modified values: {mutable_values_example}"
)

print(
    f"Object ID:       {id(mutable_values_example)}"
)

print(
    f"Same object:     "
    f"{mutable_values_example_id == id(mutable_values_example)}"
)


# The contents changed, but the list object remained the same object.


# =============================================================================
# Example 12: Immutable Object Requires a Different Value
# =============================================================================

immutable_number_value: int = 10

immutable_number_id_before: int = (
    id(immutable_number_value)
)

new_number_value: int = (
    immutable_number_value + 5
)

new_number_id: int = id(new_number_value)

print(
    f"Original value: {immutable_number_value}"
)

print(
    f"Original ID:    {immutable_number_id_before}"
)

print(
    f"New value:      {new_number_value}"
)

print(
    f"New ID:         {new_number_id}"
)


# Integers are immutable.
#
# The value 10 is not changed into 15.
#
# Instead, the expression produces the value 15.
#
# The variable names refer to integer objects representing those values.


# =============================================================================
# Example 13: Slicing and Mutability Are Separate Concepts
# =============================================================================

concept_list_values: list[int] = [
    10,
    20,
    30,
    40,
]

concept_text_value: str = "Python"

concept_list_slice: list[int] = (
    concept_list_values[1:3]
)

concept_text_slice: str = (
    concept_text_value[1:4]
)

print(
    f"List slice:   {concept_list_slice}"
)

print(
    f"String slice: {concept_text_slice}"
)


# Both operations are slicing.
#
# But:
#
# list -> mutable sequence
# str  -> immutable sequence
#
# Slicing itself does not determine mutability.


# =============================================================================
# Example 14: Modifying a List Slice
# =============================================================================

modifiable_slice_source: list[int] = [
    10,
    20,
    30,
    40,
]

modifiable_slice_result: list[int] = (
    modifiable_slice_source[1:3]
)

modifiable_source_id: int = id(
    modifiable_slice_source
)

modifiable_slice_id: int = id(
    modifiable_slice_result
)

modifiable_slice_result[0] = 200

print(
    f"Source list: {modifiable_slice_source}"
)

print(
    f"Slice result: {modifiable_slice_result}"
)

print(
    f"Source ID:   {modifiable_source_id}"
)

print(
    f"Slice ID:     {modifiable_slice_id}"
)

print(
    f"Same object:  "
    f"{modifiable_slice_source is modifiable_slice_result}"
)


# The source and slice are different list objects.
#
# Therefore modifying the slice does not modify the source list.


# =============================================================================
# Example 15: String Slice Cannot Be Modified
# =============================================================================

immutable_slice_source: str = "Python"

immutable_slice_result: str = (
    immutable_slice_source[1:4]
)

immutable_slice_source_id: int = id(
    immutable_slice_source
)

immutable_slice_result_id: int = id(
    immutable_slice_result
)

print(
    f"Source string: {immutable_slice_source}"
)

print(
    f"Source ID:     {immutable_slice_source_id}"
)

print(
    f"Slice result:  {immutable_slice_result}"
)

print(
    f"Slice ID:      {immutable_slice_result_id}"
)

print(
    f"Same object:   "
    f"{immutable_slice_source is immutable_slice_result}"
)


# The resulting object is a string.
#
# Therefore:
#
# immutable_slice_result[0] = "X"
#
# is invalid.
#
# The important point is not the ID.
#
# The important point is:
#
# str -> immutable


# =============================================================================
# Example 16: Mutability and Object Identity
# =============================================================================

identity_list_values: list[int] = [
    10,
    20,
    30,
]

identity_list_reference: list[int] = (
    identity_list_values
)

identity_shared_id: int = id(
    identity_list_values
)

print(
    f"Same list object: "
    f"{identity_list_values is identity_list_reference}"
)

print(
    f"First ID:         {identity_shared_id}"
)

print(
    f"Second ID:        {id(identity_list_reference)}"
)

identity_list_reference[0] = 100

print(
    f"Original variable:  {identity_list_values}"
)

print(
    f"Reference variable: {identity_list_reference}"
)


# Both variables refer to the same mutable list object.
#
# Therefore:
#
# identity_list_values is identity_list_reference
#
# -> True
#
# Changing the object through one reference is visible through the other.


# =============================================================================
# Example 17: Slice Creates a Separate List Object
# =============================================================================

identity_slice_source: list[int] = [
    10,
    20,
    30,
]

identity_slice_copy: list[int] = (
    identity_slice_source[:]
)

identity_source_id: int = id(
    identity_slice_source
)

identity_copy_id: int = id(
    identity_slice_copy
)

print(
    f"Source ID: {identity_source_id}"
)

print(
    f"Slice ID:  {identity_copy_id}"
)

print(
    f"Same object: "
    f"{identity_slice_source is identity_slice_copy}"
)


# Direct assignment:
#
# identity_slice_copy = identity_slice_source
#
# would make both variables refer to the same object.
#
# Slicing:
#
# identity_slice_copy = identity_slice_source[:]
#
# creates another list object.


# =============================================================================
# Example 18: Mutable vs Immutable Sequence Comparison
# =============================================================================

comparison_mutable_values: list[int] = [
    10,
    20,
    30,
]

comparison_immutable_values: tuple[int, ...] = (
    10,
    20,
    30,
)

comparison_mutable_id: int = id(
    comparison_mutable_values
)

comparison_immutable_id: int = id(
    comparison_immutable_values
)

comparison_mutable_values[0] = 100

print(
    f"Mutable sequence:   {comparison_mutable_values}"
)

print(
    f"Mutable ID:         {comparison_mutable_id}"
)

print(
    f"Immutable sequence: {comparison_immutable_values}"
)

print(
    f"Immutable ID:       {comparison_immutable_id}"
)


# Both sequences contain the same initial values.
#
# Their mutability is different:
#
# list  -> mutable
# tuple -> immutable


# =============================================================================
# Example 19: Slicing Does Not Mean Deep Copy
# =============================================================================

nested_mutable_source: list[list[int]] = [
    [10, 20],
    [30, 40],
]

nested_mutable_slice: list[list[int]] = (
    nested_mutable_source[:]
)

nested_source_id: int = id(
    nested_mutable_source
)

nested_slice_id: int = id(
    nested_mutable_slice
)

nested_source_inner_id: int = id(
    nested_mutable_source[0]
)

nested_slice_inner_id: int = id(
    nested_mutable_slice[0]
)

print(
    f"Source outer ID: {nested_source_id}"
)

print(
    f"Slice outer ID:  {nested_slice_id}"
)

print(
    f"Different outer objects: "
    f"{nested_mutable_source is not nested_mutable_slice}"
)

print(
    f"Source nested ID: {nested_source_inner_id}"
)

print(
    f"Slice nested ID:  {nested_slice_inner_id}"
)

print(
    f"Same nested object: "
    f"{nested_mutable_source[0] is nested_mutable_slice[0]}"
)

nested_mutable_slice[0][0] = 100

print(
    f"Original nested list: {nested_mutable_source}"
)

print(
    f"Sliced nested list:   {nested_mutable_slice}"
)


# This is an important connection to shallow copy.
#
# The outer lists are different objects:
#
# source outer ID != slice outer ID
#
# But their nested lists are the same objects:
#
# source nested ID == slice nested ID
#
# Therefore modifying the shared nested list affects both structures.


# =============================================================================
# Example 20: Core Relationship Between Slicing and Mutability
# =============================================================================

final_mutable_values: list[int] = [
    10,
    20,
    30,
    40,
]

final_immutable_values: str = "Python"

final_mutable_slice: list[int] = (
    final_mutable_values[1:3]
)

final_immutable_slice: str = (
    final_immutable_values[1:4]
)

print(
    f"Mutable source:    {final_mutable_values}"
)

print(
    f"Mutable slice:     {final_mutable_slice}"
)

print(
    f"Immutable source:  {final_immutable_values}"
)

print(
    f"Immutable slice:   {final_immutable_slice}"
)


# The slicing syntax is similar:
#
# list:
#
#     values[1:3]
#
# string:
#
#     text[1:4]
#
# But the resulting sequence retains the mutability characteristics
# of its type.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Mutability describes whether an object can be changed after creation.

✓ Mutable objects can be modified in place.

✓ Immutable objects cannot be modified in place.

✓ Lists are mutable.

✓ Strings are immutable.

✓ Tuples are immutable.

✓ Indexing is supported by both mutable and immutable sequences.

✓ Slicing is supported by both mutable and immutable sequences.

✓ Indexing and slicing do not determine mutability.

✓ The object's type determines its mutability behavior.

✓ A list can be modified through item assignment:

      values[0] = new_value

✓ A string cannot be modified through item assignment:

      text[0] = new_value

✓ When a different immutable value is required, a different value/object is
  produced and the variable can refer to it.

✓ `id()` can be used to observe object identity.

✓ `is` compares object identity.

✓ `id()` and `is` should not be used as the definition of mutability.

✓ Slicing a list creates a new outer list object.

✓ Slicing a tuple creates a tuple value.

✓ Slicing a string produces a string value.

✓ Slicing a nested list is shallow with respect to nested objects.

✓ In a shallow slice of a nested list:

      outer object -> different
      nested objects -> potentially shared

✓ The important conceptual relationship is:

      Sequence operation
             +
      Object mutability
             ↓
      determines what can be modified

✓ This module connects indexing, slicing, and copy operations with the broader
  Python concept of mutability and immutability.
"""


# =============================================================================
# End of File
# =============================================================================