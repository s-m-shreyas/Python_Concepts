# type: ignore
# =============================================================================
# 09. Unary Operators
# =============================================================================
"""
Python Operators

File:
    09_unary_operators.py

Topic:
    Unary Operators

Overview:
    A unary operator operates on exactly one operand.

Common Python unary operators:

    +value
        Unary plus.

    -value
        Unary minus.

    ~value
        Bitwise inversion.

    not value
        Logical negation.

Unary operators are different from binary operators because they work with
one value instead of two values.

Examples:

    +10
    -10
    ~10
    not True

Important distinction:

    -5
        Uses unary minus.

    5 - 2
        Uses binary subtraction.

    +5
        Uses unary plus.

    5 + 2
        Uses binary addition.

This file demonstrates practical uses of unary operators.
"""

# =============================================================================
# 01. Unary Plus With a Positive Integer
# =============================================================================

positive_number: int = 10

result: int = +positive_number

print(result)


# =============================================================================
# 02. Unary Plus With a Negative Integer
# =============================================================================

negative_number: int = -10

result = +negative_number

print(result)


# =============================================================================
# 03. Unary Minus With a Positive Integer
# =============================================================================

number: int = 10

result = -number

print(result)


# =============================================================================
# 04. Unary Minus With a Negative Integer
# =============================================================================

number = -10

result = -number

print(result)


# =============================================================================
# 05. Unary Plus Does Not Change the Numeric Value
# =============================================================================

value: int = 25

positive_value: int = +value

print(value)
print(positive_value)


# =============================================================================
# 06. Unary Minus Changes the Sign
# =============================================================================

value = 25

negative_value: int = -value

print(value)
print(negative_value)


# =============================================================================
# 07. Double Unary Minus
# =============================================================================

value = 20

result = -(-value)

print(result)


# =============================================================================
# 08. Double Unary Plus
# =============================================================================

value = 20

result = +(+(value))

print(result)


# =============================================================================
# 09. Unary Minus On Zero
# =============================================================================

zero: int = 0

result = -zero

print(result)


# =============================================================================
# 10. Unary Plus On Zero
# =============================================================================

zero = 0

result = +zero

print(result)


# =============================================================================
# 11. Unary Minus With Float
# =============================================================================

temperature: float = 23.5

negative_temperature: float = -temperature

print(negative_temperature)


# =============================================================================
# 12. Unary Plus With Float
# =============================================================================

temperature = -23.5

positive_temperature: float = +temperature

print(positive_temperature)


# =============================================================================
# 13. Unary Minus With Boolean
# =============================================================================

enabled: bool = True

result: int = -enabled

print(result)


# =============================================================================
# 14. Unary Plus With Boolean
# =============================================================================

enabled = True

result = +enabled

print(result)


# =============================================================================
# 15. Unary Minus With False
# =============================================================================

disabled: bool = False

result = -disabled

print(result)


# =============================================================================
# 16. Logical `not` With True
# =============================================================================

value: bool = True

result: bool = not value

print(result)


# =============================================================================
# 17. Logical `not` With False
# =============================================================================

value = False

result = not value

print(result)


# =============================================================================
# 18. `not` With Zero
# =============================================================================

number = 0

result: bool = not number

print(result)


# =============================================================================
# 19. `not` With Non-Zero Number
# =============================================================================

number = 10

result = not number

print(result)


# =============================================================================
# 20. `not` With an Empty String
# =============================================================================

text: str = ""

result: bool = not text

print(result)


# =============================================================================
# 21. `not` With a Non-Empty String
# =============================================================================

text = "Python"

result = not text

print(result)


# =============================================================================
# 22. `not` With an Empty List
# =============================================================================

items: list[int] = []

result: bool = not items

print(result)


# =============================================================================
# 23. `not` With a Non-Empty List
# =============================================================================

items = [1, 2, 3]

result = not items

print(result)


# =============================================================================
# 24. `not` With None
# =============================================================================

value: None = None

result: bool = not value

print(result)


# =============================================================================
# 25. `not` With a Truthy Value
# =============================================================================

value: str = "Python"

if not value:
    print("Value is empty.")
else:
    print("Value is not empty.")


# =============================================================================
# 26. `not` Used To Check an Empty Collection
# =============================================================================

users: list[str] = []

if not users:
    print("No users found.")


# =============================================================================
# 27. `not` Used To Check a Non-Empty Collection
# =============================================================================

users = ["Alex", "Sam"]

if not users:
    print("No users found.")
else:
    print("Users are available.")


# =============================================================================
# 28. Bitwise Inversion With Zero
# =============================================================================

number = 0

result: int = ~number

print(result)


# =============================================================================
# 29. Bitwise Inversion With One
# =============================================================================

number = 1

result = ~number

print(result)


# =============================================================================
# 30. Bitwise Inversion With Positive Number
# =============================================================================

number = 5

result = ~number

print(result)


# =============================================================================
# 31. Bitwise Inversion With Negative Number
# =============================================================================

number = -5

result = ~number

print(result)


# =============================================================================
# 32. Bitwise Inversion Formula
# =============================================================================

number = 10

result = ~number

expected: int = -(number + 1)

print(result)
print(expected)


# =============================================================================
# 33. Bitwise Inversion Twice
# =============================================================================

number = 10

result = ~~number

print(result)


# =============================================================================
# 34. Bitwise Inversion Of a Negative Number Twice
# =============================================================================

number = -10

result = ~~number

print(result)


# =============================================================================
# 35. Unary Minus In an Arithmetic Expression
# =============================================================================

price: float = 100.0

discount: float = -20.0

final_price: float = price + discount

print(final_price)


# =============================================================================
# 36. Unary Plus In an Arithmetic Expression
# =============================================================================

first_value: int = 10
second_value: int = 20

result: int = +first_value + +second_value

print(result)


# =============================================================================
# 37. Unary Minus Before Parentheses
# =============================================================================

first_number: int = 10
second_number: int = 5

result: int = -(first_number + second_number)

print(result)


# =============================================================================
# 38. Unary Minus and Operator Precedence
# =============================================================================

number = 5

result: int = -number**2

print(result)

# Exponentiation has higher precedence than unary minus.

# Therefore:
#
#     -number**2
#
# is interpreted as:
#
#     -(number**2)


# =============================================================================
# 39. Parentheses Change Unary Minus Evaluation
# =============================================================================

number = 5

result = (-number) ** 2

print(result)


# =============================================================================
# 40. Unary Minus With an Expression
# =============================================================================

first_number = 10
second_number = 3

result = -(first_number - second_number)

print(result)


# =============================================================================
# 41. Unary Plus With an Expression
# =============================================================================

first_number = 10
second_number = 3

result = +(first_number - second_number)

print(result)


# =============================================================================
# 42. Combining `not` With Comparison
# =============================================================================

age: int = 20

is_minor: bool = not age >= 18

print(is_minor)


# =============================================================================
# 43. Parentheses With `not`
# =============================================================================

age = 20

is_minor = not (age >= 18)

print(is_minor)


# =============================================================================
# 44. `not` With Membership
# =============================================================================

language: str = "Python"
languages: list[str] = ["Python", "SQL", "Go"]

not_found: bool = language not in languages

print(not_found)


# =============================================================================
# 45. `not` With Identity
# =============================================================================

value: str | None = "Python"

is_missing: bool = not (value is None)

print(is_missing)


# =============================================================================
# 46. Unary Operators In a Function
# =============================================================================

def negate(
    value: int,
) -> int:
    """Return the negative form of an integer."""
    return -value


negative_result: int = negate(25)

print(negative_result)


# =============================================================================
# 47. Unary Plus In a Function
# =============================================================================

def make_positive(
    value: int,
) -> int:
    """Apply unary plus to an integer."""
    return +value


positive_result: int = make_positive(-25)

print(positive_result)


# =============================================================================
# 48. Logical Negation In a Function
# =============================================================================

def invert_boolean(
    value: bool,
) -> bool:
    """Return the logical opposite of a boolean value."""
    return not value


print(invert_boolean(True))
print(invert_boolean(False))


# =============================================================================
# 49. Bitwise Inversion In a Function
# =============================================================================

def invert_bits(
    value: int,
) -> int:
    """Apply bitwise inversion to an integer."""
    return ~value


inverted_value: int = invert_bits(10)

print(inverted_value)


# =============================================================================
# 50. Practical Unary Operator Example
# =============================================================================

def describe_number(
    value: int,
) -> None:
    """Demonstrate unary plus, minus, and bitwise inversion."""
    positive: int = +value
    negative: int = -value
    inverted: int = ~value

    print(f"Original: {value}")
    print(f"Unary plus: {positive}")
    print(f"Unary minus: {negative}")
    print(f"Bitwise inversion: {inverted}")


describe_number(10)


# =============================================================================
# Unary Operators Summary
# =============================================================================
"""
Python's primary unary operators are:

    +value
        Unary plus.

    -value
        Unary minus.

    ~value
        Bitwise inversion.

    not value
        Logical negation.

Unary plus:

    +10
        10

    +-10
        -10

Unary minus:

    -10
        -10

    -(-10)
        10

Bitwise inversion:

    ~10
        -11

The mathematical relationship is:

    ~n == -(n + 1)

Logical negation:

    not True
        False

    not False
        True

`not` works with truthiness:

    not 0
        True

    not 1
        False

    not ""
        True

    not "Python"
        False

    not []
        True

    not [1, 2, 3]
        False

Important distinction:

    Unary operators
        Work with one operand.

    Binary operators
        Work with two operands.

Examples:

    -number
        Unary minus.

    number - 5
        Binary subtraction.

    +number
        Unary plus.

    number + 5
        Binary addition.

    ~number
        Unary bitwise inversion.

    not value
        Unary logical negation.

Important precedence rule:

    -number**2

means:

    -(number**2)

while:

    (-number)**2

means:

    (-number) ** 2

Use parentheses when the intended evaluation order should be explicit.

Core model:

    +value
        positive form

    -value
        negative form

    ~value
        bitwise inversion

    not value
        logical negation

Practical guidance:

    Use + and - for numeric sign operations.

    Use ~ for bit-level integer manipulation.

    Use not for logical negation.

    Use parentheses when combining unary operators with expressions where
    precedence may not be immediately obvious.
"""

# =============================================================================
# Key Takeaways
# =============================================================================
"""
✓ Unary operators operate on one operand.

✓ Unary plus is written as +value.

✓ Unary minus is written as -value.

✓ Unary plus generally preserves the numeric sign.

✓ Unary minus reverses the numeric sign.

✓ `not` performs logical negation.

✓ `not` operates according to Python truthiness rules.

✓ `~` performs bitwise inversion on integers.

✓ For integers:

      ~value == -(value + 1)

✓ Unary minus has an important precedence relationship with exponentiation.

✓ `-value**2` means:

      -(value**2)

✓ `(-value)**2` means:

      (-value)**2

✓ Unary operators can be used inside expressions.

✓ Unary operators can be returned from functions.

✓ Unary operators can be combined with other operators.

Core idea:

    ONE OPERAND
         |
         v
    UNARY OPERATOR
         |
         v
    RESULT

Examples:

    +10
    -10
    ~10
    not True
"""

# =============================================================================
# End of 09_unary_operators.py
# =============================================================================