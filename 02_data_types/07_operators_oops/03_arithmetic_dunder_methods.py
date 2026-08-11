# type: ignore

# =============================================================================
# 17. Arithmetic Dunder Methods
# =============================================================================
"""
Python Operators

File:
17_arithmetic_dunder_methods.py

Topic:
Arithmetic Dunder Methods

Overview:
Arithmetic dunder methods are special methods that allow classes to define
their behaviour when arithmetic operators are used with their objects.

Common arithmetic dunder methods:

    __add__       +
    __sub__       -
    __mul__       *
    __truediv__   /
    __floordiv__  //
    __mod__       %
    __pow__       **
    __neg__       -
    __pos__       +
    __abs__       abs()

Reverse arithmetic methods:

    __radd__      +
    __rsub__      -
    __rmul__      *
    __rtruediv__  /
    __rfloordiv__ //
    __rmod__      %
    __rpow__      **

In-place arithmetic methods:

    __iadd__      +=
    __isub__      -=
    __imul__      *=
    __itruediv__  /=
    __ifloordiv__ //=
    __imod__      %=
    __ipow__      **=

These methods allow custom objects to participate naturally in arithmetic
expressions.

The examples below use simple, typed classes and avoid intentionally invalid
code so the complete file can be checked with mypy or Pylance.
"""

from __future__ import annotations

from typing import Self


# =============================================================================
# 01. Basic __add__
# =============================================================================

class Number:
    """Represent a simple numeric value."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: Number) -> Number:
        """Add two Number objects."""
        return Number(self.value + other.value)

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"Number({self.value})"


number_a: Number = Number(10)
number_b: Number = Number(20)

number_sum: Number = number_a + number_b

print(number_sum)


# =============================================================================
# 02. Basic __sub__
# =============================================================================

class SubtractableNumber:
    """Represent a number supporting subtraction."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __sub__(self, other: SubtractableNumber) -> SubtractableNumber:
        """Subtract another object."""
        return SubtractableNumber(self.value - other.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"SubtractableNumber({self.value})"


subtract_a: SubtractableNumber = SubtractableNumber(50)
subtract_b: SubtractableNumber = SubtractableNumber(20)

subtract_result: SubtractableNumber = subtract_a - subtract_b

print(subtract_result)


# =============================================================================
# 03. Basic __mul__
# =============================================================================

class MultipliableNumber:
    """Represent a number supporting multiplication."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mul__(
        self,
        other: MultipliableNumber,
    ) -> MultipliableNumber:
        """Multiply two objects."""
        return MultipliableNumber(self.value * other.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"MultipliableNumber({self.value})"


multiply_a: MultipliableNumber = MultipliableNumber(6)
multiply_b: MultipliableNumber = MultipliableNumber(7)

multiply_result: MultipliableNumber = multiply_a * multiply_b

print(multiply_result)


# =============================================================================
# 04. Basic __truediv__
# =============================================================================

class DivisibleNumber:
    """Represent a number supporting true division."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __truediv__(
        self,
        other: DivisibleNumber,
    ) -> DivisibleNumber:
        """Divide two objects."""
        return DivisibleNumber(self.value / other.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"DivisibleNumber({self.value})"


divide_a: DivisibleNumber = DivisibleNumber(20.0)
divide_b: DivisibleNumber = DivisibleNumber(5.0)

divide_result: DivisibleNumber = divide_a / divide_b

print(divide_result)


# =============================================================================
# 05. Basic __floordiv__
# =============================================================================

class FloorDivisibleNumber:
    """Represent a number supporting floor division."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __floordiv__(
        self,
        other: FloorDivisibleNumber,
    ) -> FloorDivisibleNumber:
        """Perform floor division."""
        return FloorDivisibleNumber(self.value // other.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"FloorDivisibleNumber({self.value})"


floor_a: FloorDivisibleNumber = FloorDivisibleNumber(17)
floor_b: FloorDivisibleNumber = FloorDivisibleNumber(5)

floor_result: FloorDivisibleNumber = floor_a // floor_b

print(floor_result)


# =============================================================================
# 06. Basic __mod__
# =============================================================================

class ModuloNumber:
    """Represent a number supporting modulo."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mod__(
        self,
        other: ModuloNumber,
    ) -> ModuloNumber:
        """Calculate the remainder."""
        return ModuloNumber(self.value % other.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"ModuloNumber({self.value})"


modulo_a: ModuloNumber = ModuloNumber(17)
modulo_b: ModuloNumber = ModuloNumber(5)

modulo_result: ModuloNumber = modulo_a % modulo_b

print(modulo_result)


# =============================================================================
# 07. Basic __pow__
# =============================================================================

class PowerNumber:
    """Represent a number supporting exponentiation."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __pow__(
        self,
        exponent: PowerNumber,
    ) -> PowerNumber:
        """Raise the value to an exponent."""
        return PowerNumber(self.value**exponent.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"PowerNumber({self.value})"


power_base: PowerNumber = PowerNumber(2)
power_exponent: PowerNumber = PowerNumber(5)

power_result: PowerNumber = power_base**power_exponent

print(power_result)


# =============================================================================
# 08. __neg__
# =============================================================================

class SignedNumber:
    """Represent a number supporting unary negation."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __neg__(self) -> SignedNumber:
        """Return the negative value."""
        return SignedNumber(-self.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"SignedNumber({self.value})"


positive_number: SignedNumber = SignedNumber(25)
negative_number: SignedNumber = -positive_number

print(negative_number)


# =============================================================================
# 09. __pos__
# =============================================================================

class PositiveNumber:
    """Represent a number supporting unary plus."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __pos__(self) -> PositiveNumber:
        """Return the positive form."""
        return PositiveNumber(+self.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"PositiveNumber({self.value})"


number_for_positive: PositiveNumber = PositiveNumber(30)
positive_result: PositiveNumber = +number_for_positive

print(positive_result)


# =============================================================================
# 10. __abs__
# =============================================================================

class AbsoluteNumber:
    """Represent a number supporting abs()."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __abs__(self) -> int:
        """Return the absolute value."""
        return abs(self.value)

    def __repr__(self) -> str:
        """Return a readable representation."""
        return f"AbsoluteNumber({self.value})"


absolute_number: AbsoluteNumber = AbsoluteNumber(-42)

absolute_result: int = abs(absolute_number)

print(absolute_result)


# =============================================================================
# 11. Multiple Arithmetic Methods
# =============================================================================

class CalculatorValue:
    """Represent a value supporting multiple arithmetic operations."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: CalculatorValue) -> CalculatorValue:
        return CalculatorValue(self.value + other.value)

    def __sub__(self, other: CalculatorValue) -> CalculatorValue:
        return CalculatorValue(self.value - other.value)

    def __mul__(self, other: CalculatorValue) -> CalculatorValue:
        return CalculatorValue(self.value * other.value)

    def __truediv__(self, other: CalculatorValue) -> CalculatorValue:
        return CalculatorValue(self.value / other.value)

    def __repr__(self) -> str:
        return f"CalculatorValue({self.value})"


calculator_left: CalculatorValue = CalculatorValue(20.0)
calculator_right: CalculatorValue = CalculatorValue(5.0)

print(calculator_left + calculator_right)
print(calculator_left - calculator_right)
print(calculator_left * calculator_right)
print(calculator_left / calculator_right)


# =============================================================================
# 12. Arithmetic Methods With Self
# =============================================================================

class Temperature:
    """Represent a temperature in degrees Celsius."""

    def __init__(self, celsius: float) -> None:
        self.celsius: float = celsius

    def __add__(self, other: Temperature) -> Temperature:
        """Add two temperatures."""
        return Temperature(self.celsius + other.celsius)

    def __repr__(self) -> str:
        return f"Temperature({self.celsius}°C)"


temperature_a: Temperature = Temperature(20.0)
temperature_b: Temperature = Temperature(5.0)

temperature_sum: Temperature = temperature_a + temperature_b

print(temperature_sum)


# =============================================================================
# 13. Arithmetic With an Integer Field
# =============================================================================

class Score:
    """Represent a game score."""

    def __init__(self, points: int) -> None:
        self.points: int = points

    def __add__(self, other: Score) -> Score:
        """Combine scores."""
        return Score(self.points + other.points)

    def __repr__(self) -> str:
        return f"Score({self.points})"


team_a_score: Score = Score(80)
team_b_score: Score = Score(75)

combined_score: Score = team_a_score + team_b_score

print(combined_score)


# =============================================================================
# 14. Arithmetic With Floats
# =============================================================================

class Money:
    """Represent a monetary value."""

    def __init__(self, amount: float) -> None:
        self.amount: float = amount

    def __add__(self, other: Money) -> Money:
        """Add two monetary values."""
        return Money(self.amount + other.amount)

    def __sub__(self, other: Money) -> Money:
        """Subtract two monetary values."""
        return Money(self.amount - other.amount)

    def __repr__(self) -> str:
        return f"Money({self.amount:.2f})"


price_a: Money = Money(100.50)
price_b: Money = Money(25.25)

total_price: Money = price_a + price_b
remaining_price: Money = price_a - price_b

print(total_price)
print(remaining_price)


# =============================================================================
# 15. Arithmetic Method Returning Self
# =============================================================================

class CounterValue:
    """Represent a counter value."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: CounterValue) -> CounterValue:
        """Return a new CounterValue."""
        return CounterValue(self.value + other.value)

    def __repr__(self) -> str:
        return f"CounterValue({self.value})"


counter_one: CounterValue = CounterValue(10)
counter_two: CounterValue = CounterValue(15)

counter_total: CounterValue = counter_one + counter_two

print(counter_total)


# =============================================================================
# 16. Reverse Addition With __radd__
# =============================================================================

class AddableValue:
    """Support addition with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: AddableValue) -> AddableValue:
        """Add another AddableValue."""
        return AddableValue(self.value + other.value)

    def __radd__(self, other: int) -> AddableValue:
        """Support integer + AddableValue."""
        return AddableValue(other + self.value)

    def __repr__(self) -> str:
        return f"AddableValue({self.value})"


addable_value: AddableValue = AddableValue(10)

reverse_addition: AddableValue = 5 + addable_value

print(reverse_addition)


# =============================================================================
# 17. Reverse Subtraction With __rsub__
# =============================================================================

class SubtractableValue:
    """Support subtraction with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __sub__(self, other: SubtractableValue) -> SubtractableValue:
        return SubtractableValue(self.value - other.value)

    def __rsub__(self, other: int) -> SubtractableValue:
        """Support integer - SubtractableValue."""
        return SubtractableValue(other - self.value)

    def __repr__(self) -> str:
        return f"SubtractableValue({self.value})"


subtractable_value: SubtractableValue = SubtractableValue(15)

reverse_subtraction: SubtractableValue = 50 - subtractable_value

print(reverse_subtraction)


# =============================================================================
# 18. Reverse Multiplication With __rmul__
# =============================================================================

class MultipliableValue:
    """Support multiplication with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mul__(self, other: MultipliableValue) -> MultipliableValue:
        return MultipliableValue(self.value * other.value)

    def __rmul__(self, other: int) -> MultipliableValue:
        """Support integer * MultipliableValue."""
        return MultipliableValue(other * self.value)

    def __repr__(self) -> str:
        return f"MultipliableValue({self.value})"


multipliable_value: MultipliableValue = MultipliableValue(8)

reverse_multiplication: MultipliableValue = 4 * multipliable_value

print(reverse_multiplication)


# =============================================================================
# 19. Reverse Division With __rtruediv__
# =============================================================================

class DivisibleValue:
    """Support division with integers."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __truediv__(self, other: DivisibleValue) -> DivisibleValue:
        return DivisibleValue(self.value / other.value)

    def __rtruediv__(self, other: float) -> DivisibleValue:
        """Support float / DivisibleValue."""
        return DivisibleValue(other / self.value)

    def __repr__(self) -> str:
        return f"DivisibleValue({self.value})"


divisible_value: DivisibleValue = DivisibleValue(5.0)

reverse_division: DivisibleValue = 100.0 / divisible_value

print(reverse_division)


# =============================================================================
# 20. Reverse Floor Division With __rfloordiv__
# =============================================================================

class FloorDivisibleValue:
    """Support floor division with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __floordiv__(
        self,
        other: FloorDivisibleValue,
    ) -> FloorDivisibleValue:
        return FloorDivisibleValue(self.value // other.value)

    def __rfloordiv__(
        self,
        other: int,
    ) -> FloorDivisibleValue:
        """Support integer // FloorDivisibleValue."""
        return FloorDivisibleValue(other // self.value)

    def __repr__(self) -> str:
        return f"FloorDivisibleValue({self.value})"


floor_divisible_value: FloorDivisibleValue = FloorDivisibleValue(4)

reverse_floor_division: FloorDivisibleValue = 20 // floor_divisible_value

print(reverse_floor_division)


# =============================================================================
# 21. Reverse Modulo With __rmod__
# =============================================================================

class ModuloValue:
    """Support modulo with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mod__(self, other: ModuloValue) -> ModuloValue:
        return ModuloValue(self.value % other.value)

    def __rmod__(self, other: int) -> ModuloValue:
        """Support integer % ModuloValue."""
        return ModuloValue(other % self.value)

    def __repr__(self) -> str:
        return f"ModuloValue({self.value})"


modulo_value: ModuloValue = ModuloValue(7)

reverse_modulo: ModuloValue = 20 % modulo_value

print(reverse_modulo)


# =============================================================================
# 22. Reverse Power With __rpow__
# =============================================================================

class PowerValue:
    """Support exponentiation with integers."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __pow__(self, other: PowerValue) -> PowerValue:
        return PowerValue(self.value**other.value)

    def __rpow__(self, other: int) -> PowerValue:
        """Support integer ** PowerValue."""
        return PowerValue(other**self.value)

    def __repr__(self) -> str:
        return f"PowerValue({self.value})"


power_value: PowerValue = PowerValue(3)

reverse_power: PowerValue = 2**power_value

print(reverse_power)


# =============================================================================
# 23. __add__ With an Integer
# =============================================================================

class IntegerAdd:
    """Represent a value that can add an integer."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: int) -> IntegerAdd:
        """Add an integer."""
        return IntegerAdd(self.value + other)

    def __repr__(self) -> str:
        return f"IntegerAdd({self.value})"


integer_add: IntegerAdd = IntegerAdd(10)
integer_add_result: IntegerAdd = integer_add + 5

print(integer_add_result)


# =============================================================================
# 24. __mul__ With an Integer
# =============================================================================

class IntegerMultiply:
    """Represent a value that can multiply by an integer."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __mul__(self, other: int) -> IntegerMultiply:
        """Multiply by an integer."""
        return IntegerMultiply(self.value * other)

    def __repr__(self) -> str:
        return f"IntegerMultiply({self.value})"


integer_multiply: IntegerMultiply = IntegerMultiply(10)
integer_multiply_result: IntegerMultiply = integer_multiply * 5

print(integer_multiply_result)


# =============================================================================
# 25. __truediv__ With a Float
# =============================================================================

class FloatDivision:
    """Represent a value that supports division by a float."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __truediv__(self, other: float) -> FloatDivision:
        """Divide by a float."""
        return FloatDivision(self.value / other)

    def __repr__(self) -> str:
        return f"FloatDivision({self.value})"


float_division: FloatDivision = FloatDivision(100.0)
float_division_result: FloatDivision = float_division / 4.0

print(float_division_result)


# =============================================================================
# 26. __pow__ With an Integer
# =============================================================================

class IntegerPower:
    """Represent a value supporting integer exponents."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __pow__(self, exponent: int) -> IntegerPower:
        """Raise the value to an integer exponent."""
        return IntegerPower(self.value**exponent)

    def __repr__(self) -> str:
        return f"IntegerPower({self.value})"


integer_power: IntegerPower = IntegerPower(3)
integer_power_result: IntegerPower = integer_power**4

print(integer_power_result)


# =============================================================================
# 27. __neg__ For a Vector
# =============================================================================

class Vector2D:
    """Represent a two-dimensional vector."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __neg__(self) -> Vector2D:
        """Negate both coordinates."""
        return Vector2D(-self.x, -self.y)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"


vector: Vector2D = Vector2D(10.0, -5.0)
negative_vector: Vector2D = -vector

print(negative_vector)


# =============================================================================
# 28. __add__ For a Vector
# =============================================================================

class Coordinate:
    """Represent a two-dimensional coordinate."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __add__(self, other: Coordinate) -> Coordinate:
        """Add two coordinates."""
        return Coordinate(
            self.x + other.x,
            self.y + other.y,
        )

    def __repr__(self) -> str:
        return f"Coordinate(x={self.x}, y={self.y})"


coordinate_a: Coordinate = Coordinate(10.0, 20.0)
coordinate_b: Coordinate = Coordinate(5.0, 7.0)

coordinate_sum: Coordinate = coordinate_a + coordinate_b

print(coordinate_sum)


# =============================================================================
# 29. __sub__ For a Vector
# =============================================================================

class Position:
    """Represent a two-dimensional position."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __sub__(self, other: Position) -> Position:
        """Subtract two positions."""
        return Position(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self) -> str:
        return f"Position(x={self.x}, y={self.y})"


position_a: Position = Position(100.0, 80.0)
position_b: Position = Position(40.0, 30.0)

position_difference: Position = position_a - position_b

print(position_difference)


# =============================================================================
# 30. __mul__ For Scalar Multiplication
# =============================================================================

class Vector:
    """Represent a two-dimensional vector."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __mul__(self, scalar: float) -> Vector:
        """Multiply both coordinates by a scalar."""
        return Vector(
            self.x * scalar,
            self.y * scalar,
        )

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


vector_value: Vector = Vector(3.0, 4.0)
scaled_vector: Vector = vector_value * 5.0

print(scaled_vector)


# =============================================================================
# 31. __rmul__ For Scalar Multiplication
# =============================================================================

class ScalableVector:
    """Represent a vector supporting multiplication in both directions."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __mul__(self, scalar: float) -> ScalableVector:
        """Support vector * scalar."""
        return ScalableVector(
            self.x * scalar,
            self.y * scalar,
        )

    def __rmul__(self, scalar: float) -> ScalableVector:
        """Support scalar * vector."""
        return ScalableVector(
            scalar * self.x,
            scalar * self.y,
        )

    def __repr__(self) -> str:
        return f"ScalableVector(x={self.x}, y={self.y})"


scalable_vector: ScalableVector = ScalableVector(2.0, 3.0)

right_scaled: ScalableVector = scalable_vector * 4.0
left_scaled: ScalableVector = 4.0 * scalable_vector

print(right_scaled)
print(left_scaled)


# =============================================================================
# 32. __add__ Returning Self-Type
# =============================================================================

class Measurement:
    """Represent a measurement."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: Measurement) -> Self:
        """Add two measurements."""
        return type(self)(self.value + other.value)

    def __repr__(self) -> str:
        return f"Measurement({self.value})"


measurement_a: Measurement = Measurement(12.5)
measurement_b: Measurement = Measurement(7.5)

measurement_total: Measurement = measurement_a + measurement_b

print(measurement_total)


# =============================================================================
# 33. __sub__ Returning Self-Type
# =============================================================================

class Distance:
    """Represent a distance."""

    def __init__(self, meters: float) -> None:
        self.meters: float = meters

    def __sub__(self, other: Distance) -> Self:
        """Subtract distances."""
        return type(self)(self.meters - other.meters)

    def __repr__(self) -> str:
        return f"Distance({self.meters}m)"


distance_a: Distance = Distance(100.0)
distance_b: Distance = Distance(35.0)

distance_difference: Distance = distance_a - distance_b

print(distance_difference)


# =============================================================================
# 34. __iadd__
# =============================================================================

class MutableCounter:
    """Represent a mutable counter."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __iadd__(self, amount: int) -> Self:
        """Implement +=."""
        self.value += amount
        return self

    def __repr__(self) -> str:
        return f"MutableCounter({self.value})"


mutable_counter: MutableCounter = MutableCounter(10)

mutable_counter += 5

print(mutable_counter)


# =============================================================================
# 35. __isub__
# =============================================================================

class MutableBalance:
    """Represent a mutable balance."""

    def __init__(self, amount: float) -> None:
        self.amount: float = amount

    def __isub__(self, amount: float) -> Self:
        """Implement -=."""
        self.amount -= amount
        return self

    def __repr__(self) -> str:
        return f"MutableBalance({self.amount})"


balance: MutableBalance = MutableBalance(100.0)

balance -= 25.0

print(balance)


# =============================================================================
# 36. __imul__
# =============================================================================

class MutableValue:
    """Represent a mutable numeric value."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __imul__(self, multiplier: float) -> Self:
        """Implement *=."""
        self.value *= multiplier
        return self

    def __repr__(self) -> str:
        return f"MutableValue({self.value})"


mutable_value: MutableValue = MutableValue(10.0)

mutable_value *= 3.0

print(mutable_value)


# =============================================================================
# 37. __itruediv__
# =============================================================================

class MutableDivisionValue:
    """Represent a mutable value supporting /=."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __itruediv__(self, divisor: float) -> Self:
        """Implement /=."""
        self.value /= divisor
        return self

    def __repr__(self) -> str:
        return f"MutableDivisionValue({self.value})"


division_value: MutableDivisionValue = MutableDivisionValue(100.0)

division_value /= 4.0

print(division_value)


# =============================================================================
# 38. __ifloordiv__
# =============================================================================

class MutableFloorValue:
    """Represent a mutable value supporting //=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __ifloordiv__(self, divisor: int) -> Self:
        """Implement //=."""
        self.value //= divisor
        return self

    def __repr__(self) -> str:
        return f"MutableFloorValue({self.value})"


floor_value: MutableFloorValue = MutableFloorValue(25)

floor_value //= 4

print(floor_value)


# =============================================================================
# 39. __imod__
# =============================================================================

class MutableModuloValue:
    """Represent a mutable value supporting %=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __imod__(self, divisor: int) -> Self:
        """Implement %=."""
        self.value %= divisor
        return self

    def __repr__(self) -> str:
        return f"MutableModuloValue({self.value})"


modulo_value_in_place: MutableModuloValue = MutableModuloValue(29)

modulo_value_in_place %= 6

print(modulo_value_in_place)


# =============================================================================
# 40. __ipow__
# =============================================================================

class MutablePowerValue:
    """Represent a mutable value supporting **=."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __ipow__(self, exponent: int) -> Self:
        """Implement **=."""
        self.value **= exponent
        return self

    def __repr__(self) -> str:
        return f"MutablePowerValue({self.value})"


power_value_in_place: MutablePowerValue = MutablePowerValue(2)

power_value_in_place **= 5

print(power_value_in_place)


# =============================================================================
# 41. Arithmetic Dunder Methods Are Called By Operators
# =============================================================================

class OperatorDemo:
    """Demonstrate direct calls to arithmetic dunder methods."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: OperatorDemo) -> OperatorDemo:
        return OperatorDemo(self.value + other.value)

    def __sub__(self, other: OperatorDemo) -> OperatorDemo:
        return OperatorDemo(self.value - other.value)

    def __repr__(self) -> str:
        return f"OperatorDemo({self.value})"


operator_a: OperatorDemo = OperatorDemo(20)
operator_b: OperatorDemo = OperatorDemo(5)

operator_sum: OperatorDemo = operator_a + operator_b
direct_sum: OperatorDemo = operator_a.__add__(operator_b)

print(operator_sum)
print(direct_sum)


# =============================================================================
# 42. Operator Syntax And Dunder Method Equivalence
# =============================================================================

class ArithmeticValue:
    """Demonstrate operator-to-dunder mapping."""

    def __init__(self, value: int) -> None:
        self.value: int = value

    def __add__(self, other: ArithmeticValue) -> ArithmeticValue:
        return ArithmeticValue(self.value + other.value)

    def __repr__(self) -> str:
        return f"ArithmeticValue({self.value})"


left_value: ArithmeticValue = ArithmeticValue(10)
right_value: ArithmeticValue = ArithmeticValue(20)

operator_result: ArithmeticValue = left_value + right_value
method_result: ArithmeticValue = left_value.__add__(right_value)

print(operator_result)
print(method_result)


# =============================================================================
# 43. Combining Arithmetic Operations
# =============================================================================

class NumericValue:
    """Represent a value supporting arithmetic operations."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: NumericValue) -> NumericValue:
        return NumericValue(self.value + other.value)

    def __sub__(self, other: NumericValue) -> NumericValue:
        return NumericValue(self.value - other.value)

    def __mul__(self, other: NumericValue) -> NumericValue:
        return NumericValue(self.value * other.value)

    def __truediv__(self, other: NumericValue) -> NumericValue:
        return NumericValue(self.value / other.value)

    def __repr__(self) -> str:
        return f"NumericValue({self.value})"


numeric_a: NumericValue = NumericValue(20.0)
numeric_b: NumericValue = NumericValue(5.0)
numeric_c: NumericValue = NumericValue(2.0)

combined_result: NumericValue = (
    (numeric_a + numeric_b)
    * numeric_c
    / numeric_b
)

print(combined_result)


# =============================================================================
# 44. Arithmetic Dunder Methods And Validation
# =============================================================================

class PositiveValue:
    """Represent a value that must remain non-negative."""

    def __init__(self, value: int) -> None:
        if value < 0:
            raise ValueError("value must be non-negative")

        self.value: int = value

    def __add__(self, other: PositiveValue) -> PositiveValue:
        """Add two positive values."""
        return PositiveValue(self.value + other.value)

    def __repr__(self) -> str:
        return f"PositiveValue({self.value})"


positive_a: PositiveValue = PositiveValue(10)
positive_b: PositiveValue = PositiveValue(20)

positive_sum: PositiveValue = positive_a + positive_b

print(positive_sum)


# =============================================================================
# 45. Arithmetic Dunder Methods And Domain Objects
# =============================================================================

class Hours:
    """Represent a number of working hours."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: Hours) -> Hours:
        """Combine working hours."""
        return Hours(self.value + other.value)

    def __sub__(self, other: Hours) -> Hours:
        """Subtract working hours."""
        return Hours(self.value - other.value)

    def __repr__(self) -> str:
        return f"Hours({self.value})"


morning_hours: Hours = Hours(4.0)
afternoon_hours: Hours = Hours(3.5)

daily_hours: Hours = morning_hours + afternoon_hours

print(daily_hours)


# =============================================================================
# 46. Arithmetic Dunder Methods And Unit Conversion
# =============================================================================

class Kilometers:
    """Represent a distance in kilometres."""

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: Kilometers) -> Kilometers:
        """Add kilometre values."""
        return Kilometers(self.value + other.value)

    def __mul__(self, multiplier: float) -> Kilometers:
        """Scale the distance."""
        return Kilometers(self.value * multiplier)

    def __repr__(self) -> str:
        return f"Kilometers({self.value})"


trip_one: Kilometers = Kilometers(12.5)
trip_two: Kilometers = Kilometers(8.5)

total_trip: Kilometers = trip_one + trip_two
double_trip: Kilometers = total_trip * 2.0

print(total_trip)
print(double_trip)


# =============================================================================
# 47. Arithmetic Dunder Methods And Fractions
# =============================================================================

class Fraction:
    """Represent a simple fraction."""

    def __init__(
        self,
        numerator: int,
        denominator: int,
    ) -> None:
        if denominator == 0:
            raise ValueError("denominator cannot be zero")

        self.numerator: int = numerator
        self.denominator: int = denominator

    def __add__(self, other: Fraction) -> Fraction:
        """Add two fractions."""
        numerator: int = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator: int = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"


fraction_a: Fraction = Fraction(1, 2)
fraction_b: Fraction = Fraction(1, 3)

fraction_sum: Fraction = fraction_a + fraction_b

print(fraction_sum)


# =============================================================================
# 48. Arithmetic Dunder Methods And Complex Domain Objects
# =============================================================================

class Point:
    """Represent a two-dimensional point."""

    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y

    def __add__(self, other: Point) -> Point:
        """Translate the point by another point."""
        return Point(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Point) -> Point:
        """Subtract coordinates."""
        return Point(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, scalar: float) -> Point:
        """Scale the point."""
        return Point(
            self.x * scalar,
            self.y * scalar,
        )

    def __neg__(self) -> Point:
        """Negate the point."""
        return Point(
            -self.x,
            -self.y,
        )

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


point_a: Point = Point(10.0, 20.0)
point_b: Point = Point(5.0, 3.0)

point_sum: Point = point_a + point_b
point_difference: Point = point_a - point_b
point_scaled: Point = point_a * 2.0
point_negative: Point = -point_a

print(point_sum)
print(point_difference)
print(point_scaled)
print(point_negative)


# =============================================================================
# 49. Complete Arithmetic Dunder Class
# =============================================================================

class ArithmeticNumber:
    """
    Represent a number with a broad set of arithmetic operations.
    """

    def __init__(self, value: float) -> None:
        self.value: float = value

    def __add__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value + other.value)

    def __sub__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value - other.value)

    def __mul__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value * other.value)

    def __truediv__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value / other.value)

    def __floordiv__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value // other.value)

    def __mod__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value % other.value)

    def __pow__(self, other: ArithmeticNumber) -> ArithmeticNumber:
        return ArithmeticNumber(self.value**other.value)

    def __neg__(self) -> ArithmeticNumber:
        return ArithmeticNumber(-self.value)

    def __pos__(self) -> ArithmeticNumber:
        return ArithmeticNumber(+self.value)

    def __abs__(self) -> float:
        return abs(self.value)

    def __repr__(self) -> str:
        return f"ArithmeticNumber({self.value})"


arithmetic_left: ArithmeticNumber = ArithmeticNumber(20.0)
arithmetic_right: ArithmeticNumber = ArithmeticNumber(6.0)

print(arithmetic_left + arithmetic_right)
print(arithmetic_left - arithmetic_right)
print(arithmetic_left * arithmetic_right)
print(arithmetic_left / arithmetic_right)
print(arithmetic_left // arithmetic_right)
print(arithmetic_left % arithmetic_right)
print(arithmetic_left**ArithmeticNumber(2.0))
print(-arithmetic_left)
print(+arithmetic_left)
print(abs(-ArithmeticNumber(20.0)))


# =============================================================================
# 50. Complete Example: Arithmetic Value Object
# =============================================================================

class Price:
    """
    Represent a price and support common arithmetic operations.

    This example demonstrates how arithmetic dunder methods can make a
    domain-specific object behave naturally in arithmetic expressions.
    """

    def __init__(self, amount: float) -> None:
        self.amount: float = amount

    def __add__(self, other: Price) -> Price:
        """Add two prices."""
        return Price(self.amount + other.amount)

    def __sub__(self, other: Price) -> Price:
        """Subtract one price from another."""
        return Price(self.amount - other.amount)

    def __mul__(self, quantity: int) -> Price:
        """Multiply a price by a quantity."""
        return Price(self.amount * quantity)

    def __rmul__(self, quantity: int) -> Price:
        """Support quantity * price."""
        return Price(quantity * self.amount)

    def __truediv__(self, divisor: float) -> Price:
        """Divide a price by a divisor."""
        return Price(self.amount / divisor)

    def __neg__(self) -> Price:
        """Return the negative price."""
        return Price(-self.amount)

    def __abs__(self) -> float:
        """Return the absolute monetary amount."""
        return abs(self.amount)

    def __iadd__(self, other: Price) -> Self:
        """Implement +=."""
        self.amount += other.amount
        return self

    def __isub__(self, other: Price) -> Self:
        """Implement -=."""
        self.amount -= other.amount
        return self

    def __imul__(self, quantity: int) -> Self:
        """Implement *=."""
        self.amount *= quantity
        return self

    def __itruediv__(self, divisor: float) -> Self:
        """Implement /=."""
        self.amount /= divisor
        return self

    def __repr__(self) -> str:
        return f"Price({self.amount:.2f})"


base_price: Price = Price(100.0)
additional_price: Price = Price(25.0)

combined_price: Price = base_price + additional_price
discounted_price: Price = combined_price - Price(10.0)

quantity_price: Price = base_price * 3
reverse_quantity_price: Price = 3 * base_price

split_price: Price = combined_price / 2.0

negative_price: Price = -base_price
absolute_price: float = abs(negative_price)

print(combined_price)
print(discounted_price)
print(quantity_price)
print(reverse_quantity_price)
print(split_price)
print(negative_price)
print(absolute_price)

running_price: Price = Price(50.0)

running_price += Price(25.0)
running_price -= Price(5.0)
running_price *= 2
running_price /= 2.0

print(running_price)


# =============================================================================
# Arithmetic Dunder Methods Summary
# =============================================================================

"""
Arithmetic operator:

    a + b
        ↓
    a.__add__(b)

Arithmetic operator:

    a - b
        ↓
    a.__sub__(b)

Arithmetic operator:

    a * b
        ↓
    a.__mul__(b)

Arithmetic operator:

    a / b
        ↓
    a.__truediv__(b)

Arithmetic operator:

    a // b
        ↓
    a.__floordiv__(b)

Arithmetic operator:

    a % b
        ↓
    a.__mod__(b)

Arithmetic operator:

    a ** b
        ↓
    a.__pow__(b)

Unary operator:

    -a
        ↓
    a.__neg__()

Unary operator:

    +a
        ↓
    a.__pos__()

Built-in operation:

    abs(a)
        ↓
    a.__abs__()

Reverse operations:

    a + b
        ↓
    b.__radd__(a)

    a - b
        ↓
    b.__rsub__(a)

    a * b
        ↓
    b.__rmul__(a)

    a / b
        ↓
    b.__rtruediv__(a)

    a // b
        ↓
    b.__rfloordiv__(a)

    a % b
        ↓
    b.__rmod__(a)

    a ** b
        ↓
    b.__rpow__(a)

In-place operations:

    a += b
        ↓
    a.__iadd__(b)

    a -= b
        ↓
    a.__isub__(b)

    a *= b
        ↓
    a.__imul__(b)

    a /= b
        ↓
    a.__itruediv__(b)

    a //= b
        ↓
    a.__ifloordiv__(b)

    a %= b
        ↓
    a.__imod__(b)

    a **= b
        ↓
    a.__ipow__(b)

Key idea:

    Operators are syntax.

    Arithmetic dunder methods provide the object-level implementation
    behind that syntax.

Example:

    class Money:

        def __add__(self, other: Money) -> Money:
            return Money(self.amount + other.amount)

Then:

    price_a + price_b

can naturally produce:

    Money(...)

Arithmetic dunder methods are especially useful for:

    - numeric value objects
    - vectors
    - coordinates
    - money
    - measurements
    - fractions
    - domain-specific numeric types
    - scientific objects
    - matrices
    - quantities with units

Important design principle:

    Define arithmetic behaviour only when the operation has a clear
    and meaningful interpretation for the object.

Avoid implementing operators merely because Python allows it.

For example:

    Money + Money

has an obvious meaning.

But:

    User + DatabaseConnection

does not have an obvious mathematical meaning and should generally not
be implemented.

The goal of operator overloading is readable and intuitive code.

Example:

    total = price + tax

is often clearer than:

    total = price.add(tax)

when addition genuinely represents the domain operation.
"""


# =============================================================================
# End of 17_arithmetic_dunder_methods.py
# =============================================================================