# =============================================================================
# 17. First-Class Functions
# =============================================================================
# type: ignore

"""
Python Functions

File
----
17_first_class_functions.py

Topic
-----
First-Class Functions

Overview
--------
Python treats functions as first-class objects.

This means a function can be:

- Assigned to a variable
- Passed as an argument to another function
- Returned from another function
- Stored inside a list
- Stored inside a tuple
- Stored inside a dictionary
- Stored inside a set
- Used as a dictionary value
- Used as a dictionary key
- Assigned to multiple names
- Compared by object identity
- Stored and retrieved like other Python objects

The key idea is:

    FUNCTION
        |
        +--> assign to a variable
        |
        +--> pass to another function
        |
        +--> return from a function
        |
        +--> store in collections
        |
        +--> call later

Functions are objects in Python.

A function object can therefore be treated as data.

Topics Covered
--------------
- What first-class functions mean
- Functions are objects
- Function identity
- Assigning functions to variables
- Calling a function through another variable
- Multiple names for one function
- Passing functions as arguments
- Callback functions
- Returning functions
- Function factories
- Functions stored in lists
- Functions stored in tuples
- Functions stored in dictionaries
- Functions stored in sets
- Functions as dictionary values
- Functions as dictionary keys
- Functions inside other data structures
- Higher-order functions
- Functions that accept functions
- Functions that return functions
- Combining both behaviours
- map()
- filter()
- sorted() with key functions
- min() with key functions
- max() with key functions
- any() with generator expressions
- all() with generator expressions
- Custom higher-order functions
- Closures and first-class functions
- Function references versus function calls
- Passing arguments to callbacks
- Callable type annotations
- collections.abc.Callable
- Type aliases for callable objects
- Callback pipelines
- Strategy pattern
- Dispatch dictionaries
- Function composition
- Function decorators and first-class functions
- Practical design patterns
- Common mistakes
- Best practices
"""

# =============================================================================
# 01. What Are First-Class Functions?
# =============================================================================

"""
A first-class function is a function that can be treated like any other
ordinary value.

For example:

    def greet() -> str:
        return "Hello"

The function itself can be assigned to another variable:

    another_name = greet

Then:

    another_name()

calls the same function object.

The important distinction is:

    greet

means:

    "the function object"

while:

    greet()

means:

    "call the function and obtain its return value"

This distinction is fundamental to first-class functions.
"""

# =============================================================================
# 02. Functions Are Objects
# =============================================================================


def greet() -> str:
    """Return a greeting."""
    return "Hello"


greet_object = greet

print(
    greet_object
)

print(
    greet_object()
)

# greet is a function object.
#
# greet_object refers to the same function object.
#
# The function can therefore be stored in another variable.

# =============================================================================
# 03. Function Identity
# =============================================================================


def say_hello() -> str:
    """Return a greeting."""
    return "Hello"


hello_reference = say_hello

print(
    say_hello is hello_reference
)

# Both names refer to the same function object.
#
# Therefore:
#
# say_hello is hello_reference
#
# evaluates to:
#
# True

# =============================================================================
# 04. Assigning a Function to Another Variable
# =============================================================================


def calculate_square(
    number: int,
) -> int:
    """Return the square of a number."""
    return number ** 2


square_function = calculate_square

square_result: int = square_function(
    5,
)

print(
    square_result
)

# The assignment:
#
# square_function = calculate_square
#
# does not call the function.
#
# It stores another reference to the function object.

# =============================================================================
# 05. Function Reference Versus Function Call
# =============================================================================


def multiply_by_two(
    number: int,
) -> int:
    """Multiply a number by two."""
    return number * 2


function_reference = multiply_by_two

function_result: int = multiply_by_two(
    10,
)

reference_result: int = function_reference(
    10,
)

print(
    function_reference
)

print(
    function_result
)

print(
    reference_result
)

# Correct:
#
# function_reference = multiply_by_two
#
# This stores the function.
#
# Also correct:
#
# function_result = multiply_by_two(10)
#
# This calls the function and stores its returned value.
#
# These are different operations.

# =============================================================================
# 06. Multiple Names Can Refer to One Function
# =============================================================================


def get_message() -> str:
    """Return a message."""
    return "Python"


first_reference = get_message
second_reference = get_message
third_reference = first_reference

print(
    first_reference()
)

print(
    second_reference()
)

print(
    third_reference()
)

print(
    first_reference is second_reference
)

print(
    second_reference is third_reference
)

# All three names refer to the same function object.

# =============================================================================
# 07. Functions Can Be Passed as Arguments
# =============================================================================


def execute_function(
    function: Callable[[], str],
) -> str:
    """Execute a function supplied as an argument."""
    return function()


def create_message() -> str:
    """Return a message."""
    return "Function executed."


message_result: str = execute_function(
    create_message,
)

print(
    message_result
)

# create_message is passed without parentheses.
#
# execute_function receives the function object.
#
# execute_function then calls it.

# =============================================================================
# 08. Import Callable
# =============================================================================

from collections.abc import Callable

# Callable is useful when type-annotating parameters that contain functions.
#
# Example:
#
# Callable[[], str]
#
# means:
#
# a callable that accepts no arguments and returns str.
#
# Example:
#
# Callable[[int], int]
#
# means:
#
# a callable that accepts one int argument and returns int.

# =============================================================================
# 09. Passing a Function With Arguments
# =============================================================================


def add_ten(
    number: int,
) -> int:
    """Add ten to a number."""
    return number + 10


def apply_number_function(
    function: Callable[[int], int],
    number: int,
) -> int:
    """Apply a function to an integer."""
    return function(
        number,
    )


added_value: int = apply_number_function(
    add_ten,
    20,
)

print(
    added_value
)

# The function:
#
# add_ten
#
# is passed as data.
#
# The number:
#
# 20
#
# is passed separately.
#
# apply_number_function() eventually performs:
#
# function(number)

# =============================================================================
# 10. Callback Functions
# =============================================================================

"""
A callback is a function passed to another function so that the receiving
function can call it later.

General structure:

    def process(
        callback: Callable[[int], int],
    ) -> int:
        return callback(10)

The callback function controls what happens when process() invokes it.

Callbacks are common in:

- Event systems
- GUI programming
- Web frameworks
- Asynchronous programming
- Data processing
- Sorting
- Validation
- Custom pipelines
"""

# =============================================================================
# 11. Callback Example
# =============================================================================


def callback_double(
    number: int,
) -> int:
    """Double a number."""
    return number * 2


def run_callback(
    callback: Callable[[int], int],
) -> int:
    """Run a callback with a fixed input."""
    return callback(
        10,
    )


callback_result: int = run_callback(
    callback_double,
)

print(
    callback_result
)

# callback_double is the callback.
#
# run_callback receives it and executes it.

# =============================================================================
# 12. Multiple Callback Choices
# =============================================================================


def add_five(
    number: int,
) -> int:
    """Add five."""
    return number + 5


def subtract_five(
    number: int,
) -> int:
    """Subtract five."""
    return number - 5


def execute_operation(
    operation: Callable[[int], int],
    number: int,
) -> int:
    """Execute a supplied operation."""
    return operation(
        number,
    )


addition_result: int = execute_operation(
    add_five,
    20,
)

subtraction_result: int = execute_operation(
    subtract_five,
    20,
)

print(
    addition_result
)

print(
    subtraction_result
)

# The same function can accept different behaviours.
#
# The behaviour is supplied as a function argument.

# =============================================================================
# 13. Functions Can Be Returned From Functions
# =============================================================================


def create_greeting_function() -> Callable[[], str]:
    """Return a greeting function."""

    def greeting() -> str:
        """Return a greeting message."""
        return "Hello from the returned function."

    return greeting


returned_greeting = create_greeting_function()

returned_message: str = returned_greeting()

print(
    returned_message
)

# create_greeting_function() returns a function object.
#
# The returned function can then be stored in:
#
# returned_greeting
#
# and called later.

# =============================================================================
# 14. Returning a Function
# =============================================================================


def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """Create and return a multiplication function."""

    def multiply(
        number: int,
    ) -> int:
        """Multiply using the captured multiplier."""
        return number * multiplier

    return multiply


double_function: Callable[[int], int] = create_multiplier(
    2,
)

triple_function: Callable[[int], int] = create_multiplier(
    3,
)

double_result: int = double_function(
    10,
)

triple_result: int = triple_function(
    10,
)

print(
    double_result
)

print(
    triple_result
)

# This demonstrates two important ideas:
#
# 1. Functions are first-class objects.
#
# 2. Nested functions can form closures.
#
# double_function remembers multiplier = 2.
#
# triple_function remembers multiplier = 3.

# =============================================================================
# 15. Function Factory
# =============================================================================

"""
A function factory is a function that creates and returns another function.

Example:

    def create_multiplier(
        multiplier: int,
    ) -> Callable[[int], int]:
        def multiply(
            number: int,
        ) -> int:
            return number * multiplier

        return multiply

The outer function creates behaviour dynamically.

Examples:

    double = create_multiplier(2)
    triple = create_multiplier(3)

Each returned function has different behaviour.
"""

# =============================================================================
# 16. Functions Stored in a List
# =============================================================================


def operation_add(
    number: int,
) -> int:
    """Add one."""
    return number + 1


def operation_double(
    number: int,
) -> int:
    """Double a number."""
    return number * 2


def operation_square(
    number: int,
) -> int:
    """Square a number."""
    return number ** 2


operations: list[Callable[[int], int]] = [
    operation_add,
    operation_double,
    operation_square,
]

for operation in operations:
    operation_result: int = operation(
        5,
    )

    print(
        operation_result
    )

# A list can contain function objects.
#
# Each function can then be called through the list.

# =============================================================================
# 17. Functions Stored in a Tuple
# =============================================================================


def get_first_value(
    number: int,
) -> int:
    """Return the number unchanged."""
    return number


def get_second_value(
    number: int,
) -> int:
    """Add two to the number."""
    return number + 2


function_tuple: tuple[
    Callable[[int], int],
    Callable[[int], int],
] = (
    get_first_value,
    get_second_value,
)

tuple_result_one: int = function_tuple[0](
    10,
)

tuple_result_two: int = function_tuple[1](
    10,
)

print(
    tuple_result_one
)

print(
    tuple_result_two
)

# Tuples can store function references just like other objects.

# =============================================================================
# 18. Functions Stored in a Dictionary
# =============================================================================


def add_operation(
    first: int,
    second: int,
) -> int:
    """Add two numbers."""
    return first + second


def subtract_operation(
    first: int,
    second: int,
) -> int:
    """Subtract two numbers."""
    return first - second


def multiply_operation(
    first: int,
    second: int,
) -> int:
    """Multiply two numbers."""
    return first * second


operation_map: dict[
    str,
    Callable[[int, int], int],
] = {
    "add": add_operation,
    "subtract": subtract_operation,
    "multiply": multiply_operation,
}

add_result: int = operation_map["add"](
    10,
    5,
)

subtract_result: int = operation_map["subtract"](
    10,
    5,
)

multiply_result: int = operation_map["multiply"](
    10,
    5,
)

print(
    add_result
)

print(
    subtract_result
)

print(
    multiply_result
)

# A dictionary can act as a dispatch table.
#
# Instead of writing a large chain of if/elif statements,
# the desired function can be selected from the dictionary.

# =============================================================================
# 19. Dispatch Dictionary
# =============================================================================


def handle_start() -> str:
    """Handle a start command."""
    return "Starting."


def handle_stop() -> str:
    """Handle a stop command."""
    return "Stopping."


def handle_status() -> str:
    """Handle a status command."""
    return "Running."


command_handlers: dict[
    str,
    Callable[[], str],
] = {
    "start": handle_start,
    "stop": handle_stop,
    "status": handle_status,
}

command: str = "status"

handler: Callable[[], str] = command_handlers[command]

handler_result: str = handler()

print(
    handler_result
)

# The dictionary stores behaviour.
#
# The command selects the appropriate function.
#
# The selected function is then called.

# =============================================================================
# 20. Functions Stored in a Set
# =============================================================================


def first_function(
    value: int,
) -> int:
    """Return the value."""
    return value


def second_function(
    value: int,
) -> int:
    """Double the value."""
    return value * 2


function_set: set[Callable[[int], int]] = {
    first_function,
    second_function,
}

for function in function_set:
    function_set_result: int = function(
        5,
    )

    print(
        function_set_result
    )

# Function objects can be stored in sets.
#
# Function objects are hashable by default.

# =============================================================================
# 21. Functions as Dictionary Values
# =============================================================================


def format_upper(
    text: str,
) -> str:
    """Convert text to uppercase."""
    return text.upper()


def format_lower(
    text: str,
) -> str:
    """Convert text to lowercase."""
    return text.lower()


formatters: dict[
    str,
    Callable[[str], str],
] = {
    "upper": format_upper,
    "lower": format_lower,
}

upper_text: str = formatters["upper"](
    "Python",
)

lower_text: str = formatters["lower"](
    "Python",
)

print(
    upper_text
)

print(
    lower_text
)

# Functions can be used as values in dictionaries.

# =============================================================================
# 22. Functions as Dictionary Keys
# =============================================================================


def key_function_one() -> str:
    """Return the first key-function value."""
    return "one"


def key_function_two() -> str:
    """Return the second key-function value."""
    return "two"


function_key_map: dict[
    Callable[[], str],
    str,
] = {
    key_function_one: "First",
    key_function_two: "Second",
}

function_key_result: str = function_key_map[
    key_function_one
]

print(
    function_key_result
)

# Functions are hashable objects.
#
# Therefore a function can be used as a dictionary key.

# =============================================================================
# 23. Functions Inside Nested Collections
# =============================================================================


def nested_add(
    number: int,
) -> int:
    """Add one."""
    return number + 1


def nested_double(
    number: int,
) -> int:
    """Double a number."""
    return number * 2


nested_functions: dict[
    str,
    list[Callable[[int], int]],
] = {
    "basic": [
        nested_add,
        nested_double,
    ],
}

nested_result_one: int = nested_functions["basic"][0](
    10,
)

nested_result_two: int = nested_functions["basic"][1](
    10,
)

print(
    nested_result_one
)

print(
    nested_result_two
)

# Functions can appear inside complex data structures.

# =============================================================================
# 24. Higher-Order Functions
# =============================================================================

"""
A higher-order function is a function that does at least one of the
following:

1. Accepts a function as an argument.

2. Returns a function.

For example:

    def execute(
        function: Callable[[int], int],
        value: int,
    ) -> int:
        return function(value)

execute() is a higher-order function because it accepts a function.

Another example:

    def create_multiplier(
        multiplier: int,
    ) -> Callable[[int], int]:
        ...

create_multiplier() is a higher-order function because it returns a
function.

First-class functions make higher-order functions possible.
"""

# =============================================================================
# 25. Custom Higher-Order Function
# =============================================================================


def apply_operation(
    operation: Callable[[int], int],
    value: int,
) -> int:
    """Apply an operation to a value."""
    return operation(
        value,
    )


def increment(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


operation_result: int = apply_operation(
    increment,
    100,
)

print(
    operation_result
)

# apply_operation() accepts a function.
#
# Therefore it is a higher-order function.

# =============================================================================
# 26. Function That Accepts a Function
# =============================================================================


def transform_text(
    transformer: Callable[[str], str],
    text: str,
) -> str:
    """Transform text using a supplied function."""
    return transformer(
        text,
    )


def reverse_text(
    text: str,
) -> str:
    """Reverse a string."""
    return text[::-1]


transformed_text: str = transform_text(
    reverse_text,
    "Python",
)

print(
    transformed_text
)

# The function controls the behaviour.
#
# The data is supplied separately.

# =============================================================================
# 27. Function That Returns a Function
# =============================================================================


def create_prefixer(
    prefix: str,
) -> Callable[[str], str]:
    """Create a function that adds a prefix."""

    def add_prefix(
        text: str,
    ) -> str:
        """Add the captured prefix to text."""
        return f"{prefix}{text}"

    return add_prefix


error_prefixer: Callable[[str], str] = create_prefixer(
    "ERROR: ",
)

info_prefixer: Callable[[str], str] = create_prefixer(
    "INFO: ",
)

error_message: str = error_prefixer(
    "Something failed.",
)

info_message: str = info_prefixer(
    "Process completed.",
)

print(
    error_message
)

print(
    info_message
)

# Each returned function remembers its own prefix.

# =============================================================================
# 28. Functions Accepting and Returning Functions
# =============================================================================


def create_incrementer(
    amount: int,
) -> Callable[[int], int]:
    """Create an incrementing function."""

    def increment_value(
        value: int,
    ) -> int:
        """Increment using the captured amount."""
        return value + amount

    return increment_value


def execute_transformation(
    transformer: Callable[[int], int],
    value: int,
) -> int:
    """Execute a transformation."""
    return transformer(
        value,
    )


increment_by_five: Callable[[int], int] = create_incrementer(
    5,
)

transformed_number: int = execute_transformation(
    increment_by_five,
    10,
)

print(
    transformed_number
)

# This combines:
#
# - Returning functions
# - Passing functions
# - Closures
# - Higher-order functions

# =============================================================================
# 29. map()
# =============================================================================


numbers_for_map: list[int] = [
    1,
    2,
    3,
    4,
]


def square_for_map(
    number: int,
) -> int:
    """Square a number."""
    return number ** 2


mapped_numbers: list[int] = list(
    map(
        square_for_map,
        numbers_for_map,
    )
)

print(
    mapped_numbers
)

# map() accepts a function and an iterable.
#
# It applies the function to each item.

# =============================================================================
# 30. filter()
# =============================================================================


numbers_for_filter: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
]


def is_even(
    number: int,
) -> bool:
    """Return True when the number is even."""
    return number % 2 == 0


even_numbers: list[int] = list(
    filter(
        is_even,
        numbers_for_filter,
    )
)

print(
    even_numbers
)

# filter() accepts a function that determines whether each item should
# be included.

# =============================================================================
# 31. sorted() With a Key Function
# =============================================================================


names: list[str] = [
    "Charlie",
    "Alice",
    "Bob",
]


def name_length(
    name: str,
) -> int:
    """Return the length of a name."""
    return len(
        name,
    )


sorted_names: list[str] = sorted(
    names,
    key=name_length,
)

print(
    sorted_names
)

# sorted() accepts a function through its key parameter.
#
# The key function determines how items are compared for sorting.

# =============================================================================
# 32. min() With a Key Function
# =============================================================================


words: list[str] = [
    "Python",
    "Go",
    "JavaScript",
    "Rust",
]


shortest_word: str = min(
    words,
    key=len,
)

print(
    shortest_word
)

# len is itself a callable object.
#
# It is passed as the key function.

# =============================================================================
# 33. max() With a Key Function
# =============================================================================


longest_word: str = max(
    words,
    key=len,
)

print(
    longest_word
)

# max() uses the supplied callable to determine the comparison value.

# =============================================================================
# 34. any() With a Generator Expression
# =============================================================================


numbers_for_any: list[int] = [
    1,
    3,
    5,
    8,
]


def is_even_for_any(
    number: int,
) -> bool:
    """Return whether a number is even."""
    return number % 2 == 0


has_even_number: bool = any(
    is_even_for_any(
        number,
    )
    for number in numbers_for_any
)

print(
    has_even_number
)

# The function is used as part of the processing performed by any().

# =============================================================================
# 35. all() With a Generator Expression
# =============================================================================


numbers_for_all: list[int] = [
    2,
    4,
    6,
    8,
]


def is_even_for_all(
    number: int,
) -> bool:
    """Return whether a number is even."""
    return number % 2 == 0


all_numbers_even: bool = all(
    is_even_for_all(
        number,
    )
    for number in numbers_for_all
)

print(
    all_numbers_even
)

# all() checks whether every generated result is truthy.

# =============================================================================
# 36. Passing Built-in Functions
# =============================================================================


values_for_builtins: list[str] = [
    "Python",
    "Functions",
]


lengths: list[int] = list(
    map(
        len,
        values_for_builtins,
    )
)

print(
    lengths
)

# len is a built-in function.
#
# Because functions are first-class objects,
# len can be passed directly to map().

# =============================================================================
# 37. Passing Methods as Function Objects
# =============================================================================


text_values: list[str] = [
    "python",
    "functions",
]


uppercase_values: list[str] = list(
    map(
        str.upper,
        text_values,
    )
)

print(
    uppercase_values
)

# str.upper is a callable method descriptor.
#
# It can be passed as a callable to map().

# =============================================================================
# 38. Lambda Functions Are Also First-Class Objects
# =============================================================================


double_lambda: Callable[[int], int] = (
    lambda number: number * 2
)

lambda_result: int = double_lambda(
    10,
)

print(
    lambda_result
)

# Lambda expressions create function objects.
#
# Therefore lambda functions also follow first-class function rules.

# =============================================================================
# 39. Lambda Passed as an Argument
# =============================================================================


lambda_operation_result: int = apply_operation(
    lambda number: number + 100,
    50,
)

print(
    lambda_operation_result
)

# A lambda function can be passed directly without assigning it first.

# =============================================================================
# 40. Functions as Strategy Objects
# =============================================================================


def strategy_add(
    first: int,
    second: int,
) -> int:
    """Add two values."""
    return first + second


def strategy_multiply(
    first: int,
    second: int,
) -> int:
    """Multiply two values."""
    return first * second


def calculate_with_strategy(
    strategy: Callable[[int, int], int],
    first: int,
    second: int,
) -> int:
    """Calculate using a supplied strategy."""
    return strategy(
        first,
        second,
    )


strategy_add_result: int = calculate_with_strategy(
    strategy_add,
    10,
    5,
)

strategy_multiply_result: int = calculate_with_strategy(
    strategy_multiply,
    10,
    5,
)

print(
    strategy_add_result
)

print(
    strategy_multiply_result
)

# This is a simple example of the strategy pattern.
#
# The calculation function does not need to know which strategy it will
# receive.

# =============================================================================
# 41. Strategy Selection With a Dictionary
# =============================================================================


def strategy_increment(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


def strategy_decrement(
    value: int,
) -> int:
    """Decrement a value."""
    return value - 1


def strategy_square(
    value: int,
) -> int:
    """Square a value."""
    return value ** 2


strategies: dict[
    str,
    Callable[[int], int],
] = {
    "increment": strategy_increment,
    "decrement": strategy_decrement,
    "square": strategy_square,
}

selected_strategy_name: str = "square"

selected_strategy: Callable[[int], int] = strategies[
    selected_strategy_name
]

selected_strategy_result: int = selected_strategy(
    6,
)

print(
    selected_strategy_result
)

# The dictionary provides a clean mapping:
#
# operation name
#       ↓
# function
#
# This pattern is commonly called a dispatch table.

# =============================================================================
# 42. Function Composition
# =============================================================================


def add_one_for_composition(
    value: int,
) -> int:
    """Add one."""
    return value + 1


def double_for_composition(
    value: int,
) -> int:
    """Double a value."""
    return value * 2


def compose(
    first: Callable[[int], int],
    second: Callable[[int], int],
) -> Callable[[int], int]:
    """Compose two integer transformations."""

    def composed(
        value: int,
    ) -> int:
        """Apply first and then second."""
        first_result: int = first(
            value,
        )

        return second(
            first_result,
        )

    return composed


add_then_double: Callable[[int], int] = compose(
    add_one_for_composition,
    double_for_composition,
)

composed_result: int = add_then_double(
    10,
)

print(
    composed_result
)

# The flow is:
#
# 10
# ↓
# add_one
# ↓
# 11
# ↓
# double
# ↓
# 22

# =============================================================================
# 43. Function Pipeline
# =============================================================================


def increment_for_pipeline(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


def double_for_pipeline(
    value: int,
) -> int:
    """Double a value."""
    return value * 2


def square_for_pipeline(
    value: int,
) -> int:
    """Square a value."""
    return value ** 2


def run_pipeline(
    value: int,
    functions: list[Callable[[int], int]],
) -> int:
    """Apply functions sequentially."""
    current_value: int = value

    for function in functions:
        current_value = function(
            current_value,
        )

    return current_value


pipeline: list[Callable[[int], int]] = [
    increment_for_pipeline,
    double_for_pipeline,
    square_for_pipeline,
]

pipeline_result: int = run_pipeline(
    3,
    pipeline,
)

print(
    pipeline_result
)

# Pipeline:
#
# 3
# ↓
# +1
# ↓
# 4
# ↓
# *2
# ↓
# 8
# ↓
# **2
# ↓
# 64

# =============================================================================
# 44. Functions as Validators
# =============================================================================


def validate_positive(
    value: int,
) -> bool:
    """Return True when a value is positive."""
    return value > 0


def validate_even(
    value: int,
) -> bool:
    """Return True when a value is even."""
    return value % 2 == 0


def validate(
    value: int,
    validator: Callable[[int], bool],
) -> bool:
    """Validate a value with a supplied validator."""
    return validator(
        value,
    )


positive_result: bool = validate(
    10,
    validate_positive,
)

even_result: bool = validate(
    10,
    validate_even,
)

print(
    positive_result
)

print(
    even_result
)

# Functions can represent validation behaviour.

# =============================================================================
# 45. Multiple Validators
# =============================================================================


def validate_all(
    value: int,
    validators: list[Callable[[int], bool]],
) -> bool:
    """Return True when every validator passes."""
    return all(
        validator(
            value,
        )
        for validator in validators
    )


validators: list[Callable[[int], bool]] = [
    validate_positive,
    validate_even,
]

validation_result: bool = validate_all(
    10,
    validators,
)

print(
    validation_result
)

# This allows validation rules to be assembled dynamically.

# =============================================================================
# 46. Function-Based Event Handlers
# =============================================================================


def on_login() -> str:
    """Handle a login event."""
    return "Login event handled."


def on_logout() -> str:
    """Handle a logout event."""
    return "Logout event handled."


event_handlers: dict[
    str,
    Callable[[], str],
] = {
    "login": on_login,
    "logout": on_logout,
}

event_name: str = "login"

event_handler: Callable[[], str] = event_handlers[
    event_name
]

event_result: str = event_handler()

print(
    event_result
)

# Event systems commonly store callback functions and invoke them when
# an event occurs.

# =============================================================================
# 47. Functions as Configuration
# =============================================================================


def development_formatter(
    message: str,
) -> str:
    """Format a development message."""
    return f"[DEV] {message}"


def production_formatter(
    message: str,
) -> str:
    """Format a production message."""
    return f"[PROD] {message}"


formatter: Callable[[str], str] = development_formatter

formatted_message: str = formatter(
    "Application started.",
)

print(
    formatted_message
)

formatter = production_formatter

formatted_message = formatter(
    "Application started.",
)

print(
    formatted_message
)

# A function variable can be changed to select behaviour dynamically.

# =============================================================================
# 48. Functions Can Be Stored for Later Execution
# =============================================================================


def delayed_task() -> str:
    """Return a delayed task result."""
    return "Task executed."


tasks: list[Callable[[], str]] = [
    delayed_task,
]

for task in tasks:
    task_result: str = task()

    print(
        task_result
    )

# The function is stored now and executed later.

# =============================================================================
# 49. Function References Do Not Execute Immediately
# =============================================================================


def important_operation() -> str:
    """Return an operation result."""
    return "Operation completed."


stored_operation: Callable[[], str] = important_operation

print(
    "Function has been stored."
)

operation_output: str = stored_operation()

print(
    operation_output
)

# This:
#
# stored_operation = important_operation
#
# does not execute important_operation().
#
# Execution happens later:
#
# stored_operation()

# =============================================================================
# 50. Passing a Function Versus Calling a Function
# =============================================================================


def calculate_value_for_passing() -> int:
    """Return a calculated value."""
    return 100


def use_function(
    function: Callable[[], int],
) -> int:
    """Call the supplied function."""
    return function()


function_passing_result: int = use_function(
    calculate_value_for_passing,
)

function_calling_result: int = calculate_value_for_passing()

print(
    function_passing_result
)

print(
    function_calling_result
)

# Passing:
#
# use_function(calculate_value_for_passing)
#
# Calling:
#
# calculate_value_for_passing()
#
# Parentheses change the operation.

# =============================================================================
# 51. Callable Type Annotation
# =============================================================================


def process_integer(
    function: Callable[[int], int],
    value: int,
) -> int:
    """Process an integer with a callable."""
    return function(
        value,
    )


def triple_integer(
    value: int,
) -> int:
    """Triple an integer."""
    return value * 3


processed_integer: int = process_integer(
    triple_integer,
    5,
)

print(
    processed_integer
)

# Callable[[int], int]
#
# means:
#
# accepts:
#
# int
#
# returns:
#
# int

# =============================================================================
# 52. Callable With Multiple Parameters
# =============================================================================


def execute_binary_operation(
    operation: Callable[[int, int], int],
    first: int,
    second: int,
) -> int:
    """Execute a binary operation."""
    return operation(
        first,
        second,
    )


def subtract_numbers(
    first: int,
    second: int,
) -> int:
    """Subtract two numbers."""
    return first - second


binary_result: int = execute_binary_operation(
    subtract_numbers,
    20,
    7,
)

print(
    binary_result
)

# Callable[[int, int], int]
#
# means:
#
# two integer parameters
#       ↓
# integer return value

# =============================================================================
# 53. Callable Returning Another Callable
# =============================================================================


def create_adder(
    amount: int,
) -> Callable[[int], int]:
    """Return a function that adds a fixed amount."""

    def add(
        value: int,
    ) -> int:
        """Add the captured amount."""
        return value + amount

    return add


adder: Callable[[int], int] = create_adder(
    10,
)

adder_result: int = adder(
    25,
)

print(
    adder_result
)

# Callable can describe functions that return other functions.

# =============================================================================
# 54. Function Alias
# =============================================================================


def original_function() -> str:
    """Return a message."""
    return "Original function."


function_alias: Callable[[], str] = original_function

alias_result: str = function_alias()

print(
    alias_result
)

# function_alias is an alias for original_function.

# =============================================================================
# 55. Functions Can Be Compared by Identity
# =============================================================================


def identity_example() -> str:
    """Return an identity example."""
    return "Example"


identity_alias = identity_example

print(
    identity_example is identity_alias
)

# is checks whether both names refer to the same object.

# =============================================================================
# 56. Different Functions Are Different Objects
# =============================================================================


def first_identity_function() -> str:
    """Return the first value."""
    return "Value"


def second_identity_function() -> str:
    """Return the second value."""
    return "Value"


print(
    first_identity_function is second_identity_function
)

# The functions may return the same value,
# but they are different function objects.

# =============================================================================
# 57. Function Name Is a Reference
# =============================================================================


def reference_example() -> str:
    """Return a reference example."""
    return "Hello"


reference_one = reference_example
reference_two = reference_example

print(
    reference_one is reference_two
)

# The function name is a reference to a function object.
#
# Assigning the reference to another name does not duplicate the function.

# =============================================================================
# 58. Functions and Object Attributes
# =============================================================================


def attribute_example() -> str:
    """Return an attribute example."""
    return "Hello"


attribute_example.custom_value = "metadata"

custom_attribute: str = attribute_example.custom_value

print(
    custom_attribute
)

# Python function objects can have attributes.
#
# This is legal Python, although custom function attributes should be used
# only when they make the design clearer.

# =============================================================================
# 59. Function __name__
# =============================================================================


def inspect_function_name() -> str:
    """Return a function name."""
    return "Name"


print(
    inspect_function_name.__name__
)

# Functions expose metadata such as __name__.

# =============================================================================
# 60. Function __doc__
# =============================================================================


def documented_function() -> str:
    """Return a documented value."""
    return "Documentation example."


print(
    documented_function.__doc__
)

# __doc__ contains the function's docstring.

# =============================================================================
# 61. First-Class Functions and Decorators
# =============================================================================

"""
Decorators rely heavily on first-class functions.

A decorator typically:

1. Receives a function.
2. Creates another function.
3. Returns the new function.

Example:

    def decorator(
        function: Callable[[], str],
    ) -> Callable[[], str]:

        def wrapper() -> str:
            return function()

        return wrapper

The original function is treated as data.
The wrapper is another function object.
The decorator returns that function object.
"""

# =============================================================================
# 62. Simple Decorator-Like Example
# =============================================================================


def add_message_prefix(
    function: Callable[[], str],
) -> Callable[[], str]:
    """Wrap a function with a message prefix."""

    def wrapper() -> str:
        """Execute the original function with a prefix."""
        original_result: str = function()

        return f"PREFIX: {original_result}"

    return wrapper


def original_message() -> str:
    """Return an original message."""
    return "Hello."


wrapped_message: Callable[[], str] = add_message_prefix(
    original_message,
)

wrapped_result: str = wrapped_message()

print(
    wrapped_result
)

# The decorator-like function receives one function
# and returns another function.

# =============================================================================
# 63. Function Composition With Text
# =============================================================================


def strip_text(
    text: str,
) -> str:
    """Remove surrounding whitespace."""
    return text.strip()


def uppercase_text(
    text: str,
) -> str:
    """Convert text to uppercase."""
    return text.upper()


def compose_text_functions(
    first: Callable[[str], str],
    second: Callable[[str], str],
) -> Callable[[str], str]:
    """Compose two text functions."""

    def composed(
        text: str,
    ) -> str:
        """Apply the two functions sequentially."""
        first_result: str = first(
            text,
        )

        return second(
            first_result,
        )

    return composed


clean_and_uppercase: Callable[[str], str] = (
    compose_text_functions(
        strip_text,
        uppercase_text,
    )
)

cleaned_text: str = clean_and_uppercase(
    "  python  ",
)

print(
    cleaned_text
)

# Output:
#
# PYTHON

# =============================================================================
# 64. Functions as Data
# =============================================================================

"""
A useful mental model is:

    function object
        |
        +--> variable
        |
        +--> list item
        |
        +--> tuple item
        |
        +--> dictionary value
        |
        +--> dictionary key
        |
        +--> function argument
        |
        +--> function return value

Functions are therefore values that can move through a Python program.

This is the central idea behind first-class functions.
"""

# =============================================================================
# 65. Function Registry
# =============================================================================


def register_alpha() -> str:
    """Return alpha handler output."""
    return "Alpha"


def register_beta() -> str:
    """Return beta handler output."""
    return "Beta"


def register_gamma() -> str:
    """Return gamma handler output."""
    return "Gamma"


function_registry: dict[
    str,
    Callable[[], str],
] = {}

function_registry["alpha"] = register_alpha
function_registry["beta"] = register_beta
function_registry["gamma"] = register_gamma

registry_result: str = function_registry["beta"]()

print(
    registry_result
)

# A registry can dynamically associate names with functions.

# =============================================================================
# 66. Registering Functions Through a Helper
# =============================================================================


def register_function(
    registry: dict[str, Callable[[], str]],
    name: str,
    function: Callable[[], str],
) -> None:
    """Register a function under a name."""
    registry[name] = function


def registered_function() -> str:
    """Return a registered value."""
    return "Registered."


registered_functions: dict[
    str,
    Callable[[], str],
] = {}

register_function(
    registered_functions,
    "example",
    registered_function,
)

registered_result: str = registered_functions["example"]()

print(
    registered_result
)

# The helper accepts a function as an argument and stores it.

# =============================================================================
# 67. Dynamic Command System
# =============================================================================


def command_create() -> str:
    """Create a resource."""
    return "Create command."


def command_delete() -> str:
    """Delete a resource."""
    return "Delete command."


def command_update() -> str:
    """Update a resource."""
    return "Update command."


commands: dict[
    str,
    Callable[[], str],
] = {
    "create": command_create,
    "delete": command_delete,
    "update": command_update,
}

selected_command: str = "update"

command_result: str = commands[
    selected_command
]()

print(
    command_result
)

# This pattern is useful for command dispatch systems.

# =============================================================================
# 68. Functions and Iteration
# =============================================================================


def increment_value(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


increment_functions: list[
    Callable[[int], int],
] = [
    increment_value,
    increment_value,
    increment_value,
]

current_value: int = 0

for function in increment_functions:
    current_value = function(
        current_value,
    )

print(
    current_value
)

# The same function object can be stored multiple times.

# =============================================================================
# 69. Functions Can Be Reused
# =============================================================================


def normalize_text(
    text: str,
) -> str:
    """Normalize text."""
    return text.strip().lower()


texts: list[str] = [
    " Python ",
    " FUNCTIONS ",
    " FIRST CLASS ",
]

normalized_texts: list[str] = list(
    map(
        normalize_text,
        texts,
    )
)

print(
    normalized_texts
)

# The same function can be reused in multiple places.

# =============================================================================
# 70. Function Reuse With Different Inputs
# =============================================================================


def calculate_double(
    value: int,
) -> int:
    """Double a value."""
    return value * 2


first_double: int = calculate_double(
    10,
)

second_double: int = calculate_double(
    50,
)

third_double: int = calculate_double(
    100,
)

print(
    first_double
)

print(
    second_double
)

print(
    third_double
)

# First-class functions are reusable objects,
# and functions can be passed around without duplicating their implementation.

# =============================================================================
# 71. Function Factories With Different Behaviour
# =============================================================================


def create_power_function(
    exponent: int,
) -> Callable[[int], int]:
    """Create a function that raises numbers to an exponent."""

    def power(
        number: int,
    ) -> int:
        """Raise a number to the captured exponent."""
        return number ** exponent

    return power


square_function_factory: Callable[[int], int] = (
    create_power_function(
        2,
    )
)

cube_function_factory: Callable[[int], int] = (
    create_power_function(
        3,
    )
)

factory_square_result: int = square_function_factory(
    4,
)

factory_cube_result: int = cube_function_factory(
    4,
)

print(
    factory_square_result
)

print(
    factory_cube_result
)

# The factory creates functions with different captured behaviour.

# =============================================================================
# 72. First-Class Functions and Closures
# =============================================================================

"""
A closure occurs when a nested function remembers variables from its
enclosing scope.

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

Therefore:

    double = create_multiplier(2)

and:

    triple = create_multiplier(3)

create two function objects with different remembered values.

Closures are possible because functions are first-class objects.
"""

# =============================================================================
# 73. Independent Closures
# =============================================================================


def create_counter_function() -> Callable[[], int]:
    """Create an independent counter."""
    count: int = 0

    def increment_counter() -> int:
        """Increment the captured counter."""
        nonlocal count

        count += 1

        return count

    return increment_counter


counter_one: Callable[[], int] = create_counter_function()
counter_two: Callable[[], int] = create_counter_function()

counter_one_result_1: int = counter_one()
counter_one_result_2: int = counter_one()

counter_two_result_1: int = counter_two()

print(
    counter_one_result_1
)

print(
    counter_one_result_2
)

print(
    counter_two_result_1
)

# counter_one and counter_two have independent enclosing state.

# =============================================================================
# 74. Function as a Return Value
# =============================================================================


def select_operation(
    operation_name: str,
) -> Callable[[int, int], int]:
    """Select an arithmetic operation."""

    def add(
        first: int,
        second: int,
    ) -> int:
        """Add two values."""
        return first + second

    def multiply(
        first: int,
        second: int,
    ) -> int:
        """Multiply two values."""
        return first * second

    operations: dict[
        str,
        Callable[[int, int], int],
    ] = {
        "add": add,
        "multiply": multiply,
    }

    return operations[operation_name]


selected_operation: Callable[[int, int], int] = select_operation(
    "multiply",
)

selected_operation_result: int = selected_operation(
    6,
    7,
)

print(
    selected_operation_result
)

# A function can dynamically return another function based on input.

# =============================================================================
# 75. Function Selection
# =============================================================================


def choose_formatter(
    uppercase: bool,
) -> Callable[[str], str]:
    """Choose a text formatter."""

    def uppercase_formatter(
        text: str,
    ) -> str:
        """Format text as uppercase."""
        return text.upper()

    def lowercase_formatter(
        text: str,
    ) -> str:
        """Format text as lowercase."""
        return text.lower()

    if uppercase:
        return uppercase_formatter

    return lowercase_formatter


selected_formatter: Callable[[str], str] = choose_formatter(
    True,
)

selected_format_result: str = selected_formatter(
    "Python",
)

print(
    selected_format_result
)

# The function returns one of two function objects.

# =============================================================================
# 76. First-Class Functions and Dependency Injection
# =============================================================================


def print_logger(
    message: str,
) -> None:
    """Log a message using print."""
    print(
        f"LOG: {message}"
    )


def process_with_logger(
    message: str,
    logger: Callable[[str], None],
) -> None:
    """Process a message using a supplied logger."""
    logger(
        message,
    )


process_with_logger(
    "Process started.",
    print_logger,
)

# A function can receive dependencies as callable objects.
#
# This is a simple form of dependency injection.

# =============================================================================
# 77. First-Class Functions and Testing
# =============================================================================


def add_for_testing(
    first: int,
    second: int,
) -> int:
    """Add two numbers."""
    return first + second


def execute_test_operation(
    operation: Callable[[int, int], int],
) -> int:
    """Execute an operation with test values."""
    return operation(
        2,
        3,
    )


test_result: int = execute_test_operation(
    add_for_testing,
)

print(
    test_result
)

# Passing functions as dependencies can make code easier to test because
# alternative implementations can be supplied.

# =============================================================================
# 78. Mock-Like Function
# =============================================================================


def real_operation() -> str:
    """Represent a real operation."""
    return "Real operation."


def fake_operation() -> str:
    """Represent a replacement operation."""
    return "Fake operation."


def execute_operation_with_dependency(
    operation: Callable[[], str],
) -> str:
    """Execute a supplied operation."""
    return operation()


real_result: str = execute_operation_with_dependency(
    real_operation,
)

fake_result: str = execute_operation_with_dependency(
    fake_operation,
)

print(
    real_result
)

print(
    fake_result
)

# The caller can choose which implementation to provide.

# =============================================================================
# 79. First-Class Functions and Custom Sorting
# =============================================================================


def get_score(
    item: tuple[str, int],
) -> int:
    """Return the score from a tuple."""
    return item[1]


scores: list[tuple[str, int]] = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 95),
]

sorted_scores: list[tuple[str, int]] = sorted(
    scores,
    key=get_score,
    reverse=True,
)

print(
    sorted_scores
)

# get_score is passed as a first-class function to sorted().

# =============================================================================
# 80. First-Class Functions and Data Processing
# =============================================================================


def clean_number(
    number: int,
) -> int:
    """Clean a number by ensuring it is non-negative."""
    return abs(
        number,
    )


raw_numbers: list[int] = [
    -5,
    10,
    -20,
    30,
]

clean_numbers: list[int] = list(
    map(
        clean_number,
        raw_numbers,
    )
)

print(
    clean_numbers
)

# The data-processing function is passed as a value.

# =============================================================================
# 81. Combining map() and filter()
# =============================================================================


def is_positive(
    number: int,
) -> bool:
    """Return True for positive numbers."""
    return number > 0


def double_positive(
    number: int,
) -> int:
    """Double a positive number."""
    return number * 2


raw_values: list[int] = [
    -5,
    2,
    -3,
    4,
    6,
]

positive_values: list[int] = list(
    filter(
        is_positive,
        raw_values,
    )
)

doubled_positive_values: list[int] = list(
    map(
        double_positive,
        positive_values,
    )
)

print(
    doubled_positive_values
)

# First:
#
# filter()
#
# then:
#
# map()
#
# Both receive functions.

# =============================================================================
# 82. Functions in a Processing Pipeline
# =============================================================================


def remove_spaces(
    text: str,
) -> str:
    """Remove spaces from text."""
    return text.replace(
        " ",
        "",
    )


def convert_to_uppercase(
    text: str,
) -> str:
    """Convert text to uppercase."""
    return text.upper()


def add_marker(
    text: str,
) -> str:
    """Add a marker to text."""
    return f"<{text}>"


text_pipeline: list[
    Callable[[str], str],
] = [
    remove_spaces,
    convert_to_uppercase,
    add_marker,
]


def execute_text_pipeline(
    text: str,
    pipeline_functions: list[Callable[[str], str]],
) -> str:
    """Execute text-processing functions sequentially."""
    result: str = text

    for function in pipeline_functions:
        result = function(
            result,
        )

    return result


pipeline_text_result: str = execute_text_pipeline(
    "hello python",
    text_pipeline,
)

print(
    pipeline_text_result
)

# The pipeline stores behaviour as data.

# =============================================================================
# 83. First-Class Functions and Optional Behaviour
# =============================================================================


def default_transform(
    value: int,
) -> int:
    """Return the value unchanged."""
    return value


def transform_value(
    value: int,
    transformer: Callable[[int], int] = default_transform,
) -> int:
    """Transform a value using an optional function."""
    return transformer(
        value,
    )


default_transform_result: int = transform_value(
    10,
)

custom_transform_result: int = transform_value(
    10,
    lambda number: number * 10,
)

print(
    default_transform_result
)

print(
    custom_transform_result
)

# A callable can also be used as a default parameter.

# =============================================================================
# 84. Function Returning a Function With a Type Alias
# =============================================================================


IntegerFunction = Callable[[int], int]


def create_increment_function(
    amount: int,
) -> IntegerFunction:
    """Create an integer transformation function."""

    def increment(
        value: int,
    ) -> int:
        """Increment by the captured amount."""
        return value + amount

    return increment


increment_ten: IntegerFunction = create_increment_function(
    10,
)

increment_ten_result: int = increment_ten(
    50,
)

print(
    increment_ten_result
)

# A type alias can make repeated Callable annotations easier to read.

# =============================================================================
# 85. Function Type Alias With Multiple Parameters
# =============================================================================


BinaryIntegerFunction = Callable[[int, int], int]


def create_adder_function(
    amount: int,
) -> BinaryIntegerFunction:
    """Create a binary addition function."""

    def add(
        first: int,
        second: int,
    ) -> int:
        """Add two values and the captured amount."""
        return first + second + amount

    return add


adder_function: BinaryIntegerFunction = create_adder_function(
    5,
)

adder_function_result: int = adder_function(
    10,
    20,
)

print(
    adder_function_result
)

# Callable aliases can improve readability in larger programs.

# =============================================================================
# 86. Functions and the Callable Protocol
# =============================================================================

"""
Callable is broader than ordinary functions.

A value is callable if Python allows it to be invoked with parentheses.

Examples include:

- Functions
- Methods
- Classes
- Objects implementing __call__
- Some built-in objects

Therefore:

    Callable[[int], int]

describes callable behaviour rather than only a traditional def function.
"""

# =============================================================================
# 87. Callable Object
# =============================================================================


class Multiplier:
    """Create an object that can be called like a function."""

    def __init__(
        self,
        factor: int,
    ) -> None:
        """Initialize the multiplier."""
        self.factor = factor

    def __call__(
        self,
        value: int,
    ) -> int:
        """Multiply a value."""
        return value * self.factor


multiplier_object = Multiplier(
    5,
)

callable_object_result: int = multiplier_object(
    10,
)

print(
    callable_object_result
)

# Multiplier is not a function.
#
# However, its object implements __call__().
#
# Therefore the object is callable.

# =============================================================================
# 88. Callable Accepts Functions and Callable Objects
# =============================================================================


def execute_callable(
    function: Callable[[int], int],
    value: int,
) -> int:
    """Execute any compatible callable."""
    return function(
        value,
    )


callable_object_execution: int = execute_callable(
    multiplier_object,
    10,
)

print(
    callable_object_execution
)

# Callable annotations can accept compatible callable objects as well.

# =============================================================================
# 89. First-Class Functions Versus Normal Values
# =============================================================================


def function_value() -> int:
    """Return an integer."""
    return 100


integer_value: int = 100

function_reference_value: Callable[[], int] = function_value

print(
    integer_value
)

print(
    function_reference_value()
)

# Both are objects.
#
# The integer stores data.
#
# The function stores executable behaviour.
#
# Both can be assigned to names and passed around.

# =============================================================================
# 90. First-Class Functions Mental Model
# =============================================================================

"""
Think of a function as an object:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

The name:

    add

refers to the function object.

Therefore:

    operation = add

stores the reference.

Then:

    operation(10, 20)

calls that same function.

Likewise:

    execute(add)

passes the function to another function.

And:

    return add

returns the function.

The important concept is:

    FUNCTION NAME
        |
        v
    FUNCTION OBJECT
        |
        +--> assign
        +--> pass
        +--> return
        +--> store
        +--> call
"""

# =============================================================================
# 91. Common Mistake: Calling Instead of Passing
# =============================================================================


def mistake_example() -> str:
    """Return a mistake example."""
    return "Hello"


def execute_no_argument_function(
    function: Callable[[], str],
) -> str:
    """Execute a supplied function."""
    return function()


correct_reference: str = execute_no_argument_function(
    mistake_example,
)

print(
    correct_reference
)

# Correct:
#
# execute_no_argument_function(mistake_example)
#
# Incorrect:
#
# execute_no_argument_function(mistake_example())
#
# The incorrect version calls mistake_example() immediately and passes its
# returned string instead of passing the function.

# =============================================================================
# 92. Common Mistake: Forgetting Parentheses When Calling
# =============================================================================


def call_me() -> str:
    """Return a message."""
    return "Called."


call_me_reference: Callable[[], str] = call_me

call_me_result: str = call_me_reference()

print(
    call_me_result
)

# call_me
#
# means the function object.
#
# call_me()
#
# means execute the function.

# =============================================================================
# 93. Common Mistake: Passing the Wrong Callable Signature
# =============================================================================


def expects_integer(
    value: int,
) -> int:
    """Return an integer value."""
    return value * 2


def accepts_integer_function(
    function: Callable[[int], int],
) -> int:
    """Execute a compatible integer function."""
    return function(
        10,
    )


signature_result: int = accepts_integer_function(
    expects_integer,
)

print(
    signature_result
)

# A Callable annotation communicates the expected function signature.
#
# Static type checkers such as mypy and Pylance can use this information
# to detect incompatible callables.

# =============================================================================
# 94. Common Mistake: Confusing Return Value With Function
# =============================================================================


def return_number() -> int:
    """Return a number."""
    return 42


function_object: Callable[[], int] = return_number

returned_number: int = return_number()

print(
    function_object
)

print(
    returned_number
)

# function_object:
#
# function
#
# returned_number:
#
# int
#
# These have different types and different purposes.

# =============================================================================
# 95. First-Class Functions and Scope
# =============================================================================


def create_scoped_function(
    prefix: str,
) -> Callable[[str], str]:
    """Create a function using an enclosing value."""

    def format_message(
        message: str,
    ) -> str:
        """Format a message using the captured prefix."""
        return f"{prefix}: {message}"

    return format_message


scoped_function: Callable[[str], str] = create_scoped_function(
    "INFO",
)

scoped_function_result: str = scoped_function(
    "Application started.",
)

print(
    scoped_function_result
)

# The returned function is first-class.
#
# It also forms a closure over prefix.

# =============================================================================
# 96. First-Class Functions and Encapsulation
# =============================================================================


def create_private_counter() -> Callable[[], int]:
    """Create a counter with enclosed state."""
    count: int = 0

    def get_next_count() -> int:
        """Return the next counter value."""
        nonlocal count

        count += 1

        return count

    return get_next_count


private_counter: Callable[[], int] = create_private_counter()

private_counter_value_1: int = private_counter()
private_counter_value_2: int = private_counter()

print(
    private_counter_value_1
)

print(
    private_counter_value_2
)

# The count variable is not exposed directly.
#
# The returned function provides controlled access to the enclosed state.

# =============================================================================
# 97. First-Class Functions and Command Queues
# =============================================================================


def task_one() -> str:
    """Run task one."""
    return "Task one."


def task_two() -> str:
    """Run task two."""
    return "Task two."


def task_three() -> str:
    """Run task three."""
    return "Task three."


task_queue: list[Callable[[], str]] = [
    task_one,
    task_two,
    task_three,
]

for queued_task in task_queue:
    queued_result: str = queued_task()

    print(
        queued_result
    )

# Functions can represent delayed work.

# =============================================================================
# 98. First-Class Functions and Menu Actions
# =============================================================================


def show_home() -> str:
    """Show the home page."""
    return "Home"


def show_profile() -> str:
    """Show the profile page."""
    return "Profile"


def show_settings() -> str:
    """Show the settings page."""
    return "Settings"


menu_actions: dict[
    str,
    Callable[[], str],
] = {
    "home": show_home,
    "profile": show_profile,
    "settings": show_settings,
}

selected_menu: str = "profile"

menu_action_result: str = menu_actions[
    selected_menu
]()

print(
    menu_action_result
)

# Menu names map directly to functions.

# =============================================================================
# 99. First-Class Functions and Rules
# =============================================================================


def rule_is_positive(
    value: int,
) -> bool:
    """Check whether a value is positive."""
    return value > 0


def rule_is_less_than_hundred(
    value: int,
) -> bool:
    """Check whether a value is below one hundred."""
    return value < 100


rules: list[
    Callable[[int], bool],
] = [
    rule_is_positive,
    rule_is_less_than_hundred,
]


def passes_all_rules(
    value: int,
    validation_rules: list[Callable[[int], bool]],
) -> bool:
    """Check every validation rule."""
    return all(
        rule(
            value,
        )
        for rule in validation_rules
    )


rules_result: bool = passes_all_rules(
    50,
    rules,
)

print(
    rules_result
)

# Rules can be represented as function objects.

# =============================================================================
# 100. First-Class Functions and Feature Selection
# =============================================================================


def feature_a(
    value: int,
) -> int:
    """Apply feature A."""
    return value + 10


def feature_b(
    value: int,
) -> int:
    """Apply feature B."""
    return value * 10


def feature_c(
    value: int,
) -> int:
    """Apply feature C."""
    return value ** 2


features: dict[
    str,
    Callable[[int], int],
] = {
    "a": feature_a,
    "b": feature_b,
    "c": feature_c,
}

selected_feature_name: str = "c"

selected_feature: Callable[[int], int] = features[
    selected_feature_name
]

feature_result: int = selected_feature(
    5,
)

print(
    feature_result
)

# Behaviour can be selected at runtime.

# =============================================================================
# 101. First-Class Functions and Function Composition
# =============================================================================


def increment_value_composition(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


def square_value_composition(
    value: int,
) -> int:
    """Square a value."""
    return value ** 2


def build_pipeline(
    functions: list[Callable[[int], int]],
) -> Callable[[int], int]:
    """Build a reusable integer pipeline."""

    def pipeline_function(
        value: int,
    ) -> int:
        """Execute the captured pipeline."""
        result: int = value

        for function in functions:
            result = function(
                result,
            )

        return result

    return pipeline_function


integer_pipeline: Callable[[int], int] = build_pipeline(
    [
        increment_value_composition,
        square_value_composition,
    ]
)

integer_pipeline_result: int = integer_pipeline(
    4,
)

print(
    integer_pipeline_result
)

# The pipeline itself is a function object.
#
# It can be stored and executed later.

# =============================================================================
# 102. First-Class Functions and Reusable Behaviour
# =============================================================================


def make_greeting(
    greeting_word: str,
) -> Callable[[str], str]:
    """Create a reusable greeting function."""

    def greet_person(
        name: str,
    ) -> str:
        """Create a greeting for a person."""
        return f"{greeting_word}, {name}!"

    return greet_person


hello_greeting: Callable[[str], str] = make_greeting(
    "Hello",
)

welcome_greeting: Callable[[str], str] = make_greeting(
    "Welcome",
)

hello_result: str = hello_greeting(
    "Alex",
)

welcome_result: str = welcome_greeting(
    "Alex",
)

print(
    hello_result
)

print(
    welcome_result
)

# Function factories allow reusable behaviour to be generated dynamically.

# =============================================================================
# 103. First-Class Functions and Callbacks
# =============================================================================


def on_success(
    message: str,
) -> str:
    """Handle successful processing."""
    return f"SUCCESS: {message}"


def on_failure(
    message: str,
) -> str:
    """Handle failed processing."""
    return f"FAILURE: {message}"


def process_result(
    success: bool,
    success_callback: Callable[[str], str],
    failure_callback: Callable[[str], str],
) -> str:
    """Process a result using callbacks."""
    if success:
        return success_callback(
            "Operation completed.",
        )

    return failure_callback(
        "Operation failed.",
    )


success_output: str = process_result(
    True,
    on_success,
    on_failure,
)

failure_output: str = process_result(
    False,
    on_success,
    on_failure,
)

print(
    success_output
)

print(
    failure_output
)

# The function receives two callback functions.
#
# It decides which callback to execute.

# =============================================================================
# 104. First-Class Functions and Error Handling Strategy
# =============================================================================


def safe_operation(
    value: int,
) -> int:
    """Perform a safe operation."""
    return 100 // value


def handle_error(
    error: Exception,
) -> str:
    """Convert an exception into a message."""
    return f"Error: {type(error).__name__}"


def execute_safely(
    value: int,
    operation: Callable[[int], int],
    error_handler: Callable[[Exception], str],
) -> str:
    """Execute an operation and handle errors."""
    try:
        result: int = operation(
            value,
        )
    except Exception as error:
        return error_handler(
            error,
        )

    return str(
        result,
    )


safe_result: str = execute_safely(
    10,
    safe_operation,
    handle_error,
)

error_result: str = execute_safely(
    0,
    safe_operation,
    handle_error,
)

print(
    safe_result
)

print(
    error_result
)

# Different behaviours are supplied as function objects.

# =============================================================================
# 105. First-Class Functions and Separation of Concerns
# =============================================================================


def format_currency(
    value: float,
) -> str:
    """Format a currency value."""
    return f"${value:.2f}"


def format_percentage(
    value: float,
) -> str:
    """Format a percentage value."""
    return f"{value:.1f}%"


def display_value(
    value: float,
    formatter: Callable[[float], str],
) -> str:
    """Display a value using a supplied formatter."""
    return formatter(
        value,
    )


currency_output: str = display_value(
    1250.5,
    format_currency,
)

percentage_output: str = display_value(
    87.5,
    format_percentage,
)

print(
    currency_output
)

print(
    percentage_output
)

# display_value() does not need to know formatting details.
#
# Formatting behaviour is injected through a function.

# =============================================================================
# 106. First-Class Functions and Dependency Selection
# =============================================================================


def development_mode(
    message: str,
) -> str:
    """Format a development message."""
    return f"DEV -> {message}"


def production_mode(
    message: str,
) -> str:
    """Format a production message."""
    return f"PROD -> {message}"


def create_environment_formatter(
    environment_name: str,
) -> Callable[[str], str]:
    """Select a formatter based on environment."""

    formatters_by_environment: dict[
        str,
        Callable[[str], str],
    ] = {
        "development": development_mode,
        "production": production_mode,
    }

    return formatters_by_environment[
        environment_name
    ]


environment_formatter: Callable[[str], str] = (
    create_environment_formatter(
        "production",
    )
)

environment_output: str = environment_formatter(
    "Server started.",
)

print(
    environment_output
)

# A function can return a function selected from a registry.

# =============================================================================
# 107. First-Class Functions and Recursion
# =============================================================================


def factorial(
    number: int,
) -> int:
    """Calculate a factorial recursively."""
    if number <= 1:
        return 1

    return number * factorial(
        number - 1,
    )


factorial_function: Callable[[int], int] = factorial

factorial_result: int = factorial_function(
    5,
)

print(
    factorial_result
)

# A recursive function is still a first-class function object.

# =============================================================================
# 108. First-Class Functions and Function Metadata
# =============================================================================


def metadata_example(
    value: int,
) -> int:
    """Return the supplied value."""
    return value


metadata_reference: Callable[[int], int] = metadata_example

print(
    metadata_reference.__name__
)

print(
    metadata_reference.__doc__
)

# Assigning a function to another name does not remove its function
# metadata.

# =============================================================================
# 109. First-Class Functions and Scope Review
# =============================================================================

"""
When a function is passed around, the function remains the same object.

For example:

    def outer():
        value = 10

        def inner():
            return value

        return inner

The returned inner function:

- Is a first-class object.
- Can be stored in a variable.
- Can be passed to another function.
- Can be returned again.
- Can be stored in collections.
- Retains access to the enclosing value through its closure.

This connects first-class functions directly to Python scope and closures.
"""

# =============================================================================
# 110. Practical Example: Calculator
# =============================================================================


CalculatorOperation = Callable[[float, float], float]


def calculator_add(
    first: float,
    second: float,
) -> float:
    """Add two values."""
    return first + second


def calculator_subtract(
    first: float,
    second: float,
) -> float:
    """Subtract two values."""
    return first - second


def calculator_multiply(
    first: float,
    second: float,
) -> float:
    """Multiply two values."""
    return first * second


def calculator_divide(
    first: float,
    second: float,
) -> float:
    """Divide two values."""
    return first / second


calculator_operations: dict[
    str,
    CalculatorOperation,
] = {
    "add": calculator_add,
    "subtract": calculator_subtract,
    "multiply": calculator_multiply,
    "divide": calculator_divide,
}


def calculate(
    operation: str,
    first: float,
    second: float,
) -> float:
    """Execute a selected calculator operation."""
    selected_operation: CalculatorOperation = (
        calculator_operations[operation]
    )

    return selected_operation(
        first,
        second,
    )


calculator_result_add: float = calculate(
    "add",
    10.0,
    5.0,
)

calculator_result_multiply: float = calculate(
    "multiply",
    10.0,
    5.0,
)

print(
    calculator_result_add
)

print(
    calculator_result_multiply
)

# This example demonstrates:
#
# - Functions as dictionary values
# - Callable type aliases
# - Dynamic function selection
# - Function references
# - Higher-order design

# =============================================================================
# 111. Practical Example: Text Processor
# =============================================================================


TextTransformer = Callable[[str], str]


def text_strip(
    text: str,
) -> str:
    """Strip surrounding whitespace."""
    return text.strip()


def text_lower(
    text: str,
) -> str:
    """Convert text to lowercase."""
    return text.lower()


def text_upper(
    text: str,
) -> str:
    """Convert text to uppercase."""
    return text.upper()


def text_process(
    text: str,
    transformations: list[TextTransformer],
) -> str:
    """Apply text transformations in order."""
    result: str = text

    for transformation in transformations:
        result = transformation(
            result,
        )

    return result


processed_text: str = text_process(
    "  Hello Python  ",
    [
        text_strip,
        text_lower,
    ],
)

print(
    processed_text
)

# The transformations are first-class functions stored in a list.

# =============================================================================
# 112. Practical Example: Validation System
# =============================================================================


IntegerValidator = Callable[[int], bool]


def validator_positive(
    value: int,
) -> bool:
    """Validate that a value is positive."""
    return value > 0


def validator_even(
    value: int,
) -> bool:
    """Validate that a value is even."""
    return value % 2 == 0


def validator_below_hundred(
    value: int,
) -> bool:
    """Validate that a value is below one hundred."""
    return value < 100


def validate_integer(
    value: int,
    validators: list[IntegerValidator],
) -> bool:
    """Run all validators."""
    for validator in validators:
        if not validator(
            value,
        ):
            return False

    return True


validation_rules: list[IntegerValidator] = [
    validator_positive,
    validator_even,
    validator_below_hundred,
]

valid_integer: bool = validate_integer(
    50,
    validation_rules,
)

print(
    valid_integer
)

# Validation behaviour is represented by function objects.

# =============================================================================
# 113. Practical Example: Event System
# =============================================================================


EventHandler = Callable[[str], None]


def log_event(
    event: str,
) -> None:
    """Log an event."""
    print(
        f"LOG: {event}"
    )


def print_event(
    event: str,
) -> None:
    """Print an event."""
    print(
        f"EVENT: {event}"
    )


def notify_event(
    event: str,
) -> None:
    """Notify about an event."""
    print(
        f"NOTIFY: {event}"
    )


event_handlers_list: list[EventHandler] = [
    log_event,
    print_event,
    notify_event,
]


def dispatch_event(
    event: str,
    handlers: list[EventHandler],
) -> None:
    """Dispatch an event to all handlers."""
    for event_handler in handlers:
        event_handler(
            event,
        )


dispatch_event(
    "Application started.",
    event_handlers_list,
)

# This is a common real-world use of first-class functions.

# =============================================================================
# 114. Practical Example: Retry Strategy
# =============================================================================


RetryStrategy = Callable[[int], int]


def retry_immediately(
    attempt: int,
) -> int:
    """Return the same attempt number."""
    return attempt


def retry_with_backoff(
    attempt: int,
) -> int:
    """Return a simple backoff value."""
    return attempt * 2


def calculate_retry_delay(
    attempt: int,
    strategy: RetryStrategy,
) -> int:
    """Calculate retry delay using a strategy."""
    return strategy(
        attempt,
    )


immediate_delay: int = calculate_retry_delay(
    3,
    retry_immediately,
)

backoff_delay: int = calculate_retry_delay(
    3,
    retry_with_backoff,
)

print(
    immediate_delay
)

print(
    backoff_delay
)

# The retry policy is supplied as a function.

# =============================================================================
# 115. Practical Example: Sorting Strategy
# =============================================================================


def sort_by_name(
    item: tuple[str, int],
) -> str:
    """Return the name for sorting."""
    return item[0]


def sort_by_score(
    item: tuple[str, int],
) -> int:
    """Return the score for sorting."""
    return item[1]


players: list[tuple[str, int]] = [
    ("Alice", 90),
    ("Bob", 80),
    ("Charlie", 95),
]

players_by_name: list[tuple[str, int]] = sorted(
    players,
    key=sort_by_name,
)

players_by_score: list[tuple[str, int]] = sorted(
    players,
    key=sort_by_score,
    reverse=True,
)

print(
    players_by_name
)

print(
    players_by_score
)

# The sorting behaviour is supplied through key functions.

# =============================================================================
# 116. Practical Example: Function Registry
# =============================================================================


Handler = Callable[[str], str]


def handler_one(
    value: str,
) -> str:
    """Handle value using handler one."""
    return f"ONE: {value}"


def handler_two(
    value: str,
) -> str:
    """Handle value using handler two."""
    return f"TWO: {value}"


handlers: dict[str, Handler] = {
    "one": handler_one,
    "two": handler_two,
}


def execute_handler(
    name: str,
    value: str,
) -> str:
    """Execute a registered handler."""
    handler_function: Handler = handlers[name]

    return handler_function(
        value,
    )


handler_output: str = execute_handler(
    "two",
    "Python",
)

print(
    handler_output
)

# This pattern scales well when many operations are selected by a key.

# =============================================================================
# 117. Practical Example: Middleware Chain
# =============================================================================


Middleware = Callable[[str], str]


def middleware_trim(
    value: str,
) -> str:
    """Trim whitespace."""
    return value.strip()


def middleware_upper(
    value: str,
) -> str:
    """Convert text to uppercase."""
    return value.upper()


def middleware_marker(
    value: str,
) -> str:
    """Add a marker."""
    return f"[{value}]"


def execute_middleware(
    value: str,
    middleware_functions: list[Middleware],
) -> str:
    """Execute middleware functions in order."""
    result: str = value

    for middleware in middleware_functions:
        result = middleware(
            result,
        )

    return result


middleware_result: str = execute_middleware(
    "  python  ",
    [
        middleware_trim,
        middleware_upper,
        middleware_marker,
    ],
)

print(
    middleware_result
)

# Middleware chains are another practical application of first-class
# functions.

# =============================================================================
# 118. Practical Example: Predicate Function
# =============================================================================

"""
A predicate is a function that returns a boolean value.

Examples:

    def is_even(
        number: int,
    ) -> bool:
        return number % 2 == 0

Predicate functions are often passed to:

- filter()
- all()
- any()
- Custom validation functions
- Search functions
- Collection-processing functions
"""

# =============================================================================
# 119. Custom Find Function
# =============================================================================


def find_first(
    values: list[int],
    predicate: Callable[[int], bool],
) -> int | None:
    """Return the first value satisfying a predicate."""
    for value in values:
        if predicate(
            value,
        ):
            return value

    return None


def greater_than_ten(
    value: int,
) -> bool:
    """Return whether a value is greater than ten."""
    return value > 10


found_value: int | None = find_first(
    [2, 5, 8, 15, 20],
    greater_than_ten,
)

print(
    found_value
)

# The predicate determines what "find" means.

# =============================================================================
# 120. First-Class Functions and Search
# =============================================================================


def find_first_text(
    values: list[str],
    predicate: Callable[[str], bool],
) -> str | None:
    """Find the first matching string."""
    for value in values:
        if predicate(
            value,
        ):
            return value

    return None


def contains_python(
    value: str,
) -> bool:
    """Check whether text contains Python."""
    return "Python" in value


first_python_text: str | None = find_first_text(
    [
        "Java",
        "Go",
        "Python programming",
        "Rust",
    ],
    contains_python,
)

print(
    first_python_text
)

# The same search mechanism can work with different predicates.

# =============================================================================
# 121. First-Class Functions and Transformation
# =============================================================================


def transform_all(
    values: list[int],
    transformer: Callable[[int], int],
) -> list[int]:
    """Transform every value."""
    transformed_values: list[int] = []

    for value in values:
        transformed_values.append(
            transformer(
                value,
            )
        )

    return transformed_values


def cube_value(
    value: int,
) -> int:
    """Cube a value."""
    return value ** 3


transformed_values: list[int] = transform_all(
    [1, 2, 3],
    cube_value,
)

print(
    transformed_values
)

# transform_all() is a custom map-like higher-order function.

# =============================================================================
# 122. First-Class Functions and Reduction
# =============================================================================


def reduce_values(
    values: list[int],
    operation: Callable[[int, int], int],
    initial: int,
) -> int:
    """Reduce values using a binary operation."""
    result: int = initial

    for value in values:
        result = operation(
            result,
            value,
        )

    return result


def add_reduction(
    first: int,
    second: int,
) -> int:
    """Add values."""
    return first + second


reduction_result: int = reduce_values(
    [1, 2, 3, 4],
    add_reduction,
    0,
)

print(
    reduction_result
)

# The operation itself is passed as a function.

# =============================================================================
# 123. First-Class Functions and Custom Sorting
# =============================================================================


def sort_key_last_character(
    value: str,
) -> str:
    """Return the final character of a string."""
    return value[-1]


sortable_words: list[str] = [
    "Python",
    "Go",
    "Rust",
    "Java",
]

sorted_by_last_character: list[str] = sorted(
    sortable_words,
    key=sort_key_last_character,
)

print(
    sorted_by_last_character
)

# key functions provide custom sorting behaviour.

# =============================================================================
# 124. First-Class Functions and Callable Collections
# =============================================================================


CallableOperation = Callable[[int], int]

callable_operations: list[CallableOperation] = [
    lambda value: value + 1,
    lambda value: value * 2,
    lambda value: value ** 2,
]

callable_collection_value: int = 3

for callable_operation in callable_operations:
    callable_collection_value = callable_operation(
        callable_collection_value,
    )

print(
    callable_collection_value
)

# Lambda functions are also first-class function objects.

# =============================================================================
# 125. First-Class Functions and Runtime Behaviour
# =============================================================================

"""
First-class functions allow behaviour to become data.

Traditional data:

    number = 10

Function as data:

    operation = double

Now a program can select behaviour at runtime:

    operation = add
    operation = multiply
    operation = subtract

and then execute:

    operation(value)

This is one of the major reasons functional programming techniques work
well in Python.
"""

# =============================================================================
# 126. Important Distinction: Function Versus Result
# =============================================================================


def produce_value() -> int:
    """Produce a value."""
    return 123


function_reference_again: Callable[[], int] = produce_value
function_result_again: int = produce_value()

print(
    function_reference_again
)

print(
    function_result_again
)

# Function reference:
#
# produce_value
#
# Function result:
#
# produce_value()
#
# This distinction is essential when working with callbacks.

# =============================================================================
# 127. First-Class Functions and Explicit Behaviour
# =============================================================================


def execute_with_operation(
    value: int,
    operation: Callable[[int], int],
) -> int:
    """Execute a supplied operation."""
    return operation(
        value,
    )


def increment_operation(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


explicit_behaviour_result: int = execute_with_operation(
    20,
    increment_operation,
)

print(
    explicit_behaviour_result
)

# The operation is explicit in the function's parameter.

# =============================================================================
# 128. First-Class Functions and Clean Design
# =============================================================================

"""
A useful design pattern is:

    DATA
      +
    BEHAVIOUR
      ↓
    HIGHER-ORDER FUNCTION

Instead of hard-coding every behaviour:

    if operation == "add":
        ...
    elif operation == "subtract":
        ...
    elif operation == "multiply":
        ...

you can often represent behaviour directly:

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
    }

Then:

    operation = operations[name]
    result = operation(...)

This makes behaviour explicit and easier to extend.
"""

# =============================================================================
# 129. Common Mistakes
# =============================================================================

"""
Common first-class function mistakes include:

- Calling a function when you intended to pass it.
- Passing a function when you intended to call it.
- Forgetting to type-annotate callback parameters.
- Providing a callable with the wrong signature.
- Confusing a function object with its return value.
- Overusing nested functions when a normal function is clearer.
- Using complex dispatch dictionaries when simple conditionals are clearer.
- Forgetting that closures retain references to enclosing values.
- Mutating captured state unnecessarily.
- Using lambda expressions when a named function would be clearer.
- Creating deeply nested callback structures that are difficult to read.
"""

# =============================================================================
# 130. Common Mistake: Wrong Parentheses
# =============================================================================


def greet_for_callback() -> str:
    """Return a greeting."""
    return "Hello"


def execute_greeting(
    callback: Callable[[], str],
) -> str:
    """Execute a greeting callback."""
    return callback()


correct_callback_result: str = execute_greeting(
    greet_for_callback,
)

print(
    correct_callback_result
)

# Correct:
#
# execute_greeting(greet_for_callback)
#
# Wrong:
#
# execute_greeting(greet_for_callback())
#
# The wrong version passes a str instead of a Callable[[], str].

# =============================================================================
# 131. Common Mistake: Overusing Lambdas
# =============================================================================

"""
Lambdas are useful for short expressions.

Example:

    sorted(
        names,
        key=lambda name: len(name),
    )

However, when behaviour becomes complex, a named function is often clearer.

Prefer:

    def get_name_length(
        name: str,
    ) -> int:
        return len(name)

when the function needs:

- Documentation
- Reuse
- Debugging
- Type annotations
- Multiple statements
- A meaningful name
"""

# =============================================================================
# 132. Common Mistake: Overcomplicated Callback Chains
# =============================================================================

"""
First-class functions are powerful, but more abstraction is not always
better.

Prefer straightforward code when the behaviour is simple.

For example:

    result = number * 2

may be clearer than constructing a callback pipeline for a single
multiplication.

Use first-class functions when they provide a real design benefit.
"""

# =============================================================================
# 133. Best Practices
# =============================================================================

"""
Best practices:

1. Use functions as values when behaviour needs to be passed around.

2. Use Callable annotations for callback parameters.

3. Prefer named functions when behaviour is reused or complex.

4. Use lambda for short, simple expressions.

5. Use dispatch dictionaries when mapping names to behaviours.

6. Use function factories when dynamic behaviour is useful.

7. Use closures when captured state is intentional.

8. Keep callback signatures clear.

9. Avoid unnecessarily deep callback nesting.

10. Keep function responsibilities small.

11. Prefer explicit data flow.

12. Use type aliases when Callable signatures become long.

13. Remember the difference between:
       function
   and:
       function()

14. Use first-class functions to separate data from behaviour.

15. Use higher-order functions when they make code easier to extend.
"""

# =============================================================================
# 134. Core First-Class Function Model
# =============================================================================

"""
The core model is:

    FUNCTION
       |
       v
    OBJECT
       |
       +-----------------------+
       |                       |
       v                       v
    STORE                    PASS
       |                       |
       v                       v
    VARIABLE                ARGUMENT
       |                       |
       v                       v
    CALL                    CALLBACK


A function can also:

    FUNCTION
       |
       v
    RETURN
       |
       v
    ANOTHER FUNCTION
       |
       v
    STORE / PASS / CALL

This is the essence of first-class functions.
"""

# =============================================================================
# 135. First-Class Function Checklist
# =============================================================================

"""
A function is first-class if it can participate in normal object operations.

Python functions can:

✓ Be assigned to variables.

✓ Be passed as arguments.

✓ Be returned from functions.

✓ Be stored in lists.

✓ Be stored in tuples.

✓ Be stored in dictionaries.

✓ Be stored in sets.

✓ Be used as dictionary keys.

✓ Be used as dictionary values.

✓ Be selected dynamically.

✓ Be used as callbacks.

✓ Form closures.

✓ Be used in higher-order functions.

✓ Be used with map().

✓ Be used with filter().

✓ Be used with sorted().

✓ Be used with min() and max().

✓ Be used in dispatch tables.

✓ Be used in function factories.

✓ Be used in decorators.

✓ Be represented by Callable type annotations.
"""

# =============================================================================
# 136. Final Practical Example
# =============================================================================


Operation = Callable[[int], int]


def operation_increment(
    value: int,
) -> int:
    """Increment a value."""
    return value + 1


def operation_double_final(
    value: int,
) -> int:
    """Double a value."""
    return value * 2


def operation_square_final(
    value: int,
) -> int:
    """Square a value."""
    return value ** 2


def execute_operations(
    value: int,
    operations: list[Operation],
) -> int:
    """Execute a list of operations in order."""
    result: int = value

    for operation in operations:
        result = operation(
            result,
        )

    return result


final_operations: list[Operation] = [
    operation_increment,
    operation_double_final,
    operation_square_final,
]

final_result: int = execute_operations(
    4,
    final_operations,
)

print(
    final_result
)

# Calculation:
#
# 4
# ↓
# increment
# ↓
# 5
# ↓
# double
# ↓
# 10
# ↓
# square
# ↓
# 100

# =============================================================================
# 137. Final Summary
# =============================================================================

"""
First-class functions are one of Python's most important function features.

Python treats functions as objects.

Therefore:

    def add(
        first: int,
        second: int,
    ) -> int:
        return first + second

can be treated as data:

    operation = add

and then:

    operation(10, 20)

The function can also be passed:

    execute(
        add,
    )

or returned:

    return add

or stored:

    operations = [
        add,
    ]

or mapped:

    operations = {
        "add": add,
    }

This allows Python programs to represent behaviour dynamically.

The most important concepts are:

    FIRST-CLASS FUNCTION
        |
        +--> assign
        |
        +--> pass
        |
        +--> return
        |
        +--> store
        |
        +--> call


Higher-order functions are functions that:

    accept functions

or:

    return functions

Callbacks are functions passed to other functions.

Closures are returned or nested functions that retain access to enclosing
scope variables.

Callable annotations describe callable behaviour:

    Callable[[int], int]

means:

    accepts int
    returns int

A powerful practical pattern is:

    operation_name
          ↓
    dispatch dictionary
          ↓
    function object
          ↓
    function call
          ↓
    result

First-class functions make Python flexible enough to treat behaviour as
data.

Core idea:

    DATA
      +
    BEHAVIOUR
      ↓
    FIRST-CLASS FUNCTIONS
      ↓
    HIGHER-ORDER FUNCTIONS
      ↓
    CALLBACKS / CLOSURES / FUNCTION FACTORIES / DECORATORS
"""

# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Functions are objects in Python.

✓ Functions are first-class objects.

✓ A function can be assigned to a variable.

✓ Multiple variables can reference the same function.

✓ A function can be passed as an argument.

✓ A function can be returned from another function.

✓ A function can be stored in a list.

✓ A function can be stored in a tuple.

✓ A function can be stored in a dictionary.

✓ A function can be stored in a set.

✓ A function can be a dictionary key.

✓ A function can be a dictionary value.

✓ Callbacks are functions passed to other functions.

✓ Higher-order functions accept or return functions.

✓ map() accepts a function.

✓ filter() accepts a function.

✓ sorted() accepts a key function.

✓ min() and max() accept key functions.

✓ Lambda expressions create function objects.

✓ Closures rely on first-class function behaviour.

✓ Function factories return dynamically created functions.

✓ Dispatch dictionaries can map names to function objects.

✓ Callable can be used to type-annotate function parameters.

✓ Callable[[int], int] represents a callable that accepts an int and
  returns an int.

✓ A callable object can also satisfy a Callable annotation.

✓ A function reference and a function call are different:

    function
        ↓
    function object

    function()
        ↓
    return value

✓ First-class functions allow behaviour to be passed through a program
  just like ordinary data.

Final mental model:

    def function(...):
        ...
             |
             v
       FUNCTION OBJECT
             |
       +-----+-----+---------+---------+
       |           |         |         |
       v           v         v         v
     ASSIGN      PASS      RETURN    STORE
       |           |         |         |
       v           v         v         v
    VARIABLE    CALLBACK   FUNCTION  COLLECTION
       |
       v
      CALL
       |
       v
     RESULT


The central idea:

    FUNCTIONS ARE OBJECTS,
    SO FUNCTIONS CAN BE TREATED AS DATA.
"""

# =============================================================================
# End of 17_first_class_functions.py
# =============================================================================