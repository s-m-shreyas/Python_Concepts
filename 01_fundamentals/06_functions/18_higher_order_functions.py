# =============================================================================
# 18. Higher-Order Functions
# =============================================================================
# type: ignore
"""
Python Functions

File:
    18_higher_order_functions.py

Topic:
    Higher-Order Functions

Overview:
    A higher-order function is a function that does at least one of the
    following:

        1. Accepts another function as an argument.
        2. Returns another function as its result.

    Python supports higher-order functions because functions are first-class
    objects.

Topics covered:

    - What is a higher-order function?
    - Functions as arguments
    - Functions as return values
    - Passing functions to other functions
    - Returning functions
    - Function callbacks
    - Built-in higher-order functions
    - map()
    - filter()
    - sorted() with key
    - min() with key
    - max() with key
    - any()
    - all()
    - reduce()
    - functools.reduce()
    - Custom higher-order functions
    - Function factories
    - Closures
    - Higher-order functions with type annotations
    - Callable
    - collections.abc.Callable
    - Functions accepting callbacks
    - Functions returning callbacks
    - Composing functions
    - Applying transformations
    - Reusable function pipelines
    - Higher-order functions versus normal functions
    - Practical examples
    - Common mistakes
    - Best practices
    - Summary
"""

# =============================================================================
# 01. What Is a Higher-Order Function?
# =============================================================================
"""
A higher-order function is a function that works with other functions.

A function is considered higher-order when it:

    - accepts a function as an argument
    - returns a function
    - or does both

Example:

    def apply_operation(
        operation,
        value,
    ):
        return operation(value)

Here:

    apply_operation()

accepts another function:

    operation

Therefore apply_operation() is a higher-order function.

Core idea:

    FUNCTION
        ↓
    passed to another function
        ↓
    higher-order function
"""

# =============================================================================
# 02. Functions Are First-Class Objects
# =============================================================================
"""
Python functions are first-class objects.

This means functions can be:

    - assigned to variables
    - stored in lists
    - stored in dictionaries
    - passed as arguments
    - returned from functions
    - stored in tuples
    - used as dictionary values
    - used as elements of other data structures

Example:

    def greet() -> str:
        return "Hello"

    message_function = greet

The variable:

    message_function

now refers to the same function object as:

    greet
"""

# =============================================================================
# 03. Assigning a Function to a Variable
# =============================================================================


def greet() -> str:
    """
    Return a greeting.
    """
    return "Hello, Python!"


greeting_function = greet

greeting_result: str = greeting_function()

print(greeting_result)

# greet and greeting_function refer to the same function object.
#
# The function is not copied.
#
# The name greeting_function simply becomes another reference to the function.

# =============================================================================
# 04. Passing a Function as an Argument
# =============================================================================


def square(
    number: int,
) -> int:
    """
    Return the square of a number.
    """
    return number**2


def apply_function(
    function,
    value: int,
) -> int:
    """
    Apply a supplied function to a value.
    """
    return function(value)


square_result: int = apply_function(
    square,
    5,
)

print(square_result)

# square is passed to apply_function().
#
# apply_function() receives square through its function parameter.
#
# The function is then called inside apply_function().

# =============================================================================
# 05. Explicit Callable Type Annotation
# =============================================================================

from collections.abc import Callable


def cube(
    number: int,
) -> int:
    """
    Return the cube of a number.
    """
    return number**3


def apply_integer_function(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Apply a function that accepts an integer and returns an integer.
    """
    return function(value)


cube_result: int = apply_integer_function(
    cube,
    4,
)

print(cube_result)

# Callable[[int], int] means:
#
#     function accepts:
#         int
#
#     function returns:
#         int

# =============================================================================
# 06. Passing Different Functions
# =============================================================================


def add_one(
    number: int,
) -> int:
    """
    Add one to a number.
    """
    return number + 1


def double(
    number: int,
) -> int:
    """
    Double a number.
    """
    return number * 2


def apply_operation(
    operation: Callable[[int], int],
    value: int,
) -> int:
    """
    Apply an integer operation.
    """
    return operation(value)


add_one_result: int = apply_operation(
    add_one,
    10,
)

double_result: int = apply_operation(
    double,
    10,
)

print(add_one_result)
print(double_result)

# The same higher-order function can work with different functions.

# =============================================================================
# 07. Multiple Function Arguments
# =============================================================================


def add(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


def subtract(
    first: int,
    second: int,
) -> int:
    """
    Subtract two integers.
    """
    return first - second


def calculate(
    operation: Callable[[int, int], int],
    first: int,
    second: int,
) -> int:
    """
    Apply a binary integer operation.
    """
    return operation(
        first,
        second,
    )


addition: int = calculate(
    add,
    20,
    5,
)

subtraction: int = calculate(
    subtract,
    20,
    5,
)

print(addition)
print(subtraction)

# Callable[[int, int], int] means:
#
#     two integer arguments
#     ↓
#     one integer result

# =============================================================================
# 08. Functions Returning Functions
# =============================================================================


def create_greeting_function() -> Callable[[], str]:
    """
    Return a greeting function.
    """

    def greeting() -> str:
        """
        Return a greeting.
        """
        return "Hello!"

    return greeting


greeting_function = create_greeting_function()

returned_greeting: str = greeting_function()

print(returned_greeting)

# create_greeting_function() returns another function.
#
# Therefore it is a higher-order function.

# =============================================================================
# 09. Returning a Function With Parameters
# =============================================================================


def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Return a function that multiplies by multiplier.
    """

    def multiply(
        number: int,
    ) -> int:
        """
        Multiply a number by the captured multiplier.
        """
        return number * multiplier

    return multiply


double_function = create_multiplier(
    2,
)

triple_function = create_multiplier(
    3,
)

double_value: int = double_function(
    10,
)

triple_value: int = triple_function(
    10,
)

print(double_value)
print(triple_value)

# create_multiplier() returns a function.
#
# The returned function remembers multiplier.
#
# This is both:
#
#     - a higher-order function
#     - a closure

# =============================================================================
# 10. Function Factory
# =============================================================================


def create_power_function(
    exponent: int,
) -> Callable[[int], int]:
    """
    Create and return a power function.
    """

    def power(
        number: int,
    ) -> int:
        """
        Raise a number to the captured exponent.
        """
        return number**exponent

    return power


square_function = create_power_function(
    2,
)

cube_function = create_power_function(
    3,
)

square_value: int = square_function(
    5,
)

cube_value: int = cube_function(
    5,
)

print(square_value)
print(cube_value)

# A function factory creates functions dynamically.

# =============================================================================
# 11. Callback Functions
# =============================================================================
"""
A callback is a function supplied to another function so that the receiving
function can call it later.

Example:

    def process(
        callback,
    ):
        callback()

The callback function controls what happens at a particular point.

Callbacks are commonly used for:

    - event handling
    - validation
    - transformations
    - logging
    - sorting
    - asynchronous programming
    - GUI programming
    - APIs
"""

# =============================================================================
# 12. Simple Callback
# =============================================================================


def on_success() -> str:
    """
    Return a success message.
    """
    return "Operation completed successfully."


def execute_callback(
    callback: Callable[[], str],
) -> str:
    """
    Execute a callback function.
    """
    return callback()


callback_result: str = execute_callback(
    on_success,
)

print(callback_result)

# on_success is the callback.
#
# execute_callback() controls when the callback is executed.

# =============================================================================
# 13. Callback With Arguments
# =============================================================================


def format_name(
    name: str,
) -> str:
    """
    Format a person's name.
    """
    return name.upper()


def process_name(
    name: str,
    formatter: Callable[[str], str],
) -> str:
    """
    Process a name using a callback.
    """
    return formatter(name)


formatted_name: str = process_name(
    "Alex",
    format_name,
)

print(formatted_name)

# The formatter function is supplied by the caller.

# =============================================================================
# 14. Multiple Callbacks
# =============================================================================


def uppercase_text(
    text: str,
) -> str:
    """
    Convert text to uppercase.
    """
    return text.upper()


def lowercase_text(
    text: str,
) -> str:
    """
    Convert text to lowercase.
    """
    return text.lower()


def process_text(
    text: str,
    formatter: Callable[[str], str],
) -> str:
    """
    Process text with a formatter.
    """
    return formatter(text)


uppercase_result: str = process_text(
    "Python",
    uppercase_text,
)

lowercase_result: str = process_text(
    "Python",
    lowercase_text,
)

print(uppercase_result)
print(lowercase_result)

# =============================================================================
# 15. Applying a Function to Every Item
# =============================================================================


def apply_to_all(
    values: list[int],
    function: Callable[[int], int],
) -> list[int]:
    """
    Apply a function to every item.
    """
    results: list[int] = []

    for value in values:
        results.append(
            function(value),
        )

    return results


numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
]

squared_numbers: list[int] = apply_to_all(
    numbers,
    square,
)

print(squared_numbers)

# apply_to_all() is a higher-order function because it accepts a function.

# =============================================================================
# 16. Transforming Data
# =============================================================================


def increment(
    number: int,
) -> int:
    """
    Increment a number.
    """
    return number + 1


incremented_numbers: list[int] = apply_to_all(
    numbers,
    increment,
)

print(incremented_numbers)

# The higher-order function separates:
#
#     HOW to iterate
#
# from:
#
#     WHAT transformation to perform.

# =============================================================================
# 17. Built-in map()
# =============================================================================
"""
map() is a built-in higher-order function.

It applies a function to every item in an iterable.

General form:

    map(
        function,
        iterable,
    )

Example:

    map(
        square,
        numbers,
    )

map() returns a map iterator.

It can be converted to a list when needed.
"""

mapped_squares: list[int] = list(
    map(
        square,
        numbers,
    ),
)

print(mapped_squares)

# =============================================================================
# 18. map() With a Named Function
# =============================================================================


def add_ten(
    number: int,
) -> int:
    """
    Add ten to a number.
    """
    return number + 10


mapped_values: list[int] = list(
    map(
        add_ten,
        numbers,
    ),
)

print(mapped_values)

# =============================================================================
# 19. map() With Multiple Iterables
# =============================================================================


def add_values(
    first: int,
    second: int,
) -> int:
    """
    Add two integers.
    """
    return first + second


first_numbers: list[int] = [
    1,
    2,
    3,
]

second_numbers: list[int] = [
    10,
    20,
    30,
]

added_numbers: list[int] = list(
    map(
        add_values,
        first_numbers,
        second_numbers,
    ),
)

print(added_numbers)

# map() passes corresponding items to add_values().

# =============================================================================
# 20. map() With a Lambda
# =============================================================================

lambda_squared_numbers: list[int] = list(
    map(
        lambda number: number**2,
        numbers,
    ),
)

print(lambda_squared_numbers)

# The lambda is itself a function object.
#
# map() receives that function and applies it to each item.

# =============================================================================
# 21. Built-in filter()
# =============================================================================
"""
filter() is another higher-order function.

It keeps items for which a supplied function returns a truthy value.

General form:

    filter(
        function,
        iterable,
    )

Example:

    filter(
        is_even,
        numbers,
    )
"""

# =============================================================================
# 22. filter() With a Named Function
# =============================================================================


def is_even(
    number: int,
) -> bool:
    """
    Return True when number is even.
    """
    return number % 2 == 0


even_numbers: list[int] = list(
    filter(
        is_even,
        numbers,
    ),
)

print(even_numbers)

# =============================================================================
# 23. filter() With a Lambda
# =============================================================================

odd_numbers: list[int] = list(
    filter(
        lambda number: number % 2 != 0,
        numbers,
    ),
)

print(odd_numbers)

# =============================================================================
# 24. map() and filter() Together
# =============================================================================

even_squared_numbers: list[int] = list(
    map(
        square,
        filter(
            is_even,
            numbers,
        ),
    ),
)

print(even_squared_numbers)

# Processing flow:
#
#     numbers
#         ↓
#     filter()
#         ↓
#     even numbers
#         ↓
#     map()
#         ↓
#     squared even numbers

# =============================================================================
# 25. sorted() as a Higher-Order Function
# =============================================================================
"""
sorted() accepts an optional key function.

The key function determines the value used for comparison.

Example:

    sorted(
        values,
        key=function,
    )

Therefore sorted() can work with another function.
"""

# =============================================================================
# 26. Sorting Strings by Length
# =============================================================================


words: list[str] = [
    "Python",
    "Go",
    "Java",
    "JavaScript",
]

words_by_length: list[str] = sorted(
    words,
    key=len,
)

print(words_by_length)

# len is passed as a function.
#
# sorted() calls len() for each item.

# =============================================================================
# 27. Sorting With a Custom Function
# =============================================================================


def get_word_length(
    word: str,
) -> int:
    """
    Return the length of a word.
    """
    return len(word)


sorted_words: list[str] = sorted(
    words,
    key=get_word_length,
)

print(sorted_words)

# get_word_length is a callback supplied to sorted().

# =============================================================================
# 28. Sorting in Reverse
# =============================================================================

longest_first: list[str] = sorted(
    words,
    key=len,
    reverse=True,
)

print(longest_first)

# =============================================================================
# 29. Sorting Objects
# =============================================================================


students: list[dict[str, object]] = [
    {
        "name": "Alex",
        "score": 85,
    },
    {
        "name": "Sam",
        "score": 95,
    },
    {
        "name": "Jordan",
        "score": 75,
    },
]


def get_score(
    student: dict[str, object],
) -> object:
    """
    Return a student's score.
    """
    return student["score"]


students_by_score: list[dict[str, object]] = sorted(
    students,
    key=get_score,
)

print(students_by_score)

# =============================================================================
# 30. min() With key
# =============================================================================


shortest_word: str = min(
    words,
    key=len,
)

print(shortest_word)

# min() accepts a key function.
#
# It uses the result of the key function for comparison.

# =============================================================================
# 31. max() With key
# =============================================================================


longest_word: str = max(
    words,
    key=len,
)

print(longest_word)

# max() also accepts a key function.

# =============================================================================
# 32. any() and all()
# =============================================================================
"""
any() and all() are commonly used with generator expressions.

any():

    Returns True when at least one item is truthy.

all():

    Returns True when every item is truthy.

They are often used together with higher-order-style transformations
and predicates.
"""

# =============================================================================
# 33. any() Example
# =============================================================================


numbers_for_any: list[int] = [
    1,
    3,
    5,
    8,
]

contains_even: bool = any(
    number % 2 == 0
    for number in numbers_for_any
)

print(contains_even)

# =============================================================================
# 34. all() Example
# =============================================================================


numbers_for_all: list[int] = [
    2,
    4,
    6,
    8,
]

all_even: bool = all(
    number % 2 == 0
    for number in numbers_for_all
)

print(all_even)

# =============================================================================
# 35. functools.reduce()
# =============================================================================
"""
reduce() repeatedly applies a function to the items of an iterable.

Import:

    from functools import reduce

Conceptually:

    reduce(
        function,
        [1, 2, 3, 4],
    )

can perform:

    ((1 operation 2) operation 3) operation 4

reduce() is useful when many values need to be combined into one value.
"""

# =============================================================================
# 36. reduce() Example
# =============================================================================

from functools import reduce


def multiply_values(
    first: int,
    second: int,
) -> int:
    """
    Multiply two integers.
    """
    return first * second


product: int = reduce(
    multiply_values,
    [1, 2, 3, 4, 5],
)

print(product)

# reduce() repeatedly calls multiply_values().

# =============================================================================
# 37. reduce() With an Initial Value
# =============================================================================

sum_with_initial: int = reduce(
    add_values,
    [1, 2, 3, 4],
    100,
)

print(sum_with_initial)

# The initial value becomes the starting accumulator.

# =============================================================================
# 38. Custom Reduce-Like Function
# =============================================================================


def accumulate_values(
    values: list[int],
    operation: Callable[[int, int], int],
    initial: int,
) -> int:
    """
    Combine values using a supplied binary operation.
    """
    result: int = initial

    for value in values:
        result = operation(
            result,
            value,
        )

    return result


accumulated_sum: int = accumulate_values(
    [1, 2, 3, 4],
    add_values,
    0,
)

print(accumulated_sum)

# This is a custom higher-order function.
#
# It receives:
#
#     operation
#
# and uses that function repeatedly.

# =============================================================================
# 39. Different Operations With the Same Higher-Order Function
# =============================================================================


accumulated_product: int = accumulate_values(
    [1, 2, 3, 4],
    multiply_values,
    1,
)

print(accumulated_product)

# Same higher-order function.
#
# Different operation.
#
# This makes the code reusable.

# =============================================================================
# 40. Predicate Functions
# =============================================================================
"""
A predicate is a function that evaluates a condition and usually returns
True or False.

Examples:

    is_even()
    is_positive()
    is_valid()
    has_permission()

Predicates are commonly passed to higher-order functions.
"""

# =============================================================================
# 41. Custom Predicate-Based Filter
# =============================================================================


def filter_values(
    values: list[int],
    predicate: Callable[[int], bool],
) -> list[int]:
    """
    Keep values that satisfy a predicate.
    """
    results: list[int] = []

    for value in values:
        if predicate(value):
            results.append(value)

    return results


positive_numbers: list[int] = filter_values(
    [
        -2,
        -1,
        0,
        1,
        2,
    ],
    lambda number: number > 0,
)

print(positive_numbers)

# =============================================================================
# 42. Reusable Predicate
# =============================================================================


def is_positive(
    number: int,
) -> bool:
    """
    Return True for positive numbers.
    """
    return number > 0


positive_values: list[int] = filter_values(
    [
        -10,
        0,
        5,
        10,
    ],
    is_positive,
)

print(positive_values)

# =============================================================================
# 43. Higher-Order Function for Validation
# =============================================================================


def validate_value(
    value: int,
    validator: Callable[[int], bool],
) -> bool:
    """
    Validate a value using a supplied validator.
    """
    return validator(value)


is_valid_number: bool = validate_value(
    10,
    is_positive,
)

print(is_valid_number)

# =============================================================================
# 44. Multiple Validation Rules
# =============================================================================


def is_greater_than_five(
    number: int,
) -> bool:
    """
    Return True when number is greater than five.
    """
    return number > 5


greater_than_five: bool = validate_value(
    10,
    is_greater_than_five,
)

print(greater_than_five)

# =============================================================================
# 45. Function Composition
# =============================================================================
"""
Function composition means combining functions so that the output of one
function becomes the input of another.

For example:

    square(
        increment(
            4,
        ),
    )

can be represented as a composed function.
"""

# =============================================================================
# 46. Simple Function Composition
# =============================================================================


def compose(
    first: Callable[[int], int],
    second: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Return a function that applies first and then second.
    """

    def composed(
        value: int,
    ) -> int:
        """
        Apply the composed functions.
        """
        first_result: int = first(value)

        return second(first_result)

    return composed


increment_then_square = compose(
    increment,
    square,
)

composed_result: int = increment_then_square(
    4,
)

print(composed_result)

# Execution:
#
#     4
#     ↓
#     increment()
#     ↓
#     5
#     ↓
#     square()
#     ↓
#     25

# =============================================================================
# 47. Reverse Function Composition
# =============================================================================


def compose_reverse(
    first: Callable[[int], int],
    second: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Return a function that applies second and then first.
    """

    def composed(
        value: int,
    ) -> int:
        """
        Apply the functions in reverse order.
        """
        second_result: int = second(value)

        return first(second_result)

    return composed


square_then_increment = compose_reverse(
    increment,
    square,
)

reverse_composed_result: int = square_then_increment(
    4,
)

print(reverse_composed_result)

# Execution:
#
#     4
#     ↓
#     square()
#     ↓
#     16
#     ↓
#     increment()
#     ↓
#     17

# =============================================================================
# 48. Applying Multiple Transformations
# =============================================================================


def apply_pipeline(
    value: int,
    functions: list[Callable[[int], int]],
) -> int:
    """
    Apply multiple functions sequentially.
    """
    result: int = value

    for function in functions:
        result = function(result)

    return result


pipeline_result: int = apply_pipeline(
    5,
    [
        increment,
        double,
        square,
    ],
)

print(pipeline_result)

# Execution:
#
#     5
#     ↓
#     increment -> 6
#     ↓
#     double    -> 12
#     ↓
#     square    -> 144

# =============================================================================
# 49. Pipeline With Named Functions
# =============================================================================


def subtract_one(
    number: int,
) -> int:
    """
    Subtract one from a number.
    """
    return number - 1


pipeline_functions: list[Callable[[int], int]] = [
    double,
    subtract_one,
    square,
]

pipeline_output: int = apply_pipeline(
    5,
    pipeline_functions,
)

print(pipeline_output)

# =============================================================================
# 50. Pipeline With Lambda Functions
# =============================================================================

lambda_pipeline_result: int = apply_pipeline(
    5,
    [
        lambda number: number + 10,
        lambda number: number * 2,
        lambda number: number - 5,
    ],
)

print(lambda_pipeline_result)

# =============================================================================
# 51. Function Returning a Validator
# =============================================================================


def create_minimum_validator(
    minimum: int,
) -> Callable[[int], bool]:
    """
    Return a validator that checks a minimum value.
    """

    def validate(
        value: int,
    ) -> bool:
        """
        Check whether value meets the minimum.
        """
        return value >= minimum

    return validate


validate_at_least_ten = create_minimum_validator(
    10,
)

minimum_validation_result: bool = validate_at_least_ten(
    15,
)

print(minimum_validation_result)

# =============================================================================
# 52. Function Returning a Formatter
# =============================================================================


def create_prefix_formatter(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a formatter with a fixed prefix.
    """

    def format_text(
        text: str,
    ) -> str:
        """
        Add the captured prefix.
        """
        return f"{prefix}: {text}"

    return format_text


info_formatter = create_prefix_formatter(
    "INFO",
)

error_formatter = create_prefix_formatter(
    "ERROR",
)

info_message: str = info_formatter(
    "Application started",
)

error_message: str = error_formatter(
    "Application failed",
)

print(info_message)
print(error_message)

# =============================================================================
# 53. Higher-Order Function for Logging
# =============================================================================


def log_result(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Execute a function and print its result.
    """
    result: int = function(value)

    print(
        f"Result: {result}",
    )

    return result


logged_square: int = log_result(
    square,
    8,
)

print(logged_square)

# =============================================================================
# 54. Wrapper Function
# =============================================================================


def with_message(
    function: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Return a wrapper around another function.
    """

    def wrapper(
        value: int,
    ) -> int:
        """
        Execute the wrapped function with messages.
        """
        print(
            "Function started.",
        )

        result: int = function(value)

        print(
            "Function completed.",
        )

        return result

    return wrapper


wrapped_square = with_message(
    square,
)

wrapped_square_result: int = wrapped_square(
    5,
)

print(wrapped_square_result)

# This pattern is closely related to decorators.

# =============================================================================
# 55. Higher-Order Function and Closures
# =============================================================================


def create_tax_calculator(
    tax_rate: float,
) -> Callable[[float], float]:
    """
    Create a tax calculator using a captured tax rate.
    """

    def calculate_tax(
        price: float,
    ) -> float:
        """
        Calculate tax using the captured rate.
        """
        return price * tax_rate

    return calculate_tax


calculate_eighteen_percent_tax = create_tax_calculator(
    0.18,
)

tax_amount: float = calculate_eighteen_percent_tax(
    1000.0,
)

print(tax_amount)

# tax_rate belongs to the enclosing scope.
#
# calculate_tax() remembers tax_rate.
#
# This is a closure.

# =============================================================================
# 56. Returning a Function With Multiple Captured Values
# =============================================================================


def create_price_calculator(
    tax_rate: float,
    discount_rate: float,
) -> Callable[[float], float]:
    """
    Create a price calculator with captured configuration.
    """

    def calculate_price(
        price: float,
    ) -> float:
        """
        Calculate the final price.
        """
        discounted_price: float = (
            price
            - price * discount_rate
        )

        final_price: float = (
            discounted_price
            + discounted_price * tax_rate
        )

        return final_price

    return calculate_price


calculate_sale_price = create_price_calculator(
    0.18,
    0.10,
)

sale_price: float = calculate_sale_price(
    1000.0,
)

print(sale_price)

# The returned function remembers:
#
#     tax_rate
#     discount_rate

# =============================================================================
# 57. Higher-Order Function With a List of Functions
# =============================================================================


def execute_all(
    value: int,
    functions: list[Callable[[int], int]],
) -> list[int]:
    """
    Execute every supplied function using the same value.
    """
    results: list[int] = []

    for function in functions:
        results.append(
            function(value),
        )

    return results


function_results: list[int] = execute_all(
    5,
    [
        square,
        cube,
        double,
        increment,
    ],
)

print(function_results)

# The functions are stored as data in a list.

# =============================================================================
# 58. Dictionary of Functions
# =============================================================================


def multiply_by_two(
    number: int,
) -> int:
    """
    Multiply by two.
    """
    return number * 2


def divide_by_two(
    number: int,
) -> int:
    """
    Divide by two using integer division.
    """
    return number // 2


operations: dict[str, Callable[[int], int]] = {
    "square": square,
    "double": multiply_by_two,
    "half": divide_by_two,
}

selected_operation: Callable[[int], int] = operations[
    "square"
]

dictionary_operation_result: int = selected_operation(
    6,
)

print(dictionary_operation_result)

# Functions can be stored as dictionary values.
#
# This can be useful for command dispatch and strategy selection.

# =============================================================================
# 59. Command Dispatch
# =============================================================================


def command_start() -> str:
    """
    Execute the start command.
    """
    return "Application started."


def command_stop() -> str:
    """
    Execute the stop command.
    """
    return "Application stopped."


def command_status() -> str:
    """
    Execute the status command.
    """
    return "Application is running."


commands: dict[str, Callable[[], str]] = {
    "start": command_start,
    "stop": command_stop,
    "status": command_status,
}

command_name: str = "status"

command_function: Callable[[], str] = commands[
    command_name
]

command_result: str = command_function()

print(command_result)

# This avoids a long chain of if/elif statements.

# =============================================================================
# 60. Strategy Pattern With Functions
# =============================================================================


def calculate_total_with_strategy(
    values: list[int],
    strategy: Callable[[list[int]], int],
) -> int:
    """
    Calculate a result using a supplied strategy.
    """
    return strategy(values)


def total_sum(
    values: list[int],
) -> int:
    """
    Calculate the sum of values.
    """
    return sum(values)


def total_maximum(
    values: list[int],
) -> int:
    """
    Calculate the maximum value.
    """
    return max(values)


strategy_values: list[int] = [
    10,
    20,
    30,
]

sum_result: int = calculate_total_with_strategy(
    strategy_values,
    total_sum,
)

maximum_result: int = calculate_total_with_strategy(
    strategy_values,
    total_maximum,
)

print(sum_result)
print(maximum_result)

# The calculation function does not need to know which strategy is used.

# =============================================================================
# 61. Higher-Order Function for Retry-Like Behaviour
# =============================================================================


def execute_multiple_times(
    function: Callable[[], str],
    times: int,
) -> list[str]:
    """
    Execute a function multiple times.
    """
    results: list[str] = []

    for _ in range(times):
        results.append(
            function(),
        )

    return results


def get_status_message() -> str:
    """
    Return a status message.
    """
    return "OK"


status_messages: list[str] = execute_multiple_times(
    get_status_message,
    3,
)

print(status_messages)

# =============================================================================
# 62. Higher-Order Function for Conditional Execution
# =============================================================================


def execute_if(
    condition: bool,
    function: Callable[[], str],
) -> str | None:
    """
    Execute a function only when condition is true.
    """
    if condition:
        return function()

    return None


conditional_result: str | None = execute_if(
    True,
    get_status_message,
)

print(conditional_result)

# =============================================================================
# 63. Higher-Order Function With Optional Callback
# =============================================================================


def process_number_with_callback(
    number: int,
    callback: Callable[[int], int] | None = None,
) -> int:
    """
    Process a number and optionally apply a callback.
    """
    result: int = number * 2

    if callback is not None:
        result = callback(result)

    return result


callback_processing_result: int = process_number_with_callback(
    5,
    square,
)

print(callback_processing_result)

# =============================================================================
# 64. Callback Without Optional Value
# =============================================================================

normal_processing_result: int = process_number_with_callback(
    5,
)

print(normal_processing_result)

# =============================================================================
# 65. Higher-Order Function With Generic Type Variables
# =============================================================================
"""
Higher-order functions can be made more reusable with generic type
annotations.

TypeVar allows the input and output relationships to be expressed.

Example concept:

    T = TypeVar("T")

    def apply(
        function: Callable[[T], T],
        value: T,
    ) -> T:
        return function(value)
"""

# =============================================================================
# 66. Generic Identity Function
# =============================================================================

from typing import TypeVar


T = TypeVar("T")


def apply_identity(
    function: Callable[[T], T],
    value: T,
) -> T:
    """
    Apply a function that preserves the value type.
    """
    return function(value)


identity_text: str = apply_identity(
    lambda text: text.upper(),
    "python",
)

identity_number: int = apply_identity(
    lambda number: number + 1,
    10,
)

print(identity_text)
print(identity_number)

# =============================================================================
# 67. Generic Transformation
# =============================================================================

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


def transform(
    value: InputT,
    function: Callable[[InputT], OutputT],
) -> OutputT:
    """
    Transform a value using a supplied function.
    """
    return function(value)


transformed_text: int = transform(
    "Python",
    len,
)

transformed_number: str = transform(
    100,
    str,
)

print(transformed_text)
print(transformed_number)

# The input and output types can be different.
#
# str -> int
#
# int -> str

# =============================================================================
# 68. Generic map-Like Function
# =============================================================================


def transform_all(
    values: list[InputT],
    function: Callable[[InputT], OutputT],
) -> list[OutputT]:
    """
    Transform every item in a list.
    """
    results: list[OutputT] = []

    for value in values:
        results.append(
            function(value),
        )

    return results


text_lengths: list[int] = transform_all(
    [
        "Python",
        "Go",
        "Java",
    ],
    len,
)

print(text_lengths)

# =============================================================================
# 69. Generic Filter-Like Function
# =============================================================================


def select_values(
    values: list[InputT],
    predicate: Callable[[InputT], bool],
) -> list[InputT]:
    """
    Select values that satisfy a predicate.
    """
    results: list[InputT] = []

    for value in values:
        if predicate(value):
            results.append(value)

    return results


long_words: list[str] = select_values(
    [
        "Python",
        "Go",
        "Programming",
    ],
    lambda word: len(word) > 4,
)

print(long_words)

# =============================================================================
# 70. Function Composition With Different Types
# =============================================================================


def compose_text_length(
    formatter: Callable[[str], str],
    converter: Callable[[str], int],
) -> Callable[[str], int]:
    """
    Compose a text formatter and a length converter.
    """

    def composed(
        text: str,
    ) -> int:
        """
        Format text and return its length.
        """
        formatted: str = formatter(text)

        return converter(formatted)

    return composed


formatted_length = compose_text_length(
    str.upper,
    len,
)

formatted_length_result: int = formatted_length(
    "python",
)

print(formatted_length_result)

# =============================================================================
# 71. Higher-Order Function Versus Normal Function
# =============================================================================
"""
Normal function:

    def square(
        number: int,
    ) -> int:
        return number ** 2

It receives a value.

Higher-order function:

    def apply(
        function,
        value,
    ):
        return function(value)

It receives a function.

The important difference is that a higher-order function operates on
functions as values.
"""

# =============================================================================
# 72. Function as Data
# =============================================================================


def operation_a(
    value: int,
) -> int:
    """
    Add five.
    """
    return value + 5


def operation_b(
    value: int,
) -> int:
    """
    Multiply by five.
    """
    return value * 5


function_list: list[Callable[[int], int]] = [
    operation_a,
    operation_b,
]

for function in function_list:
    print(
        function(10),
    )

# Functions can be treated like other values.

# =============================================================================
# 73. Higher-Order Function for Sorting Records
# =============================================================================


records: list[dict[str, object]] = [
    {
        "name": "Alice",
        "age": 30,
    },
    {
        "name": "Bob",
        "age": 25,
    },
    {
        "name": "Charlie",
        "age": 35,
    },
]


def get_age(
    record: dict[str, object],
) -> object:
    """
    Return the age from a record.
    """
    return record["age"]


records_by_age: list[dict[str, object]] = sorted(
    records,
    key=get_age,
)

print(records_by_age)

# =============================================================================
# 74. Higher-Order Function for Custom Searching
# =============================================================================


def find_first(
    values: list[InputT],
    predicate: Callable[[InputT], bool],
) -> InputT | None:
    """
    Return the first value satisfying predicate.
    """
    for value in values:
        if predicate(value):
            return value

    return None


first_even: int | None = find_first(
    [
        1,
        3,
        5,
        8,
        10,
    ],
    is_even,
)

print(first_even)

# =============================================================================
# 75. Higher-Order Function for Counting
# =============================================================================


def count_matching(
    values: list[InputT],
    predicate: Callable[[InputT], bool],
) -> int:
    """
    Count values satisfying a predicate.
    """
    count: int = 0

    for value in values:
        if predicate(value):
            count += 1

    return count


even_count: int = count_matching(
    [
        1,
        2,
        3,
        4,
        5,
        6,
    ],
    is_even,
)

print(even_count)

# =============================================================================
# 76. Higher-Order Function for Partitioning
# =============================================================================


def partition_values(
    values: list[InputT],
    predicate: Callable[[InputT], bool],
) -> tuple[list[InputT], list[InputT]]:
    """
    Split values into matching and non-matching groups.
    """
    matching: list[InputT] = []
    non_matching: list[InputT] = []

    for value in values:
        if predicate(value):
            matching.append(value)
        else:
            non_matching.append(value)

    return matching, non_matching


even_values, odd_values = partition_values(
    [
        1,
        2,
        3,
        4,
        5,
        6,
    ],
    is_even,
)

print(even_values)
print(odd_values)

# =============================================================================
# 77. Higher-Order Function for Repeated Transformation
# =============================================================================


def repeat_function(
    function: Callable[[int], int],
    value: int,
    times: int,
) -> int:
    """
    Apply a function repeatedly.
    """
    result: int = value

    for _ in range(times):
        result = function(result)

    return result


repeated_increment: int = repeat_function(
    increment,
    0,
    5,
)

print(repeated_increment)

# Execution:
#
#     0
#     ↓
#     1
#     ↓
#     2
#     ↓
#     3
#     ↓
#     4
#     ↓
#     5

# =============================================================================
# 78. Repeated Function With Different Operations
# =============================================================================


repeated_double: int = repeat_function(
    double,
    1,
    4,
)

print(repeated_double)

# Execution:
#
#     1
#     ↓
#     2
#     ↓
#     4
#     ↓
#     8
#     ↓
#     16

# =============================================================================
# 79. Higher-Order Function for Conditional Transformation
# =============================================================================


def transform_if(
    value: InputT,
    condition: Callable[[InputT], bool],
    transformation: Callable[[InputT], OutputT],
) -> InputT | OutputT:
    """
    Transform a value only when a condition is satisfied.
    """
    if condition(value):
        return transformation(value)

    return value


conditional_transformation: int | str = transform_if(
    10,
    is_even,
    lambda number: number * 100,
)

print(conditional_transformation)

# =============================================================================
# 80. Higher-Order Function for Default Behaviour
# =============================================================================


def execute_or_default(
    function: Callable[[], str],
    default: str,
) -> str:
    """
    Execute a function and return its result.
    """
    result: str = function()

    if result:
        return result

    return default


default_execution_result: str = execute_or_default(
    get_status_message,
    "No status available.",
)

print(default_execution_result)

# =============================================================================
# 81. Higher-Order Function for Formatting
# =============================================================================


def format_items(
    values: list[int],
    formatter: Callable[[int], str],
) -> list[str]:
    """
    Format every integer using a formatter.
    """
    results: list[str] = []

    for value in values:
        results.append(
            formatter(value),
        )

    return results


formatted_numbers: list[str] = format_items(
    [
        10,
        20,
        30,
    ],
    lambda number: f"Value={number}",
)

print(formatted_numbers)

# =============================================================================
# 82. Higher-Order Function for Data Processing
# =============================================================================


def process_data(
    values: list[int],
    transformer: Callable[[int], int],
    predicate: Callable[[int], bool],
) -> list[int]:
    """
    Filter values and then transform the selected values.
    """
    results: list[int] = []

    for value in values:
        if predicate(value):
            results.append(
                transformer(value),
            )

    return results


processed_data: list[int] = process_data(
    [
        1,
        2,
        3,
        4,
        5,
    ],
    square,
    is_even,
)

print(processed_data)

# Processing:
#
#     filter even numbers
#         ↓
#     2, 4
#         ↓
#     square
#         ↓
#     4, 16

# =============================================================================
# 83. Higher-Order Function With Configuration
# =============================================================================


def create_range_validator(
    minimum: int,
    maximum: int,
) -> Callable[[int], bool]:
    """
    Create a validator for an integer range.
    """

    def validate(
        value: int,
    ) -> bool:
        """
        Check whether value is inside the configured range.
        """
        return minimum <= value <= maximum

    return validate


validate_age = create_range_validator(
    18,
    60,
)

valid_age: bool = validate_age(
    30,
)

invalid_age: bool = validate_age(
    70,
)

print(valid_age)
print(invalid_age)

# =============================================================================
# 84. Higher-Order Function for Access Control
# =============================================================================


def create_permission_checker(
    required_role: str,
) -> Callable[[str], bool]:
    """
    Create a role-checking function.
    """

    def check_role(
        user_role: str,
    ) -> bool:
        """
        Check whether the user has the required role.
        """
        return user_role == required_role

    return check_role


is_admin = create_permission_checker(
    "admin",
)

admin_access: bool = is_admin(
    "admin",
)

user_access: bool = is_admin(
    "user",
)

print(admin_access)
print(user_access)

# =============================================================================
# 85. Higher-Order Function for Prefixing
# =============================================================================


def create_prefixer(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a function that adds a prefix.
    """

    def prefix_text(
        text: str,
    ) -> str:
        """
        Add the captured prefix.
        """
        return f"{prefix}{text}"

    return prefix_text


python_prefixer = create_prefixer(
    "Python: ",
)

prefixed_text: str = python_prefixer(
    "Higher-order functions",
)

print(prefixed_text)

# =============================================================================
# 86. Higher-Order Function and Decorator Concept
# =============================================================================
"""
A decorator is a specialized higher-order function.

A decorator typically:

    1. receives a function
    2. creates a wrapper function
    3. returns the wrapper

Conceptually:

    def decorator(function):
        def wrapper():
            ...
            function()
            ...
        return wrapper

Therefore decorators are built directly on higher-order function concepts.
"""

# =============================================================================
# 87. Basic Decorator-Like Higher-Order Function
# =============================================================================


def add_logging(
    function: Callable[[], str],
) -> Callable[[], str]:
    """
    Wrap a zero-argument function with logging.
    """

    def wrapper() -> str:
        """
        Execute the wrapped function with logging.
        """
        print(
            "Starting function.",
        )

        result: str = function()

        print(
            "Finished function.",
        )

        return result

    return wrapper


def get_message() -> str:
    """
    Return a message.
    """
    return "Hello!"


logged_function = add_logging(
    get_message,
)

logged_message: str = logged_function()

print(logged_message)

# =============================================================================
# 88. Higher-Order Function With *args and **kwargs
# =============================================================================


def execute_function(
    function: Callable[..., OutputT],
    *args: object,
    **kwargs: object,
) -> OutputT:
    """
    Execute a supplied function with arbitrary arguments.
    """
    return function(
        *args,
        **kwargs,
    )


executed_result: int = execute_function(
    add,
    10,
    20,
)

print(executed_result)

# Callable[..., OutputT] means the function can accept arbitrary arguments
# and returns OutputT.

# =============================================================================
# 89. Higher-Order Function for Safe Execution
# =============================================================================


def safe_execute(
    function: Callable[[], OutputT],
    fallback: OutputT,
) -> OutputT:
    """
    Execute a function and return fallback on an exception.
    """
    try:
        return function()
    except Exception:
        return fallback


safe_result: str = safe_execute(
    get_status_message,
    "Fallback",
)

print(safe_result)

# =============================================================================
# 90. Higher-Order Function for Comparison
# =============================================================================


def compare_values(
    first: int,
    second: int,
    comparator: Callable[[int, int], bool],
) -> bool:
    """
    Compare two values using a supplied comparator.
    """
    return comparator(
        first,
        second,
    )


greater_than: Callable[[int, int], bool] = (
    lambda first, second: first > second
)

less_than: Callable[[int, int], bool] = (
    lambda first, second: first < second
)

greater_result: bool = compare_values(
    10,
    5,
    greater_than,
)

less_result: bool = compare_values(
    10,
    5,
    less_than,
)

print(greater_result)
print(less_result)

# =============================================================================
# 91. Higher-Order Function for Custom Ordering
# =============================================================================


def choose_larger(
    first: int,
    second: int,
    selector: Callable[[int, int], int],
) -> int:
    """
    Select a value using a supplied selector.
    """
    return selector(
        first,
        second,
    )


larger_value: int = choose_larger(
    10,
    20,
    max,
)

smaller_value: int = choose_larger(
    10,
    20,
    min,
)

print(larger_value)
print(smaller_value)

# max and min themselves can receive or operate with callable behaviour
# through their key parameter, and here they are also passed as functions.

# =============================================================================
# 92. Higher-Order Function With Built-in str Functions
# =============================================================================


def transform_text(
    text: str,
    transformer: Callable[[str], str],
) -> str:
    """
    Transform text using a supplied function.
    """
    return transformer(text)


upper_text: str = transform_text(
    "hello",
    str.upper,
)

lower_text: str = transform_text(
    "HELLO",
    str.lower,
)

print(upper_text)
print(lower_text)

# Methods such as str.upper and str.lower can also be used as function
# objects.

# =============================================================================
# 93. Higher-Order Function With Method References
# =============================================================================


def apply_string_method(
    text: str,
    method: Callable[[str], str],
) -> str:
    """
    Apply a string transformation.
    """
    return method(text)


method_result: str = apply_string_method(
    "python",
    str.title,
)

print(method_result)

# =============================================================================
# 94. Function Pipeline With Strings
# =============================================================================


def clean_text(
    text: str,
) -> str:
    """
    Remove surrounding whitespace.
    """
    return text.strip()


def uppercase(
    text: str,
) -> str:
    """
    Convert text to uppercase.
    """
    return text.upper()


def add_period(
    text: str,
) -> str:
    """
    Add a period.
    """
    return f"{text}."


def apply_text_pipeline(
    text: str,
    functions: list[Callable[[str], str]],
) -> str:
    """
    Apply string functions sequentially.
    """
    result: str = text

    for function in functions:
        result = function(result)

    return result


pipeline_text: str = apply_text_pipeline(
    "  hello python  ",
    [
        clean_text,
        uppercase,
        add_period,
    ],
)

print(pipeline_text)

# =============================================================================
# 95. Higher-Order Function for Event Handling
# =============================================================================


def handle_event(
    event_name: str,
    handler: Callable[[str], str],
) -> str:
    """
    Process an event with a handler.
    """
    return handler(event_name)


def format_event(
    event_name: str,
) -> str:
    """
    Format an event name.
    """
    return f"Event received: {event_name}"


event_result: str = handle_event(
    "LOGIN",
    format_event,
)

print(event_result)

# =============================================================================
# 96. Higher-Order Function for Dependency Injection
# =============================================================================
"""
Passing a function into another function is a simple form of dependency
injection.

Instead of hard-coding behaviour:

    def process():
        save_to_database()

we can provide the behaviour:

    def process(
        saver,
    ):
        saver()

This makes the function easier to test and reuse.
"""

# =============================================================================
# 97. Simple Dependency Injection
# =============================================================================


def save_to_database() -> str:
    """
    Simulate saving to a database.
    """
    return "Saved to database."


def save_to_file() -> str:
    """
    Simulate saving to a file.
    """
    return "Saved to file."


def save_data(
    saver: Callable[[], str],
) -> str:
    """
    Save data using the supplied strategy.
    """
    return saver()


database_result: str = save_data(
    save_to_database,
)

file_result: str = save_data(
    save_to_file,
)

print(database_result)
print(file_result)

# =============================================================================
# 98. Higher-Order Functions Improve Reusability
# =============================================================================
"""
Without higher-order functions, separate functions might be needed for:

    - square every number
    - double every number
    - increment every number
    - cube every number

With a higher-order function:

    apply_to_all()

the iteration logic is written once.

Only the transformation changes.

This is a major reason higher-order functions are useful.
"""

# =============================================================================
# 99. Separation of Concerns
# =============================================================================
"""
Higher-order functions allow two concerns to be separated.

Example:

    process_data()

can handle:

    - iteration
    - control flow
    - result collection

while a callback can handle:

    - the actual transformation
    - validation
    - formatting
    - comparison

This separation can make code easier to maintain.
"""

# =============================================================================
# 100. Higher-Order Function With a Predicate and Transformer
# =============================================================================


def select_and_transform(
    values: list[InputT],
    predicate: Callable[[InputT], bool],
    transformer: Callable[[InputT], OutputT],
) -> list[OutputT]:
    """
    Select values using a predicate and transform them.
    """
    results: list[OutputT] = []

    for value in values:
        if predicate(value):
            results.append(
                transformer(value),
            )

    return results


selected_and_transformed: list[str] = select_and_transform(
    [
        1,
        2,
        3,
        4,
        5,
    ],
    is_even,
    lambda number: f"Even: {number}",
)

print(selected_and_transformed)

# =============================================================================
# 101. Higher-Order Function With Multiple Transformations
# =============================================================================


def transform_many(
    value: InputT,
    functions: list[Callable[[InputT], InputT]],
) -> InputT:
    """
    Apply multiple transformations of the same type.
    """
    result: InputT = value

    for function in functions:
        result = function(result)

    return result


same_type_result: int = transform_many(
    10,
    [
        lambda number: number + 5,
        lambda number: number * 2,
        lambda number: number - 10,
    ],
)

print(same_type_result)

# =============================================================================
# 102. Higher-Order Functions Can Be Nested
# =============================================================================


def create_outer_function() -> Callable[[int], int]:
    """
    Return a function that itself uses another function.
    """

    def outer_function(
        value: int,
    ) -> int:
        """
        Apply a transformation.
        """

        def inner_function(
            number: int,
        ) -> int:
            """
            Double the supplied number.
            """
            return number * 2

        return inner_function(value)

    return outer_function


nested_higher_order_result: int = create_outer_function()(
    10,
)

print(nested_higher_order_result)

# Multiple levels of functions can participate in higher-order behaviour.

# =============================================================================
# 103. Higher-Order Function and Closure State
# =============================================================================


def create_accumulator(
    initial: int,
) -> Callable[[int], int]:
    """
    Create an accumulator using enclosing state.
    """
    total: int = initial

    def add_to_total(
        value: int,
    ) -> int:
        """
        Add value to the captured total.
        """
        nonlocal total

        total += value

        return total

    return add_to_total


accumulator = create_accumulator(
    100,
)

accumulated_value_1: int = accumulator(
    10,
)

accumulated_value_2: int = accumulator(
    20,
)

accumulated_value_3: int = accumulator(
    30,
)

print(accumulated_value_1)
print(accumulated_value_2)
print(accumulated_value_3)

# This example combines:
#
#     - higher-order functions
#     - returning functions
#     - closures
#     - nonlocal state

# =============================================================================
# 104. Higher-Order Function With Independent Closures
# =============================================================================


first_accumulator = create_accumulator(
    0,
)

second_accumulator = create_accumulator(
    100,
)

first_accumulator_result: int = first_accumulator(
    10,
)

second_accumulator_result: int = second_accumulator(
    10,
)

print(first_accumulator_result)
print(second_accumulator_result)

# Each returned function has independent enclosing state.

# =============================================================================
# 105. map() Versus a for Loop
# =============================================================================
"""
Using a for loop:

    squared = []

    for number in numbers:
        squared.append(
            square(number),
        )

Using map():

    squared = list(
        map(
            square,
            numbers,
        ),
    )

Both are valid.

The choice depends on readability and the complexity of the transformation.

For simple transformations, map() can be concise.

For complicated logic, a normal for loop can sometimes be clearer.
"""

# =============================================================================
# 106. filter() Versus a for Loop
# =============================================================================
"""
Using a for loop:

    even_numbers = []

    for number in numbers:
        if is_even(number):
            even_numbers.append(number)

Using filter():

    even_numbers = list(
        filter(
            is_even,
            numbers,
        ),
    )

Both approaches are valid.

Choose the form that communicates the intent most clearly.
"""

# =============================================================================
# 107. Lambda Functions and Higher-Order Functions
# =============================================================================
"""
Lambda functions are frequently used with higher-order functions.

Examples:

    map()
    filter()
    sorted()
    min()
    max()

Example:

    numbers = [1, 2, 3]

    result = list(
        map(
            lambda number: number * 2,
            numbers,
        ),
    )

The lambda is a function object.

map() receives and executes that function.
"""

# =============================================================================
# 108. Higher-Order Functions and Readability
# =============================================================================
"""
Higher-order functions are powerful, but they should not be used simply
because they are available.

Prefer straightforward code when it is clearer.

For example:

    total = 0

    for number in numbers:
        total += number

may be clearer than an unnecessarily complicated reduce() expression.

The goal is:

    readable
    reusable
    maintainable
    predictable

code.
"""

# =============================================================================
# 109. Common Mistake: Calling Instead of Passing
# =============================================================================
"""
When passing a function as an argument, pass the function object.

Correct:

    apply_function(
        square,
        5,
    )

Incorrect:

    apply_function(
        square(5),
        5,
    )

Why?

square:

    function object

square(5):

    result of calling the function

Higher-order functions generally need the function object itself.
"""

# =============================================================================
# 110. Passing a Function Correctly
# =============================================================================


correct_function_result: int = apply_function(
    square,
    5,
)

print(correct_function_result)

# =============================================================================
# 111. Common Mistake: Calling a Callback Too Early
# =============================================================================
"""
Suppose:

    def execute(
        callback,
    ):
        return callback()

The caller should provide:

    execute(
        get_status_message,
    )

not:

    execute(
        get_status_message(),
    )

The second expression calls the function immediately and passes its result.
"""

# =============================================================================
# 112. Function Object Versus Function Result
# =============================================================================


function_object = square

function_result: int = square(
    5,
)

print(function_object)
print(function_result)

# function_object:
#
#     refers to the function
#
# function_result:
#
#     contains the returned value

# =============================================================================
# 113. Higher-Order Functions and Immutability
# =============================================================================
"""
Higher-order functions often work especially well with functions that:

    - accept input
    - return output
    - avoid hidden state
    - avoid unexpected side effects

For example:

    def square(number):
        return number ** 2

This makes the function easy to pass to:

    map()
    apply_to_all()
    transform()
    pipelines
"""

# =============================================================================
# 114. Pure Transformation Example
# =============================================================================


def add_tax(
    price: float,
) -> float:
    """
    Add eighteen percent tax.
    """
    return price * 1.18


prices: list[float] = [
    100.0,
    200.0,
    300.0,
]

prices_with_tax: list[float] = list(
    map(
        add_tax,
        prices,
    ),
)

print(prices_with_tax)

# =============================================================================
# 115. Higher-Order Function for Price Processing
# =============================================================================


def process_prices(
    prices: list[float],
    transformation: Callable[[float], float],
) -> list[float]:
    """
    Apply a price transformation.
    """
    return [
        transformation(price)
        for price in prices
    ]


discounted_prices: list[float] = process_prices(
    prices,
    lambda price: price * 0.90,
)

taxed_prices: list[float] = process_prices(
    prices,
    add_tax,
)

print(discounted_prices)
print(taxed_prices)

# =============================================================================
# 116. Higher-Order Function for User Data
# =============================================================================


user_names: list[str] = [
    "alice",
    "bob",
    "charlie",
]


def normalize_name(
    name: str,
) -> str:
    """
    Normalize a user name.
    """
    return name.strip().title()


normalized_names: list[str] = list(
    map(
        normalize_name,
        user_names,
    ),
)

print(normalized_names)

# =============================================================================
# 117. Higher-Order Function for Validation
# =============================================================================


user_name_valid: list[str] = list(
    filter(
        lambda name: len(name) >= 4,
        user_names,
    ),
)

print(user_name_valid)

# =============================================================================
# 118. Higher-Order Function for Sorting Names
# =============================================================================


names_by_length: list[str] = sorted(
    user_names,
    key=len,
)

print(names_by_length)

# =============================================================================
# 119. Complete Data Pipeline
# =============================================================================


def normalize(
    text: str,
) -> str:
    """
    Normalize text.
    """
    return text.strip().lower()


def is_long_enough(
    text: str,
) -> bool:
    """
    Check whether text contains at least five characters.
    """
    return len(text) >= 5


def format_name_value(
    text: str,
) -> str:
    """
    Format a normalized name.
    """
    return text.title()


raw_names: list[str] = [
    "  alice  ",
    "bob",
    "  charlie ",
    "dave",
    "  emily ",
]

normalized_name_values: list[str] = list(
    map(
        normalize,
        raw_names,
    ),
)

long_name_values: list[str] = list(
    filter(
        is_long_enough,
        normalized_name_values,
    ),
)

formatted_name_values: list[str] = list(
    map(
        format_name_value,
        long_name_values,
    ),
)

print(formatted_name_values)

# Pipeline:
#
#     raw data
#         ↓
#     normalize
#         ↓
#     filter
#         ↓
#     format
#         ↓
#     final data

# =============================================================================
# 120. Custom Pipeline Function
# =============================================================================


def string_pipeline(
    values: list[str],
    transformations: list[Callable[[str], str]],
) -> list[str]:
    """
    Apply a sequence of string transformations to every value.
    """
    results: list[str] = []

    for value in values:
        result: str = value

        for transformation in transformations:
            result = transformation(result)

        results.append(result)

    return results


pipeline_names: list[str] = string_pipeline(
    [
        "  alice  ",
        "  bob  ",
        "  charlie  ",
    ],
    [
        str.strip,
        str.lower,
        str.title,
    ],
)

print(pipeline_names)

# =============================================================================
# 121. Higher-Order Functions and Testability
# =============================================================================
"""
Higher-order functions can improve testing because behaviour can be
supplied from outside.

For example:

    def process(
        operation,
    ):
        return operation(10)

A test can provide a simple test operation.

This reduces hard-coded dependencies.
"""

# =============================================================================
# 122. Simple Test Operation
# =============================================================================


def test_operation(
    value: int,
) -> int:
    """
    Provide predictable test behaviour.
    """
    return value + 100


testable_result: int = apply_function(
    test_operation,
    10,
)

print(testable_result)

# =============================================================================
# 123. Higher-Order Function With Side Effects
# =============================================================================
"""
Higher-order functions can also accept functions that perform side effects.

Example:

    print_message()

can be passed to another function.

However, side effects should be intentional.

Prefer clear function contracts.

"""

# =============================================================================
# 124. Side-Effect Callback
# =============================================================================


def print_value(
    value: int,
) -> None:
    """
    Print a value.
    """
    print(
        f"Value: {value}",
    )


def process_with_side_effect(
    value: int,
    callback: Callable[[int], None],
) -> None:
    """
    Process a value with a side-effect callback.
    """
    callback(value)


process_with_side_effect(
    100,
    print_value,
)

# =============================================================================
# 125. Higher-Order Function With None Return Type
# =============================================================================


def run_action(
    action: Callable[[], None],
) -> None:
    """
    Execute an action that returns None.
    """
    action()


def display_message() -> None:
    """
    Display a message.
    """
    print(
        "Action executed.",
    )


run_action(
    display_message,
)

# =============================================================================
# 126. Higher-Order Function for Event Registration Concept
# =============================================================================


def register_handler(
    handler: Callable[[str], None],
) -> Callable[[str], None]:
    """
    Return the supplied event handler.
    """

    def wrapped_handler(
        event: str,
    ) -> None:
        """
        Execute the registered handler.
        """
        print(
            "Handling event.",
        )

        handler(event)

    return wrapped_handler


def event_handler(
    event: str,
) -> None:
    """
    Handle an event.
    """
    print(
        f"Received: {event}",
    )


registered_handler = register_handler(
    event_handler,
)

registered_handler(
    "LOGIN",
)

# =============================================================================
# 127. Higher-Order Functions and Abstraction
# =============================================================================
"""
A higher-order function can abstract an algorithm while allowing the
caller to supply the specific behaviour.

For example:

    process_values()

can define:

    - iteration
    - ordering
    - control flow

while a callback defines:

    - transformation
    - validation
    - comparison

This is a form of behavioural abstraction.
"""

# =============================================================================
# 128. Algorithm With Injected Behaviour
# =============================================================================


def find_best(
    values: list[int],
    comparison: Callable[[int, int], bool],
) -> int | None:
    """
    Find the best value using a comparison function.
    """
    if not values:
        return None

    best: int = values[0]

    for value in values[1:]:
        if comparison(
            value,
            best,
        ):
            best = value

    return best


maximum_value: int | None = find_best(
    [
        5,
        10,
        3,
        20,
    ],
    lambda first, second: first > second,
)

minimum_value: int | None = find_best(
    [
        5,
        10,
        3,
        20,
    ],
    lambda first, second: first < second,
)

print(maximum_value)
print(minimum_value)

# The algorithm is the same.
#
# Only the comparison behaviour changes.

# =============================================================================
# 129. Higher-Order Function for Grouping
# =============================================================================


def group_by(
    values: list[InputT],
    key_function: Callable[[InputT], str],
) -> dict[str, list[InputT]]:
    """
    Group values according to a key function.
    """
    groups: dict[str, list[InputT]] = {}

    for value in values:
        key: str = key_function(value)

        if key not in groups:
            groups[key] = []

        groups[key].append(value)

    return groups


grouped_words: dict[str, list[str]] = group_by(
    [
        "apple",
        "ant",
        "banana",
        "boat",
        "cat",
    ],
    lambda word: word[0],
)

print(grouped_words)

# =============================================================================
# 130. Higher-Order Function for Mapping Dictionaries
# =============================================================================


def map_records(
    records_to_map: list[dict[str, object]],
    mapper: Callable[[dict[str, object]], dict[str, object]],
) -> list[dict[str, object]]:
    """
    Transform records using a mapper function.
    """
    return [
        mapper(record)
        for record in records_to_map
    ]


mapped_records: list[dict[str, object]] = map_records(
    [
        {
            "name": "Alice",
            "age": 30,
        },
        {
            "name": "Bob",
            "age": 25,
        },
    ],
    lambda record: {
        "name": str(record["name"]).upper(),
        "age": record["age"],
    },
)

print(mapped_records)

# =============================================================================
# 131. Higher-Order Function for Filtering Dictionaries
# =============================================================================


def filter_records(
    records_to_filter: list[dict[str, object]],
    predicate: Callable[[dict[str, object]], bool],
) -> list[dict[str, object]]:
    """
    Filter records using a predicate.
    """
    return [
        record
        for record in records_to_filter
        if predicate(record)
    ]


adult_records: list[dict[str, object]] = filter_records(
    [
        {
            "name": "Alice",
            "age": 30,
        },
        {
            "name": "Bob",
            "age": 15,
        },
    ],
    lambda record: int(record["age"]) >= 18,
)

print(adult_records)

# =============================================================================
# 132. Higher-Order Function for Sorting Dictionaries
# =============================================================================


records_sorted_by_name: list[dict[str, object]] = sorted(
    [
        {
            "name": "Charlie",
            "age": 35,
        },
        {
            "name": "Alice",
            "age": 30,
        },
        {
            "name": "Bob",
            "age": 25,
        },
    ],
    key=lambda record: str(record["name"]),
)

print(records_sorted_by_name)

# =============================================================================
# 133. Higher-Order Functions Can Return Higher-Order Functions
# =============================================================================


def create_processor(
    multiplier: int,
) -> Callable[[Callable[[int], int]], Callable[[int], int]]:
    """
    Return a function that wraps another integer function.
    """

    def configure(
        function: Callable[[int], int],
    ) -> Callable[[int], int]:
        """
        Configure a function with a multiplier.
        """

        def processor(
            value: int,
        ) -> int:
            """
            Apply the supplied function and multiplier.
            """
            return function(value) * multiplier

        return processor

    return configure


configure_double = create_processor(
    2,
)

process_square = configure_double(
    square,
)

processor_result: int = process_square(
    5,
)

print(processor_result)

# This demonstrates multiple layers of higher-order behaviour.

# =============================================================================
# 134. Higher-Order Functions and Closures Together
# =============================================================================
"""
A common pattern is:

    outer function
        ↓
    creates configuration
        ↓
    returns higher-order function
        ↓
    returned function accepts another function
        ↓
    returned processor performs the operation

This pattern appears in:

    - decorators
    - middleware
    - validation frameworks
    - web frameworks
    - function factories
    - event systems
    - data processing pipelines
"""

# =============================================================================
# 135. Best Practice: Use Clear Callable Types
# =============================================================================
"""
Prefer explicit callable annotations when they improve readability.

Example:

    Callable[[int], int]

is clearer than an untyped:

    function

For complex callbacks, descriptive type aliases can also help.
"""

# =============================================================================
# 136. Callable Type Alias
# =============================================================================


IntegerOperation = Callable[[int], int]


def execute_integer_operation(
    operation: IntegerOperation,
    value: int,
) -> int:
    """
    Execute an integer operation.
    """
    return operation(value)


type_alias_result: int = execute_integer_operation(
    square,
    7,
)

print(type_alias_result)

# =============================================================================
# 137. Callable Type Alias for Predicates
# =============================================================================


IntegerPredicate = Callable[[int], bool]


def check_integer(
    value: int,
    predicate: IntegerPredicate,
) -> bool:
    """
    Check an integer using a predicate.
    """
    return predicate(value)


predicate_result: bool = check_integer(
    20,
    is_even,
)

print(predicate_result)

# =============================================================================
# 138. Callable Type Alias for String Transformers
# =============================================================================


StringTransformer = Callable[[str], str]


def transform_string(
    value: str,
    transformer: StringTransformer,
) -> str:
    """
    Transform a string.
    """
    return transformer(value)


string_transform_result: str = transform_string(
    "python",
    str.upper,
)

print(string_transform_result)

# =============================================================================
# 139. Higher-Order Functions and Explicit Return Types
# =============================================================================


def make_incrementer(
    amount: int,
) -> Callable[[int], int]:
    """
    Return a function that increments by amount.
    """

    def increment_by_amount(
        value: int,
    ) -> int:
        """
        Increment a value.
        """
        return value + amount

    return increment_by_amount


increment_by_five = make_incrementer(
    5,
)

increment_by_five_result: int = increment_by_five(
    10,
)

print(increment_by_five_result)

# =============================================================================
# 140. Higher-Order Functions and Variable Capture
# =============================================================================


def create_offset_function(
    offset: int,
) -> Callable[[int], int]:
    """
    Create a function that remembers offset.
    """

    def add_offset(
        value: int,
    ) -> int:
        """
        Add the captured offset.
        """
        return value + offset

    return add_offset


add_ten_function = create_offset_function(
    10,
)

add_twenty_function = create_offset_function(
    20,
)

offset_ten_result: int = add_ten_function(
    100,
)

offset_twenty_result: int = add_twenty_function(
    100,
)

print(offset_ten_result)
print(offset_twenty_result)

# =============================================================================
# 141. Common Mistake: Confusing Function With Result
# =============================================================================
"""
Remember:

    function
        ↓
    callable object

while:

    function()
        ↓
    function result

For higher-order functions, the distinction is critical.

Pass:

    square

when another function expects:

    Callable[[int], int]

Do not pass:

    square(5)

because square(5) is an int.
"""

# =============================================================================
# 142. Common Mistake: Wrong Callback Signature
# =============================================================================
"""
If a function expects:

    Callable[[int], int]

the supplied function should accept one int and return an int.

Correct:

    def square(
        number: int,
    ) -> int:
        return number ** 2

Incorrect conceptually:

    def greet(
        name: str,
    ) -> str:
        return f"Hello {name}"

The signatures do not match.
"""

# =============================================================================
# 143. Common Mistake: Forgetting to Return the Function
# =============================================================================


def create_correct_function() -> Callable[[int], int]:
    """
    Correctly return a nested function.
    """

    def operation(
        value: int,
    ) -> int:
        """
        Double a value.
        """
        return value * 2

    return operation


correct_function = create_correct_function()

correct_function_result: int = correct_function(
    10,
)

print(correct_function_result)

# If the outer function forgot:
#
#     return operation
#
# the caller would receive None instead of the function.

# =============================================================================
# 144. Common Mistake: Recreating Unnecessary Functions
# =============================================================================
"""
Avoid creating a separate wrapper when an existing function already matches
the required signature.

For example:

    sorted(
        words,
        key=len,
    )

is simpler than:

    def get_length(word):
        return len(word)

    sorted(
        words,
        key=get_length,
    )

Both work, but the direct version is often clearer.
"""

# =============================================================================
# 145. Higher-Order Functions and Readable Design
# =============================================================================
"""
Use higher-order functions when they make the behaviour:

    - reusable
    - configurable
    - composable
    - testable
    - easy to understand

Avoid excessive abstraction when a simple loop or direct function call
would be easier to read.
"""

# =============================================================================
# 146. Practical Example: Number Processor
# =============================================================================


def process_numbers(
    values: list[int],
    predicate: Callable[[int], bool],
    transformer: Callable[[int], int],
) -> list[int]:
    """
    Filter and transform numbers.
    """
    selected: list[int] = [
        value
        for value in values
        if predicate(value)
    ]

    transformed: list[int] = [
        transformer(value)
        for value in selected
    ]

    return transformed


number_processing_result: list[int] = process_numbers(
    [
        1,
        2,
        3,
        4,
        5,
        6,
    ],
    is_even,
    square,
)

print(number_processing_result)

# =============================================================================
# 147. Practical Example: Text Processor
# =============================================================================


def process_text_values(
    values: list[str],
    predicate: Callable[[str], bool],
    transformer: Callable[[str], str],
) -> list[str]:
    """
    Filter and transform text values.
    """
    selected: list[str] = [
        value
        for value in values
        if predicate(value)
    ]

    transformed: list[str] = [
        transformer(value)
        for value in selected
    ]

    return transformed


text_processing_result: list[str] = process_text_values(
    [
        "python",
        "go",
        "javascript",
        "sql",
    ],
    lambda text: len(text) >= 4,
    str.upper,
)

print(text_processing_result)

# =============================================================================
# 148. Practical Example: Price Processor
# =============================================================================


def process_prices_with_rules(
    values: list[float],
    predicate: Callable[[float], bool],
    transformer: Callable[[float], float],
) -> list[float]:
    """
    Filter and transform prices.
    """
    return [
        transformer(value)
        for value in values
        if predicate(value)
    ]


price_processing_result: list[float] = process_prices_with_rules(
    [
        50.0,
        100.0,
        150.0,
        200.0,
    ],
    lambda price: price >= 100.0,
    lambda price: price * 0.90,
)

print(price_processing_result)

# =============================================================================
# 149. Practical Example: Employee Processor
# =============================================================================


employees: list[dict[str, object]] = [
    {
        "name": "Alice",
        "salary": 50000,
    },
    {
        "name": "Bob",
        "salary": 70000,
    },
    {
        "name": "Charlie",
        "salary": 90000,
    },
]


def employee_salary(
    employee: dict[str, object],
) -> int:
    """
    Return an employee salary.
    """
    return int(employee["salary"])


high_salary_employees: list[dict[str, object]] = list(
    filter(
        lambda employee: int(employee["salary"]) >= 70000,
        employees,
    ),
)

sorted_employees: list[dict[str, object]] = sorted(
    employees,
    key=employee_salary,
    reverse=True,
)

print(high_salary_employees)
print(sorted_employees)

# =============================================================================
# 150. Higher-Order Functions Core Model
# =============================================================================
"""
The core concept can be represented as:

    FUNCTION
       │
       ├───────────────┐
       ↓               ↓
   argument          return
       ↓               ↓
   function        function
       │               │
       └───────┬───────┘
               ↓
      HIGHER-ORDER FUNCTION

A higher-order function treats functions as values.

Examples:

    map()
    filter()
    sorted()
    min()
    max()
    reduce()

and custom functions such as:

    apply_function()
    transform()
    compose()
    execute_all()
    process_data()
"""

# =============================================================================
# 151. Higher-Order Functions Summary
# =============================================================================
"""
Higher-order functions:

    - accept functions as arguments
    - return functions
    - or do both

Functions are first-class objects in Python.

Therefore functions can be:

    - assigned
    - passed
    - returned
    - stored
    - composed
    - selected dynamically

Important concepts:

    Function object
        ↓
    Callable
        ↓
    Higher-order function
        ↓
    Callback
        ↓
    Function factory
        ↓
    Closure
        ↓
    Function composition
        ↓
    Pipeline
        ↓
    Decorator

Built-in higher-order functions include:

    map()
    filter()
    sorted()
    min()
    max()

reduce() from functools is also a common higher-order function.

"""

# =============================================================================
# 152. Key Takeaways
# =============================================================================
"""
✓ Functions are first-class objects in Python.

✓ A function can be assigned to a variable.

✓ A function can be passed as an argument.

✓ A function can be returned from another function.

✓ A function that accepts or returns another function is a higher-order
  function.

✓ A callback is a function supplied to another function for later execution.

✓ Callable can be used to type-annotate function parameters and returns.

✓ map() applies a function to items.

✓ filter() selects items according to a predicate.

✓ sorted() accepts a key function.

✓ min() accepts a key function.

✓ max() accepts a key function.

✓ reduce() combines values using a function.

✓ Higher-order functions allow behaviour to be passed as data.

✓ Function factories create functions dynamically.

✓ Closures allow returned functions to remember enclosing variables.

✓ Higher-order functions are useful for reusable transformations.

✓ Higher-order functions can implement pipelines.

✓ Higher-order functions can implement function composition.

✓ Higher-order functions can simplify callback-based designs.

✓ Higher-order functions can support dependency injection.

✓ Higher-order functions can improve testability.

✓ Decorators are built on higher-order function concepts.

✓ A function object is different from calling the function.

    square
        ↓
    function object

    square(5)
        ↓
    function result

✓ Prefer clear and readable higher-order abstractions.

Core model:

    function
        ↓
    passed to another function
        ↓
    callback

or:

    function
        ↓
    returns another function
        ↓
    function factory

or:

    function
        ↓
    receives function
        ↓
    processes data
        ↓
    returns result

Higher-order functions allow behaviour to become configurable instead of
hard-coded.

"""

# =============================================================================
# End of 18_higher_order_functions.py
# =============================================================================