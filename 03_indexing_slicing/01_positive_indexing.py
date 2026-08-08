"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Positive Indexing

Overview
--------
Indexing is one of the most fundamental concepts in Python.

It allows individual elements of a sequence to be accessed using their
position, called an index.

Python uses zero-based indexing, which means the first element is located
at index 0.

Positive indexing starts from the beginning of a sequence and moves from
left to right.

Python supports positive indexing on sequence types such as:

    • Strings
    • Lists
    • Tuples
    • Bytes
    • Bytearrays
    • Range objects

Sets do not support indexing because they are unordered collections.

Dictionaries are mapping types and are accessed using keys rather than
sequence indexes.

Index Structure
---------------
For the string:

    some_string = "some_string"

The positive indexes are:

    Character:  s  o  m  e  _  s  t  r  i  n  g
    Index:      0  1  2  3  4  5  6  7  8  9  10

Syntax
------
sequence[index]

Example:

    some_string[2]

returns the element located at index 2.

Important
---------
The index identifies the position.

The element is the value stored at that position.

For example:

    some_string[2]

    Index  -> 2
    Element -> "m"

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: String Indexing
# =============================================================================

some_string: str = "some_string"

third_character: str = some_string[2]

print(
    f"Index: 2 -> Element: {third_character}"
)


# =============================================================================
# Example 2: Accessing Different String Positions
# =============================================================================

first_character: str = some_string[0]

fifth_character: str = some_string[4]

last_character: str = some_string[10]

print(
    f"First character: {first_character}"
)

print(
    f"Fifth character: {fifth_character}"
)

print(
    f"Last character: {last_character}"
)


# =============================================================================
# Example 3: List Indexing
# =============================================================================

some_list: list[str | int | list[int]] = [
    "some_string",
    10,
    20,
    "my_name",
    [1, 2]
]

first_list_element: str = some_list[0]  # type: ignore[assignment]

second_list_element: int = some_list[1]  # type: ignore[assignment]

last_list_element: list[int] = some_list[4]  # type: ignore[assignment]

print(
    f"Index: 0 -> Element: {first_list_element}"
)

print(
    f"Index: 1 -> Element: {second_list_element}"
)

print(
    f"Index: 4 -> Element: {last_list_element}"
)


# =============================================================================
# Example 4: Indexing a Nested List
# =============================================================================

nested_numbers: list[int] = [1, 2]

print(
    f"Outer index: 4 -> Element: {some_list[4]}"
)

print(
    f"Nested index: 0 -> Element: {nested_numbers[0]}"
)

print(
    f"Nested index: 1 -> Element: {nested_numbers[1]}"
)


# =============================================================================
# Example 5: Tuple Indexing
# =============================================================================

some_tuple: tuple[str, int, float] = (
    "Python",
    100,
    99.5
)

tuple_name: str = some_tuple[0]

tuple_count: int = some_tuple[1]

tuple_percentage: float = some_tuple[2]

print(
    f"Index: 0 -> Element: {tuple_name}"
)

print(
    f"Index: 1 -> Element: {tuple_count}"
)

print(
    f"Index: 2 -> Element: {tuple_percentage}"
)


# =============================================================================
# Example 6: Bytes Indexing
# =============================================================================

some_bytes: bytes = b"Python"

byte_value: int = some_bytes[0]

print(
    f"Index: 0 -> Byte value: {byte_value}"
)


# =============================================================================
# Example 7: Bytearray Indexing
# =============================================================================

some_bytearray: bytearray = bytearray(
    b"Python"
)

bytearray_value: int = some_bytearray[0]

print(
    f"Index: 0 -> Byte value: {bytearray_value}"
)


# =============================================================================
# Example 8: Range Indexing
# =============================================================================

number_range: range = range(10, 15)

range_element: int = number_range[2]

print(
    f"Index: 2 -> Element: {range_element}"
)


# =============================================================================
# Example 9: Indexing Starts from Zero
# =============================================================================

programming_languages: list[str] = [
    "Python",
    "Java",
    "C++"
]

print(
    f"Index: 0 -> Element: {programming_languages[0]}"
)

print(
    f"Index: 1 -> Element: {programming_languages[1]}"
)

print(
    f"Index: 2 -> Element: {programming_languages[2]}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Indexing accesses one element from a sequence.

✓ Python uses zero-based indexing.

✓ The first element is at index 0.

✓ Positive indexing moves from left to right.

✓ The index represents the position.

✓ The element is the value stored at that position.

✓ Nested sequences can have their own independent indexes.

✓ Strings, lists, tuples, bytes, bytearrays, and range objects support
  indexing.

✓ Sets do not support indexing.

✓ Dictionaries are accessed using keys rather than sequence indexes.
"""


# =============================================================================
# End of File
# =============================================================================