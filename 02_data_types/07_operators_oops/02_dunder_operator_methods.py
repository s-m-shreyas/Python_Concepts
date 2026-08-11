# type: ignore
# =============================================================================
# 16. Dunder Operator Methods
# =============================================================================
"""
Python Operators

File
----
16_dunder_operator_methods.py

Topic
-----
Dunder Operator Methods

Overview
--------
Dunder methods are special methods whose names begin and end with double
underscores.

They allow custom classes to define how Python operators and built-in
operations behave.

Examples:

    __add__        +
    __sub__        -
    __mul__        *
    __truediv__    /
    __floordiv__   //
    __mod__        %
    __pow__        **
    __eq__         ==
    __ne__         !=
    __lt__         <
    __le__         <=
    __gt__         >
    __ge__         >=
    __neg__        -
    __pos__        +
    __abs__        abs()
    __bool__       bool()
    __len__        len()
    __getitem__    []
    __setitem__    [] =
    __contains__   in
    __call__       object()
    __str__        str()
    __repr__       repr()
    __iadd__       +=
    __isub__       -=
    __imul__       *=
    __itruediv__   /=
    __enter__      with
    __exit__       with

Dunder methods are also called:

    - Special methods
    - Magic methods

The purpose of this file is to demonstrate the most useful operator-related
dunder methods with practical examples.

All examples are designed to be valid Python and suitable for static
type checkers such as MyPy and Pylance.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Self


# =============================================================================
# 01. Basic __add__
# =============================================================================


class Number:
    """Represent a number with custom addition."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: Number) -> Number:
        return Number(self.value + other.value)


number_a: Number = Number(10)
number_b: Number = Number(20)

number_sum: Number = number_a + number_b

print(number_sum.value)


# =============================================================================
# 02. __sub__
# =============================================================================


class Score:
    """Represent a score with custom subtraction."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __sub__(self, other: Score) -> Score:
        return Score(self.value - other.value)


score_a: Score = Score(100)
score_b: Score = Score(30)

score_difference: Score = score_a - score_b

print(score_difference.value)


# =============================================================================
# 03. __mul__
# =============================================================================


class Quantity:
    """Represent a quantity that can be multiplied."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mul__(self, multiplier: int) -> Quantity:
        return Quantity(self.value * multiplier)


quantity: Quantity = Quantity(5)
multiplied_quantity: Quantity = quantity * 4

print(multiplied_quantity.value)


# =============================================================================
# 04. __truediv__
# =============================================================================


class Measurement:
    """Represent a measurement that supports true division."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __truediv__(self, divisor: float) -> Measurement:
        return Measurement(self.value / divisor)


measurement: Measurement = Measurement(100.0)
half_measurement: Measurement = measurement / 2.0

print(half_measurement.value)


# =============================================================================
# 05. __floordiv__
# =============================================================================


class Points:
    """Represent points that support floor division."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __floordiv__(self, divisor: int) -> Points:
        return Points(self.value // divisor)


points: Points = Points(17)
groups: Points = points // 5

print(groups.value)


# =============================================================================
# 06. __mod__
# =============================================================================


class Counter:
    """Represent a counter supporting modulo."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mod__(self, divisor: int) -> Counter:
        return Counter(self.value % divisor)


counter: Counter = Counter(17)
remainder: Counter = counter % 5

print(remainder.value)


# =============================================================================
# 07. __pow__
# =============================================================================


class BaseNumber:
    """Represent a number supporting exponentiation."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __pow__(self, exponent: int) -> BaseNumber:
        return BaseNumber(self.value**exponent)


base_number: BaseNumber = BaseNumber(2)
power_result: BaseNumber = base_number**3

print(power_result.value)


# =============================================================================
# 08. __neg__
# =============================================================================


class Temperature:
    """Represent a temperature supporting unary negation."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __neg__(self) -> Temperature:
        return Temperature(-self.value)


temperature: Temperature = Temperature(25.0)
negative_temperature: Temperature = -temperature

print(negative_temperature.value)


# =============================================================================
# 09. __pos__
# =============================================================================


class Amount:
    """Represent an amount supporting unary plus."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __pos__(self) -> Amount:
        return Amount(+self.value)


amount: Amount = Amount(150.0)
positive_amount: Amount = +amount

print(positive_amount.value)


# =============================================================================
# 10. __abs__
# =============================================================================


class Distance:
    """Represent a distance supporting abs()."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __abs__(self) -> float:
        return abs(self.value)


distance: Distance = Distance(-25.5)

print(abs(distance))


# =============================================================================
# 11. __eq__
# =============================================================================


class Product:
    """Represent a product with equality comparison."""

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.name == other.name and self.price == other.price


product_a: Product = Product("Keyboard", 50.0)
product_b: Product = Product("Keyboard", 50.0)

print(product_a == product_b)


# =============================================================================
# 12. __ne__
# =============================================================================


class User:
    """Represent a user with inequality comparison."""

    def __init__(self, user_id: int) -> None:
        self.user_id: int = user_id

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented

        return self.user_id != other.user_id


user_a: User = User(1)
user_b: User = User(2)

print(user_a != user_b)


# =============================================================================
# 13. __lt__
# =============================================================================


class Age:
    """Represent an age supporting less-than comparison."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __lt__(self, other: Age) -> bool:
        return self.value < other.value


age_a: Age = Age(20)
age_b: Age = Age(30)

print(age_a < age_b)


# =============================================================================
# 14. __le__
# =============================================================================


class Version:
    """Represent a version supporting less-than-or-equal comparison."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __le__(self, other: Version) -> bool:
        return self.value <= other.value


version_a: Version = Version(2)
version_b: Version = Version(2)

print(version_a <= version_b)


# =============================================================================
# 15. __gt__
# =============================================================================


class Priority:
    """Represent a priority supporting greater-than comparison."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __gt__(self, other: Priority) -> bool:
        return self.value > other.value


priority_a: Priority = Priority(10)
priority_b: Priority = Priority(5)

print(priority_a > priority_b)


# =============================================================================
# 16. __ge__
# =============================================================================


class Rating:
    """Represent a rating supporting greater-than-or-equal comparison."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __ge__(self, other: Rating) -> bool:
        return self.value >= other.value


rating_a: Rating = Rating(4.5)
rating_b: Rating = Rating(4.0)

print(rating_a >= rating_b)


# =============================================================================
# 17. __str__
# =============================================================================


class Book:
    """Represent a book with a custom string representation."""

    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


book: Book = Book("Python Basics", "Alex")

print(str(book))
print(book)


# =============================================================================
# 18. __repr__
# =============================================================================


class Coordinate:
    """Represent a coordinate with a useful developer representation."""

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __repr__(self) -> str:
        return f"Coordinate(x={self.x}, y={self.y})"


coordinate: Coordinate = Coordinate(10.0, 20.0)

print(repr(coordinate))


# =============================================================================
# 19. __len__
# =============================================================================


class Playlist:
    """Represent a playlist with a custom length."""

    def __init__(self, songs: list[str]) -> None:
        self.songs: list[str] = songs

    def __len__(self) -> int:
        return len(self.songs)


playlist: Playlist = Playlist(
    [
        "Song A",
        "Song B",
        "Song C",
    ]
)

print(len(playlist))


# =============================================================================
# 20. __bool__
# =============================================================================


class Cart:
    """Represent a cart whose truth value depends on its contents."""

    def __init__(self, items: list[str]) -> None:
        self.items: list[str] = items

    def __bool__(self) -> bool:
        return bool(self.items)


empty_cart: Cart = Cart([])
filled_cart: Cart = Cart(["Keyboard"])

print(bool(empty_cart))
print(bool(filled_cart))


# =============================================================================
# 21. __contains__
# =============================================================================


class Team:
    """Represent a team with membership testing."""

    def __init__(self, members: list[str]) -> None:
        self.members: list[str] = members

    def __contains__(self, member: str) -> bool:
        return member in self.members


team: Team = Team(
    [
        "Alice",
        "Bob",
        "Charlie",
    ]
)

print("Alice" in team)
print("David" in team)


# =============================================================================
# 22. __getitem__
# =============================================================================


class Scores:
    """Represent a collection supporting index access."""

    def __init__(self, values: list[int]) -> None:
        self.values: list[int] = values

    def __getitem__(self, index: int) -> int:
        return self.values[index]


scores: Scores = Scores(
    [
        90,
        85,
        95,
    ]
)

print(scores[0])
print(scores[2])


# =============================================================================
# 23. __setitem__
# =============================================================================


class Inventory:
    """Represent an inventory supporting item assignment."""

    def __init__(self, items: list[str]) -> None:
        self.items: list[str] = items

    def __getitem__(self, index: int) -> str:
        return self.items[index]

    def __setitem__(self, index: int, value: str) -> None:
        self.items[index] = value


inventory: Inventory = Inventory(
    [
        "Keyboard",
        "Mouse",
        "Monitor",
    ]
)

inventory[1] = "Wireless Mouse"

print(inventory[1])


# =============================================================================
# 24. __delitem__
# =============================================================================


class TaskList:
    """Represent tasks supporting deletion by index."""

    def __init__(self, tasks: list[str]) -> None:
        self.tasks: list[str] = tasks

    def __getitem__(self, index: int) -> str:
        return self.tasks[index]

    def __delitem__(self, index: int) -> None:
        del self.tasks[index]


tasks: TaskList = TaskList(
    [
        "Study",
        "Exercise",
        "Read",
    ]
)

del tasks[1]

print(tasks.tasks)


# =============================================================================
# 25. __call__
# =============================================================================


class Multiplier:
    """Represent an object that behaves like a function."""

    def __init__(self, factor: int) -> None:
        self.factor: int = factor

    def __call__(self, value: int) -> int:
        return value * self.factor


double: Multiplier = Multiplier(2)

print(double(10))
print(double(25))


# =============================================================================
# 26. __iadd__
# =============================================================================


class CounterValue:
    """Represent a mutable counter supporting +=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __iadd__(self, amount: int) -> Self:
        self.value += amount
        return self


counter_value: CounterValue = CounterValue(10)

counter_value += 5

print(counter_value.value)


# =============================================================================
# 27. __isub__
# =============================================================================


class Balance:
    """Represent a balance supporting -=."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __isub__(self, amount: float) -> Self:
        self.value -= amount
        return self


balance: Balance = Balance(1000.0)

balance -= 250.0

print(balance.value)


# =============================================================================
# 28. __imul__
# =============================================================================


class ScoreMultiplier:
    """Represent a score supporting *=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __imul__(self, multiplier: int) -> Self:
        self.value *= multiplier
        return self


score_multiplier: ScoreMultiplier = ScoreMultiplier(10)

score_multiplier *= 3

print(score_multiplier.value)


# =============================================================================
# 29. __itruediv__
# =============================================================================


class AmountValue:
    """Represent an amount supporting /=."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __itruediv__(self, divisor: float) -> Self:
        self.value /= divisor
        return self


amount_value: AmountValue = AmountValue(100.0)

amount_value /= 4.0

print(amount_value.value)


# =============================================================================
# 30. __ifloordiv__
# =============================================================================


class PageCount:
    """Represent a page count supporting //=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __ifloordiv__(self, divisor: int) -> Self:
        self.value //= divisor
        return self


page_count: PageCount = PageCount(25)

page_count //= 4

print(page_count.value)


# =============================================================================
# 31. __imod__
# =============================================================================


class RemainderValue:
    """Represent a value supporting %=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __imod__(self, divisor: int) -> Self:
        self.value %= divisor
        return self


remainder_value: RemainderValue = RemainderValue(27)

remainder_value %= 5

print(remainder_value.value)


# =============================================================================
# 32. __ipow__
# =============================================================================


class ExponentValue:
    """Represent a value supporting **=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __ipow__(self, exponent: int) -> Self:
        self.value **= exponent
        return self


exponent_value: ExponentValue = ExponentValue(2)

exponent_value **= 3

print(exponent_value.value)


# =============================================================================
# 33. __and__
# =============================================================================


class PermissionSet:
    """Represent permissions using bitwise AND."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __and__(self, other: PermissionSet) -> PermissionSet:
        return PermissionSet(self.value & other.value)


read_permission: PermissionSet = PermissionSet(0b001)
write_permission: PermissionSet = PermissionSet(0b011)

common_permission: PermissionSet = read_permission & write_permission

print(bin(common_permission.value))


# =============================================================================
# 34. __or__
# =============================================================================


class FeatureFlags:
    """Represent feature flags using bitwise OR."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __or__(self, other: FeatureFlags) -> FeatureFlags:
        return FeatureFlags(self.value | other.value)


feature_a: FeatureFlags = FeatureFlags(0b001)
feature_b: FeatureFlags = FeatureFlags(0b100)

combined_features: FeatureFlags = feature_a | feature_b

print(bin(combined_features.value))


# =============================================================================
# 35. __xor__
# =============================================================================


class BitMask:
    """Represent a bit mask supporting XOR."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __xor__(self, other: BitMask) -> BitMask:
        return BitMask(self.value ^ other.value)


mask_a: BitMask = BitMask(0b1010)
mask_b: BitMask = BitMask(0b1100)

xor_mask: BitMask = mask_a ^ mask_b

print(bin(xor_mask.value))


# =============================================================================
# 36. __invert__
# =============================================================================


class BinaryValue:
    """Represent a value supporting bitwise inversion."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __invert__(self) -> BinaryValue:
        return BinaryValue(~self.value)


binary_value: BinaryValue = BinaryValue(0b1010)
inverted_value: BinaryValue = ~binary_value

print(inverted_value.value)


# =============================================================================
# 37. __lshift__
# =============================================================================


class BitValue:
    """Represent a value supporting left shift."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __lshift__(self, positions: int) -> BitValue:
        return BitValue(self.value << positions)


bit_value: BitValue = BitValue(2)
shifted_left: BitValue = bit_value << 3

print(shifted_left.value)


# =============================================================================
# 38. __rshift__
# =============================================================================


class ShiftValue:
    """Represent a value supporting right shift."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __rshift__(self, positions: int) -> ShiftValue:
        return ShiftValue(self.value >> positions)


shift_value: ShiftValue = ShiftValue(32)
shifted_right: ShiftValue = shift_value >> 2

print(shifted_right.value)


# =============================================================================
# 39. __hash__
# =============================================================================


class ProductCode:
    """Represent a hashable product code."""

    def __init__(self, code: str) -> None:
        self.code: str = code

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProductCode):
            return NotImplemented

        return self.code == other.code

    def __hash__(self) -> int:
        return hash(self.code)


product_code: ProductCode = ProductCode("PY-001")

product_codes: set[ProductCode] = {
    product_code,
}

print(product_code in product_codes)


# =============================================================================
# 40. __index__
# =============================================================================


class IndexValue:
    """Represent an integer-like value usable as an index."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __index__(self) -> int:
        return self.value


items: list[str] = [
    "Python",
    "Java",
    "Go",
]

index_value: IndexValue = IndexValue(1)

print(items[index_value])


# =============================================================================
# 41. __round__
# =============================================================================


class Price:
    """Represent a price supporting round()."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __round__(self, ndigits: int = 0) -> int | float:
        rounded: float = round(self.value, ndigits)

        if ndigits == 0:
            return int(rounded)

        return rounded


price: Price = Price(19.8765)

print(round(price))
print(round(price, 2))


# =============================================================================
# 42. __enter__ and __exit__
# =============================================================================


class Resource:
    """Represent a simple context-manager resource."""

    def __enter__(self) -> Resource:
        print("Resource opened")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: Any,
    ) -> None:
        print("Resource closed")


with Resource() as resource:
    print(resource)


# =============================================================================
# 43. __iter__
# =============================================================================


class NumberCollection:
    """Represent a collection supporting iteration."""

    def __init__(self, values: list[int]) -> None:
        self.values: list[int] = values

    def __iter__(self) -> Iterator[int]:
        return iter(self.values)


number_collection: NumberCollection = NumberCollection(
    [
        10,
        20,
        30,
    ]
)

for number in number_collection:
    print(number)


# =============================================================================
# 44. __next__
# =============================================================================


class Countdown:
    """Represent an iterator using __iter__ and __next__."""

    def __init__(self, start: int) -> None:
        self.current: int = start

    def __iter__(self) -> Countdown:
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration

        value: int = self.current
        self.current -= 1

        return value


countdown: Countdown = Countdown(3)

for value in countdown:
    print(value)


# =============================================================================
# 45. __format__
# =============================================================================


class Percentage:
    """Represent a percentage with custom formatting."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __format__(self, format_spec: str) -> str:
        return f"{self.value:{format_spec}}%"


percentage: Percentage = Percentage(87.456)

print(f"{percentage:.2f}")


# =============================================================================
# 46. __bytes__
# =============================================================================


class Message:
    """Represent a message that can be converted to bytes."""

    def __init__(self, text: str) -> None:
        self.text: str = text

    def __bytes__(self) -> bytes:
        return self.text.encode("utf-8")


message: Message = Message("Hello Python")

message_bytes: bytes = bytes(message)

print(message_bytes)


# =============================================================================
# 47. __bool__ With Business Logic
# =============================================================================


class Account:
    """Represent an account whose truth value depends on its balance."""

    def __init__(self, balance: float) -> None:
        self.balance: float = balance

    def __bool__(self) -> bool:
        return self.balance > 0


active_account: Account = Account(500.0)
empty_account: Account = Account(0.0)

if active_account:
    print("Account has funds")

if not empty_account:
    print("Account has no funds")


# =============================================================================
# 48. Combining Multiple Dunder Methods
# =============================================================================


class Money:
    """Represent money with arithmetic and comparison operations."""

    def __init__(self, amount: float) -> None:
        self.amount: float = amount

    def __add__(self, other: Money) -> Money:
        return Money(self.amount + other.amount)

    def __sub__(self, other: Money) -> Money:
        return Money(self.amount - other.amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented

        return self.amount == other.amount

    def __lt__(self, other: Money) -> bool:
        return self.amount < other.amount

    def __str__(self) -> str:
        return f"${self.amount:.2f}"


money_a: Money = Money(100.0)
money_b: Money = Money(50.0)

money_total: Money = money_a + money_b
money_difference: Money = money_a - money_b

print(money_total)
print(money_difference)
print(money_a == money_b)
print(money_a < money_b)


# =============================================================================
# 49. Reverse Operator __radd__
# =============================================================================


class ScoreValue:
    """Represent a score supporting normal and reverse addition."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: ScoreValue) -> ScoreValue:
        return ScoreValue(self.value + other.value)

    def __radd__(self, other: int) -> ScoreValue:
        return ScoreValue(other + self.value)


score_value: ScoreValue = ScoreValue(25)

regular_sum: ScoreValue = ScoreValue(10) + score_value
reverse_sum: ScoreValue = 100 + score_value

print(regular_sum.value)
print(reverse_sum.value)


# =============================================================================
# 50. Reverse Multiplication __rmul__
# =============================================================================


class DistanceValue:
    """Represent a distance supporting normal and reverse multiplication."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __mul__(self, multiplier: float) -> DistanceValue:
        return DistanceValue(self.value * multiplier)

    def __rmul__(self, multiplier: float) -> DistanceValue:
        return DistanceValue(multiplier * self.value)

    def __str__(self) -> str:
        return f"{self.value:.2f} km"


distance_value: DistanceValue = DistanceValue(10.0)

normal_distance: DistanceValue = distance_value * 2
reverse_distance: DistanceValue = 3 * distance_value

print(normal_distance)
print(reverse_distance)


# =============================================================================
# Dunder Operator Method Summary
# =============================================================================
"""
Arithmetic:

    __add__        +
    __sub__        -
    __mul__        *
    __truediv__    /
    __floordiv__   //
    __mod__        %
    __pow__        **

Reverse arithmetic:

    __radd__
    __rsub__
    __rmul__
    __rtruediv__
    __rfloordiv__
    __rmod__
    __rpow__

Comparison:

    __eq__         ==
    __ne__         !=
    __lt__         <
    __le__         <=
    __gt__         >
    __ge__         >=

Unary:

    __neg__        -
    __pos__        +
    __abs__        abs()
    __invert__     ~

In-place:

    __iadd__       +=
    __isub__       -=
    __imul__       *=
    __itruediv__   /=
    __ifloordiv__  //=
    __imod__       %=
    __ipow__       **=

Bitwise:

    __and__        &
    __or__         |
    __xor__        ^
    __invert__     ~
    __lshift__     <<
    __rshift__     >>

Container behavior:

    __len__        len()
    __getitem__    []
    __setitem__    [] =
    __delitem__    del []
    __contains__   in
    __iter__       iteration
    __next__       next()

Object behavior:

    __str__        str()
    __repr__       repr()
    __bool__       bool()
    __hash__       hash()
    __call__       object()
    __format__     format()
    __bytes__      bytes()
    __index__      integer/index conversion

Context managers:

    __enter__
    __exit__

Important idea:

    Python syntax
        |
        v
    Special method
        |
        v
    Custom class behavior

For example:

    first + second

becomes conceptually:

    first.__add__(second)

Similarly:

    first == second

uses:

    first.__eq__(second)

and:

    -value

uses:

    value.__neg__()

Dunder methods allow user-defined objects to participate naturally in
Python's operator system.
"""


# =============================================================================
# Key Takeaways
# =============================================================================
"""
✓ Dunder methods are special methods defined by Python's data model.

✓ Their names begin and end with double underscores.

✓ Operators on custom objects can trigger dunder methods.

✓ __add__ implements +.

✓ __sub__ implements -.

✓ __mul__ implements *.

✓ __truediv__ implements /.

✓ __floordiv__ implements //.

✓ __mod__ implements %.

✓ __pow__ implements **.

✓ Comparison operators use methods such as __eq__, __lt__, and __gt__.

✓ Unary operators use methods such as __neg__, __pos__, and __invert__.

✓ In-place operators can use methods such as __iadd__ and __imul__.

✓ __getitem__ controls [] access.

✓ __setitem__ controls indexed assignment.

✓ __contains__ controls membership testing.

✓ __len__ controls len().

✓ __bool__ controls truth-value testing.

✓ __call__ makes an object callable.

✓ __str__ controls the user-facing string representation.

✓ __repr__ provides a developer-oriented representation.

✓ __iter__ and __next__ allow custom iteration.

✓ __enter__ and __exit__ allow custom context managers.

✓ Reverse operators such as __radd__ handle operations where the custom
  object appears on the right-hand side.

✓ __hash__ allows suitable immutable objects to participate in sets and
  dictionary keys.

✓ Dunder methods should model behavior that is natural for the object.

Core model:

    Python operator
        |
        v
    Special method
        |
        v
    Custom object behavior

Example:

    a + b
        |
        v
    a.__add__(b)

Example:

    a == b
        |
        v
    a.__eq__(b)

Example:

    -a
        |
        v
    a.__neg__()

The goal of operator overloading is not merely to make every operator
available.

The goal is to make custom objects behave naturally and predictably
when used with normal Python syntax.
"""


# =============================================================================
# End of 16_dunder_operator_methods.py
# =============================================================================