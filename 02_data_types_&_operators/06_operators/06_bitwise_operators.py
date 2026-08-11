# type: ignore

# =============================================================================
# 06. Bitwise Operators
# =============================================================================
"""
Python Operators

File:
06_bitwise_operators.py

Topic:
Bitwise Operators

Overview:
Bitwise operators work directly with the individual bits of integer values.

The main bitwise operators are:

    &   Bitwise AND
    |   Bitwise OR
    ^   Bitwise XOR
    ~   Bitwise NOT
    <<  Left shift
    >>  Right shift

Bitwise operators are commonly used for:

    - Flags
    - Bit masks
    - Permissions
    - Binary protocols
    - Low-level data processing
    - Embedded programming
    - Performance-oriented integer operations
    - Setting and clearing individual bits

Important:
Bitwise operators work on integer values.

Binary representation examples:

    5  -> 0101
    3  -> 0011

The result of:

    5 & 3

is:

    0101
    0011
    ----
    0001

which is:

    1
"""

# =============================================================================
# 01. Bitwise AND
# =============================================================================

first_value: int = 5
second_value: int = 3

and_result: int = first_value & second_value

print(and_result)

# Binary:
#
# 5 -> 0101
# 3 -> 0011
#
#     0101
#     0011
#     ----
#     0001
#
# Result:
#
# 1

# =============================================================================
# 02. Bitwise OR
# =============================================================================

first_value = 5
second_value = 3

or_result: int = first_value | second_value

print(or_result)

# Binary:
#
#     0101
#     0011
#     ----
#     0111
#
# Result:
#
# 7

# =============================================================================
# 03. Bitwise XOR
# =============================================================================

first_value = 5
second_value = 3

xor_result: int = first_value ^ second_value

print(xor_result)

# XOR returns 1 when the corresponding bits are different.
#
#     0101
#     0011
#     ----
#     0110
#
# Result:
#
# 6

# =============================================================================
# 04. Bitwise NOT
# =============================================================================

number: int = 5

not_result: int = ~number

print(not_result)

# Python represents integers using signed integer semantics.
#
# The identity is:
#
#     ~x == -(x + 1)
#
# Therefore:
#
#     ~5
#     == -(5 + 1)
#     == -6

# =============================================================================
# 05. Left Shift
# =============================================================================

number = 5

left_shift_result: int = number << 1

print(left_shift_result)

# Binary representation:
#
#     5 -> 0101
#
# Shift left by one:
#
#     0101 << 1
#     1010
#
# Result:
#
#     10
#
# For non-negative integers, shifting left by one position is equivalent
# to multiplying by 2.

# =============================================================================
# 06. Right Shift
# =============================================================================

number = 20

right_shift_result: int = number >> 1

print(right_shift_result)

# Binary representation:
#
#     20 -> 10100
#
# Shift right by one:
#
#     10100 >> 1
#     01010
#
# Result:
#
#     10
#
# For non-negative integers, shifting right by one position is equivalent
# to integer division by 2.

# =============================================================================
# 07. AND With Two Binary Values
# =============================================================================

first_value = 12
second_value = 10

result: int = first_value & second_value

print(result)

#     1100
#     1010
#     ----
#     1000
#
# Result:
#
# 8

# =============================================================================
# 08. OR With Two Binary Values
# =============================================================================

first_value = 12
second_value = 10

result = first_value | second_value

print(result)

#     1100
#     1010
#     ----
#     1110
#
# Result:
#
# 14

# =============================================================================
# 09. XOR With Two Binary Values
# =============================================================================

first_value = 12
second_value = 10

result = first_value ^ second_value

print(result)

#     1100
#     1010
#     ----
#     0110
#
# Result:
#
# 6

# =============================================================================
# 10. AND Can Check Whether a Bit Is Set
# =============================================================================

value: int = 10
mask: int = 2

is_set: bool = (value & mask) != 0

print(is_set)

# 10 in binary:
#
#     1010
#
# 2 in binary:
#
#     0010
#
#     1010
#     0010
#     ----
#     0010
#
# Since the result is not zero, the selected bit is set.

# =============================================================================
# 11. Checking a Specific Bit
# =============================================================================

value = 13
bit_position: int = 2

mask = 1 << bit_position

bit_is_set: bool = (value & mask) != 0

print(bit_is_set)

# value:
#
#     13 -> 1101
#
# bit position:
#
#     2
#
# mask:
#
#     1 << 2
#     0100
#
# Checking:
#
#     1101
#     0100
#     ----
#     0100
#
# The bit is set.

# =============================================================================
# 12. Setting a Bit With OR
# =============================================================================

value = 8
bit_position = 1

mask = 1 << bit_position

value = value | mask

print(value)

# Original:
#
#     1000
#
# Mask:
#
#     0010
#
# OR:
#
#     1000
#     0010
#     ----
#     1010
#
# Result:
#
# 10

# =============================================================================
# 13. Clearing a Bit With AND and NOT
# =============================================================================

value = 15
bit_position = 2

mask = 1 << bit_position

value = value & ~mask

print(value)

# Original:
#
#     1111
#
# Mask:
#
#     0100
#
# NOT mask:
#
#     ...1011
#
# AND:
#
#     1111
#     1011
#     ----
#     1011
#
# Result:
#
# 11

# =============================================================================
# 14. Toggling a Bit With XOR
# =============================================================================

value = 10
bit_position = 1

mask = 1 << bit_position

value = value ^ mask

print(value)

# Original:
#
#     1010
#
# Mask:
#
#     0010
#
# XOR:
#
#     1010
#     0010
#     ----
#     1000
#
# Result:
#
# 8

# =============================================================================
# 15. Toggling the Same Bit Twice
# =============================================================================

value = 10
mask = 2

value = value ^ mask
value = value ^ mask

print(value)

# XOR with the same mask twice restores the original value.

# =============================================================================
# 16. Multiple Bit Flags
# =============================================================================

READ: int = 1 << 0
WRITE: int = 1 << 1
EXECUTE: int = 1 << 2

permissions: int = READ | WRITE

print(permissions)

# Flags:
#
# READ:
#     001
#
# WRITE:
#     010
#
# EXECUTE:
#     100
#
# READ | WRITE:
#
#     001
#     010
#     ---
#     011
#
# Result:
#
# 3

# =============================================================================
# 17. Checking a Permission Flag
# =============================================================================

READ = 1 << 0
WRITE = 1 << 1
EXECUTE = 1 << 2

permissions = READ | WRITE

can_read: bool = (permissions & READ) != 0
can_write: bool = (permissions & WRITE) != 0
can_execute: bool = (permissions & EXECUTE) != 0

print(can_read)
print(can_write)
print(can_execute)

# Output:
#
# True
# True
# False

# =============================================================================
# 18. Adding a Permission
# =============================================================================

READ = 1 << 0
WRITE = 1 << 1
EXECUTE = 1 << 2

permissions = READ

permissions = permissions | WRITE

print(permissions)

# Initially:
#
#     READ
#     001
#
# After adding WRITE:
#
#     001
#     010
#     ---
#     011

# =============================================================================
# 19. Removing a Permission
# =============================================================================

READ = 1 << 0
WRITE = 1 << 1
EXECUTE = 1 << 2

permissions = READ | WRITE | EXECUTE

permissions = permissions & ~WRITE

print(permissions)

# WRITE is cleared while READ and EXECUTE remain enabled.

# =============================================================================
# 20. Toggling a Permission
# =============================================================================

READ = 1 << 0
WRITE = 1 << 1

permissions = READ

permissions = permissions ^ WRITE

print(permissions)

# WRITE was disabled, so XOR enables it.
#
# Toggle again:
#
# permissions = permissions ^ WRITE
#
# would disable it.

# =============================================================================
# 21. Combining Multiple Masks
# =============================================================================

BIT_0: int = 1 << 0
BIT_1: int = 1 << 1
BIT_2: int = 1 << 2
BIT_3: int = 1 << 3

combined_mask: int = BIT_0 | BIT_2 | BIT_3

print(combined_mask)

# Combined binary mask:
#
#     1101

# =============================================================================
# 22. Checking Multiple Bits
# =============================================================================

value = 13
mask = BIT_0 | BIT_2

required_bits_are_set: bool = (value & mask) == mask

print(required_bits_are_set)

# value:
#
#     1101
#
# mask:
#
#     0101
#
# AND:
#
#     1101
#     0101
#     ----
#     0101
#
# Result equals the mask, so all requested bits are set.

# =============================================================================
# 23. Left Shift By Multiple Positions
# =============================================================================

number = 3

shifted_value: int = number << 3

print(shifted_value)

#     3 -> 0011
#
#     0011 << 3
#     11000
#
# Result:
#
# 24

# =============================================================================
# 24. Right Shift By Multiple Positions
# =============================================================================

number = 40

shifted_value = number >> 3

print(shifted_value)

#     40 -> 101000
#
#     101000 >> 3
#     000101
#
# Result:
#
# 5

# =============================================================================
# 25. Left Shift As Multiplication
# =============================================================================

number = 7

shifted_value = number << 2
multiplied_value: int = number * 4

print(shifted_value)
print(multiplied_value)

# For this non-negative integer:
#
#     number << 2
#
# is equivalent to:
#
#     number * 4

# =============================================================================
# 26. Right Shift As Integer Division
# =============================================================================

number = 20

shifted_value = number >> 2
divided_value: int = number // 4

print(shifted_value)
print(divided_value)

# For this non-negative integer:
#
#     number >> 2
#
# is equivalent to:
#
#     number // 4

# =============================================================================
# 27. Bitwise Operators With Zero
# =============================================================================

value = 42

and_zero: int = value & 0
or_zero: int = value | 0
xor_zero: int = value ^ 0

print(and_zero)
print(or_zero)
print(xor_zero)

# AND with zero:
#
#     value & 0
#     -> 0
#
# OR with zero:
#
#     value | 0
#     -> value
#
# XOR with zero:
#
#     value ^ 0
#     -> value

# =============================================================================
# 28. XOR Can Be Used To Detect Differences
# =============================================================================

first_value = 12
second_value = 10

difference_mask: int = first_value ^ second_value

print(difference_mask)

# XOR produces 1 at positions where the two values have different bits.
#
#     1100
#     1010
#     ----
#     0110

# =============================================================================
# 29. XOR Of A Value With Itself
# =============================================================================

value = 25

result = value ^ value

print(result)

# Every bit is equal, so XOR produces zero.
#
#     x ^ x
#     -> 0

# =============================================================================
# 30. AND Of A Value With Itself
# =============================================================================

value = 25

result = value & value

print(result)

# A value AND itself produces the same value.
#
#     x & x
#     -> x

# =============================================================================
# 31. OR Of A Value With Itself
# =============================================================================

value = 25

result = value | value

print(result)

# A value OR itself produces the same value.
#
#     x | x
#     -> x

# =============================================================================
# 32. Bitwise Operations With Binary Literals
# =============================================================================

first_value = 0b1100
second_value = 0b1010

and_result = first_value & second_value
or_result = first_value | second_value
xor_result = first_value ^ second_value

print(and_result)
print(or_result)
print(xor_result)

# Python supports binary integer literals using:
#
#     0b
#
# Example:
#
#     0b1100 == 12
#     0b1010 == 10

# =============================================================================
# 33. Binary Output With bin()
# =============================================================================

value = 13

binary_value: str = bin(value)

print(binary_value)

# bin() returns a string representation of an integer in binary.
#
# Example:
#
#     bin(13)
#     -> '0b1101'

# =============================================================================
# 34. Formatting Binary Values
# =============================================================================

value = 13

binary_value = format(
    value,
    "08b",
)

print(binary_value)

# "08b" means:
#
#     0  -> zero padding
#     8  -> width of eight characters
#     b  -> binary format
#
# Result:
#
#     00001101

# =============================================================================
# 35. Extracting The Lowest Bit
# =============================================================================

value = 13

lowest_bit: int = value & 1

print(lowest_bit)

# If the lowest bit is:
#
#     1
#
# the number is odd.
#
# If the lowest bit is:
#
#     0
#
# the number is even.

# =============================================================================
# 36. Checking Whether A Number Is Even
# =============================================================================

number = 24

is_even: bool = (number & 1) == 0

print(is_even)

# 24:
#
#     11000
#
# Lowest bit:
#
#     0
#
# Therefore the number is even.

# =============================================================================
# 37. Checking Whether A Number Is Odd
# =============================================================================

number = 25

is_odd: bool = (number & 1) == 1

print(is_odd)

# 25:
#
#     11001
#
# Lowest bit:
#
#     1
#
# Therefore the number is odd.

# =============================================================================
# 38. Extracting A Bit Field
# =============================================================================

value = 0b11010110

mask = 0b00001111

lowest_four_bits: int = value & mask

print(lowest_four_bits)

# The mask keeps only the lowest four bits.
#
#     11010110
#     00001111
#     --------
#     00000110
#
# Result:
#
# 6

# =============================================================================
# 39. Extracting Bits After Shifting
# =============================================================================

value = 0b11010110

shifted_value: int = value >> 4
field: int = shifted_value & 0b00001111

print(field)

# Original:
#
#     11010110
#
# Shift right:
#
#     00001101
#
# Mask:
#
#     00001111
#
# Result:
#
#     00001101
#
# which is:
#
# 13

# =============================================================================
# 40. Combining Bit Fields
# =============================================================================

first_field: int = 0b0101
second_field: int = 0b1010

combined_value: int = (
    (first_field << 4)
    | second_field
)

print(combined_value)

# first_field:
#
#     0101
#
# Shift left:
#
#     01010000
#
# second_field:
#
#     00001010
#
# OR:
#
#     01010000
#     00001010
#     --------
#     01011010

# =============================================================================
# 41. Using Hexadecimal Masks
# =============================================================================

value = 0xAB

mask = 0x0F

result = value & mask

print(result)

# Hexadecimal:
#
#     0xAB
#     0x0F
#     ----
#     0x0B
#
# Result:
#
# 11

# =============================================================================
# 42. Setting A Bit With A Hexadecimal Mask
# =============================================================================

value = 0x10
mask = 0x04

result = value | mask

print(result)

#     0x10 -> 00010000
#     0x04 -> 00000100
#
# OR:
#
#     00010100
#
# Result:
#
# 0x14

# =============================================================================
# 43. Clearing Bits With A Mask
# =============================================================================

value = 0b11111111
mask = 0b00001111

result = value & ~mask

print(result)

# The lowest four bits are cleared.

# =============================================================================
# 44. Inverting Bits With XOR
# =============================================================================

value = 0b1010
mask = 0b1111

result = value ^ mask

print(result)

#     1010
#     1111
#     ----
#     0101
#
# Result:
#
# 5

# =============================================================================
# 45. Bitwise Operators With Negative Integers
# =============================================================================

positive_value: int = 5
negative_value: int = -5

and_result = positive_value & negative_value
or_result = positive_value | negative_value
xor_result = positive_value ^ negative_value

print(and_result)
print(or_result)
print(xor_result)

# Python's negative integers use two's-complement-style semantics for
# bitwise operations.
#
# Bitwise operations involving negative numbers can therefore produce
# results that may be surprising if you only think in terms of finite
# unsigned binary representations.

# =============================================================================
# 46. Operator Precedence
# =============================================================================

value = 4

result_without_parentheses: int = value << 1 + 1
result_with_parentheses: int = value << (1 + 1)

print(result_without_parentheses)
print(result_with_parentheses)

# Use parentheses when combining shifts with arithmetic or other operators.
#
# Explicit parentheses make the intended operation easier to understand.
#
# Prefer:
#
#     value << (1 + 1)
#
# when the shift amount itself is an expression.

# =============================================================================
# 47. Combining Comparison And Bitwise Operations
# =============================================================================

value = 12
mask = 4

is_set = (value & mask) != 0

print(is_set)

# Parentheses make the intended grouping explicit:
#
#     (value & mask) != 0

# =============================================================================
# 48. Bit Mask Helper Function
# =============================================================================

def is_bit_set(
    value: int,
    bit_position: int,
) -> bool:
    """
    Return True when the requested bit is set.
    """
    mask: int = 1 << bit_position

    return (value & mask) != 0


value = 13

bit_zero_set: bool = is_bit_set(
    value,
    0,
)

bit_one_set: bool = is_bit_set(
    value,
    1,
)

bit_two_set: bool = is_bit_set(
    value,
    2,
)

print(bit_zero_set)
print(bit_one_set)
print(bit_two_set)

# 13 in binary:
#
#     1101
#
# Bit 0:
#     set
#
# Bit 1:
#     not set
#
# Bit 2:
#     set

# =============================================================================
# 49. Setting A Bit With A Helper Function
# =============================================================================

def set_bit(
    value: int,
    bit_position: int,
) -> int:
    """
    Set a specific bit to 1.
    """
    mask: int = 1 << bit_position

    return value | mask


value = 8

updated_value: int = set_bit(
    value,
    1,
)

print(updated_value)

#     1000
# OR:
#     0010
#     ----
#     1010
#
# Result:
#
# 10

# =============================================================================
# 50. Clearing And Toggling Bits With Helper Functions
# =============================================================================

def clear_bit(
    value: int,
    bit_position: int,
) -> int:
    """
    Clear a specific bit.
    """
    mask: int = 1 << bit_position

    return value & ~mask


def toggle_bit(
    value: int,
    bit_position: int,
) -> int:
    """
    Toggle a specific bit.
    """
    mask: int = 1 << bit_position

    return value ^ mask


value = 15

cleared_value: int = clear_bit(
    value,
    2,
)

toggled_value: int = toggle_bit(
value,
    1,
)

print(cleared_value)
print(toggled_value)

# clear_bit(15, 2):
#
#     1111
#     0100
#     ----
#     1011
#
# Result:
#
# 11
#
# toggle_bit(15, 1):
#
#     1111
#     0010
#     ----
#     1101
#
# Result:
#
# 13

# =============================================================================
# Bitwise Operators Summary
# =============================================================================

"""
Bitwise AND:

    &
    
    Keeps a bit as 1 only when both corresponding bits are 1.

Bitwise OR:

    |

    Keeps a bit as 1 when at least one corresponding bit is 1.

Bitwise XOR:

    ^

    Keeps a bit as 1 when the corresponding bits are different.

Bitwise NOT:

    ~

    Inverts the bits according to Python's integer semantics.

Left shift:

    <<

    Shifts bits toward higher positions.

Right shift:

    >>

    Shifts bits toward lower positions.

Common bit-mask operations:

    Check a bit:
        value & mask

    Set a bit:
        value | mask

    Clear a bit:
        value & ~mask

    Toggle a bit:
        value ^ mask

    Create a bit mask:
        1 << bit_position
"""

# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Bitwise operators operate on integer values.

✓ The main bitwise operators are:

    &
    |
    ^
    ~
    <<
    >>

✓ AND is useful for testing and masking bits.

✓ OR is useful for setting bits.

✓ XOR is useful for toggling bits and detecting differences.

✓ NOT inverts bits according to Python's signed integer semantics.

✓ Left shift moves bits toward higher positions.

✓ Right shift moves bits toward lower positions.

✓ A mask is commonly created using:

    1 << bit_position

✓ A bit can be checked using:

    (value & mask) != 0

✓ A bit can be set using:

    value | mask

✓ A bit can be cleared using:

    value & ~mask

✓ A bit can be toggled using:

    value ^ mask

✓ Multiple flags can be combined using OR.

✓ Multiple flags can be checked using AND.

✓ XOR with the same value produces zero:

    value ^ value == 0

✓ AND with zero produces zero:

    value & 0 == 0

✓ OR with zero preserves the value:

    value | 0 == value

✓ XOR with zero preserves the value:

    value ^ 0 == value

✓ Binary literals use:

    0b

✓ Hexadecimal literals are useful when working with bit masks.

✓ bin() can display an integer in binary.

✓ format(value, "08b") can display a zero-padded binary representation.

✓ Bitwise operations are especially useful for flags, permissions,
  masks, protocols, and low-level data representation.

Core model:

    VALUE
      ↓
    BINARY BITS
      ↓
    BITWISE OPERATOR
      ↓
    NEW INTEGER

Bit-mask model:

    BIT POSITION
          ↓
    1 << position
          ↓
       MASK
          ↓
    ┌─────┼─────────────┐
    ↓     ↓             ↓
  CHECK  SET          CLEAR
    ↓     ↓             ↓
   &     |            & ~

Toggle:

    value ^ mask
         ↓
      toggle bit

The most important patterns to remember are:

    mask = 1 << bit_position

    is_set = (value & mask) != 0

    value = value | mask

    value = value & ~mask

    value = value ^ mask

"""

# =============================================================================
# End of 06_bitwise_operators.py
# =============================================================================