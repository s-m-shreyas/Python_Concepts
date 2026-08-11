# =============================================================================
# 20. Callable Objects
# =============================================================================
# type: ignore

"""
Python Functions

File:
    20_callable_objects.py

Topic:
    Callable Objects

Overview:
    In Python, an object is callable when it can be used with parentheses:

        object()

    Functions are callable objects, but functions are not the only callable
    objects in Python.

    Classes can define the special method:

        __call__()

    When an instance of such a class is followed by parentheses, Python
    executes its __call__() method.

Topics covered:

    - What is a callable object?
    - Functions are callable objects
    - Checking whether an object is callable
    - The callable() built-in function
    - __call__()
    - Creating a callable class
    - Calling an object like a function
    - Callable objects with state
    - Callable objects with parameters
    - Callable objects versus normal methods
    - Callable objects and closures
    - Callable objects and classes
    - Callable objects as function replacements
    - Callable objects as configuration containers
    - Callable objects for counters
    - Callable objects for validation
    - Callable objects for formatting
    - Callable objects for mathematical operations
    - Callable objects in higher-order functions
    - Callable objects in decorators
    - Callable objects with __call__ annotations
    - Maintaining state with callable objects
    - __call__() and return values
    - Multiple callable instances
    - Callable objects and isinstance()
    - Callable objects and method lookup
    - Practical design guidelines
"""


# =============================================================================
# 01. What Is a Callable Object?
# =============================================================================
"""
A callable object is an object that can be invoked using parentheses.

Examples of callable objects include:

    - Functions
    - Classes
    - Methods
    - Objects implementing __call__()

For example:

    def greet() -> str:
        return "Hello"

    message: str = greet()

Here:

    greet

is a callable object.

Python provides:

    callable()

to check whether an object can be called.
"""


# =============================================================================
# 02. A Normal Function Is Callable
# =============================================================================

def greet_user() -> str:
    """
    Return a greeting.
    """
    return "Hello, Python!"


greeting: str = greet_user()

print(greeting)


# =============================================================================
# 03. Checking Whether a Function Is Callable
# =============================================================================

def add_numbers(
    first: int,
    second: int,
) -> int:
    """
    Add two numbers.
    """
    return first + second


print(
    callable(add_numbers),
)


# Expected:
#
# True


# =============================================================================
# 04. Non-Callable Objects
# =============================================================================

number: int = 100
message: str = "Hello"
numbers: list[int] = [1, 2, 3]

print(
    callable(number),
)

print(
    callable(message),
)

print(
    callable(numbers),
)


# Expected:
#
# False
# False
# False


# =============================================================================
# 05. The callable() Built-in Function
# =============================================================================
"""
callable() checks whether an object appears to be callable.

Example:

    callable(print)

returns:

    True

Example:

    callable(100)

returns:

    False

The general pattern is:

    callable(object)

The result is a bool.
"""


def calculate_square(
    number: int,
) -> int:
    """
    Return the square of a number.
    """
    return number ** 2


square_callable: bool = callable(calculate_square)
number_callable: bool = callable(100)

print(square_callable)
print(number_callable)


# =============================================================================
# 06. Classes Are Callable
# =============================================================================
"""
Classes themselves are callable.

When a class is called:

    Person()

Python creates an instance of that class.

Therefore:

    callable(Person)

returns True.
"""


class Person:
    """
    Represent a person.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name


print(
    callable(Person),
)


person: Person = Person(
    "Alex",
)

print(
    person.name,
)


# =============================================================================
# 07. Instances Are Not Automatically Callable
# =============================================================================
"""
An ordinary instance is not callable unless its class provides __call__().
"""


class Calculator:
    """
    Represent a calculator.
    """

    def add(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Add two numbers.
        """
        return first + second


calculator: Calculator = Calculator()

print(
    callable(calculator),
)


# Expected:
#
# False


# =============================================================================
# 08. Creating a Callable Object
# =============================================================================
"""
An object becomes callable when its class defines:

    __call__()

Example:

    class Greeter:
        def __call__(self) -> str:
            return "Hello"

    greeter = Greeter()

    greeter()

The expression:

    greeter()

is translated conceptually into:

    greeter.__call__()
"""


class Greeter:
    """
    Represent a callable greeter.
    """

    def __call__(self) -> str:
        """
        Return a greeting.
        """
        return "Hello from a callable object!"


greeter: Greeter = Greeter()

print(
    callable(greeter),
)

greeter_message: str = greeter()

print(greeter_message)


# =============================================================================
# 09. __call__() Is a Special Method
# =============================================================================
"""
__call__() is a special method that controls what happens when an instance
is called with parentheses.

For example:

    object()

Python looks for the object's callable behaviour.

A class can define:

    def __call__(self) -> ...

to make its instances callable.
"""


class WelcomeMessage:
    """
    Represent a callable welcome-message object.
    """

    def __call__(
        self,
        name: str,
    ) -> str:
        """
        Create a welcome message.
        """
        return f"Welcome, {name}!"


welcome: WelcomeMessage = WelcomeMessage()

welcome_message: str = welcome(
    "Shreyas",
)

print(welcome_message)


# =============================================================================
# 10. Callable Object With State
# =============================================================================
"""
One important advantage of callable objects is that they can store state.

A normal function can receive arguments, but a callable object can store
configuration or state on the instance itself.
"""


class Multiplier:
    """
    Multiply numbers using stored configuration.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor

    def __call__(
        self,
        number: int,
    ) -> int:
        """
        Multiply a number by the stored factor.
        """
        return number * self.factor


double: Multiplier = Multiplier(
    2,
)

triple: Multiplier = Multiplier(
    3,
)

double_result: int = double(
    10,
)

triple_result: int = triple(
    10,
)

print(double_result)
print(triple_result)


# =============================================================================
# 11. Multiple Callable Objects Can Have Different State
# =============================================================================

class Power:
    """
    Calculate powers using a stored exponent.
    """

    def __init__(
        self,
        exponent: int,
    ) -> None:
        self.exponent: int = exponent

    def __call__(
        self,
        number: int,
    ) -> int:
        """
        Raise a number to the configured exponent.
        """
        return number ** self.exponent


square: Power = Power(
    2,
)

cube: Power = Power(
    3,
)

square_result: int = square(
    5,
)

cube_result: int = cube(
    5,
)

print(square_result)
print(cube_result)


# =============================================================================
# 12. Callable Object With Multiple Parameters
# =============================================================================

class CalculatorFunction:
    """
    Represent a callable calculator.
    """

    def __call__(
        self,
        first: float,
        second: float,
    ) -> float:
        """
        Add two numbers.
        """
        return first + second


calculator_function: CalculatorFunction = CalculatorFunction()

calculation_result: float = calculator_function(
    10.5,
    20.5,
)

print(calculation_result)


# =============================================================================
# 13. Callable Object Can Have Normal Methods
# =============================================================================

class Counter:
    """
    Represent a callable counter.
    """

    def __init__(self) -> None:
        self.value: int = 0

    def __call__(self) -> int:
        """
        Increment and return the counter.
        """
        self.value += 1
        return self.value

    def reset(self) -> None:
        """
        Reset the counter.
        """
        self.value = 0


counter: Counter = Counter()

print(counter())
print(counter())
print(counter())

counter.reset()

print(counter())


# =============================================================================
# 14. Callable Object Can Store Configuration
# =============================================================================

class Prefixer:
    """
    Add a configured prefix to text.
    """

    def __init__(
        self,
        prefix: str,
    ) -> None:
        self.prefix: str = prefix

    def __call__(
        self,
        message: str,
    ) -> str:
        """
        Prefix the supplied message.
        """
        return f"{self.prefix}: {message}"


info: Prefixer = Prefixer(
    "INFO",
)

error: Prefixer = Prefixer(
    "ERROR",
)

print(
    info("Application started"),
)

print(
    error("Application failed"),
)


# =============================================================================
# 15. Callable Object for Validation
# =============================================================================

class MinimumLengthValidator:
    """
    Validate that text has a minimum length.
    """

    def __init__(
        self,
        minimum_length: int,
    ) -> None:
        self.minimum_length: int = minimum_length

    def __call__(
        self,
        value: str,
    ) -> bool:
        """
        Return whether the value meets the minimum length.
        """
        return len(value) >= self.minimum_length


validate_username: MinimumLengthValidator = MinimumLengthValidator(
    5,
)

print(
    validate_username("Alex"),
)

print(
    validate_username("Python"),
)


# =============================================================================
# 16. Callable Object for Formatting
# =============================================================================

class Formatter:
    """
    Format text using stored configuration.
    """

    def __init__(
        self,
        prefix: str,
        suffix: str,
    ) -> None:
        self.prefix: str = prefix
        self.suffix: str = suffix

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Format the supplied value.
        """
        return f"{self.prefix}{value}{self.suffix}"


quote_formatter: Formatter = Formatter(
    '"',
    '"',
)

formatted_text: str = quote_formatter(
    "Hello",
)

print(formatted_text)


# =============================================================================
# 17. Callable Object for Mathematical Operations
# =============================================================================

class Adder:
    """
    Add a stored amount to a number.
    """

    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount: int = amount

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add the configured amount.
        """
        return value + self.amount


add_ten: Adder = Adder(
    10,
)

add_twenty: Adder = Adder(
    20,
)

print(
    add_ten(100),
)

print(
    add_twenty(100),
)


# =============================================================================
# 18. Callable Objects Can Be Passed to Functions
# =============================================================================
"""
A callable object can be passed anywhere a function-like callable is
expected.
"""


def apply_operation(
    operation: object,
    value: int,
) -> int:
    """
    Apply a callable operation.

    This example intentionally uses a runtime callable check because
    operation is accepted as a generic object.
    """
    if not callable(operation):
        raise TypeError(
            "operation must be callable",
        )

    result: object = operation(value)

    if not isinstance(result, int):
        raise TypeError(
            "operation must return an int",
        )

    return result


add_five: Adder = Adder(
    5,
)

operation_result: int = apply_operation(
    add_five,
    100,
)

print(operation_result)


# =============================================================================
# 19. Callable Objects and Higher-Order Functions
# =============================================================================
"""
A higher-order function is a function that accepts a callable, returns a
callable, or both.

Callable objects can therefore be used with higher-order functions.
"""


def apply_to_values(
    operation: object,
    values: list[int],
) -> list[int]:
    """
    Apply a callable operation to every value.
    """
    if not callable(operation):
        raise TypeError(
            "operation must be callable",
        )

    results: list[int] = []

    for value in values:
        result: object = operation(value)

        if not isinstance(result, int):
            raise TypeError(
                "operation must return an int",
            )

        results.append(result)

    return results


double_values: Multiplier = Multiplier(
    2,
)

values: list[int] = [
    1,
    2,
    3,
    4,
]

doubled_values: list[int] = apply_to_values(
    double_values,
    values,
)

print(doubled_values)


# =============================================================================
# 20. Callable Object Versus Function
# =============================================================================
"""
A normal function:

    def double(value: int) -> int:
        return value * 2

A callable object:

    class Doubler:
        def __call__(self, value: int) -> int:
            return value * 2

Both can be used as:

    double(10)

or:

    doubler(10)

The callable object has the additional advantage of being able to maintain
instance state.
"""


def double_function(
    value: int,
) -> int:
    """
    Double a value using a function.
    """
    return value * 2


class Doubler:
    """
    Double values using a callable object.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Double the supplied value.
        """
        return value * 2


doubler: Doubler = Doubler()

print(
    double_function(10),
)

print(
    doubler(10),
)


# =============================================================================
# 21. Callable Object With Mutable State
# =============================================================================

class RunningTotal:
    """
    Maintain a running total.
    """

    def __init__(self) -> None:
        self.total: int = 0

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add value to the running total.
        """
        self.total += value
        return self.total


running_total: RunningTotal = RunningTotal()

print(
    running_total(10),
)

print(
    running_total(20),
)

print(
    running_total(30),
)


# =============================================================================
# 22. Callable Object With a Reset Method
# =============================================================================

class Accumulator:
    """
    Accumulate integer values.
    """

    def __init__(self) -> None:
        self.total: int = 0

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add a value to the accumulator.
        """
        self.total += value
        return self.total

    def reset(self) -> None:
        """
        Reset the accumulated value.
        """
        self.total = 0


accumulator: Accumulator = Accumulator()

print(
    accumulator(10),
)

print(
    accumulator(20),
)

accumulator.reset()

print(
    accumulator(5),
)


# =============================================================================
# 23. Callable Objects Can Have Properties
# =============================================================================

class TemperatureConverter:
    """
    Convert Celsius values to Fahrenheit.
    """

    def __init__(
        self,
        offset: float = 32.0,
    ) -> None:
        self.offset: float = offset

    def __call__(
        self,
        celsius: float,
    ) -> float:
        """
        Convert Celsius to Fahrenheit.
        """
        return (
            celsius * 9.0 / 5.0
        ) + self.offset


converter: TemperatureConverter = TemperatureConverter()

fahrenheit: float = converter(
    25.0,
)

print(fahrenheit)


# =============================================================================
# 24. Callable Object Can Be Stateful
# =============================================================================
"""
A function can maintain state using external mechanisms such as closures,
but a class makes the state explicit as instance attributes.

Example:

    class Counter:
        def __init__(self) -> None:
            self.count = 0

        def __call__(self) -> int:
            self.count += 1
            return self.count

The state belongs to the object.
"""


class CallCounter:
    """
    Count how many times the object is called.
    """

    def __init__(self) -> None:
        self.calls: int = 0

    def __call__(self) -> int:
        """
        Increment and return the number of calls.
        """
        self.calls += 1
        return self.calls


call_counter: CallCounter = CallCounter()

print(
    call_counter(),
)

print(
    call_counter(),
)

print(
    call_counter(),
)


# =============================================================================
# 25. Separate Instances Have Separate State
# =============================================================================

counter_one: CallCounter = CallCounter()
counter_two: CallCounter = CallCounter()

print(
    counter_one(),
)

print(
    counter_one(),
)

print(
    counter_two(),
)

print(
    counter_two(),
)

print(
    counter_two(),
)


# counter_one and counter_two maintain independent state.


# =============================================================================
# 26. callable() With a Callable Object
# =============================================================================

class SimpleCallable:
    """
    Represent a simple callable object.
    """

    def __call__(
        self,
    ) -> str:
        """
        Return a message.
        """
        return "Object was called"


simple_callable: SimpleCallable = SimpleCallable()

is_callable: bool = callable(
    simple_callable,
)

print(is_callable)

print(
    simple_callable(),
)


# =============================================================================
# 27. callable() Does Not Mean "Function"
# =============================================================================
"""
callable() answers:

    "Can this object be called?"

It does not answer:

    "Is this object a function?"

For example:

    callable(function)

can be True.

    callable(class)

can be True.

    callable(callable_instance)

can be True.

These objects have different types but are all callable.
"""


class CallableExample:
    """
    Example callable class.
    """

    def __call__(self) -> str:
        """
        Return a message.
        """
        return "Callable"


callable_instance: CallableExample = CallableExample()

print(
    callable(callable_instance),
)

print(
    callable(CallableExample),
)

print(
    callable(greet_user),
)


# =============================================================================
# 28. Callable Objects Can Return Any Value
# =============================================================================

class StringProducer:
    """
    Produce a string.
    """

    def __call__(self) -> str:
        """
        Return a string.
        """
        return "Hello"


class NumberProducer:
    """
    Produce an integer.
    """

    def __call__(self) -> int:
        """
        Return an integer.
        """
        return 100


class ListProducer:
    """
    Produce a list.
    """

    def __call__(self) -> list[int]:
        """
        Return a list.
        """
        return [1, 2, 3]


string_producer: StringProducer = StringProducer()
number_producer: NumberProducer = NumberProducer()
list_producer: ListProducer = ListProducer()

print(
    string_producer(),
)

print(
    number_producer(),
)

print(
    list_producer(),
)


# =============================================================================
# 29. Callable Object With Keyword Arguments
# =============================================================================

class GreeterWithOptions:
    """
    Create greetings using configurable options.
    """

    def __init__(
        self,
        prefix: str,
    ) -> None:
        self.prefix: str = prefix

    def __call__(
        self,
        name: str,
        *,
        punctuation: str = "!",
    ) -> str:
        """
        Create a configurable greeting.
        """
        return (
            f"{self.prefix}, "
            f"{name}"
            f"{punctuation}"
        )


friendly_greeter: GreeterWithOptions = GreeterWithOptions(
    "Hello",
)

print(
    friendly_greeter(
        "Alex",
    ),
)

print(
    friendly_greeter(
        "Alex",
        punctuation=".",
    ),
)


# =============================================================================
# 30. Callable Object With Validation
# =============================================================================

class RangeValidator:
    """
    Validate whether a number is inside a configured range.
    """

    def __init__(
        self,
        minimum: int,
        maximum: int,
    ) -> None:
        self.minimum: int = minimum
        self.maximum: int = maximum

    def __call__(
        self,
        value: int,
    ) -> bool:
        """
        Check whether value is inside the range.
        """
        return (
            self.minimum
            <= value
            <= self.maximum
        )


age_validator: RangeValidator = RangeValidator(
    18,
    60,
)

print(
    age_validator(25),
)

print(
    age_validator(70),
)


# =============================================================================
# 31. Callable Object for Filtering
# =============================================================================

class GreaterThan:
    """
    Check whether a value is greater than a configured threshold.
    """

    def __init__(
        self,
        threshold: int,
    ) -> None:
        self.threshold: int = threshold

    def __call__(
        self,
        value: int,
    ) -> bool:
        """
        Return whether value is greater than the threshold.
        """
        return value > self.threshold


def filter_values(
    predicate: object,
    values: list[int],
) -> list[int]:
    """
    Filter values using a callable predicate.
    """
    if not callable(predicate):
        raise TypeError(
            "predicate must be callable",
        )

    filtered: list[int] = []

    for value in values:
        result: object = predicate(value)

        if not isinstance(result, bool):
            raise TypeError(
                "predicate must return bool",
            )

        if result:
            filtered.append(value)

    return filtered


greater_than_ten: GreaterThan = GreaterThan(
    10,
)

filtered_values: list[int] = filter_values(
    greater_than_ten,
    [5, 10, 15, 20],
)

print(filtered_values)


# =============================================================================
# 32. Callable Object for Sorting Keys
# =============================================================================

class StringLength:
    """
    Return the length of a string.
    """

    def __call__(
        self,
        value: str,
    ) -> int:
        """
        Return string length.
        """
        return len(value)


length_key: StringLength = StringLength()

words: list[str] = [
    "Python",
    "Go",
    "Programming",
    "SQL",
]

sorted_words: list[str] = sorted(
    words,
    key=length_key,
)

print(sorted_words)


# =============================================================================
# 33. Callable Objects and map()
# =============================================================================

class Square:
    """
    Square an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the square.
        """
        return value ** 2


square_callable: Square = Square()

numbers_for_map: list[int] = [
    1,
    2,
    3,
    4,
]

squared_numbers: list[int] = list(
    map(
        square_callable,
        numbers_for_map,
    )
)

print(squared_numbers)


# =============================================================================
# 34. Callable Objects and filter()
# =============================================================================

class IsEven:
    """
    Check whether an integer is even.
    """

    def __call__(
        self,
        value: int,
    ) -> bool:
        """
        Return whether value is even.
        """
        return value % 2 == 0


is_even: IsEven = IsEven()

numbers_for_filter: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
]

even_numbers: list[int] = list(
    filter(
        is_even,
        numbers_for_filter,
    )
)

print(even_numbers)


# =============================================================================
# 35. Callable Objects and sorted()
# =============================================================================

class AbsoluteValue:
    """
    Return the absolute value of an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the absolute value.
        """
        return abs(value)


absolute_value: AbsoluteValue = AbsoluteValue()

values_to_sort: list[int] = [
    -10,
    5,
    -2,
    8,
    -1,
]

sorted_values: list[int] = sorted(
    values_to_sort,
    key=absolute_value,
)

print(sorted_values)


# =============================================================================
# 36. Callable Objects and Function Factories
# =============================================================================

class Offset:
    """
    Add a configured offset to a value.
    """

    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount: int = amount

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add the configured offset.
        """
        return value + self.amount


add_one: Offset = Offset(
    1,
)

add_hundred: Offset = Offset(
    100,
)

print(
    add_one(10),
)

print(
    add_hundred(10),
)


# =============================================================================
# 37. Callable Objects Can Replace Simple Closures
# =============================================================================
"""
A closure can store state:

    def create_multiplier(factor: int):
        def multiply(value: int) -> int:
            return value * factor

        return multiply

A callable object can represent the same idea:

    class Multiplier:
        def __init__(self, factor: int) -> None:
            self.factor = factor

        def __call__(self, value: int) -> int:
            return value * self.factor

The class-based version makes the stored state explicit.
"""


def create_multiplier_closure(
    factor: int,
):
    """
    Create a multiplier using a closure.
    """

    def multiply(
        value: int,
    ) -> int:
        """
        Multiply using the captured factor.
        """
        return value * factor

    return multiply


closure_double = create_multiplier_closure(
    2,
)

object_double: Multiplier = Multiplier(
    2,
)

print(
    closure_double(10),
)

print(
    object_double(10),
)


# =============================================================================
# 38. Callable Objects Can Be Inspected
# =============================================================================

class InspectableCallable:
    """
    Callable object with explicit configuration.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name

    def __call__(
        self,
    ) -> str:
        """
        Return the configured name.
        """
        return self.name


inspectable: InspectableCallable = InspectableCallable(
    "Example",
)

print(
    inspectable.name,
)

print(
    inspectable(),
)


# =============================================================================
# 39. Callable Object With __repr__()
# =============================================================================

class ConfiguredMultiplier:
    """
    Callable multiplier with a useful representation.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply value by factor.
        """
        return value * self.factor

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation.
        """
        return (
            f"{type(self).__name__}("
            f"factor={self.factor!r}"
            f")"
        )


configured_multiplier: ConfiguredMultiplier = ConfiguredMultiplier(
    5,
)

print(
    configured_multiplier,
)

print(
    configured_multiplier(10),
)


# =============================================================================
# 40. Callable Object With __str__()
# =============================================================================

class NamedOperation:
    """
    Represent a named callable operation.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name

    def __call__(
        self,
        value: int,
    ) -> str:
        """
        Return a description of the operation.
        """
        return f"{self.name}: {value}"

    def __str__(self) -> str:
        """
        Return a user-friendly description.
        """
        return f"Operation<{self.name}>"


operation: NamedOperation = NamedOperation(
    "double",
)

print(
    operation,
)

print(
    operation(10),
)


# =============================================================================
# 41. Callable Object With __call__ Returning self
# =============================================================================

class FluentCounter:
    """
    Demonstrate that __call__ can return the same object.
    """

    def __init__(self) -> None:
        self.value: int = 0

    def __call__(
        self,
        amount: int = 1,
    ) -> "FluentCounter":
        """
        Increase the value and return self.
        """
        self.value += amount
        return self


fluent_counter: FluentCounter = FluentCounter()

fluent_counter(
    5,
)(
    10,
)

print(
    fluent_counter.value,
)


# =============================================================================
# 42. Callable Object Can Implement a Protocol
# =============================================================================
"""
For static typing, Python provides typing.Protocol.

A protocol can describe callable behaviour.

For example:

    class Operation(Protocol):
        def __call__(self, value: int) -> int:
            ...

Any object with a compatible __call__() method can satisfy that protocol
structurally.
"""

from typing import Protocol


class IntOperation(Protocol):
    """
    Describe an object callable with an int and returning an int.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Define the required callable interface.
        """
        ...


class Triple:
    """
    Triple an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return three times the value.
        """
        return value * 3


def execute_operation(
    operation: IntOperation,
    value: int,
) -> int:
    """
    Execute a typed callable operation.
    """
    return operation(value)


triple: Triple = Triple()

protocol_result: int = execute_operation(
    triple,
    10,
)

print(protocol_result)


# =============================================================================
# 43. Callable Object With a Typed Callable Interface
# =============================================================================

class Incrementer:
    """
    Increment an integer by a configured amount.
    """

    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount: int = amount

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Increment value.
        """
        return value + self.amount


def run_operation(
    operation: IntOperation,
    value: int,
) -> int:
    """
    Run a callable operation.
    """
    return operation(value)


increment_by_five: Incrementer = Incrementer(
    5,
)

incremented: int = run_operation(
    increment_by_five,
    10,
)

print(incremented)


# =============================================================================
# 44. Callable Object as a Strategy
# =============================================================================
"""
Callable objects are useful for the strategy pattern.

Different objects can implement the same callable interface while providing
different behaviour.
"""


class AddOperation:
    """
    Add two numbers.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Add two integers.
        """
        return first + second


class MultiplyOperation:
    """
    Multiply two numbers.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Multiply two integers.
        """
        return first * second


def execute_binary_operation(
    operation: object,
    first: int,
    second: int,
) -> int:
    """
    Execute a callable binary operation.
    """
    if not callable(operation):
        raise TypeError(
            "operation must be callable",
        )

    result: object = operation(
        first,
        second,
    )

    if not isinstance(result, int):
        raise TypeError(
            "operation must return an int",
        )

    return result


adder: AddOperation = AddOperation()
multiplier: MultiplyOperation = MultiplyOperation()

print(
    execute_binary_operation(
        adder,
        10,
        20,
    ),
)

print(
    execute_binary_operation(
        multiplier,
        10,
        20,
    ),
)


# =============================================================================
# 45. Callable Object as a Validator Pipeline
# =============================================================================

class PositiveNumberValidator:
    """
    Validate that a number is positive.
    """

    def __call__(
        self,
        value: int,
    ) -> bool:
        """
        Return whether value is positive.
        """
        return value > 0


class EvenNumberValidator:
    """
    Validate that a number is even.
    """

    def __call__(
        self,
        value: int,
    ) -> bool:
        """
        Return whether value is even.
        """
        return value % 2 == 0


def validate(
    validator: object,
    value: int,
) -> bool:
    """
    Run a callable validator.
    """
    if not callable(validator):
        raise TypeError(
            "validator must be callable",
        )

    result: object = validator(value)

    if not isinstance(result, bool):
        raise TypeError(
            "validator must return bool",
        )

    return result


positive_validator: PositiveNumberValidator = PositiveNumberValidator()
even_validator: EvenNumberValidator = EvenNumberValidator()

print(
    validate(
        positive_validator,
        10,
    ),
)

print(
    validate(
        even_validator,
        10,
    ),
)


# =============================================================================
# 46. Callable Object as a Configuration-Based Function
# =============================================================================

class DiscountCalculator:
    """
    Calculate discounts using stored configuration.
    """

    def __init__(
        self,
        discount_percentage: float,
    ) -> None:
        self.discount_percentage: float = discount_percentage

    def __call__(
        self,
        price: float,
    ) -> float:
        """
        Return the discounted price.
        """
        discount: float = (
            price
            * self.discount_percentage
            / 100.0
        )

        return price - discount


ten_percent_discount: DiscountCalculator = DiscountCalculator(
    10.0,
)

twenty_percent_discount: DiscountCalculator = DiscountCalculator(
    20.0,
)

print(
    ten_percent_discount(1000.0),
)

print(
    twenty_percent_discount(1000.0),
)


# =============================================================================
# 47. Callable Objects Can Be Stored in Variables
# =============================================================================

class SubtractOperation:
    """
    Subtract one integer from another.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Subtract second from first.
        """
        return first - second


subtract: SubtractOperation = SubtractOperation()

operation_reference: SubtractOperation = subtract

stored_result: int = operation_reference(
    20,
    5,
)

print(stored_result)


# =============================================================================
# 48. Callable Objects Can Be Stored in Lists
# =============================================================================

class AddOne:
    """
    Add one to an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add one.
        """
        return value + 1


class MultiplyByTwo:
    """
    Multiply an integer by two.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply by two.
        """
        return value * 2


operations: list[IntOperation] = [
    AddOne(),
    MultiplyByTwo(),
]

current_value: int = 10

for operation_item in operations:
    current_value = operation_item(
        current_value,
    )

print(current_value)


# =============================================================================
# 49. Callable Objects Can Be Stored in Dictionaries
# =============================================================================

class AddOperationForDictionary:
    """
    Add two integers.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Add two values.
        """
        return first + second


class MultiplyOperationForDictionary:
    """
    Multiply two integers.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Multiply two values.
        """
        return first * second


operations_by_name: dict[str, object] = {
    "add": AddOperationForDictionary(),
    "multiply": MultiplyOperationForDictionary(),
}

selected_operation: object = operations_by_name[
    "add"
]

if not callable(selected_operation):
    raise TypeError(
        "selected operation must be callable",
    )

dictionary_result: object = selected_operation(
    10,
    20,
)

print(dictionary_result)


# =============================================================================
# 50. Callable Objects and Closures Comparison
# =============================================================================

def create_adder_closure(
    amount: int,
):
    """
    Create an adder using a closure.
    """

    def add(
        value: int,
    ) -> int:
        """
        Add the captured amount.
        """
        return value + amount

    return add


class AdderObject:
    """
    Create an adder using a callable object.
    """

    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount: int = amount

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add the stored amount.
        """
        return value + self.amount


closure_adder = create_adder_closure(
    10,
)

object_adder: AdderObject = AdderObject(
    10,
)

print(
    closure_adder(20),
)

print(
    object_adder(20),
)


# =============================================================================
# 51. Callable Object With Explicit State
# =============================================================================

class PercentageCalculator:
    """
    Calculate a percentage using stored configuration.
    """

    def __init__(
        self,
        percentage: float,
    ) -> None:
        self.percentage: float = percentage

    def __call__(
        self,
        value: float,
    ) -> float:
        """
        Calculate the configured percentage.
        """
        return (
            value
            * self.percentage
            / 100.0
        )


tax_calculator: PercentageCalculator = PercentageCalculator(
    18.0,
)

tax_amount: float = tax_calculator(
    1000.0,
)

print(tax_amount)


# =============================================================================
# 52. Callable Objects and __call__ Arguments
# =============================================================================

class MessageBuilder:
    """
    Build messages using a stored application name.
    """

    def __init__(
        self,
        application_name: str,
    ) -> None:
        self.application_name: str = application_name

    def __call__(
        self,
        message: str,
        *,
        level: str = "INFO",
    ) -> str:
        """
        Build a formatted application message.
        """
        return (
            f"[{level}] "
            f"{self.application_name}: "
            f"{message}"
        )


message_builder: MessageBuilder = MessageBuilder(
    "DataPipeline",
)

print(
    message_builder(
        "Job completed",
    ),
)

print(
    message_builder(
        "Job failed",
        level="ERROR",
    ),
)


# =============================================================================
# 53. Callable Object Can Be Used Like a Function
# =============================================================================
"""
The syntax is intentionally simple:

    callable_object(argument)

This allows an object to provide function-like behaviour while still
supporting object-oriented features such as:

    - instance attributes
    - methods
    - inheritance
    - properties
    - custom representations
    - configuration
"""


class GreetingFunction:
    """
    Function-like greeting object.
    """

    def __init__(
        self,
        greeting: str,
    ) -> None:
        self.greeting: str = greeting

    def __call__(
        self,
        name: str,
    ) -> str:
        """
        Create a greeting.
        """
        return f"{self.greeting}, {name}!"


greeting_function: GreetingFunction = GreetingFunction(
    "Hello",
)

print(
    greeting_function("Alex"),
)


# =============================================================================
# 54. Callable Object With Inheritance
# =============================================================================

class BaseOperation:
    """
    Base callable operation.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the value unchanged.
        """
        return value


class DoubleOperation(BaseOperation):
    """
    Double a value.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return twice the value.
        """
        return value * 2


class TripleOperation(BaseOperation):
    """
    Triple a value.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return three times the value.
        """
        return value * 3


double_operation: DoubleOperation = DoubleOperation()
triple_operation: TripleOperation = TripleOperation()

print(
    double_operation(10),
)

print(
    triple_operation(10),
)


# =============================================================================
# 55. Callable Object and Method Resolution
# =============================================================================
"""
__call__() follows normal method lookup rules.

If a subclass overrides __call__(), the subclass implementation is used.
"""


class ParentCallable:
    """
    Parent callable object.
    """

    def __call__(
        self,
    ) -> str:
        """
        Return the parent message.
        """
        return "Parent"


class ChildCallable(ParentCallable):
    """
    Child callable object.
    """

    def __call__(
        self,
    ) -> str:
        """
        Return the child message.
        """
        return "Child"


child_callable: ChildCallable = ChildCallable()

print(
    child_callable(),
)


# =============================================================================
# 56. Callable Objects and isinstance()
# =============================================================================

class Action:
    """
    Represent a callable action.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the value unchanged.
        """
        return value


action: Action = Action()

print(
    isinstance(
        action,
        Action,
    ),
)

print(
    callable(action),
)


# =============================================================================
# 57. callable() and None
# =============================================================================

nothing: None = None

print(
    callable(nothing),
)


# Expected:
#
# False


# =============================================================================
# 58. callable() and a String
# =============================================================================

text: str = "Python"

print(
    callable(text),
)


# Expected:
#
# False


# =============================================================================
# 59. callable() and a Class
# =============================================================================

class ExampleClass:
    """
    Simple example class.
    """

    pass


print(
    callable(ExampleClass),
)


# Expected:
#
# True


# =============================================================================
# 60. Callable Objects and Type Safety
# =============================================================================
"""
When using static type checking, it is preferable to describe the expected
callable interface rather than using object everywhere.

For example:

    Callable[[int], int]

means:

    accepts one int
    returns one int

A class instance implementing:

    __call__(self, value: int) -> int

can satisfy that callable shape.
"""


from collections.abc import Callable


class SquareOperation:
    """
    Callable square operation.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the square.
        """
        return value ** 2


def execute_square(
    operation: Callable[[int], int],
    value: int,
) -> int:
    """
    Execute a callable that accepts an int and returns an int.
    """
    return operation(value)


square_operation: SquareOperation = SquareOperation()

typed_callable_result: int = execute_square(
    square_operation,
    10,
)

print(typed_callable_result)


# =============================================================================
# 61. Callable Type Annotation
# =============================================================================

def execute_callable(
    operation: Callable[[int], int],
    value: int,
) -> int:
    """
    Execute an integer operation.
    """
    return operation(value)


class AddTen:
    """
    Add ten to an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add ten.
        """
        return value + 10


add_ten_callable: AddTen = AddTen()

callable_annotation_result: int = execute_callable(
    add_ten_callable,
    50,
)

print(callable_annotation_result)


# =============================================================================
# 62. Callable Objects and map() With Static Typing
# =============================================================================

class Increment:
    """
    Increment an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Increment the value.
        """
        return value + 1


increment: Increment = Increment()

incremented_values: list[int] = list(
    map(
        increment,
        [1, 2, 3, 4],
    )
)

print(incremented_values)


# =============================================================================
# 63. Callable Object for Normalization
# =============================================================================

class Normalizer:
    """
    Normalize text using stored configuration.
    """

    def __init__(
        self,
        lowercase: bool = True,
        strip_whitespace: bool = True,
    ) -> None:
        self.lowercase: bool = lowercase
        self.strip_whitespace: bool = strip_whitespace

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Normalize a string.
        """
        result: str = value

        if self.strip_whitespace:
            result = result.strip()

        if self.lowercase:
            result = result.lower()

        return result


normalizer: Normalizer = Normalizer()

normalized_text: str = normalizer(
    "  PYTHON FUNCTIONS  ",
)

print(normalized_text)


# =============================================================================
# 64. Callable Object for Parsing
# =============================================================================

class IntegerParser:
    """
    Parse strings into integers with a fallback value.
    """

    def __init__(
        self,
        default: int,
    ) -> None:
        self.default: int = default

    def __call__(
        self,
        value: str,
    ) -> int:
        """
        Parse the value or return the configured default.
        """
        try:
            return int(value)
        except ValueError:
            return self.default


parser: IntegerParser = IntegerParser(
    0,
)

print(
    parser("100"),
)

print(
    parser("invalid"),
)


# =============================================================================
# 65. Callable Object for Caching
# =============================================================================
"""
A callable object can maintain a cache between calls.

This is useful when the operation has reusable results.
"""


class CachedSquare:
    """
    Calculate and cache squares.
    """

    def __init__(self) -> None:
        self.cache: dict[int, int] = {}

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return a cached or newly calculated square.
        """
        if value not in self.cache:
            self.cache[value] = value ** 2

        return self.cache[value]


cached_square: CachedSquare = CachedSquare()

print(
    cached_square(10),
)

print(
    cached_square(10),
)

print(
    cached_square.cache,
)


# =============================================================================
# 66. Callable Object for Logging
# =============================================================================

class Logger:
    """
    Store a logging level and create log messages.
    """

    def __init__(
        self,
        level: str,
    ) -> None:
        self.level: str = level

    def __call__(
        self,
        message: str,
    ) -> str:
        """
        Create a log message.
        """
        return f"[{self.level}] {message}"


info_logger: Logger = Logger(
    "INFO",
)

warning_logger: Logger = Logger(
    "WARNING",
)

print(
    info_logger("Application started"),
)

print(
    warning_logger("Low disk space"),
)


# =============================================================================
# 67. Callable Object for Conversion
# =============================================================================

class KilometersToMiles:
    """
    Convert kilometers to miles.
    """

    def __call__(
        self,
        kilometers: float,
    ) -> float:
        """
        Convert kilometers to miles.
        """
        return kilometers * 0.621371


kilometers_to_miles: KilometersToMiles = KilometersToMiles()

miles: float = kilometers_to_miles(
    10.0,
)

print(miles)


# =============================================================================
# 68. Callable Object for Tax Calculation
# =============================================================================

class TaxCalculator:
    """
    Calculate tax using a configured tax rate.
    """

    def __init__(
        self,
        rate: float,
    ) -> None:
        self.rate: float = rate

    def __call__(
        self,
        amount: float,
    ) -> float:
        """
        Calculate tax.
        """
        return amount * self.rate / 100.0


tax_18_percent: TaxCalculator = TaxCalculator(
    18.0,
)

tax_value: float = tax_18_percent(
    5000.0,
)

print(tax_value)


# =============================================================================
# 69. Callable Object for Currency Conversion
# =============================================================================

class CurrencyConverter:
    """
    Convert an amount using a stored exchange rate.
    """

    def __init__(
        self,
        exchange_rate: float,
    ) -> None:
        self.exchange_rate: float = exchange_rate

    def __call__(
        self,
        amount: float,
    ) -> float:
        """
        Convert the amount.
        """
        return amount * self.exchange_rate


usd_to_eur: CurrencyConverter = CurrencyConverter(
    0.92,
)

converted_amount: float = usd_to_eur(
    100.0,
)

print(converted_amount)


# =============================================================================
# 70. Callable Object as a Command
# =============================================================================

class PrintCommand:
    """
    Represent a callable command.
    """

    def __init__(
        self,
        message: str,
    ) -> None:
        self.message: str = message

    def __call__(self) -> None:
        """
        Execute the command.
        """
        print(self.message)


command: PrintCommand = PrintCommand(
    "Command executed",
)

command()


# =============================================================================
# 71. Callable Object With Lifecycle State
# =============================================================================

class Job:
    """
    Represent a callable job.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name
        self.executed: bool = False

    def __call__(self) -> str:
        """
        Execute the job.
        """
        self.executed = True

        return f"Executed: {self.name}"


job: Job = Job(
    "Data processing",
)

print(
    job.executed,
)

print(
    job(),
)

print(
    job.executed,
)


# =============================================================================
# 72. Callable Object With Arguments and State
# =============================================================================

class RequestCounter:
    """
    Count requests received by the callable object.
    """

    def __init__(
        self,
    ) -> None:
        self.count: int = 0

    def __call__(
        self,
        request_name: str,
    ) -> str:
        """
        Count and describe a request.
        """
        self.count += 1

        return (
            f"Request {self.count}: "
            f"{request_name}"
        )


request_counter: RequestCounter = RequestCounter()

print(
    request_counter("login"),
)

print(
    request_counter("profile"),
)

print(
    request_counter("logout"),
)


# =============================================================================
# 73. Callable Object With Different Instances
# =============================================================================

class Greeting:
    """
    Store a greeting word.
    """

    def __init__(
        self,
        greeting: str,
    ) -> None:
        self.greeting: str = greeting

    def __call__(
        self,
        name: str,
    ) -> str:
        """
        Return the configured greeting.
        """
        return f"{self.greeting}, {name}!"


hello: Greeting = Greeting(
    "Hello",
)

welcome_greeting: Greeting = Greeting(
    "Welcome",
)

print(
    hello("Alex"),
)

print(
    welcome_greeting("Alex"),
)


# =============================================================================
# 74. Callable Object as a Parser Pipeline
# =============================================================================

class StripText:
    """
    Remove surrounding whitespace.
    """

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Strip surrounding whitespace.
        """
        return value.strip()


class LowerText:
    """
    Convert text to lowercase.
    """

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Convert text to lowercase.
        """
        return value.lower()


def apply_text_operation(
    operation: Callable[[str], str],
    value: str,
) -> str:
    """
    Apply a string transformation.
    """
    return operation(value)


strip_text: StripText = StripText()
lower_text: LowerText = LowerText()

pipeline_value: str = "  PYTHON  "

pipeline_value = apply_text_operation(
    strip_text,
    pipeline_value,
)

pipeline_value = apply_text_operation(
    lower_text,
    pipeline_value,
)

print(pipeline_value)


# =============================================================================
# 75. Callable Object With Internal Validation
# =============================================================================

class SafeDivider:
    """
    Divide numbers while protecting against division by zero.
    """

    def __call__(
        self,
        numerator: float,
        denominator: float,
    ) -> float:
        """
        Divide numerator by denominator.
        """
        if denominator == 0:
            raise ValueError(
                "denominator cannot be zero",
            )

        return numerator / denominator


safe_divider: SafeDivider = SafeDivider()

division_result: float = safe_divider(
    100.0,
    4.0,
)

print(division_result)


# =============================================================================
# 76. Callable Object Can Raise Exceptions
# =============================================================================

class PositiveOnly:
    """
    Accept only positive integers.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return value if it is positive.
        """
        if value <= 0:
            raise ValueError(
                "value must be positive",
            )

        return value


positive_only: PositiveOnly = PositiveOnly()

positive_value: int = positive_only(
    10,
)

print(positive_value)


# =============================================================================
# 77. Callable Object and Exception Handling
# =============================================================================

try:
    positive_only(
        -10,
    )
except ValueError as error:
    print(
        f"Validation error: {error}",
    )


# =============================================================================
# 78. Callable Objects and __name__
# =============================================================================
"""
Normal functions have useful attributes such as __name__.

Instances of callable classes do not automatically have a __name__
attribute.

Instead, callable objects can expose their own descriptive attributes.
"""


class NamedCallable:
    """
    Callable object with an explicit name.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name

    def __call__(
        self,
    ) -> str:
        """
        Return the configured name.
        """
        return self.name


named_callable: NamedCallable = NamedCallable(
    "example_operation",
)

print(
    named_callable.name,
)


# =============================================================================
# 79. Callable Objects and inspect-like Metadata
# =============================================================================
"""
Callable objects can expose configuration through normal attributes.

This can be useful when debugging or building configurable systems.
"""


class Operation:
    """
    Callable operation with metadata.
    """

    def __init__(
        self,
        name: str,
        multiplier: int,
    ) -> None:
        self.name: str = name
        self.multiplier: int = multiplier

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Apply the configured multiplier.
        """
        return value * self.multiplier


operation_with_metadata: Operation = Operation(
    "double",
    2,
)

print(
    operation_with_metadata.name,
)

print(
    operation_with_metadata.multiplier,
)

print(
    operation_with_metadata(10),
)


# =============================================================================
# 80. Callable Objects and Encapsulation
# =============================================================================
"""
Callable objects can encapsulate:

    - configuration
    - state
    - behaviour

Example:

    calculator.factor

stores configuration.

    calculator(value)

executes behaviour.

This combines data and operation into one object.
"""


class ConfiguredOperation:
    """
    Encapsulate a multiplication operation.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Apply the configured operation.
        """
        return value * self.factor


configured_operation: ConfiguredOperation = ConfiguredOperation(
    10,
)

print(
    configured_operation(5),
)


# =============================================================================
# 81. Callable Objects and Dependency Injection
# =============================================================================
"""
A callable object can be supplied as a dependency.

The receiving function does not need to know whether it received:

    - a normal function
    - a lambda
    - a callable class instance
"""


class PriceCalculator:
    """
    Calculate a price using a configured multiplier.
    """

    def __init__(
        self,
        multiplier: float,
    ) -> None:
        self.multiplier: float = multiplier

    def __call__(
        self,
        price: float,
    ) -> float:
        """
        Apply the configured multiplier.
        """
        return price * self.multiplier


def calculate_price(
    calculator: Callable[[float], float],
    price: float,
) -> float:
    """
    Calculate a price using an injected callable.
    """
    return calculator(price)


price_calculator: PriceCalculator = PriceCalculator(
    1.18,
)

final_price: float = calculate_price(
    price_calculator,
    1000.0,
)

print(final_price)


# =============================================================================
# 82. Callable Object as a Service
# =============================================================================

class EmailFormatter:
    """
    Format an email subject using a stored application name.
    """

    def __init__(
        self,
        application_name: str,
    ) -> None:
        self.application_name: str = application_name

    def __call__(
        self,
        subject: str,
    ) -> str:
        """
        Format an email subject.
        """
        return (
            f"[{self.application_name}] "
            f"{subject}"
        )


email_formatter: EmailFormatter = EmailFormatter(
    "DataPipeline",
)

email_subject: str = email_formatter(
    "Daily Report",
)

print(email_subject)


# =============================================================================
# 83. Callable Object for Retry Configuration
# =============================================================================

class RetryPolicy:
    """
    Store a retry configuration.
    """

    def __init__(
        self,
        maximum_attempts: int,
    ) -> None:
        self.maximum_attempts: int = maximum_attempts

    def __call__(
        self,
        attempts: int,
    ) -> bool:
        """
        Return whether another attempt is allowed.
        """
        return attempts < self.maximum_attempts


retry_policy: RetryPolicy = RetryPolicy(
    3,
)

print(
    retry_policy(0),
)

print(
    retry_policy(2),
)

print(
    retry_policy(3),
)


# =============================================================================
# 84. Callable Object as a Predicate
# =============================================================================

class StartsWith:
    """
    Check whether text starts with a configured prefix.
    """

    def __init__(
        self,
        prefix: str,
    ) -> None:
        self.prefix: str = prefix

    def __call__(
        self,
        value: str,
    ) -> bool:
        """
        Return whether value starts with prefix.
        """
        return value.startswith(
            self.prefix,
        )


starts_with_py: StartsWith = StartsWith(
    "Py",
)

print(
    starts_with_py("Python"),
)

print(
    starts_with_py("Java"),
)


# =============================================================================
# 85. Callable Object as a Transformer
# =============================================================================

class UpperCase:
    """
    Transform text to uppercase.
    """

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Return uppercase text.
        """
        return value.upper()


upper_case: UpperCase = UpperCase()

transformed_text: str = upper_case(
    "python",
)

print(transformed_text)


# =============================================================================
# 86. Callable Object as a Reducer
# =============================================================================

class Add:
    """
    Add two integers.
    """

    def __call__(
        self,
        first: int,
        second: int,
    ) -> int:
        """
        Add two values.
        """
        return first + second


def reduce_values(
    operation: Callable[[int, int], int],
    values: list[int],
) -> int:
    """
    Reduce a list using a binary callable.
    """
    if not values:
        raise ValueError(
            "values cannot be empty",
        )

    result: int = values[0]

    for value in values[1:]:
        result = operation(
            result,
            value,
        )

    return result


add_operation: Add = Add()

reduced_total: int = reduce_values(
    add_operation,
    [1, 2, 3, 4],
)

print(reduced_total)


# =============================================================================
# 87. Callable Object and Composition
# =============================================================================

class DoubleValue:
    """
    Double an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Double the value.
        """
        return value * 2


class AddThree:
    """
    Add three to an integer.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add three.
        """
        return value + 3


def compose_operations(
    first: Callable[[int], int],
    second: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Compose two integer operations.
    """

    def composed(
        value: int,
    ) -> int:
        """
        Apply first operation and then second operation.
        """
        return second(
            first(value),
        )

    return composed


double_value: DoubleValue = DoubleValue()
add_three: AddThree = AddThree()

double_then_add_three: Callable[[int], int] = compose_operations(
    double_value,
    add_three,
)

composition_result: int = double_then_add_three(
    10,
)

print(composition_result)


# =============================================================================
# 88. Callable Object and Decorator Pattern
# =============================================================================
"""
Callable classes can also be used to implement decorators.

A decorator object can receive a function and later call that function.
"""


from collections.abc import Callable
from functools import wraps
from typing import Any


class CallLogger:
    """
    Log calls to a wrapped function.
    """

    def __init__(
        self,
        function: Callable[..., Any],
    ) -> None:
        self.function: Callable[..., Any] = function

        wraps(function)(
            self,
        )

    def __call__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Call the wrapped function.
        """
        print(
            f"Calling {self.function.__name__}",
        )

        return self.function(
            *args,
            **kwargs,
        )


@CallLogger
def greet_with_logging(
    name: str,
) -> str:
    """
    Return a greeting.
    """
    return f"Hello, {name}!"


logged_greeting: str = greet_with_logging(
    "Alex",
)

print(logged_greeting)


# =============================================================================
# 89. Callable Decorator Object With State
# =============================================================================

class CallCounterDecorator:
    """
    Count calls to a wrapped function.
    """

    def __init__(
        self,
        function: Callable[..., Any],
    ) -> None:
        self.function: Callable[..., Any] = function
        self.call_count: int = 0

        wraps(function)(
            self,
        )

    def __call__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Count and execute the wrapped function.
        """
        self.call_count += 1

        return self.function(
            *args,
            **kwargs,
        )


@CallCounterDecorator
def add_for_decorator(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


print(
    add_for_decorator(
        10,
        20,
    ),
)

print(
    add_for_decorator(
        30,
        40,
    ),
)

print(
    add_for_decorator.call_count,
)


# =============================================================================
# 90. Callable Object and Function Attributes
# =============================================================================
"""
Callable objects can have attributes just like other Python objects.

This makes them useful when the callable needs associated metadata.
"""


class TaggedOperation:
    """
    Callable operation with a tag.
    """

    def __init__(
        self,
        tag: str,
    ) -> None:
        self.tag: str = tag

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the value unchanged.
        """
        return value


tagged_operation: TaggedOperation = TaggedOperation(
    "production",
)

print(
    tagged_operation.tag,
)

print(
    tagged_operation(100),
)


# =============================================================================
# 91. Callable Object for State Machine-Like Behaviour
# =============================================================================

class Toggle:
    """
    Toggle between True and False on every call.
    """

    def __init__(
        self,
        initial: bool = False,
    ) -> None:
        self.state: bool = initial

    def __call__(self) -> bool:
        """
        Toggle and return the current state.
        """
        self.state = not self.state
        return self.state


toggle: Toggle = Toggle()

print(toggle())
print(toggle())
print(toggle())
print(toggle())


# =============================================================================
# 92. Callable Object With Explicit Reset
# =============================================================================

class ToggleWithReset:
    """
    Toggle state with reset support.
    """

    def __init__(
        self,
        initial: bool = False,
    ) -> None:
        self.initial: bool = initial
        self.state: bool = initial

    def __call__(self) -> bool:
        """
        Toggle and return the state.
        """
        self.state = not self.state
        return self.state

    def reset(self) -> None:
        """
        Restore the initial state.
        """
        self.state = self.initial


toggle_with_reset: ToggleWithReset = ToggleWithReset()

print(
    toggle_with_reset(),
)

print(
    toggle_with_reset(),
)

toggle_with_reset.reset()

print(
    toggle_with_reset(),
)


# =============================================================================
# 93. Callable Object and Resource-Like Behaviour
# =============================================================================

class QueryBuilder:
    """
    Build simple query strings using stored configuration.
    """

    def __init__(
        self,
        table: str,
    ) -> None:
        self.table: str = table

    def __call__(
        self,
        column: str,
        value: str,
    ) -> str:
        """
        Build a simple query string.
        """
        return (
            f"SELECT * FROM {self.table} "
            f"WHERE {column} = '{value}'"
        )


query_builder: QueryBuilder = QueryBuilder(
    "users",
)

query: str = query_builder(
    "name",
    "Alex",
)

print(query)


# =============================================================================
# 94. Callable Object With Multiple Behaviours
# =============================================================================

class NumberProcessor:
    """
    Process numbers using a configured operation.
    """

    def __init__(
        self,
        operation: str,
    ) -> None:
        allowed_operations: set[str] = {
            "double",
            "square",
        }

        if operation not in allowed_operations:
            raise ValueError(
                f"Unsupported operation: {operation}",
            )

        self.operation: str = operation

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Apply the configured operation.
        """
        if self.operation == "double":
            return value * 2

        return value ** 2


double_processor: NumberProcessor = NumberProcessor(
    "double",
)

square_processor: NumberProcessor = NumberProcessor(
    "square",
)

print(
    double_processor(10),
)

print(
    square_processor(10),
)


# =============================================================================
# 95. Callable Object as a Small State Machine
# =============================================================================

class TrafficLight:
    """
    Cycle through traffic-light states.
    """

    def __init__(self) -> None:
        self.states: tuple[str, ...] = (
            "red",
            "green",
            "yellow",
        )
        self.index: int = 0

    def __call__(self) -> str:
        """
        Move to and return the next state.
        """
        state: str = self.states[self.index]

        self.index = (
            self.index + 1
        ) % len(self.states)

        return state


traffic_light: TrafficLight = TrafficLight()

print(
    traffic_light(),
)

print(
    traffic_light(),
)

print(
    traffic_light(),
)

print(
    traffic_light(),
)


# =============================================================================
# 96. Callable Object and Explicit Interface
# =============================================================================
"""
A callable object is often useful when the object represents a concept
that naturally behaves like an operation.

Good examples include:

    - Validators
    - Parsers
    - Formatters
    - Converters
    - Calculators
    - Counters
    - Predicates
    - Strategies
    - Commands
    - Stateful transformations
    - Decorators
"""


class EmailValidator:
    """
    Validate a basic email-like string.
    """

    def __call__(
        self,
        email: str,
    ) -> bool:
        """
        Return whether the email contains a basic required pattern.
        """
        return (
            "@" in email
            and "." in email
        )


email_validator: EmailValidator = EmailValidator()

print(
    email_validator("user@example.com"),
)

print(
    email_validator("invalid"),
)


# =============================================================================
# 97. Callable Object Versus Class Method
# =============================================================================

class MathTools:
    """
    Provide mathematical operations through methods.
    """

    def double(
        self,
        value: int,
    ) -> int:
        """
        Double a value.
        """
        return value * 2


class DoubleCallable:
    """
    Provide mathematical behaviour through __call__().
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Double a value.
        """
        return value * 2


math_tools: MathTools = MathTools()
double_callable: DoubleCallable = DoubleCallable()

method_result: int = math_tools.double(
    10,
)

callable_result: int = double_callable(
    10,
)

print(method_result)
print(callable_result)


# The method version communicates:
#
#     math_tools.double(value)
#
# The callable-object version communicates:
#
#     double_callable(value)
#
# A callable object is useful when the object itself represents the
# operation.


# =============================================================================
# 98. Callable Object and Object Identity
# =============================================================================

class IdentityOperation:
    """
    Return the supplied object unchanged.
    """

    def __call__(
        self,
        value: object,
    ) -> object:
        """
        Return value unchanged.
        """
        return value


identity_operation: IdentityOperation = IdentityOperation()

sample_object: list[int] = [
    1,
    2,
    3,
]

returned_object: object = identity_operation(
    sample_object,
)

print(
    returned_object is sample_object,
)


# Expected:
#
# True


# =============================================================================
# 99. Callable Object and Mutable State
# =============================================================================

class History:
    """
    Store every value supplied to the callable object.
    """

    def __init__(self) -> None:
        self.values: list[int] = []

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Store and return the value.
        """
        self.values.append(value)
        return value


history: History = History()

history(10)
history(20)
history(30)

print(
    history.values,
)


# =============================================================================
# 100. Callable Object as a Collector
# =============================================================================

class Collector:
    """
    Collect strings supplied through calls.
    """

    def __init__(self) -> None:
        self.items: list[str] = []

    def __call__(
        self,
        item: str,
    ) -> None:
        """
        Store an item.
        """
        self.items.append(item)


collector: Collector = Collector()

collector("Python")
collector("Functions")
collector("Callable Objects")

print(
    collector.items,
)


# =============================================================================
# 101. Callable Object With a Maximum Value
# =============================================================================

class ClampedValue:
    """
    Clamp values between configured minimum and maximum values.
    """

    def __init__(
        self,
        minimum: int,
        maximum: int,
    ) -> None:
        if minimum > maximum:
            raise ValueError(
                "minimum cannot be greater than maximum",
            )

        self.minimum: int = minimum
        self.maximum: int = maximum

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Clamp value to the configured range.
        """
        return max(
            self.minimum,
            min(
                value,
                self.maximum,
            ),
        )


clamp: ClampedValue = ClampedValue(
    0,
    100,
)

print(
    clamp(-10),
)

print(
    clamp(50),
)

print(
    clamp(150),
)


# =============================================================================
# 102. Callable Object for Pagination
# =============================================================================

class Paginator:
    """
    Return a configured page from a list.
    """

    def __init__(
        self,
        page_size: int,
    ) -> None:
        if page_size <= 0:
            raise ValueError(
                "page_size must be positive",
            )

        self.page_size: int = page_size

    def __call__(
        self,
        values: list[int],
        page_number: int,
    ) -> list[int]:
        """
        Return values belonging to the requested page.
        """
        if page_number <= 0:
            raise ValueError(
                "page_number must be positive",
            )

        start: int = (
            page_number - 1
        ) * self.page_size

        end: int = (
            start + self.page_size
        )

        return values[start:end]


paginator: Paginator = Paginator(
    3,
)

page: list[int] = paginator(
    [1, 2, 3, 4, 5, 6, 7],
    2,
)

print(page)


# =============================================================================
# 103. Callable Object for Batching
# =============================================================================

class BatchProcessor:
    """
    Process values in batches of a configured size.
    """

    def __init__(
        self,
        batch_size: int,
    ) -> None:
        if batch_size <= 0:
            raise ValueError(
                "batch_size must be positive",
            )

        self.batch_size: int = batch_size

    def __call__(
        self,
        values: list[int],
    ) -> list[list[int]]:
        """
        Split values into batches.
        """
        batches: list[list[int]] = []

        for start in range(
            0,
            len(values),
            self.batch_size,
        ):
            end: int = (
                start + self.batch_size
            )

            batches.append(
                values[start:end],
            )

        return batches


batch_processor: BatchProcessor = BatchProcessor(
    3,
)

batches: list[list[int]] = batch_processor(
    [1, 2, 3, 4, 5, 6, 7],
)

print(batches)


# =============================================================================
# 104. Callable Object for String Replacement
# =============================================================================

class Replacer:
    """
    Replace one configured string with another.
    """

    def __init__(
        self,
        old: str,
        new: str,
    ) -> None:
        self.old: str = old
        self.new: str = new

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Replace configured text.
        """
        return value.replace(
            self.old,
            self.new,
        )


python_to_go: Replacer = Replacer(
    "Python",
    "Go",
)

replacement_result: str = python_to_go(
    "Python is a programming language.",
)

print(replacement_result)


# =============================================================================
# 105. Callable Object for Prefix and Suffix
# =============================================================================

class Wrapper:
    """
    Wrap text with a configured prefix and suffix.
    """

    def __init__(
        self,
        prefix: str,
        suffix: str,
    ) -> None:
        self.prefix: str = prefix
        self.suffix: str = suffix

    def __call__(
        self,
        value: str,
    ) -> str:
        """
        Wrap the supplied value.
        """
        return (
            f"{self.prefix}"
            f"{value}"
            f"{self.suffix}"
        )


markdown_code: Wrapper = Wrapper(
    "`",
    "`",
)

wrapped_value: str = markdown_code(
    "Python",
)

print(wrapped_value)


# =============================================================================
# 106. Callable Object for Reusable Business Rules
# =============================================================================

class MinimumOrderValue:
    """
    Validate a minimum order value.
    """

    def __init__(
        self,
        minimum_value: float,
    ) -> None:
        self.minimum_value: float = minimum_value

    def __call__(
        self,
        order_value: float,
    ) -> bool:
        """
        Check whether an order meets the minimum value.
        """
        return order_value >= self.minimum_value


minimum_order: MinimumOrderValue = MinimumOrderValue(
    500.0,
)

print(
    minimum_order(400.0),
)

print(
    minimum_order(500.0),
)

print(
    minimum_order(750.0),
)


# =============================================================================
# 107. Callable Objects and Composition Pipeline
# =============================================================================

class AddFive:
    """
    Add five.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add five to value.
        """
        return value + 5


class MultiplyByThree:
    """
    Multiply by three.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply value by three.
        """
        return value * 3


pipeline_operations: list[IntOperation] = [
    AddFive(),
    MultiplyByThree(),
]

pipeline_result: int = 10

for pipeline_operation in pipeline_operations:
    pipeline_result = pipeline_operation(
        pipeline_result,
    )

print(pipeline_result)


# =============================================================================
# 108. Callable Objects and Explicit State Flow
# =============================================================================

class StateTransformer:
    """
    Transform an integer and store the number of transformations.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor
        self.transformations: int = 0

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Transform value and count the transformation.
        """
        self.transformations += 1

        return value * self.factor


state_transformer: StateTransformer = StateTransformer(
    2,
)

print(
    state_transformer(5),
)

print(
    state_transformer(10),
)

print(
    state_transformer.transformations,
)


# =============================================================================
# 109. When To Use a Callable Object
# =============================================================================
"""
Callable objects are especially useful when:

    1. The operation needs persistent state.

    2. The operation has configuration.

    3. The operation has several related methods.

    4. The operation should behave like a function.

    5. The object needs metadata.

    6. The object will be passed as a callable strategy.

    7. The object participates in a larger object-oriented design.

For a simple stateless operation, a normal function is often clearer.

Example:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

For a configurable or stateful operation, a callable class may be more
appropriate.
"""


# =============================================================================
# 110. When Not To Use a Callable Object
# =============================================================================
"""
Do not create a callable class merely because __call__() exists.

For very simple behaviour, prefer a normal function.

Instead of:

    class Add:
        def __call__(
            self,
            first: int,
            second: int,
        ) -> int:
            return first + second

a normal function may be clearer:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

Callable objects become more useful when the object needs:

    - state
    - configuration
    - metadata
    - related methods
    - lifecycle behaviour
    - reusable strategy behaviour
"""


# =============================================================================
# 111. Function Versus Callable Object
# =============================================================================

def function_multiplier(
    value: int,
) -> int:
    """
    Multiply a value by two.
    """
    return value * 2


class ObjectMultiplier:
    """
    Multiply values using a callable object.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply value by the configured factor.
        """
        return value * self.factor


object_multiplier: ObjectMultiplier = ObjectMultiplier(
    2,
)

print(
    function_multiplier(10),
)

print(
    object_multiplier(10),
)


# =============================================================================
# 112. Callable Object Core Example
# =============================================================================

class CalculatorCallable:
    """
    A simple callable calculator.
    """

    def __init__(
        self,
        multiplier: int,
    ) -> None:
        self.multiplier: int = multiplier

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply value using stored configuration.
        """
        return value * self.multiplier


calculator_callable: CalculatorCallable = CalculatorCallable(
    10,
)

print(
    calculator_callable(5),
)

print(
    callable(calculator_callable),
)


# =============================================================================
# 113. Complete Practical Example
# =============================================================================

class PriceProcessor:
    """
    Process prices using configurable tax and discount rates.
    """

    def __init__(
        self,
        discount_percentage: float,
        tax_percentage: float,
    ) -> None:
        self.discount_percentage: float = discount_percentage
        self.tax_percentage: float = tax_percentage

    def __call__(
        self,
        price: float,
    ) -> float:
        """
        Apply discount and then tax.
        """
        discount: float = (
            price
            * self.discount_percentage
            / 100.0
        )

        discounted_price: float = (
            price
            - discount
        )

        tax: float = (
            discounted_price
            * self.tax_percentage
            / 100.0
        )

        final_price: float = (
            discounted_price
            + tax
        )

        return final_price


price_processor: PriceProcessor = PriceProcessor(
    discount_percentage=10.0,
    tax_percentage=18.0,
)

processed_price: float = price_processor(
    1000.0,
)

print(processed_price)


# =============================================================================
# 114. Practical Example With a Callable Interface
# =============================================================================

class Processor(Protocol):
    """
    Describe a callable integer processor.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Process an integer.
        """
        ...


class AddProcessor:
    """
    Add a configured amount.
    """

    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount: int = amount

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Add the configured amount.
        """
        return value + self.amount


class MultiplyProcessor:
    """
    Multiply by a configured factor.
    """

    def __init__(
        self,
        factor: int,
    ) -> None:
        self.factor: int = factor

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Multiply by the configured factor.
        """
        return value * self.factor


def process_value(
    processor: Processor,
    value: int,
) -> int:
    """
    Process an integer using a callable object.
    """
    return processor(value)


add_processor: AddProcessor = AddProcessor(
    5,
)

multiply_processor: MultiplyProcessor = MultiplyProcessor(
    3,
)

print(
    process_value(
        add_processor,
        10,
    ),
)

print(
    process_value(
        multiply_processor,
        10,
    ),
)


# =============================================================================
# 115. Important __call__ Rules
# =============================================================================
"""
Important rules:

    1. __call__() is a special method.

    2. Defining __call__() makes instances callable.

    3. The syntax:

           instance(...)

       invokes the callable behaviour.

    4. __call__() can accept parameters.

    5. __call__() can return any appropriate value.

    6. A callable object can store state in instance attributes.

    7. Different instances can maintain different state.

    8. callable(instance) can be used to test whether an instance is
       callable.

    9. Callable objects can be passed to higher-order functions.

    10. Callable objects can be used with APIs such as map(), filter(),
        sorted(), and custom higher-order functions.

    11. Callable objects can implement protocols such as:

            Callable[[int], int]

    12. Callable objects can also provide normal methods.

    13. Callable objects are especially useful for configurable or
        stateful operations.
"""


# =============================================================================
# 116. Common Mistakes
# =============================================================================
"""
Common mistakes include:

    - Forgetting to define __call__().
    - Defining __call__() with the wrong parameters.
    - Forgetting self in __call__().
    - Assuming every object is callable.
    - Confusing a class with an instance.
    - Using a callable class when a simple function would be clearer.
    - Forgetting that callable() checks callability, not a specific type.
    - Accidentally sharing mutable class-level state between instances.
    - Using excessive state inside callable objects.
    - Using object instead of a precise Callable type when static typing
      matters.
"""


# =============================================================================
# 117. Correct __call__ Structure
# =============================================================================

class CorrectCallable:
    """
    Demonstrate the standard __call__ structure.
    """

    def __call__(
        self,
        value: int,
    ) -> int:
        """
        Return the supplied value.
        """
        return value


correct_callable: CorrectCallable = CorrectCallable()

correct_result: int = correct_callable(
    100,
)

print(correct_result)


# =============================================================================
# 118. Callable Object Checklist
# =============================================================================
"""
Before creating a callable object, ask:

    - Does this object represent an operation?
    - Does the operation need stored state?
    - Does the operation need configuration?
    - Should the object itself behave like a function?
    - Will the object be passed to another function?
    - Would a normal function be simpler?
    - Does the object need additional methods?
    - Does the object need metadata?
    - Can the callable interface be described with Callable or Protocol?
"""


# =============================================================================
# 119. Final Callable Object Example
# =============================================================================

class ScoreCalculator:
    """
    Calculate scores using configurable points and multiplier.
    """

    def __init__(
        self,
        base_points: int,
        multiplier: int,
    ) -> None:
        self.base_points: int = base_points
        self.multiplier: int = multiplier

    def __call__(
        self,
        score: int,
    ) -> int:
        """
        Calculate the final score.
        """
        adjusted_score: int = (
            score
            + self.base_points
        )

        final_score: int = (
            adjusted_score
            * self.multiplier
        )

        return final_score


score_calculator: ScoreCalculator = ScoreCalculator(
    base_points=10,
    multiplier=2,
)

final_score: int = score_calculator(
    50,
)

print(final_score)

print(
    callable(score_calculator),
)


# =============================================================================
# 120. Callable Objects Summary
# =============================================================================
"""
Callable objects are objects that can be invoked using parentheses.

The fundamental mechanism is:

    __call__()

Example:

    class Greeter:
        def __call__(
            self,
            name: str,
        ) -> str:
            return f"Hello, {name}!"

    greeter = Greeter()

    greeter("Alex")

The important concepts are:

    Callable object
        ↓
    class defines __call__()
        ↓
    instance becomes callable
        ↓
    instance(...)
        ↓
    __call__(...)

Callable objects are useful because they combine:

    object state
        +
    object configuration
        +
    function-like syntax

Typical use cases include:

    - Validators
    - Parsers
    - Formatters
    - Converters
    - Calculators
    - Predicates
    - Strategies
    - Commands
    - Counters
    - Stateful transformations
    - Function factories
    - Decorators
    - Caching
    - Business rules

The core model:

    OBJECT
      |
      +-- attributes/state
      |
      +-- normal methods
      |
      +-- __call__()
             |
             +-- object(...)

The most important distinction is:

    normal object
        ↓
    object(...)
        ↓
    TypeError if not callable

    object with __call__()
        ↓
    object(...)
        ↓
    __call__(...)

Callable objects allow Python classes to behave like functions while
retaining the full capabilities of objects.
"""


# =============================================================================
# Key Takeaways
# =============================================================================
"""
✓ A callable object is an object that can be called using parentheses.

✓ Functions are callable objects.

✓ Classes are callable because calling a class creates an instance.

✓ Instances become callable when their class defines __call__().

✓ The callable() built-in checks whether an object is callable.

✓ __call__() is a special method.

✓ __call__() can accept parameters.

✓ __call__() can return values.

✓ Callable objects can maintain state.

✓ Callable objects can store configuration.

✓ Separate callable instances can maintain separate state.

✓ Callable objects can also provide normal methods.

✓ Callable objects can be passed to higher-order functions.

✓ Callable objects work naturally with map(), filter(), sorted(), and
  custom higher-order functions.

✓ Callable objects can implement Callable type interfaces.

✓ Protocol can describe a callable object's interface.

✓ Callable objects can be used as strategies.

✓ Callable objects can be used as validators.

✓ Callable objects can be used as parsers.

✓ Callable objects can be used as formatters.

✓ Callable objects can be used as converters.

✓ Callable objects can be used as counters.

✓ Callable objects can be used as stateful transformations.

✓ Callable objects can implement decorators.

✓ A callable object is not necessarily a function.

✓ callable() checks whether something can be called; it does not check
  whether something is specifically a function.

✓ A simple stateless operation is often clearer as a normal function.

✓ A configurable or stateful operation is often a good candidate for a
  callable object.

Core syntax:

    class MyCallable:
        def __call__(
            self,
            value: int,
        ) -> int:
            return value * 2


    operation: MyCallable = MyCallable()

    result: int = operation(
        10,
    )


Core relationship:

    class
      ↓
    __call__()
      ↓
    instance
      ↓
    instance(...)
      ↓
    __call__(...)


Final idea:

    FUNCTION
        ↓
    simple callable behaviour

    CALLABLE OBJECT
        ↓
    callable behaviour
        +
    state
        +
    configuration
        +
    methods
        +
    metadata

A callable object is therefore a powerful way to create reusable,
configurable, and stateful function-like behaviour in Python.
"""


# =============================================================================
# End of 20_callable_objects.py
# =============================================================================