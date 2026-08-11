"""
==============================================================================
Python Indexing & Slicing
==============================================================================

Module
------
Negative Indexing

Overview
--------
Negative indexing allows elements to be accessed from the end of a sequence.

While positive indexing starts from 0 at the beginning of a sequence, negative
indexing starts from -1 at the end.

Negative Index Structure
------------------------
For the string:

    some_string = "some_string"

The indexes can be represented as:

    Positive Index:
    Index:    0   1   2   3   4   5   6   7   8   9   10
    Element:  s   o   m   e   _   s   t   r   i   n   g

    Negative Index:
    Index:   -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
    Element:   s   o   m   e   _   s   t   r   i   n   g

The last element always has index -1.

Syntax
------
sequence[-index]

Example:

    some_string[-1]

returns the last element of the sequence.

Important
---------
Negative indexing starts at -1, not 0.

The following relationship exists:

    sequence[-1] -> last element
    sequence[-2] -> second-last element
    sequence[-3] -> third-last element

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
"""


# =============================================================================
# Example 1: Negative Indexing with Strings
# =============================================================================

some_string: str = "some_string"

last_character: str = some_string[-1]

second_last_character: str = some_string[-2]

third_last_character: str = some_string[-3]

print(
    f"Index: -1 -> Element: {last_character}"
)

print(
    f"Index: -2 -> Element: {second_last_character}"
)

print(
    f"Index: -3 -> Element: {third_last_character}"
)


# =============================================================================
# Example 2: Accessing the Last Element
# =============================================================================

programming_language: str = "Python"

last_letter: str = programming_language[-1]

print(
    f"Last letter: {last_letter}"
)


# =============================================================================
# Example 3: Negative Indexing with Lists
# =============================================================================

numbers: list[int] = [
    10,
    20,
    30,
    40,
    50
]

last_number: int = numbers[-1]

second_last_number: int = numbers[-2]

print(
    f"Index: -1 -> Element: {last_number}"
)

print(
    f"Index: -2 -> Element: {second_last_number}"
)


# =============================================================================
# Example 4: Negative Indexing with Tuples
# =============================================================================

languages: tuple[str, str, str] = (
    "Python",
    "Java",
    "C++"
)

last_language: str = languages[-1]

print(
    f"Index: -1 -> Element: {last_language}"
)


# =============================================================================
# Example 5: Negative Indexing with Bytes
# =============================================================================

some_bytes: bytes = b"Python"

last_byte: int = some_bytes[-1]

print(
    f"Index: -1 -> Byte value: {last_byte}"
)


# =============================================================================
# Example 6: Negative Indexing with Bytearray
# =============================================================================

some_bytearray: bytearray = bytearray(
    b"Python"
)

last_bytearray_value: int = some_bytearray[-1]

print(
    f"Index: -1 -> Byte value: {last_bytearray_value}"
)


# =============================================================================
# Example 7: Negative Indexing with a Range
# =============================================================================

number_range: range = range(10, 15)

last_range_element: int = number_range[-1]

second_last_range_element: int = number_range[-2]

print(
    f"Index: -1 -> Element: {last_range_element}"
)

print(
    f"Index: -2 -> Element: {second_last_range_element}"
)


# =============================================================================
# Example 8: Positive vs Negative Indexing
# =============================================================================

values: list[str] = [
    "first",
    "second",
    "third",
    "fourth"
]

first_value: str = values[0]

last_value: str = values[-1]

print(
    f"Positive index 0:  {first_value}"
)

print(
    f"Negative index -1: {last_value}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Negative indexing accesses elements from the end of a sequence.

✓ The last element has index -1.

✓ The second-last element has index -2.

✓ The third-last element has index -3.

✓ Negative indexing is available on sequence types that support indexing.

✓ Negative indexing does not start from zero.

✓ Positive and negative indexes can refer to the same element.

Example:

    sequence[0]
    sequence[-len(sequence)]

can refer to the same first element when the sequence is non-empty.
"""


# =============================================================================
# End of File
# =============================================================================