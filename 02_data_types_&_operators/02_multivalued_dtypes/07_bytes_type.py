"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Bytes (`bytes`)

Overview
--------
`bytes` represents an immutable sequence of integers.

Each element of a bytes object is an integer in the range:

    0 <= value <= 255

Bytes are commonly used for:

    - Binary data
    - File contents
    - Network communication
    - Encoded text
    - Cryptographic data
    - Protocol data

Examples:

    b"Python"
    bytes([80, 121, 116, 104, 111, 110])

Important:

    b"Python"

does NOT store Python characters internally as string objects.

When indexed, a bytes object returns integers representing byte values.

For example:

    b"A"[0] -> 65

This module covers:

    - Bytes literals
    - Default and non-default values
    - Empty bytes
    - Byte values
    - ASCII representation
    - Type identification
    - Runtime type checking
    - Length
    - Positive indexing
    - Negative indexing
    - Slicing
    - Iteration
    - Membership testing
    - bytes()
    - Conversion from strings
    - Encoding
    - Decoding
    - Conversion from integers
    - Conversion from iterables
    - Immutability
    - Bytearray comparison
    - Common bytes methods
    - Hexadecimal representation
    - Hashability

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Bytes Literal
# =============================================================================

empty_bytes_value: bytes = b""

text_bytes_value: bytes = b"Python"

binary_bytes_value: bytes = b"\x50\x79\x74\x68\x6f\x6e"

print(
    f"Empty bytes:    {empty_bytes_value!r}"
)

print(
    f"Text bytes:     {text_bytes_value!r}"
)

print(
    f"Binary bytes:   {binary_bytes_value!r}"
)


# A bytes literal begins with `b`.
#
# Example:
#
#     b"Python"


# =============================================================================
# Example 2: Default and Non-Default Bytes Values
# =============================================================================

default_like_bytes_value: bytes = b""

non_default_bytes_primary: bytes = b"Python"

non_default_bytes_secondary: bytes = (
    b"\x01\x02\x03"
)

print(
    f"Default-like bytes: "
    f"{default_like_bytes_value!r}"
)

print(
    f"First bytes value:  "
    f"{non_default_bytes_primary!r}"
)

print(
    f"Second bytes value: "
    f"{non_default_bytes_secondary!r}"
)


# Python does NOT automatically assign b"" to an annotated bytes variable.
#
# This:
#
#     values: bytes
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: bytes = b""


# =============================================================================
# Example 3: Empty Bytes
# =============================================================================

empty_bytes_sample: bytes = b""

print(
    f"Value: {empty_bytes_sample!r}"
)

print(
    f"Length: {len(empty_bytes_sample)}"
)

print(
    f"Type: {type(empty_bytes_sample)}"
)


# Expected:
#
#     Value: b''
#     Length: 0
#     Type: <class 'bytes'>


# =============================================================================
# Example 4: Type Identification
# =============================================================================

bytes_type_sample: bytes = b"Python"

print(
    f"Value: {bytes_type_sample!r}"
)

print(
    f"Type:  {type(bytes_type_sample)}"
)


# Expected:
#
#     <class 'bytes'>


# =============================================================================
# Example 5: Runtime Bytes Type Checking
# =============================================================================

bytes_runtime_candidate: object = b"Python"

string_runtime_candidate_for_bytes: object = "Python"

bytes_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    bytes_runtime_candidate,
    bytes,
)

string_bytes_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    string_runtime_candidate_for_bytes,
    bytes,
)

print(
    f"b'Python' is bytes: "
    f"{bytes_runtime_check}"
)

print(
    f"'Python' is bytes:  "
    f"{string_bytes_check}"
)


# The candidates are intentionally typed as `object`.
#
# The Pyright suppression is used because this example intentionally
# demonstrates runtime isinstance() behaviour.


# =============================================================================
# Example 6: Byte Length
# =============================================================================

bytes_length_sample: bytes = b"Python"

bytes_length_result: int = len(
    bytes_length_sample
)

print(
    f"Bytes length: {bytes_length_result}"
)


# `len()` returns the number of bytes.


# =============================================================================
# Example 7: Positive Indexing
# =============================================================================

positive_bytes_index_sample: bytes = (
    b"Python"
)

positive_bytes_first_value: int = (
    positive_bytes_index_sample[0]
)

positive_bytes_third_value: int = (
    positive_bytes_index_sample[2]
)

print(
    f"First byte:  {positive_bytes_first_value}"
)

print(
    f"Third byte:  {positive_bytes_third_value}"
)


# IMPORTANT:
#
# Indexing bytes returns an integer.
#
# For example:
#
#     b"P"[0] -> 80
#
# It does NOT return:
#
#     b"P"
#
# and it does NOT return:
#
#     "P"


# =============================================================================
# Example 8: Negative Indexing
# =============================================================================

negative_bytes_index_sample: bytes = (
    b"Python"
)

negative_bytes_last_value: int = (
    negative_bytes_index_sample[-1]
)

negative_bytes_second_last_value: int = (
    negative_bytes_index_sample[-2]
)

print(
    f"Last byte:        {negative_bytes_last_value}"
)

print(
    f"Second-last byte: {negative_bytes_second_last_value}"
)


# =============================================================================
# Example 9: Bytes Slicing
# =============================================================================

bytes_slice_source: bytes = b"Python"

bytes_first_slice: bytes = (
    bytes_slice_source[0:3]
)

bytes_second_slice: bytes = (
    bytes_slice_source[2:6]
)

print(
    f"First slice:  {bytes_first_slice!r}"
)

print(
    f"Second slice: {bytes_second_slice!r}"
)


# Important:
#
# Indexing:
#
#     bytes[index] -> int
#
# Slicing:
#
#     bytes[start:stop] -> bytes


# =============================================================================
# Example 10: Bytes Iteration
# =============================================================================

bytes_iteration_sample: bytes = b"ABC"

for bytes_iteration_value in (
    bytes_iteration_sample
):
    print(
        bytes_iteration_value
    )


# Iterating over bytes produces integers.


# =============================================================================
# Example 11: Membership Testing
# =============================================================================

bytes_membership_sample: bytes = b"Python"

bytes_integer_membership: bool = (
    80 in bytes_membership_sample
)

bytes_subsequence_membership: bool = (
    b"Python" in bytes_membership_sample
)

print(
    f"80 is present: "
    f"{bytes_integer_membership}"
)

print(
    f"b'Python' is present: "
    f"{bytes_subsequence_membership}"
)


# Bytes membership can be checked using:
#
#     an integer
#
# or:
#
#     another bytes-like sequence


# =============================================================================
# Example 12: bytes() With No Arguments
# =============================================================================

bytes_constructor_empty: bytes = bytes()

print(
    f"bytes(): {bytes_constructor_empty!r}"
)


# `bytes()` creates an empty bytes object when no argument is supplied.


# =============================================================================
# Example 13: bytes() From an Integer
# =============================================================================

bytes_from_integer: bytes = bytes(
    5
)

print(
    f"Bytes from integer: "
    f"{bytes_from_integer!r}"
)


# An integer argument creates that many zero bytes.
#
# Therefore:
#
#     bytes(5)
#
# produces:
#
#     b"\x00\x00\x00\x00\x00"


# =============================================================================
# Example 14: bytes() From an Iterable of Integers
# =============================================================================

bytes_from_integer_values: bytes = bytes([
    65,
    66,
    67,
])

print(
    f"Bytes: {bytes_from_integer_values!r}"
)


# Each integer must be within:
#
#     0 <= value <= 255
#
# 65 -> A
# 66 -> B
# 67 -> C


# =============================================================================
# Example 15: bytes() From a String
# =============================================================================

string_for_bytes_conversion: str = (
    "Python"
)

encoded_string_bytes: bytes = (
    bytes(
        string_for_bytes_conversion,
        "utf-8",
    )
)

print(
    f"String: {string_for_bytes_conversion}"
)

print(
    f"Bytes:  {encoded_string_bytes!r}"
)


# A string cannot be directly passed to bytes() without specifying an encoding.
#
# Encoding defines how characters are converted into bytes.


# =============================================================================
# Example 16: encode()
# =============================================================================

text_for_encoding: str = (
    "Python"
)

encoded_python_text: bytes = (
    text_for_encoding.encode(
        "utf-8"
    )
)

print(
    f"Original text: {text_for_encoding}"
)

print(
    f"Encoded bytes: {encoded_python_text!r}"
)


# `str.encode()` converts text into bytes.


# =============================================================================
# Example 17: UTF-8 With Non-ASCII Text
# =============================================================================

unicode_text_for_encoding: str = (
    "café"
)

unicode_encoded_bytes: bytes = (
    unicode_text_for_encoding.encode(
        "utf-8"
    )
)

print(
    f"Text:  {unicode_text_for_encoding}"
)

print(
    f"Bytes: {unicode_encoded_bytes!r}"
)


# One character does not necessarily correspond to one byte.
#
# In UTF-8:
#
#     ASCII characters generally use 1 byte.
#
#     Many non-ASCII characters use multiple bytes.


# =============================================================================
# Example 18: decode()
# =============================================================================

encoded_text_sample: bytes = (
    b"Python"
)

decoded_text_value: str = (
    encoded_text_sample.decode(
        "utf-8"
    )
)

print(
    f"Bytes:  {encoded_text_sample!r}"
)

print(
    f"Text:   {decoded_text_value}"
)


# `bytes.decode()` converts bytes into a string using the specified encoding.


# =============================================================================
# Example 19: Encoding and Decoding Round Trip
# =============================================================================

round_trip_original_text: str = (
    "Data Engineering"
)

round_trip_encoded_value: bytes = (
    round_trip_original_text.encode(
        "utf-8"
    )
)

round_trip_decoded_value: str = (
    round_trip_encoded_value.decode(
        "utf-8"
    )
)

print(
    f"Original: {round_trip_original_text}"
)

print(
    f"Encoded:  {round_trip_encoded_value!r}"
)

print(
    f"Decoded:  {round_trip_decoded_value}"
)


# Conceptually:
#
#     str
#      |
#      | encode()
#      v
#     bytes
#      |
#      | decode()
#      v
#     str


# =============================================================================
# Example 20: ASCII Numeric Values
# =============================================================================

ascii_bytes_sample: bytes = b"ABC"

ascii_first_value: int = (
    ascii_bytes_sample[0]
)

ascii_second_value: int = (
    ascii_bytes_sample[1]
)

ascii_third_value: int = (
    ascii_bytes_sample[2]
)

print(
    f"A -> {ascii_first_value}"
)

print(
    f"B -> {ascii_second_value}"
)

print(
    f"C -> {ascii_third_value}"
)


# ASCII defines numeric codes for characters.
#
# A -> 65
# B -> 66
# C -> 67


# =============================================================================
# Example 21: chr() and bytes
# =============================================================================

character_from_integer: str = chr(65)

print(
    f"chr(65): {character_from_integer}"
)


# `chr()` converts an integer Unicode code point into a string character.
#
# This is related to, but conceptually different from, bytes encoding.


# =============================================================================
# Example 22: bytes.hex()
# =============================================================================

hex_bytes_sample: bytes = b"ABC"

hexadecimal_representation: str = (
    hex_bytes_sample.hex()
)

print(
    f"Bytes: {hex_bytes_sample!r}"
)

print(
    f"Hex:   {hexadecimal_representation}"
)


# `.hex()` returns a string containing the hexadecimal representation
# of each byte.


# =============================================================================
# Example 23: bytes.fromhex()
# =============================================================================

hexadecimal_source_text: str = (
    "41 42 43"
)

bytes_from_hexadecimal: bytes = (
    bytes.fromhex(
        hexadecimal_source_text
    )
)

print(
    f"Hex text: {hexadecimal_source_text}"
)

print(
    f"Bytes:    {bytes_from_hexadecimal!r}"
)


# `bytes.fromhex()` performs the reverse operation of `.hex()` for
# hexadecimal byte representations.


# =============================================================================
# Example 24: count()
# =============================================================================

bytes_count_sample: bytes = (
    b"banana"
)

bytes_count_result: int = (
    bytes_count_sample.count(
        b"a"
    )
)

print(
    f"Number of 'a' bytes: "
    f"{bytes_count_result}"
)


# `count()` counts occurrences of a byte value or bytes subsequence.


# =============================================================================
# Example 25: find()
# =============================================================================

bytes_find_sample: bytes = (
    b"Python SQL"
)

bytes_find_result: int = (
    bytes_find_sample.find(
        b"SQL"
    )
)

print(
    f"SQL starts at index: "
    f"{bytes_find_result}"
)


# `find()` returns the first matching position.
#
# If no match exists, it returns -1.


# =============================================================================
# Example 26: startswith() and endswith()
# =============================================================================

bytes_prefix_suffix_sample: bytes = (
    b"Python SQL"
)

bytes_starts_result: bool = (
    bytes_prefix_suffix_sample.startswith(
        b"Python"
    )
)

bytes_ends_result: bool = (
    bytes_prefix_suffix_sample.endswith(
        b"SQL"
    )
)

print(
    f"Starts with Python: "
    f"{bytes_starts_result}"
)

print(
    f"Ends with SQL: "
    f"{bytes_ends_result}"
)


# =============================================================================
# Example 27: replace()
# =============================================================================

bytes_replace_sample: bytes = (
    b"Python SQL"
)

bytes_replace_result: bytes = (
    bytes_replace_sample.replace(
        b"SQL",
        b"Airflow",
    )
)

print(
    f"Original: {bytes_replace_sample!r}"
)

print(
    f"Result:   {bytes_replace_result!r}"
)


# `replace()` returns a new bytes object.
#
# It does NOT modify the original bytes object.


# =============================================================================
# Example 28: Bytes Immutability
# =============================================================================

immutable_bytes_sample: bytes = (
    b"Python"
)

print(
    f"Original bytes: "
    f"{immutable_bytes_sample!r}"
)


# The following operation is invalid:
#
#     immutable_bytes_sample[0] = 80
#
# Bytes objects are immutable.
#
# Individual byte values cannot be reassigned.


# =============================================================================
# Example 29: Bytes vs Bytearray
# =============================================================================

immutable_binary_value: bytes = (
    b"Python"
)

mutable_binary_value: bytearray = (
    bytearray(b"Python")
)

print(
    f"bytes:    {immutable_binary_value!r}"
)

print(
    f"bytearray: {mutable_binary_value}"
)


# Main distinction:
#
#     bytes     -> immutable
#     bytearray -> mutable
#
# `bytearray` will be covered in the next file.


# =============================================================================
# Example 30: bytes Hashability
# =============================================================================

hashable_bytes_value: bytes = (
    b"Python"
)

bytes_hash_result: int = hash(
    hashable_bytes_value
)

print(
    f"Bytes hash: {bytes_hash_result}"
)


# Bytes are hashable because they are immutable.
#
# Therefore, bytes can be used as:
#
#     - dictionary keys
#     - set elements


# =============================================================================
# Example 31: Bytes as Dictionary Key
# =============================================================================

bytes_dictionary_key: bytes = (
    b"user_id"
)

bytes_key_dictionary: dict[bytes, str] = {
    bytes_dictionary_key: "12345"
}

print(
    bytes_key_dictionary
)


# =============================================================================
# Example 32: Bytes as Set Element
# =============================================================================

bytes_set_element: bytes = (
    b"Python"
)

bytes_container_set: set[bytes] = {
    bytes_set_element,
}

print(
    f"Set containing bytes: "
    f"{bytes_container_set}"
)


# =============================================================================
# Example 33: bytes Equality
# =============================================================================

bytes_equality_left: bytes = (
    b"Python"
)

bytes_equality_right: bytes = (
    b"Python"
)

bytes_equality_result: bool = (
    bytes_equality_left
    == bytes_equality_right
)

print(
    f"Equal bytes: {bytes_equality_result}"
)


# `==` compares the byte contents.


# =============================================================================
# Example 34: bytes Identity
# =============================================================================

bytes_identity_source: bytes = (
    b"Python"
)

bytes_identity_copy: bytes = bytes(
    bytearray(bytes_identity_source)
)

bytes_identity_result: bool = (
    bytes_identity_source
    is bytes_identity_copy
)

print(
    f"Same bytes object: "
    f"{bytes_identity_result}"
)


# `is` compares object identity.
#
# `==` compares contents.


# =============================================================================
# Example 35: bytes to List
# =============================================================================

bytes_for_list_conversion: bytes = (
    b"ABC"
)

integer_list_from_bytes: list[int] = list(
    bytes_for_list_conversion
)

print(
    f"Bytes: {bytes_for_list_conversion!r}"
)

print(
    f"List:  {integer_list_from_bytes}"
)


# Converting bytes to a list produces integer byte values.


# =============================================================================
# Example 36: Bytes to Bytearray
# =============================================================================

bytes_for_bytearray_conversion: bytes = (
    b"Python"
)

converted_bytearray_value: bytearray = (
    bytearray(
        bytes_for_bytearray_conversion
    )
)

print(
    f"Bytes:     {bytes_for_bytearray_conversion!r}"
)

print(
    f"Bytearray: {converted_bytearray_value}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `bytes` represents an immutable sequence of integers.

✓ Every byte value must be between:
      0 and 255

✓ `b"Python"` creates a bytes literal.

✓ `b""` represents empty bytes.

✓ `bytes()` creates an empty bytes object when called without arguments.

✓ `bytes(n)` creates n zero-valued bytes.

✓ `bytes(iterable)` creates bytes from integer values in the range 0–255.

✓ Strings can be converted to bytes by specifying an encoding.

✓ `str.encode()` converts strings to bytes.

✓ `bytes.decode()` converts bytes back to strings.

✓ UTF-8 can represent non-ASCII characters using multiple bytes.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of bytes.

✓ Bytes support:
      - positive indexing
      - negative indexing
      - slicing
      - iteration
      - membership testing

✓ Indexing bytes returns an integer.

✓ Slicing bytes returns another bytes object.

✓ Iterating over bytes produces integers.

✓ Bytes are immutable.

✓ Bytes do not support item assignment.

✓ Methods such as `replace()` return a new bytes object rather than
  modifying the original.

✓ `.hex()` converts bytes into hexadecimal text.

✓ `bytes.fromhex()` converts hexadecimal text into bytes.

✓ `count()` counts byte values or byte sequences.

✓ `find()` searches for a byte sequence.

✓ `startswith()` checks the beginning of bytes.

✓ `endswith()` checks the end of bytes.

✓ `bytes` and `bytearray` both represent binary data, but:

      bytes     -> immutable
      bytearray -> mutable

✓ Bytes are hashable.

✓ Bytes can be dictionary keys.

✓ Bytes can be set elements.

✓ `==` compares byte contents.

✓ `is` compares object identity.

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================