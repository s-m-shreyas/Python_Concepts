# =============================================================================
# 03. Assignment Operators
# =============================================================================
# type: ignore

"""
Python Operators

File:
    03_assignment_operators.py

Topic:
    Assignment Operators

Overview:
    Assignment operators are used to assign values to variables.

    The basic assignment operator is:

        =

    Python also provides augmented assignment operators:

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

    Assignment expressions can also be used with:

        :=

    This file contains 50 distinct examples covering the most important
    assignment-operator patterns in Python.
"""

# =============================================================================
# 01. Basic Assignment
# =============================================================================

number: int = 10

print(number)


# =============================================================================
# 02. Assigning a String
# =============================================================================

name: str = "Python"

print(name)


# =============================================================================
# 03. Assigning a Float
# =============================================================================

price: float = 99.99

print(price)


# =============================================================================
# 04. Assigning a Boolean
# =============================================================================

is_active: bool = True

print(is_active)


# =============================================================================
# 05. Assigning None
# =============================================================================

result: None = None

print(result)


# =============================================================================
# 06. Multiple Assignment
# =============================================================================

first_number: int
second_number: int

first_number, second_number = 10, 20

print(first_number)
print(second_number)


# =============================================================================
# 07. Assigning the Same Value to Multiple Variables
# =============================================================================

x: int
y: int
z: int

x = y = z = 100

print(x)
print(y)
print(z)


# =============================================================================
# 08. Swapping Two Variables
# =============================================================================

left: int = 10
right: int = 20

left, right = right, left

print(left)
print(right)


# =============================================================================
# 09. += Addition Assignment
# =============================================================================

score: int = 100

score += 25

print(score)


# =============================================================================
# 10. += With a Negative Value
# =============================================================================

balance: int = 500

balance += -100

print(balance)


# =============================================================================
# 11. += With Strings
# =============================================================================

message: str = "Hello"

message += " Python"

print(message)


# =============================================================================
# 12. += With Lists
# =============================================================================

numbers: list[int] = [1, 2, 3]

numbers += [4, 5]

print(numbers)


# =============================================================================
# 13. -= Subtraction Assignment
# =============================================================================

points: int = 100

points -= 30

print(points)


# =============================================================================
# 14. -= With Floats
# =============================================================================

temperature: float = 35.5

temperature -= 2.5

print(temperature)


# =============================================================================
# 15. *= Multiplication Assignment
# =============================================================================

quantity: int = 5

quantity *= 4

print(quantity)


# =============================================================================
# 16. *= With Strings
# =============================================================================

separator: str = "-"

separator *= 10

print(separator)


# =============================================================================
# 17. *= With Lists
# =============================================================================

items: list[str] = ["Python"]

items *= 3

print(items)


# =============================================================================
# 18. /= Division Assignment
# =============================================================================

total: float = 100.0

total /= 4

print(total)


# =============================================================================
# 19. /= Produces a Float
# =============================================================================

number_value: int = 20

number_value /= 2

print(number_value)
print(type(number_value).__name__)


# =============================================================================
# 20. //= Floor Division Assignment
# =============================================================================

total_items: int = 17

total_items //= 5

print(total_items)


# =============================================================================
# 21. //= With Negative Numbers
# =============================================================================

negative_number: int = -17

negative_number //= 5

print(negative_number)


# =============================================================================
# 22. %= Modulo Assignment
# =============================================================================

remaining: int = 17

remaining %= 5

print(remaining)


# =============================================================================
# 23. %= For Even and Odd Detection
# =============================================================================

number_to_check: int = 42

number_to_check %= 2

print(number_to_check)


# =============================================================================
# 24. **= Exponentiation Assignment
# =============================================================================

base: int = 5

base **= 2

print(base)


# =============================================================================
# 25. **= With Floating-Point Values
# =============================================================================

value: float = 2.5

value **= 2

print(value)


# =============================================================================
# 26. &= Bitwise AND Assignment
# =============================================================================

bitwise_and_value: int = 12

bitwise_and_value &= 10

print(bitwise_and_value)


# =============================================================================
# 27. |= Bitwise OR Assignment
# =============================================================================

bitwise_or_value: int = 12

bitwise_or_value |= 10

print(bitwise_or_value)


# =============================================================================
# 28. ^= Bitwise XOR Assignment
# =============================================================================

bitwise_xor_value: int = 12

bitwise_xor_value ^= 10

print(bitwise_xor_value)


# =============================================================================
# 29. <<= Left Shift Assignment
# =============================================================================

left_shift_value: int = 5

left_shift_value <<= 2

print(left_shift_value)


# =============================================================================
# 30. >>= Right Shift Assignment
# =============================================================================

right_shift_value: int = 20

right_shift_value >>= 2

print(right_shift_value)


# =============================================================================
# 31. Assignment With an Expression
# =============================================================================

width: int = 10
height: int = 5

area: int = width * height

print(area)


# =============================================================================
# 32. Augmented Assignment With an Expression
# =============================================================================

total_price: float = 100.0

tax: float = 18.0

total_price += tax

print(total_price)


# =============================================================================
# 33. Assignment Inside a Loop
# =============================================================================

running_total: int = 0

for value in range(1, 6):
    running_total += value

print(running_total)


# =============================================================================
# 34. Assignment Inside a Conditional
# =============================================================================

status: str = "inactive"

is_enabled: bool = True

if is_enabled:
    status = "active"

print(status)


# =============================================================================
# 35. Assignment in a Function
# =============================================================================

def calculate_total(price: float, quantity: int) -> float:
    """Calculate a total price."""
    total: float = price * quantity

    return total


function_total: float = calculate_total(
    25.0,
    4,
)

print(function_total)


# =============================================================================
# 36. Augmented Assignment in a Function
# =============================================================================

def add_points(initial_score: int, points: int) -> int:
    """Add points to a local score."""
    score: int = initial_score

    score += points

    return score


updated_score: int = add_points(
    100,
    25,
)

print(updated_score)


# =============================================================================
# 37. Assignment to a List Element
# =============================================================================

values: list[int] = [10, 20, 30]

values[1] = 200

print(values)


# =============================================================================
# 38. Augmented Assignment to a List Element
# =============================================================================

scores: list[int] = [10, 20, 30]

scores[0] += 5

print(scores)


# =============================================================================
# 39. Assignment to a Dictionary Value
# =============================================================================

user: dict[str, object] = {
    "name": "Alex",
    "age": 25,
}

user["age"] = 26

print(user)


# =============================================================================
# 40. Augmented Assignment to a Dictionary Value
# =============================================================================

inventory: dict[str, int] = {
    "books": 10,
}

inventory["books"] += 5

print(inventory)


# =============================================================================
# 41. Assignment to an Object Attribute
# =============================================================================

class Product:
    """Represent a simple product."""

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price


product: Product = Product(
    "Keyboard",
    50.0,
)

product.price = 45.0

print(product.price)


# =============================================================================
# 42. Augmented Assignment to an Object Attribute
# =============================================================================

product.price += 5.0

print(product.price)


# =============================================================================
# 43. Assignment Expression With :=
# =============================================================================

text: str = "Python"

if (length := len(text)) > 5:
    print(length)


# =============================================================================
# 44. Assignment Expression in a While Loop
# =============================================================================

values_to_process: list[int] = [10, 20, 30]

index: int = 0

while index < len(values_to_process):
    current_value: int = values_to_process[index]

    print(current_value)

    index += 1


# =============================================================================
# 45. Assignment Expression With a Function Call
# =============================================================================

def get_message() -> str:
    """Return a message."""
    return "Hello from Python"


if (message_value := get_message()):
    print(message_value)


# =============================================================================
# 46. Chained Augmented Assignments Are Separate Operations
# =============================================================================

first: int = 10
second: int = 20

first += 5
second += 5

print(first)
print(second)


# =============================================================================
# 47. Assignment to a Tuple
# =============================================================================

coordinates: tuple[int, int] = (10, 20)

x_coordinate: int
y_coordinate: int

x_coordinate, y_coordinate = coordinates

print(x_coordinate)
print(y_coordinate)


# =============================================================================
# 48. Extended Iterable Unpacking Assignment
# =============================================================================

numbers_to_unpack: list[int] = [1, 2, 3, 4, 5]

first_item: int
middle_items: list[int]
last_item: int

first_item, *middle_items, last_item = numbers_to_unpack

print(first_item)
print(middle_items)
print(last_item)


# =============================================================================
# 49. Assignment and Mutable Object Aliasing
# =============================================================================

original_numbers: list[int] = [1, 2, 3]

aliased_numbers: list[int] = original_numbers

aliased_numbers += [4]

print(original_numbers)
print(aliased_numbers)


# =============================================================================
# 50. Assignment Operators in a Practical Example
# =============================================================================

def calculate_invoice(
    price: float,
    quantity: int,
    discount_percentage: float,
    tax_percentage: float,
) -> float:
    """Calculate an invoice using assignment operators."""
    subtotal: float = price * quantity

    discount: float = subtotal * discount_percentage / 100

    subtotal -= discount

    tax: float = subtotal * tax_percentage / 100

    subtotal += tax

    return subtotal


invoice_total: float = calculate_invoice(
    price=1000.0,
    quantity=2,
    discount_percentage=10.0,
    tax_percentage=18.0,
)

print(invoice_total)


# =============================================================================
# Assignment Operators Summary
# =============================================================================
"""
Basic assignment:

    =

Arithmetic assignment:

    +=
    -=
    *=
    /=
    //=
    %=
    **=

Bitwise assignment:

    &=
    |=
    ^=
    <<=
    >>=

Assignment expression:

    :=

Core idea:

    variable = value

    variable += value
    variable -= value
    variable *= value
    variable /= value

Augmented assignment is generally equivalent in meaning to:

    x += y

being conceptually similar to:

    x = x + y

The augmented form performs the operation and updates the binding in
one expression.

Important distinction:

    =

creates or replaces a binding.

For example:

    value = 10

while:

    value += 5

updates the existing value using an augmented assignment operation.

Assignment can also target:

    - Variables
    - Multiple variables
    - Tuple-unpacking targets
    - List elements
    - Dictionary values
    - Object attributes

The assignment expression:

    :=

allows a value to be assigned while an expression is being evaluated.

Example:

    if (length := len("Python")) > 5:
        print(length)

Remember:

    =

is assignment.

    ==

is comparison.

    :=

is an assignment expression.
"""

# =============================================================================
# End of 03_assignment_operators.py
# =============================================================================