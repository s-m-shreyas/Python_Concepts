# type: ignore
# =============================================================================
# 18. Comparison Dunder Methods
# =============================================================================
"""
Python Functions / Operators

File:
18_comparison_dunder_methods.py

Topic:
Comparison Dunder Methods

Overview:
Comparison dunder methods allow custom classes to define how comparison
operators behave.

The main comparison operators are:

    ==      __eq__()
    !=      __ne__()
    <       __lt__()
    <=      __le__()
    >       __gt__()
    >=      __ge__()

Python calls these special methods when comparison operators are used
with objects.

This file covers:

    - What comparison dunder methods are
    - __eq__()
    - __ne__()
    - __lt__()
    - __le__()
    - __gt__()
    - __ge__()
    - Comparison methods with custom classes
    - Comparing attributes
    - Comparing multiple attributes
    - Equality versus identity
    - Returning bool
    - Returning NotImplemented
    - Comparing compatible types
    - Comparing incompatible types
    - Rich comparison methods
    - Reverse comparison behaviour
    - functools.total_ordering
    - Dataclass comparison
    - Sorting custom objects
    - min() and max()
    - Comparing objects by one attribute
    - Comparing objects by multiple attributes
    - Comparison chaining
    - Hashing and equality
    - Mutable objects and equality
    - Good comparison design
    - Common comparison mistakes
"""

# =============================================================================
# 01. Basic Equality With __eq__()
# =============================================================================


class Point:
    """Represent a two-dimensional point."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        """Compare two points by coordinates."""
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y


point_a = Point(10, 20)
point_b = Point(10, 20)
point_c = Point(5, 15)

print(point_a == point_b)
print(point_a == point_c)


# =============================================================================
# 02. Equality Without __eq__()
# =============================================================================
"""
Without implementing __eq__(), custom objects normally compare by identity.

For example:

    object_a == object_b

is normally False when object_a and object_b are different objects.

Two objects can contain identical data while still being different objects.

Implementing __eq__() allows the class to define value-based equality.
"""


class Coordinate:
    """Represent a coordinate without custom equality."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


coordinate_a = Coordinate(1, 2)
coordinate_b = Coordinate(1, 2)

print(coordinate_a == coordinate_b)


# =============================================================================
# 03. Value-Based Equality
# =============================================================================


class User:
    """Represent a user with value-based equality."""

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age

    def __eq__(self, other: object) -> bool:
        """Compare username and age."""
        if not isinstance(other, User):
            return NotImplemented

        return (
            self.username == other.username
            and self.age == other.age
        )


user_a = User("alex", 30)
user_b = User("alex", 30)
user_c = User("sam", 30)

print(user_a == user_b)
print(user_a == user_c)


# =============================================================================
# 04. __ne__() For Not Equal
# =============================================================================


class Product:
    """Represent a product with equality and inequality."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        """Compare products by name and price."""
        if not isinstance(other, Product):
            return NotImplemented

        return (
            self.name == other.name
            and self.price == other.price
        )

    def __ne__(self, other: object) -> bool:
        """Compare products for inequality."""
        result = self.__eq__(other)

        if result is NotImplemented:
            return NotImplemented

        return not result


product_a = Product("Keyboard", 50.0)
product_b = Product("Keyboard", 50.0)
product_c = Product("Mouse", 25.0)

print(product_a != product_b)
print(product_a != product_c)


# =============================================================================
# 05. __lt__() For Less Than
# =============================================================================


class Score:
    """Represent a score."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare scores using less-than."""
        if not isinstance(other, Score):
            return NotImplemented

        return self.value < other.value


score_a = Score(50)
score_b = Score(80)

print(score_a < score_b)
print(score_b < score_a)


# =============================================================================
# 06. __le__() For Less Than Or Equal
# =============================================================================


class Temperature:
    """Represent a temperature."""

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    def __le__(self, other: object) -> bool:
        """Compare temperatures using less-than-or-equal."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.celsius <= other.celsius


temperature_a = Temperature(20.0)
temperature_b = Temperature(20.0)
temperature_c = Temperature(25.0)

print(temperature_a <= temperature_b)
print(temperature_a <= temperature_c)


# =============================================================================
# 07. __gt__() For Greater Than
# =============================================================================


class Priority:
    """Represent a priority value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __gt__(self, other: object) -> bool:
        """Compare priorities using greater-than."""
        if not isinstance(other, Priority):
            return NotImplemented

        return self.value > other.value


priority_a = Priority(10)
priority_b = Priority(5)

print(priority_a > priority_b)
print(priority_b > priority_a)


# =============================================================================
# 08. __ge__() For Greater Than Or Equal
# =============================================================================


class Version:
    """Represent a simple numeric version."""

    def __init__(self, number: int) -> None:
        self.number = number

    def __ge__(self, other: object) -> bool:
        """Compare versions using greater-than-or-equal."""
        if not isinstance(other, Version):
            return NotImplemented

        return self.number >= other.number


version_a = Version(3)
version_b = Version(3)
version_c = Version(2)

print(version_a >= version_b)
print(version_a >= version_c)


# =============================================================================
# 09. All Six Rich Comparison Methods
# =============================================================================


class Number:
    """Represent a number with all rich comparisons."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Implement equality."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        """Implement inequality."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value != other.value

    def __lt__(self, other: object) -> bool:
        """Implement less-than."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value < other.value

    def __le__(self, other: object) -> bool:
        """Implement less-than-or-equal."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value <= other.value

    def __gt__(self, other: object) -> bool:
        """Implement greater-than."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value > other.value

    def __ge__(self, other: object) -> bool:
        """Implement greater-than-or-equal."""
        if not isinstance(other, Number):
            return NotImplemented

        return self.value >= other.value


number_a = Number(10)
number_b = Number(20)

print(number_a == number_b)
print(number_a != number_b)
print(number_a < number_b)
print(number_a <= number_b)
print(number_a > number_b)
print(number_a >= number_b)


# =============================================================================
# 10. __eq__() Can Compare Multiple Attributes
# =============================================================================


class Employee:
    """Represent an employee."""

    def __init__(self, employee_id: int, name: str, department: str) -> None:
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def __eq__(self, other: object) -> bool:
        """Compare all important employee attributes."""
        if not isinstance(other, Employee):
            return NotImplemented

        return (
            self.employee_id == other.employee_id
            and self.name == other.name
            and self.department == other.department
        )


employee_a = Employee(1, "Alex", "Engineering")
employee_b = Employee(1, "Alex", "Engineering")

print(employee_a == employee_b)


# =============================================================================
# 11. Equality Based On One Attribute
# =============================================================================


class Customer:
    """Represent a customer identified by customer ID."""

    def __init__(self, customer_id: int, name: str) -> None:
        self.customer_id = customer_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Compare customers by customer ID."""
        if not isinstance(other, Customer):
            return NotImplemented

        return self.customer_id == other.customer_id


customer_a = Customer(100, "Alex")
customer_b = Customer(100, "Alexander")
customer_c = Customer(200, "Sam")

print(customer_a == customer_b)
print(customer_a == customer_c)


# =============================================================================
# 12. Equality Is Different From Identity
# =============================================================================


class Book:
    """Represent a book."""

    def __init__(self, title: str) -> None:
        self.title = title

    def __eq__(self, other: object) -> bool:
        """Compare books by title."""
        if not isinstance(other, Book):
            return NotImplemented

        return self.title == other.title


book_a = Book("Python")
book_b = Book("Python")
book_c = book_a

print(book_a == book_b)
print(book_a is book_b)
print(book_a is book_c)

"""
Important distinction:

    ==

means:

    "Are these objects equal according to their value?"

while:

    is

means:

    "Are these two names referring to the exact same object?"

__eq__() controls ==.

It does not control is.
"""


# =============================================================================
# 13. Comparing With Another Type
# =============================================================================


class Age:
    """Represent an age."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare Age objects only."""
        if not isinstance(other, Age):
            return NotImplemented

        return self.value == other.value


age = Age(30)

print(age == Age(30))
print(age == Age(40))
print(age == 30)


# =============================================================================
# 14. Why Return NotImplemented?
# =============================================================================
"""
Comparison methods should normally return NotImplemented when the other
operand is of an unsupported type.

Important:

    NotImplemented

is not the same thing as:

    False

Returning NotImplemented tells Python:

    "This class does not know how to compare itself with this type."

Python can then try the reflected operation or apply the appropriate
fallback behavior.
"""


class Measurement:
    """Represent a numeric measurement."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare measurements."""
        if not isinstance(other, Measurement):
            return NotImplemented

        return self.value == other.value


measurement = Measurement(10.0)

print(measurement == Measurement(10.0))
print(measurement == "10")


# =============================================================================
# 15. Returning False For Unsupported Types
# =============================================================================
"""
Returning False can sometimes be appropriate when the semantic design of
the class explicitly says that different types are never equal.

However, for rich comparison methods such as <, <=, >, and >=,
NotImplemented is generally preferable for unsupported types because it
allows Python to handle the comparison correctly.
"""


class Identifier:
    """Represent an identifier."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Return False for unrelated types."""
        if not isinstance(other, Identifier):
            return False

        return self.value == other.value


identifier = Identifier(10)

print(identifier == Identifier(10))
print(identifier == "10")


# =============================================================================
# 16. Comparison By Name
# =============================================================================


class Student:
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __lt__(self, other: object) -> bool:
        """Sort students alphabetically by name."""
        if not isinstance(other, Student):
            return NotImplemented

        return self.name < other.name


student_a = Student("Alex")
student_b = Student("Brian")

print(student_a < student_b)


# =============================================================================
# 17. Comparison By Numeric Attribute
# =============================================================================


class Player:
    """Represent a player with a score."""

    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __lt__(self, other: object) -> bool:
        """Sort players by score."""
        if not isinstance(other, Player):
            return NotImplemented

        return self.score < other.score


player_a = Player("Alex", 80)
player_b = Player("Sam", 95)

print(player_a < player_b)


# =============================================================================
# 18. Sorting Objects With __lt__()
# =============================================================================


class Task:
    """Represent a task with a priority."""

    def __init__(self, name: str, priority: int) -> None:
        self.name = name
        self.priority = priority

    def __lt__(self, other: object) -> bool:
        """Sort tasks by priority."""
        if not isinstance(other, Task):
            return NotImplemented

        return self.priority < other.priority


tasks = [
    Task("Database", 3),
    Task("API", 1),
    Task("Testing", 2),
]

sorted_tasks = sorted(tasks)

for task in sorted_tasks:
    print(task.name, task.priority)


# =============================================================================
# 19. max() Uses Comparison Behaviour
# =============================================================================


class TemperatureReading:
    """Represent a temperature reading."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare temperature readings."""
        if not isinstance(other, TemperatureReading):
            return NotImplemented

        return self.value < other.value


readings = [
    TemperatureReading(18.5),
    TemperatureReading(25.0),
    TemperatureReading(21.5),
]

highest_reading = max(readings)

print(highest_reading.value)


# =============================================================================
# 20. min() Uses Comparison Behaviour
# =============================================================================


class Price:
    """Represent a price."""

    def __init__(self, value: float) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare prices."""
        if not isinstance(other, Price):
            return NotImplemented

        return self.value < other.value


prices = [
    Price(100.0),
    Price(50.0),
    Price(75.0),
]

lowest_price = min(prices)

print(lowest_price.value)


# =============================================================================
# 21. Comparison By Multiple Attributes
# =============================================================================


class StudentRecord:
    """Represent a student record."""

    def __init__(self, grade: int, name: str) -> None:
        self.grade = grade
        self.name = name

    def __lt__(self, other: object) -> bool:
        """Compare grade first, then name."""
        if not isinstance(other, StudentRecord):
            return NotImplemented

        return (self.grade, self.name) < (other.grade, other.name)


student_record_a = StudentRecord(90, "Alex")
student_record_b = StudentRecord(90, "Brian")
student_record_c = StudentRecord(85, "Sam")

print(student_record_a < student_record_b)
print(student_record_a < student_record_c)


# =============================================================================
# 22. Tuple Comparison Inside Dunder Methods
# =============================================================================


class VersionNumber:
    """Represent a semantic-style numeric version."""

    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def __lt__(self, other: object) -> bool:
        """Compare versions using tuple ordering."""
        if not isinstance(other, VersionNumber):
            return NotImplemented

        return (
            self.major,
            self.minor,
            self.patch,
        ) < (
            other.major,
            other.minor,
            other.patch,
        )


version_a = VersionNumber(2, 5, 1)
version_b = VersionNumber(2, 6, 0)

print(version_a < version_b)


# =============================================================================
# 23. Equality Using a Tuple
# =============================================================================


class Address:
    """Represent an address."""

    def __init__(
        self,
        city: str,
        state: str,
        postal_code: str,
    ) -> None:
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def __eq__(self, other: object) -> bool:
        """Compare all address components."""
        if not isinstance(other, Address):
            return NotImplemented

        return (
            self.city,
            self.state,
            self.postal_code,
        ) == (
            other.city,
            other.state,
            other.postal_code,
        )


address_a = Address("Bengaluru", "Karnataka", "560001")
address_b = Address("Bengaluru", "Karnataka", "560001")

print(address_a == address_b)


# =============================================================================
# 24. Comparison Chaining
# =============================================================================


class Rating:
    """Represent a rating."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare ratings."""
        if not isinstance(other, Rating):
            return NotImplemented

        return self.value < other.value


rating_a = Rating(3)
rating_b = Rating(4)
rating_c = Rating(5)

print(rating_a < rating_b < rating_c)


# =============================================================================
# 25. Equality With None
# =============================================================================


class Token:
    """Represent a token."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare tokens."""
        if not isinstance(other, Token):
            return NotImplemented

        return self.value == other.value


token = Token("abc")

print(token == Token("abc"))
print(token is None)
print(token == None)


# =============================================================================
# 26. Prefer is None Over == None
# =============================================================================
"""
When checking specifically for None, use:

    value is None

rather than:

    value == None

The identity operator is the correct semantic tool for checking whether
a value is the singleton None object.
"""


class OptionalValue:
    """Represent an optional value."""

    def __init__(self, value: str | None) -> None:
        self.value = value

    def is_empty(self) -> bool:
        """Check whether the stored value is None."""
        return self.value is None


optional_value = OptionalValue(None)

print(optional_value.is_empty())


# =============================================================================
# 27. Comparing With Subclasses
# =============================================================================


class Animal:
    """Represent an animal."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Compare animals by name."""
        if not isinstance(other, Animal):
            return NotImplemented

        return self.name == other.name


class Dog(Animal):
    """Represent a dog."""


animal = Animal("Buddy")
dog = Dog("Buddy")

print(animal == dog)
print(dog == animal)


# =============================================================================
# 28. Strict Type Equality
# =============================================================================
"""
Sometimes a class should only consider objects of exactly the same type
to be equal.

In that situation, type(self) can be compared with type(other).
"""


class StrictValue:
    """Represent a value requiring exact type equality."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Require the exact same class."""
        if type(self) is not type(other):
            return NotImplemented

        if not isinstance(other, StrictValue):
            return NotImplemented

        return self.value == other.value


strict_a = StrictValue(10)
strict_b = StrictValue(10)

print(strict_a == strict_b)


# =============================================================================
# 29. functools.total_ordering
# =============================================================================
"""
functools.total_ordering can generate the remaining ordering methods when
a class provides __eq__() and one ordering method such as __lt__().

This can reduce boilerplate.

The trade-off is that explicitly implementing all required comparison
methods can sometimes be clearer and faster.
"""

from functools import total_ordering


@total_ordering
class RankedItem:
    """Represent an item with an integer rank."""

    def __init__(self, rank: int) -> None:
        self.rank = rank

    def __eq__(self, other: object) -> bool:
        """Compare ranks for equality."""
        if not isinstance(other, RankedItem):
            return NotImplemented

        return self.rank == other.rank

    def __lt__(self, other: object) -> bool:
        """Compare ranks using less-than."""
        if not isinstance(other, RankedItem):
            return NotImplemented

        return self.rank < other.rank


ranked_a = RankedItem(10)
ranked_b = RankedItem(20)

print(ranked_a == ranked_b)
print(ranked_a != ranked_b)
print(ranked_a < ranked_b)
print(ranked_a <= ranked_b)
print(ranked_a > ranked_b)
print(ranked_a >= ranked_b)


# =============================================================================
# 30. total_ordering With Sorting
# =============================================================================


@total_ordering
class ScoreRecord:
    """Represent a sortable score."""

    def __init__(self, score: int) -> None:
        self.score = score

    def __eq__(self, other: object) -> bool:
        """Compare scores for equality."""
        if not isinstance(other, ScoreRecord):
            return NotImplemented

        return self.score == other.score

    def __lt__(self, other: object) -> bool:
        """Compare scores."""
        if not isinstance(other, ScoreRecord):
            return NotImplemented

        return self.score < other.score


score_records = [
    ScoreRecord(90),
    ScoreRecord(70),
    ScoreRecord(80),
]

sorted_scores = sorted(score_records)

for score_record in sorted_scores:
    print(score_record.score)


# =============================================================================
# 31. Dataclass Equality
# =============================================================================
"""
dataclasses can automatically provide equality behaviour.

When eq=True, the generated __eq__() compares the relevant fields.

This is useful when the class primarily represents data.
"""

from dataclasses import dataclass


@dataclass
class CoordinateRecord:
    """Represent a coordinate using dataclass equality."""

    x: int
    y: int


coordinate_record_a = CoordinateRecord(10, 20)
coordinate_record_b = CoordinateRecord(10, 20)

print(coordinate_record_a == coordinate_record_b)


# =============================================================================
# 32. Dataclass Ordering
# =============================================================================
"""
A dataclass can also generate ordering methods when:

    order=True

is supplied.

The fields are compared in declaration order.
"""


@dataclass(order=True)
class RankedRecord:
    """Represent a sortable ranked record."""

    rank: int
    name: str


ranked_record_a = RankedRecord(1, "Alex")
ranked_record_b = RankedRecord(2, "Sam")

print(ranked_record_a < ranked_record_b)
print(ranked_record_a <= ranked_record_b)
print(ranked_record_a > ranked_record_b)
print(ranked_record_a >= ranked_record_b)


# =============================================================================
# 33. Dataclass Multiple-Field Ordering
# =============================================================================


@dataclass(order=True)
class EmployeeRecord:
    """Represent an employee ordered by department and name."""

    department: str
    name: str


employee_record_a = EmployeeRecord("Engineering", "Alex")
employee_record_b = EmployeeRecord("Engineering", "Brian")

print(employee_record_a < employee_record_b)


# =============================================================================
# 34. Excluding Fields From Comparison
# =============================================================================
"""
A dataclass field can be excluded from comparisons using:

    compare=False

This is useful when a field should exist on the object but should not
participate in equality or ordering.
"""


@dataclass(order=True)
class TaskRecord:
    """Represent a task with a non-comparison identifier."""

    priority: int
    name: str
    internal_id: int = 0


task_record_a = TaskRecord(1, "API", 100)
task_record_b = TaskRecord(1, "API", 200)

print(task_record_a == task_record_b)


# =============================================================================
# 35. Equality and Mutable State
# =============================================================================


class MutableProfile:
    """Represent a mutable profile."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other: object) -> bool:
        """Compare current profile state."""
        if not isinstance(other, MutableProfile):
            return NotImplemented

        return (
            self.name == other.name
            and self.age == other.age
        )


profile_a = MutableProfile("Alex", 30)
profile_b = MutableProfile("Alex", 30)

print(profile_a == profile_b)

profile_b.age = 31

print(profile_a == profile_b)


# =============================================================================
# 36. Equality Should Usually Be Consistent
# =============================================================================
"""
A useful equality relationship should generally be:

    a == a

and should behave consistently for equivalent objects.

For ordinary value objects, equality should normally be:

    reflexive
    symmetric
    transitive

Example:

    a == b
    b == a

should normally produce the same result.
"""


class Value:
    """Represent a simple value."""

    def __init__(self, number: int) -> None:
        self.number = number

    def __eq__(self, other: object) -> bool:
        """Compare values."""
        if not isinstance(other, Value):
            return NotImplemented

        return self.number == other.number


value_a = Value(10)
value_b = Value(10)

print(value_a == value_b)
print(value_b == value_a)


# =============================================================================
# 37. Comparison Should Represent Natural Meaning
# =============================================================================
"""
Operator overloading should have a clear semantic meaning.

Good:

    price_a < price_b
    date_a < date_b
    version_a < version_b
    point_a == point_b

Avoid giving comparison operators surprising meanings that do not match
the domain.
"""


class Money:
    """Represent money."""

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __lt__(self, other: object) -> bool:
        """Compare monetary amounts."""
        if not isinstance(other, Money):
            return NotImplemented

        return self.amount < other.amount


money_a = Money(100.0)
money_b = Money(150.0)

print(money_a < money_b)


# =============================================================================
# 38. Sorting Descending
# =============================================================================


class Rank:
    """Represent a rank."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare ranks."""
        if not isinstance(other, Rank):
            return NotImplemented

        return self.value < other.value


ranks = [
    Rank(10),
    Rank(30),
    Rank(20),
]

descending_ranks = sorted(
    ranks,
    reverse=True,
)

for rank in descending_ranks:
    print(rank.value)


# =============================================================================
# 39. Equality In Collections
# =============================================================================


class Tag:
    """Represent a tag."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Compare tags by name."""
        if not isinstance(other, Tag):
            return NotImplemented

        return self.name == other.name


tags = [
    Tag("python"),
    Tag("sql"),
    Tag("linux"),
]

target_tag = Tag("python")

print(target_tag in tags)


# =============================================================================
# 40. Equality And List Membership
# =============================================================================


class ProductCode:
    """Represent a product code."""

    def __init__(self, code: str) -> None:
        self.code = code

    def __eq__(self, other: object) -> bool:
        """Compare product codes."""
        if not isinstance(other, ProductCode):
            return NotImplemented

        return self.code == other.code


product_codes = [
    ProductCode("A100"),
    ProductCode("B200"),
]

search_code = ProductCode("B200")

print(search_code in product_codes)


# =============================================================================
# 41. Comparison With Strings
# =============================================================================


class Username:
    """Represent a username."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare usernames alphabetically."""
        if not isinstance(other, Username):
            return NotImplemented

        return self.value < other.value


username_a = Username("alex")
username_b = Username("sam")

print(username_a < username_b)


# =============================================================================
# 42. Comparing Case-Insensitive Values
# =============================================================================


class CaseInsensitiveName:
    """Represent a case-insensitive name."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare names without considering case."""
        if not isinstance(other, CaseInsensitiveName):
            return NotImplemented

        return self.value.casefold() == other.value.casefold()


name_a = CaseInsensitiveName("Python")
name_b = CaseInsensitiveName("PYTHON")

print(name_a == name_b)


# =============================================================================
# 43. Comparing Normalized Values
# =============================================================================


class EmailAddress:
    """Represent an email address."""

    def __init__(self, address: str) -> None:
        self.address = address

    def __eq__(self, other: object) -> bool:
        """Compare normalized email addresses."""
        if not isinstance(other, EmailAddress):
            return NotImplemented

        return (
            self.address.strip().casefold()
            == other.address.strip().casefold()
        )


email_a = EmailAddress("  Alex@example.com")
email_b = EmailAddress("alex@example.com")

print(email_a == email_b)


# =============================================================================
# 44. __ne__() And Equality
# =============================================================================
"""
Python can often derive != behaviour from ==.

For a straightforward value object, implementing __eq__() is frequently
enough.

Implement __ne__() explicitly when the class has a specific reason to
define inequality independently.
"""


class SimpleValue:
    """Represent a simple comparable value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare values."""
        if not isinstance(other, SimpleValue):
            return NotImplemented

        return self.value == other.value


simple_a = SimpleValue(10)
simple_b = SimpleValue(20)

print(simple_a == simple_b)
print(simple_a != simple_b)


# =============================================================================
# 45. Reflected Comparison Behaviour
# =============================================================================
"""
Rich comparisons have reflected counterparts conceptually.

For example:

    a < b

can involve:

    a.__lt__(b)

while Python may consider the reflected operation on b when appropriate.

For comparisons, the reflected relationship is not expressed using names
such as __rlt__(). Instead, Python uses the corresponding opposite
comparison method.

Examples:

    a < b
    b > a

    a <= b
    b >= a

    a > b
    b < a

    a >= b
    b <= a
"""


class ComparableNumber:
    """Represent a number with less-than comparison."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare numbers."""
        if not isinstance(other, ComparableNumber):
            return NotImplemented

        return self.value < other.value


comparable_a = ComparableNumber(10)
comparable_b = ComparableNumber(20)

print(comparable_a < comparable_b)
print(comparable_b > comparable_a)


# =============================================================================
# 46. Comparison And NotImplemented
# =============================================================================


class TemperatureValue:
    """Represent a temperature value."""

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    def __lt__(self, other: object) -> bool:
        """Compare temperature values."""
        if not isinstance(other, TemperatureValue):
            return NotImplemented

        return self.celsius < other.celsius


temperature_value = TemperatureValue(25.0)

print(temperature_value < TemperatureValue(30.0))


# =============================================================================
# 47. Unsupported Ordering
# =============================================================================
"""
If two unrelated custom classes do not support an ordering operation,
Python can raise TypeError.

This is preferable to silently pretending that unrelated objects have
a meaningful ordering.
"""


class FirstType:
    """First unrelated type."""


class SecondType:
    """Second unrelated type."""


first_object = FirstType()
second_object = SecondType()

try:
    print(first_object < second_object)
except TypeError as error:
    print(type(error).__name__)


# =============================================================================
# 48. Equality Usually Does Not Raise For Unrelated Types
# =============================================================================
"""
Equality comparisons commonly produce False for unrelated objects after
the comparison methods return NotImplemented.

Ordering comparisons generally require a meaningful ordering relationship.
"""


class EqualityValue:
    """Represent a value for equality comparison."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare only with EqualityValue."""
        if not isinstance(other, EqualityValue):
            return NotImplemented

        return self.value == other.value


equality_value = EqualityValue(10)

print(equality_value == 10)
print(equality_value == "10")


# =============================================================================
# 49. Comparison Methods Should Return Boolean Results
# =============================================================================
"""
Comparison methods are normally expected to produce a truth value.

For example:

    __eq__() -> bool
    __lt__() -> bool
    __le__() -> bool
    __gt__() -> bool
    __ge__() -> bool

The exception is that NotImplemented can be returned when the operand
type is unsupported.
"""


class BooleanComparison:
    """Represent a boolean-comparable value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __lt__(self, other: object) -> bool:
        """Compare values."""
        if not isinstance(other, BooleanComparison):
            return NotImplemented

        return self.value < other.value


boolean_a = BooleanComparison(1)
boolean_b = BooleanComparison(2)

comparison_result: bool = boolean_a < boolean_b

print(comparison_result)


# =============================================================================
# 50. Complete Comparison Example
# =============================================================================


class Invoice:
    """
    Represent an invoice with value-based equality and ordering.

    Invoices are compared by total amount and then invoice number.
    """

    def __init__(
        self,
        invoice_number: str,
        total: float,
    ) -> None:
        self.invoice_number = invoice_number
        self.total = total

    def _comparison_key(self) -> tuple[float, str]:
        """Return the values used for comparison."""
        return (
            self.total,
            self.invoice_number,
        )

    def __eq__(self, other: object) -> bool:
        """Compare invoices for equality."""
        if not isinstance(other, Invoice):
            return NotImplemented

        return self._comparison_key() == other._comparison_key()

    def __lt__(self, other: object) -> bool:
        """Compare invoices for ordering."""
        if not isinstance(other, Invoice):
            return NotImplemented

        return self._comparison_key() < other._comparison_key()


invoice_a = Invoice("INV-001", 1000.0)
invoice_b = Invoice("INV-002", 1500.0)
invoice_c = Invoice("INV-003", 1000.0)

print(invoice_a == invoice_b)
print(invoice_a == invoice_c)
print(invoice_a < invoice_b)
print(invoice_b > invoice_a)
print(invoice_a <= invoice_c)
print(invoice_b >= invoice_a)

invoices = [
    invoice_b,
    invoice_c,
    invoice_a,
]

sorted_invoices = sorted(invoices)

for invoice in sorted_invoices:
    print(
        invoice.invoice_number,
        invoice.total,
    )


# =============================================================================
# 51. Comparison Dunder Method Mapping
# =============================================================================
"""
The primary rich comparison methods are:

    Operator       Dunder method

    ==             __eq__()
    !=             __ne__()
    <              __lt__()
    <=             __le__()
    >              __gt__()
    >=             __ge__()

Example:

    object_a == object_b

conceptually invokes:

    object_a.__eq__(object_b)

Likewise:

    object_a < object_b

uses:

    object_a.__lt__(object_b)

These methods are called automatically by Python when the corresponding
operators are used.
"""


# =============================================================================
# 52. Equality Versus Ordering
# =============================================================================
"""
Equality answers:

    "Are these objects equivalent?"

Ordering answers:

    "Which object comes before the other?"

Examples:

    a == b

means:

    a and b represent the same value.

While:

    a < b

means:

    a comes before b according to the class's ordering rule.

A class may support equality without supporting ordering.
"""


class EqualityOnly:
    """Represent an object that supports equality only."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare values."""
        if not isinstance(other, EqualityOnly):
            return NotImplemented

        return self.value == other.value


equality_only_a = EqualityOnly(10)
equality_only_b = EqualityOnly(20)

print(equality_only_a == equality_only_b)

try:
    print(equality_only_a < equality_only_b)
except TypeError as error:
    print(type(error).__name__)


# =============================================================================
# 53. Comparison Design With a Private Key
# =============================================================================
"""
A useful pattern is to centralize comparison data in a helper method.

Example:

    def _comparison_key(self) -> tuple[...]:
        return (...)

Then comparison methods can use:

    self._comparison_key()

This reduces duplicated comparison logic.
"""


class Person:
    """Represent a person ordered by age and name."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def _comparison_key(self) -> tuple[int, str]:
        """Return the comparison key."""
        return (
            self.age,
            self.name,
        )

    def __eq__(self, other: object) -> bool:
        """Compare people."""
        if not isinstance(other, Person):
            return NotImplemented

        return self._comparison_key() == other._comparison_key()

    def __lt__(self, other: object) -> bool:
        """Order people by age and name."""
        if not isinstance(other, Person):
            return NotImplemented

        return self._comparison_key() < other._comparison_key()


person_a = Person("Alex", 30)
person_b = Person("Sam", 35)

print(person_a == person_b)
print(person_a < person_b)


# =============================================================================
# 54. Comparison With Computed Values
# =============================================================================


class Rectangle:
    """Represent a rectangle ordered by area."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def _area(self) -> float:
        """Calculate rectangle area."""
        return self.width * self.height

    def __lt__(self, other: object) -> bool:
        """Compare rectangles by area."""
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self._area() < other._area()

    def __eq__(self, other: object) -> bool:
        """Compare rectangles by area."""
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self._area() == other._area()


rectangle_a = Rectangle(10.0, 20.0)
rectangle_b = Rectangle(5.0, 50.0)

print(rectangle_a == rectangle_b)
print(rectangle_a < rectangle_b)


# =============================================================================
# 55. Comparison With Explicit Ordering Semantics
# =============================================================================


class PriorityTask:
    """Represent a task ordered by priority."""

    def __init__(self, name: str, priority: int) -> None:
        self.name = name
        self.priority = priority

    def __eq__(self, other: object) -> bool:
        """Compare tasks by priority."""
        if not isinstance(other, PriorityTask):
            return NotImplemented

        return self.priority == other.priority

    def __lt__(self, other: object) -> bool:
        """Place lower priority values first."""
        if not isinstance(other, PriorityTask):
            return NotImplemented

        return self.priority < other.priority


priority_tasks = [
    PriorityTask("Database", 3),
    PriorityTask("Authentication", 1),
    PriorityTask("Testing", 2),
]

for task in sorted(priority_tasks):
    print(task.name, task.priority)


# =============================================================================
# 56. Important Rules
# =============================================================================
"""
Important comparison dunder-method rules:

1. __eq__() implements ==.

2. __ne__() implements !=.

3. __lt__() implements <.

4. __le__() implements <=.

5. __gt__() implements >.

6. __ge__() implements >=.

7. Comparison methods are called automatically by comparison operators.

8. __eq__() usually compares meaningful object state.

9. __lt__() should represent a natural ordering when possible.

10. Return NotImplemented for unsupported operand types.

11. NotImplemented is different from False.

12. == tests equality.

13. is tests object identity.

14. Sorting commonly relies on __lt__().

15. min() and max() rely on ordering comparisons.

16. list membership uses equality semantics.

17. functools.total_ordering can generate missing ordering methods.

18. dataclasses can automatically generate comparison methods.

19. Comparison should be predictable and consistent.

20. Operator overloading should reflect the natural meaning of the
    operator.

21. Equality does not automatically mean objects are identical.

22. A class can support equality without supporting ordering.

23. A class should not invent surprising meanings for comparison operators.

24. A comparison method may return NotImplemented so Python can attempt
    another comparison strategy.

25. Comparison methods are also called rich comparison methods.
"""


# =============================================================================
# 57. Core Mental Model
# =============================================================================
"""
When Python evaluates:

    first == second

Python uses rich comparison machinery involving:

    __eq__()

When Python evaluates:

    first < second

Python uses:

    __lt__()

When Python evaluates:

    first <= second

Python uses:

    __le__()

When Python evaluates:

    first > second

Python uses:

    __gt__()

When Python evaluates:

    first >= second

Python uses:

    __ge__()

When Python evaluates:

    first != second

Python uses:

    __ne__()

Therefore:

    comparison operator
            |
            v
    comparison dunder method
            |
            v
    custom comparison behaviour
"""


# =============================================================================
# 58. Final Example: Comparable Domain Object
# =============================================================================


class BankAccount:
    """
    Represent a bank account.

    Accounts are considered equal when they have the same account number.
    Accounts are ordered by balance.
    """

    def __init__(
        self,
        account_number: str,
        balance: float,
    ) -> None:
        self.account_number = account_number
        self.balance = balance

    def __eq__(self, other: object) -> bool:
        """Compare accounts by account number."""
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.account_number == other.account_number

    def __lt__(self, other: object) -> bool:
        """Order accounts by balance."""
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.balance < other.balance


account_a = BankAccount("ACC-001", 5000.0)
account_b = BankAccount("ACC-002", 7500.0)
account_c = BankAccount("ACC-001", 9000.0)

print(account_a == account_c)
print(account_a == account_b)
print(account_a < account_b)
print(account_b > account_a)

accounts = [
    account_b,
    account_a,
    account_c,
]

for account in sorted(accounts):
    print(
        account.account_number,
        account.balance,
    )


# =============================================================================
# Key Takeaways
# =============================================================================
"""
Comparison dunder methods allow custom objects to participate naturally
in Python comparisons.

Core mapping:

    ==      -> __eq__()
    !=      -> __ne__()
    <       -> __lt__()
    <=      -> __le__()
    >       -> __gt__()
    >=      -> __ge__()

The most important pattern is:

    def __eq__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, MyClass):
            return NotImplemented

        return self.value == other.value

For ordering:

    def __lt__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, MyClass):
            return NotImplemented

        return self.value < other.value

Remember:

    ==

means equality.

    is

means identity.

    NotImplemented

means:

    "This comparison method does not support this operand type."

Comparison dunder methods are useful when objects have a natural concept
of equality or ordering.

Good examples include:

    - numbers
    - prices
    - dates
    - versions
    - coordinates
    - rankings
    - measurements
    - domain records
    - tasks
    - database entities

Avoid operator overloading when the comparison has no clear or natural
meaning.

The goal is not merely to make:

    object_a < object_b

possible.

The goal is to make it meaningful, predictable, and consistent with what
a Python programmer would naturally expect.
"""


# =============================================================================
# End of 18_comparison_dunder_methods.py
# =============================================================================