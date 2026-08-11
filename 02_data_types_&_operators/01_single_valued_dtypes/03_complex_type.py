"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Single-Valued Data Types

Data Type
---------
Complex (`complex`)

Overview
--------
A complex number consists of two parts:

    - Real part
    - Imaginary part

The general mathematical form is:

    a + bj

where:

    a -> real part
    b -> imaginary part
    j -> imaginary unit

Python uses `j` to represent the imaginary component.

Examples:

    3 + 4j
    -2 + 5j
    7j
    5 + 0j

This module covers:

    - Complex literals
    - Default and non-default values
    - Real and imaginary components
    - Type identification
    - Runtime type checking
    - Complex arithmetic
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Exponentiation
    - Conjugates
    - Magnitude
    - Polar representation
    - Complex construction
    - Conversion behaviour
    - Complex-specific attributes and methods

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


import cmath
import math


# =============================================================================
# Example 1: Complex Literals
# =============================================================================

positive_complex_number: complex = 3 + 4j
negative_complex_number: complex = -2 - 5j
imaginary_only_number: complex = 7j
real_only_complex_number: complex = 5 + 0j

print(f"Positive complex:      {positive_complex_number}")
print(f"Negative complex:      {negative_complex_number}")
print(f"Imaginary-only value:  {imaginary_only_number}")
print(f"Real-only complex:     {real_only_complex_number}")


# Python uses `j` to represent the imaginary component.
#
# General form:
#
#     a + bj
#
# where:
#
#     a -> real part
#     b -> imaginary part


# =============================================================================
# Example 2: Default and Non-Default Complex Values
# =============================================================================

default_like_complex: complex = 0j

non_default_complex_a: complex = 3 + 4j
non_default_complex_b: complex = -5 - 2j

print(f"Default-like value: {default_like_complex}")
print(f"Non-default value:  {non_default_complex_a}")
print(f"Another value:      {non_default_complex_b}")


# Python does NOT automatically assign `0j` to an annotated complex variable.
#
# This:
#
#     number: complex
#
# is only a type annotation.
#
# It does NOT initialize the variable.
#
# Explicit initialization is required:
#
#     number: complex = 0j
#
# Therefore, `0j` is a commonly used default-like value, not Python's
# automatic default.


# =============================================================================
# Example 3: Checking the Complex Type
# =============================================================================

complex_type_sample: complex = 8 + 6j

print(f"Value: {complex_type_sample}")
print(f"Type:  {type(complex_type_sample)}")


# `type()` returns the type/class of an object.
#
# Expected:
#
#     <class 'complex'>


# =============================================================================
# Example 4: Runtime Complex Type Checking
# =============================================================================

complex_runtime_candidate: object = 4 + 9j
integer_runtime_candidate: object = 12

complex_runtime_check: bool = isinstance(
    complex_runtime_candidate,
    complex,
)

integer_runtime_check: bool = isinstance(
    integer_runtime_candidate,
    complex,
)

print(
    f"4 + 9j is complex: "
    f"{complex_runtime_check}"
)

print(
    f"12 is complex:      "
    f"{integer_runtime_check}"
)


# The candidates are intentionally typed as `object`.
#
# This gives `isinstance()` meaningful runtime work to perform.
#
# If a value were already annotated as `complex`, a static type checker could
# determine that it is already a complex value and report the check as
# unnecessary.


# =============================================================================
# Example 5: Accessing the Real and Imaginary Parts
# =============================================================================

component_sample_value: complex = 12 + 7j

real_component_value: float = (
    component_sample_value.real
)

imaginary_component_value: float = (
    component_sample_value.imag
)

print(f"Complex value:     {component_sample_value}")
print(f"Real component:    {real_component_value}")
print(f"Imaginary component: {imaginary_component_value}")


# Every complex number has:
#
#     .real
#     .imag
#
# attributes.
#
# Both components are represented as floats.


# =============================================================================
# Example 6: Complex Number From Separate Components
# =============================================================================

constructed_real_component: float = 6.5
constructed_imaginary_component: float = 2.5

constructed_complex_value: complex = complex(
    constructed_real_component,
    constructed_imaginary_component,
)

print(
    f"Constructed complex value: "
    f"{constructed_complex_value}"
)


# `complex(real, imaginary)` constructs a complex number from two components.
#
#     complex(6.5, 2.5)
#
# produces:
#
#     (6.5+2.5j)


# =============================================================================
# Example 7: Addition
# =============================================================================

addition_complex_left: complex = 4 + 3j
addition_complex_right: complex = 2 + 5j

addition_complex_result: complex = (
    addition_complex_left
    + addition_complex_right
)

print(
    f"Addition result: "
    f"{addition_complex_result}"
)


# Complex numbers are added component by component:
#
#     (4 + 3j) + (2 + 5j)
#
#     = (4 + 2) + (3 + 5)j
#
#     = 6 + 8j


# =============================================================================
# Example 8: Subtraction
# =============================================================================

subtraction_complex_left: complex = 9 + 7j
subtraction_complex_right: complex = 3 + 2j

subtraction_complex_result: complex = (
    subtraction_complex_left
    - subtraction_complex_right
)

print(
    f"Subtraction result: "
    f"{subtraction_complex_result}"
)


# Complex subtraction also happens component by component.


# =============================================================================
# Example 9: Multiplication
# =============================================================================

multiplication_complex_left: complex = 3 + 2j
multiplication_complex_right: complex = 4 + 5j

multiplication_complex_result: complex = (
    multiplication_complex_left
    * multiplication_complex_right
)

print(
    f"Multiplication result: "
    f"{multiplication_complex_result}"
)


# Multiplication follows algebraic expansion.
#
#     (3 + 2j)(4 + 5j)
#
#     = 12 + 15j + 8j + 10j²
#
# Since:
#
#     j² = -1
#
# the result becomes:
#
#     2 + 23j


# =============================================================================
# Example 10: Division
# =============================================================================

division_complex_numerator: complex = 8 + 6j
division_complex_denominator: complex = 2 + 1j

division_complex_result: complex = (
    division_complex_numerator
    / division_complex_denominator
)

print(
    f"Division result: "
    f"{division_complex_result}"
)


# Complex numbers support division.
#
# Python handles the required complex-number arithmetic automatically.


# =============================================================================
# Example 11: Exponentiation
# =============================================================================

power_complex_base: complex = 2 + 3j
power_complex_exponent: int = 2

power_complex_result: complex = (
    power_complex_base
    ** power_complex_exponent
)

print(
    f"Power result: "
    f"{power_complex_result}"
)


# Complex numbers support exponentiation using `**`.


# =============================================================================
# Example 12: Unary Operators
# =============================================================================

unary_complex_value: complex = 5 + 4j

positive_complex_result: complex = (
    +unary_complex_value
)

negative_complex_result: complex = (
    -unary_complex_value
)

print(
    f"Positive: {positive_complex_result}"
)

print(
    f"Negative: {negative_complex_result}"
)


# Unary operators:
#
#     +value
#     -value


# =============================================================================
# Example 13: Complex Conjugate
# =============================================================================

conjugate_source_value: complex = 7 + 3j

conjugate_result_value: complex = (
    conjugate_source_value.conjugate()
)

print(
    f"Original:   {conjugate_source_value}"
)

print(
    f"Conjugate:  {conjugate_result_value}"
)


# The conjugate of:
#
#     a + bj
#
# is:
#
#     a - bj
#
# The sign of the imaginary component changes.


# =============================================================================
# Example 14: Magnitude
# =============================================================================

magnitude_complex_value: complex = 3 + 4j

magnitude_result: float = abs(
    magnitude_complex_value
)

print(
    f"Complex value: {magnitude_complex_value}"
)

print(
    f"Magnitude:     {magnitude_result}"
)


# `abs()` returns the magnitude of a complex number.
#
# Mathematically:
#
#     |a + bj| = √(a² + b²)
#
# For:
#
#     3 + 4j
#
# the magnitude is:
#
#     5.0


# =============================================================================
# Example 15: Complex Magnitude Using math.hypot()
# =============================================================================

hypot_real_component: float = 5.0
hypot_imaginary_component: float = 12.0

hypot_magnitude_result: float = math.hypot(
    hypot_real_component,
    hypot_imaginary_component,
)

print(
    f"Magnitude: {hypot_magnitude_result}"
)


# `math.hypot()` calculates:
#
#     √(x² + y²)
#
# and can therefore be used to calculate the magnitude from the real and
# imaginary components.


# =============================================================================
# Example 16: Phase Angle
# =============================================================================

phase_complex_value: complex = 1 + 1j

phase_angle_radians: float = cmath.phase(
    phase_complex_value
)

print(
    f"Complex value:  {phase_complex_value}"
)

print(
    f"Phase radians:  {phase_angle_radians}"
)


# `cmath.phase()` returns the phase angle of a complex number in radians.


# =============================================================================
# Example 17: Polar Representation
# =============================================================================

polar_complex_value: complex = 3 + 4j

polar_magnitude: float
polar_angle: float

polar_magnitude, polar_angle = cmath.polar(
    polar_complex_value
)

print(
    f"Magnitude: {polar_magnitude}"
)

print(
    f"Angle:     {polar_angle}"
)


# `cmath.polar()` converts a complex number into:
#
#     (magnitude, phase)
#
# representation.


# =============================================================================
# Example 18: Converting Polar Coordinates to Complex
# =============================================================================

polar_radius_value: float = 5.0
polar_angle_value: float = math.pi / 4

polar_to_complex_result: complex = (
    cmath.rect(
        polar_radius_value,
        polar_angle_value,
    )
)

print(
    f"Complex value: "
    f"{polar_to_complex_result}"
)


# `cmath.rect(radius, angle)` converts polar representation back into a
# complex number.


# =============================================================================
# Example 19: Complex String Conversion
# =============================================================================

complex_text_value: str = "3+4j"

parsed_complex_value: complex = complex(
    complex_text_value
)

print(
    f"Original text:  {complex_text_value}"
)

print(
    f"Converted value: {parsed_complex_value}"
)


# `complex()` can parse a valid complex-number string.
#
#     "3+4j"
#
# becomes:
#
#     (3+4j)


# =============================================================================
# Example 20: Integer and Float Components
# =============================================================================

mixed_real_component: int = 8
mixed_imaginary_component: float = 2.5

mixed_complex_result: complex = complex(
    mixed_real_component,
    mixed_imaginary_component,
)

print(
    f"Complex result: {mixed_complex_result}"
)


# The real and imaginary components can originate from different numeric
# types.


# =============================================================================
# Example 21: Complex Equality
# =============================================================================

equality_complex_left: complex = 5 + 8j
equality_complex_right: complex = 5 + 8j

complex_equality_result: bool = (
    equality_complex_left
    == equality_complex_right
)

print(
    f"Equal complex values: "
    f"{complex_equality_result}"
)


# `==` compares the real and imaginary components of complex numbers.


# =============================================================================
# Example 22: Complex Identity
# =============================================================================

identity_complex_left: complex = complex(
    "1000+500j"
)

identity_complex_right: complex = complex(
    "1000+500j"
)

complex_identity_result: bool = (
    identity_complex_left
    is identity_complex_right
)

print(
    f"Same complex object: "
    f"{complex_identity_result}"
)


# `is` compares object identity.
#
# Two complex objects can contain equal values without being the same object.
#
# Therefore:
#
#     == -> value comparison
#     is -> identity comparison
#
# The complete distinction is covered later under:
#
#     17_type_behaviour/03_equality_vs_identity.py


# =============================================================================
# Example 23: Complex Numbers and Boolean Conversion
# =============================================================================

zero_complex_value: complex = 0j
nonzero_complex_value: complex = 0 + 5j

zero_complex_bool: bool = bool(
    zero_complex_value
)

nonzero_complex_bool: bool = bool(
    nonzero_complex_value
)

print(
    f"bool(0j):    {zero_complex_bool}"
)

print(
    f"bool(5j):    {nonzero_complex_bool}"
)


# A complex number is considered:
#
#     0j       -> False
#     non-zero -> True
#
# A complex number is zero only when BOTH its real and imaginary components
# are zero.


# =============================================================================
# Example 24: Complex Number With a Zero Imaginary Component
# =============================================================================

real_only_complex: complex = 12 + 0j

print(
    f"Value: {real_only_complex}"
)

print(
    f"Real:  {real_only_complex.real}"
)

print(
    f"Imag:  {real_only_complex.imag}"
)


# A complex number can have a zero imaginary component.
#
#     12 + 0j
#
# is still a complex object even though its imaginary component is zero.


# =============================================================================
# Example 25: Complex Number With a Zero Real Component
# =============================================================================

imaginary_only_complex: complex = 0 + 12j

print(
    f"Value: {imaginary_only_complex}"
)

print(
    f"Real:  {imaginary_only_complex.real}"
)

print(
    f"Imag:  {imaginary_only_complex.imag}"
)


# A complex number can have a zero real component.
#
#     0 + 12j
#
# is a purely imaginary complex number.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `complex` represents complex numbers.

✓ A complex number contains:
      - real component
      - imaginary component

✓ Python uses `j` for the imaginary component.

✓ The general form is:
      a + bj

✓ `0j` is a commonly used default-like complex value, but Python does not
  automatically initialize an annotated complex variable with `0j`.

✓ A type annotation alone does not initialize a variable.

✓ `type()` identifies the concrete type of an object.

✓ `isinstance()` performs runtime type checking.

✓ `object` is useful when demonstrating runtime type inspection.

✓ Complex numbers support:
      + addition
      - subtraction
      * multiplication
      / division
      ** exponentiation

✓ `.real` returns the real component.

✓ `.imag` returns the imaginary component.

✓ `complex(real, imaginary)` constructs a complex number.

✓ `conjugate()` returns the complex conjugate.

✓ `abs()` returns the magnitude of a complex number.

✓ `cmath.phase()` returns the phase angle in radians.

✓ `cmath.polar()` converts a complex number into polar representation.

✓ `cmath.rect()` converts polar representation into a complex number.

✓ `complex()` can convert suitable strings into complex numbers.

✓ Complex numbers support equality comparison using `==`.

✓ `is` checks object identity, not numerical equality.

✓ A zero complex number evaluates to `False`.

✓ A non-zero complex number evaluates to `True`.

✓ A complex number can have:
      - a zero real component
      - a zero imaginary component

✓ General equality vs identity behaviour is covered separately.

✓ General type conversion behaviour is covered separately.
"""


# =============================================================================
# End of File
# =============================================================================