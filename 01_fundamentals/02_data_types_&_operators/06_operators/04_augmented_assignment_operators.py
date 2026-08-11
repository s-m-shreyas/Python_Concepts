# =============================================================================
# 04. Augmented Assignment Operators
# =============================================================================
# type: ignore

"""
Python Operators

File:
    04_augmented_assignment_operators.py

Topic:
    Augmented Assignment Operators

Overview:
    Augmented assignment operators combine an operation with assignment.

    Instead of writing:

        value = value + 10

    we can write:

        value += 10

    Python provides augmented assignment operators for arithmetic,
    bitwise, and other supported operations.

    Operators covered in this file:

        +=
        -=
        *=
        /=
        //=
        %=
        **=
        &=
        |=
        ^=
        <<=
        >>=

    This file contains 50 distinct examples demonstrating practical and
    important uses of augmented assignment operators.
"""

# =============================================================================
# 01. Basic +=
# =============================================================================

number: int = 10

number += 5

print(number)


# =============================================================================
# 02. += With a Negative Number
# =============================================================================

balance: int = 100

balance += -25

print(balance)


# =============================================================================
# 03. += With Multiple Operations
# =============================================================================

score: int = 50

score += 10
score += 20
score += 15

print(score)


# =============================================================================
# 04. += With Floating-Point Numbers
# =============================================================================

price: float = 100.0

price += 25.5

print(price)


# =============================================================================
# 05. += With Strings
# =============================================================================

message: str = "Hello"

message += " Python"

print(message)


# =============================================================================
# 06. += With Multiple Strings
# =============================================================================

sentence: str = "Python"

sentence += " is"
sentence += " powerful"

print(sentence)


# =============================================================================
# 07. += With Lists
# =============================================================================

numbers: list[int] = [1, 2, 3]

numbers += [4, 5]

print(numbers)


# =============================================================================
# 08. += With Tuples
# =============================================================================

values: tuple[int, ...] = (1, 2)

values += (3, 4)

print(values)


# =============================================================================
# 09. += With Sets
# =============================================================================

languages: set[str] = {"Python", "Java"}

languages |= {"Go", "Rust"}

print(languages)


# =============================================================================
# 10. -= Basic Subtraction Assignment
# =============================================================================

points: int = 100

points -= 30

print(points)


# =============================================================================
# 11. -= With Multiple Operations
# =============================================================================

remaining: int = 500

remaining -= 50
remaining -= 75
remaining -= 25

print(remaining)


# =============================================================================
# 12. -= With Floating-Point Numbers
# =============================================================================

temperature: float = 35.5

temperature -= 2.5

print(temperature)


# =============================================================================
# 13. *= Basic Multiplication Assignment
# =============================================================================

quantity: int = 5

quantity *= 4

print(quantity)


# =============================================================================
# 14. *= With a Float
# =============================================================================

amount: float = 100.0

amount *= 1.18

print(amount)


# =============================================================================
# 15. *= With a String
# =============================================================================

separator: str = "-"

separator *= 10

print(separator)


# =============================================================================
# 16. *= With a List
# =============================================================================

items: list[str] = ["Python"]

items *= 3

print(items)


# =============================================================================
# 17. /= Basic Division Assignment
# =============================================================================

total: float = 100.0

total /= 4

print(total)


# =============================================================================
# 18. /= Multiple Times
# =============================================================================

value: float = 1000.0

value /= 10
value /= 2

print(value)


# =============================================================================
# 19. /= Produces a Float
# =============================================================================

integer_value: int = 20

integer_value /= 2

print(integer_value)
print(type(integer_value).__name__)


# =============================================================================
# 20. //= Basic Floor Division Assignment
# =============================================================================

items_to_distribute: int = 17

items_to_distribute //= 5

print(items_to_distribute)


# =============================================================================
# 21. //= With a Negative Number
# =============================================================================

negative_value: int = -17

negative_value //= 5

print(negative_value)


# =============================================================================
# 22. //= Multiple Times
# =============================================================================

large_number: int = 1000

large_number //= 10
large_number //= 5

print(large_number)


# =============================================================================
# 23. %= Basic Modulo Assignment
# =============================================================================

remainder: int = 17

remainder %= 5

print(remainder)


# =============================================================================
# 24. %= For Even and Odd Checking
# =============================================================================

number_to_check: int = 42

number_to_check %= 2

print(number_to_check)


# =============================================================================
# 25. %= Multiple Times
# =============================================================================

value_modulo: int = 100

value_modulo %= 30
value_modulo %= 7

print(value_modulo)


# =============================================================================
# 26. **= Basic Exponentiation Assignment
# =============================================================================

base: int = 5

base **= 2

print(base)


# =============================================================================
# 27. **= With a Floating-Point Number
# =============================================================================

decimal_base: float = 2.5

decimal_base **= 2

print(decimal_base)


# =============================================================================
# 28. **= Multiple Times
# =============================================================================

power_value: int = 2

power_value **= 3

print(power_value)


# =============================================================================
# 29. &= Bitwise AND Assignment
# =============================================================================

and_value: int = 12

and_value &= 10

print(and_value)


# =============================================================================
# 30. &= With Binary Values
# =============================================================================

binary_and: int = 0b1100

binary_and &= 0b1010

print(bin(binary_and))


# =============================================================================
# 31. |= Bitwise OR Assignment
# =============================================================================

or_value: int = 12

or_value |= 10

print(or_value)


# =============================================================================
# 32. |= With Binary Values
# =============================================================================

binary_or: int = 0b1100

binary_or |= 0b0011

print(bin(binary_or))


# =============================================================================
# 33. ^= Bitwise XOR Assignment
# =============================================================================

xor_value: int = 12

xor_value ^= 10

print(xor_value)


# =============================================================================
# 34. ^= For Toggling Bits
# =============================================================================

toggle_value: int = 0b1010

toggle_value ^= 0b0011

print(bin(toggle_value))


# =============================================================================
# 35. <<= Basic Left Shift Assignment
# =============================================================================

left_shift: int = 5

left_shift <<= 2

print(left_shift)


# =============================================================================
# 36. <<= Multiple Times
# =============================================================================

shifted_value: int = 1

shifted_value <<= 3
shifted_value <<= 1

print(shifted_value)


# =============================================================================
# 37. >>= Basic Right Shift Assignment
# =============================================================================

right_shift: int = 20

right_shift >>= 2

print(right_shift)


# =============================================================================
# 38. >>= Multiple Times
# =============================================================================

shifted_number: int = 128

shifted_number >>= 2
shifted_number >>= 2

print(shifted_number)


# =============================================================================
# 39. += Inside a for Loop
# =============================================================================

running_total: int = 0

for value in range(1, 6):
    running_total += value

print(running_total)


# =============================================================================
# 40. *= Inside a for Loop
# =============================================================================

factorial_value: int = 1

for value in range(1, 6):
    factorial_value *= value

print(factorial_value)


# =============================================================================
# 41. += With Function Results
# =============================================================================

def get_points() -> int:
    """Return a number of points."""
    return 25


total_points: int = 50

total_points += get_points()

print(total_points)


# =============================================================================
# 42. -= With Function Results
# =============================================================================

def get_discount() -> float:
    """Return a discount amount."""
    return 15.0


original_price: float = 100.0

original_price -= get_discount()

print(original_price)


# =============================================================================
# 43. Augmented Assignment With List Elements
# =============================================================================

scores: list[int] = [10, 20, 30]

scores[0] += 5
scores[1] += 10

print(scores)


# =============================================================================
# 44. Augmented Assignment With Dictionary Values
# =============================================================================

inventory: dict[str, int] = {
    "books": 10,
    "pens": 20,
}

inventory["books"] += 5
inventory["pens"] -= 3

print(inventory)


# =============================================================================
# 45. Augmented Assignment With Object Attributes
# =============================================================================

class Account:
    """Represent a simple account."""

    def __init__(self, balance: float) -> None:
        self.balance: float = balance


account: Account = Account(1000.0)

account.balance += 250.0
account.balance -= 100.0

print(account.balance)


# =============================================================================
# 46. Practical Shopping Cart Total
# =============================================================================

cart_total: float = 0.0

cart_total += 25.0
cart_total += 50.0
cart_total += 15.0

print(cart_total)


# =============================================================================
# 47. Practical Counter
# =============================================================================

counter: int = 0

counter += 1
counter += 1
counter += 1

print(counter)


# =============================================================================
# 48. Practical Percentage Calculation
# =============================================================================

salary: float = 50000.0

salary *= 1.10

print(salary)


# =============================================================================
# 49. Practical Bit Flags
# =============================================================================

READ_PERMISSION: int = 0b001
WRITE_PERMISSION: int = 0b010
EXECUTE_PERMISSION: int = 0b100

permissions: int = 0

permissions |= READ_PERMISSION
permissions |= WRITE_PERMISSION

print(bin(permissions))

permissions ^= WRITE_PERMISSION

print(bin(permissions))


# =============================================================================
# 50. Practical Invoice Calculation
# =============================================================================

def calculate_invoice(
    price: float,
    quantity: int,
    discount_percentage: float,
    tax_percentage: float,
) -> float:
    """Calculate an invoice using augmented assignment operators."""
    total: float = price * quantity

    discount: float = total * discount_percentage / 100
    total -= discount

    tax: float = total * tax_percentage / 100
    total += tax

    return total


invoice_total: float = calculate_invoice(
    price=1000.0,
    quantity=2,
    discount_percentage=10.0,
    tax_percentage=18.0,
)

print(invoice_total)


# =============================================================================
# Augmented Assignment Operator Summary
# =============================================================================
"""
Arithmetic augmented assignment operators:

    +=
        Addition assignment.

        value += amount

        Equivalent in basic meaning to:

        value = value + amount


    -=
        Subtraction assignment.

        value -= amount

        Equivalent in basic meaning to:

        value = value - amount


    *=
        Multiplication assignment.

        value *= amount

        Equivalent in basic meaning to:

        value = value * amount


    /=
        Division assignment.

        value /= amount

        Equivalent in basic meaning to:

        value = value / amount


    //=
        Floor division assignment.

        value //= amount

        Equivalent in basic meaning to:

        value = value // amount


    %=
        Modulo assignment.

        value %= amount

        Equivalent in basic meaning to:

        value = value % amount


    **=
        Exponentiation assignment.

        value **= exponent

        Equivalent in basic meaning to:

        value = value ** exponent


Bitwise augmented assignment operators:

    &=
        Bitwise AND assignment.


    |=
        Bitwise OR assignment.


    ^=
        Bitwise XOR assignment.


    <<=
        Left-shift assignment.


    >>=
        Right-shift assignment.


Important idea:

    x += y

updates the variable using the result of:

    x + y


Similarly:

    x -= y
    x *= y
    x /= y
    x //= y
    x %= y
    x **= y

perform their respective operation and assign the result back.

Augmented assignment is especially useful for:

    - Counters
    - Running totals
    - Accumulators
    - Scores
    - Quantities
    - Mathematical calculations
    - String building
    - List extension
    - Bit manipulation
    - Object attributes
    - Dictionary values
    - Loop calculations

Important distinction:

    =

is normal assignment.

    +=
    -=
    *=
    /=
    //=
    %=
    **=
    &=
    |=
    ^=
    <<=
    >>=

are augmented assignment operators.

Augmented assignment does not mean that the operation is always identical
to manually writing the expanded expression at the implementation level.

For mutable objects, Python can use the object's in-place operation when
supported.

For example:

    numbers += [4, 5]

can modify the existing list object.

By contrast, immutable objects such as integers and strings require a new
value to be produced and the variable name to be rebound.

Core model:

    VARIABLE
        ↓
    AUGMENTED OPERATION
        ↓
    UPDATED VALUE

Examples:

    counter += 1

    price -= discount

    quantity *= multiplier

    total /= divisor

    items //= batch_size

    remainder %= divisor

    value **= exponent

    flags |= permission

    flags &= mask

    flags ^= permission

    value <<= positions

    value >>= positions
"""

# =============================================================================
# End of 04_augmented_assignment_operators.py
# =============================================================================