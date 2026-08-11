# type: ignore
# =============================================================================
# 19. In-Place Operators
# =============================================================================
"""
Python Operators

File:
19_inplace_operators.py

Topic:
In-Place Operators

Overview:
In-place operators update an existing variable using an operator and
assignment together.

Common in-place operators:

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

Examples:

    x += 5

is conceptually similar to:

    x = x + 5

However, for mutable objects such as lists, in-place operations can
often modify the existing object instead of creating a completely
new object.

Topics covered:

    - What are in-place operators?
    - +=
    - -=
    - *=
    - /=
    - //=
    - %=
    - **=
    - &=
    - |=
    - ^=
    - <<=
    - >>=
    - In-place operators with integers
    - In-place operators with floats
    - In-place operators with strings
    - In-place operators with lists
    - In-place operators with dictionaries
    - In-place operators with sets
    - Mutation versus rebinding
    - Object identity
    - Mutable objects
    - Immutable objects
    - Function parameters
    - Practical examples
"""

# =============================================================================
# 01. Basic +=
# =============================================================================

value: int = 10

value += 5

print(value)


# =============================================================================
# 02. Basic -=
# =============================================================================

value = 20

value -= 5

print(value)


# =============================================================================
# 03. Basic *=
# =============================================================================

value = 10

value *= 3

print(value)


# =============================================================================
# 04. Basic /=
# =============================================================================

value = 20.0

value /= 4

print(value)


# =============================================================================
# 05. Basic //=
# =============================================================================

value = 17

value //= 5

print(value)


# =============================================================================
# 06. Basic %=
# =============================================================================

value = 17

value %= 5

print(value)


# =============================================================================
# 07. Basic **=
# =============================================================================

value = 2

value **= 4

print(value)


# =============================================================================
# 08. Basic &=
# =============================================================================

value = 12

value &= 10

print(value)


# =============================================================================
# 09. Basic |=
# =============================================================================

value = 12

value |= 10

print(value)


# =============================================================================
# 10. Basic ^=
# =============================================================================

value = 12

value ^= 10

print(value)


# =============================================================================
# 11. Basic <<=
# =============================================================================

value = 3

value <<= 2

print(value)


# =============================================================================
# 12. Basic >>=
# =============================================================================

value = 20

value >>= 2

print(value)


# =============================================================================
# 13. += With Multiple Operations
# =============================================================================

total: int = 100

total += 25
total += 50
total += 75

print(total)


# =============================================================================
# 14. -= With Multiple Operations
# =============================================================================

balance: int = 1000

balance -= 100
balance -= 250
balance -= 50

print(balance)


# =============================================================================
# 15. *= With a Float
# =============================================================================

price: float = 100.0

price *= 1.18

print(price)


# =============================================================================
# 16. /= With a Float
# =============================================================================

temperature: float = 100.0

temperature /= 2

print(temperature)


# =============================================================================
# 17. //= For Integer Division
# =============================================================================

items: int = 23

items //= 5

print(items)


# =============================================================================
# 18. %= For Remainder
# =============================================================================

remaining_items: int = 23

remaining_items %= 5

print(remaining_items)


# =============================================================================
# 19. **= For Powers
# =============================================================================

number: int = 3

number **= 3

print(number)


# =============================================================================
# 20. += With Strings
# =============================================================================

message: str = "Hello"

message += ", Python"

message += "!"

print(message)


# =============================================================================
# 21. *= With Strings
# =============================================================================

separator: str = "-"

separator *= 20

print(separator)


# =============================================================================
# 22. += With Lists
# =============================================================================

numbers: list[int] = [1, 2, 3]

numbers += [4, 5, 6]

print(numbers)


# =============================================================================
# 23. *= With Lists
# =============================================================================

values: list[int] = [1, 2]

values *= 3

print(values)


# =============================================================================
# 24. += With Sets
# =============================================================================

languages: set[str] = {"Python", "Java"}

languages |= {"Go", "Rust"}

print(languages)


# =============================================================================
# 25. &= With Sets
# =============================================================================

available_languages: set[str] = {
    "Python",
    "Java",
    "Go",
}

supported_languages: set[str] = {
    "Python",
    "Go",
    "Rust",
}

available_languages &= supported_languages

print(available_languages)


# =============================================================================
# 26. |= With Sets
# =============================================================================

frontend_languages: set[str] = {
    "JavaScript",
    "TypeScript",
}

backend_languages: set[str] = {
    "Python",
    "Go",
}

frontend_languages |= backend_languages

print(frontend_languages)


# =============================================================================
# 27. -= With Sets
# =============================================================================

all_languages: set[str] = {
    "Python",
    "Java",
    "Go",
    "Rust",
}

unwanted_languages: set[str] = {
    "Java",
    "Rust",
}

all_languages -= unwanted_languages

print(all_languages)


# =============================================================================
# 28. ^= With Sets
# =============================================================================

first_set: set[int] = {
    1,
    2,
    3,
}

second_set: set[int] = {
    3,
    4,
    5,
}

first_set ^= second_set

print(first_set)


# =============================================================================
# 29. In-Place Addition Versus Normal Addition
# =============================================================================

first_value: int = 10

first_value += 5

second_value: int = 10

second_value = second_value + 5

print(first_value)
print(second_value)


# =============================================================================
# 30. In-Place Subtraction Versus Normal Subtraction
# =============================================================================

first_value = 20

first_value -= 5

second_value = 20

second_value = second_value - 5

print(first_value)
print(second_value)


# =============================================================================
# 31. In-Place Multiplication Versus Normal Multiplication
# =============================================================================

first_value = 10

first_value *= 3

second_value = 10

second_value = second_value * 3

print(first_value)
print(second_value)


# =============================================================================
# 32. In-Place Operators With Function Parameters
# =============================================================================

def increase_value(
    value: int,
) -> int:
    """
    Increase a local integer value.
    """
    value += 10

    return value


original_value: int = 50

updated_value: int = increase_value(
    original_value,
)

print(original_value)
print(updated_value)


# =============================================================================
# 33. += With a Mutable List Parameter
# =============================================================================

def add_values(
    values: list[int],
) -> None:
    """
    Add values to a list using +=.
    """
    values += [4, 5]


numbers = [1, 2, 3]

add_values(
    numbers,
)

print(numbers)


# =============================================================================
# 34. append() Versus +=
# =============================================================================

first_list: list[int] = [1, 2]

first_list.append(3)

second_list: list[int] = [1, 2]

second_list += [3]

print(first_list)
print(second_list)


# =============================================================================
# 35. List Identity With +=
# =============================================================================

numbers = [1, 2, 3]

original_identity: int = id(numbers)

numbers += [4, 5]

new_identity: int = id(numbers)

print(original_identity == new_identity)
print(numbers)


# =============================================================================
# 36. List Identity With Normal +
# =============================================================================

numbers = [1, 2, 3]

original_identity = id(numbers)

numbers = numbers + [4, 5]

new_identity = id(numbers)

print(original_identity == new_identity)
print(numbers)


# =============================================================================
# 37. += Can Mutate a Mutable Object
# =============================================================================

values = [10, 20]

alias: list[int] = values

values += [30]

print(values)
print(alias)


# =============================================================================
# 38. Normal + Can Create a New List
# =============================================================================

values = [10, 20]

alias = values

values = values + [30]

print(values)
print(alias)


# =============================================================================
# 39. String +=
# =============================================================================

text: str = "Python"

text += " is"

text += " powerful"

print(text)


# =============================================================================
# 40. String Identity Is Not Guaranteed To Remain The Same
# =============================================================================

text = "Hello"

original_identity = id(text)

text += " World"

new_identity = id(text)

print(original_identity == new_identity)
print(text)


# =============================================================================
# 41. Integer += Rebinds the Name
# =============================================================================

number = 10

alias_number: int = number

number += 5

print(number)
print(alias_number)


# =============================================================================
# 42. Float += Rebinds the Name
# =============================================================================

amount: float = 100.0

alias_amount: float = amount

amount += 50.0

print(amount)
print(alias_amount)


# =============================================================================
# 43. Dictionary |=
# =============================================================================

user: dict[str, str] = {
    "name": "Alex",
}

additional_data: dict[str, str] = {
    "language": "Python",
}

user |= additional_data

print(user)


# =============================================================================
# 44. Dictionary Update With |=
# =============================================================================

configuration: dict[str, str] = {
    "environment": "development",
    "debug": "false",
}

configuration |= {
    "debug": "true",
    "version": "1.0",
}

print(configuration)


# =============================================================================
# 45. Dictionary Key Replacement With |=
# =============================================================================

settings: dict[str, int] = {
    "timeout": 30,
    "retries": 3,
}

settings |= {
    "timeout": 60,
}

print(settings)


# =============================================================================
# 46. Bitwise In-Place Operations
# =============================================================================

flags: int = 0b1010

flags |= 0b0100

print(bin(flags))


# =============================================================================
# 47. Combining Multiple In-Place Operators
# =============================================================================

score: int = 100

score += 50
score *= 2
score -= 25
score //= 5

print(score)


# =============================================================================
# 48. In-Place Operators Inside a Loop
# =============================================================================

total = 0

for number in range(1, 6):
    total += number

print(total)


# =============================================================================
# 49. Building a String With +=
# =============================================================================

result: str = ""

for number in range(1, 6):
    result += str(number)

print(result)


# =============================================================================
# 50. Building a List With +=
# =============================================================================

result_list: list[int] = []

for number in range(1, 6):
    result_list += [number * 10]

print(result_list)


# =============================================================================
# 51. In-Place Operators With Object Attributes
# =============================================================================

class Counter:
    """
    Store a mutable counter value.
    """

    def __init__(
        self,
        value: int = 0,
    ) -> None:
        self.value: int = value

    def increment(
        self,
        amount: int,
    ) -> None:
        """
        Increase the counter using +=.
        """
        self.value += amount


counter = Counter()

counter.increment(10)
counter.increment(20)

print(counter.value)


# =============================================================================
# 52. In-Place Operators With Dictionary Values
# =============================================================================

inventory: dict[str, int] = {
    "apples": 10,
    "oranges": 5,
}

inventory["apples"] += 5
inventory["oranges"] -= 2

print(inventory)


# =============================================================================
# 53. In-Place Operators With List Elements
# =============================================================================

numbers = [10, 20, 30]

numbers[0] += 5
numbers[1] *= 2
numbers[2] -= 10

print(numbers)


# =============================================================================
# 54. In-Place Operators With Nested Lists
# =============================================================================

matrix: list[list[int]] = [
    [1, 2],
    [3, 4],
]

matrix[0][0] += 10
matrix[1][1] *= 2

print(matrix)


# =============================================================================
# 55. In-Place Operators With Boolean Values
# =============================================================================

enabled: bool = True

enabled &= False

print(enabled)


# =============================================================================
# 56. In-Place OR With Boolean Values
# =============================================================================

has_permission: bool = False

has_permission |= True

print(has_permission)


# =============================================================================
# 57. In-Place XOR With Boolean Values
# =============================================================================

is_active: bool = True

is_active ^= True

print(is_active)


# =============================================================================
# 58. In-Place Shift Operations
# =============================================================================

value = 1

value <<= 3

print(value)


# =============================================================================
# 59. Right Shift Operation
# =============================================================================

value = 32

value >>= 3

print(value)


# =============================================================================
# 60. Practical Example: Shopping Cart
# =============================================================================

cart_total: float = 0.0

cart_total += 120.0
cart_total += 250.0
cart_total += 80.0

discount: float = 50.0

cart_total -= discount

tax_rate: float = 0.18

tax: float = cart_total * tax_rate

cart_total += tax

print(cart_total)


# =============================================================================
# 61. Practical Example: Bank Balance
# =============================================================================

balance: float = 5000.0

balance += 1500.0
balance -= 750.0
balance -= 250.0

print(balance)


# =============================================================================
# 62. Practical Example: Score Calculation
# =============================================================================

score = 0

score += 100
score += 50
score -= 25
score *= 2

print(score)


# =============================================================================
# 63. Practical Example: Inventory
# =============================================================================

inventory_count: int = 100

inventory_count -= 20
inventory_count += 50
inventory_count -= 10

print(inventory_count)


# =============================================================================
# 64. Practical Example: Running Average
# =============================================================================

total_score: float = 0.0
score_count: int = 0

scores: list[float] = [
    80.0,
    90.0,
    70.0,
]

for score in scores:
    total_score += score
    score_count += 1

average_score: float = total_score / score_count

print(average_score)


# =============================================================================
# 65. Practical Example: Frequency Counter
# =============================================================================

frequency: dict[str, int] = {}

words: list[str] = [
    "python",
    "go",
    "python",
    "rust",
    "python",
]

for word in words:
    frequency[word] = frequency.get(word, 0)
    frequency[word] += 1

print(frequency)


# =============================================================================
# 66. Practical Example: Character Counter
# =============================================================================

character_count: dict[str, int] = {}

text = "banana"

for character in text:
    character_count[character] = character_count.get(
        character,
        0,
    )
    character_count[character] += 1

print(character_count)


# =============================================================================
# 67. Practical Example: Bit Flags
# =============================================================================

READ_PERMISSION: int = 1
WRITE_PERMISSION: int = 2
EXECUTE_PERMISSION: int = 4

permissions: int = 0

permissions |= READ_PERMISSION
permissions |= WRITE_PERMISSION

print(permissions)

permissions &= ~WRITE_PERMISSION

print(permissions)


# =============================================================================
# 68. Practical Example: Removing a Bit Flag
# =============================================================================

READ: int = 1
WRITE: int = 2
EXECUTE: int = 4

permissions = READ | WRITE | EXECUTE

permissions &= ~WRITE

print(permissions)


# =============================================================================
# 69. Practical Example: Toggle a Bit Flag
# =============================================================================

FEATURE_ENABLED: int = 1

features: int = 0

features ^= FEATURE_ENABLED

print(features)

features ^= FEATURE_ENABLED

print(features)


# =============================================================================
# 70. In-Place Operator Summary
# =============================================================================

"""
In-place operators combine an operation with assignment.

Examples:

    x += y
    x -= y
    x *= y
    x /= y
    x //= y
    x %= y
    x **= y
    x &= y
    x |= y
    x ^= y
    x <<= y
    x >>= y

They are useful for concise updates.

For immutable objects such as:

    int
    float
    str

the operation generally results in a new object being assigned to
the variable name.

For mutable objects such as:

    list
    set
    dict

an in-place operation may modify the existing object.

For example:

    values += [4, 5]

can modify the existing list.

Whereas:

    values = values + [4, 5]

creates a new list and rebinds the name.

The important distinction is:

    mutation
        ↓
    existing object changes

versus:

    rebinding
        ↓
    name refers to another object

In-place operators are therefore more than just shorter syntax.

Their behaviour depends on the type implementing the corresponding
in-place operation.

Core idea:

    variable
        ↓
    in-place operator
        ↓
    update existing value

Examples:

    total += amount
    balance -= payment
    count *= multiplier
    flags |= permission
    flags &= mask
    values += new_values

Remember:

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

are assignment operators that combine assignment with another
operation.

"""