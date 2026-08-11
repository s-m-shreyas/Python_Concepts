# type: ignore
# =============================================================================
# 15. Operator Overloading
# =============================================================================
"""
Python Operators
15_operator_overloading.py

Topic
-----
Operator Overloading

Overview
--------
Operator overloading allows user-defined classes to define how Python
operators behave with their objects.

Python operators such as:

    +
    -
    *
    /
    //
    %
    **
    ==
    !=
    <
    <=
    >
    >=
    []
    in
    +=
    -
    bool()
    str()
    repr()

can be customized by implementing special methods, also called
dunder methods.

Common examples:

    __add__       -> +
    __sub__       -> -
    __mul__       -> *
    __truediv__   -> /
    __floordiv__  -> //
    __mod__       -> %
    __pow__       -> **
    __eq__        -> ==
    __ne__        -> !=
    __lt__        -> <
    __le__        -> <=
    __gt__        -> >
    __ge__        -> >=
    __neg__       -> unary -
    __pos__       -> unary +
    __abs__       -> abs()
    __bool__      -> bool()
    __str__       -> str()
    __repr__      -> repr()
    __len__       -> len()
    __getitem__   -> []
    __contains__  -> in
    __call__      -> object()
    __iadd__      -> +=

Operator overloading does not create new operators.

Instead, it defines how existing Python operators work with objects
created from custom classes.

The important idea is:

    Python operator
            ↓
    special method
            ↓
    custom class behavior

Example:

    first + second

can internally invoke:

    first.__add__(second)

"""

# =============================================================================
# 01. Basic __add__
# =============================================================================

class Number:
    """Represent a number with custom addition behavior."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: "Number") -> "Number":
        return Number(self.value + other.value)


number_a = Number(10)
number_b = Number(20)

number_sum = number_a + number_b

print(number_sum.value)


# =============================================================================
# 02. Basic __sub__
# =============================================================================

class Score:
    """Represent a score with subtraction support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __sub__(self, other: "Score") -> "Score":
        return Score(self.value - other.value)


score_a = Score(100)
score_b = Score(30)

score_difference = score_a - score_b

print(score_difference.value)


# =============================================================================
# 03. Basic __mul__
# =============================================================================

class Price:
    """Represent a price with multiplication support."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __mul__(self, quantity: int) -> "Price":
        return Price(self.amount * quantity)


price = Price(25.50)

total_price = price * 4

print(total_price.amount)


# =============================================================================
# 04. Basic __truediv__
# =============================================================================

class Distance:
    """Represent a distance with division support."""

    def __init__(self, kilometers: float) -> None:
        self.kilometers = kilometers

    def __truediv__(self, divisor: float) -> "Distance":
        return Distance(self.kilometers / divisor)


distance = Distance(100.0)

half_distance = distance / 2

print(half_distance.kilometers)


# =============================================================================
# 05. Basic __floordiv__
# =============================================================================

class Quantity:
    """Represent a quantity with floor-division support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __floordiv__(self, divisor: int) -> "Quantity":
        return Quantity(self.value // divisor)


quantity = Quantity(17)

groups = quantity // 5

print(groups.value)


# =============================================================================
# 06. Basic __mod__
# =============================================================================

class Counter:
    """Represent a counter with modulo support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __mod__(self, divisor: int) -> int:
        return self.value % divisor


counter = Counter(17)

remainder = counter % 5

print(remainder)


# =============================================================================
# 07. Basic __pow__
# =============================================================================

class BaseNumber:
    """Represent a number with exponentiation support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __pow__(self, exponent: int) -> "BaseNumber":
        return BaseNumber(self.value ** exponent)


base = BaseNumber(2)

power_result = base ** 5

print(power_result.value)


# =============================================================================
# 08. __add__ With Strings
# =============================================================================

class FullName:
    """Represent a name that can be combined with another name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __add__(self, other: "FullName") -> "FullName":
        combined_name = f"{self.name} {other.name}"
        return FullName(combined_name)


first_name = FullName("John")
last_name = FullName("Smith")

full_name = first_name + last_name

print(full_name.name)


# =============================================================================
# 09. __eq__ Equality
# =============================================================================

class User:
    """Represent a user with value-based equality."""

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented

        return self.user_id == other.user_id


user_one = User(101)
user_two = User(101)
user_three = User(202)

print(user_one == user_two)
print(user_one == user_three)


# =============================================================================
# 10. __ne__ Inequality
# =============================================================================

class Product:
    """Represent a product with custom inequality behavior."""

    def __init__(self, product_id: int) -> None:
        self.product_id = product_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.product_id == other.product_id

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.product_id != other.product_id


product_a = Product(10)
product_b = Product(20)

print(product_a != product_b)


# =============================================================================
# 11. __lt__ Less Than
# =============================================================================

class Age:
    """Represent an age with comparison support."""

    def __init__(self, years: int) -> None:
        self.years = years

    def __lt__(self, other: "Age") -> bool:
        return self.years < other.years


age_a = Age(20)
age_b = Age(30)

print(age_a < age_b)


# =============================================================================
# 12. __le__ Less Than Or Equal
# =============================================================================

class Temperature:
    """Represent a temperature with <= support."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __le__(self, other: "Temperature") -> bool:
        return self.value <= other.value


temperature_a = Temperature(20.0)
temperature_b = Temperature(20.0)

print(temperature_a <= temperature_b)


# =============================================================================
# 13. __gt__ Greater Than
# =============================================================================

class Salary:
    """Represent salary values with > support."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __gt__(self, other: "Salary") -> bool:
        return self.amount > other.amount


salary_a = Salary(50000.0)
salary_b = Salary(40000.0)

print(salary_a > salary_b)


# =============================================================================
# 14. __ge__ Greater Than Or Equal
# =============================================================================

class Rating:
    """Represent a rating with >= support."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __ge__(self, other: "Rating") -> bool:
        return self.value >= other.value


rating_a = Rating(4.5)
rating_b = Rating(4.0)

print(rating_a >= rating_b)


# =============================================================================
# 15. Multiple Comparison Operators
# =============================================================================

class Version:
    """Represent a version using multiple comparison operators."""

    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor

    def _key(self) -> tuple[int, int]:
        return self.major, self.minor

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented

        return self._key() == other._key()

    def __lt__(self, other: "Version") -> bool:
        return self._key() < other._key()


version_one = Version(1, 2)
version_two = Version(2, 0)

print(version_one == version_two)
print(version_one < version_two)


# =============================================================================
# 16. @total_ordering
# =============================================================================

from functools import total_ordering


@total_ordering
class Priority:
    """Represent a priority with generated ordering methods."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Priority):
            return NotImplemented

        return self.value == other.value

    def __lt__(self, other: "Priority") -> bool:
        return self.value < other.value


low_priority = Priority(1)
high_priority = Priority(5)

print(low_priority < high_priority)
print(low_priority <= high_priority)
print(high_priority > low_priority)
print(high_priority >= low_priority)


# =============================================================================
# 17. __neg__ Unary Minus
# =============================================================================

class Balance:
    """Represent a balance with unary minus support."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __neg__(self) -> "Balance":
        return Balance(-self.amount)


balance = Balance(500.0)

negative_balance = -balance

print(negative_balance.amount)


# =============================================================================
# 18. __pos__ Unary Plus
# =============================================================================

class Measurement:
    """Represent a measurement with unary plus support."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __pos__(self) -> "Measurement":
        return Measurement(+self.value)


measurement = Measurement(25.0)

positive_measurement = +measurement

print(positive_measurement.value)


# =============================================================================
# 19. __abs__ Absolute Value
# =============================================================================

class Coordinate:
    """Represent a coordinate with abs() support."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __abs__(self) -> float:
        return abs(self.value)


coordinate = Coordinate(-25.0)

absolute_coordinate = abs(coordinate)

print(absolute_coordinate)


# =============================================================================
# 20. __bool__ Boolean Conversion
# =============================================================================

class Account:
    """Represent an account whose truth value depends on its balance."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def __bool__(self) -> bool:
        return self.balance > 0


active_account = Account(100.0)
empty_account = Account(0.0)

print(bool(active_account))
print(bool(empty_account))


# =============================================================================
# 21. __str__ String Conversion
# =============================================================================

class Person:
    """Represent a person with a custom string representation."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"


person = Person("Alice", 30)

print(str(person))
print(person)


# =============================================================================
# 22. __repr__ Developer Representation
# =============================================================================

class Point:
    """Represent a point with a useful developer representation."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


point = Point(10.0, 20.0)

print(repr(point))


# =============================================================================
# 23. __str__ And __repr__ Together
# =============================================================================

class Book:
    """Represent a book with user and developer representations."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r})"


book = Book("Python Basics", "John Doe")

print(str(book))
print(repr(book))


# =============================================================================
# 24. __len__
# =============================================================================

class Playlist:
    """Represent a playlist with len() support."""

    def __init__(self, songs: list[str]) -> None:
        self.songs = songs

    def __len__(self) -> int:
        return len(self.songs)


playlist = Playlist(
    [
        "Song A",
        "Song B",
        "Song C",
    ]
)

print(len(playlist))


# =============================================================================
# 25. __getitem__
# =============================================================================

class Team:
    """Represent a team that supports index access."""

    def __init__(self, members: list[str]) -> None:
        self.members = members

    def __getitem__(self, index: int) -> str:
        return self.members[index]


team = Team(
    [
        "Alice",
        "Bob",
        "Charlie",
    ]
)

print(team[0])
print(team[1])


# =============================================================================
# 26. __setitem__
# =============================================================================

class Scores:
    """Represent scores with index assignment support."""

    def __init__(self, values: list[int]) -> None:
        self.values = values

    def __getitem__(self, index: int) -> int:
        return self.values[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.values[index] = value


scores = Scores(
    [
        10,
        20,
        30,
    ]
)

scores[1] = 100

print(scores[1])


# =============================================================================
# 27. __contains__
# =============================================================================

class Inventory:
    """Represent an inventory with membership testing."""

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __contains__(self, item: str) -> bool:
        return item in self.items


inventory = Inventory(
    [
        "Laptop",
        "Mouse",
        "Keyboard",
    ]
)

print("Laptop" in inventory)
print("Monitor" in inventory)


# =============================================================================
# 28. __iter__
# =============================================================================

class NumberCollection:
    """Represent a collection that supports iteration."""

    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def __iter__(self):
        return iter(self.numbers)


number_collection = NumberCollection(
    [
        10,
        20,
        30,
    ]
)

for number in number_collection:
    print(number)


# =============================================================================
# 29. __call__
# =============================================================================

class Multiplier:
    """Represent an object that can be called like a function."""

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, value: int) -> int:
        return value * self.factor


double = Multiplier(2)

double_result = double(10)

print(double_result)


# =============================================================================
# 30. Callable Object With Multiple Arguments
# =============================================================================

class Calculator:
    """Represent a callable calculator."""

    def __call__(self, first: float, second: float) -> float:
        return first + second


calculator = Calculator()

calculator_result = calculator(10.0, 20.0)

print(calculator_result)


# =============================================================================
# 31. __iadd__ In-Place Addition
# =============================================================================

class CounterValue:
    """Represent a counter with += support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __iadd__(self, amount: int) -> "CounterValue":
        self.value += amount
        return self


counter_value = CounterValue(10)

counter_value += 5

print(counter_value.value)


# =============================================================================
# 32. __isub__ In-Place Subtraction
# =============================================================================

class Wallet:
    """Represent a wallet with -= support."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def __isub__(self, amount: float) -> "Wallet":
        self.balance -= amount
        return self


wallet = Wallet(100.0)

wallet -= 25.0

print(wallet.balance)


# =============================================================================
# 33. __imul__ In-Place Multiplication
# =============================================================================

class QuantityValue:
    """Represent a quantity with *= support."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __imul__(self, multiplier: int) -> "QuantityValue":
        self.value *= multiplier
        return self


quantity_value = QuantityValue(5)

quantity_value *= 3

print(quantity_value.value)


# =============================================================================
# 34. __itruediv__ In-Place Division
# =============================================================================

class MeasurementValue:
    """Represent a measurement with /= support."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __itruediv__(self, divisor: float) -> "MeasurementValue":
        self.value /= divisor
        return self


measurement_value = MeasurementValue(100.0)

measurement_value /= 4.0

print(measurement_value.value)


# =============================================================================
# 35. Reflected Addition With __radd__
# =============================================================================

class NumberWrapper:
    """Support addition when the custom object appears on the right."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return self.value + other

    def __radd__(self, other: int) -> int:
        return other + self.value


wrapped_number = NumberWrapper(10)

print(wrapped_number + 5)
print(5 + wrapped_number)


# =============================================================================
# 36. Reflected Multiplication With __rmul__
# =============================================================================

class Factor:
    """Support multiplication from either side."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __mul__(self, other: int) -> int:
        return self.value * other

    def __rmul__(self, other: int) -> int:
        return other * self.value


factor = Factor(5)

print(factor * 3)
print(3 * factor)


# =============================================================================
# 37. __rsub__
# =============================================================================

class Subtractable:
    """Support reflected subtraction."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __sub__(self, other: int) -> int:
        return self.value - other

    def __rsub__(self, other: int) -> int:
        return other - self.value


subtractable = Subtractable(10)

print(subtractable - 3)
print(20 - subtractable)


# =============================================================================
# 38. __rtruediv__
# =============================================================================

class Divisor:
    """Support reflected true division."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __truediv__(self, other: float) -> float:
        return self.value / other

    def __rtruediv__(self, other: float) -> float:
        return other / self.value


divisor = Divisor(5.0)

print(divisor / 2.0)
print(20.0 / divisor)


# =============================================================================
# 39. __hash__
# =============================================================================

class EmployeeId:
    """Represent a hashable employee identifier."""

    def __init__(self, employee_id: int) -> None:
        self.employee_id = employee_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EmployeeId):
            return NotImplemented

        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        return hash(self.employee_id)


employee_one = EmployeeId(101)
employee_two = EmployeeId(101)

employee_set = {
    employee_one,
    employee_two,
}

print(len(employee_set))


# =============================================================================
# 40. Operator Overloading With a Vector
# =============================================================================

class Vector:
    """Represent a two-dimensional vector."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


vector_one = Vector(10.0, 20.0)
vector_two = Vector(5.0, 3.0)

vector_sum = vector_one + vector_two
vector_difference = vector_one - vector_two

print(vector_sum)
print(vector_difference)


# =============================================================================
# 41. Scalar Multiplication
# =============================================================================

class CoordinateVector:
    """Represent a vector that supports scalar multiplication."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __mul__(self, scalar: float) -> "CoordinateVector":
        return CoordinateVector(
            self.x * scalar,
            self.y * scalar,
        )

    def __rmul__(self, scalar: float) -> "CoordinateVector":
        return self * scalar

    def __repr__(self) -> str:
        return (
            f"CoordinateVector("
            f"x={self.x}, "
            f"y={self.y}"
            f")"
        )


coordinate_vector = CoordinateVector(2.0, 3.0)

scaled_one = coordinate_vector * 4.0
scaled_two = 4.0 * coordinate_vector

print(scaled_one)
print(scaled_two)


# =============================================================================
# 42. Complex Number Addition
# =============================================================================

class SimpleComplex:
    """Represent a simple complex number."""

    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: "SimpleComplex") -> "SimpleComplex":
        return SimpleComplex(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def __repr__(self) -> str:
        return (
            f"SimpleComplex("
            f"real={self.real}, "
            f"imaginary={self.imaginary}"
            f")"
        )


complex_one = SimpleComplex(2.0, 3.0)
complex_two = SimpleComplex(4.0, 5.0)

complex_sum = complex_one + complex_two

print(complex_sum)


# =============================================================================
# 43. Money Addition
# =============================================================================

class Money:
    """Represent money with currency-aware addition."""

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Currencies must match.")

        return Money(
            self.amount + other.amount,
            self.currency,
        )

    def __repr__(self) -> str:
        return (
            f"Money("
            f"amount={self.amount}, "
            f"currency={self.currency!r}"
            f")"
        )


money_one = Money(100.0, "USD")
money_two = Money(50.0, "USD")

total_money = money_one + money_two

print(total_money)


# =============================================================================
# 44. Preventing Invalid Operator Usage
# =============================================================================

class TemperatureValue:
    """Represent a temperature that only adds to another temperature."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __add__(self, other: object) -> "TemperatureValue":
        if not isinstance(other, TemperatureValue):
            return NotImplemented

        return TemperatureValue(
            self.value + other.value,
        )

    def __repr__(self) -> str:
        return f"TemperatureValue(value={self.value})"


temperature_one = TemperatureValue(20.0)
temperature_two = TemperatureValue(5.0)

temperature_sum = temperature_one + temperature_two

print(temperature_sum)


# =============================================================================
# 45. Returning NotImplemented
# =============================================================================

class SafeNumber:
    """Demonstrate NotImplemented for unsupported operands."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: object) -> "SafeNumber":
        if not isinstance(other, SafeNumber):
            return NotImplemented

        return SafeNumber(
            self.value + other.value,
        )

    def __repr__(self) -> str:
        return f"SafeNumber(value={self.value})"


safe_one = SafeNumber(10)
safe_two = SafeNumber(20)

safe_sum = safe_one + safe_two

print(safe_sum)


# =============================================================================
# 46. Operator Overloading Should Preserve Meaning
# =============================================================================

class Rectangle:
    """Represent a rectangle that can be added by dimensions."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __add__(self, other: "Rectangle") -> "Rectangle":
        return Rectangle(
            self.width + other.width,
            self.height + other.height,
        )

    def area(self) -> float:
        """Return the rectangle area."""
        return self.width * self.height

    def __repr__(self) -> str:
        return (
            f"Rectangle("
            f"width={self.width}, "
            f"height={self.height}"
            f")"
        )


rectangle_one = Rectangle(10.0, 5.0)
rectangle_two = Rectangle(4.0, 3.0)

combined_rectangle = rectangle_one + rectangle_two

print(combined_rectangle)
print(combined_rectangle.area())


# =============================================================================
# 47. Operator Overloading With Immutable-Style Objects
# =============================================================================

class ImmutablePoint:
    """Return a new point instead of modifying the existing point."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "ImmutablePoint") -> "ImmutablePoint":
        return ImmutablePoint(
            self.x + other.x,
            self.y + other.y,
        )

    def __repr__(self) -> str:
        return (
            f"ImmutablePoint("
            f"x={self.x}, "
            f"y={self.y}"
            f")"
        )


point_one = ImmutablePoint(1.0, 2.0)
point_two = ImmutablePoint(3.0, 4.0)

point_three = point_one + point_two

print(point_one)
print(point_two)
print(point_three)


# =============================================================================
# 48. Operator Overloading With In-Place Mutation
# =============================================================================

class MutableVector:
    """Represent a mutable vector with += support."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __iadd__(self, other: "MutableVector") -> "MutableVector":
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self) -> str:
        return (
            f"MutableVector("
            f"x={self.x}, "
            f"y={self.y}"
            f")"
        )


mutable_vector = MutableVector(1.0, 2.0)
increment_vector = MutableVector(3.0, 4.0)

mutable_vector += increment_vector

print(mutable_vector)


# =============================================================================
# 49. Operator Overloading With Sorting
# =============================================================================

class Student:
    """Represent a student that can be sorted by score."""

    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __lt__(self, other: "Student") -> bool:
        return self.score < other.score

    def __repr__(self) -> str:
        return (
            f"Student("
            f"name={self.name!r}, "
            f"score={self.score}"
            f")"
        )


student_one = Student("Alice", 85)
student_two = Student("Bob", 72)
student_three = Student("Charlie", 95)

students = [
    student_one,
    student_two,
    student_three,
]

sorted_students = sorted(students)

print(sorted_students)


# =============================================================================
# 50. Complete Operator-Overloading Example
# =============================================================================

class Vector2D:
    """
    Complete example demonstrating several overloaded operators.

    Supported operators:

        +
        -
        *
        ==
        <
        len()
        abs()
        str()
        repr()
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Add two vectors."""
        return Vector2D(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """Subtract two vectors."""
        return Vector2D(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, scalar: float) -> "Vector2D":
        """Multiply a vector by a scalar."""
        return Vector2D(
            self.x * scalar,
            self.y * scalar,
        )

    def __rmul__(self, scalar: float) -> "Vector2D":
        """Support scalar multiplication from the left."""
        return self * scalar

    def __eq__(self, other: object) -> bool:
        """Compare two vectors."""
        if not isinstance(other, Vector2D):
            return NotImplemented

        return (
            self.x == other.x
            and self.y == other.y
        )

    def __lt__(self, other: "Vector2D") -> bool:
        """Compare vectors using their magnitude."""
        return abs(self) < abs(other)

    def __len__(self) -> int:
        """Return the number of components."""
        return 2

    def __abs__(self) -> float:
        """Return the vector magnitude."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self) -> str:
        """Return a user-friendly representation."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return (
            f"Vector2D("
            f"x={self.x}, "
            f"y={self.y}"
            f")"
        )


vector_a = Vector2D(3.0, 4.0)
vector_b = Vector2D(1.0, 2.0)

vector_addition = vector_a + vector_b
vector_subtraction = vector_a - vector_b
vector_multiplication = vector_a * 2.0
reverse_multiplication = 2.0 * vector_a
vector_equality = vector_a == vector_b
vector_comparison = vector_b < vector_a
vector_length = len(vector_a)
vector_magnitude = abs(vector_a)
vector_string = str(vector_a)
vector_representation = repr(vector_a)

print(vector_addition)
print(vector_subtraction)
print(vector_multiplication)
print(reverse_multiplication)
print(vector_equality)
print(vector_comparison)
print(vector_length)
print(vector_magnitude)
print(vector_string)
print(vector_representation)


# =============================================================================
# Operator Overloading Reference
# =============================================================================

"""
Common operator-to-method mappings:

Arithmetic:

    a + b
        -> a.__add__(b)

    a - b
        -> a.__sub__(b)

    a * b
        -> a.__mul__(b)

    a / b
        -> a.__truediv__(b)

    a // b
        -> a.__floordiv__(b)

    a % b
        -> a.__mod__(b)

    a ** b
        -> a.__pow__(b)


Comparison:

    a == b
        -> a.__eq__(b)

    a != b
        -> a.__ne__(b)

    a < b
        -> a.__lt__(b)

    a <= b
        -> a.__le__(b)

    a > b
        -> a.__gt__(b)

    a >= b
        -> a.__ge__(b)


Unary:

    -a
        -> a.__neg__()

    +a
        -> a.__pos__()

    abs(a)
        -> a.__abs__()

    bool(a)
        -> a.__bool__()


Container:

    len(a)
        -> a.__len__()

    a[index]
        -> a.__getitem__(index)

    a[index] = value
        -> a.__setitem__(index, value)

    item in a
        -> a.__contains__(item)

    for item in a
        -> a.__iter__()


Callable:

    a(...)
        -> a.__call__()


In-place:

    a += b
        -> a.__iadd__(b)

    a -= b
        -> a.__isub__(b)

    a *= b
        -> a.__imul__(b)

    a /= b
        -> a.__itruediv__(b)


Reflected operators:

    b + a
        -> potentially a.__radd__(b)

    b - a
        -> potentially a.__rsub__(b)

    b * a
        -> potentially a.__rmul__(b)

    b / a
        -> potentially a.__rtruediv__(b)


String representation:

    str(a)
        -> a.__str__()

    repr(a)
        -> a.__repr__()


Hashing:

    hash(a)
        -> a.__hash__()


Core principle:

    operator
        ↓
    special method
        ↓
    custom class behavior


Important design rules:

    1. Overload operators only when the operation has a clear meaning.

    2. Keep operator behavior intuitive.

    3. Return a new object for immutable-style classes.

    4. Use in-place operators such as __iadd__ when mutation is intentional.

    5. Return NotImplemented for unsupported operand types.

    6. Keep equality and hashing consistent.

    7. Avoid surprising meanings for common operators.

    8. Use __repr__ for useful debugging output.

    9. Use __str__ for user-friendly output.

    10. Use @total_ordering carefully when implementing ordered classes.

Core model:

    Python expression
            ↓
    special / dunder method
            ↓
    custom class behavior

Example:

    first + second

becomes conceptually:

    first.__add__(second)

Example:

    first == second

uses:

    first.__eq__(second)

Example:

    -first

uses:

    first.__neg__()

Example:

    len(first)

uses:

    first.__len__()

Example:

    first(value)

uses:

    first.__call__(value)

Operator overloading is therefore the mechanism that allows custom Python
objects to behave naturally with Python's built-in operators.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Operator overloading allows custom classes to define operator behavior.

✓ Python uses special methods to implement overloaded operators.

✓ __add__ implements +.

✓ __sub__ implements -.

✓ __mul__ implements *.

✓ __truediv__ implements /.

✓ __floordiv__ implements //.

✓ __mod__ implements %.

✓ __pow__ implements **.

✓ __eq__ implements ==.

✓ __ne__ implements !=.

✓ __lt__ implements <.

✓ __le__ implements <=.

✓ __gt__ implements >.

✓ __ge__ implements >=.

✓ __neg__ implements unary -.

✓ __pos__ implements unary +.

✓ __abs__ implements abs().

✓ __bool__ controls boolean conversion.

✓ __str__ controls user-friendly string conversion.

✓ __repr__ controls developer-oriented representation.

✓ __len__ implements len().

✓ __getitem__ implements indexing.

✓ __setitem__ implements indexed assignment.

✓ __contains__ implements membership testing.

✓ __iter__ makes an object iterable.

✓ __call__ makes an object callable.

✓ __iadd__ implements +=.

✓ __isub__ implements -=.

✓ __imul__ implements *=.

✓ __itruediv__ implements /=.

✓ Reflected methods such as __radd__ support operations where the custom
  object appears on the right-hand side.

✓ __hash__ controls hashing behavior.

✓ Operator overloading should have an intuitive meaning.

✓ Unsupported operand types should generally return NotImplemented.

✓ Returning NotImplemented allows Python to try the reflected operation
  or eventually raise an appropriate TypeError.

✓ Equality and hashing should be designed consistently.

✓ Operator overloading can make custom classes feel like native Python
  objects.

Core idea:

    CUSTOM CLASS
          ↓
    SPECIAL METHODS
          ↓
    PYTHON OPERATORS
          ↓
    NATURAL OBJECT BEHAVIOR
"""


# =============================================================================
# End of 15_operator_overloading.py
# =============================================================================