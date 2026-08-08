"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Bytearray (`bytearray`)

Overview
--------
`bytearray` represents a mutable sequence of integers in the range:

    0 <= value <= 255

It is similar to `bytes`, but unlike `bytes`, a bytearray can be modified
after creation.

Bytearray is commonly used when binary data needs to be changed in place.

Examples:

    bytearray()
    bytearray(b"Python")
    bytearray([65, 66, 67])

Bytearrays are:

    - Mutable
    - Ordered
    - Iterable
    - Indexable
    - Sliceable
    - Capable of storing values from 0 to 255
    - Unhashable
    - Useful for mutable binary data

Important distinction:

    bytes
        -> immutable

    bytearray
        -> mutable

This module covers:

    - Bytearray creation
    - Default and non-default values
    - Empty bytearray
    - Byte values
    - Type identification
    - Runtime type checking
    - Length
    - Positive indexing
    - Negative indexing
    - Index assignment
    - Slicing
    - Slice assignment
    - Iteration
    - Membership testing
    - bytes conversion
    - String encoding
    - Decoding
    - append()
    - extend()
    - insert()
    - remove()
    - pop()
    - clear()
    - reverse()
    - replace()
    - hex()
    - fromhex()
    - Immutability vs mutability
    - Hashability
    - Equality
    - Identity

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Bytearray Creation
# =============================================================================

empty_bytearray_value: bytearray = bytearray()

text_bytearray_value: bytearray = bytearray(
    b"Python"
)

numeric_bytearray_value: bytearray = bytearray([
    65,
    66,
    67,
])

print(
    f"Empty bytearray:  {empty_bytearray_value!r}"
)

print(
    f"Text bytearray:   {text_bytearray_value!r}"
)

print(
    f"Numeric bytearray:"
    f" {numeric_bytearray_value!r}"
)


# =============================================================================
# Example 2: Default and Non-Default Bytearray Values
# =============================================================================

default_like_bytearray_value: bytearray = (
    bytearray()
)

non_default_bytearray_primary: bytearray = (
    bytearray(b"Python")
)

non_default_bytearray_secondary: bytearray = (
    bytearray([1, 2, 3])
)

print(
    f"Default-like bytearray: "
    f"{default_like_bytearray_value!r}"
)

print(
    f"First bytearray value:  "
    f"{non_default_bytearray_primary!r}"
)

print(
    f"Second bytearray value: "
    f"{non_default_bytearray_secondary!r}"
)


# Python does NOT automatically assign bytearray() to an annotated variable.
#
# This:
#
#     values: bytearray
#
# is only a type annotation.
#
# Explicit initialization is required:
#
#     values: bytearray = bytearray()


# =============================================================================
# Example 3: Empty Bytearray
# =============================================================================

empty_bytearray_sample: bytearray = (
    bytearray()
)

print(
    f"Value:  {empty_bytearray_sample!r}"
)

print(
    f"Length: {len(empty_bytearray_sample)}"
)

print(
    f"Type:   {type(empty_bytearray_sample)}"
)


# Expected:
#
#     Value:  bytearray(b'')
#     Length: 0
#     Type:   <class 'bytearray'>


# =============================================================================
# Example 4: Type Identification
# =============================================================================

bytearray_type_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Value: {bytearray_type_sample!r}"
)

print(
    f"Type:  {type(bytearray_type_sample)}"
)


# Expected:
#
#     <class 'bytearray'>


# =============================================================================
# Example 5: Runtime Bytearray Type Checking
# =============================================================================

bytearray_runtime_candidate: object = (
    bytearray(b"Python")
)

bytes_runtime_candidate_for_bytearray: object = (
    b"Python"
)

bytearray_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    bytearray_runtime_candidate,
    bytearray,
)

bytes_bytearray_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    bytes_runtime_candidate_for_bytearray,
    bytearray,
)

print(
    f"bytearray(b'Python') is bytearray: "
    f"{bytearray_runtime_check}"
)

print(
    f"b'Python' is bytearray: "
    f"{bytes_bytearray_check}"
)


# =============================================================================
# Example 6: Bytearray Length
# =============================================================================

bytearray_length_sample: bytearray = (
    bytearray(b"Python")
)

bytearray_length_result: int = len(
    bytearray_length_sample
)

print(
    f"Bytearray length: "
    f"{bytearray_length_result}"
)


# =============================================================================
# Example 7: Positive Indexing
# =============================================================================

positive_bytearray_index_sample: bytearray = (
    bytearray(b"Python")
)

positive_bytearray_first_value: int = (
    positive_bytearray_index_sample[0]
)

positive_bytearray_third_value: int = (
    positive_bytearray_index_sample[2]
)

print(
    f"First byte: {positive_bytearray_first_value}"
)

print(
    f"Third byte: {positive_bytearray_third_value}"
)


# Indexing a bytearray returns an integer.


# =============================================================================
# Example 8: Negative Indexing
# =============================================================================

negative_bytearray_index_sample: bytearray = (
    bytearray(b"Python")
)

negative_bytearray_last_value: int = (
    negative_bytearray_index_sample[-1]
)

negative_bytearray_second_last_value: int = (
    negative_bytearray_index_sample[-2]
)

print(
    f"Last byte:        {negative_bytearray_last_value}"
)

print(
    f"Second-last byte: "
    f"{negative_bytearray_second_last_value}"
)


# =============================================================================
# Example 9: Index Assignment
# =============================================================================

bytearray_index_assignment_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before assignment: "
    f"{bytearray_index_assignment_sample!r}"
)

bytearray_index_assignment_sample[0] = 74

print(
    f"After assignment:  "
    f"{bytearray_index_assignment_sample!r}"
)


# 74 is the ASCII value for "J".
#
# Therefore:
#
#     b"Python"
#
# becomes:
#
#     bytearray(b"Jython")


# =============================================================================
# Example 10: Invalid Byte Value
# =============================================================================

bytearray_invalid_value_sample: bytearray = (
    bytearray(b"Python")
)

# The following operations are invalid:
#
#     bytearray_invalid_value_sample[0] = 256
#
#     bytearray_invalid_value_sample[0] = -1
#
# Every assigned byte value must satisfy:
#
#     0 <= value <= 255


# =============================================================================
# Example 11: Bytearray Slicing
# =============================================================================

bytearray_slice_source: bytearray = (
    bytearray(b"Python")
)

bytearray_first_slice: bytearray = (
    bytearray_slice_source[0:3]
)

bytearray_second_slice: bytearray = (
    bytearray_slice_source[2:6]
)

print(
    f"Original:    {bytearray_slice_source!r}"
)

print(
    f"First slice: {bytearray_first_slice!r}"
)

print(
    f"Second slice:"
    f" {bytearray_second_slice!r}"
)


# Slicing a bytearray produces another bytearray.


# =============================================================================
# Example 12: Slice Assignment
# =============================================================================

bytearray_slice_assignment_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before slice assignment: "
    f"{bytearray_slice_assignment_sample!r}"
)

bytearray_slice_assignment_sample[0:2] = (
    b"Ja"
)

print(
    f"After slice assignment:  "
    f"{bytearray_slice_assignment_sample!r}"
)


# Slice assignment can modify multiple bytes at once.


# =============================================================================
# Example 13: Slice Assignment With Different Length
# =============================================================================

bytearray_variable_slice_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before: "
    f"{bytearray_variable_slice_sample!r}"
)

bytearray_variable_slice_sample[0:2] = (
    b"Data"
)

print(
    f"After:  "
    f"{bytearray_variable_slice_sample!r}"
)


# Unlike ordinary index assignment, slice assignment can change the
# total length of the bytearray.


# =============================================================================
# Example 14: Iteration
# =============================================================================

bytearray_iteration_sample: bytearray = (
    bytearray(b"ABC")
)

for bytearray_iteration_value in (
    bytearray_iteration_sample
):
    print(
        bytearray_iteration_value
    )


# Iterating over a bytearray produces integers.


# =============================================================================
# Example 15: Membership Testing
# =============================================================================

bytearray_membership_sample: bytearray = (
    bytearray(b"Python")
)

bytearray_integer_membership: bool = (
    80 in bytearray_membership_sample
)

bytearray_subsequence_membership: bool = (
    b"Python"
    in bytearray_membership_sample
)

print(
    f"80 is present: "
    f"{bytearray_integer_membership}"
)

print(
    f"b'Python' is present: "
    f"{bytearray_subsequence_membership}"
)


# =============================================================================
# Example 16: bytes() to bytearray()
# =============================================================================

source_bytes_for_bytearray: bytes = (
    b"Python"
)

converted_bytearray_from_bytes: bytearray = (
    bytearray(source_bytes_for_bytearray)
)

print(
    f"Bytes:     {source_bytes_for_bytearray!r}"
)

print(
    f"Bytearray: "
    f"{converted_bytearray_from_bytes!r}"
)


# =============================================================================
# Example 17: String Encoding to Bytearray
# =============================================================================

text_for_bytearray_encoding: str = (
    "Python"
)

encoded_bytearray_text: bytearray = (
    bytearray(
        text_for_bytearray_encoding,
        "utf-8",
    )
)

print(
    f"Text:      {text_for_bytearray_encoding!r}"
)

print(
    f"Bytearray: {encoded_bytearray_text!r}"
)


# A string can be converted to bytearray by specifying an encoding.


# =============================================================================
# Example 18: Bytearray decode()
# =============================================================================

encoded_bytearray_sample: bytearray = (
    bytearray(b"Python")
)

decoded_bytearray_text: str = (
    encoded_bytearray_sample.decode(
        "utf-8"
    )
)

print(
    f"Bytearray: {encoded_bytearray_sample!r}"
)

print(
    f"Text:      {decoded_bytearray_text!r}"
)


# `decode()` converts the byte data into a string.


# =============================================================================
# Example 19: append()
# =============================================================================

bytearray_append_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before append: "
    f"{bytearray_append_sample!r}"
)

bytearray_append_sample.append(33)

print(
    f"After append:  "
    f"{bytearray_append_sample!r}"
)


# 33 is the ASCII value for "!".

# append() modifies the bytearray in place.


# =============================================================================
# Example 20: extend()
# =============================================================================

bytearray_extend_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before extend: "
    f"{bytearray_extend_sample!r}"
)

bytearray_extend_sample.extend(
    b" SQL"
)

print(
    f"After extend:  "
    f"{bytearray_extend_sample!r}"
)


# extend() adds multiple byte values.


# =============================================================================
# Example 21: insert()
# =============================================================================

bytearray_insert_sample: bytearray = (
    bytearray(b"Pyton")
)

print(
    f"Before insert: "
    f"{bytearray_insert_sample!r}"
)

bytearray_insert_sample.insert(
    2,
    116,
)

print(
    f"After insert:  "
    f"{bytearray_insert_sample!r}"
)


# 116 is the ASCII value for "t".


# =============================================================================
# Example 22: remove()
# =============================================================================

bytearray_remove_sample: bytearray = (
    bytearray(b"Pyton")
)

print(
    f"Before remove: "
    f"{bytearray_remove_sample!r}"
)

bytearray_remove_sample.remove(116)

print(
    f"After remove:  "
    f"{bytearray_remove_sample!r}"
)


# remove() removes the first occurrence of the specified byte value.


# =============================================================================
# Example 23: pop()
# =============================================================================

bytearray_pop_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before pop: "
    f"{bytearray_pop_sample!r}"
)

bytearray_popped_value: int = (
    bytearray_pop_sample.pop()
)

print(
    f"Popped value: "
    f"{bytearray_popped_value}"
)

print(
    f"After pop:   "
    f"{bytearray_pop_sample!r}"
)


# pop() removes and returns a byte.
#
# Without an index, the last byte is removed.


# =============================================================================
# Example 24: clear()
# =============================================================================

bytearray_clear_sample: bytearray = (
    bytearray(b"Python")
)

bytearray_clear_sample.clear()

print(
    f"After clear(): "
    f"{bytearray_clear_sample!r}"
)


# clear() removes all bytes.


# =============================================================================
# Example 25: reverse()
# =============================================================================

bytearray_reverse_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Before reverse: "
    f"{bytearray_reverse_sample!r}"
)

bytearray_reverse_sample.reverse()

print(
    f"After reverse:  "
    f"{bytearray_reverse_sample!r}"
)


# reverse() modifies the bytearray in place.


# =============================================================================
# Example 26: replace()
# =============================================================================

bytearray_replace_sample: bytearray = (
    bytearray(b"Python SQL")
)

bytearray_replace_result: bytearray = (
    bytearray_replace_sample.replace(
        b"SQL",
        b"Airflow",
    )
)

print(
    f"Original: "
    f"{bytearray_replace_sample!r}"
)

print(
    f"Result:   "
    f"{bytearray_replace_result!r}"
)


# replace() returns a new bytearray.
#
# The original bytearray remains unchanged by this operation.


# =============================================================================
# Example 27: hex()
# =============================================================================

bytearray_hex_sample: bytearray = (
    bytearray(b"ABC")
)

bytearray_hex_result: str = (
    bytearray_hex_sample.hex()
)

print(
    f"Bytearray: "
    f"{bytearray_hex_sample!r}"
)

print(
    f"Hex:       "
    f"{bytearray_hex_result!r}"
)


# =============================================================================
# Example 28: fromhex()
# =============================================================================

hexadecimal_bytearray_source: str = (
    "41 42 43"
)

bytearray_from_hex_result: bytearray = (
    bytearray.fromhex(
        hexadecimal_bytearray_source
    )
)

print(
    f"Hex text: "
    f"{hexadecimal_bytearray_source!r}"
)

print(
    f"Bytearray:"
    f" {bytearray_from_hex_result!r}"
)


# =============================================================================
# Example 29: Mutability
# =============================================================================

mutable_bytearray_sample: bytearray = (
    bytearray(b"Python")
)

print(
    f"Original: "
    f"{mutable_bytearray_sample!r}"
)

mutable_bytearray_sample[0] = 74

print(
    f"Modified: "
    f"{mutable_bytearray_sample!r}"
)


# The same bytearray object was modified.


# =============================================================================
# Example 30: bytes vs bytearray
# =============================================================================

comparison_bytes_value: bytes = (
    b"Python"
)

comparison_bytearray_value: bytearray = (
    bytearray(b"Python")
)

print(
    f"bytes:     "
    f"{comparison_bytes_value!r}"
)

print(
    f"bytearray: "
    f"{comparison_bytearray_value!r}"
)

print(
    f"bytes type:     "
    f"{type(comparison_bytes_value)}"
)

print(
    f"bytearray type: "
    f"{type(comparison_bytearray_value)}"
)


# Main distinction:
#
#     bytes
#         -> immutable
#
#     bytearray
#         -> mutable


# =============================================================================
# Example 31: Bytearray Is Not Hashable
# =============================================================================

unhashable_bytearray_sample: bytearray = (
    bytearray(b"Python")
)

# The following operation is invalid:
#
#     hash(unhashable_bytearray_sample)
#
# bytearray is mutable and therefore unhashable.


# =============================================================================
# Example 32: Bytearray Cannot Be a Dictionary Key
# =============================================================================

bytearray_key_dictionary: dict[object, str] = {}

# The following operation is invalid:
#
#     bytearray_key_dictionary[
#         bytearray(b"Python")
#     ] = "value"
#
# bytearray objects are unhashable.


# =============================================================================
# Example 33: Bytearray Cannot Be a Set Element
# =============================================================================

bytearray_container_set: set[object] = set()

# The following operation is invalid:
#
#     bytearray_container_set.add(
#         bytearray(b"Python")
#     )
#
# A mutable bytearray cannot be a set element.


# =============================================================================
# Example 34: Equality
# =============================================================================

bytearray_equality_left: bytearray = (
    bytearray(b"Python")
)

bytearray_equality_right: bytearray = (
    bytearray(b"Python")
)

bytearray_equality_result: bool = (
    bytearray_equality_left
    == bytearray_equality_right
)

print(
    f"Equal bytearrays: "
    f"{bytearray_equality_result}"
)


# `==` compares the byte contents.


# =============================================================================
# Example 35: Identity
# =============================================================================

bytearray_identity_source: bytearray = (
    bytearray(b"Python")
)

bytearray_identity_copy: bytearray = (
    bytearray(bytearray_identity_source)
)

bytearray_identity_result: bool = (
    bytearray_identity_source
    is bytearray_identity_copy
)

print(
    f"Same bytearray object: "
    f"{bytearray_identity_result}"
)


# `==` checks content equality.
#
# `is` checks whether both variables refer to the same object.


# =============================================================================
# Example 36: Object Identity After In-Place Mutation
# =============================================================================

bytearray_identity_mutation_sample: bytearray = (
    bytearray(b"Python")
)

bytearray_identity_before_mutation: int = id(
    bytearray_identity_mutation_sample
)

bytearray_identity_mutation_sample[0] = 74

bytearray_identity_after_mutation: int = id(
    bytearray_identity_mutation_sample
)

print(
    f"Before mutation: "
    f"{bytearray_identity_before_mutation}"
)

print(
    f"After mutation:  "
    f"{bytearray_identity_after_mutation}"
)

print(
    f"Same object: "
    f"{bytearray_identity_before_mutation == bytearray_identity_after_mutation}"
)


# The contents changed, but the object itself remained the same object.
#
# This is an important characteristic of mutability.


# =============================================================================
# Example 37: Creating a New Bytearray From Existing Data
# =============================================================================

bytearray_original_object: bytearray = (
    bytearray(b"Python")
)

bytearray_new_object: bytearray = (
    bytearray(bytearray_original_object)
)

print(
    f"Original: "
    f"{bytearray_original_object!r}"
)

print(
    f"New:      "
    f"{bytearray_new_object!r}"
)

print(
    f"Equal: "
    f"{bytearray_original_object == bytearray_new_object}"
)

print(
    f"Same object: "
    f"{bytearray_original_object is bytearray_new_object}"
)


# The contents are equal, but these are two distinct bytearray objects.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `bytearray` represents a mutable sequence of bytes.

✓ Every byte value must be between:
      0 and 255

✓ `bytearray()` creates an empty bytearray.

✓ A type annotation alone does not initialize a bytearray.

✓ `bytearray(b"Python")` creates a mutable binary sequence from bytes.

✓ A string can be converted to bytearray by specifying an encoding.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of bytes.

✓ Bytearrays support:
      - positive indexing
      - negative indexing
      - slicing
      - slice assignment
      - iteration
      - membership testing

✓ Indexing a bytearray returns an integer.

✓ Slicing a bytearray returns another bytearray.

✓ Bytearrays can be modified in place.

✓ Individual bytes can be changed using index assignment.

✓ Slices can be replaced.

✓ Slice replacement can change the total length.

✓ Common mutating methods include:
      append()
      extend()
      insert()
      remove()
      pop()
      clear()
      reverse()

✓ `replace()` returns a new bytearray.

✓ `.hex()` converts byte values to hexadecimal text.

✓ `fromhex()` creates a bytearray from hexadecimal text.

✓ `decode()` converts byte data into a string.

✓ Bytearray is mutable.

✓ Bytearray is NOT hashable.

✓ Bytearray cannot be:
      - a dictionary key
      - a set element

✓ `bytes` and `bytearray` both represent binary data.

✓ The major distinction is:

      bytes
          -> immutable
          -> hashable

      bytearray
          -> mutable
          -> unhashable

✓ `==` compares contents.

✓ `is` compares object identity.

✓ Mutating a bytearray changes its contents without creating a new object.

✓ Creating a new bytearray from an existing bytearray produces a distinct
  object containing equal data.

✓ `!r` is useful when displaying the actual Python representation of
  bytes and bytearray objects.

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================