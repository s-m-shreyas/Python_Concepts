# =============================================================================
# 13. Nested Functions
# =============================================================================

# type: ignore

"""
Python Functions

File
----
13_nested_functions.py

Topic
-----
Nested Functions

Overview
--------
A nested function is a function defined inside another function.

The outer function creates the enclosing scope, while the nested function
creates its own local scope.

Nested functions are useful for:

- Encapsulation
- Helper functions
- Closures
- Function factories
- Maintaining private state
- Decorators
- Callbacks
- Validation helpers
- Separating implementation details

A basic nested-function structure looks like:

    def outer() -> None:
        def inner() -> None:
            pass

        inner()

The nested function can access names from its enclosing function.

Python commonly resolves names using the LEGB rule:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

Topics covered:

- What is a nested function?
- Basic nested functions
- Calling a nested function
- Nested function local scope
- Outer function scope
- Accessing outer variables
- Local variables of nested functions
- Parameters of nested functions
- Nested functions cannot directly access caller scope
- Multiple nested functions
- Multiple levels of nesting
- Returning a nested function
- Function factories
- Closures
- Closure state
- nonlocal with nested functions
- global with nested functions
- Reading enclosing variables
- Modifying enclosing variables
- Mutable enclosing variables
- Nested functions and mutable objects
- Nested functions and loops
- Nested functions and default arguments
- Nested functions and annotations
- Nested helper functions
- Validation helpers
- Calculation helpers
- Private implementation helpers
- Callback-style nested functions
- Nested functions returning values
- Nested functions accepting arguments
- Nested functions calling outer functions
- Nested functions calling other nested functions
- Closures with parameters
- Independent closures
- Function factories
- Decorator-like structures
- Practical nested-function patterns
- Common mistakes
- Best practices
"""

# =============================================================================
# 01. What Is a Nested Function?
# =============================================================================
"""
A nested function is a function defined inside another function.

Example:

    def outer() -> None:
        def inner() -> None:
            print("Inside inner")

        inner()

Here:

    outer()

is the outer function.

    inner()

is the nested function.

The nested function is defined inside the local scope of the outer function.

A nested function is also commonly called an inner function.
"""

# =============================================================================
# 02. Basic Nested Function
# =============================================================================


def greet_user() -> str:
    """
    Demonstrate a basic nested function.
    """

    def create_message() -> str:
        """
        Create a greeting message.
        """
        return "Hello, Guest!"

    return create_message()


basic_greeting: str = greet_user()

print(basic_greeting)


# =============================================================================
# 03. Calling a Nested Function
# =============================================================================


def outer_function() -> str:
    """
    Define and call a nested function.
    """

    def inner_function() -> str:
        """
        Return a message from the nested function.
        """
        return "Hello from inner_function()"

    result: str = inner_function()

    return result


outer_result: str = outer_function()

print(outer_result)


# =============================================================================
# 04. Nested Function Has Its Own Local Scope
# =============================================================================


def demonstrate_local_scope() -> str:
    """
    Demonstrate local scope inside a nested function.
    """

    def inner() -> str:
        """
        Create a local variable.
        """
        message: str = "Inner message"

        return message

    return inner()


local_scope_result: str = demonstrate_local_scope()

print(local_scope_result)

# The variable:
#
#     message
#
# belongs to inner().
#
# It is not a variable in the module's global scope.


# =============================================================================
# 05. Outer Function Has Its Own Local Scope
# =============================================================================


def demonstrate_outer_scope() -> str:
    """
    Demonstrate a variable belonging to the outer function.
    """
    outer_message: str = "Outer message"

    def inner() -> str:
        """
        Read the enclosing variable.
        """
        return outer_message

    return inner()


outer_scope_result: str = demonstrate_outer_scope()

print(outer_scope_result)

# outer_message belongs to:
#
#     demonstrate_outer_scope()
#
# It is an enclosing variable for inner().


# =============================================================================
# 06. Nested Function Can Read Outer Variables
# =============================================================================


def create_greeting(name: str) -> str:
    """
    Create a greeting using an enclosing variable.
    """
    prefix: str = "Hello"

    def build_message() -> str:
        """
        Use the enclosing prefix and name.
        """
        return f"{prefix}, {name}!"

    return build_message()


greeting: str = create_greeting("Shreyas")

print(greeting)


# =============================================================================
# 07. Nested Function Parameters
# =============================================================================


def create_message_builder(prefix: str) -> str:
    """
    Demonstrate parameters of a nested function.
    """

    def build_message(message: str) -> str:
        """
        Combine a local parameter with an enclosing variable.
        """
        return f"{prefix}: {message}"

    return build_message("Process completed")


message_result: str = create_message_builder("INFO")

print(message_result)

# prefix:
#
#     enclosing variable
#
# message:
#
#     local parameter of build_message()


# =============================================================================
# 08. Nested Function With Multiple Parameters
# =============================================================================


def calculate_values() -> int:
    """
    Use a nested function with multiple parameters.
    """

    def add_numbers(first: int, second: int) -> int:
        """
        Add two numbers.
        """
        return first + second

    return add_numbers(10, 20)


calculation_result: int = calculate_values()

print(calculation_result)


# =============================================================================
# 09. Outer Variable and Inner Parameters
# =============================================================================


def multiply_with_factor(factor: int) -> int:
    """
    Demonstrate an enclosing variable and a nested parameter.
    """

    def multiply(number: int) -> int:
        """
        Multiply using the enclosing factor.
        """
        return number * factor

    return multiply(10)


factor_result: int = multiply_with_factor(5)

print(factor_result)


# =============================================================================
# 10. Nested Function With Local Variables
# =============================================================================


def calculate_invoice() -> float:
    """
    Calculate an invoice using a nested helper function.
    """

    def calculate_tax(amount: float) -> float:
        """
        Calculate tax for an amount.
        """
        tax_rate: float = 0.18

        return amount * tax_rate

    price: float = 1000.0
    tax: float = calculate_tax(price)
    total: float = price + tax

    return total


invoice_total: float = calculate_invoice()

print(invoice_total)


# =============================================================================
# 11. Nested Function Can Access Outer Parameters
# =============================================================================


def create_multiplier(multiplier: float) -> float:
    """
    Demonstrate access to an outer function parameter.
    """

    def multiply(number: float) -> float:
        """
        Multiply using the enclosing multiplier.
        """
        return number * multiplier

    return multiply(10.0)


multiplied_value: float = create_multiplier(3.0)

print(multiplied_value)


# =============================================================================
# 12. Nested Function Can Access Outer Local Variables
# =============================================================================


def create_user_message() -> str:
    """
    Demonstrate access to an outer local variable.
    """
    username: str = "Alex"
    role: str = "Developer"

    def build_message() -> str:
        """
        Access variables from the enclosing function.
        """
        return f"{username} is a {role}."

    return build_message()


user_message: str = create_user_message()

print(user_message)


# =============================================================================
# 13. Nested Function Has Its Own Parameters
# =============================================================================


def create_report(title: str) -> str:
    """
    Create a report using a nested function.
    """

    def format_line(value: str) -> str:
        """
        Format a report line.
        """
        return f"{title}: {value}"

    first_line: str = format_line("Completed")
    second_line: str = format_line("Successful")

    return f"{first_line}\n{second_line}"


report: str = create_report("Data Pipeline")

print(report)


# =============================================================================
# 14. Outer and Inner Variables With Different Names
# =============================================================================


def demonstrate_different_variables() -> str:
    """
    Demonstrate independent variables in different scopes.
    """
    outer_value: int = 10

    def inner() -> str:
        """
        Use a local variable and an enclosing variable.
        """
        inner_value: int = 20

        return f"{outer_value}, {inner_value}"

    return inner()


different_variables_result: str = demonstrate_different_variables()

print(different_variables_result)


# =============================================================================
# 15. Same Variable Name in Outer and Inner Scope
# =============================================================================


def demonstrate_shadowing() -> str:
    """
    Demonstrate local shadowing inside a nested function.
    """
    message: str = "Outer message"

    def inner() -> str:
        """
        Shadow the enclosing message.
        """
        message: str = "Inner message"

        return message

    return f"Outer={message}; Inner={inner()}"


shadowing_result: str = demonstrate_shadowing()

print(shadowing_result)

# The inner message shadows the outer message inside inner().
#
# The outer variable remains unchanged.


# =============================================================================
# 16. Reading the Outer Variable Without Shadowing
# =============================================================================


def read_enclosing_variable() -> str:
    """
    Read an enclosing variable without creating a local variable.
    """
    message: str = "Enclosing message"

    def inner() -> str:
        """
        Read the enclosing message.
        """
        return message

    return inner()


enclosing_read_result: str = read_enclosing_variable()

print(enclosing_read_result)


# =============================================================================
# 17. Nested Function and LEGB
# =============================================================================


global_message: str = "Global message"


def demonstrate_legb() -> str:
    """
    Demonstrate LEGB lookup with a nested function.
    """
    enclosing_message: str = "Enclosing message"

    def inner() -> str:
        """
        Read the nearest available variable.
        """
        local_message: str = "Local message"

        return (
            f"{local_message}; "
            f"{enclosing_message}; "
            f"{global_message}"
        )

    return inner()


legb_result: str = demonstrate_legb()

print(legb_result)

# inner() has access to:
#
# Local:
#     local_message
#
# Enclosing:
#     enclosing_message
#
# Global:
#     global_message
#
# Built-in:
#     Python built-in names


# =============================================================================
# 18. Nested Function Cannot Access Caller Scope
# =============================================================================


def nested_scope_caller() -> str:
    """
    Demonstrate that caller-local variables are not enclosing variables.
    """
    caller_message: str = "Caller message"

    def nested() -> str:
        """
        Return a fixed message.
        """
        return "Nested message"

    nested_result: str = nested()

    return f"{caller_message}; {nested_result}"


caller_scope_result: str = nested_scope_caller()

print(caller_scope_result)

# A function called by another function does not automatically gain access
# to the caller's local variables.
#
# Only lexical nesting creates an enclosing scope.


# =============================================================================
# 19. Nested Functions Are Defined Where They Are Written
# =============================================================================


global_value: str = "Global"


def lexical_scope_example() -> str:
    """
    Demonstrate lexical scope.
    """
    local_value: str = "Outer"

    def inner() -> str:
        """
        Read the lexically enclosing variable.
        """
        return local_value

    return inner()


lexical_result: str = lexical_scope_example()

print(lexical_result)


# =============================================================================
# 20. Multiple Nested Functions
# =============================================================================


def create_messages() -> str:
    """
    Demonstrate multiple nested functions.
    """

    def first_message() -> str:
        """
        Return the first message.
        """
        return "First message"

    def second_message() -> str:
        """
        Return the second message.
        """
        return "Second message"

    first: str = first_message()
    second: str = second_message()

    return f"{first}; {second}"


multiple_functions_result: str = create_messages()

print(multiple_functions_result)


# =============================================================================
# 21. Nested Functions Calling Each Other
# =============================================================================


def calculate_with_helpers(value: int) -> int:
    """
    Demonstrate nested functions calling other nested functions.
    """

    def double(number: int) -> int:
        """
        Double a number.
        """
        return number * 2

    def add_ten(number: int) -> int:
        """
        Add ten to a number.
        """
        return number + 10

    doubled: int = double(value)
    result: int = add_ten(doubled)

    return result


helper_result: int = calculate_with_helpers(5)

print(helper_result)


# =============================================================================
# 22. Nested Function Calling Another Nested Function
# =============================================================================


def create_processor() -> str:
    """
    Demonstrate one nested function calling another.
    """

    def clean(value: str) -> str:
        """
        Clean a string.
        """
        return value.strip()

    def uppercase(value: str) -> str:
        """
        Convert a string to uppercase.
        """
        return clean(value).upper()

    return uppercase("  python  ")


processed_value: str = create_processor()

print(processed_value)


# =============================================================================
# 23. Nested Function As a Helper
# =============================================================================


def process_username(username: str) -> str:
    """
    Use a nested helper function to normalize a username.
    """

    def normalize(value: str) -> str:
        """
        Normalize a string.
        """
        return value.strip().lower()

    normalized_username: str = normalize(username)

    return normalized_username


processed_username: str = process_username("  SHREYAS  ")

print(processed_username)


# =============================================================================
# 24. Nested Validation Helper
# =============================================================================


def validate_age(age: int) -> str:
    """
    Validate an age using a nested helper function.
    """

    def is_valid(value: int) -> bool:
        """
        Return whether the age is valid.
        """
        return 0 <= value <= 120

    if is_valid(age):
        return "Valid age"

    return "Invalid age"


age_result: str = validate_age(30)

print(age_result)


# =============================================================================
# 25. Nested String Validation Helper
# =============================================================================


def validate_username(username: str) -> str:
    """
    Validate a username using nested helper functions.
    """

    def has_minimum_length(value: str) -> bool:
        """
        Check minimum username length.
        """
        return len(value) >= 3

    def contains_only_letters(value: str) -> bool:
        """
        Check whether the username contains only letters.
        """
        return value.isalpha()

    if not has_minimum_length(username):
        return "Username is too short"

    if not contains_only_letters(username):
        return "Username contains invalid characters"

    return "Username is valid"


username_validation: str = validate_username("Alex")

print(username_validation)


# =============================================================================
# 26. Nested Calculation Helper
# =============================================================================


def calculate_order_total(price: float, quantity: int) -> float:
    """
    Calculate an order total using a nested helper.
    """

    def calculate_subtotal() -> float:
        """
        Calculate the subtotal from enclosing variables.
        """
        return price * quantity

    return calculate_subtotal()


order_total: float = calculate_order_total(100.0, 3)

print(order_total)


# =============================================================================
# 27. Nested Tax Helper
# =============================================================================


def calculate_total_with_tax(price: float) -> float:
    """
    Calculate a total using a nested tax helper.
    """
    tax_rate: float = 0.18

    def calculate_tax() -> float:
        """
        Calculate tax using enclosing values.
        """
        return price * tax_rate

    tax: float = calculate_tax()

    return price + tax


total_with_tax: float = calculate_total_with_tax(1000.0)

print(total_with_tax)


# =============================================================================
# 28. Returning a Nested Function
# =============================================================================

from collections.abc import Callable


def create_greeter() -> Callable[[str], str]:
    """
    Return a nested function.
    """

    def greet(name: str) -> str:
        """
        Create a greeting.
        """
        return f"Hello, {name}!"

    return greet


greeter: Callable[[str], str] = create_greeter()

returned_greeting: str = greeter("Alex")

print(returned_greeting)

# The nested function is returned as a function object.
#
# It can then be called outside the outer function.


# =============================================================================
# 29. Function Factory
# =============================================================================


def create_multiplier_function(
    multiplier: float,
) -> Callable[[float], float]:
    """
    Create a multiplier function.
    """

    def multiply(number: float) -> float:
        """
        Multiply using the enclosing multiplier.
        """
        return number * multiplier

    return multiply


double: Callable[[float], float] = create_multiplier_function(2.0)
triple: Callable[[float], float] = create_multiplier_function(3.0)

double_result: float = double(10.0)
triple_result: float = triple(10.0)

print(double_result)
print(triple_result)


# =============================================================================
# 30. Function Factory With Addition
# =============================================================================


def create_adder(
    amount: int,
) -> Callable[[int], int]:
    """
    Create a function that adds a fixed amount.
    """

    def add(value: int) -> int:
        """
        Add the enclosing amount.
        """
        return value + amount

    return add


add_five: Callable[[int], int] = create_adder(5)
add_ten: Callable[[int], int] = create_adder(10)

print(add_five(100))
print(add_ten(100))


# =============================================================================
# 31. Function Factory With Strings
# =============================================================================


def create_prefixer(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a function that adds a prefix.
    """

    def add_prefix(value: str) -> str:
        """
        Add the enclosing prefix.
        """
        return f"{prefix}{value}"

    return add_prefix


error_prefixer: Callable[[str], str] = create_prefixer("ERROR: ")
info_prefixer: Callable[[str], str] = create_prefixer("INFO: ")

print(error_prefixer("File not found"))
print(info_prefixer("Process completed"))


# =============================================================================
# 32. Closure
# =============================================================================
"""
A closure is a nested function that remembers variables from its enclosing
scope.

Example:

    def create_multiplier(
        multiplier: float,
    ) -> Callable[[float], float]:

        def multiply(
            number: float,
        ) -> float:
            return number * multiplier

        return multiply

The returned function remembers multiplier.

For:

    double = create_multiplier(2.0)

double remembers:

    multiplier = 2.0

For:

    triple = create_multiplier(3.0)

triple remembers:

    multiplier = 3.0

This behaviour is called a closure.
"""


# =============================================================================
# 33. Basic Closure
# =============================================================================


def create_multiplier_closure(
    multiplier: float,
) -> Callable[[float], float]:
    """
    Create a closure around multiplier.
    """

    def multiply(number: float) -> float:
        """
        Multiply using the captured multiplier.
        """
        return number * multiplier

    return multiply


double_closure: Callable[[float], float] = create_multiplier_closure(2.0)
triple_closure: Callable[[float], float] = create_multiplier_closure(3.0)

print(double_closure(10.0))
print(triple_closure(10.0))


# =============================================================================
# 34. Independent Closures
# =============================================================================


def create_counter(
    start: int,
) -> Callable[[], int]:
    """
    Create an independent counter closure.
    """
    count: int = start

    def increment() -> int:
        """
        Increment the enclosing counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


counter_one: Callable[[], int] = create_counter(0)
counter_two: Callable[[], int] = create_counter(100)

print(counter_one())
print(counter_one())
print(counter_two())
print(counter_two())


# counter_one and counter_two have separate enclosing scopes.
#
# counter_one remembers its own count.
#
# counter_two remembers a different count.


# =============================================================================
# 35. nonlocal With Nested Functions
# =============================================================================


def create_sequence() -> Callable[[], int]:
    """
    Create a sequence generator using nonlocal.
    """
    current_value: int = 0

    def next_value() -> int:
        """
        Modify the enclosing current_value.
        """
        nonlocal current_value

        current_value += 1

        return current_value

    return next_value


sequence: Callable[[], int] = create_sequence()

sequence_value_one: int = sequence()
sequence_value_two: int = sequence()
sequence_value_three: int = sequence()

print(sequence_value_one)
print(sequence_value_two)
print(sequence_value_three)


# =============================================================================
# 36. nonlocal Is Required For Rebinding
# =============================================================================


def create_score_updater() -> Callable[[int], int]:
    """
    Create a function that updates enclosing score.
    """
    score: int = 0

    def add_score(points: int) -> int:
        """
        Update the enclosing score.
        """
        nonlocal score

        score += points

        return score

    return add_score


score_updater: Callable[[int], int] = create_score_updater()

print(score_updater(10))
print(score_updater(20))
print(score_updater(30))


# =============================================================================
# 37. Reading Enclosing Variables Does Not Need nonlocal
# =============================================================================


def create_reader() -> Callable[[], str]:
    """
    Create a function that reads an enclosing variable.
    """
    message: str = "Stored message"

    def read() -> str:
        """
        Read the enclosing message.
        """
        return message

    return read


reader: Callable[[], str] = create_reader()

print(reader())


# =============================================================================
# 38. nonlocal Changes the Enclosing Variable
# =============================================================================


def create_status_manager() -> Callable[[str], str]:
    """
    Create a status manager.
    """
    status: str = "pending"

    def update_status(new_status: str) -> str:
        """
        Update the enclosing status.
        """
        nonlocal status

        status = new_status

        return status

    return update_status


status_manager: Callable[[str], str] = create_status_manager()

print(status_manager("processing"))
print(status_manager("completed"))


# =============================================================================
# 39. Closure Captures Configuration
# =============================================================================


def create_formatter(
    prefix: str,
    suffix: str,
) -> Callable[[str], str]:
    """
    Create a configurable formatter.
    """

    def format_value(value: str) -> str:
        """
        Format using captured prefix and suffix.
        """
        return f"{prefix}{value}{suffix}"

    return format_value


html_formatter: Callable[[str], str] = create_formatter("<b>", "</b>")
bracket_formatter: Callable[[str], str] = create_formatter("[", "]")

print(html_formatter("Python"))
print(bracket_formatter("Python"))


# =============================================================================
# 40. Closure Capturing Multiple Variables
# =============================================================================


def create_range_checker(
    minimum: int,
    maximum: int,
) -> Callable[[int], bool]:
    """
    Create a function that remembers a minimum and maximum.
    """

    def is_in_range(value: int) -> bool:
        """
        Check the value against captured bounds.
        """
        return minimum <= value <= maximum

    return is_in_range


age_checker: Callable[[int], bool] = create_range_checker(18, 60)

print(age_checker(25))
print(age_checker(70))


# =============================================================================
# 41. Nested Function With Mutable Enclosing State
# =============================================================================


def create_item_manager() -> Callable[[str], list[str]]:
    """
    Create a manager that remembers a mutable list.
    """
    items: list[str] = []

    def add_item(item: str) -> list[str]:
        """
        Mutate the enclosing list.
        """
        items.append(item)

        return items.copy()

    return add_item


item_manager: Callable[[str], list[str]] = create_item_manager()

print(item_manager("Python"))
print(item_manager("SQL"))
print(item_manager("Go"))


# No nonlocal statement is required here.
#
# The list object is being mutated.
#
# The name items itself is not being rebound.


# =============================================================================
# 42. Mutable State Versus Rebinding
# =============================================================================


def create_list_manager() -> Callable[[str], list[str]]:
    """
    Demonstrate mutation of an enclosing list.
    """
    values: list[str] = []

    def add_value(value: str) -> list[str]:
        """
        Mutate the enclosing list.
        """
        values.append(value)

        return values.copy()

    return add_value


list_manager: Callable[[str], list[str]] = create_list_manager()

print(list_manager("Python"))
print(list_manager("Java"))


# =============================================================================
# 43. Rebinding an Enclosing List
# =============================================================================


def create_replacing_manager() -> Callable[[str], list[str]]:
    """
    Demonstrate rebinding an enclosing variable.
    """
    values: list[str] = []

    def replace_value(value: str) -> list[str]:
        """
        Replace the enclosing list.
        """
        nonlocal values

        values = [value]

        return values.copy()

    return replace_value


replacing_manager: Callable[[str], list[str]] = (
    create_replacing_manager()
)

print(replacing_manager("Python"))
print(replacing_manager("SQL"))


# =============================================================================
# 44. Nested Functions With Multiple Helpers
# =============================================================================


def process_product(
    product_name: str,
    price: float,
) -> str:
    """
    Process a product using multiple nested helpers.
    """

    def normalize_name(value: str) -> str:
        """
        Normalize the product name.
        """
        return value.strip().title()

    def format_price(value: float) -> str:
        """
        Format the product price.
        """
        return f"${value:.2f}"

    normalized_name: str = normalize_name(product_name)
    formatted_price: str = format_price(price)

    return f"{normalized_name}: {formatted_price}"


product_result: str = process_product("  python book  ", 49.99)

print(product_result)


# =============================================================================
# 45. Nested Validation Functions
# =============================================================================


def validate_product(
    name: str,
    price: float,
) -> bool:
    """
    Validate a product using nested helpers.
    """

    def valid_name(value: str) -> bool:
        """
        Validate the product name.
        """
        return bool(value.strip())

    def valid_price(value: float) -> bool:
        """
        Validate the product price.
        """
        return value > 0.0

    return valid_name(name) and valid_price(price)


product_is_valid: bool = validate_product("Python", 100.0)

print(product_is_valid)


# =============================================================================
# 46. Nested Functions For Private Implementation Details
# =============================================================================


def generate_report(total: float) -> str:
    """
    Generate a report using a private local helper.
    """

    def format_currency(value: float) -> str:
        """
        Format currency internally.
        """
        return f"${value:.2f}"

    formatted_total: str = format_currency(total)

    return f"Total: {formatted_total}"


report_result: str = generate_report(1250.50)

print(report_result)


# format_currency() is only needed by generate_report().
#
# Keeping it nested prevents it from becoming part of the module-level
# public namespace.


# =============================================================================
# 47. Nested Function For Normalization
# =============================================================================


def normalize_user_data(
    name: str,
    email: str,
) -> tuple[str, str]:
    """
    Normalize user data using a local helper.
    """

    def normalize(value: str) -> str:
        """
        Normalize one string value.
        """
        return value.strip().lower()

    normalized_name: str = normalize(name)
    normalized_email: str = normalize(email)

    return normalized_name, normalized_email


normalized_name, normalized_email = normalize_user_data(
    "  Alex  ",
    "  ALEX@EXAMPLE.COM  ",
)

print(normalized_name)
print(normalized_email)


# =============================================================================
# 48. Nested Function Returning Multiple Values
# =============================================================================


def calculate_dimensions(
    width: float,
    height: float,
) -> tuple[float, float]:
    """
    Calculate area and perimeter using a nested helper.
    """

    def calculate_area() -> float:
        """
        Calculate the area.
        """
        return width * height

    def calculate_perimeter() -> float:
        """
        Calculate the perimeter.
        """
        return 2.0 * (width + height)

    area: float = calculate_area()
    perimeter: float = calculate_perimeter()

    return area, perimeter


area_result, perimeter_result = calculate_dimensions(10.0, 5.0)

print(area_result)
print(perimeter_result)


# =============================================================================
# 49. Nested Function Returning a Boolean
# =============================================================================


def is_valid_number(value: int) -> bool:
    """
    Validate a number using a nested helper.
    """

    def is_positive(number: int) -> bool:
        """
        Check whether a number is positive.
        """
        return number > 0

    return is_positive(value)


positive_result: bool = is_valid_number(10)

print(positive_result)


# =============================================================================
# 50. Nested Function Returning a String
# =============================================================================


def create_status_message(status: str) -> str:
    """
    Create a formatted status message.
    """

    def format_status(value: str) -> str:
        """
        Format the status.
        """
        return value.strip().upper()

    formatted_status: str = format_status(status)

    return f"STATUS: {formatted_status}"


status_message: str = create_status_message(" completed ")

print(status_message)


# =============================================================================
# 51. Nested Function Receiving Outer Data
# =============================================================================


def calculate_discount(
    price: float,
    percentage: float,
) -> float:
    """
    Calculate a discount using an inner helper.
    """

    def calculate_amount() -> float:
        """
        Calculate the discount amount.
        """
        return price * percentage / 100.0

    discount_amount: float = calculate_amount()

    return discount_amount


discount: float = calculate_discount(1000.0, 10.0)

print(discount)


# =============================================================================
# 52. Nested Function With No Parameters
# =============================================================================


def create_constant_message() -> str:
    """
    Demonstrate a nested function without parameters.
    """
    message: str = "Hello from the outer function."

    def get_message() -> str:
        """
        Return the enclosing message.
        """
        return message

    return get_message()


constant_message: str = create_constant_message()

print(constant_message)


# =============================================================================
# 53. Nested Function With Parameters
# =============================================================================


def create_calculator() -> int:
    """
    Demonstrate a nested function with parameters.
    """

    def calculate(first: int, second: int) -> int:
        """
        Add two numbers.
        """
        return first + second

    return calculate(10, 20)


calculator_result: int = create_calculator()

print(calculator_result)


# =============================================================================
# 54. Nested Function Can Use Global Variables
# =============================================================================


DEFAULT_TAX_RATE: float = 0.18


def calculate_global_tax(price: float) -> float:
    """
    Use a global constant from a nested function.
    """

    def calculate() -> float:
        """
        Read the global tax rate.
        """
        return price * DEFAULT_TAX_RATE

    return calculate()


global_tax: float = calculate_global_tax(1000.0)

print(global_tax)


# =============================================================================
# 55. Nested Function With global
# =============================================================================
"""
A nested function can also use the global statement.

The global statement refers to module-level scope.

Example:

    counter: int = 0

    def outer() -> None:
        def inner() -> None:
            global counter
            counter += 1

The global statement does not refer to the outer function's local scope.

For an outer-function variable, use nonlocal instead.
"""


nested_global_counter: int = 0


def increment_nested_global() -> int:
    """
    Modify a module-level variable from a nested function.
    """

    def increment() -> int:
        """
        Modify the global counter.
        """
        global nested_global_counter

        nested_global_counter += 1

        return nested_global_counter

    return increment()


print(increment_nested_global())
print(increment_nested_global())


# =============================================================================
# 56. Nested Function With nonlocal
# =============================================================================


def increment_nested_value() -> int:
    """
    Demonstrate nonlocal inside a nested function.
    """
    value: int = 0

    def increment() -> int:
        """
        Modify the enclosing value.
        """
        nonlocal value

        value += 1

        return value

    return increment()


nested_value_result: int = increment_nested_value()

print(nested_value_result)


# =============================================================================
# 57. Returning a Closure With State
# =============================================================================


def create_running_total() -> Callable[[int], int]:
    """
    Create a function that maintains a running total.
    """
    total: int = 0

    def add(value: int) -> int:
        """
        Add a value to the running total.
        """
        nonlocal total

        total += value

        return total

    return add


running_total: Callable[[int], int] = create_running_total()

print(running_total(10))
print(running_total(20))
print(running_total(30))


# =============================================================================
# 58. Independent Running Totals
# =============================================================================


def create_total() -> Callable[[int], int]:
    """
    Create an independent total function.
    """
    total: int = 0

    def add(value: int) -> int:
        """
        Update the enclosing total.
        """
        nonlocal total

        total += value

        return total

    return add


sales_total: Callable[[int], int] = create_total()
expense_total: Callable[[int], int] = create_total()

print(sales_total(100))
print(sales_total(200))

print(expense_total(50))
print(expense_total(75))


# Each returned function has its own enclosing state.


# =============================================================================
# 59. Nested Function Factory For Comparisons
# =============================================================================


def create_threshold_checker(
    threshold: float,
) -> Callable[[float], bool]:
    """
    Create a threshold-checking function.
    """

    def is_above(value: float) -> bool:
        """
        Check whether value is above the threshold.
        """
        return value > threshold

    return is_above


high_score_checker: Callable[[float], bool] = (
    create_threshold_checker(80.0)
)

print(high_score_checker(90.0))
print(high_score_checker(70.0))


# =============================================================================
# 60. Nested Function Factory For Validation
# =============================================================================


def create_length_validator(
    minimum_length: int,
) -> Callable[[str], bool]:
    """
    Create a string-length validator.
    """

    def is_valid(value: str) -> bool:
        """
        Validate string length.
        """
        return len(value) >= minimum_length

    return is_valid


password_validator: Callable[[str], bool] = (
    create_length_validator(8)
)

print(password_validator("password"))
print(password_validator("abc"))


# =============================================================================
# 61. Nested Functions And Callbacks
# =============================================================================


def process_values(
    values: list[int],
) -> list[int]:
    """
    Process values using a nested callback function.
    """

    def double(value: int) -> int:
        """
        Double one value.
        """
        return value * 2

    return [double(value) for value in values]


processed_values: list[int] = process_values(
    [1, 2, 3, 4],
)

print(processed_values)


# =============================================================================
# 62. Nested Function Used With map
# =============================================================================


def double_values(
    values: list[int],
) -> list[int]:
    """
    Use a nested function with map.
    """

    def double(value: int) -> int:
        """
        Double a number.
        """
        return value * 2

    return list(map(double, values))


doubled_values: list[int] = double_values(
    [1, 2, 3, 4],
)

print(doubled_values)


# =============================================================================
# 63. Nested Function Used With filter
# =============================================================================


def filter_positive_values(
    values: list[int],
) -> list[int]:
    """
    Use a nested predicate function with filter.
    """

    def is_positive(value: int) -> bool:
        """
        Check whether a value is positive.
        """
        return value > 0

    return list(filter(is_positive, values))


positive_values: list[int] = filter_positive_values(
    [-3, -1, 0, 2, 5],
)

print(positive_values)


# =============================================================================
# 64. Nested Function Used With sorted
# =============================================================================


def sort_words_by_length(
    words: list[str],
) -> list[str]:
    """
    Sort words using a nested key function.
    """

    def get_length(value: str) -> int:
        """
        Return the length of a word.
        """
        return len(value)

    return sorted(words, key=get_length)


sorted_words: list[str] = sort_words_by_length(
    ["Python", "Go", "Java", "SQL"],
)

print(sorted_words)


# =============================================================================
# 65. Nested Function With a List Comprehension
# =============================================================================


def create_squares(
    values: list[int],
) -> list[int]:
    """
    Create squares using a nested helper.
    """

    def square(value: int) -> int:
        """
        Return the square of a value.
        """
        return value**2

    return [square(value) for value in values]


squares: list[int] = create_squares(
    [1, 2, 3, 4],
)

print(squares)


# =============================================================================
# 66. Nested Function Inside a Loop
# =============================================================================


def create_messages_for_names(
    names: list[str],
) -> list[str]:
    """
    Use a nested function inside a loop.
    """

    def create_message(name: str) -> str:
        """
        Create a message for one name.
        """
        return f"Hello, {name}!"

    messages: list[str] = []

    for name in names:
        messages.append(create_message(name))

    return messages


messages_for_names: list[str] = create_messages_for_names(
    ["Alex", "Sam", "John"],
)

print(messages_for_names)


# =============================================================================
# 67. Nested Function And Default Arguments
# =============================================================================


def create_default_message(
    prefix: str,
) -> str:
    """
    Demonstrate a nested function with a default argument.
    """

    def build_message(
        value: str = "Default message",
    ) -> str:
        """
        Build a message using the enclosing prefix.
        """
        return f"{prefix}: {value}"

    return build_message()


default_nested_message: str = create_default_message("INFO")

print(default_nested_message)


# =============================================================================
# 68. Nested Function And Type Annotations
# =============================================================================


def calculate_area_with_helper(
    width: float,
    height: float,
) -> float:
    """
    Demonstrate type annotations on nested functions.
    """

    def multiply(
        first: float,
        second: float,
    ) -> float:
        """
        Multiply two numbers.
        """
        return first * second

    return multiply(width, height)


typed_area: float = calculate_area_with_helper(
    10.0,
    5.0,
)

print(typed_area)


# =============================================================================
# 69. Nested Function Returning Callable
# =============================================================================


def create_operation(
    operation: str,
) -> Callable[[int, int], int]:
    """
    Create a mathematical operation.
    """

    def calculate(
        first: int,
        second: int,
    ) -> int:
        """
        Perform the selected operation.
        """
        if operation == "add":
            return first + second

        if operation == "subtract":
            return first - second

        if operation == "multiply":
            return first * second

        if operation == "divide":
            if second == 0:
                raise ValueError("Cannot divide by zero.")

            return first // second

        raise ValueError(f"Unsupported operation: {operation}")

    return calculate


add_operation: Callable[[int, int], int] = create_operation("add")
multiply_operation: Callable[[int, int], int] = (
    create_operation("multiply")
)

print(add_operation(10, 5))
print(multiply_operation(10, 5))


# =============================================================================
# 70. Nested Function As a Private Helper
# =============================================================================


def prepare_email(
    recipient: str,
    subject: str,
) -> str:
    """
    Prepare an email using private local helpers.
    """

    def normalize_recipient(value: str) -> str:
        """
        Normalize the recipient.
        """
        return value.strip().lower()

    def normalize_subject(value: str) -> str:
        """
        Normalize the subject.
        """
        return value.strip()

    clean_recipient: str = normalize_recipient(recipient)
    clean_subject: str = normalize_subject(subject)

    return f"To: {clean_recipient}\nSubject: {clean_subject}"


email_result: str = prepare_email(
    "  user@example.com  ",
    "  Python Update  ",
)

print(email_result)


# =============================================================================
# 71. Nested Function For Reusable Local Logic
# =============================================================================


def process_prices(
    prices: list[float],
) -> list[float]:
    """
    Apply a local price transformation.
    """

    def apply_tax(price: float) -> float:
        """
        Apply an 18 percent tax.
        """
        return price * 1.18

    return [apply_tax(price) for price in prices]


processed_prices: list[float] = process_prices(
    [100.0, 200.0, 300.0],
)

print(processed_prices)


# =============================================================================
# 72. Nested Functions And Data Validation
# =============================================================================


def validate_order(
    quantity: int,
    price: float,
) -> str:
    """
    Validate an order using local validation helpers.
    """

    def valid_quantity(value: int) -> bool:
        """
        Check the quantity.
        """
        return value > 0

    def valid_price(value: float) -> bool:
        """
        Check the price.
        """
        return value > 0.0

    if not valid_quantity(quantity):
        return "Invalid quantity"

    if not valid_price(price):
        return "Invalid price"

    return "Order is valid"


order_validation: str = validate_order(2, 100.0)

print(order_validation)


# =============================================================================
# 73. Multiple Levels of Nested Functions
# =============================================================================


def level_one() -> str:
    """
    Demonstrate three levels of nested functions.
    """
    value_one: str = "Level One"

    def level_two() -> str:
        """
        Define the second level.
        """
        value_two: str = "Level Two"

        def level_three() -> str:
            """
            Access both enclosing values.
            """
            return f"{value_one}; {value_two}"

        return level_three()

    return level_two()


multiple_level_result: str = level_one()

print(multiple_level_result)


# =============================================================================
# 74. Three Levels With LEGB
# =============================================================================


nested_global_value: str = "Global"


def first_level() -> str:
    """
    Create the first enclosing scope.
    """
    first_value: str = "First"

    def second_level() -> str:
        """
        Create the second enclosing scope.
        """
        second_value: str = "Second"

        def third_level() -> str:
            """
            Access multiple enclosing levels and global scope.
            """
            return (
                f"{first_value}; "
                f"{second_value}; "
                f"{nested_global_value}"
            )

        return third_level()

    return second_level()


three_level_result: str = first_level()

print(three_level_result)


# =============================================================================
# 75. Nearest Enclosing Scope Wins
# =============================================================================


def demonstrate_nearest_scope() -> str:
    """
    Demonstrate nearest enclosing scope resolution.
    """
    

    value: str = "Outer"

    def middle() -> str:
        """
        Create another enclosing variable.
        """
        value: str = "Middle"

        def inner() -> str:
            """
            Read the nearest enclosing value.
            """
            return value

        return inner()

    return middle()


nearest_scope_result: str = demonstrate_nearest_scope()

print(nearest_scope_result)

# inner() finds:
#
# Local:
#     value not found
#
# Enclosing:
#     middle() has value = "Middle"
#
# Therefore "Middle" is returned.


# =============================================================================
# 76. nonlocal Uses the Nearest Enclosing Scope
# =============================================================================


def demonstrate_nearest_nonlocal() -> str:
    """
    Demonstrate nearest enclosing scope with nonlocal.
    """
    value: str = "Outer"

    def middle() -> str:
        """
        Create another value.
        """
        value: str = "Middle"

        def inner() -> str:
            """
            Modify the nearest enclosing value.
            """
            nonlocal value

            value = "Changed"

            return value

        return inner()

    return middle()


nearest_nonlocal_result: str = demonstrate_nearest_nonlocal()

print(nearest_nonlocal_result)


# =============================================================================
# 77. Closure Captures Function Parameters
# =============================================================================


def create_greeting_function(
    greeting: str,
) -> Callable[[str], str]:
    """
    Create a greeting function using a captured parameter.
    """

    def greet(name: str) -> str:
        """
        Use the captured greeting.
        """
        return f"{greeting}, {name}!"

    return greet


hello: Callable[[str], str] = create_greeting_function("Hello")
welcome: Callable[[str], str] = create_greeting_function("Welcome")

print(hello("Alex"))
print(welcome("Alex"))


# =============================================================================
# 78. Closure Captures Multiple Parameters
# =============================================================================


def create_formatter_function(
    prefix: str,
    suffix: str,
) -> Callable[[str], str]:
    """
    Capture multiple outer parameters.
    """

    def format_value(value: str) -> str:
        """
        Use both captured parameters.
        """
        return f"{prefix}{value}{suffix}"

    return format_value


quote_formatter: Callable[[str], str] = (
    create_formatter_function('"', '"')
)

tag_formatter: Callable[[str], str] = (
    create_formatter_function("<p>", "</p>")
)

print(quote_formatter("Python"))
print(tag_formatter("Python"))


# =============================================================================
# 79. Closure With a Configuration Object
# =============================================================================


def create_price_calculator(
    tax_rate: float,
) -> Callable[[float], float]:
    """
    Create a price calculator that remembers tax_rate.
    """

    def calculate(price: float) -> float:
        """
        Calculate the final price.
        """
        tax: float = price * tax_rate

        return price + tax

    return calculate


india_tax_calculator: Callable[[float], float] = (
    create_price_calculator(0.18)
)

print(india_tax_calculator(1000.0))


# =============================================================================
# 80. Closure With Mutable State
# =============================================================================


def create_history() -> Callable[[str], list[str]]:
    """
    Create a function that remembers history.
    """
    history: list[str] = []

    def add_entry(entry: str) -> list[str]:
        """
        Add an entry to the history.
        """
        history.append(entry)

        return history.copy()

    return add_entry


history: Callable[[str], list[str]] = create_history()

print(history("Started"))
print(history("Processing"))
print(history("Completed"))


# =============================================================================
# 81. Closure State Is Independent
# =============================================================================


history_one: Callable[[str], list[str]] = create_history()
history_two: Callable[[str], list[str]] = create_history()

print(history_one("One"))
print(history_one("Two"))

print(history_two("A"))
print(history_two("B"))


# history_one and history_two do not share the same enclosing list.


# =============================================================================
# 82. Nested Function Returning Another Nested Function
# =============================================================================


def create_nested_factory() -> Callable[[int], Callable[[int], int]]:
    """
    Demonstrate multiple nested function levels.
    """

    def create_adder(
        amount: int,
    ) -> Callable[[int], int]:
        """
        Create an adder function.
        """

        def add(value: int) -> int:
            """
            Add the captured amount.
            """
            return value + amount

        return add

    return create_adder


adder_factory: Callable[[int], Callable[[int], int]] = (
    create_nested_factory()
)

add_ten_nested: Callable[[int], int] = adder_factory(10)

print(add_ten_nested(50))


# =============================================================================
# 83. Nested Functions And Function Annotations
# =============================================================================


def create_typed_operation(
    multiplier: float,
) -> Callable[[float], float]:
    """
    Create a typed nested operation.
    """

    def multiply(
        value: float,
    ) -> float:
        """
        Multiply using the enclosing multiplier.
        """
        return value * multiplier

    return multiply


typed_multiplier: Callable[[float], float] = (
    create_typed_operation(4.0)
)

typed_multiplier_result: float = typed_multiplier(5.0)

print(typed_multiplier_result)


# =============================================================================
# 84. Nested Function With Optional Value
# =============================================================================


def format_optional_name(
    name: str | None,
) -> str:
    """
    Format an optional name using a nested helper.
    """

    def format_name(value: str) -> str:
        """
        Format a known string.
        """
        return value.strip().title()

    if name is None:
        return "Unknown"

    return format_name(name)


print(format_optional_name(" alex "))
print(format_optional_name(None))


# =============================================================================
# 85. Nested Function With Exception Handling
# =============================================================================


def safe_integer_conversion(
    value: str,
) -> int:
    """
    Convert a string to an integer using a nested helper.
    """

    def convert() -> int:
        """
        Perform the conversion.
        """
        return int(value)

    try:
        return convert()
    except ValueError:
        return 0


print(safe_integer_conversion("100"))
print(safe_integer_conversion("invalid"))


# =============================================================================
# 86. Nested Function With Resource-Like Processing
# =============================================================================


def process_text(
    text: str,
) -> str:
    """
    Process text using local helper functions.
    """

    def clean(value: str) -> str:
        """
        Clean whitespace.
        """
        return value.strip()

    def uppercase(value: str) -> str:
        """
        Convert text to uppercase.
        """
        return value.upper()

    cleaned_text: str = clean(text)
    processed_text: str = uppercase(cleaned_text)

    return processed_text


text_result: str = process_text("  hello python  ")

print(text_result)


# =============================================================================
# 87. Nested Function For Pipeline Processing
# =============================================================================


def process_pipeline(
    value: str,
) -> str:
    """
    Process a value through nested helper functions.
    """

    def strip_value(data: str) -> str:
        """
        Remove surrounding whitespace.
        """
        return data.strip()

    def lower_value(data: str) -> str:
        """
        Convert to lowercase.
        """
        return data.lower()

    def replace_spaces(data: str) -> str:
        """
        Replace spaces with underscores.
        """
        return data.replace(" ", "_")

    result: str = strip_value(value)
    result = lower_value(result)
    result = replace_spaces(result)

    return result


pipeline_result: str = process_pipeline(
    "  Python Nested Functions  ",
)

print(pipeline_result)


# =============================================================================
# 88. Nested Function For Logging
# =============================================================================


def process_task(
    task_name: str,
) -> str:
    """
    Process a task using a local logging helper.
    """

    def log(message: str) -> str:
        """
        Format a local log message.
        """
        return f"[{task_name}] {message}"

    started_message: str = log("Started")
    completed_message: str = log("Completed")

    return f"{started_message}\n{completed_message}"


task_result: str = process_task("Data Import")

print(task_result)


# =============================================================================
# 89. Nested Function For Formatting
# =============================================================================


def format_user(
    name: str,
    age: int,
) -> str:
    """
    Format user information with a nested helper.
    """

    def format_field(
        label: str,
        value: str,
    ) -> str:
        """
        Format one field.
        """
        return f"{label}: {value}"

    name_field: str = format_field("Name", name)
    age_field: str = format_field("Age", str(age))

    return f"{name_field}\n{age_field}"


formatted_user: str = format_user("Alex", 30)

print(formatted_user)


# =============================================================================
# 90. Nested Function For Data Transformation
# =============================================================================


def transform_numbers(
    values: list[int],
) -> list[int]:
    """
    Transform numbers using a nested helper.
    """

    def transform(value: int) -> int:
        """
        Apply a transformation.
        """
        return value**2 + 1

    return [transform(value) for value in values]


transformed_numbers: list[int] = transform_numbers(
    [1, 2, 3, 4],
)

print(transformed_numbers)


# =============================================================================
# 91. Nested Function For Searching
# =============================================================================


def find_first_positive(
    values: list[int],
) -> int | None:
    """
    Find the first positive number using a nested predicate.
    """

    def is_positive(value: int) -> bool:
        """
        Check whether a value is positive.
        """
        return value > 0

    for value in values:
        if is_positive(value):
            return value

    return None


first_positive: int | None = find_first_positive(
    [-5, -2, 0, 7, 10],
)

print(first_positive)


# =============================================================================
# 92. Nested Function For Searching Strings
# =============================================================================


def find_matching_name(
    names: list[str],
    target: str,
) -> str | None:
    """
    Search for a matching name.
    """

    def matches(value: str) -> bool:
        """
        Compare a name case-insensitively.
        """
        return value.lower() == target.lower()

    for name in names:
        if matches(name):
            return name

    return None


matching_name: str | None = find_matching_name(
    ["Alex", "Sam", "John"],
    "sam",
)

print(matching_name)


# =============================================================================
# 93. Nested Function For Aggregation
# =============================================================================


def calculate_total_values(
    values: list[float],
) -> float:
    """
    Calculate a total using a nested helper.
    """

    def normalize(value: float) -> float:
        """
        Normalize one value.
        """
        return round(value, 2)

    total: float = 0.0

    for value in values:
        total += normalize(value)

    return total


total_values: float = calculate_total_values(
    [10.123, 20.456, 30.789],
)

print(total_values)


# =============================================================================
# 94. Nested Function And Recursion
# =============================================================================


def factorial(
    number: int,
) -> int:
    """
    Calculate factorial using a nested recursive helper.
    """

    def calculate(value: int) -> int:
        """
        Recursively calculate factorial.
        """
        if value <= 1:
            return 1

        return value * calculate(value - 1)

    if number < 0:
        raise ValueError("Factorial requires a non-negative integer.")

    return calculate(number)


factorial_result: int = factorial(5)

print(factorial_result)


# =============================================================================
# 95. Nested Function And Recursion With Closure
# =============================================================================


def create_counter_until(
    limit: int,
) -> Callable[[], int]:
    """
    Create a counter closure with a limit.
    """
    current: int = 0

    def next_value() -> int:
        """
        Increment the counter until the limit.
        """
        nonlocal current

        if current >= limit:
            return current

        current += 1

        return current

    return next_value


limited_counter: Callable[[], int] = create_counter_until(3)

print(limited_counter())
print(limited_counter())
print(limited_counter())
print(limited_counter())
print(limited_counter())


# =============================================================================
# 96. Nested Function As a Strategy
# =============================================================================


def calculate_using_strategy(
    first: int,
    second: int,
    strategy: str,
) -> int:
    """
    Select a local strategy for calculation.
    """

    def add() -> int:
        """
        Add the values.
        """
        return first + second

    def subtract() -> int:
        """
        Subtract the values.
        """
        return first - second

    if strategy == "add":
        return add()

    if strategy == "subtract":
        return subtract()

    raise ValueError(f"Unsupported strategy: {strategy}")


strategy_add_result: int = calculate_using_strategy(
    10,
    5,
    "add",
)

strategy_subtract_result: int = calculate_using_strategy(
    10,
    5,
    "subtract",
)

print(strategy_add_result)
print(strategy_subtract_result)


# =============================================================================
# 97. Nested Function For Configuration
# =============================================================================


def create_api_client(
    base_url: str,
) -> Callable[[str], str]:
    """
    Create a simple API URL builder.
    """

    def build_url(endpoint: str) -> str:
        """
        Build a URL using the captured base URL.
        """
        clean_base_url: str = base_url.rstrip("/")
        clean_endpoint: str = endpoint.lstrip("/")

        return f"{clean_base_url}/{clean_endpoint}"

    return build_url


api_client: Callable[[str], str] = create_api_client(
    "https://example.com/api",
)

print(api_client("/users"))


# =============================================================================
# 98. Nested Function For File Naming
# =============================================================================


def create_file_namer(
    extension: str,
) -> Callable[[str], str]:
    """
    Create a file-name generator.
    """

    def create_name(base_name: str) -> str:
        """
        Create a file name using the captured extension.
        """
        clean_extension: str = extension.lstrip(".")

        return f"{base_name}.{clean_extension}"

    return create_name


python_file: Callable[[str], str] = create_file_namer("py")
json_file: Callable[[str], str] = create_file_namer(".json")

print(python_file("main"))
print(json_file("config"))


# =============================================================================
# 99. Nested Function For ID Generation
# =============================================================================


def create_id_generator(
    prefix: str,
) -> Callable[[], str]:
    """
    Create an ID generator with enclosing state.
    """
    counter: int = 0

    def generate_id() -> str:
        """
        Generate the next ID.
        """
        nonlocal counter

        counter += 1

        return f"{prefix}-{counter}"

    return generate_id


user_id_generator: Callable[[], str] = create_id_generator("USER")

print(user_id_generator())
print(user_id_generator())
print(user_id_generator())


# =============================================================================
# 100. Nested Function For Event Generation
# =============================================================================


def create_event_generator(
    event_type: str,
) -> Callable[[str], str]:
    """
    Create an event generator.
    """

    def create_event(message: str) -> str:
        """
        Create an event string.
        """
        return f"{event_type}: {message}"

    return create_event


info_event: Callable[[str], str] = create_event_generator("INFO")
error_event: Callable[[str], str] = create_event_generator("ERROR")

print(info_event("Application started"))
print(error_event("Application failed"))


# =============================================================================
# 101. Nested Function And Decorator-Like Structure
# =============================================================================
"""
Decorators make heavy use of nested functions.

A simplified decorator-like structure is:

    def decorator(function):
        def wrapper():
            ...
            function()
            ...
        return wrapper

The wrapper function is nested inside decorator().

The wrapper can access the enclosing function parameter:

    function

This is another example of a closure.
"""


# =============================================================================
# 102. Simple Decorator-Like Function
# =============================================================================


from collections.abc import Callable


def add_logging(
    function: Callable[[], str],
) -> Callable[[], str]:
    """
    Wrap a function with simple logging behaviour.
    """

    def wrapper() -> str:
        """
        Execute the wrapped function.
        """
        print("Function started.")

        result: str = function()

        print("Function completed.")

        return result

    return wrapper


def get_status() -> str:
    """
    Return a status message.
    """
    return "Completed"


logged_status: Callable[[], str] = add_logging(get_status)

print(logged_status())


# =============================================================================
# 103. Decorator-Like Function With Arguments
# =============================================================================


def add_prefix_to_function(
    prefix: str,
    function: Callable[[str], str],
) -> Callable[[str], str]:
    """
    Create a wrapper that adds a prefix.
    """

    def wrapper(value: str) -> str:
        """
        Add the captured prefix.
        """
        return f"{prefix}{function(value)}"

    return wrapper


def uppercase_text(
    value: str,
) -> str:
    """
    Convert text to uppercase.
    """
    return value.upper()


prefixed_uppercase: Callable[[str], str] = add_prefix_to_function(
    "RESULT: ",
    uppercase_text,
)

print(prefixed_uppercase("python"))


# =============================================================================
# 104. Nested Function With Callable Parameter
# =============================================================================


def apply_operation(
    value: int,
    operation: Callable[[int], int],
) -> int:
    """
    Apply a supplied callable.
    """

    def execute() -> int:
        """
        Execute the operation.
        """
        return operation(value)

    return execute()


def square_number(
    number: int,
) -> int:
    """
    Return the square of a number.
    """
    return number**2


operation_result: int = apply_operation(
    5,
    square_number,
)

print(operation_result)


# =============================================================================
# 105. Nested Function With Callable Return
# =============================================================================


def create_square_function() -> Callable[[int], int]:
    """
    Create a square function.
    """

    def square(number: int) -> int:
        """
        Return a number squared.
        """
        return number**2

    return square


square_function: Callable[[int], int] = create_square_function()

print(square_function(10))


# =============================================================================
# 106. Nested Function With Generic Callable Shape
# =============================================================================


def create_transformer(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a transformation function.
    """

    def transform(value: int) -> int:
        """
        Apply the captured multiplier.
        """
        return value * multiplier

    return transform


transform_by_two: Callable[[int], int] = create_transformer(2)
transform_by_five: Callable[[int], int] = create_transformer(5)

print(transform_by_two(10))
print(transform_by_five(10))


# =============================================================================
# 107. Nested Functions And Scope Visualization
# =============================================================================
"""
Consider:

    global_value = "global"

    def outer():
        enclosing_value = "enclosing"

        def inner():
            local_value = "local"
            return local_value

        return inner()

The scopes are:

    Global scope
        |
        +-- outer() local/enclosing scope
                |
                +-- inner() local scope

When inner() searches for local_value:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

The first matching name is used.
"""


# =============================================================================
# 108. Nested Functions And Scope Summary
# =============================================================================
"""
A nested function has:

1. Its own local scope.

2. Access to variables in its enclosing function.

3. Access to global names through normal LEGB lookup.

4. Access to built-in names.

5. The ability to create closures when returned or retained.

Example:

    def outer(value: int) -> Callable[[int], int]:

        def inner(number: int) -> int:
            return value + number

        return inner

Here:

    value

belongs to the enclosing scope.

    number

belongs to the local scope of inner().

The returned function remembers value.
"""


# =============================================================================
# 109. Nested Function Scope And Shadowing
# =============================================================================


def nested_shadowing_example() -> str:
    """
    Demonstrate nested shadowing.
    """
    value: str = "outer"

    def inner() -> str:
        """
        Shadow the enclosing value.
        """
        value: str = "inner"

        return value

    outer_result: str = value
    inner_result: str = inner()

    return f"{outer_result}; {inner_result}"


nested_shadowing_result: str = nested_shadowing_example()

print(nested_shadowing_result)


# =============================================================================
# 110. Nested Function Scope Without Shadowing
# =============================================================================


def nested_no_shadowing_example() -> str:
    """
    Demonstrate nested lookup without shadowing.
    """
    value: str = "outer"

    def inner() -> str:
        """
        Read the enclosing value.
        """
        return value

    return inner()


nested_no_shadowing_result: str = nested_no_shadowing_example()

print(nested_no_shadowing_result)


# =============================================================================
# 111. Nested Function Cannot Modify Outer Variable Without nonlocal
# =============================================================================
"""
Consider:

    def outer():
        count = 0

        def inner():
            count += 1

        inner()

This does not work.

Because:

    count += 1

is an assignment.

Python therefore treats count as local to inner().

The local count has not been initialized before the operation.

Use:

    nonlocal count

when the nested function needs to modify the enclosing variable.
"""


# =============================================================================
# 112. Correct Modification With nonlocal
# =============================================================================


def create_incrementer() -> Callable[[], int]:
    """
    Correctly modify enclosing state with nonlocal.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the enclosing count.
        """
        nonlocal count

        count += 1

        return count

    return increment


incrementer: Callable[[], int] = create_incrementer()

print(incrementer())
print(incrementer())
print(incrementer())


# =============================================================================
# 113. Nested Function And Immutable Enclosing Value
# =============================================================================


def create_name_updater() -> Callable[[str], str]:
    """
    Create a name updater using nonlocal.
    """
    name: str = "Unknown"

    def update(new_name: str) -> str:
        """
        Rebind the enclosing name.
        """
        nonlocal name

        name = new_name

        return name

    return update


name_updater: Callable[[str], str] = create_name_updater()

print(name_updater("Alex"))
print(name_updater("Sam"))


# =============================================================================
# 114. Nested Function And Mutable Enclosing Value
# =============================================================================


def create_log() -> Callable[[str], list[str]]:
    """
    Create a log function using a mutable enclosing list.
    """
    messages: list[str] = []

    def add_message(message: str) -> list[str]:
        """
        Mutate the enclosing list.
        """
        messages.append(message)

        return messages.copy()

    return add_message


log: Callable[[str], list[str]] = create_log()

print(log("Started"))
print(log("Processing"))
print(log("Finished"))


# =============================================================================
# 115. Nested Function Factory For Multiplication
# =============================================================================


def multiplication_factory(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a multiplication function.
    """

    def multiply(value: int) -> int:
        """
        Multiply by the captured multiplier.
        """
        return value * multiplier

    return multiply


times_two: Callable[[int], int] = multiplication_factory(2)
times_ten: Callable[[int], int] = multiplication_factory(10)

print(times_two(7))
print(times_ten(7))


# =============================================================================
# 116. Nested Function Factory For Power
# =============================================================================


def power_factory(
    exponent: int,
) -> Callable[[int], int]:
    """
    Create a power function.
    """

    def power(value: int) -> int:
        """
        Raise a value to the captured exponent.
        """
        return value**exponent

    return power


square_factory: Callable[[int], int] = power_factory(2)
cube_factory: Callable[[int], int] = power_factory(3)

print(square_factory(5))
print(cube_factory(5))


# =============================================================================
# 117. Nested Function Factory For Formatting
# =============================================================================


def formatter_factory(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a formatting function.
    """

    def format_value(value: str) -> str:
        """
        Format using the captured prefix.
        """
        return f"{prefix}{value}"

    return format_value


info_formatter: Callable[[str], str] = formatter_factory("INFO: ")
warning_formatter: Callable[[str], str] = formatter_factory(
    "WARNING: "
)

print(info_formatter("Application started"))
print(warning_formatter("Low memory"))


# =============================================================================
# 118. Nested Function Factory For Comparison
# =============================================================================


def comparison_factory(
    expected: int,
) -> Callable[[int], bool]:
    """
    Create a comparison function.
    """

    def is_equal(value: int) -> bool:
        """
        Compare against the captured expected value.
        """
        return value == expected

    return is_equal


is_ten: Callable[[int], bool] = comparison_factory(10)

print(is_ten(10))
print(is_ten(20))


# =============================================================================
# 119. Nested Function Factory For Prefix Matching
# =============================================================================


def prefix_checker_factory(
    prefix: str,
) -> Callable[[str], bool]:
    """
    Create a prefix checker.
    """

    def starts_with(value: str) -> bool:
        """
        Check whether a string starts with the captured prefix.
        """
        return value.startswith(prefix)

    return starts_with


python_checker: Callable[[str], bool] = prefix_checker_factory(
    "Python"
)

print(python_checker("Python Functions"))
print(python_checker("Java Functions"))


# =============================================================================
# 120. Practical Nested Function Example
# =============================================================================


def calculate_invoice_total(
    price: float,
    quantity: int,
    tax_rate: float,
) -> float:
    """
    Calculate an invoice using nested helper functions.
    """

    def calculate_subtotal() -> float:
        """
        Calculate the subtotal.
        """
        return price * quantity

    def calculate_tax(subtotal: float) -> float:
        """
        Calculate tax.
        """
        return subtotal * tax_rate

    subtotal: float = calculate_subtotal()
    tax: float = calculate_tax(subtotal)

    return subtotal + tax


final_invoice_total: float = calculate_invoice_total(
    1000.0,
    2,
    0.18,
)

print(final_invoice_total)


# =============================================================================
# 121. Practical Nested Validation Example
# =============================================================================


def validate_user(
    username: str,
    age: int,
) -> str:
    """
    Validate user data with nested helper functions.
    """

    def valid_username(value: str) -> bool:
        """
        Validate username.
        """
        return len(value.strip()) >= 3

    def valid_age(value: int) -> bool:
        """
        Validate age.
        """
        return 0 <= value <= 120

    if not valid_username(username):
        return "Invalid username"

    if not valid_age(age):
        return "Invalid age"

    return "User is valid"


valid_user_result: str = validate_user(
    "Alex",
    30,
)

print(valid_user_result)


# =============================================================================
# 122. Practical Closure Example
# =============================================================================


def create_discount_calculator(
    discount_percentage: float,
) -> Callable[[float], float]:
    """
    Create a discount calculator using a closure.
    """

    def calculate(price: float) -> float:
        """
        Calculate the discounted price.
        """
        discount: float = price * discount_percentage / 100.0

        return price - discount

    return calculate


ten_percent_discount: Callable[[float], float] = (
    create_discount_calculator(10.0)
)

twenty_percent_discount: Callable[[float], float] = (
    create_discount_calculator(20.0)
)

print(ten_percent_discount(1000.0))
print(twenty_percent_discount(1000.0))


# =============================================================================
# 123. Practical State Management Example
# =============================================================================


def create_request_tracker() -> Callable[[str], int]:
    """
    Create a request tracker with private state.
    """
    request_count: int = 0

    def record_request(request_name: str) -> int:
        """
        Record a request and return the count.
        """
        nonlocal request_count

        request_count += 1

        print(f"Recorded request: {request_name}")

        return request_count

    return record_request


request_tracker: Callable[[str], int] = create_request_tracker()

print(request_tracker("GET /users"))
print(request_tracker("GET /products"))
print(request_tracker("POST /orders"))


# =============================================================================
# 124. Practical Function Factory Example
# =============================================================================


def create_validator(
    minimum: int,
    maximum: int,
) -> Callable[[int], bool]:
    """
    Create a reusable range validator.
    """

    def validate(value: int) -> bool:
        """
        Validate a value against captured bounds.
        """
        return minimum <= value <= maximum

    return validate


percentage_validator: Callable[[int], bool] = create_validator(
    0,
    100,
)

age_validator: Callable[[int], bool] = create_validator(
    0,
    120,
)

print(percentage_validator(75))
print(age_validator(30))


# =============================================================================
# 125. Common Nested Function Mistake
# =============================================================================
"""
A common mistake is defining a nested function but never calling or
returning it.

Example:

    def outer():
        def inner():
            return "Hello"

The inner function is defined, but outer() does not use it.

To use it:

    def outer():
        def inner():
            return "Hello"

        return inner()

or:

    def outer():
        def inner():
            return "Hello"

        return inner

The first returns the result.

The second returns the function itself.
"""


# =============================================================================
# 126. Returning Result Versus Returning Function
# =============================================================================


def return_result() -> str:
    """
    Return the result of a nested function.
    """

    def inner() -> str:
        """
        Return a string.
        """
        return "Result"

    return inner()


def return_function() -> Callable[[], str]:
    """
    Return the nested function itself.
    """

    def inner() -> str:
        """
        Return a string.
        """
        return "Function result"

    return inner


result_value: str = return_result()

returned_function: Callable[[], str] = return_function()
function_result: str = returned_function()

print(result_value)
print(function_result)


# =============================================================================
# 127. Nested Function As a Local Implementation Detail
# =============================================================================


def calculate_statistics(
    values: list[float],
) -> tuple[float, float]:
    """
    Calculate minimum and maximum values.
    """

    def find_minimum(items: list[float]) -> float:
        """
        Find the minimum value.
        """
        if not items:
            raise ValueError("The list cannot be empty.")

        return min(items)

    def find_maximum(items: list[float]) -> float:
        """
        Find the maximum value.
        """
        if not items:
            raise ValueError("The list cannot be empty.")

        return max(items)

    minimum: float = find_minimum(values)
    maximum: float = find_maximum(values)

    return minimum, maximum


minimum_value, maximum_value = calculate_statistics(
    [10.0, 20.0, 5.0, 30.0],
)

print(minimum_value)
print(maximum_value)


# =============================================================================
# 128. Nested Function And Explicit Data Flow
# =============================================================================


def calculate_final_price(
    price: float,
    discount: float,
    tax: float,
) -> float:
    """
    Calculate a final price using explicit data flow.
    """

    def apply_discount(value: float) -> float:
        """
        Apply a discount percentage.
        """
        return value - (value * discount / 100.0)

    def apply_tax(value: float) -> float:
        """
        Apply a tax percentage.
        """
        return value + (value * tax / 100.0)

    discounted_price: float = apply_discount(price)
    final_price: float = apply_tax(discounted_price)

    return final_price


final_price: float = calculate_final_price(
    1000.0,
    10.0,
    18.0,
)

print(final_price)


# =============================================================================
# 129. Nested Function And Encapsulation
# =============================================================================
"""
Nested functions can hide implementation details.

If a helper function is needed only by one outer function, placing it
inside the outer function can make the relationship clear.

Example:

    def process_data(data):
        def clean():
            ...

        def validate():
            ...

        clean()
        validate()

The helpers are conceptually private to process_data().

They are not available as module-level names.
"""


# =============================================================================
# 130. Nested Functions And Closures Summary
# =============================================================================
"""
A closure is created when a nested function retains access to variables
from its enclosing scope.

Example:

    def create_multiplier(
        multiplier: int,
    ) -> Callable[[int], int]:

        def multiply(
            number: int,
        ) -> int:
            return number * multiplier

        return multiply

The returned function remembers multiplier.

This allows:

    double = create_multiplier(2)
    triple = create_multiplier(3)

Then:

    double(10)

returns:

    20

and:

    triple(10)

returns:

    30

The outer function has already returned, but the nested functions retain
access to their captured values.
"""


# =============================================================================
# 131. Nested Functions And nonlocal Summary
# =============================================================================
"""
Use nonlocal when a nested function needs to rebind a variable belonging
to an enclosing function.

Example:

    def create_counter() -> Callable[[], int]:
        count: int = 0

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

Without nonlocal, count += 1 would cause Python to treat count as a
local variable inside increment().

Important:

    nonlocal
        ↓
    enclosing function scope

while:

    global
        ↓
    module/global scope
"""


# =============================================================================
# 132. Nested Functions And Mutable Objects
# =============================================================================
"""
Mutation and rebinding are different.

Mutation:

    values.append(item)

does not require nonlocal when values belongs to the enclosing scope.

Rebinding:

    values = [item]

does require nonlocal if values belongs to the enclosing function.

Example:

    def outer():
        values = []

        def add():
            values.append(10)

Mutation does not require nonlocal.

But:

    def outer():
        values = []

        def replace():
            nonlocal values
            values = [10]

Rebinding requires nonlocal.
"""


# =============================================================================
# 133. Nested Function Rules
# =============================================================================
"""
Important nested-function rules:

1. A nested function is defined inside another function.

2. The nested function has its own local scope.

3. The outer function provides an enclosing scope.

4. A nested function can read enclosing variables.

5. Reading an enclosing variable does not require nonlocal.

6. Rebinding an enclosing variable requires nonlocal.

7. global refers to module/global scope.

8. nonlocal refers to the nearest enclosing function scope.

9. Nested functions can access global variables through LEGB.

10. Nested functions can access built-in names.

11. A nested function can be returned from its outer function.

12. Returning a nested function can create a closure.

13. Closures can remember outer parameters.

14. Closures can maintain private state.

15. Multiple calls to a function factory can create independent closures.

16. Nested functions are useful for local helper logic.

17. Nested functions can be used for validation.

18. Nested functions can be used for transformation.

19. Nested functions can be used for callbacks.

20. Nested functions are heavily used by decorators.

21. A called function does not inherit the caller's local scope.

22. Only lexical nesting creates an enclosing scope.

23. A nested function can shadow an enclosing variable.

24. Mutating an enclosing object is different from rebinding its name.

25. Nested functions should be used when the local relationship improves
    readability and encapsulation.
"""


# =============================================================================
# 134. LEGB With Nested Functions
# =============================================================================
"""
For a nested function:

    def outer():
        value = "enclosing"

        def inner():
            value = "local"
            return value

        return inner()

Python searches:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

The local value is found first.

If inner() did not define value, Python would search outer().

If outer() did not define value, Python would search global scope.

If the global scope did not contain value, Python would search built-in
scope.

If no matching name exists, Python raises NameError.
"""


# =============================================================================
# 135. Nested Function Core Example
# =============================================================================


def core_nested_example(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Demonstrate the core nested-function pattern.
    """

    def multiply(value: int) -> int:
        """
        Multiply using an enclosing variable.
        """
        return value * multiplier

    return multiply


core_double: Callable[[int], int] = core_nested_example(2)
core_triple: Callable[[int], int] = core_nested_example(3)

print(core_double(10))
print(core_triple(10))


# =============================================================================
# 136. Nested Functions Best Practices
# =============================================================================
"""
Good practices:

- Use nested functions for logic that belongs only to one outer function.
- Give nested functions descriptive names.
- Add type annotations to parameters and return values.
- Use nonlocal only when enclosing state genuinely needs to be changed.
- Prefer explicit parameters and return values when state does not need
  to persist.
- Use closures when a function needs to remember configuration or state.
- Avoid unnecessarily deep nesting.
- Keep nested functions small and focused.
- Avoid shadowing names unless the meaning is clear.
- Use Callable annotations when returning function objects.
- Keep mutable closure state intentional and easy to understand.
- Prefer simple local helpers for one-off implementation details.
"""


# =============================================================================
# 137. Common Mistakes
# =============================================================================
"""
Common nested-function mistakes include:

- Forgetting to call the nested function.
- Forgetting to return the nested function when a closure is intended.
- Confusing returning a function with calling a function.
- Forgetting nonlocal when rebinding an enclosing variable.
- Using global when nonlocal is required.
- Assuming the caller's local variables are available.
- Accidentally shadowing an enclosing variable.
- Rebinding a mutable object when mutation was intended.
- Creating unnecessary levels of nesting.
- Returning a callable without an appropriate type annotation.
"""


# =============================================================================
# 138. Return Function Versus Call Function
# =============================================================================
"""
Important distinction:

    return inner

returns the function object.

while:

    return inner()

calls the function and returns its result.

Example:

    def outer() -> Callable[[], str]:

        def inner() -> str:
            return "Hello"

        return inner

Here the caller receives a function.

Example:

    def outer() -> str:

        def inner() -> str:
            return "Hello"

        return inner()

Here the caller receives the string "Hello".
"""


# =============================================================================
# 139. Complete Closure Model
# =============================================================================
"""
A closure can be understood as:

    Outer function
          |
          | creates
          ↓
    Enclosing variables
          |
          | captured by
          ↓
    Nested function
          |
          | returned
          ↓
    Callable object
          |
          | remembers
          ↓
    Enclosing state

Example:

    def create_counter() -> Callable[[], int]:
        count = 0

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

The returned increment function remembers count.
"""


# =============================================================================
# 140. Final Practical Example
# =============================================================================


def create_user_service(
    service_name: str,
) -> tuple[
    Callable[[str], str],
    Callable[[str], str],
]:
    """
    Create a small service using nested functions and closures.
    """

    def create_message(
        username: str,
    ) -> str:
        """
        Create a service message.
        """
        return f"{service_name}: Hello, {username}!"

    def create_status(
        username: str,
    ) -> str:
        """
        Create a service status message.
        """
        return f"{service_name}: {username} is active."

    return create_message, create_status


user_message_function, user_status_function = create_user_service(
    "UserService",
)

print(user_message_function("Alex"))
print(user_status_function("Alex"))


# =============================================================================
# 141. Final Nested Counter Example
# =============================================================================


def create_private_counter(
    initial_value: int = 0,
) -> Callable[[], int]:
    """
    Create a private counter using a closure.
    """
    count: int = initial_value

    def increment() -> int:
        """
        Increment the private counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


private_counter: Callable[[], int] = create_private_counter(100)

print(private_counter())
print(private_counter())
print(private_counter())


# =============================================================================
# 142. Final Function Factory Example
# =============================================================================


def create_power(
    exponent: int,
) -> Callable[[int], int]:
    """
    Create a reusable power function.
    """

    def calculate(number: int) -> int:
        """
        Calculate the power using the captured exponent.
        """
        return number**exponent

    return calculate


square: Callable[[int], int] = create_power(2)
cube: Callable[[int], int] = create_power(3)

square_result: int = square(10)
cube_result: int = cube(10)

print(square_result)
print(cube_result)


# =============================================================================
# 143. Final Scope Model
# =============================================================================
"""
Nested functions fit directly into the LEGB model.

Example:

    global_value = "global"

    def outer():
        enclosing_value = "enclosing"

        def inner():
            local_value = "local"

            return (
                local_value,
                enclosing_value,
                global_value,
            )

        return inner()

The lookup structure is:

    inner()
       |
       +--> Local
       |
       +--> Enclosing
       |
       +--> Global
       |
       +--> Built-in

The closest matching name is selected.
"""


# =============================================================================
# 144. Nested Functions Summary
# =============================================================================
"""
Nested functions are functions defined inside other functions.

Core structure:

    def outer():
        def inner():
            pass

        inner()

The outer function creates an enclosing scope.

The nested function has its own local scope.

A nested function can:

- Read enclosing variables.
- Read global variables.
- Use built-in names.
- Define its own local variables.
- Receive its own parameters.
- Call other functions.
- Call other nested functions.
- Be returned from the outer function.
- Form a closure.
- Maintain private state.
- Use nonlocal to modify enclosing variables.
- Use global to modify module-level variables.
- Act as a local helper.
- Act as a callback.
- Be used to build decorators.
- Be used to create function factories.

The most important distinction is:

    Local
        ↓
    variables belonging to the current function

    Enclosing
        ↓
    variables belonging to surrounding functions

    Global
        ↓
    variables belonging to the module

    Built-in
        ↓
    names provided by Python

This is the LEGB rule.
"""


# =============================================================================
# Key Takeaways
# =============================================================================
"""
✓ A nested function is a function defined inside another function.

✓ A nested function has its own local scope.

✓ The outer function creates an enclosing scope.

✓ Nested functions can read variables from their enclosing function.

✓ Reading an enclosing variable does not require nonlocal.

✓ Rebinding an enclosing variable requires nonlocal.

✓ global refers to module/global scope.

✓ nonlocal refers to the nearest enclosing function scope.

✓ Nested functions follow the LEGB name-resolution rule.

✓ A called function does not inherit the caller's local scope.

✓ Lexical nesting creates an enclosing scope.

✓ A nested function can shadow an enclosing variable.

✓ Nested functions can be used as local implementation helpers.

✓ Nested functions can perform validation.

✓ Nested functions can perform calculations.

✓ Nested functions can perform transformations.

✓ Nested functions can act as callbacks.

✓ Nested functions can be returned from outer functions.

✓ Returning a nested function can create a closure.

✓ A closure remembers variables from its enclosing scope.

✓ Function factories commonly use closures.

✓ Closures can remember configuration values.

✓ Closures can maintain private state.

✓ Multiple closures can maintain independent state.

✓ Mutable enclosing objects can be changed without nonlocal when the
  object itself is mutated.

✓ Rebinding an enclosing name requires nonlocal.

✓ Returning a function and calling a function are different operations.

✓ Callable annotations should be used when returning function objects.

✓ Nested functions are an important foundation for decorators.

Core pattern:

    def outer(
        configuration: int,
    ) -> Callable[[int], int]:

        def inner(
            value: int,
        ) -> int:
            return value + configuration

        return inner

Core closure pattern:

    outer()
        ↓
    creates enclosing state
        ↓
    nested function
        ↓
    captures enclosing state
        ↓
    returned function
        ↓
    closure

Core nonlocal pattern:

    def outer() -> Callable[[], int]:
        value: int = 0

        def inner() -> int:
            nonlocal value
            value += 1
            return value

        return inner

Core function-factory pattern:

    def create_multiplier(
        multiplier: int,
    ) -> Callable[[int], int]:

        def multiply(
            value: int,
        ) -> int:
            return value * multiplier

        return multiply

The central idea:

    OUTER FUNCTION
          ↓
    ENCLOSING SCOPE
          ↓
    NESTED FUNCTION
          ↓
    LOCAL SCOPE
          ↓
    OPTIONAL CLOSURE
          ↓
    REMEMBERED STATE / CONFIGURATION

Nested functions are therefore one of the fundamental mechanisms behind
closures, function factories, decorators, callbacks, and encapsulated
function-level behaviour.
"""


# =============================================================================
# End of 13_nested_functions.py
# =============================================================================