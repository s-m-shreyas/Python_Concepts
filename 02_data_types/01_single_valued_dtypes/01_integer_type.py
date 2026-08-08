
"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Single-Valued Data Types

Data Type
---------
Integer (`int`)

Overview
--------
An integer represents a whole number without a fractional component.

Examples:

    0
    10
    -25

Python integers can represent arbitrarily large whole numbers, limited
primarily by available memory.

This module covers:

    - Integer literals
    - Default and non-default values
    - Positive, negative, and zero integers
    - Type identification
    - Integer arithmetic
    - Division and floor division
    - Modulo
    - Exponentiation
    - Unary operators
    - Comparison operations
    - Absolute, minimum, maximum, and sum operations
    - Binary, octal, and hexadecimal representations
    - Integer conversion
    - Integer methods
    - Bitwise operations
    - Bit shifting
    - Boolean interpretation of integers

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
# Example 1: Integer Literals
# =============================================================================

positive_integer: int = 100
negative_integer: int = -100
zero_integer: int = 0

print(
    f"Positive integer: {positive_integer}"
)

print(
    f"Negative integer: {negative_integer}"
)

print(
    f"Zero integer:     {zero_integer}"
)


# An integer literal is written as a whole number.
#
# Examples:
#
#     100
#     -100
#     0


# =============================================================================
# Example 2: Default and Non-Default Integer Values
# =============================================================================

default_like_integer: int = 0

non_default_positive_integer: int = 100
non_default_negative_integer: int = -100

print(
    f"Default-like value: {default_like_integer}"
)

print(
    f"Positive value:     {non_default_positive_integer}"
)

print(
    f"Negative value:     {non_default_negative_integer}"
)


# Important:
#
# Python does NOT automatically assign 0 to an integer variable.
#
# This:
#
#     number: int
#
# is only a type annotation.
#
# It does NOT mean:
#
#     number = 0
#
# An explicit value must be assigned:
#
#     number: int = 0
#
# Therefore, 0 is commonly used as a default-like integer value in
# programming, but it is not Python's automatic default for an annotated
# variable.


# =============================================================================
# Example 3: Checking the Integer Type
# =============================================================================

integer_value: int = 250

print(
    f"Value: {integer_value}"
)

print(
    f"Type:  {type(integer_value)}"
)


# `type()` returns the type/class of an object.
#
# Expected type:
#
#     <class 'int'>


# =============================================================================
# Example 4: Checking Whether a Value Is an Integer
# =============================================================================

candidate_value: int = 500

is_integer: bool = isinstance(
    candidate_value,
    int,
)  # pyright: ignore[reportUnnecessaryIsInstance]

print(f"Is integer: {is_integer}")

# `isinstance()` performs a runtime type check.
#
# The variable is intentionally typed as `object` because every Python value
# is an object, while its concrete runtime type is not known from the
# annotation alone.
#
# Therefore, `isinstance()` has meaningful work to perform:
#
#     object
#       ↓
# isinstance(..., int)
#       ↓
#     True
#
# This is different from:
#
#     candidate_integer: int = 500
#     isinstance(candidate_integer, int)
#
# where a static type checker already knows that `candidate_integer` is an
# integer and can therefore report the check as unnecessary.
#
# `isinstance()` checks whether an object is an instance of a specified type.
#
# `cast()` is used here to prevent the static type checker from preserving
# the literal type `Literal[500]` and reporting the `isinstance()` call as
# unnecessary.
#
# `cast()` does not change the runtime value or perform a conversion.
#
# The important concept being demonstrated is the runtime use of:
#
#     isinstance(value, int)
#
# `isinstance()` checks whether an object is an instance of a specified type.
#
# It is generally preferred when checking type relationships.


# =============================================================================
# Example 5: Basic Integer Arithmetic
# =============================================================================

first_integer: int = 20
second_integer: int = 6

addition_result: int = (
    first_integer + second_integer
)

subtraction_result: int = (
    first_integer - second_integer
)

multiplication_result: int = (
    first_integer * second_integer
)

print(
    f"Addition:       {addition_result}"
)

print(
    f"Subtraction:    {subtraction_result}"
)

print(
    f"Multiplication: {multiplication_result}"
)


# Arithmetic operators:
#
#     +   addition
#     -   subtraction
#     *   multiplication


# =============================================================================
# Example 6: True Division
# =============================================================================

division_left: int = 20
division_right: int = 5

division_result: float = (
    division_left / division_right
)

print(
    f"Division result: {division_result}"
)

print(
    f"Result type:     {type(division_result)}"
)


# `/` performs true division.
#
# Even when both operands are integers, the result is a float.
#
#     20 / 5
#
# produces:
#
#     4.0


# =============================================================================
# Example 7: Floor Division
# =============================================================================

floor_dividend: int = 20
floor_divisor: int = 6

floor_result: int = (
    floor_dividend // floor_divisor
)

print(
    f"Floor division: {floor_result}"
)


# `//` performs floor division.
#
#     20 // 6
#
# produces:
#
#     3
#
# Floor division returns the mathematical floor of the division result.


# =============================================================================
# Example 8: Floor Division With Negative Numbers
# =============================================================================

negative_floor_dividend: int = -20
negative_floor_divisor: int = 6

negative_floor_result: int = (
    negative_floor_dividend
    // negative_floor_divisor
)

print(
    f"Result: {negative_floor_result}"
)


# Important:
#
# Python's `//` performs FLOOR division.
#
#     -20 / 6 ≈ -3.333...
#
# Therefore:
#
#     -20 // 6 == -4
#
# because -4 is the mathematical floor of -3.333...


# =============================================================================
# Example 9: Modulo
# =============================================================================

modulo_dividend: int = 20
modulo_divisor: int = 6

remainder_result: int = (
    modulo_dividend
    % modulo_divisor
)

print(
    f"Remainder: {remainder_result}"
)


# `%` returns the remainder associated with floor division.
#
#     20 % 6
#
# produces:
#
#     2


# =============================================================================
# Example 10: Quotient and Remainder Together
# =============================================================================

division_dividend: int = 29
division_divisor: int = 5

division_quotient: int = (
    division_dividend
    // division_divisor
)

division_remainder: int = (
    division_dividend
    % division_divisor
)

print(
    f"Quotient:  {division_quotient}"
)

print(
    f"Remainder: {division_remainder}"
)


# The relationship is:
#
#     dividend = (divisor * quotient) + remainder
#
# Therefore:
#
#     29 = (5 * 5) + 4


# =============================================================================
# Example 11: Exponentiation
# =============================================================================

power_base: int = 2
power_exponent: int = 5

power_result: int = (
    power_base ** power_exponent
)

print(
    f"Power result: {power_result}"
)


# `**` performs exponentiation.
#
#     2 ** 5
#
# means:
#
#     2 * 2 * 2 * 2 * 2
#
# resulting in:
#
#     32


# =============================================================================
# Example 12: Unary Operators
# =============================================================================

unary_integer: int = 25

positive_unary_result: int = (
    +unary_integer
)

negative_unary_result: int = (
    -unary_integer
)

print(
    f"Positive: {positive_unary_result}"
)

print(
    f"Negative: {negative_unary_result}"
)


# Unary operators work with one operand:
#
#     +value
#     -value


# =============================================================================
# Example 13: Comparison Operations
# =============================================================================

# `cast()` is used here deliberately.
#
# Without the cast, a static type checker may preserve the literal types:
#
#     Literal[20]
#     Literal[10]
#
# and therefore determine that:
#
#     20 == 10
#
# can never be True.
#
# The cast tells the static type checker to treat these values as ordinary
# integers for the purpose of this teaching example.
#
# `cast()` does not perform a runtime conversion.

comparison_left_value: int = cast(
    int,
    20,
)

comparison_right_value: int = cast(
    int,
    10,
)

print(
    f"Equal:         "
    f"{comparison_left_value == comparison_right_value}"
)

print(
    f"Not equal:     "
    f"{comparison_left_value != comparison_right_value}"
)

print(
    f"Greater than:  "
    f"{comparison_left_value > comparison_right_value}"
)

print(
    f"Less than:     "
    f"{comparison_left_value < comparison_right_value}"
)

print(
    f"Greater/equal: "
    f"{comparison_left_value >= comparison_right_value}"
)

print(
    f"Less/equal:    "
    f"{comparison_left_value <= comparison_right_value}"
)


# Comparison expressions produce Boolean values:
#
#     True
#     False


# =============================================================================
# Example 14: Absolute Value
# =============================================================================

absolute_source: int = -250

absolute_result: int = abs(
    absolute_source
)

print(
    f"Original value: {absolute_source}"
)

print(
    f"Absolute value: {absolute_result}"
)


# `abs()` returns the absolute value of a number.


# =============================================================================
# Example 15: Minimum and Maximum
# =============================================================================

minimum_first: int = 40
minimum_second: int = 10
minimum_third: int = 75

minimum_result: int = min(
    minimum_first,
    minimum_second,
    minimum_third,
)

maximum_result: int = max(
    minimum_first,
    minimum_second,
    minimum_third,
)

print(
    f"Minimum: {minimum_result}"
)

print(
    f"Maximum: {maximum_result}"
)


# `min()` returns the smallest supplied value.
#
# `max()` returns the largest supplied value.


# =============================================================================
# Example 16: Sum of Integers
# =============================================================================

integer_collection: list[int] = [
    10,
    20,
    30,
    40,
]

integer_sum: int = sum(
    integer_collection
)

print(
    f"Values: {integer_collection}"
)

print(
    f"Sum:    {integer_sum}"
)


# `sum()` adds the values from an iterable.


# =============================================================================
# Example 17: Binary, Octal, and Hexadecimal Representations
# =============================================================================

representation_integer: int = 42

binary_representation: str = bin(
    representation_integer
)

octal_representation: str = oct(
    representation_integer
)

hexadecimal_representation: str = hex(
    representation_integer
)

print(
    f"Decimal:     {representation_integer}"
)

print(
    f"Binary:      {binary_representation}"
)

print(
    f"Octal:       {octal_representation}"
)

print(
    f"Hexadecimal: {hexadecimal_representation}"
)


# `bin()` -> binary representation
# `oct()` -> octal representation
# `hex()` -> hexadecimal representation
#
# These functions return strings.


# =============================================================================
# Example 18: Integer Literals in Different Bases
# =============================================================================

binary_integer_literal: int = 0b1010
octal_integer_literal: int = 0o12
hexadecimal_integer_literal: int = 0xA

print(
    f"Binary literal:      {binary_integer_literal}"
)

print(
    f"Octal literal:       {octal_integer_literal}"
)

print(
    f"Hexadecimal literal: {hexadecimal_integer_literal}"
)


# Prefixes:
#
#     0b -> binary
#     0o -> octal
#     0x -> hexadecimal
#
# All three literals above represent the decimal value 10.


# =============================================================================
# Example 19: Converting a String to an Integer
# =============================================================================

numeric_text_value: str = "250"

converted_integer_value: int = int(
    numeric_text_value
)

print(
    f"Original value:  {numeric_text_value}"
)

print(
    f"Original type:   {type(numeric_text_value)}"
)

print(
    f"Converted value: {converted_integer_value}"
)

print(
    f"Converted type:  {type(converted_integer_value)}"
)


# `int()` can convert suitable values into integers.
#
#     "250" -> 250
#
# General type-conversion behaviour is covered later under type behaviour.


# =============================================================================
# Example 20: Converting Strings From Different Bases
# =============================================================================

binary_text_value: str = "1010"
hexadecimal_text_value: str = "2A"

converted_binary_value: int = int(
    binary_text_value,
    2,
)

converted_hexadecimal_value: int = int(
    hexadecimal_text_value,
    16,
)

print(
    f"Binary text:       {binary_text_value}"
)

print(
    f"Binary as integer: {converted_binary_value}"
)

print(
    f"Hexadecimal text:  {hexadecimal_text_value}"
)

print(
    f"Hex as integer:    {converted_hexadecimal_value}"
)


# The second argument specifies the base used to interpret the string.
#
#     int("1010", 2)
#
# interprets "1010" as binary.
#
#     int("2A", 16)
#
# interprets "2A" as hexadecimal.


# =============================================================================
# Example 21: Integer Methods
# =============================================================================

integer_method_value: int = 42

integer_bit_length: int = (
    integer_method_value.bit_length()
)

integer_byte_value: bytes = (
    integer_method_value.to_bytes(
        length=2,
        byteorder="big",
    )
)

print(
    f"Bit length: {integer_bit_length}"
)

print(
    f"Bytes:      {integer_byte_value!r}"
)


# `bit_length()` returns the number of bits required to represent the integer,
# excluding the sign and leading zeros.
#
# `to_bytes()` converts an integer into a bytes representation.
#
# These methods become particularly useful when working with binary data.


# =============================================================================
# Example 22: Bitwise Operations
# =============================================================================

bitwise_first: int = 6
bitwise_second: int = 3

bitwise_and: int = (
    bitwise_first & bitwise_second
)

bitwise_or: int = (
    bitwise_first | bitwise_second
)

bitwise_xor: int = (
    bitwise_first ^ bitwise_second
)

bitwise_not: int = (
    ~bitwise_first
)

print(
    f"AND: {bitwise_and}"
)

print(
    f"OR:  {bitwise_or}"
)

print(
    f"XOR: {bitwise_xor}"
)

print(
    f"NOT: {bitwise_not}"
)


# Bitwise operators work on the binary representation of integers.
#
#     &   AND
#     |   OR
#     ^   XOR
#     ~   NOT


# =============================================================================
# Example 23: Bit Shifting
# =============================================================================

shift_source: int = 8

left_shift_result: int = (
    shift_source << 2
)

right_shift_result: int = (
    shift_source >> 2
)

print(
    f"Original:    {shift_source}"
)

print(
    f"Left shift:  {left_shift_result}"
)

print(
    f"Right shift: {right_shift_result}"
)


# `<<` shifts bits to the left.
#
# `>>` shifts bits to the right.
#
# For positive integers:
#
#     8 << 2
#
# is equivalent to:
#
#     8 * 2 * 2
#
# producing 32.
#
# Similarly:
#
#     8 >> 2
#
# produces 2.


# =============================================================================
# Example 24: Boolean Interpretation
# =============================================================================

zero_integer_value: int = 0
nonzero_integer_value: int = 10

zero_as_bool: bool = bool(
    zero_integer_value
)

nonzero_as_bool: bool = bool(
    nonzero_integer_value
)

print(
    f"bool(0):  {zero_as_bool}"
)

print(
    f"bool(10): {nonzero_as_bool}"
)


# Integer values have Boolean interpretations:
#
#     0        -> False
#     non-zero -> True
#
# The relationship between `bool` and `int` will be explored more formally
# in the Boolean data type module.


# =============================================================================
# Example 25: Equality and Identity Preview
# =============================================================================

first_integer_value: int = cast(
    int,
    1000,
)

second_integer_value: int = cast(
    int,
    1000,
)

print(
    f"Equal values: "
    f"{first_integer_value == second_integer_value}"
)

print(
    f"Same object:  "
    f"{first_integer_value is second_integer_value}"
)


# `==` compares values.
#
# `is` compares object identity.
#
# `cast()` is used here for the same teaching purpose as the comparison
# example above: it prevents static literal analysis from treating the two
# assignments as known literal values.
#
# The result of `is` should NOT be used as a substitute for `==`.
#
# The complete distinction between equality and identity belongs in:
#
#     17_type_behaviour/03_equality_vs_identity.py


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `int` represents whole numbers.

✓ Integers can be positive, negative, or zero.

✓ Python integers can grow beyond fixed 32-bit or 64-bit ranges, subject
  primarily to available memory.

✓ `0` is a common default-like integer value, but Python does not automatically
  assign 0 to an annotated integer variable.

✓ A type annotation such as:

      number: int

  does not initialize the variable.

✓ Explicit initialization is required:

      number: int = 0

✓ `type()` identifies the type of an object.

✓ `isinstance()` checks whether an object is an instance of a type.

✓ `/` performs true division and produces a float.

✓ `//` performs floor division.

✓ `%` returns the modulo/remainder.

✓ `**` performs exponentiation.

✓ Comparison operators produce Boolean values.

✓ `abs()` returns an absolute value.

✓ `min()` and `max()` find minimum and maximum values.

✓ `sum()` adds values from an iterable.

✓ `bin()`, `oct()`, and `hex()` return string representations of integers
  in different bases.

✓ Binary, octal, and hexadecimal integer literals use:

      0b
      0o
      0x

✓ `int()` can convert suitable values to integers.

✓ `int(value, base)` can interpret strings using a specified numeric base.

✓ Integer methods include `bit_length()` and `to_bytes()`.

✓ Integers support bitwise operations.

✓ Integers support bit shifting.

✓ `0` evaluates to `False` when converted to `bool`.

✓ Non-zero integers evaluate to `True` when converted to `bool`.

✓ `==` compares values, while `is` compares object identity.

✓ Static type checking should be treated as part of the quality standard for
  examples in this repository.

✓ `cast()` should be used deliberately when static analysis needs explicit
  type information; it should not be used as a blanket warning suppressor.

✓ General type behaviour is intentionally covered separately.
"""


# =============================================================================
# End of File
# =============================================================================
"""
**the identity preview also uses `cast()`**, 
because otherwise we risk the same 
static-analysis/literal-inference issue in a later example. 
The cast is documented exactly where it is used, 
so the learner knows *why* it's there rather than thinking 
`cast()` is required for normal integer assignment.
"""