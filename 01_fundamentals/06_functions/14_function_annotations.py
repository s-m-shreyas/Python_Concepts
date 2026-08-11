# =============================================================================
# 14. Function Annotations
# =============================================================================
# type: ignore

"""
Python Functions

File:
14_function_annotations.py

Topic:
Function Annotations

Overview:
Function annotations allow developers to attach metadata to function
parameters and return values.

Annotations are commonly used to describe expected types.

Example:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

Annotations improve readability, editor support, static type checking,
documentation, and maintainability.

Important:
Python does not normally enforce function annotations at runtime.

The annotation:

    first: int

does not automatically prevent a different type from being passed.

A type checker such as mypy or an IDE such as Pylance can use annotations
to detect potential type-related problems.

Topics covered:

- What are function annotations?
- Parameter annotations
- Return annotations
- Multiple parameter annotations
- Variables and annotations
- Annotation syntax
- String annotations
- Built-in generic types
- List annotations
- Dictionary annotations
- Tuple annotations
- Set annotations
- Optional values
- Union types
- Type aliases
- Callable annotations
- Any
- None return annotations
- Functions accepting other functions
- Functions returning functions
- Annotating *args
- Annotating **kwargs
- Keyword-only parameters
- Positional-only parameters
- Default values with annotations
- Annotations do not enforce types
- Runtime inspection of annotations
- __annotations__
- inspect.signature
- Forward references
- from __future__ import annotations
- Generic collections
- Iterable
- Sequence
- Mapping
- TypeVar
- Generic functions
- Type checking concepts
- Common annotation mistakes
- Practical annotation patterns
"""

# =============================================================================
# 01. Basic Function Annotation
# =============================================================================


def greet() -> str:
    """
    Return a greeting.
    """
    return "Hello, Python!"


greeting: str = greet()

print(greeting)


# =============================================================================
# 02. Parameter Annotation
# =============================================================================


def greet_user(
    name: str,
) -> str:
    """
    Return a greeting for a user.
    """
    return f"Hello, {name}!"


user_greeting: str = greet_user(
    "Shreyas",
)

print(user_greeting)


# =============================================================================
# 03. Multiple Parameter Annotations
# =============================================================================


def add_numbers(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


addition_result: int = add_numbers(
    10,
    20,
)

print(addition_result)


# =============================================================================
# 04. Return Annotation
# =============================================================================


def calculate_square(
    number: int,
) -> int:
    """
    Return the square of an integer.
    """
    result: int = number ** 2

    return result


square_result: int = calculate_square(
    5,
)

print(square_result)


# =============================================================================
# 05. Float Annotations
# =============================================================================


def calculate_area(
    width: float,
    height: float,
) -> float:
    """
    Calculate the area of a rectangle.
    """
    area: float = width * height

    return area


rectangle_area: float = calculate_area(
    10.5,
    5.0,
)

print(rectangle_area)


# =============================================================================
# 06. String Annotations
# =============================================================================


def format_name(
    first_name: str,
    last_name: str,
) -> str:
    """
    Combine a first name and last name.
    """
    full_name: str = f"{first_name} {last_name}"

    return full_name


formatted_name: str = format_name(
    "Shreyas",
    "Kumar",
)

print(formatted_name)


# =============================================================================
# 07. Boolean Annotations
# =============================================================================


def is_positive(
    number: int,
) -> bool:
    """
    Check whether a number is positive.
    """
    return number > 0


positive_result: bool = is_positive(
    10,
)

print(positive_result)


# =============================================================================
# 08. None Return Annotation
# =============================================================================


def display_message(
    message: str,
) -> None:
    """
    Display a message without returning a value.
    """
    print(message)


display_message(
    "Function annotation example",
)


# =============================================================================
# 09. List Annotation
# =============================================================================


def calculate_total(
    values: list[int],
) -> int:
    """
    Calculate the total of integer values.
    """
    total: int = sum(values)

    return total


numbers: list[int] = [
    10,
    20,
    30,
]

total_result: int = calculate_total(
    numbers,
)

print(total_result)


# =============================================================================
# 10. List of Strings
# =============================================================================


def join_words(
    words: list[str],
) -> str:
    """
    Join a list of strings.
    """
    result: str = " ".join(words)

    return result


words: list[str] = [
    "Python",
    "functions",
    "are",
    "useful",
]

joined_words: str = join_words(
    words,
)

print(joined_words)


# =============================================================================
# 11. Dictionary Annotation
# =============================================================================


def get_user_age(
    users: dict[str, int],
    username: str,
) -> int:
    """
    Return the age associated with a username.
    """
    return users[username]


user_ages: dict[str, int] = {
    "Alex": 25,
    "Sam": 30,
    "John": 28,
}

alex_age: int = get_user_age(
    user_ages,
    "Alex",
)

print(alex_age)


# =============================================================================
# 12. Dictionary With String Values
# =============================================================================


def get_configuration(
    configuration: dict[str, str],
    key: str,
) -> str:
    """
    Return a configuration value.
    """
    return configuration[key]


application_configuration: dict[str, str] = {
    "environment": "development",
    "region": "india",
}

environment: str = get_configuration(
    application_configuration,
    "environment",
)

print(environment)


# =============================================================================
# 13. Tuple Annotation
# =============================================================================


def get_coordinates() -> tuple[float, float]:
    """
    Return two-dimensional coordinates.
    """
    return (
        10.5,
        20.5,
    )


coordinates: tuple[float, float] = get_coordinates()

print(coordinates)


# =============================================================================
# 14. Tuple With Multiple Types
# =============================================================================


def get_user_record() -> tuple[str, int, bool]:
    """
    Return a user record.
    """
    return (
        "Alex",
        25,
        True,
    )


user_record: tuple[str, int, bool] = get_user_record()

print(user_record)


# =============================================================================
# 15. Set Annotation
# =============================================================================


def unique_numbers(
    values: set[int],
) -> set[int]:
    """
    Return a set containing unique integers.
    """
    return values


number_set: set[int] = {
    1,
    2,
    3,
}

unique_result: set[int] = unique_numbers(
    number_set,
)

print(unique_result)


# =============================================================================
# 16. Optional Values
# =============================================================================


def greet_optional(
    name: str | None,
) -> str:
    """
    Greet a user when a name is available.
    """
    if name is None:
        return "Hello, Guest!"

    return f"Hello, {name}!"


named_result: str = greet_optional(
    "Alex",
)

guest_result: str = greet_optional(
    None,
)

print(named_result)
print(guest_result)


# =============================================================================
# 17. Union Types
# =============================================================================


def format_identifier(
    identifier: int | str,
) -> str:
    """
    Convert an integer or string identifier to a string.
    """
    return str(identifier)


integer_identifier: str = format_identifier(
    100,
)

string_identifier: str = format_identifier(
    "USER-100",
)

print(integer_identifier)
print(string_identifier)


# =============================================================================
# 18. Union Return Type
# =============================================================================


def find_value(
    enabled: bool,
) -> int | None:
    """
    Return an integer when enabled, otherwise None.
    """
    if enabled:
        return 100

    return None


found_value: int | None = find_value(
    True,
)

missing_value: int | None = find_value(
    False,
)

print(found_value)
print(missing_value)


# =============================================================================
# 19. Type Alias
# =============================================================================


UserId = int


def get_user_id() -> UserId:
    """
    Return a user identifier.
    """
    return 1001


user_id: UserId = get_user_id()

print(user_id)


# =============================================================================
# 20. Type Alias For a Complex Type
# =============================================================================


UserRecord = dict[str, str]


def create_user_record(
    name: str,
    email: str,
) -> UserRecord:
    """
    Create a user record.
    """
    return {
        "name": name,
        "email": email,
    }


record: UserRecord = create_user_record(
    "Alex",
    "alex@example.com",
)

print(record)


# =============================================================================
# 21. Callable Annotation
# =============================================================================


from collections.abc import Callable


def apply_operation(
    operation: Callable[[int, int], int],
    first: int,
    second: int,
) -> int:
    """
    Apply a callable operation to two integers.
    """
    return operation(
        first,
        second,
    )


def multiply(
    first: int,
    second: int,
) -> int:
    """
    Multiply two integers.
    """
    return first * second


operation_result: int = apply_operation(
    multiply,
    5,
    4,
)

print(operation_result)


# =============================================================================
# 22. Callable With a Return Value
# =============================================================================


def execute_function(
    function: Callable[[], str],
) -> str:
    """
    Execute a function that takes no arguments.
    """
    return function()


def get_status() -> str:
    """
    Return an application status.
    """
    return "Running"


status: str = execute_function(
    get_status,
)

print(status)


# =============================================================================
# 23. Function Returning a Function
# =============================================================================


def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a function that multiplies by a fixed value.
    """

    def multiply_value(
        number: int,
    ) -> int:
        """
        Multiply a number by the captured multiplier.
        """
        return number * multiplier

    return multiply_value


double: Callable[[int], int] = create_multiplier(
    2,
)

double_result: int = double(
    10,
)

print(double_result)


# =============================================================================
# 24. Function Returning Another Function
# =============================================================================


def create_greeting_function(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a greeting function.
    """

    def create_message(
        name: str,
    ) -> str:
        """
        Create a greeting message.
        """
        return f"{prefix}, {name}!"

    return create_message


greet_with_hello: Callable[[str], str] = create_greeting_function(
    "Hello",
)

hello_message: str = greet_with_hello(
    "Alex",
)

print(hello_message)


# =============================================================================
# 25. *args Annotation
# =============================================================================


def calculate_sum(
    *numbers: int,
) -> int:
    """
    Calculate the sum of arbitrary integer arguments.
    """
    return sum(numbers)


sum_result: int = calculate_sum(
    10,
    20,
    30,
)

print(sum_result)


# =============================================================================
# 26. **kwargs Annotation
# =============================================================================


def display_configuration(
    **configuration: str,
) -> None:
    """
    Display string configuration values.
    """
    for key, value in configuration.items():
        print(
            f"{key}: {value}",
        )


display_configuration(
    environment="development",
    region="india",
)


# =============================================================================
# 27. *args and **kwargs Together
# =============================================================================


def describe_values(
    *values: int,
    **metadata: str,
) -> None:
    """
    Display positional values and string metadata.
    """
    print(values)
    print(metadata)


describe_values(
    10,
    20,
    30,
    source="database",
    environment="development",
)


# =============================================================================
# 28. Keyword-Only Parameter Annotations
# =============================================================================


def create_user(
    name: str,
    *,
    age: int,
    active: bool,
) -> str:
    """
    Create a user description.
    """
    return (
        f"name={name}, "
        f"age={age}, "
        f"active={active}"
    )


user_description: str = create_user(
    "Alex",
    age=25,
    active=True,
)

print(user_description)


# =============================================================================
# 29. Positional-Only Parameter Annotations
# =============================================================================


def calculate_discount(
    price: float,
    discount: float,
    /,
) -> float:
    """
    Calculate a discounted price.

    The parameters before / are positional-only.
    """
    discount_amount: float = price * discount

    return price - discount_amount


discounted_price: float = calculate_discount(
    1000.0,
    0.10,
)

print(discounted_price)


# =============================================================================
# 30. Positional-Only and Keyword-Only Parameters
# =============================================================================


def process_order(
    order_id: int,
    /,
    *,
    priority: bool,
) -> str:
    """
    Process an order using positional-only and keyword-only parameters.
    """
    return (
        f"order={order_id}, "
        f"priority={priority}"
    )


order_result: str = process_order(
    1001,
    priority=True,
)

print(order_result)


# =============================================================================
# 31. Default Values With Annotations
# =============================================================================


def greet_with_default(
    name: str = "Guest",
) -> str:
    """
    Return a greeting with a default name.
    """
    return f"Hello, {name}!"


default_greeting: str = greet_with_default()

custom_greeting: str = greet_with_default(
    "Alex",
)

print(default_greeting)
print(custom_greeting)


# =============================================================================
# 32. Boolean Default Value
# =============================================================================


def configure_application(
    debug: bool = False,
) -> str:
    """
    Return an application mode.
    """
    if debug:
        return "Debug mode"

    return "Production mode"


production_mode: str = configure_application()

debug_mode: str = configure_application(
    debug=True,
)

print(production_mode)
print(debug_mode)


# =============================================================================
# 33. Annotations Do Not Enforce Types
# =============================================================================


def add_values(
    first: int,
    second: int,
) -> int:
    """
    Add two values.

    The annotations describe the intended types.
    They do not perform runtime validation.
    """
    return first + second


valid_addition: int = add_values(
    10,
    20,
)

print(valid_addition)

# A static type checker can use the annotations to identify invalid calls.
#
# For example, the following call should be avoided:
#
# invalid_addition = add_values(
#     "10",
#     "20",
# )
#
# The annotation says that first and second should be int.
#
# Python itself does not automatically reject the call because annotations
# are not runtime type enforcement.


# =============================================================================
# 34. Annotation Inspection With __annotations__
# =============================================================================


def calculate_total_price(
    price: float,
    quantity: int,
) -> float:
    """
    Calculate a total price.
    """
    return price * quantity


function_annotations: dict[str, object] = (
    calculate_total_price.__annotations__
)

print(function_annotations)


# =============================================================================
# 35. Inspecting Parameter Annotations
# =============================================================================


def create_product(
    name: str,
    price: float,
) -> str:
    """
    Create a product description.
    """
    return f"{name}: {price}"


product_annotations: dict[str, object] = (
    create_product.__annotations__
)

print(product_annotations)


# =============================================================================
# 36. Return Annotation Inspection
# =============================================================================


def get_version() -> str:
    """
    Return an application version.
    """
    return "1.0.0"


version_annotations: dict[str, object] = (
    get_version.__annotations__
)

print(version_annotations)


# =============================================================================
# 37. inspect.signature
# =============================================================================


import inspect


def calculate_profit(
    revenue: float,
    cost: float,
) -> float:
    """
    Calculate profit.
    """
    return revenue - cost


signature: inspect.Signature = inspect.signature(
    calculate_profit,
)

print(signature)


# =============================================================================
# 38. Inspecting Individual Parameters
# =============================================================================


def calculate_tax(
    amount: float,
    rate: float,
) -> float:
    """
    Calculate tax.
    """
    return amount * rate


tax_signature: inspect.Signature = inspect.signature(
    calculate_tax,
)

for parameter in tax_signature.parameters.values():
    print(
        parameter.name,
        parameter.annotation,
    )


# =============================================================================
# 39. String Annotations
# =============================================================================


def get_description(
    value: "str",
) -> "str":
    """
    Demonstrate annotations written as strings.
    """
    return value


description: str = get_description(
    "Python",
)

print(description)


# =============================================================================
# 40. Future Annotations
# =============================================================================


"""
A modern Python file can use:

    from __future__ import annotations

to postpone evaluation of annotations.

That import must appear near the beginning of the file, before normal
module-level code.

Because this educational file already demonstrates ordinary annotations,
string annotations, and runtime inspection, the import is intentionally
not used globally here.

For a new project, using:

    from __future__ import annotations

can simplify forward references and reduce runtime evaluation of annotations.
"""


# =============================================================================
# 41. Forward Reference
# =============================================================================


class Employee:
    """
    Represent an employee.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name


def get_employee_name(
    employee: "Employee",
) -> str:
    """
    Return an employee name.
    """
    return employee.name


employee: Employee = Employee(
    "Alex",
)

employee_name: str = get_employee_name(
    employee,
)

print(employee_name)


# =============================================================================
# 42. Class Annotation In a Function
# =============================================================================


class Product:
    """
    Represent a product.
    """

    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        self.name: str = name
        self.price: float = price


def get_product_price(
    product: Product,
) -> float:
    """
    Return a product price.
    """
    return product.price


product: Product = Product(
    "Laptop",
    75000.0,
)

product_price: float = get_product_price(
    product,
)

print(product_price)


# =============================================================================
# 43. Iterable Annotation
# =============================================================================


from collections.abc import Iterable


def calculate_iterable_sum(
    values: Iterable[int],
) -> int:
    """
    Calculate the sum of an iterable of integers.
    """
    return sum(values)


iterable_sum: int = calculate_iterable_sum(
    [10, 20, 30],
)

print(iterable_sum)


# =============================================================================
# 44. Sequence Annotation
# =============================================================================


from collections.abc import Sequence


def first_item(
    values: Sequence[str],
) -> str:
    """
    Return the first item from a sequence.
    """
    return values[0]


first_value: str = first_item(
    [
        "Python",
        "SQL",
        "Go",
    ],
)

print(first_value)


# =============================================================================
# 45. Mapping Annotation
# =============================================================================


from collections.abc import Mapping


def get_mapping_value(
    values: Mapping[str, int],
    key: str,
) -> int:
    """
    Return a value from a mapping.
    """
    return values[key]


mapping_values: dict[str, int] = {
    "python": 10,
    "sql": 20,
}

mapping_result: int = get_mapping_value(
    mapping_values,
    "python",
)

print(mapping_result)


# =============================================================================
# 46. Callable With Named Parameters
# =============================================================================


def process_numbers(
    operation: Callable[[int, int], int],
) -> int:
    """
    Apply an operation to two numbers.
    """
    return operation(
        10,
        5,
    )


def subtract(
    first: int,
    second: int,
) -> int:
    """
    Subtract two integers.
    """
    return first - second


subtraction_result: int = process_numbers(
    subtract,
)

print(subtraction_result)


# =============================================================================
# 47. Callable Returning None
# =============================================================================


def run_callback(
    callback: Callable[[str], None],
    message: str,
) -> None:
    """
    Run a callback that returns None.
    """
    callback(message)


def print_message(
    message: str,
) -> None:
    """
    Print a message.
    """
    print(message)


run_callback(
    print_message,
    "Callback executed",
)


# =============================================================================
# 48. Any Annotation
# =============================================================================


from typing import Any


def display_any(
    value: Any,
) -> None:
    """
    Display a value of any type.
    """
    print(value)


display_any(
    "Python",
)

display_any(
    100,
)

display_any(
    [1, 2, 3],
)


# =============================================================================
# 49. Why Any Should Be Used Carefully
# =============================================================================


"""
Any disables many useful static type-checking guarantees.

For example:

    value: Any

tells a type checker that almost any operation may be allowed.

Prefer a specific annotation when the expected type is known.

Prefer:

    value: int

over:

    value: Any

when the function specifically requires an integer.
"""


# =============================================================================
# 50. TypeVar
# =============================================================================


from typing import TypeVar


T = TypeVar(
    "T",
)


def get_first(
    values: Sequence[T],
) -> T:
    """
    Return the first value while preserving its type.
    """
    return values[0]


first_integer: int = get_first(
    [10, 20, 30],
)

first_string: str = get_first(
    ["Python", "SQL", "Go"],
)

print(first_integer)
print(first_string)


# =============================================================================
# 51. Generic Function
# =============================================================================


TValue = TypeVar(
    "TValue",
)


def return_same_value(
    value: TValue,
) -> TValue:
    """
    Return the same value while preserving its type.
    """
    return value


integer_value: int = return_same_value(
    100,
)

string_value: str = return_same_value(
    "Python",
)

print(integer_value)
print(string_value)


# =============================================================================
# 52. TypeVar With a List
# =============================================================================


TItem = TypeVar(
    "TItem",
)


def first_list_item(
    values: list[TItem],
) -> TItem:
    """
    Return the first item from a list.
    """
    return values[0]


first_number: int = first_list_item(
    [1, 2, 3],
)

first_word: str = first_list_item(
    ["one", "two", "three"],
)

print(first_number)
print(first_word)


# =============================================================================
# 53. Generic Callable
# =============================================================================


TInput = TypeVar(
    "TInput",
)

TOutput = TypeVar(
    "TOutput",
)


def transform(
    value: TInput,
    function: Callable[[TInput], TOutput],
) -> TOutput:
    """
    Transform a value using a callable.
    """
    return function(value)


def number_to_string(
    number: int,
) -> str:
    """
    Convert an integer to a string.
    """
    return str(number)


transformed_value: str = transform(
    100,
    number_to_string,
)

print(transformed_value)


# =============================================================================
# 54. Function Annotation With a Tuple Return
# =============================================================================


def divide_numbers(
    dividend: float,
    divisor: float,
) -> tuple[float, float]:
    """
    Return quotient and remainder-like information.
    """
    quotient: float = dividend / divisor
    remainder: float = dividend % divisor

    return (
        quotient,
        remainder,
    )


division_result: tuple[float, float] = divide_numbers(
    10.0,
    3.0,
)

print(division_result)


# =============================================================================
# 55. Function Annotation With a Dictionary Return
# =============================================================================


def create_configuration() -> dict[str, str]:
    """
    Create an application configuration.
    """
    return {
        "environment": "development",
        "region": "india",
    }


configuration: dict[str, str] = create_configuration()

print(configuration)


# =============================================================================
# 56. Function Annotation With a List Return
# =============================================================================


def create_numbers() -> list[int]:
    """
    Return a list of integers.
    """
    return [
        1,
        2,
        3,
    ]


created_numbers: list[int] = create_numbers()

print(created_numbers)


# =============================================================================
# 57. Function Annotation With a Set Return
# =============================================================================


def create_unique_values() -> set[str]:
    """
    Return a set of unique strings.
    """
    return {
        "Python",
        "SQL",
        "Python",
    }


unique_values: set[str] = create_unique_values()

print(unique_values)


# =============================================================================
# 58. Function Annotation With None
# =============================================================================


def clear_values(
    values: list[int],
) -> None:
    """
    Remove all values from a list.
    """
    values.clear()


values_to_clear: list[int] = [
    1,
    2,
    3,
]

clear_values(
    values_to_clear,
)

print(values_to_clear)


# =============================================================================
# 59. Optional Parameter With Default None
# =============================================================================


def find_username(
    user_id: int,
    username: str | None = None,
) -> str:
    """
    Return a username or a generated fallback.
    """
    if username is not None:
        return username

    return f"user-{user_id}"


known_username: str = find_username(
    100,
    "Alex",
)

generated_username: str = find_username(
    200,
)

print(known_username)
print(generated_username)


# =============================================================================
# 60. Annotation Does Not Change Runtime Behaviour
# =============================================================================


def multiply_values(
    first: int,
    second: int,
) -> int:
    """
    Multiply two values.
    """
    return first * second


result: int = multiply_values(
    5,
    4,
)

print(result)

"""
The annotations:

    first: int
    second: int
    -> int

describe the intended interface.

They do not transform values.

For example, an annotation does not automatically convert:

    "5"

into:

    5

If runtime validation or conversion is required, it must be implemented
explicitly.
"""


# =============================================================================
# 61. Runtime Validation Is Separate From Annotation
# =============================================================================


def parse_integer(
    value: str,
) -> int:
    """
    Convert a string into an integer.
    """
    return int(value)


parsed_value: int = parse_integer(
    "100",
)

print(parsed_value)

"""
The annotation:

    value: str

documents the expected input.

The implementation:

    int(value)

performs the actual runtime conversion.

Annotations and runtime validation are separate concerns.
"""


# =============================================================================
# 62. Annotation and Static Type Checking
# =============================================================================


def calculate_average(
    total: float,
    count: int,
) -> float:
    """
    Calculate an average.
    """
    return total / count


average: float = calculate_average(
    100.0,
    4,
)

print(average)

"""
A static type checker can inspect the annotations and detect calls that
appear inconsistent with the declared interface.

For example, a type checker can report a problem with:

    calculate_average(
        "100",
        "4",
    )

because the function declares:

    total: float
    count: int

Static checking happens before runtime and does not itself execute the
function.
"""


# =============================================================================
# 63. Annotation and IDE Support
# =============================================================================


def calculate_percentage(
    value: float,
    total: float,
) -> float:
    """
    Calculate a percentage.
    """
    return (
        value
        / total
        * 100.0
    )


percentage: float = calculate_percentage(
    25.0,
    100.0,
)

print(percentage)

"""
Editors such as Pylance can use annotations to provide:

- autocomplete
- parameter information
- type warnings
- navigation
- documentation hints
- refactoring assistance

Annotations therefore improve development tooling even though Python does
not automatically enforce them.
"""


# =============================================================================
# 64. Annotations Improve Documentation
# =============================================================================


def calculate_invoice_total(
    price: float,
    quantity: int,
    tax_rate: float,
) -> float:
    """
    Calculate an invoice total.

    Parameters:
        price: Unit price.
        quantity: Number of units.
        tax_rate: Tax rate as a decimal.

    Returns:
        The final invoice total.
    """
    subtotal: float = price * quantity
    tax: float = subtotal * tax_rate

    return subtotal + tax


invoice_total: float = calculate_invoice_total(
    100.0,
    5,
    0.18,
)

print(invoice_total)


# =============================================================================
# 65. Annotation of a Class Parameter
# =============================================================================


class Customer:
    """
    Represent a customer.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name: str = name


def get_customer_name(
    customer: Customer,
) -> str:
    """
    Return the customer's name.
    """
    return customer.name


customer: Customer = Customer(
    "Alex",
)

customer_name: str = get_customer_name(
    customer,
)

print(customer_name)


# =============================================================================
# 66. Annotation of an Iterable
# =============================================================================


def count_items(
    values: Iterable[str],
) -> int:
    """
    Count values from an iterable.
    """
    return sum(
        1
        for _ in values
    )


item_count: int = count_items(
    [
        "Python",
        "SQL",
        "Go",
    ],
)

print(item_count)


# =============================================================================
# 67. Annotation of a Sequence
# =============================================================================


def last_value(
    values: Sequence[int],
) -> int:
    """
    Return the last item in a sequence.
    """
    return values[-1]


last_number: int = last_value(
    [
        10,
        20,
        30,
    ],
)

print(last_number)


# =============================================================================
# 68. Annotation of a Mapping
# =============================================================================


def total_mapping_values(
    values: Mapping[str, int],
) -> int:
    """
    Sum integer values from a mapping.
    """
    return sum(values.values())


mapping_total: int = total_mapping_values(
    {
        "first": 10,
        "second": 20,
        "third": 30,
    },
)

print(mapping_total)


# =============================================================================
# 69. Annotation With Nested Collections
# =============================================================================


def flatten_numbers(
    values: list[list[int]],
) -> list[int]:
    """
    Flatten a two-dimensional list of integers.
    """
    flattened: list[int] = []

    for group in values:
        flattened.extend(group)

    return flattened


nested_numbers: list[list[int]] = [
    [1, 2],
    [3, 4],
    [5, 6],
]

flattened_numbers: list[int] = flatten_numbers(
    nested_numbers,
)

print(flattened_numbers)


# =============================================================================
# 70. Nested Dictionary Annotation
# =============================================================================


def get_settings() -> dict[str, dict[str, str]]:
    """
    Return nested application settings.
    """
    return {
        "database": {
            "host": "localhost",
            "engine": "postgresql",
        },
        "application": {
            "environment": "development",
            "region": "india",
        },
    }


settings: dict[str, dict[str, str]] = get_settings()

print(settings)


# =============================================================================
# 71. Callable Annotation With Multiple Arguments
# =============================================================================


def run_binary_operation(
    operation: Callable[[float, float], float],
    first: float,
    second: float,
) -> float:
    """
    Run a binary floating-point operation.
    """
    return operation(
        first,
        second,
    )


def divide(
    first: float,
    second: float,
) -> float:
    """
    Divide two floating-point values.
    """
    return first / second


division_result: float = run_binary_operation(
    divide,
    20.0,
    4.0,
)

print(division_result)


# =============================================================================
# 72. Callable Annotation With No Parameters
# =============================================================================


def execute(
    operation: Callable[[], int],
) -> int:
    """
    Execute a function that returns an integer.
    """
    return operation()


def get_answer() -> int:
    """
    Return a fixed integer.
    """
    return 42


answer: int = execute(
    get_answer,
)

print(answer)


# =============================================================================
# 73. Function Annotation With a Generator
# =============================================================================


from collections.abc import Iterator


def generate_numbers(
    limit: int,
) -> Iterator[int]:
    """
    Generate integers from zero through limit - 1.
    """
    for number in range(limit):
        yield number


generated_numbers: Iterator[int] = generate_numbers(
    3,
)

for number in generated_numbers:
    print(number)


# =============================================================================
# 74. Generator Return Annotation
# =============================================================================


def generate_names() -> Iterator[str]:
    """
    Generate several names.
    """
    yield "Alex"
    yield "Sam"
    yield "Jordan"


names: Iterator[str] = generate_names()

for name in names:
    print(name)


# =============================================================================
# 75. Annotation of a Coroutine
# =============================================================================


"""
For asynchronous functions, the return annotation describes the value
produced when the coroutine is awaited.

For example:

    async def fetch_name() -> str:
        return "Alex"

The annotation is:

    -> str

not:

    -> Coroutine[Any, Any, str]

In normal application code, annotating the async function with the type
of the awaited result is usually the clearest approach.
"""


# =============================================================================
# 76. Async Function Example
# =============================================================================


import asyncio


async def get_async_message() -> str:
    """
    Return an asynchronous message.
    """
    await asyncio.sleep(0)

    return "Async function completed"


async def run_async_example() -> None:
    """
    Run the asynchronous example.
    """
    message: str = await get_async_message()

    print(message)


asyncio.run(
    run_async_example(),
)


# =============================================================================
# 77. Annotation of a Decorator
# =============================================================================


from functools import wraps
from typing import ParamSpec


P = ParamSpec(
    "P",
)


def log_call(
    function: Callable[P, TOutput],
) -> Callable[P, TOutput]:
    """
    Return a decorator that logs a function call.
    """

    @wraps(function)
    def wrapper(
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> TOutput:
        print(
            f"Calling {function.__name__}",
        )

        return function(
            *args,
            **kwargs,
        )

    return wrapper


@log_call
def add_with_logging(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


logged_result: int = add_with_logging(
    10,
    20,
)

print(logged_result)


# =============================================================================
# 78. ParamSpec
# =============================================================================


"""
ParamSpec is useful when a decorator needs to preserve the parameter types
of the function it wraps.

In the decorator above:

    P = ParamSpec("P")

represents the parameter specification of the original function.

The wrapper uses:

    *args: P.args
    **kwargs: P.kwargs

This allows a type checker to preserve the original callable signature
through the decorator.
"""


# =============================================================================
# 79. Type Alias For Callable
# =============================================================================


Operation = Callable[[int, int], int]


def execute_operation(
    operation: Operation,
    first: int,
    second: int,
) -> int:
    """
    Execute an integer operation.
    """
    return operation(
        first,
        second,
    )


def add_operation(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


operation_output: int = execute_operation(
    add_operation,
    10,
    20,
)

print(operation_output)


# =============================================================================
# 80. Annotation With Literal
# =============================================================================


from typing import Literal


def set_environment(
    environment: Literal["development", "production"],
) -> str:
    """
    Set an environment from a restricted set of string values.
    """
    return environment


development_environment: str = set_environment(
    "development",
)

production_environment: str = set_environment(
    "production",
)

print(development_environment)
print(production_environment)


# =============================================================================
# 81. Annotation With Final
# =============================================================================


from typing import Final


DEFAULT_PORT: Final[int] = 8000


def get_default_port() -> int:
    """
    Return the configured default port.
    """
    return DEFAULT_PORT


port: int = get_default_port()

print(port)


# =============================================================================
# 82. Annotation With Type
# =============================================================================


def create_instance(
    class_type: type[Customer],
    name: str,
) -> Customer:
    """
    Create a Customer instance from a class type.
    """
    return class_type(name)


new_customer: Customer = create_instance(
    Customer,
    "Sam",
)

print(new_customer.name)


# =============================================================================
# 83. Function Annotation Best Practice
# =============================================================================


def calculate_net_price(
    gross_price: float,
    tax_rate: float,
) -> float:
    """
    Calculate net price from gross price and tax rate.
    """
    tax_amount: float = gross_price * tax_rate
    net_price: float = gross_price - tax_amount

    return net_price


net_price: float = calculate_net_price(
    1000.0,
    0.18,
)

print(net_price)


# =============================================================================
# 84. Avoid Overly Broad Annotations
# =============================================================================


def format_value(
    value: str | int | float,
) -> str:
    """
    Format common scalar values as strings.
    """
    return str(value)


formatted_integer: str = format_value(
    100,
)

formatted_float: str = format_value(
    10.5,
)

formatted_string: str = format_value(
    "Python",
)

print(formatted_integer)
print(formatted_float)
print(formatted_string)


# =============================================================================
# 85. Annotation Should Match the Function Contract
# =============================================================================


def get_positive_number(
    number: int,
) -> int:
    """
    Return the supplied integer when it is positive.

    Raise ValueError otherwise.
    """
    if number <= 0:
        raise ValueError(
            "number must be positive",
        )

    return number


positive_number: int = get_positive_number(
    10,
)

print(positive_number)


# =============================================================================
# 86. Annotation Does Not Describe Exceptions
# =============================================================================


def parse_positive_number(
    value: str,
) -> int:
    """
    Parse a positive integer.

    Raises:
        ValueError: If the value is not a positive integer.
    """
    number: int = int(value)

    if number <= 0:
        raise ValueError(
            "value must be positive",
        )

    return number


parsed_positive: int = parse_positive_number(
    "25",
)

print(parsed_positive)


# =============================================================================
# 87. Annotation and Documentation Work Together
# =============================================================================


def calculate_compound_interest(
    principal: float,
    rate: float,
    years: int,
) -> float:
    """
    Calculate compound interest.

    Parameters:
        principal: Initial amount.
        rate: Annual rate as a decimal.
        years: Number of years.

    Returns:
        Final amount after compound growth.
    """
    return principal * (
        1.0 + rate
    ) ** years


compound_result: float = calculate_compound_interest(
    1000.0,
    0.05,
    3,
)

print(compound_result)


# =============================================================================
# 88. Common Mistake: Wrong Return Annotation
# =============================================================================


def correct_total(
    first: int,
    second: int,
) -> int:
    """
    Return an integer total.
    """
    return first + second


correct_result: int = correct_total(
    10,
    20,
)

print(correct_result)

"""
The return annotation should describe the value actually returned.

Avoid declaring:

    -> str

when the function actually returns an int.

Accurate annotations are important because static type checkers and IDEs
rely on them.
"""


# =============================================================================
# 89. Common Mistake: Missing Parameter Annotation
# =============================================================================


def partially_annotated(
    value: int,
):
    """
    This function intentionally demonstrates a missing return annotation.
    """
    return value * 2


"""
For production code, prefer:

    def fully_annotated(
        value: int,
    ) -> int:
        return value * 2

A complete annotation makes the function contract clearer.
"""


# =============================================================================
# 90. Fully Annotated Function
# =============================================================================


def fully_annotated(
    value: int,
) -> int:
    """
    Return twice the supplied integer.
    """
    result: int = value * 2

    return result


fully_annotated_result: int = fully_annotated(
    25,
)

print(fully_annotated_result)


# =============================================================================
# 91. Function Annotation Checklist
# =============================================================================


"""
When writing a function, consider annotating:

1. Every parameter.

2. The return value.

3. Callback parameters using Callable.

4. Collections using list, dict, set, tuple, or collections.abc types.

5. Optional values using | None.

6. Multiple allowed types using |.

7. Reusable complex types using type aliases.

8. Generic functions using TypeVar when appropriate.

9. Decorators using ParamSpec when preserving signatures.

10. Constants using Final when appropriate.

Good:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        return price * quantity

Less informative:

    def calculate_total(price, quantity):
        return price * quantity
"""


# =============================================================================
# 92. Practical Annotation Example
# =============================================================================


def process_invoice(
    customer_name: str,
    items: list[float],
    tax_rate: float,
) -> float:
    """
    Calculate the total invoice amount.
    """
    subtotal: float = sum(items)
    tax: float = subtotal * tax_rate
    total: float = subtotal + tax

    print(
        f"Customer: {customer_name}",
    )

    return total


invoice_result: float = process_invoice(
    "Alex",
    [
        100.0,
        250.0,
        50.0,
    ],
    0.18,
)

print(invoice_result)


# =============================================================================
# 93. Practical Callable Example
# =============================================================================


def process_numbers_with_operation(
    values: Sequence[int],
    operation: Callable[[int], int],
) -> list[int]:
    """
    Apply an operation to every integer.
    """
    results: list[int] = []

    for value in values:
        results.append(
            operation(value),
        )

    return results


def square_number(
    number: int,
) -> int:
    """
    Return the square of a number.
    """
    return number ** 2


processed_numbers: list[int] = process_numbers_with_operation(
    [
        1,
        2,
        3,
        4,
    ],
    square_number,
)

print(processed_numbers)


# =============================================================================
# 94. Practical Generic Example
# =============================================================================


TValue = TypeVar(
    "TValue",
)


def get_last_item(
    values: Sequence[TValue],
) -> TValue:
    """
    Return the last item while preserving its type.
    """
    return values[-1]


last_integer: int = get_last_item(
    [
        10,
        20,
        30,
    ],
)

last_string: str = get_last_item(
    [
        "Python",
        "SQL",
        "Go",
    ],
)

print(last_integer)
print(last_string)


# =============================================================================
# 95. Practical Decorator Annotation Example
# =============================================================================


PDecorator = ParamSpec(
    "PDecorator",
)

TReturn = TypeVar(
    "TReturn",
)


def announce(
    function: Callable[PDecorator, TReturn],
) -> Callable[PDecorator, TReturn]:
    """
    Decorate a function while preserving its parameter and return types.
    """

    @wraps(function)
    def wrapper(
        *args: PDecorator.args,
        **kwargs: PDecorator.kwargs,
    ) -> TReturn:
        print(
            f"Running {function.__name__}",
        )

        return function(
            *args,
            **kwargs,
        )

    return wrapper


@announce
def calculate_sum_annotated(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


annotated_sum: int = calculate_sum_annotated(
    5,
    10,
)

print(annotated_sum)


# =============================================================================
# 96. Scope and Function Annotations
# =============================================================================


def annotated_function(
    value: int,
) -> int:
    """
    Demonstrate that annotations belong to the function definition.
    """
    result: int = value * 2

    return result


annotation_scope_result: int = annotated_function(
    10,
)

print(annotation_scope_result)

"""
The parameter annotation:

    value: int

belongs to the function's parameter definition.

The return annotation:

    -> int

belongs to the function's return contract.

The local variable annotation:

    result: int

belongs to the function's local variable.

Annotations do not change the normal scope rules of Python.
"""


# =============================================================================
# 97. Function Annotation Summary
# =============================================================================


"""
Function annotation syntax:

    def function(
        parameter: Type,
    ) -> ReturnType:
        ...

Examples:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

    def greet(
        name: str,
    ) -> str:
        return f"Hello, {name}!"

    def display(
        message: str,
    ) -> None:
        print(message)

    def get_values() -> list[int]:
        return [1, 2, 3]

    def find_user(
        user_id: int,
    ) -> User | None:
        ...

Annotations are useful for:

- readability
- documentation
- IDE support
- static type checking
- refactoring
- maintainability
- API design
- understanding function contracts
"""


# =============================================================================
# 98. Key Rules
# =============================================================================


"""
Important rules:

1. Parameter annotations use:

       parameter: Type

2. Return annotations use:

       -> ReturnType

3. A function returning nothing should normally use:

       -> None

4. Collection annotations can use modern built-in generic syntax:

       list[int]
       dict[str, int]
       set[str]
       tuple[int, str]

5. Optional values can use:

       str | None

6. Multiple accepted types can use:

       int | str

7. Functions can be annotated with Callable.

8. Generic functions can use TypeVar.

9. Decorators can use ParamSpec to preserve callable signatures.

10. Annotations do not automatically enforce runtime types.

11. Static type checkers can use annotations to detect potential problems.

12. IDEs can use annotations for autocomplete and diagnostics.

13. Annotations can be inspected using:

       function.__annotations__

14. Function signatures can be inspected using:

       inspect.signature(function)

15. String annotations can be used for forward references.

16. from __future__ import annotations can postpone annotation evaluation.

17. Accurate annotations should match the actual function contract.

18. Annotations do not change Python's normal scope rules.
"""


# =============================================================================
# 99. Final Example
# =============================================================================


User = dict[str, str]


def create_user(
    name: str,
    email: str,
    active: bool = True,
) -> User:
    """
    Create a user record.

    Parameters:
        name: User's display name.
        email: User's email address.
        active: Whether the user is active.

    Returns:
        A dictionary containing user information.
    """
    return {
        "name": name,
        "email": email,
        "active": str(active),
    }


created_user: User = create_user(
    "Alex",
    "alex@example.com",
)

print(created_user)


# =============================================================================
# Key Takeaways
# =============================================================================


"""
✓ Function annotations describe parameters and return values.

✓ Parameter annotations use:

    parameter: Type

✓ Return annotations use:

    -> ReturnType

✓ Functions can annotate every parameter.

✓ Functions can annotate their return value.

✓ Variables can also have annotations.

✓ list[int] describes a list containing integers.

✓ dict[str, int] describes a dictionary with string keys and integer values.

✓ tuple[str, int] describes a tuple containing a string and an integer.

✓ set[str] describes a set containing strings.

✓ str | None describes either a string or None.

✓ int | str describes either an integer or a string.

✓ Callable describes functions and other callable objects.

✓ TypeVar allows generic functions to preserve relationships between types.

✓ ParamSpec helps decorators preserve callable parameter information.

✓ Any allows arbitrary values but should be used carefully.

✓ Literal can restrict a parameter to specific literal values.

✓ Final can document values intended not to be reassigned.

✓ Annotations do not automatically enforce types at runtime.

✓ Static type checkers such as mypy can analyze annotations.

✓ IDE tools such as Pylance can use annotations for diagnostics and
  autocomplete.

✓ Annotations can be inspected through __annotations__.

✓ inspect.signature() can inspect a function's signature.

✓ Forward references can use string annotations.

✓ from __future__ import annotations can postpone annotation evaluation.

✓ Accurate annotations make function contracts easier to understand.

✓ Good annotations improve readability, tooling, documentation, and
  maintainability.

Core syntax:

    def function(
        parameter: Type,
    ) -> ReturnType:
        return value

Core examples:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

    def greet(
        name: str,
    ) -> str:
        return f"Hello, {name}!"

    def get_values() -> list[int]:
        return [1, 2, 3]

    def find_user(
        user_id: int,
    ) -> User | None:
        ...

The most important idea:

    annotations
        ↓
    describe the function contract
        ↓
    improve readability and tooling
        ↓
    do not automatically enforce runtime types
"""


# =============================================================================
# End of 14_function_annotation.py
# =============================================================================