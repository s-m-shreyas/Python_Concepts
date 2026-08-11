# =============================================================================
# 15. Docstrings
# =============================================================================
"""
Python Functions

File:
15_docstrings.py

Topic:
Docstrings

Overview:

A docstring is a string literal used to document a Python module, function,
class, or method.

Docstrings explain what code does and provide information to developers,
IDEs, documentation generators, and tools such as help().

A docstring is normally written immediately after:

    - a module definition
    - a function definition
    - a class definition
    - a method definition

The most common form uses triple-quoted strings:

    '''
    Documentation goes here.
    '''

or:

    \"\"\"
    Documentation goes here.
    \"\"\"

Topics covered:

    - What is a docstring?
    - Module docstrings
    - Function docstrings
    - Class docstrings
    - Method docstrings
    - Docstrings versus comments
    - Accessing __doc__
    - Using help()
    - One-line docstrings
    - Multi-line docstrings
    - PEP 257 style
    - Describing function behavior
    - Documenting parameters
    - Documenting return values
    - Documenting exceptions
    - Documenting side effects
    - Documenting mutable arguments
    - Documenting optional parameters
    - Documenting keyword-only parameters
    - Documenting callable functions
    - Docstrings with type annotations
    - Google-style docstrings
    - NumPy-style docstrings
    - Sphinx-style docstrings
    - Good docstring practices
    - Common docstring mistakes
    - Practical docstring patterns
"""

# =============================================================================
# 01. What Is a Docstring?
# =============================================================================
"""
A docstring is a string literal that documents a Python object.

For example:

    def greet() -> str:
        \"\"\"
        Return a greeting.
        \"\"\"
        return "Hello"

The string immediately after the function definition becomes the
function's docstring.

Python stores the docstring in:

    function_name.__doc__

Docstrings are useful because they can be inspected at runtime and can also
be displayed by development tools and documentation systems.
"""

# =============================================================================
# 02. Basic Function Docstring
# =============================================================================


def greet_user() -> str:
    """Return a simple greeting."""
    return "Hello, user!"


greeting: str = greet_user()

print(greeting)


# =============================================================================
# 03. Accessing a Function's Docstring
# =============================================================================


def add_numbers(
    first: int,
    second: int,
) -> int:
    """Return the sum of two integers."""
    return first + second


print(add_numbers.__doc__)


# =============================================================================
# 04. __doc__ Attribute
# =============================================================================
"""
Python automatically provides a __doc__ attribute for objects that have
docstrings.

Example:

    def greet() -> str:
        \"\"\"Return a greeting.\"\"\"
        return "Hello"

The following expression:

    greet.__doc__

returns:

    "Return a greeting."

If an object has no docstring, its __doc__ attribute is normally None.
"""

# =============================================================================
# 05. Function Without a Docstring
# =============================================================================


def function_without_docstring() -> str:
    return "No explicit docstring."


missing_docstring: str | None = function_without_docstring.__doc__

print(missing_docstring)


# =============================================================================
# 06. Function With a Docstring
# =============================================================================


def function_with_docstring() -> str:
    """Return a message demonstrating a docstring."""
    return "Documented function."


existing_docstring: str | None = function_with_docstring.__doc__

print(existing_docstring)


# =============================================================================
# 07. One-Line Docstrings
# =============================================================================
"""
A one-line docstring is appropriate for a simple function whose behavior
can be described briefly.

Example:

    def square(number: int) -> int:
        \"\"\"Return the square of number.\"\"\"
        return number ** 2

The opening and closing quotes remain on the same line.
"""

# =============================================================================
# 08. One-Line Docstring Example
# =============================================================================


def square(number: int) -> int:
    """Return the square of a number."""
    return number**2


square_result: int = square(5)

print(square_result)


# =============================================================================
# 09. Multi-Line Docstrings
# =============================================================================
"""
Use a multi-line docstring when a function needs more detailed
documentation.

Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"
        Calculate the total price.

        The function multiplies the price by the quantity.
        \"\"\"
        return price * quantity

The first line should provide a concise summary.

Additional lines can provide more details.
"""

# =============================================================================
# 10. Multi-Line Function Docstring
# =============================================================================


def calculate_total(
    price: float,
    quantity: int,
) -> float:
    """
    Calculate the total price.

    The total is calculated by multiplying the price by the quantity.
    """
    return price * quantity


total: float = calculate_total(
    100.0,
    3,
)

print(total)


# =============================================================================
# 11. Docstrings Should Describe Behavior
# =============================================================================


def calculate_discount(
    price: float,
    percentage: float,
) -> float:
    """
    Calculate the discount amount.

    The percentage should be provided as a value between 0 and 100.
    """
    return price * percentage / 100.0


discount: float = calculate_discount(
    1000.0,
    10.0,
)

print(discount)


# =============================================================================
# 12. Docstrings Versus Comments
# =============================================================================
"""
Docstrings and comments have different purposes.

A comment explains implementation details to developers reading the source.

Example:

    # Multiply the price by the quantity.
    total = price * quantity

A docstring documents the purpose and behavior of a function.

Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"Return the total price for the requested quantity.\"\"\"
        return price * quantity

Comments:

    - explain implementation details
    - are ignored as documentation metadata
    - begin with #

Docstrings:

    - document Python objects
    - are stored in __doc__
    - can be displayed by help()
    - can be processed by documentation tools
"""

# =============================================================================
# 13. Comment Example
# =============================================================================


def calculate_area(
    width: float,
    height: float,
) -> float:
    """Return the area of a rectangle."""
    # Multiply width by height to calculate the area.
    return width * height


area: float = calculate_area(
    10.0,
    5.0,
)

print(area)


# =============================================================================
# 14. Documenting Parameters
# =============================================================================
"""
When a function has several parameters, the docstring can explain what
each parameter represents.

Example:

    def create_user(
        name: str,
        age: int,
    ) -> str:
        \"\"\"
        Create a user description.

        Args:
            name: The user's name.
            age: The user's age.
        \"\"\"
        return f"{name} is {age} years old."

This style is commonly called Google-style documentation.
"""

# =============================================================================
# 15. Parameter Documentation
# =============================================================================


def create_user_description(
    name: str,
    age: int,
) -> str:
    """
    Create a description for a user.

    Args:
        name: The user's name.
        age: The user's age.

    Returns:
        A formatted description containing the user's name and age.
    """
    return f"{name} is {age} years old."


user_description: str = create_user_description(
    "Alex",
    30,
)

print(user_description)


# =============================================================================
# 16. Documenting Return Values
# =============================================================================


def calculate_square(
    number: float,
) -> float:
    """
    Calculate the square of a number.

    Args:
        number: The number to square.

    Returns:
        The square of the supplied number.
    """
    return number**2


square_value: float = calculate_square(
    8.0,
)

print(square_value)


# =============================================================================
# 17. Documenting Exceptions
# =============================================================================
"""
A docstring can document exceptions that callers should know about.

Example:

    def divide(
        numerator: float,
        denominator: float,
    ) -> float:
        \"\"\"
        Divide two numbers.

        Raises:
            ValueError: If denominator is zero.
        \"\"\"
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        return numerator / denominator

Documenting expected exceptions helps callers understand how a function
can fail.
"""

# =============================================================================
# 18. Exception Documentation
# =============================================================================


def divide_numbers(
    numerator: float,
    denominator: float,
) -> float:
    """
    Divide one number by another.

    Args:
        numerator: The number being divided.
        denominator: The number used as the divisor.

    Returns:
        The division result.

    Raises:
        ValueError: If denominator is zero.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    return numerator / denominator


division_result: float = divide_numbers(
    10.0,
    2.0,
)

print(division_result)


# =============================================================================
# 19. Documenting Side Effects
# =============================================================================
"""
A side effect occurs when a function changes something outside its direct
return value.

Examples include:

    - modifying a list
    - changing an object
    - writing a file
    - updating application state
    - modifying a database
    - logging information

A docstring should mention important side effects when callers need to
know about them.
"""

# =============================================================================
# 20. Mutable Argument Side Effect
# =============================================================================


def append_item(
    items: list[str],
    item: str,
) -> None:
    """
    Append an item to the supplied list.

    Args:
        items: The list that will be modified.
        item: The item to append.

    Side Effects:
        Modifies the supplied list in place.
    """
    items.append(item)


languages: list[str] = [
    "Python",
]

append_item(
    languages,
    "SQL",
)

print(languages)


# =============================================================================
# 21. Documenting Mutable Arguments
# =============================================================================
"""
Mutable arguments deserve special attention.

Consider:

    def add_item(
        values: list[int],
    ) -> None:
        \"\"\"Append an item to values.\"\"\"
        values.append(10)

The caller's list is modified.

The docstring should make this behavior clear when it is important.

This prevents callers from assuming that the function creates a new list
without modifying the original.
"""

# =============================================================================
# 22. Documenting Optional Parameters
# =============================================================================


def greet_with_name(
    name: str | None = None,
) -> str:
    """
    Return a greeting.

    Args:
        name: Optional name to include in the greeting.

    Returns:
        A personalized greeting when name is supplied, otherwise a
        generic greeting.
    """
    if name is None:
        return "Hello!"

    return f"Hello, {name}!"


generic_greeting: str = greet_with_name()

personalized_greeting: str = greet_with_name(
    "Alex",
)

print(generic_greeting)
print(personalized_greeting)


# =============================================================================
# 23. Documenting Keyword-Only Parameters
# =============================================================================


def create_account(
    username: str,
    *,
    active: bool = True,
) -> str:
    """
    Create a simple account description.

    Args:
        username: The account username.
        active: Whether the account should be marked as active.

    Returns:
        A formatted account description.
    """
    status: str = "active" if active else "inactive"

    return f"{username}: {status}"


account_description: str = create_account(
    "alex",
    active=True,
)

print(account_description)


# =============================================================================
# 24. Docstrings and Type Annotations
# =============================================================================
"""
Type annotations and docstrings complement each other.

Type annotations describe expected types.

Docstrings explain meaning and behavior.

Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"
        Calculate the total price.

        Args:
            price: Price of one item.
            quantity: Number of items.

        Returns:
            Total price before tax.
        \"\"\"
        return price * quantity

The annotation tells us:

    price -> float
    quantity -> int
    return -> float

The docstring tells us what those values mean.
"""

# =============================================================================
# 25. Type Annotations Do Not Replace Docstrings
# =============================================================================


def calculate_tax(
    amount: float,
    rate: float,
) -> float:
    """
    Calculate tax for an amount.

    Args:
        amount: The monetary amount before tax.
        rate: Tax rate expressed as a percentage.

    Returns:
        The calculated tax amount.
    """
    return amount * rate / 100.0


tax: float = calculate_tax(
    1000.0,
    18.0,
)

print(tax)


# =============================================================================
# 26. Module Docstrings
# =============================================================================
"""
The string at the beginning of a Python file can act as the module
docstring.

The module docstring should appear before imports and other executable
statements.

Example:

    \"\"\"
    Utilities for working with invoices.
    \"\"\"

    from decimal import Decimal

The module docstring describes the purpose of the entire module.
"""

# =============================================================================
# 27. Class Docstrings
# =============================================================================


class User:
    """
    Represent a simple user.

    Attributes:
        name: The user's name.
        age: The user's age.
    """

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        """
        Initialize a user.

        Args:
            name: The user's name.
            age: The user's age.
        """
        self.name: str = name
        self.age: int = age

    def description(self) -> str:
        """Return a description of the user."""
        return f"{self.name} is {self.age} years old."


user: User = User(
    "Alex",
    30,
)

print(user.description())


# =============================================================================
# 28. Method Docstrings
# =============================================================================
"""
Methods are functions defined inside classes.

Methods can have their own docstrings.

Example:

    class Calculator:
        \"\"\"Perform basic calculations.\"\"\"

        def add(
            self,
            first: int,
            second: int,
        ) -> int:
            \"\"\"Return the sum of two integers.\"\"\"
            return first + second

The class and each method can have separate documentation.
"""

# =============================================================================
# 29. Class and Method Documentation
# =============================================================================


class Calculator:
    """Provide basic arithmetic operations."""

    def add(
        self,
        first: int,
        second: int,
    ) -> int:
        """Return the sum of two integers."""
        return first + second

    def multiply(
        self,
        first: int,
        second: int,
    ) -> int:
        """Return the product of two integers."""
        return first * second


calculator: Calculator = Calculator()

addition: int = calculator.add(
    10,
    20,
)

multiplication: int = calculator.multiply(
    10,
    20,
)

print(addition)
print(multiplication)


# =============================================================================
# 30. Accessing Class Docstrings
# =============================================================================


class Product:
    """Represent a product."""

    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        """Initialize a product."""
        self.name: str = name
        self.price: float = price


product_docstring: str | None = Product.__doc__

print(product_docstring)


# =============================================================================
# 31. Accessing Method Docstrings
# =============================================================================


class Printer:
    """Provide simple printing operations."""

    def print_message(
        self,
        message: str,
    ) -> None:
        """Print a message."""
        print(message)


printer_method_docstring: str | None = Printer.print_message.__doc__

print(printer_method_docstring)


# =============================================================================
# 32. Using help()
# =============================================================================
"""
Python's built-in help() function can display documentation.

For example:

    help(calculate_total)

The output can include:

    - function name
    - function signature
    - docstring

help() is especially useful when exploring unfamiliar code.
"""

# =============================================================================
# 33. help() Example
# =============================================================================


def convert_to_uppercase(
    text: str,
) -> str:
    """
    Convert text to uppercase.

    Args:
        text: The text to convert.

    Returns:
        The uppercase version of the supplied text.
    """
    return text.upper()


print(convert_to_uppercase("hello"))

# Uncomment the following line when interactive documentation is desired:
#
# help(convert_to_uppercase)


# =============================================================================
# 34. PEP 257
# =============================================================================
"""
PEP 257 describes conventions for Python docstrings.

Important principles include:

    - Use triple-quoted strings for docstrings.
    - Keep the first line as a concise summary.
    - Separate a summary from additional explanation with a blank line.
    - Write docstrings for public modules, functions, classes, and methods.
    - Keep the summary line meaningful.
    - Use consistent formatting.

A simple example:

    def square(
        number: int,
    ) -> int:
        \"\"\"Return the square of number.\"\"\"
        return number ** 2
"""

# =============================================================================
# 35. Concise Summary First
# =============================================================================


def get_username(
    username: str,
) -> str:
    """
    Return the supplied username.

    The function currently performs no additional transformation.
    """
    return username


username_result: str = get_username(
    "alex",
)

print(username_result)


# =============================================================================
# 36. Blank Line After Summary
# =============================================================================
"""
For a longer docstring, the summary can be followed by a blank line.

Example:

    def calculate_invoice(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"
        Calculate an invoice total.

        The function multiplies the unit price by the quantity.
        \"\"\"
        return price * quantity

The blank line visually separates the short summary from the extended
description.
"""

# =============================================================================
# 37. Google-Style Docstrings
# =============================================================================
"""
Google-style docstrings commonly use sections such as:

    Args:
    Returns:
    Raises:
    Yields:
    Examples:
    Notes:
    Warning:

Example:

    def divide(
        numerator: float,
        denominator: float,
    ) -> float:
        \"\"\"
        Divide two numbers.

        Args:
            numerator: Number being divided.
            denominator: Number used as divisor.

        Returns:
            The division result.

        Raises:
            ValueError: If denominator is zero.
        \"\"\"
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        return numerator / denominator
"""

# =============================================================================
# 38. Google-Style Example
# =============================================================================


def calculate_average(
    values: list[float],
) -> float:
    """
    Calculate the arithmetic mean.

    Args:
        values: A non-empty list of numbers.

    Returns:
        The arithmetic mean of the supplied values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty.")

    return sum(values) / len(values)


average: float = calculate_average(
    [10.0, 20.0, 30.0],
)

print(average)


# =============================================================================
# 39. NumPy-Style Docstrings
# =============================================================================
"""
NumPy-style documentation commonly uses section headers such as:

    Parameters
    ----------
    Returns
    -------
    Raises
    ------
    Examples
    --------

Example:

    def square(
        number: float,
    ) -> float:
        \"\"\"
        Calculate the square of a number.

        Parameters
        ----------
        number:
            Number to square.

        Returns
        -------
        float
            The squared value.
        \"\"\"
        return number ** 2

NumPy-style documentation is common in scientific Python projects.
"""

# =============================================================================
# 40. NumPy-Style Example
# =============================================================================


def calculate_cube(
    number: float,
) -> float:
    """
    Calculate the cube of a number.

    Parameters
    ----------
    number:
        Number to cube.

    Returns
    -------
    float
        The cubed value.
    """
    return number**3


cube_result: float = calculate_cube(
    4.0,
)

print(cube_result)


# =============================================================================
# 41. Sphinx-Style Docstrings
# =============================================================================
"""
Sphinx-style documentation commonly uses directives such as:

    :param:
    :return:
    :raises:

Example:

    def divide(
        numerator: float,
        denominator: float,
    ) -> float:
        \"\"\"
        Divide two numbers.

        :param numerator: Number being divided.
        :param denominator: Number used as divisor.
        :return: Division result.
        :raises ValueError: If denominator is zero.
        \"\"\"
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        return numerator / denominator

Sphinx-style documentation is commonly used with documentation generators.
"""

# =============================================================================
# 42. Sphinx-Style Example
# =============================================================================


def subtract_numbers(
    first: int,
    second: int,
) -> int:
    """
    Subtract one integer from another.

    :param first: Number from which to subtract.
    :param second: Number to subtract.
    :return: The subtraction result.
    """
    return first - second


subtraction_result: int = subtract_numbers(
    20,
    5,
)

print(subtraction_result)


# =============================================================================
# 43. Documenting a Boolean Parameter
# =============================================================================


def format_status(
    active: bool,
) -> str:
    """
    Format an account status.

    Args:
        active: Whether the account is currently active.

    Returns:
        "Active" when active is True, otherwise "Inactive".
    """
    if active:
        return "Active"

    return "Inactive"


active_status: str = format_status(
    True,
)

inactive_status: str = format_status(
    False,
)

print(active_status)
print(inactive_status)


# =============================================================================
# 44. Documenting a Dictionary Parameter
# =============================================================================


def get_setting(
    settings: dict[str, str],
    key: str,
) -> str | None:
    """
    Retrieve a setting from a dictionary.

    Args:
        settings: Dictionary containing configuration values.
        key: Name of the setting to retrieve.

    Returns:
        The setting value when the key exists, otherwise None.
    """
    return settings.get(key)


settings: dict[str, str] = {
    "environment": "production",
    "region": "india",
}

environment: str | None = get_setting(
    settings,
    "environment",
)

print(environment)


# =============================================================================
# 45. Documenting a Callable Parameter
# =============================================================================
"""
A function can receive another function as an argument.

The docstring can explain what the callable is expected to do.
"""

# =============================================================================
# 46. Callable Parameter Example
# =============================================================================


from collections.abc import Callable


def apply_operation(
    value: int,
    operation: Callable[[int], int],
) -> int:
    """
    Apply an operation to an integer.

    Args:
        value: The input integer.
        operation: A callable that accepts an integer and returns an integer.

    Returns:
        The result produced by operation.
    """
    return operation(value)


def double_value(
    value: int,
) -> int:
    """Return twice the supplied value."""
    return value * 2


operation_result: int = apply_operation(
    10,
    double_value,
)

print(operation_result)


# =============================================================================
# 47. Documenting Generator Functions
# =============================================================================


def generate_numbers(
    count: int,
) -> list[int]:
    """
    Generate a sequence of integers.

    Args:
        count: Number of integers to generate.

    Returns:
        A list containing integers from zero through count - 1.

    Raises:
        ValueError: If count is negative.
    """
    if count < 0:
        raise ValueError("count must not be negative.")

    return list(range(count))


generated_numbers: list[int] = generate_numbers(
    5,
)

print(generated_numbers)


# =============================================================================
# 48. Documenting a Function With No Return Value
# =============================================================================


def display_message(
    message: str,
) -> None:
    """
    Display a message.

    Args:
        message: Text to display.
    """
    print(message)


display_message(
    "Hello from a documented function.",
)


# =============================================================================
# 49. Documenting an In-Place Operation
# =============================================================================


def sort_numbers(
    numbers: list[int],
) -> None:
    """
    Sort a list of integers in place.

    Args:
        numbers: The list to sort.

    Side Effects:
        Mutates numbers by sorting it in ascending order.
    """
    numbers.sort()


unsorted_numbers: list[int] = [
    5,
    2,
    8,
    1,
]

sort_numbers(
    unsorted_numbers,
)

print(unsorted_numbers)


# =============================================================================
# 50. Documenting an In-Place Dictionary Update
# =============================================================================


def update_settings(
    settings: dict[str, str],
    key: str,
    value: str,
) -> None:
    """
    Update a setting in place.

    Args:
        settings: Dictionary to modify.
        key: Name of the setting.
        value: New value for the setting.

    Side Effects:
        Adds or replaces the specified dictionary entry.
    """
    settings[key] = value


configuration: dict[str, str] = {
    "environment": "development",
}

update_settings(
    configuration,
    "environment",
    "production",
)

print(configuration)


# =============================================================================
# 51. Docstrings and Exceptions Should Match Behavior
# =============================================================================
"""
A docstring should describe behavior that the function actually performs.

Avoid documenting an exception that the function never raises.

Bad documentation:

    def add(
        first: int,
        second: int,
    ) -> int:
        \"\"\"
        Add two numbers.

        Raises:
            ValueError: When the database connection fails.
        \"\"\"
        return first + second

The documented exception has nothing to do with the implementation.

Documentation should remain synchronized with code.
"""

# =============================================================================
# 52. Accurate Exception Documentation
# =============================================================================


def positive_square(
    number: float,
) -> float:
    """
    Calculate the square of a positive number.

    Args:
        number: Number that must be greater than zero.

    Returns:
        The square of number.

    Raises:
        ValueError: If number is zero or negative.
    """
    if number <= 0:
        raise ValueError("number must be positive.")

    return number**2


positive_square_result: float = positive_square(
    5.0,
)

print(positive_square_result)


# =============================================================================
# 53. Documenting Units
# =============================================================================
"""
When a parameter represents a measurement, the docstring should clarify
the unit when it is not obvious from the type.

For example:

    timeout: float

does not tell the reader whether the value is:

    - seconds
    - milliseconds
    - minutes

A useful docstring can specify the unit.
"""

# =============================================================================
# 54. Unit Documentation Example
# =============================================================================


def calculate_distance(
    speed_kilometers_per_hour: float,
    hours: float,
) -> float:
    """
    Calculate distance traveled.

    Args:
        speed_kilometers_per_hour: Speed measured in kilometers per hour.
        hours: Travel duration measured in hours.

    Returns:
        Distance traveled in kilometers.
    """
    return speed_kilometers_per_hour * hours


distance: float = calculate_distance(
    60.0,
    2.0,
)

print(distance)


# =============================================================================
# 55. Documenting Percentages
# =============================================================================


def calculate_percentage(
    value: float,
    percentage: float,
) -> float:
    """
    Calculate a percentage of a value.

    Args:
        value: Base value.
        percentage: Percentage expressed from 0 to 100.

    Returns:
        The requested percentage of value.
    """
    return value * percentage / 100.0


percentage_result: float = calculate_percentage(
    500.0,
    20.0,
)

print(percentage_result)


# =============================================================================
# 56. Documenting Valid Ranges
# =============================================================================


def calculate_percentage_strict(
    value: float,
    percentage: float,
) -> float:
    """
    Calculate a percentage within a valid range.

    Args:
        value: Base value.
        percentage: Percentage between 0 and 100 inclusive.

    Returns:
        The requested percentage of value.

    Raises:
        ValueError: If percentage is outside the range 0 through 100.
    """
    if percentage < 0.0 or percentage > 100.0:
        raise ValueError("percentage must be between 0 and 100.")

    return value * percentage / 100.0


strict_percentage: float = calculate_percentage_strict(
    1000.0,
    15.0,
)

print(strict_percentage)


# =============================================================================
# 57. Docstrings Can Include Examples
# =============================================================================


def multiply_numbers(
    first: int,
    second: int,
) -> int:
    """
    Multiply two integers.

    Args:
        first: First integer.
        second: Second integer.

    Returns:
        The product of the two integers.

    Examples:
        >>> multiply_numbers(3, 4)
        12
    """
    return first * second


multiplication_result: int = multiply_numbers(
    3,
    4,
)

print(multiplication_result)


# =============================================================================
# 58. Example Sections Should Be Accurate
# =============================================================================
"""
Examples inside docstrings should match the actual behavior of the code.

For example:

    def square(
        number: int,
    ) -> int:
        \"\"\"
        Return the square of a number.

        Examples:
            >>> square(5)
            25
        \"\"\"
        return number ** 2

Documentation examples can be used by documentation systems and, depending
on tooling and configuration, may also be tested as doctests.
"""

# =============================================================================
# 59. Docstrings and Doctests
# =============================================================================


def add_for_doctest(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.

    Examples:
        >>> add_for_doctest(2, 3)
        5
    """
    return first + second


doctest_result: int = add_for_doctest(
    2,
    3,
)

print(doctest_result)


# =============================================================================
# 60. Avoid Unnecessary Docstrings
# =============================================================================
"""
Not every tiny private implementation detail requires a long docstring.

For example:

    def double(
        value: int,
    ) -> int:
        \"\"\"Return twice value.\"\"\"
        return value * 2

A short docstring is sufficient.

The goal is useful documentation, not maximum documentation length.
"""

# =============================================================================
# 61. Avoid Repeating the Function Name
# =============================================================================


def get_total(
    values: list[int],
) -> int:
    """Return the sum of all values."""
    return sum(values)


total_value: int = get_total(
    [1, 2, 3, 4],
)

print(total_value)


# =============================================================================
# 62. Bad Versus Better Docstrings
# =============================================================================
"""
Bad:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"
        This function calculates the total.
        \"\"\"
        return price * quantity

Better:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"Return the total price for the requested quantity.\"\"\"
        return price * quantity

The better version is concise and provides useful information.
"""

# =============================================================================
# 63. Docstring Should Match the Return Value
# =============================================================================


def get_full_name(
    first_name: str,
    last_name: str,
) -> str:
    """
    Combine a first name and last name.

    Args:
        first_name: Person's first name.
        last_name: Person's last name.

    Returns:
        The combined full name.
    """
    return f"{first_name} {last_name}"


full_name: str = get_full_name(
    "Alex",
    "Smith",
)

print(full_name)


# =============================================================================
# 64. Documenting Boolean Results
# =============================================================================


def is_even(
    number: int,
) -> bool:
    """
    Determine whether a number is even.

    Args:
        number: Integer to test.

    Returns:
        True if number is even, otherwise False.
    """
    return number % 2 == 0


even_result: bool = is_even(
    10,
)

print(even_result)


# =============================================================================
# 65. Documenting None Results
# =============================================================================


def reset_items(
    items: list[str],
) -> None:
    """
    Remove all items from a list.

    Args:
        items: List to clear.

    Side Effects:
        Removes every element from items.
    """
    items.clear()


items: list[str] = [
    "Python",
    "SQL",
]

reset_items(
    items,
)

print(items)


# =============================================================================
# 66. Documenting Dictionaries Returned From Functions
# =============================================================================


def create_configuration() -> dict[str, str]:
    """
    Create the default application configuration.

    Returns:
        A dictionary containing default configuration values.
    """
    return {
        "environment": "development",
        "region": "india",
    }


default_configuration: dict[str, str] = create_configuration()

print(default_configuration)


# =============================================================================
# 67. Documenting Lists Returned From Functions
# =============================================================================


def get_supported_languages() -> list[str]:
    """
    Return the supported programming languages.

    Returns:
        A list containing supported language names.
    """
    return [
        "Python",
        "Go",
        "Java",
    ]


supported_languages: list[str] = get_supported_languages()

print(supported_languages)


# =============================================================================
# 68. Documenting Tuples Returned From Functions
# =============================================================================


def get_coordinates() -> tuple[float, float]:
    """
    Return example geographic coordinates.

    Returns:
        A tuple containing latitude and longitude.
    """
    return (
        12.9716,
        77.5946,
    )


coordinates: tuple[float, float] = get_coordinates()

print(coordinates)


# =============================================================================
# 69. Documenting Union Return Types
# =============================================================================


def find_username(
    usernames: dict[int, str],
    user_id: int,
) -> str | None:
    """
    Find a username by user ID.

    Args:
        usernames: Mapping of user IDs to usernames.
        user_id: ID to search for.

    Returns:
        The username when found, otherwise None.
    """
    return usernames.get(user_id)


users: dict[int, str] = {
    1: "alex",
    2: "sam",
}

found_username: str | None = find_username(
    users,
    1,
)

print(found_username)


# =============================================================================
# 70. Documenting Keyword-Only Options
# =============================================================================


def format_price(
    price: float,
    *,
    currency: str = "USD",
    decimals: int = 2,
) -> str:
    """
    Format a monetary value.

    Args:
        price: Numeric price.
        currency: Currency code to display.
        decimals: Number of decimal places.

    Returns:
        Formatted monetary value.
    """
    return f"{currency} {price:.{decimals}f}"


formatted_price: str = format_price(
    1250.5,
    currency="INR",
    decimals=2,
)

print(formatted_price)


# =============================================================================
# 71. Documenting *args
# =============================================================================


def sum_numbers(
    *numbers: int,
) -> int:
    """
    Sum any number of integers.

    Args:
        *numbers: Integers to add together.

    Returns:
        The sum of all supplied integers.
    """
    return sum(numbers)


numbers_sum: int = sum_numbers(
    10,
    20,
    30,
)

print(numbers_sum)


# =============================================================================
# 72. Documenting **kwargs
# =============================================================================


def describe_options(
    **options: str,
) -> dict[str, str]:
    """
    Return supplied string options.

    Args:
        **options: Named string options.

    Returns:
        A dictionary containing the supplied options.
    """
    return options


options: dict[str, str] = describe_options(
    environment="production",
    region="india",
)

print(options)


# =============================================================================
# 73. Docstrings for Public APIs
# =============================================================================
"""
Public functions are especially important to document.

A public API may be used by:

    - other modules
    - other developers
    - external applications
    - documentation generators
    - IDEs
    - automated tooling

A good public API should communicate:

    - what the function does
    - what inputs mean
    - what it returns
    - what errors can occur
    - important side effects
    - important constraints
"""

# =============================================================================
# 74. Public API Example
# =============================================================================


def process_payment(
    amount: float,
    currency: str,
) -> str:
    """
    Process a payment request.

    Args:
        amount: Payment amount. Must be greater than zero.
        currency: Three-letter currency code.

    Returns:
        A confirmation message.

    Raises:
        ValueError: If amount is not positive or currency is empty.
    """
    if amount <= 0:
        raise ValueError("amount must be greater than zero.")

    if not currency:
        raise ValueError("currency must not be empty.")

    return f"Payment processed: {amount:.2f} {currency}"


payment_message: str = process_payment(
    100.0,
    "USD",
)

print(payment_message)


# =============================================================================
# 75. Docstrings and Private Functions
# =============================================================================
"""
Private functions can also have docstrings.

For example:

    def _normalize_name(
        name: str,
    ) -> str:
        \"\"\"Normalize a name for internal use.\"\"\"
        return name.strip().lower()

The underscore indicates that the function is intended for internal use,
but documentation can still be useful for complex private functions.
"""

# =============================================================================
# 76. Private Function Example
# =============================================================================


def _normalize_name(
    name: str,
) -> str:
    """Normalize a name by removing surrounding whitespace and lowercasing."""
    return name.strip().lower()


normalized_name: str = _normalize_name(
    "  Alex  ",
)

print(normalized_name)


# =============================================================================
# 77. Docstrings and Naming
# =============================================================================
"""
Good names reduce the amount of documentation required.

Compare:

    def calculate_total_price(
        item_price: float,
        item_quantity: int,
    ) -> float:
        \"\"\"Return item price multiplied by item quantity.\"\"\"

with a poorly named function:

    def process(
        x: float,
        y: int,
    ) -> float:
        \"\"\"Calculate the total price.\"\"\"

The first function communicates more through its names.

Docstrings should complement good naming rather than compensate for
unclear names.
"""

# =============================================================================
# 78. Documenting Complex Logic
# =============================================================================


def calculate_progress(
    completed: int,
    total: int,
) -> float:
    """
    Calculate completion progress as a percentage.

    Args:
        completed: Number of completed items.
        total: Total number of items.

    Returns:
        Completion percentage between 0 and 100.

    Raises:
        ValueError: If total is zero or negative.
    """
    if total <= 0:
        raise ValueError("total must be greater than zero.")

    return completed / total * 100.0


progress: float = calculate_progress(
    75,
    100,
)

print(progress)


# =============================================================================
# 79. Docstrings Should Explain Constraints
# =============================================================================


def calculate_ratio(
    numerator: float,
    denominator: float,
) -> float:
    """
    Calculate a numeric ratio.

    Args:
        numerator: Number placed above the division line.
        denominator: Number placed below the division line.

    Returns:
        The ratio of numerator to denominator.

    Raises:
        ValueError: If denominator is zero.
    """
    if denominator == 0:
        raise ValueError("denominator must not be zero.")

    return numerator / denominator


ratio: float = calculate_ratio(
    50.0,
    10.0,
)

print(ratio)


# =============================================================================
# 80. Docstrings and Readability
# =============================================================================
"""
A good docstring should make code easier to understand.

Avoid unnecessarily complicated wording.

Instead of:

    \"\"\"
    This function is responsible for the purpose of taking a supplied
    integer value and subsequently performing a multiplication operation
    against itself.
    \"\"\"

Prefer:

    \"\"\"Return the square of an integer.\"\"\"

Clear documentation is usually better than verbose documentation.
"""

# =============================================================================
# 81. Avoid Implementation Details When Unnecessary
# =============================================================================


def get_active_users(
    users: list[str],
) -> list[str]:
    """
    Return the supplied active-user list.

    Args:
        users: Usernames considered active.
    """
    return users


active_users: list[str] = get_active_users(
    ["alex", "sam"],
)

print(active_users)


# =============================================================================
# 82. Document Why When Necessary
# =============================================================================
"""
Sometimes the important information is not what the function does, but why
a particular behavior exists.

For example:

    def normalize_identifier(
        identifier: str,
    ) -> str:
        \"\"\"
        Normalize an identifier.

        Identifiers are normalized before comparison so that equivalent
        identifiers can be compared consistently.
        \"\"\"
        return identifier.strip().lower()

Documenting important reasons can be more valuable than describing obvious
implementation details.
"""

# =============================================================================
# 83. Docstring With Notes
# =============================================================================


def normalize_identifier(
    identifier: str,
) -> str:
    """
    Normalize an identifier.

    Args:
        identifier: Identifier to normalize.

    Returns:
        Lowercase identifier without surrounding whitespace.

    Notes:
        Normalization allows identifiers to be compared consistently.
    """
    return identifier.strip().lower()


identifier: str = normalize_identifier(
    "  USER-001  ",
)

print(identifier)


# =============================================================================
# 84. Docstring With Warning
# =============================================================================


def remove_all_items(
    items: list[str],
) -> None:
    """
    Remove all items from a list.

    Args:
        items: List to clear.

    Warning:
        This operation permanently removes the current list contents.
    """
    items.clear()


values_to_clear: list[str] = [
    "A",
    "B",
    "C",
]

remove_all_items(
    values_to_clear,
)

print(values_to_clear)


# =============================================================================
# 85. Docstrings Are Runtime Metadata
# =============================================================================
"""
A docstring is not simply discarded like an ordinary comment.

For supported objects, Python stores the documentation string in __doc__.

This makes docstrings runtime metadata.

For example:

    def greet() -> str:
        \"\"\"Return a greeting.\"\"\"
        return "Hello"

Then:

    greet.__doc__

contains:

    "Return a greeting."

This is one of the main technical differences between comments and
docstrings.
"""

# =============================================================================
# 86. Inspecting Documentation Programmatically
# =============================================================================


def documented_function() -> str:
    """Return a message from a documented function."""
    return "Documentation example."


documentation: str | None = documented_function.__doc__

if documentation is not None:
    print(documentation)


# =============================================================================
# 87. Docstrings and IDEs
# =============================================================================
"""
Modern IDEs can display docstrings while developers work with functions.

For example, when calling:

    calculate_total(

an IDE can display documentation explaining:

    - parameter meanings
    - return values
    - exceptions
    - additional notes

Good docstrings therefore improve the developer experience directly inside
the editor.
"""

# =============================================================================
# 88. Docstrings and Type Checkers
# =============================================================================
"""
Type checkers such as mypy primarily use type annotations to verify types.

Docstrings do not replace type annotations.

For example:

    def add(
        first: int,
        second: int,
    ) -> int:
        \"\"\"Return the sum of two integers.\"\"\"
        return first + second

The annotations communicate types.

The docstring communicates behavior.

Using both provides more complete information.
"""

# =============================================================================
# 89. Docstrings and Documentation Generators
# =============================================================================
"""
Documentation generators can inspect Python docstrings and create
human-readable documentation.

Common documentation ecosystems include:

    - Sphinx
    - MkDocs
    - pydoc
    - IDE documentation systems

The exact syntax expected by a documentation generator can vary.
"""

# =============================================================================
# 90. Module-Level Documentation Example
# =============================================================================
"""
A well-documented module typically begins with:

    1. Module docstring.
    2. Imports.
    3. Constants.
    4. Functions.
    5. Classes.
    6. Other implementation details.

For example:

    \"\"\"
    Utilities for processing invoices.
    \"\"\"

    from decimal import Decimal

    DEFAULT_TAX_RATE = Decimal("0.18")

    def calculate_total(...):
        \"\"\"Calculate an invoice total.\"\"\"
        ...

The module docstring describes the overall purpose.
"""

# =============================================================================
# 91. Function Documentation Template
# =============================================================================
"""
A practical function documentation template is:

    def function_name(
        parameter: Type,
    ) -> ReturnType:
        \"\"\"
        Short summary.

        Additional explanation when necessary.

        Args:
            parameter: Explanation of the parameter.

        Returns:
            Explanation of the returned value.

        Raises:
            ValueError: Explanation of when this exception occurs.
        \"\"\"
        ...

Not every section is required.

Include only sections that provide useful information.
"""

# =============================================================================
# 92. Simple Function Documentation Template
# =============================================================================


def simple_function(
    value: int,
) -> int:
    """Return the supplied value doubled."""
    return value * 2


simple_result: int = simple_function(
    10,
)

print(simple_result)


# =============================================================================
# 93. Detailed Function Documentation Template
# =============================================================================


def detailed_function(
    price: float,
    quantity: int,
    *,
    tax_rate: float = 18.0,
) -> float:
    """
    Calculate the final price including tax.

    The tax rate is interpreted as a percentage.

    Args:
        price: Price of one item.
        quantity: Number of items.
        tax_rate: Tax percentage applied to the subtotal.

    Returns:
        Final price including calculated tax.

    Raises:
        ValueError: If price, quantity, or tax_rate is negative.
    """
    if price < 0:
        raise ValueError("price must not be negative.")

    if quantity < 0:
        raise ValueError("quantity must not be negative.")

    if tax_rate < 0:
        raise ValueError("tax_rate must not be negative.")

    subtotal: float = price * quantity
    tax: float = subtotal * tax_rate / 100.0

    return subtotal + tax


detailed_total: float = detailed_function(
    100.0,
    2,
    tax_rate=18.0,
)

print(detailed_total)


# =============================================================================
# 94. Docstrings for Classes
# =============================================================================


class BankAccount:
    """
    Represent a basic bank account.

    Attributes:
        owner: Name of the account owner.
        balance: Current account balance.
    """

    def __init__(
        self,
        owner: str,
        balance: float = 0.0,
    ) -> None:
        """
        Initialize a bank account.

        Args:
            owner: Name of the account owner.
            balance: Initial account balance.
        """
        self.owner: str = owner
        self.balance: float = balance

    def deposit(
        self,
        amount: float,
    ) -> None:
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit.

        Raises:
            ValueError: If amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("amount must be greater than zero.")

        self.balance += amount

    def withdraw(
        self,
        amount: float,
    ) -> None:
        """
        Withdraw money from the account.

        Args:
            amount: Amount to withdraw.

        Raises:
            ValueError: If amount is zero, negative, or greater than balance.
        """
        if amount <= 0:
            raise ValueError("amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("insufficient balance.")

        self.balance -= amount


account: BankAccount = BankAccount(
    "Alex",
    1000.0,
)

account.deposit(
    500.0,
)

account.withdraw(
    200.0,
)

print(account.balance)


# =============================================================================
# 95. Docstrings for Properties
# =============================================================================


class Rectangle:
    """Represent a rectangle."""

    def __init__(
        self,
        width: float,
        height: float,
    ) -> None:
        """Initialize a rectangle."""
        self.width: float = width
        self.height: float = height

    @property
    def area(self) -> float:
        """Return the rectangle's area."""
        return self.width * self.height


rectangle: Rectangle = Rectangle(
    10.0,
    5.0,
)

print(rectangle.area)


# =============================================================================
# 96. Docstrings for Static Methods
# =============================================================================


class NumberTools:
    """Provide utility operations for numbers."""

    @staticmethod
    def double(
        value: int,
    ) -> int:
        """Return twice the supplied value."""
        return value * 2


static_result: int = NumberTools.double(
    10,
)

print(static_result)


# =============================================================================
# 97. Docstrings for Class Methods
# =============================================================================


class UserProfile:
    """Represent a user profile."""

    def __init__(
        self,
        username: str,
    ) -> None:
        """Initialize a user profile."""
        self.username: str = username

    @classmethod
    def guest(cls) -> "UserProfile":
        """Create a guest user profile."""
        return cls("guest")


guest_profile: UserProfile = UserProfile.guest()

print(guest_profile.username)


# =============================================================================
# 98. Docstrings and Inheritance
# =============================================================================


class Animal:
    """Represent a generic animal."""

    def speak(self) -> str:
        """Return the animal's sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> str:
        """Return the sound produced by a dog."""
        return "Woof"


animal: Animal = Animal()
dog: Dog = Dog()

print(animal.speak())
print(dog.speak())


# =============================================================================
# 99. Docstrings and Overrides
# =============================================================================
"""
When overriding a method, documenting the overridden behavior can still be
useful when the subclass changes or specializes the behavior.

Example:

    class Dog(Animal):
        \"\"\"Represent a dog.\"\"\"

        def speak(self) -> str:
            \"\"\"Return the sound produced by a dog.\"\"\"
            return "Woof"

The subclass docstring explains the specialized behavior.
"""

# =============================================================================
# 100. Docstring Formatting Rules
# =============================================================================
"""
Common formatting practices:

    - Use triple quotes.
    - Place the opening docstring immediately after the definition.
    - Start with a concise summary.
    - Use a blank line before detailed sections.
    - Indent the docstring consistently.
    - Document public APIs.
    - Explain parameters when their meaning is not obvious.
    - Explain return values when useful.
    - Document important exceptions.
    - Document important side effects.
    - Keep examples accurate.
    - Keep documentation synchronized with implementation.
"""

# =============================================================================
# 101. Docstring Placement
# =============================================================================
"""
Correct:

    def greet() -> str:
        \"\"\"Return a greeting.\"\"\"
        return "Hello"

Incorrect:

    def greet() -> str:
        return "Hello"

        \"\"\"Return a greeting.\"\"\"

The docstring must be the first statement in the function body.

The same principle applies to modules, classes, and methods.
"""

# =============================================================================
# 102. Docstring Must Be First Statement
# =============================================================================


def first_statement_example() -> str:
    """Return a message demonstrating correct docstring placement."""
    return "Correct placement"


first_statement_result: str = first_statement_example()

print(first_statement_result)


# =============================================================================
# 103. Triple Single Quotes
# =============================================================================
"""
Docstrings can use triple single quotes.

Example:

    def greet() -> str:
        '''
        Return a greeting.
        '''
        return "Hello"

Triple double quotes are also valid.

The important point is that the string must be the first statement in the
documented object's body.
"""

# =============================================================================
# 104. Triple Double Quotes
# =============================================================================


def triple_double_quote_example() -> str:
    """
    Return a message using a triple-double-quoted docstring.
    """
    return "Triple double quotes."


triple_quote_result: str = triple_double_quote_example()

print(triple_quote_result)


# =============================================================================
# 105. Docstring Indentation
# =============================================================================
"""
Docstrings should follow the indentation level of the object they document.

Example:

    class Example:
        \"\"\"Document the class.\"\"\"

        def method(self) -> None:
            \"\"\"Document the method.\"\"\"
            pass

Incorrect indentation can cause syntax errors or formatting problems.
"""

# =============================================================================
# 106. Docstrings and Nested Functions
# =============================================================================


def outer_function() -> str:
    """Create a nested function and return its result."""

    def inner_function() -> str:
        """Return a message from the nested function."""
        return "Nested function."

    return inner_function()


nested_result: str = outer_function()

print(nested_result)


# =============================================================================
# 107. Accessing Nested Function Documentation
# =============================================================================


def create_documented_function() -> Callable[[], str]:
    """Create and return a documented nested function."""

    def nested() -> str:
        """Return a message from the nested function."""
        return "Nested documentation."

    return nested


documented_nested: Callable[[], str] = create_documented_function()

nested_docstring: str | None = documented_nested.__doc__

print(nested_docstring)


# =============================================================================
# 108. Docstrings and Closures
# =============================================================================


def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a multiplication function.

    Args:
        multiplier: Value remembered by the returned function.

    Returns:
        A function that multiplies an integer by multiplier.
    """

    def multiply(
        number: int,
    ) -> int:
        """Multiply number by the captured multiplier."""
        return number * multiplier

    return multiply


double: Callable[[int], int] = create_multiplier(
    2,
)

double_value_result: int = double(
    10,
)

print(double_value_result)


# =============================================================================
# 109. Docstrings and Decorators
# =============================================================================
"""
Decorators can affect function metadata.

When writing decorators, functools.wraps is commonly used so that metadata
such as the wrapped function's name and docstring is preserved.
"""

# =============================================================================
# 110. functools.wraps Example
# =============================================================================


from functools import wraps


def announce(
    function: Callable[[], str],
) -> Callable[[], str]:
    """Decorate a function with a simple announcement."""

    @wraps(function)
    def wrapper() -> str:
        """Call the wrapped function and return its result."""
        print("Calling function.")
        return function()

    return wrapper


@announce
def documented_action() -> str:
    """Return a documented action message."""
    return "Action completed."


action_result: str = documented_action()

print(action_result)
print(documented_action.__doc__)


# =============================================================================
# 111. Why functools.wraps Matters
# =============================================================================
"""
Without functools.wraps, a decorator can replace the original function's
metadata with the wrapper's metadata.

Using:

    @wraps(function)

helps preserve metadata such as:

    - __name__
    - __doc__
    - __module__
    - __annotations__

This is particularly important when documentation and introspection are
used.
"""

# =============================================================================
# 112. Docstrings and __annotations__
# =============================================================================


def annotated_function(
    value: int,
) -> str:
    """Convert an integer into a string."""
    return str(value)


print(annotated_function.__doc__)
print(annotated_function.__annotations__)


# =============================================================================
# 113. Docstrings Are Not Type Annotations
# =============================================================================
"""
Do not confuse:

    __doc__

with:

    __annotations__

For example:

    def example(
        value: int,
    ) -> str:
        \"\"\"Convert value to text.\"\"\"
        return str(value)

The docstring is available through:

    example.__doc__

The type annotations are available through:

    example.__annotations__

They provide different kinds of information.
"""

# =============================================================================
# 114. Practical Documentation Pattern
# =============================================================================


def calculate_invoice_total(
    unit_price: float,
    quantity: int,
    *,
    tax_rate: float = 18.0,
) -> float:
    """
    Calculate the final invoice total.

    Args:
        unit_price: Price of one item.
        quantity: Number of items.
        tax_rate: Tax rate expressed as a percentage.

    Returns:
        Final total including tax.

    Raises:
        ValueError: If unit_price, quantity, or tax_rate is negative.
    """
    if unit_price < 0:
        raise ValueError("unit_price must not be negative.")

    if quantity < 0:
        raise ValueError("quantity must not be negative.")

    if tax_rate < 0:
        raise ValueError("tax_rate must not be negative.")

    subtotal: float = unit_price * quantity
    tax: float = subtotal * tax_rate / 100.0

    return subtotal + tax


invoice_total: float = calculate_invoice_total(
    100.0,
    5,
    tax_rate=18.0,
)

print(invoice_total)


# =============================================================================
# 115. Common Mistakes
# =============================================================================
"""
Common docstring mistakes include:

    - Forgetting the docstring entirely.
    - Putting the docstring after another statement.
    - Writing an inaccurate description.
    - Documenting parameters incorrectly.
    - Documenting exceptions that never occur.
    - Forgetting important side effects.
    - Writing excessively long documentation for simple functions.
    - Using inconsistent formatting.
    - Providing outdated examples.
    - Repeating obvious implementation details.
    - Confusing docstrings with comments.
    - Assuming type annotations replace documentation.
"""

# =============================================================================
# 116. Bad Docstring Placement
# =============================================================================
"""
Incorrect:

    def example() -> None:
        value: int = 10
        \"\"\"This is not the function docstring.\"\"\"

The string is not the first statement.

Correct:

    def example() -> None:
        \"\"\"Document the function.\"\"\"
        value: int = 10

Always place the docstring first.
"""

# =============================================================================
# 117. Bad Documentation Example
# =============================================================================
"""
Bad:

    def calculate(
        x: float,
        y: int,
    ) -> float:
        \"\"\"
        Do stuff.
        \"\"\"
        return x * y

The phrase "Do stuff" does not provide useful information.

Better:

    def calculate(
        price: float,
        quantity: int,
    ) -> float:
        \"\"\"Return price multiplied by quantity.\"\"\"
        return price * quantity

Meaningful names and meaningful documentation work together.
"""

# =============================================================================
# 118. Documentation Should Stay Current
# =============================================================================
"""
If implementation changes, documentation should change with it.

For example, suppose a function originally accepts:

    percentage: float

and later changes to accept:

    rate: float

The documentation should be updated accordingly.

Outdated documentation can be worse than missing documentation because it
can actively mislead users.
"""

# =============================================================================
# 119. Documentation Should Describe the Public Contract
# =============================================================================
"""
A useful way to think about a docstring is as a description of a function's
public contract.

The contract can include:

    - accepted inputs
    - expected input meaning
    - returned output
    - errors
    - side effects
    - constraints
    - important behavior

Implementation details that are irrelevant to callers generally do not need
to be included.
"""

# =============================================================================
# 120. Practical Public Contract Example
# =============================================================================


def withdraw_money(
    balance: float,
    amount: float,
) -> float:
    """
    Withdraw money from an account balance.

    Args:
        balance: Current account balance.
        amount: Amount to withdraw.

    Returns:
        Remaining account balance.

    Raises:
        ValueError: If amount is not positive or exceeds balance.
    """
    if amount <= 0:
        raise ValueError("amount must be greater than zero.")

    if amount > balance:
        raise ValueError("amount exceeds balance.")

    return balance - amount


remaining_balance: float = withdraw_money(
    1000.0,
    250.0,
)

print(remaining_balance)


# =============================================================================
# 121. Scope of Docstrings
# =============================================================================
"""
A docstring belongs to the Python object immediately following it.

At module level:

    \"\"\"Module documentation.\"\"\"

documents the module.

After a function definition:

    def example() -> None:
        \"\"\"Function documentation.\"\"\"

documents the function.

Inside a class:

    class Example:
        \"\"\"Class documentation.\"\"\"

documents the class.

Inside a method:

    def method(self) -> None:
        \"\"\"Method documentation.\"\"\"

documents the method.
"""

# =============================================================================
# 122. Docstring Summary
# =============================================================================
"""
Docstrings are an important part of Python documentation.

Core ideas:

    - A docstring documents a Python object.
    - A function docstring appears immediately inside the function.
    - A class docstring appears immediately inside the class.
    - A module docstring appears at the beginning of the module.
    - Docstrings are stored in __doc__.
    - help() can display docstrings.
    - IDEs can display docstrings while coding.
    - Documentation generators can process docstrings.
    - Type annotations describe types.
    - Docstrings describe meaning and behavior.
    - Comments usually explain implementation details.
    - Good docstrings are concise and accurate.
    - Longer functions may need Args, Returns, Raises, Notes, or Examples.
    - Side effects should be documented when they matter.
    - Exceptions should be documented when callers need to know about them.
    - Examples should match actual behavior.
    - Documentation should stay synchronized with implementation.
"""

# =============================================================================
# 123. Key Takeaways
# =============================================================================
"""
✓ A docstring is a string used to document Python code.

✓ A function docstring must be the first statement in the function body.

✓ A class docstring must be the first statement in the class body.

✓ A module docstring appears at the beginning of the module.

✓ Python stores docstrings in the __doc__ attribute.

✓ help() can display documentation.

✓ Docstrings are different from comments.

✓ Comments usually explain implementation details.

✓ Docstrings describe the public purpose and behavior of Python objects.

✓ Type annotations describe expected types.

✓ Type annotations do not replace docstrings.

✓ One-line docstrings are appropriate for simple functions.

✓ Multi-line docstrings are useful for more complex behavior.

✓ PEP 257 provides conventions for Python docstrings.

✓ Google-style docstrings commonly use:

    Args:
    Returns:
    Raises:
    Examples:
    Notes:
    Warning:

✓ NumPy-style docstrings commonly use:

    Parameters
    ----------
    Returns
    -------
    Raises
    ------

✓ Sphinx-style docstrings commonly use:

    :param:
    :return:
    :raises:

✓ Parameter documentation should explain the meaning of parameters.

✓ Return documentation should explain important return values.

✓ Exception documentation should describe important expected failures.

✓ Side effects should be documented when they matter to callers.

✓ Mutable arguments should be documented when the function mutates them.

✓ Units and valid ranges should be documented when they are important.

✓ Examples should be accurate.

✓ Public APIs deserve especially clear documentation.

✓ Good names and good docstrings complement each other.

✓ Documentation should describe the public contract rather than unnecessary
  implementation details.

✓ Decorators should commonly use functools.wraps when preserving function
  metadata is important.

✓ Docstrings are runtime metadata and can be inspected programmatically.

Core model:

    MODULE
        ↓
    module docstring

    CLASS
        ↓
    class docstring

    FUNCTION
        ↓
    function docstring

    METHOD
        ↓
    method docstring

Documentation model:

    WHAT DOES IT DO?
        ↓
    SUMMARY

    WHAT INPUTS DOES IT ACCEPT?
        ↓
    Args

    WHAT DOES IT RETURN?
        ↓
    Returns

    WHAT CAN GO WRONG?
        ↓
    Raises

    WHAT DOES IT CHANGE?
        ↓
    Side Effects

    WHAT SPECIAL CONDITIONS EXIST?
        ↓
    Notes / Warnings

    HOW IS IT USED?
        ↓
    Examples
"""

# =============================================================================
# End of 15_docstrings.py
# =============================================================================