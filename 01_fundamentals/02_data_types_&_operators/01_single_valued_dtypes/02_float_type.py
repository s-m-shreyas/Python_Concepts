"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Single-Valued Data Types

Data Type
---------
Float (`float`)

Overview
--------
A float represents a real number using Python's floating-point representation.

Examples:

    0.0
    3.14
    -12.5

This module covers:

    - Float literals
    - Default and non-default values
    - Positive, negative, and zero values
    - Type identification
    - Runtime type checking
    - Arithmetic operations
    - Division
    - Floor division
    - Modulo
    - Exponentiation
    - Unary operators
    - Absolute values
    - Minimum and maximum values
    - Rounding
    - Floating-point precision
    - Floating-point comparison
    - Scientific notation
    - Infinity
    - NaN
    - Float conversion
    - Float methods

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""

import math


# =============================================================================
# Example 1: Float Literals
# =============================================================================

positive_float: float = 3.14
negative_float: float = -3.14
zero_float: float = 0.0

print(f"Positive float: {positive_float}")
print(f"Negative float: {negative_float}")
print(f"Zero float:     {zero_float}")


# A floating-point literal normally contains a decimal point.
#
# Examples:
#
#     3.14
#     -3.14
#     0.0


# =============================================================================
# Example 2: Default and Non-Default Float Values
# =============================================================================

default_like_float: float = 0.0

non_default_positive_float: float = 12.5
non_default_negative_float: float = -12.5

print(f"Default-like value: {default_like_float}")
print(f"Positive value:     {non_default_positive_float}")
print(f"Negative value:     {non_default_negative_float}")


# Python does NOT automatically assign 0.0 to an annotated float variable.
#
# This:
#
#     measurement: float
#
# is only a type annotation.
#
# It does NOT initialize the variable.
#
# Explicit initialization is required:
#
#     measurement: float = 0.0


# =============================================================================
# Example 3: Checking the Float Type
# =============================================================================

float_value: float = 25.75

print(f"Value: {float_value}")
print(f"Type:  {type(float_value)}")


# `type()` returns the type/class of an object.
#
# Expected:
#
#     <class 'float'>


# =============================================================================
# Example 4: Runtime Float Type Checking
# =============================================================================

float_candidate: object = 25.75
integer_candidate: object = 25

float_check: bool = isinstance(
    float_candidate,
    float,
)

integer_check: bool = isinstance(
    integer_candidate,
    float,
)

print(f"25.75 is a float: {float_check}")
print(f"25 is a float:    {integer_check}")


# The variables are intentionally typed as `object`.
#
# This gives `isinstance()` meaningful runtime work to perform.
#
# If we wrote:
#
#     value: float = 25.75
#
# a static type checker already knows that `value` is a float and may report:
#
#     Unnecessary isinstance call
#
# Therefore, `object` is used when specifically teaching runtime type
# inspection.


# =============================================================================
# Example 5: Basic Float Arithmetic
# =============================================================================

first_float: float = 10.5
second_float: float = 2.5

addition_result: float = first_float + second_float
subtraction_result: float = first_float - second_float
multiplication_result: float = first_float * second_float
division_result: float = first_float / second_float

print(f"Addition:       {addition_result}")
print(f"Subtraction:    {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division:       {division_result}")


# Standard arithmetic operators:
#
#     +   addition
#     -   subtraction
#     *   multiplication
#     /   division


# =============================================================================
# Example 6: True Division
# =============================================================================

division_left: float = 10.0
division_right: float = 4.0

true_division_result: float = division_left / division_right

print(f"Result: {true_division_result}")
print(f"Type:   {type(true_division_result)}")


# `/` performs true division.
#
# The result is a float.


# =============================================================================
# Example 7: Floor Division
# =============================================================================

floor_dividend: float = 10.5
floor_divisor: float = 3.0

floor_result: float = floor_dividend // floor_divisor

print(f"Floor division: {floor_result}")


# `//` performs floor division.
#
# With float operands, the result is also a float.
#
#     10.5 // 3.0
#
# produces:
#
#     3.0


# =============================================================================
# Example 8: Modulo
# =============================================================================

modulo_dividend: float = 10.5
modulo_divisor: float = 3.0

remainder_result: float = modulo_dividend % modulo_divisor

print(f"Remainder: {remainder_result}")


# `%` returns the remainder associated with floor division.
#
#     10.5 % 3.0
#
# produces:
#
#     1.5


# =============================================================================
# Example 9: Exponentiation
# =============================================================================

power_base: float = 2.5
power_exponent: int = 2

power_result: float = power_base ** power_exponent

print(f"Power result: {power_result}")


# `**` performs exponentiation.
#
#     2.5 ** 2
#
# produces:
#
#     6.25


# =============================================================================
# Example 10: Unary Operators
# =============================================================================

unary_float: float = 25.5

positive_unary_result: float = +unary_float
negative_unary_result: float = -unary_float

print(f"Positive: {positive_unary_result}")
print(f"Negative: {negative_unary_result}")


# Unary operators:
#
#     +value
#     -value


# =============================================================================
# Example 11: Absolute Value
# =============================================================================

absolute_source: float = -42.75

absolute_result: float = abs(absolute_source)

print(f"Original value: {absolute_source}")
print(f"Absolute value: {absolute_result}")


# `abs()` returns the absolute value of a number.


# =============================================================================
# Example 12: Minimum and Maximum
# =============================================================================

first_measurement: float = 12.5
second_measurement: float = 7.25
third_measurement: float = 18.75

minimum_result: float = min(
    first_measurement,
    second_measurement,
    third_measurement,
)

maximum_result: float = max(
    first_measurement,
    second_measurement,
    third_measurement,
)

print(f"Minimum: {minimum_result}")
print(f"Maximum: {maximum_result}")


# `min()` returns the smallest supplied value.
#
# `max()` returns the largest supplied value.


# =============================================================================
# Example 13: Rounding
# =============================================================================

rounding_value: float = 12.56789

rounded_to_two_places: float = round(
    rounding_value,
    2,
)

rounded_to_zero_places: int = round(
    rounding_value,
)

print(f"Original:      {rounding_value}")
print(f"Two decimals:  {rounded_to_two_places}")
print(f"Zero decimals: {rounded_to_zero_places}")


# `round()` rounds a numerical value.
#
#     round(float, ndigits)
#
# returns a float when `ndigits` is supplied.
#
#     round(float)
#
# returns an integer.


# =============================================================================
# Example 14: Floating-Point Precision
# =============================================================================

precision_first: float = 0.1
precision_second: float = 0.2

precision_result: float = (
    precision_first
    + precision_second
)

print(f"0.1 + 0.2 = {precision_result}")
print(f"0.1 + 0.2 == 0.3: {precision_result == 0.3}")


# Floating-point numbers use binary floating-point representation.
#
# Some decimal fractions cannot be represented exactly in binary.
#
# Therefore:
#
#     0.1 + 0.2
#
# may produce:
#
#     0.30000000000000004
#
# instead of exactly:
#
#     0.3
#
# This is a representation limitation, not an arithmetic bug.


# =============================================================================
# Example 15: Comparing Floats Safely
# =============================================================================

comparison_first: float = 0.1
comparison_second: float = 0.2
comparison_expected: float = 0.3

comparison_result: bool = math.isclose(
    comparison_first + comparison_second,
    comparison_expected,
)

print(
    f"Values are approximately equal: "
    f"{comparison_result}"
)


# `math.isclose()` is useful when floating-point precision makes direct
# equality comparison unreliable.


# =============================================================================
# Example 16: Scientific Notation
# =============================================================================

large_scientific_value: float = 1.5e6
small_scientific_value: float = 2.5e-3

print(f"Large value: {large_scientific_value}")
print(f"Small value: {small_scientific_value}")


# Scientific notation uses `e` or `E`.
#
#     1.5e6
#
# means:
#
#     1.5 × 10^6
#
#     2.5e-3
#
# means:
#
#     2.5 × 10^-3


# =============================================================================
# Example 17: Infinity
# =============================================================================

positive_infinity: float = float("inf")
negative_infinity: float = float("-inf")

print(f"Positive infinity: {positive_infinity}")
print(f"Negative infinity: {negative_infinity}")

print(
    f"Is positive infinity infinite: "
    f"{math.isinf(positive_infinity)}"
)


# Python floats support positive and negative infinity.
#
# `math.isinf()` checks whether a float represents infinity.


# =============================================================================
# Example 18: NaN
# =============================================================================

not_a_number: float = float("nan")

print(f"NaN value: {not_a_number}")
print(f"Is NaN: {math.isnan(not_a_number)}")


# `NaN` means "Not a Number".
#
# It represents an undefined or unrepresentable floating-point result.
#
# `math.isnan()` should be used to test for NaN.


# =============================================================================
# Example 19: NaN Comparison Behaviour
# =============================================================================

nan_value: float = float("nan")

nan_equality_result: bool = nan_value == nan_value
nan_identity_result: bool = nan_value is nan_value

print(f"NaN == NaN: {nan_equality_result}")
print(f"NaN is NaN: {nan_identity_result}")


# NaN has special comparison behaviour.
#
#     nan_value == nan_value
#
# evaluates to:
#
#     False
#
# while:
#
#     nan_value is nan_value
#
# evaluates to:
#
#     True
#
# This is a useful preview of the difference between equality and identity.


# =============================================================================
# Example 20: Converting an Integer to a Float
# =============================================================================

integer_value: int = 25

converted_float_value: float = float(
    integer_value
)

print(f"Original value:  {integer_value}")
print(f"Original type:   {type(integer_value)}")
print(f"Converted value: {converted_float_value}")
print(f"Converted type:  {type(converted_float_value)}")


# `float()` can convert suitable numeric values into floating-point values.
#
#     25 -> 25.0


# =============================================================================
# Example 21: Converting a String to a Float
# =============================================================================

numeric_text_value: str = "25.75"

converted_float_value_str: float = float(
    numeric_text_value
)

print(f"Original value:  {numeric_text_value}")
print(f"Original type:   {type(numeric_text_value)}")
print(f"Converted value: {converted_float_value_str}")
print(f"Converted type:  {type(converted_float_value_str)}")


# A string containing a valid floating-point representation can be converted
# using `float()`.


# =============================================================================
# Example 22: Converting a Float to an Integer
# =============================================================================

source_float: float = 12.75

converted_integer: int = int(
    source_float
)

print(f"Original float:    {source_float}")
print(f"Converted integer: {converted_integer}")


# Converting a float to an integer with `int()` truncates toward zero.
#
#     int(12.75)  -> 12
#     int(-12.75) -> -12
#
# This is different from mathematical floor division.


# =============================================================================
# Example 23: Float Methods
# =============================================================================

method_value: float = 42.75

integer_check_method: bool = method_value.is_integer()

as_integer_ratio: tuple[int, int] = (
    method_value.as_integer_ratio()
)

hexadecimal_value: str = method_value.hex()

print(f"Is integer:         {integer_check_method}")
print(f"Integer ratio:      {as_integer_ratio}")
print(f"Hex representation: {hexadecimal_value}")


# `is_integer()` checks whether the float has no fractional component.
#
# `as_integer_ratio()` returns an exact numerator/denominator pair.
#
# `hex()` returns a hexadecimal string representation of the float.


# =============================================================================
# Example 24: Float Constants From the Math Module
# =============================================================================

print(f"Pi:        {math.pi}")
print(f"Euler's e: {math.e}")
print(f"Tau:       {math.tau}")


# These are ordinary float values provided by the `math` module.
#
#     math.pi
#     math.e
#     math.tau


# =============================================================================
# Example 25: Float Identity and Equality Preview
# =============================================================================

first_float_value: float = float(
    "1000.5"
)

second_float_value: float = float(
    "1000.5"
)

print(
    f"Equal values: "
    f"{first_float_value == second_float_value}"
)

print(
    f"Same object:  "
    f"{first_float_value is second_float_value}"
)


# The values are created from runtime string conversion so static analysis
# does not reduce the example to known float literals.
#
# `==` compares values.
#
# `is` compares object identity.
#
# Identity should never be used as a substitute for value comparison.
#
# The complete distinction is covered later under:
#
#     17_type_behaviour/03_equality_vs_identity.py


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `float` represents floating-point numerical values.

✓ Positive, negative, and zero floating-point values are valid.

✓ `0.0` is a common default-like value, but Python does not automatically
  initialize an annotated float variable with `0.0`.

✓ A type annotation alone does not initialize a variable.

✓ `type()` identifies the concrete type of an object.

✓ `isinstance()` performs runtime type checking.

✓ `object` is useful when demonstrating runtime type inspection because the
  concrete runtime type is not already fixed by the annotation.

✓ Float values support standard arithmetic operations.

✓ `/` performs true division.

✓ `//` performs floor division.

✓ `%` returns a remainder.

✓ `**` performs exponentiation.

✓ `abs()` returns the absolute value.

✓ `min()` and `max()` can operate on float values.

✓ `round()` rounds floating-point values.

✓ Floating-point representation can introduce precision differences.

✓ `math.isclose()` is useful for approximate floating-point comparisons.

✓ Scientific notation can represent very large and very small values.

✓ Python floats support positive infinity, negative infinity, and NaN.

✓ `math.isinf()` checks for infinity.

✓ `math.isnan()` checks for NaN.

✓ NaN has special equality behaviour.

✓ `float()` can convert suitable numeric values and strings to floats.

✓ `int(float_value)` truncates toward zero.

✓ Float methods include:
      is_integer()
      as_integer_ratio()
      hex()

✓ `math.pi`, `math.e`, and `math.tau` are float values.

✓ `==` compares values, while `is` compares object identity.

✓ General type behaviour is covered separately.
"""


# =============================================================================
# End of File
# =============================================================================