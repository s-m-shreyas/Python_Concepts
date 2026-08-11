# type: ignore
# =============================================================================
# 20. Custom Operator Overloading
# =============================================================================
"""
Python Operators
File:
20_custom_operator_overloading.py

Topic:
Custom Operator Overloading

Overview:

Custom operator overloading allows a user-defined class to define how
Python operators behave with its objects.

For example:

    +
    -
    *
    /
    //
    %
    **
    <
    <=
    >
    >=
    ==
    !=
    &
    |
    ^
    ~
    <<
    >>
    +=
    -=
    *=
    /=
    in
    []
    ()

can be customized by implementing special methods.

Examples:

    __add__      -> +
    __sub__      -> -
    __mul__      -> *
    __truediv__  -> /
    __floordiv__ -> //
    __mod__      -> %
    __pow__      -> **
    __eq__       -> ==
    __ne__       -> !=
    __lt__       -> <
    __le__       -> <=
    __gt__       -> >
    __ge__       -> >=
    __and__      -> &
    __or__       -> |
    __xor__      -> ^
    __invert__   -> ~
    __lshift__   -> <<
    __rshift__   -> >>
    __neg__      -> -
    __pos__      -> +
    __abs__      -> abs()
    __iadd__     -> +=
    __isub__     -> -=
    __imul__     -> *=
    __contains__ -> in
    __getitem__  -> []
    __call__     -> ()

The goal of custom operator overloading is not to create new operators.

Instead, it allows existing Python operators to have meaningful behavior
for custom objects.

Important principle:

    Use operator overloading only when the operator meaning is natural
    and intuitive for the custom type.
"""

# =============================================================================
# 01. Custom + Operator
# =============================================================================


class Number:
    """Represent a simple custom numeric value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: Number) -> Number:
        return Number(self.value + other.value)

    def __repr__(self) -> str:
        return f"Number({self.value})"


number_a = Number(10)
number_b = Number(20)

number_c = number_a + number_b

print(number_c)


# =============================================================================
# 02. Custom - Operator
# =============================================================================


class Difference:
    """Represent a value supporting subtraction."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __sub__(self, other: Difference) -> Difference:
        return Difference(self.value - other.value)

    def __repr__(self) -> str:
        return f"Difference({self.value})"


difference_a = Difference(50)
difference_b = Difference(20)

difference_c = difference_a - difference_b

print(difference_c)


# =============================================================================
# 03. Custom * Operator
# =============================================================================


class Product:
    """Represent a value supporting multiplication."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __mul__(self, other: Product) -> Product:
        return Product(self.value * other.value)

    def __repr__(self) -> str:
        return f"Product({self.value})"


product_a = Product(5)
product_b = Product(4)

product_c = product_a * product_b

print(product_c)


# =============================================================================
# 04. Custom / Operator
# =============================================================================


class Division:
    """Represent a value supporting true division."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __truediv__(self, other: Division) -> Division:
        return Division(self.value / other.value)

    def __repr__(self) -> str:
        return f"Division({self.value})"


division_a = Division(20.0)
division_b = Division(4.0)

division_c = division_a / division_b

print(division_c)


# =============================================================================
# 05. Custom // Operator
# =============================================================================


class FloorDivision:
    """Represent a value supporting floor division."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __floordiv__(self, other: FloorDivision) -> FloorDivision:
        return FloorDivision(self.value // other.value)

    def __repr__(self) -> str:
        return f"FloorDivision({self.value})"


floor_a = FloorDivision(17)
floor_b = FloorDivision(5)

floor_c = floor_a // floor_b

print(floor_c)


# =============================================================================
# 06. Custom % Operator
# =============================================================================


class Remainder:
    """Represent a value supporting modulo."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __mod__(self, other: Remainder) -> Remainder:
        return Remainder(self.value % other.value)

    def __repr__(self) -> str:
        return f"Remainder({self.value})"


remainder_a = Remainder(17)
remainder_b = Remainder(5)

remainder_c = remainder_a % remainder_b

print(remainder_c)


# =============================================================================
# 07. Custom ** Operator
# =============================================================================


class Power:
    """Represent a value supporting exponentiation."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __pow__(self, other: Power) -> Power:
        return Power(self.value**other.value)

    def __repr__(self) -> str:
        return f"Power({self.value})"


power_a = Power(2)
power_b = Power(5)

power_c = power_a**power_b

print(power_c)


# =============================================================================
# 08. Custom Unary - Operator
# =============================================================================


class Temperature:
    """Represent a temperature value."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __neg__(self) -> Temperature:
        return Temperature(-self.value)

    def __repr__(self) -> str:
        return f"Temperature({self.value})"


temperature = Temperature(25.0)

negative_temperature = -temperature

print(negative_temperature)


# =============================================================================
# 09. Custom Unary + Operator
# =============================================================================


class Score:
    """Represent a score supporting unary plus."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __pos__(self) -> Score:
        return Score(+self.value)

    def __repr__(self) -> str:
        return f"Score({self.value})"


score = Score(100)

positive_score = +score

print(positive_score)


# =============================================================================
# 10. Custom ~ Operator
# =============================================================================


class Flags:
    """Represent an integer flag value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __invert__(self) -> Flags:
        return Flags(~self.value)

    def __repr__(self) -> str:
        return f"Flags({self.value})"


flags = Flags(10)

inverted_flags = ~flags

print(inverted_flags)


# =============================================================================
# 11. Custom abs() Behavior
# =============================================================================


class Measurement:
    """Represent a signed measurement."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __abs__(self) -> Measurement:
        return Measurement(abs(self.value))

    def __repr__(self) -> str:
        return f"Measurement({self.value})"


measurement = Measurement(-42.5)

absolute_measurement = abs(measurement)

print(absolute_measurement)


# =============================================================================
# 12. Custom == Operator
# =============================================================================


class User:
    """Represent a user identified by an ID."""

    def __init__(self, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented

        return self.user_id == other.user_id


user_a = User(1, "Alice")
user_b = User(1, "Alice")

print(user_a == user_b)


# =============================================================================
# 13. Custom != Operator
# =============================================================================


class ProductCode:
    """Represent a product code."""

    def __init__(self, code: str) -> None:
        self.code = code

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProductCode):
            return NotImplemented

        return self.code == other.code

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, ProductCode):
            return NotImplemented

        return self.code != other.code


code_a = ProductCode("PY-001")
code_b = ProductCode("PY-002")

print(code_a != code_b)


# =============================================================================
# 14. Custom < Operator
# =============================================================================


class Age:
    """Represent an age."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: Age) -> bool:
        return self.value < other.value


age_a = Age(20)
age_b = Age(30)

print(age_a < age_b)


# =============================================================================
# 15. Custom <= Operator
# =============================================================================


class Price:
    """Represent a price."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __le__(self, other: Price) -> bool:
        return self.amount <= other.amount


price_a = Price(100.0)
price_b = Price(100.0)

print(price_a <= price_b)


# =============================================================================
# 16. Custom > Operator
# =============================================================================


class ScoreValue:
    """Represent a comparable score."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __gt__(self, other: ScoreValue) -> bool:
        return self.value > other.value


score_a = ScoreValue(90)
score_b = ScoreValue(80)

print(score_a > score_b)


# =============================================================================
# 17. Custom >= Operator
# =============================================================================


class Version:
    """Represent a simple numeric version."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __ge__(self, other: Version) -> bool:
        return self.value >= other.value


version_a = Version(3)
version_b = Version(2)

print(version_a >= version_b)


# =============================================================================
# 18. Custom & Operator
# =============================================================================


class Permission:
    """Represent a permission bit mask."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __and__(self, other: Permission) -> Permission:
        return Permission(self.value & other.value)

    def __repr__(self) -> str:
        return f"Permission({self.value})"


read_permission = Permission(0b001)
write_permission = Permission(0b010)

combined_permission = read_permission & write_permission

print(combined_permission)


# =============================================================================
# 19. Custom | Operator
# =============================================================================


class PermissionSet:
    """Represent a permission bit mask."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __or__(self, other: PermissionSet) -> PermissionSet:
        return PermissionSet(self.value | other.value)

    def __repr__(self) -> str:
        return f"PermissionSet({self.value})"


read_set = PermissionSet(0b001)
write_set = PermissionSet(0b010)

combined_set = read_set | write_set

print(combined_set)


# =============================================================================
# 20. Custom ^ Operator
# =============================================================================


class BitValue:
    """Represent a bitwise value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __xor__(self, other: BitValue) -> BitValue:
        return BitValue(self.value ^ other.value)

    def __repr__(self) -> str:
        return f"BitValue({self.value})"


bit_a = BitValue(0b1010)
bit_b = BitValue(0b0110)

bit_result = bit_a ^ bit_b

print(bit_result)


# =============================================================================
# 21. Custom << Operator
# =============================================================================


class BitShift:
    """Represent an integer supporting left shifts."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lshift__(self, other: int) -> BitShift:
        return BitShift(self.value << other)

    def __repr__(self) -> str:
        return f"BitShift({self.value})"


shift_value = BitShift(4)

shifted_value = shift_value << 2

print(shifted_value)


# =============================================================================
# 22. Custom >> Operator
# =============================================================================


class RightShift:
    """Represent an integer supporting right shifts."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __rshift__(self, other: int) -> RightShift:
        return RightShift(self.value >> other)

    def __repr__(self) -> str:
        return f"RightShift({self.value})"


right_shift_value = RightShift(32)

shifted_right = right_shift_value >> 2

print(shifted_right)


# =============================================================================
# 23. Custom += Operator
# =============================================================================


class Counter:
    """Represent a mutable counter."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __iadd__(self, amount: int) -> Counter:
        self.value += amount
        return self

    def __repr__(self) -> str:
        return f"Counter({self.value})"


counter = Counter(10)

counter += 5

print(counter)


# =============================================================================
# 24. Custom -= Operator
# =============================================================================


class Balance:
    """Represent a mutable balance."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __isub__(self, amount: float) -> Balance:
        self.amount -= amount
        return self

    def __repr__(self) -> str:
        return f"Balance({self.amount})"


balance = Balance(1000.0)

balance -= 250.0

print(balance)


# =============================================================================
# 25. Custom *= Operator
# =============================================================================


class Quantity:
    """Represent a mutable quantity."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __imul__(self, multiplier: int) -> Quantity:
        self.value *= multiplier
        return self

    def __repr__(self) -> str:
        return f"Quantity({self.value})"


quantity = Quantity(5)

quantity *= 3

print(quantity)


# =============================================================================
# 26. Custom /= Operator
# =============================================================================


class AccountValue:
    """Represent a mutable numeric value."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __itruediv__(self, divisor: float) -> AccountValue:
        self.value /= divisor
        return self

    def __repr__(self) -> str:
        return f"AccountValue({self.value})"


account_value = AccountValue(100.0)

account_value /= 4.0

print(account_value)


# =============================================================================
# 27. Custom //= Operator
# =============================================================================


class PageCount:
    """Represent a mutable page count."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __ifloordiv__(self, divisor: int) -> PageCount:
        self.value //= divisor
        return self

    def __repr__(self) -> str:
        return f"PageCount({self.value})"


page_count = PageCount(100)

page_count //= 3

print(page_count)


# =============================================================================
# 28. Custom %= Operator
# =============================================================================


class RemainderValue:
    """Represent a mutable integer value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __imod__(self, divisor: int) -> RemainderValue:
        self.value %= divisor
        return self

    def __repr__(self) -> str:
        return f"RemainderValue({self.value})"


remainder_value = RemainderValue(17)

remainder_value %= 5

print(remainder_value)


# =============================================================================
# 29. Custom **= Operator
# =============================================================================


class ExponentValue:
    """Represent a mutable numeric value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __ipow__(self, exponent: int) -> ExponentValue:
        self.value **= exponent
        return self

    def __repr__(self) -> str:
        return f"ExponentValue({self.value})"


exponent_value = ExponentValue(2)

exponent_value **= 5

print(exponent_value)


# =============================================================================
# 30. Custom in Operator
# =============================================================================


class TagCollection:
    """Represent a collection of tags."""

    def __init__(self, tags: list[str]) -> None:
        self.tags = tags

    def __contains__(self, tag: str) -> bool:
        return tag.lower() in {
            current_tag.lower()
            for current_tag in self.tags
        }


tags = TagCollection(
    [
        "Python",
        "SQL",
        "Docker",
    ]
)

print("python" in tags)
print("Java" in tags)


# =============================================================================
# 31. Custom not in Operator
# =============================================================================


class BlockedWords:
    """Represent a collection of blocked words."""

    def __init__(self, words: set[str]) -> None:
        self.words = words

    def __contains__(self, word: str) -> bool:
        return word.lower() in self.words


blocked_words = BlockedWords(
    {
        "spam",
        "scam",
        "fraud",
    }
)

print("python" not in blocked_words)
print("spam" not in blocked_words)


# =============================================================================
# 32. Custom [] Indexing
# =============================================================================


class NumberList:
    """Represent a list-like custom object."""

    def __init__(self, values: list[int]) -> None:
        self.values = values

    def __getitem__(self, index: int) -> int:
        return self.values[index]


number_list = NumberList(
    [
        10,
        20,
        30,
    ]
)

print(number_list[1])


# =============================================================================
# 33. Custom [] Assignment
# =============================================================================


class MutableNumberList:
    """Represent a mutable list-like custom object."""

    def __init__(self, values: list[int]) -> None:
        self.values = values

    def __getitem__(self, index: int) -> int:
        return self.values[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.values[index] = value


mutable_numbers = MutableNumberList(
    [
        10,
        20,
        30,
    ]
)

mutable_numbers[1] = 200

print(mutable_numbers[1])


# =============================================================================
# 34. Custom del [] Indexing
# =============================================================================


class DeletableList:
    """Represent a list supporting indexed deletion."""

    def __init__(self, values: list[int]) -> None:
        self.values = values

    def __getitem__(self, index: int) -> int:
        return self.values[index]

    def __delitem__(self, index: int) -> None:
        del self.values[index]


deletable_numbers = DeletableList(
    [
        10,
        20,
        30,
    ]
)

del deletable_numbers[1]

print(deletable_numbers.values)


# =============================================================================
# 35. Custom Function Call Operator
# =============================================================================


class Multiplier:
    """Represent a callable multiplier object."""

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, value: int) -> int:
        return value * self.factor


double_value = Multiplier(2)

print(double_value(10))


# =============================================================================
# 36. Custom + With Scalar Support
# =============================================================================


class Money:
    """Represent a monetary amount."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __add__(self, other: float) -> Money:
        return Money(self.amount + other)

    def __repr__(self) -> str:
        return f"Money({self.amount})"


money = Money(100.0)

updated_money = money + 50.0

print(updated_money)


# =============================================================================
# 37. Custom + With Another Object
# =============================================================================


class Point:
    """Represent a two-dimensional point."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        return Point(
            self.x + other.x,
            self.y + other.y,
        )

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


point_a = Point(2.0, 3.0)
point_b = Point(4.0, 5.0)

point_c = point_a + point_b

print(point_c)


# =============================================================================
# 38. Custom - For Vectors
# =============================================================================


class Vector:
    """Represent a two-dimensional vector."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


vector_a = Vector(10.0, 8.0)
vector_b = Vector(3.0, 2.0)

vector_c = vector_a - vector_b

print(vector_c)


# =============================================================================
# 39. Custom * For Vector Scaling
# =============================================================================


class ScalableVector:
    """Represent a vector that supports scalar multiplication."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __mul__(self, scalar: float) -> ScalableVector:
        return ScalableVector(
            self.x * scalar,
            self.y * scalar,
        )

    def __repr__(self) -> str:
        return f"ScalableVector(x={self.x}, y={self.y})"


vector = ScalableVector(3.0, 4.0)

scaled_vector = vector * 2.0

print(scaled_vector)


# =============================================================================
# 40. Custom @ Operator
# =============================================================================


class Matrix:
    """Represent a simple 2x2 matrix."""

    def __init__(
        self,
        values: tuple[
            tuple[int, int],
            tuple[int, int],
        ],
    ) -> None:
        self.values = values

    def __matmul__(self, other: Matrix) -> Matrix:
        a = self.values
        b = other.values

        result = (
            (
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ),
            (
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ),
        )

        return Matrix(result)

    def __repr__(self) -> str:
        return f"Matrix({self.values})"


matrix_a = Matrix(
    (
        (1, 2),
        (3, 4),
    )
)

matrix_b = Matrix(
    (
        (5, 6),
        (7, 8),
    )
)

matrix_c = matrix_a @ matrix_b

print(matrix_c)


# =============================================================================
# 41. Custom Right-Hand + Operator
# =============================================================================


class TemperatureValue:
    """Represent a temperature supporting right-hand addition."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __add__(self, other: float) -> TemperatureValue:
        return TemperatureValue(self.value + other)

    def __radd__(self, other: float) -> TemperatureValue:
        return TemperatureValue(other + self.value)

    def __repr__(self) -> str:
        return f"TemperatureValue({self.value})"


temperature_value = TemperatureValue(25.0)

result_left = temperature_value + 5.0
result_right = 5.0 + temperature_value

print(result_left)
print(result_right)


# =============================================================================
# 42. Custom Right-Hand * Operator
# =============================================================================


class Distance:
    """Represent a distance supporting scalar multiplication."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __mul__(self, scalar: float) -> Distance:
        return Distance(self.value * scalar)

    def __rmul__(self, scalar: float) -> Distance:
        return Distance(scalar * self.value)

    def __repr__(self) -> str:
        return f"Distance({self.value})"


distance = Distance(10.0)

print(distance * 3.0)
print(3.0 * distance)


# =============================================================================
# 43. Custom Comparison With Multiple Attributes
# =============================================================================


class Student:
    """Represent a student with a grade."""

    def __init__(self, name: str, grade: float) -> None:
        self.name = name
        self.grade = grade

    def __lt__(self, other: Student) -> bool:
        return self.grade < other.grade

    def __repr__(self) -> str:
        return (
            f"Student(name={self.name!r}, "
            f"grade={self.grade})"
        )


student_a = Student("Alice", 85.0)
student_b = Student("Bob", 92.0)

print(student_a < student_b)


# =============================================================================
# 44. Custom Equality Based On Multiple Attributes
# =============================================================================


class Coordinate:
    """Represent a two-dimensional coordinate."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented

        return (
            self.x == other.x
            and self.y == other.y
        )


coordinate_a = Coordinate(10, 20)
coordinate_b = Coordinate(10, 20)
coordinate_c = Coordinate(30, 40)

print(coordinate_a == coordinate_b)
print(coordinate_a == coordinate_c)


# =============================================================================
# 45. Custom Hashing With Equality
# =============================================================================


class UserIdentity:
    """Represent an immutable-style user identity."""

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserIdentity):
            return NotImplemented

        return self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash(self.user_id)

    def __repr__(self) -> str:
        return f"UserIdentity({self.user_id})"


identity_a = UserIdentity(100)
identity_b = UserIdentity(100)

identity_set = {
    identity_a,
    identity_b,
}

print(identity_set)


# =============================================================================
# 46. Custom Operator Chaining
# =============================================================================


class Amount:
    """Represent an amount supporting chained addition."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __add__(self, other: Amount) -> Amount:
        return Amount(self.value + other.value)

    def __repr__(self) -> str:
        return f"Amount({self.value})"


amount_a = Amount(10.0)
amount_b = Amount(20.0)
amount_c = Amount(30.0)

total_amount = amount_a + amount_b + amount_c

print(total_amount)


# =============================================================================
# 47. Custom Operator Returning a New Object
# =============================================================================


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __mul__(self, scale: float) -> Rectangle:
        return Rectangle(
            self.width * scale,
            self.height * scale,
        )

    def __repr__(self) -> str:
        return (
            f"Rectangle(width={self.width}, "
            f"height={self.height})"
        )


rectangle = Rectangle(10.0, 5.0)

larger_rectangle = rectangle * 2.0

print(larger_rectangle)


# =============================================================================
# 48. Custom Operator Preserving the Same Object
# =============================================================================


class MutableScore:
    """Represent a mutable score."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __iadd__(self, points: int) -> MutableScore:
        self.value += points
        return self

    def __repr__(self) -> str:
        return f"MutableScore({self.value})"


mutable_score = MutableScore(50)

original_id = id(mutable_score)

mutable_score += 25

new_id = id(mutable_score)

print(mutable_score)
print(original_id == new_id)


# =============================================================================
# 49. Custom Operators For Domain Objects
# =============================================================================


class MoneyAmount:
    """Represent money in a simple domain model."""

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: MoneyAmount) -> MoneyAmount:
        if self.currency != other.currency:
            raise ValueError(
                "Cannot add amounts with different currencies."
            )

        return MoneyAmount(
            self.amount + other.amount,
            self.currency,
        )

    def __repr__(self) -> str:
        return (
            f"MoneyAmount("
            f"amount={self.amount}, "
            f"currency={self.currency!r})"
        )


money_a = MoneyAmount(100.0, "USD")
money_b = MoneyAmount(50.0, "USD")

money_total = money_a + money_b

print(money_total)


# =============================================================================
# 50. Complete Custom Operator Example
# =============================================================================


class Vector2D:
    """
    Represent a two-dimensional vector with several overloaded operators.

    Supported operators:

        +
        -
        *
        ==
        <
        -
        abs()
        +=
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, scalar: float) -> Vector2D:
        return Vector2D(
            self.x * scalar,
            self.y * scalar,
        )

    def __rmul__(self, scalar: float) -> Vector2D:
        return Vector2D(
            scalar * self.x,
            scalar * self.y,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented

        return (
            self.x == other.x
            and self.y == other.y
        )

    def __lt__(self, other: Vector2D) -> bool:
        return self.magnitude() < other.magnitude()

    def __neg__(self) -> Vector2D:
        return Vector2D(
            -self.x,
            -self.y,
        )

    def __abs__(self) -> float:
        return self.magnitude()

    def __iadd__(self, other: Vector2D) -> Vector2D:
        self.x += other.x
        self.y += other.y

        return self

    def magnitude(self) -> float:
        return (
            self.x**2
            + self.y**2
        ) ** 0.5

    def __repr__(self) -> str:
        return (
            f"Vector2D("
            f"x={self.x}, "
            f"y={self.y})"
        )


vector_a = Vector2D(3.0, 4.0)
vector_b = Vector2D(1.0, 2.0)

vector_sum = vector_a + vector_b
vector_difference = vector_a - vector_b
scaled_vector = vector_a * 2.0
reverse_scaled_vector = 2.0 * vector_a
negative_vector = -vector_a
vector_length = abs(vector_a)

vector_copy = Vector2D(3.0, 4.0)
vectors_equal = vector_a == vector_copy
vector_is_smaller = vector_b < vector_a

vector_a += vector_b

print(vector_sum)
print(vector_difference)
print(scaled_vector)
print(reverse_scaled_vector)
print(negative_vector)
print(vector_length)
print(vectors_equal)
print(vector_is_smaller)
print(vector_a)


# =============================================================================
# Custom Operator Overloading - Core Rules
# =============================================================================
"""
Custom operator overloading follows a simple model:

    Python operator
            |
            v
    special / dunder method
            |
            v
    custom class behavior

Examples:

    a + b
        -> a.__add__(b)

    a - b
        -> a.__sub__(b)

    a * b
        -> a.__mul__(b)

    a / b
        -> a.__truediv__(b)

    a == b
        -> a.__eq__(b)

    a < b
        -> a.__lt__(b)

    a & b
        -> a.__and__(b)

    a | b
        -> a.__or__(b)

    a ^ b
        -> a.__xor__(b)

    ~a
        -> a.__invert__()

    -a
        -> a.__neg__()

    +a
        -> a.__pos__()

    a += b
        -> a.__iadd__(b)

    a in b
        -> b.__contains__(a)

    a[b]
        -> a.__getitem__(b)

    a(b)
        -> a.__call__(b)

Operator overloading does not create a new Python operator.

It defines behavior for an existing Python operator.

The best custom operators are:

    - predictable
    - intuitive
    - consistent
    - type-safe
    - meaningful for the domain

For example, vector addition is intuitive:

    vector_a + vector_b

Money addition can also be intuitive:

    money_a + money_b

But using + for an unrelated operation can make code confusing.

Good operator overloading improves readability.

Bad operator overloading hides what the code is actually doing.
"""


# =============================================================================
# Common Operator Mapping
# =============================================================================
"""
Arithmetic:

    +       __add__
    -       __sub__
    *       __mul__
    /       __truediv__
    //      __floordiv__
    %       __mod__
    **      __pow__

Reverse arithmetic:

    +       __radd__
    -       __rsub__
    *       __rmul__
    /       __rtruediv__
    //      __rfloordiv__
    %       __rmod__
    **      __rpow__

Comparison:

    ==      __eq__
    !=      __ne__
    <       __lt__
    <=      __le__
    >       __gt__
    >=      __ge__

Bitwise:

    &       __and__
    |       __or__
    ^       __xor__
    ~       __invert__
    <<      __lshift__
    >>      __rshift__

Unary:

    +       __pos__
    -       __neg__
    abs()   __abs__

In-place:

    +=      __iadd__
    -=      __isub__
    *=      __imul__
    /=      __itruediv__
    //=     __ifloordiv__
    %=      __imod__
    **=     __ipow__
    &=      __iand__
    |=      __ior__
    ^=      __ixor__
    <<=     __ilshift__
    >>=     __irshift__

Container-like:

    in      __contains__
    []      __getitem__
    [] =    __setitem__
    del []  __delitem__

Callable:

    object() -> __call__

Matrix multiplication:

    @       __matmul__
"""


# =============================================================================
# Operator Overloading Versus Normal Methods
# =============================================================================
"""
Normal method:

    vector.add(other)

Operator overloaded method:

    vector + other

Both can perform an operation.

The difference is the interface.

Normal method:

    result = vector.add(other)

Operator:

    result = vector + other

Operator syntax can be more readable when the operation has a natural
mathematical or container meaning.

For example:

    total = price_a + price_b

is generally more natural than:

    total = price_a.add(price_b)

for a numeric-style domain object.
"""


# =============================================================================
# Operator Overloading Versus Custom Operators
# =============================================================================
"""
Python does not allow a class to invent syntax such as:

    a %% b

or:

    a <=> b

Instead, a class can overload operators already provided by Python.

Therefore:

    operator overloading
        =
    customizing existing Python operator behavior

It does NOT mean:

    creating a brand-new Python operator
"""


# =============================================================================
# Final Summary
# =============================================================================
"""
Custom operator overloading allows classes to participate naturally in
Python expressions.

Core idea:

    custom object
          |
          v
    Python operator
          |
          v
    dunder method
          |
          v
    custom behavior

Examples:

    Vector2D(1, 2) + Vector2D(3, 4)

    MoneyAmount(100, "USD") + MoneyAmount(50, "USD")

    Point(1, 2) == Point(1, 2)

    Permission(0b001) | Permission(0b010)

    5.0 * Distance(10.0)

    "python" in TagCollection(["Python"])

    numbers[0]

    callable_object(10)

The most important rule is:

    Do not overload operators merely because Python allows it.

Use an operator when its normal meaning makes sense for the custom object.

Good:

    vector_a + vector_b

    money_a + money_b

    date_a < date_b

    matrix_a @ matrix_b

Potentially confusing:

    user_a + user_b

    employee_a * employee_b

unless those operations have a clear domain-specific meaning.

Operator overloading is most useful when it makes custom objects behave
naturally like the kind of objects they represent.
"""


# =============================================================================
# End of 20_custom_operator_overloading.py
# =============================================================================