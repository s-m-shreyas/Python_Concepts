# =============================================================================
# 16. Lambda Functions
# =============================================================================
# type: ignore

"""
Python Functions

File:
    16_lambda_functions.py

Topic:
    Lambda Functions

Overview:
    A lambda function is a small anonymous function created using the
    lambda keyword.

    A lambda function can accept any number of parameters, but its body
    must contain exactly one expression.

Basic syntax:

    lambda parameters: expression

Example:

    square = lambda number: number ** 2

    print(square(5))

Lambda functions are commonly used when a short function is needed
temporarily, especially with functions such as:

    - sorted()
    - min()
    - max()
    - map()
    - filter()
    - reduce()
    - key parameters
    - callbacks

Topics covered:

    - What is a lambda function?
    - Lambda syntax
    - Lambda parameters
    - Lambda return values
    - Lambda functions are expressions
    - Assigning lambda functions to variables
    - Calling lambda functions
    - Lambda functions with one parameter
    - Lambda functions with multiple parameters
    - Lambda functions with no parameters
    - Lambda functions with default parameters
    - Lambda functions with keyword arguments
    - Lambda functions with *args
    - Lambda functions with **kwargs
    - Lambda functions and type annotations
    - Lambda functions with conditional expressions
    - Lambda functions with built-in functions
    - Lambda functions with sorted()
    - Lambda functions with min()
    - Lambda functions with max()
    - Lambda functions with map()
    - Lambda functions with filter()
    - Lambda functions with reduce()
    - Lambda functions and closures
    - Lambda functions inside loops
    - Lambda functions and late binding
    - Lambda functions as callbacks
    - Lambda functions and comprehensions
    - Lambda functions versus def
    - Readability of lambda functions
    - Common lambda mistakes
    - Practical lambda patterns
    - Lambda best practices
    - Lambda summary
"""


# =============================================================================
# 01. What Is a Lambda Function?
# =============================================================================
"""
A lambda function is a small anonymous function.

The general syntax is:

    lambda parameters: expression

Example:

    lambda number: number * 2

The lambda function:

    lambda number: number * 2

accepts one parameter:

    number

and returns the result of:

    number * 2

A lambda function does not require a normal def statement.
"""


# =============================================================================
# 02. Basic Lambda Function
# =============================================================================

double = lambda number: number * 2

double_result: int = double(5)

print(double_result)

# Output:
#
# 10


# =============================================================================
# 03. Lambda Function With One Parameter
# =============================================================================

square = lambda number: number ** 2

square_result: int = square(6)

print(square_result)

# Output:
#
# 36


# =============================================================================
# 04. Lambda Function With Multiple Parameters
# =============================================================================

add = lambda first, second: first + second

addition_result: int = add(10, 20)

print(addition_result)

# Output:
#
# 30


# =============================================================================
# 05. Lambda Function With Three Parameters
# =============================================================================

calculate_total = lambda price, quantity, tax: (
    price * quantity
    + tax
)

total_result: float = calculate_total(
    100.0,
    3,
    20.0,
)

print(total_result)

# Output:
#
# 320.0


# =============================================================================
# 06. Lambda Function With No Parameters
# =============================================================================

get_message = lambda: "Hello, Python!"

message_result: str = get_message()

print(message_result)

# Output:
#
# Hello, Python!


# =============================================================================
# 07. Lambda Functions Return Automatically
# =============================================================================
"""
A lambda function does not use an explicit return statement.

For example:

    square = lambda number: number ** 2

The expression:

    number ** 2

is automatically returned.

This:

    lambda number: number ** 2

is conceptually similar to:

    def square(number):
        return number ** 2

A lambda function contains an expression rather than a normal block of
statements.
"""


# =============================================================================
# 08. Lambda Versus def
# =============================================================================

def square_with_def(number: int) -> int:
    """
    Calculate a square using def.
    """
    return number ** 2


square_with_lambda = lambda number: number ** 2

def_result: int = square_with_def(5)
lambda_result: int = square_with_lambda(5)

print(def_result)
print(lambda_result)

# Both produce:
#
# 25


# =============================================================================
# 09. Lambda Is an Expression
# =============================================================================
"""
A lambda expression can be used where an expression is expected.

For example:

    result = (lambda number: number * 2)(10)

The lambda is created and immediately called.

This is called an immediately invoked lambda expression.
"""


# =============================================================================
# 10. Immediately Calling a Lambda
# =============================================================================

immediate_result: int = (
    lambda number: number * 2
)(
    10,
)

print(immediate_result)

# Output:
#
# 20


# =============================================================================
# 11. Lambda With a String
# =============================================================================

get_uppercase = lambda text: text.upper()

uppercase_result: str = get_uppercase(
    "python",
)

print(uppercase_result)

# Output:
#
# PYTHON


# =============================================================================
# 12. Lambda With String Length
# =============================================================================

get_length = lambda text: len(text)

length_result: int = get_length(
    "Python",
)

print(length_result)

# Output:
#
# 6


# =============================================================================
# 13. Lambda With Boolean Expression
# =============================================================================

is_positive = lambda number: number > 0

positive_result: bool = is_positive(
    10,
)

negative_result: bool = is_positive(
    -5,
)

print(positive_result)
print(negative_result)

# Output:
#
# True
# False


# =============================================================================
# 14. Lambda With a Conditional Expression
# =============================================================================
"""
A lambda function can contain a conditional expression.

Syntax:

    lambda value: result_if_true if condition else result_if_false
"""


# =============================================================================
# 15. Even or Odd With Lambda
# =============================================================================

get_parity = lambda number: (
    "even"
    if number % 2 == 0
    else "odd"
)

even_result: str = get_parity(10)
odd_result: str = get_parity(7)

print(even_result)
print(odd_result)

# Output:
#
# even
# odd


# =============================================================================
# 16. Positive or Negative With Lambda
# =============================================================================

get_sign = lambda number: (
    "positive"
    if number > 0
    else "negative"
    if number < 0
    else "zero"
)

print(get_sign(10))
print(get_sign(-10))
print(get_sign(0))

# Output:
#
# positive
# negative
# zero


# =============================================================================
# 17. Lambda With Default Parameter
# =============================================================================

greet = lambda name="Guest": f"Hello, {name}!"

default_greeting: str = greet()

custom_greeting: str = greet(
    "Shreyas",
)

print(default_greeting)
print(custom_greeting)

# Output:
#
# Hello, Guest!
# Hello, Shreyas!


# =============================================================================
# 18. Lambda With Multiple Default Parameters
# =============================================================================

calculate_power = lambda number=2, exponent=2: number ** exponent

power_result: int = calculate_power()

custom_power_result: int = calculate_power(
    3,
    3,
)

print(power_result)
print(custom_power_result)

# Output:
#
# 4
# 27


# =============================================================================
# 19. Lambda With Keyword Arguments
# =============================================================================

subtract = lambda first, second: first - second

keyword_result: int = subtract(
    first=20,
    second=5,
)

print(keyword_result)

# Output:
#
# 15


# =============================================================================
# 20. Lambda With Positional Arguments
# =============================================================================

multiply = lambda first, second: first * second

positional_result: int = multiply(
    4,
    5,
)

print(positional_result)

# Output:
#
# 20


# =============================================================================
# 21. Lambda With Mixed Arguments
# =============================================================================

divide = lambda dividend, divisor=1: dividend / divisor

division_result: float = divide(
    20,
    divisor=4,
)

print(division_result)

# Output:
#
# 5.0


# =============================================================================
# 22. Lambda With *args
# =============================================================================
"""
A lambda can accept variable positional arguments using *args.

Example:

    lambda *values: sum(values)
"""


# =============================================================================
# 23. Lambda With Variable Positional Arguments
# =============================================================================

sum_values = lambda *values: sum(values)

sum_result: int = sum_values(
    10,
    20,
    30,
    40,
)

print(sum_result)

# Output:
#
# 100


# =============================================================================
# 24. Lambda With *args and Another Parameter
# =============================================================================

add_base = lambda base, *values: base + sum(values)

base_result: int = add_base(
    10,
    20,
    30,
)

print(base_result)

# Output:
#
# 60


# =============================================================================
# 25. Lambda With **kwargs
# =============================================================================
"""
A lambda can accept variable keyword arguments using **kwargs.
"""


# =============================================================================
# 26. Lambda With Variable Keyword Arguments
# =============================================================================

count_keyword_arguments = lambda **kwargs: len(kwargs)

keyword_count: int = count_keyword_arguments(
    name="Alex",
    age=30,
    city="Bengaluru",
)

print(keyword_count)

# Output:
#
# 3


# =============================================================================
# 27. Lambda With *args and **kwargs
# =============================================================================

describe_arguments = lambda *args, **kwargs: (
    len(args),
    len(kwargs),
)

argument_description: tuple[int, int] = describe_arguments(
    10,
    20,
    name="Alex",
    city="Bengaluru",
)

print(argument_description)

# Output:
#
# (2, 2)


# =============================================================================
# 28. Lambda and Type Annotations
# =============================================================================
"""
Lambda parameters cannot be annotated using the normal function syntax
inside a lambda expression.

For example, this is not valid lambda syntax:

    lambda number: int: number * 2

Type annotations can instead be applied to the variable receiving the
callable when appropriate.

For example:

    from collections.abc import Callable

    double: Callable[[int], int] = lambda number: number * 2
"""


# =============================================================================
# 29. Typed Lambda Variable
# =============================================================================

from collections.abc import Callable


typed_double: Callable[[int], int] = lambda number: number * 2

typed_double_result: int = typed_double(
    8,
)

print(typed_double_result)

# Output:
#
# 16


# =============================================================================
# 30. Typed Lambda With Multiple Parameters
# =============================================================================

typed_add: Callable[[int, int], int] = (
    lambda first, second: first + second
)

typed_add_result: int = typed_add(
    10,
    15,
)

print(typed_add_result)

# Output:
#
# 25


# =============================================================================
# 31. Lambda With sorted()
# =============================================================================
"""
One of the most common uses of lambda functions is supplying a key
function to sorted().

Example:

    sorted(
        values,
        key=lambda value: value,
    )

The key function determines what value should be used for comparison.
"""


# =============================================================================
# 32. Sort Numbers by Absolute Value
# =============================================================================

numbers: list[int] = [
    -10,
    5,
    -2,
    8,
    -1,
]

sorted_numbers: list[int] = sorted(
    numbers,
    key=lambda number: abs(number),
)

print(sorted_numbers)

# Output:
#
# [-1, -2, 5, 8, -10]


# =============================================================================
# 33. Sort Strings by Length
# =============================================================================

words: list[str] = [
    "Python",
    "Go",
    "JavaScript",
    "SQL",
    "Rust",
]

sorted_words: list[str] = sorted(
    words,
    key=lambda word: len(word),
)

print(sorted_words)

# Output:
#
# ['Go', 'SQL', 'Rust', 'Python', 'JavaScript']


# =============================================================================
# 34. Sort Strings by Reverse Length
# =============================================================================

reverse_length_words: list[str] = sorted(
    words,
    key=lambda word: len(word),
    reverse=True,
)

print(reverse_length_words)

# Output:
#
# ['JavaScript', 'Python', 'Rust', 'SQL', 'Go']


# =============================================================================
# 35. Sort Strings Case-Insensitively
# =============================================================================

mixed_case_words: list[str] = [
    "python",
    "Java",
    "go",
    "Rust",
]

case_insensitive_words: list[str] = sorted(
    mixed_case_words,
    key=lambda word: word.lower(),
)

print(case_insensitive_words)

# Output:
#
# ['go', 'Java', 'python', 'Rust']


# =============================================================================
# 36. Sort Tuples by the Second Element
# =============================================================================

students: list[tuple[str, int]] = [
    ("Alex", 85),
    ("John", 70),
    ("Maria", 95),
    ("David", 80),
]

students_by_score: list[tuple[str, int]] = sorted(
    students,
    key=lambda student: student[1],
)

print(students_by_score)

# Output:
#
# [('John', 70), ('David', 80), ('Alex', 85), ('Maria', 95)]


# =============================================================================
# 37. Sort Tuples by the First Element
# =============================================================================

students_by_name: list[tuple[str, int]] = sorted(
    students,
    key=lambda student: student[0],
)

print(students_by_name)

# Output:
#
# [('Alex', 85), ('David', 80), ('John', 70), ('Maria', 95)]


# =============================================================================
# 38. Sort Dictionaries by a Value
# =============================================================================

employees: list[dict[str, object]] = [
    {
        "name": "Alex",
        "salary": 70000,
    },
    {
        "name": "Maria",
        "salary": 90000,
    },
    {
        "name": "John",
        "salary": 60000,
    },
]

employees_by_salary: list[dict[str, object]] = sorted(
    employees,
    key=lambda employee: int(employee["salary"]),
)

print(employees_by_salary)


# =============================================================================
# 39. Sort Dictionaries by Name
# =============================================================================

employees_by_name: list[dict[str, object]] = sorted(
    employees,
    key=lambda employee: str(employee["name"]),
)

print(employees_by_name)


# =============================================================================
# 40. Lambda With min()
# =============================================================================

minimum_number: int = min(
    numbers,
    key=lambda number: abs(number),
)

print(minimum_number)

# The number closest to zero is selected.


# =============================================================================
# 41. Lambda With max()
# =============================================================================

maximum_number: int = max(
    numbers,
    key=lambda number: abs(number),
)

print(maximum_number)

# The number farthest from zero is selected.


# =============================================================================
# 42. Find Shortest Word
# =============================================================================

shortest_word: str = min(
    words,
    key=lambda word: len(word),
)

print(shortest_word)


# =============================================================================
# 43. Find Longest Word
# =============================================================================

longest_word: str = max(
    words,
    key=lambda word: len(word),
)

print(longest_word)


# =============================================================================
# 44. Lambda With map()
# =============================================================================
"""
map() applies a function to every item in an iterable.

Example:

    map(
        lambda value: value * 2,
        values,
    )

map() returns an iterator.

Convert it to a list when a list is required.
"""


# =============================================================================
# 45. Double Every Number With map()
# =============================================================================

original_numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
]

doubled_numbers: list[int] = list(
    map(
        lambda number: number * 2,
        original_numbers,
    )
)

print(doubled_numbers)

# Output:
#
# [2, 4, 6, 8, 10]


# =============================================================================
# 46. Square Every Number With map()
# =============================================================================

squared_numbers: list[int] = list(
    map(
        lambda number: number ** 2,
        original_numbers,
    )
)

print(squared_numbers)

# Output:
#
# [1, 4, 9, 16, 25]


# =============================================================================
# 47. Convert Strings to Uppercase
# =============================================================================

language_names: list[str] = [
    "python",
    "go",
    "rust",
]

uppercase_languages: list[str] = list(
    map(
        lambda language: language.upper(),
        language_names,
    )
)

print(uppercase_languages)

# Output:
#
# ['PYTHON', 'GO', 'RUST']


# =============================================================================
# 48. Lambda With Multiple Iterables in map()
# =============================================================================

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

combined_numbers: list[int] = list(
    map(
        lambda first, second: first + second,
        first_numbers,
        second_numbers,
    )
)

print(combined_numbers)

# Output:
#
# [11, 22, 33]


# =============================================================================
# 49. Lambda With filter()
# =============================================================================
"""
filter() keeps items for which the supplied function returns True.

Example:

    filter(
        lambda value: value > 10,
        values,
    )
"""


# =============================================================================
# 50. Filter Even Numbers
# =============================================================================

even_numbers: list[int] = list(
    filter(
        lambda number: number % 2 == 0,
        original_numbers,
    )
)

print(even_numbers)

# Output:
#
# [2, 4]


# =============================================================================
# 51. Filter Odd Numbers
# =============================================================================

odd_numbers: list[int] = list(
    filter(
        lambda number: number % 2 != 0,
        original_numbers,
    )
)

print(odd_numbers)

# Output:
#
# [1, 3, 5]


# =============================================================================
# 52. Filter Positive Numbers
# =============================================================================

mixed_numbers: list[int] = [
    -10,
    5,
    -3,
    8,
    0,
    12,
]

positive_numbers: list[int] = list(
    filter(
        lambda number: number > 0,
        mixed_numbers,
    )
)

print(positive_numbers)

# Output:
#
# [5, 8, 12]


# =============================================================================
# 53. Filter Strings by Length
# =============================================================================

long_words: list[str] = list(
    filter(
        lambda word: len(word) > 4,
        words,
    )
)

print(long_words)


# =============================================================================
# 54. Lambda With reduce()
# =============================================================================
"""
reduce() is available from functools.

It repeatedly applies a function to the items of an iterable.

For example:

    reduce(
        lambda first, second: first + second,
        values,
    )

The result is a single value.
"""

from functools import reduce


# =============================================================================
# 55. Sum Values With reduce()
# =============================================================================

reduced_sum: int = reduce(
    lambda first, second: first + second,
    original_numbers,
)

print(reduced_sum)

# Output:
#
# 15


# =============================================================================
# 56. Multiply Values With reduce()
# =============================================================================

reduced_product: int = reduce(
    lambda first, second: first * second,
    original_numbers,
)

print(reduced_product)

# Output:
#
# 120


# =============================================================================
# 57. reduce() With an Initial Value
# =============================================================================

reduced_sum_with_initial: int = reduce(
    lambda first, second: first + second,
    original_numbers,
    100,
)

print(reduced_sum_with_initial)

# Output:
#
# 115


# =============================================================================
# 58. Lambda With any() and all()
# =============================================================================

has_even_number: bool = any(
    map(
        lambda number: number % 2 == 0,
        original_numbers,
    )
)

all_positive: bool = all(
    map(
        lambda number: number > 0,
        original_numbers,
    )
)

print(has_even_number)
print(all_positive)

# Output:
#
# True
# True


# =============================================================================
# 59. Lambda With sorted() and Multiple Criteria
# =============================================================================
"""
A lambda can return a tuple.

This allows multiple sorting criteria.

Example:

    key=lambda item: (item[1], item[0])

Python compares the first tuple element first and then uses the second
element when needed.
"""


# =============================================================================
# 60. Multiple Sorting Criteria
# =============================================================================

products: list[tuple[str, float]] = [
    ("Laptop", 900.0),
    ("Mouse", 50.0),
    ("Keyboard", 50.0),
    ("Monitor", 900.0),
]

products_sorted: list[tuple[str, float]] = sorted(
    products,
    key=lambda product: (
        product[1],
        product[0],
    ),
)

print(products_sorted)


# =============================================================================
# 61. Lambda With Objects
# =============================================================================
"""
Lambda functions can access object attributes.

For example:

    key=lambda student: student.score

This is useful when sorting custom objects.
"""


# =============================================================================
# 62. Lambda With a Dataclass
# =============================================================================

from dataclasses import dataclass


@dataclass
class Student:
    """
    Represent a student.
    """

    name: str
    score: int


student_objects: list[Student] = [
    Student(
        name="Alex",
        score=85,
    ),
    Student(
        name="Maria",
        score=95,
    ),
    Student(
        name="John",
        score=70,
    ),
]

students_sorted_by_score: list[Student] = sorted(
    student_objects,
    key=lambda student: student.score,
)

for student in students_sorted_by_score:
    print(
        student.name,
        student.score,
    )


# =============================================================================
# 63. Lambda as a Callback
# =============================================================================
"""
A callback is a function passed to another function.

Lambda functions are convenient callbacks when the operation is small.
"""


# =============================================================================
# 64. Callback Example
# =============================================================================

def apply_operation(
    first: int,
    second: int,
    operation: Callable[[int, int], int],
) -> int:
    """
    Apply a supplied operation to two integers.
    """
    return operation(
        first,
        second,
    )


callback_add_result: int = apply_operation(
    10,
    20,
    lambda first, second: first + second,
)

callback_multiply_result: int = apply_operation(
    10,
    20,
    lambda first, second: first * second,
)

print(callback_add_result)
print(callback_multiply_result)

# Output:
#
# 30
# 200


# =============================================================================
# 65. Lambda With a Callback
# =============================================================================

def transform_value(
    value: int,
    transformer: Callable[[int], int],
) -> int:
    """
    Transform a value using a callback.
    """
    return transformer(value)


transformed_value: int = transform_value(
    10,
    lambda number: number ** 2,
)

print(transformed_value)

# Output:
#
# 100


# =============================================================================
# 66. Lambda Functions Can Be Stored in Collections
# =============================================================================

operations: dict[str, Callable[[int, int], int]] = {
    "add": lambda first, second: first + second,
    "subtract": lambda first, second: first - second,
    "multiply": lambda first, second: first * second,
}

print(
    operations["add"](
        10,
        5,
    )
)

print(
    operations["subtract"](
        10,
        5,
    )
)

print(
    operations["multiply"](
        10,
        5,
    )
)


# =============================================================================
# 67. Lambda Function Factory
# =============================================================================

def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a multiplier function.
    """
    return lambda number: number * multiplier


double_function: Callable[[int], int] = create_multiplier(
    2,
)

triple_function: Callable[[int], int] = create_multiplier(
    3,
)

print(
    double_function(10)
)

print(
    triple_function(10)
)

# Output:
#
# 20
# 30


# =============================================================================
# 68. Lambda and Closures
# =============================================================================
"""
A lambda can form a closure.

A closure allows a function to remember values from an enclosing scope.

Example:

    def create_multiplier(multiplier):
        return lambda number: number * multiplier

The returned lambda remembers multiplier.

This is an example of an enclosing variable being captured by a function.
"""


# =============================================================================
# 69. Lambda Closure With a Prefix
# =============================================================================

def create_prefix_function(
    prefix: str,
) -> Callable[[str], str]:
    """
    Create a function that adds a prefix.
    """
    return lambda message: f"{prefix}: {message}"


info_message: Callable[[str], str] = create_prefix_function(
    "INFO",
)

error_message: Callable[[str], str] = create_prefix_function(
    "ERROR",
)

print(
    info_message("Application started")
)

print(
    error_message("Application failed")
)


# =============================================================================
# 70. Lambda Closure With a Suffix
# =============================================================================

def create_suffix_function(
    suffix: str,
) -> Callable[[str], str]:
    """
    Create a function that adds a suffix.
    """
    return lambda message: f"{message}{suffix}"


exclamation: Callable[[str], str] = create_suffix_function(
    "!",
)

question: Callable[[str], str] = create_suffix_function(
    "?",
)

print(
    exclamation("Hello")
)

print(
    question("Are you ready")
)


# =============================================================================
# 71. Lambda Inside a Loop
# =============================================================================
"""
Be careful when creating lambdas inside loops.

A lambda defined inside a loop can capture a variable from the enclosing
scope.

The captured variable may be evaluated later rather than immediately.
This is related to late binding.
"""


# =============================================================================
# 72. Late Binding Example
# =============================================================================

functions: list[Callable[[], int]] = []

for number in range(3):
    functions.append(
        lambda: number,
    )

# All functions refer to the same loop variable.
#
# After the loop completes:
#
# number == 2
#
# Therefore each function returns 2.

late_binding_results: list[int] = [
    function()
    for function in functions
]

print(late_binding_results)

# Output:
#
# [2, 2, 2]


# =============================================================================
# 73. Avoid Late Binding With a Default Parameter
# =============================================================================
"""
A common solution is to capture the current value using a default
parameter.

Example:

    lambda number=number: number
"""


# =============================================================================
# 74. Correct Lambda Loop Capture
# =============================================================================

correct_functions: list[Callable[[], int]] = []

for number in range(3):
    correct_functions.append(
        lambda number=number: number,
    )

correct_results: list[int] = [
    function()
    for function in correct_functions
]

print(correct_results)

# Output:
#
# [0, 1, 2]


# =============================================================================
# 75. Lambda and List Comprehension
# =============================================================================

square_functions: list[Callable[[int], int]] = [
    lambda number: number ** 2
    for _ in range(3)
]

print(
    square_functions[0](5)
)

print(
    square_functions[1](6)
)

print(
    square_functions[2](7)
)


# =============================================================================
# 76. Lambda in a Dictionary Comprehension
# =============================================================================

multipliers: dict[int, Callable[[int], int]] = {
    number: (
        lambda value, multiplier=number: value * multiplier
    )
    for number in range(1, 4)
}

print(
    multipliers[1](10)
)

print(
    multipliers[2](10)
)

print(
    multipliers[3](10)
)

# Output:
#
# 10
# 20
# 30


# =============================================================================
# 77. Lambda With Conditional Filtering
# =============================================================================

numbers_77: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
]

even_squared: list[int] = list(
    map(
        lambda number: number ** 2,
        filter(
            lambda number: number % 2 == 0,
            numbers_77,
        ),
    )
)

print(even_squared)

# Output:
#
# [4, 16, 36]


# =============================================================================
# 78. Lambda With map() and filter()
# =============================================================================
"""
Lambda functions can be combined with map() and filter().

However, if the expression becomes difficult to read, a normal named
function or a comprehension is often better.
"""


# =============================================================================
# 79. Lambda Versus List Comprehension
# =============================================================================

numbers_79: list[int] = [
    1,
    2,
    3,
    4,
]

squares_with_map: list[int] = list(
    map(
        lambda number: number ** 2,
        numbers_79,
    )
)

squares_with_comprehension: list[int] = [
    number ** 2
    for number in numbers_79
]

print(squares_with_map)
print(squares_with_comprehension)

# Both produce:
#
# [1, 4, 9, 16]


# =============================================================================
# 80. Lambda Versus Named Function
# =============================================================================

def calculate_square(
    number: int,
) -> int:
    """
    Calculate the square of a number.
    """
    return number ** 2


square_lambda: Callable[[int], int] = (
    lambda number: number ** 2
)

print(
    calculate_square(5)
)

print(
    square_lambda(5)
)

# A named function is generally preferable when:
#
# - The logic is reused.
# - The logic is complex.
# - The function needs documentation.
# - The function needs multiple statements.
# - The function needs a meaningful name.


# =============================================================================
# 81. Lambda Functions Can Only Contain One Expression
# =============================================================================
"""
A lambda function contains exactly one expression.

This is valid:

    lambda number: number * 2

This is valid:

    lambda number: number * 2 if number > 0 else 0

A lambda cannot contain normal statements such as:

    if:
    for:
    while:
    try:
    return:
    assignment statements

when those are used as normal statements inside the lambda body.

For complex logic, use def.
"""


# =============================================================================
# 82. Complex Logic Should Usually Use def
# =============================================================================

def process_number(
    number: int,
) -> int:
    """
    Process a number using multiple steps.
    """
    doubled: int = number * 2
    result: int = doubled + 10

    return result


processed_number: int = process_number(
    5,
)

print(processed_number)


# =============================================================================
# 83. Lambda Readability
# =============================================================================
"""
A lambda should generally be short and easy to understand.

Good example:

    key=lambda student: student.score

Potentially difficult example:

    lambda x: (
        x[1] * 2
        if x[0] > 10
        else x[1] / 2
    )

If a lambda requires extensive nesting or complicated conditions,
consider replacing it with a named function.
"""


# =============================================================================
# 84. Lambda With abs()
# =============================================================================

absolute_value = lambda number: abs(number)

absolute_result: int = absolute_value(
    -25,
)

print(absolute_result)

# Output:
#
# 25


# =============================================================================
# 85. Lambda With round()
# =============================================================================

round_number = lambda number: round(number, 2)

rounded_result: float = round_number(
    10.5678,
)

print(rounded_result)

# Output:
#
# 10.57


# =============================================================================
# 86. Lambda With isinstance()
# =============================================================================

is_integer = lambda value: isinstance(value, int)

integer_check: bool = is_integer(
    100,
)

print(integer_check)

# Output:
#
# True


# =============================================================================
# 87. Lambda Returning a Tuple
# =============================================================================

get_coordinates = lambda point: (
    point[0],
    point[1],
)

coordinate_result: tuple[int, int] = get_coordinates(
    (10, 20),
)

print(coordinate_result)


# =============================================================================
# 88. Lambda Returning a Dictionary
# =============================================================================

create_user = lambda name, age: {
    "name": name,
    "age": age,
}

user_result: dict[str, object] = create_user(
    "Alex",
    30,
)

print(user_result)


# =============================================================================
# 89. Lambda Returning a List
# =============================================================================

create_range = lambda start, end: list(
    range(
        start,
        end,
    )
)

range_result: list[int] = create_range(
    1,
    5,
)

print(range_result)

# Output:
#
# [1, 2, 3, 4]


# =============================================================================
# 90. Lambda With String Formatting
# =============================================================================

format_user = lambda name, age: (
    f"{name} is {age} years old."
)

formatted_user: str = format_user(
    "Alex",
    30,
)

print(formatted_user)


# =============================================================================
# 91. Lambda With Membership Testing
# =============================================================================

contains_python = lambda language: language in {
    "Python",
    "Python 3",
}

python_check: bool = contains_python(
    "Python",
)

print(python_check)


# =============================================================================
# 92. Lambda With a Dictionary Lookup
# =============================================================================

status_codes: dict[int, str] = {
    200: "OK",
    404: "Not Found",
    500: "Server Error",
}

get_status = lambda code: status_codes.get(
    code,
    "Unknown",
)

status_result: str = get_status(
    404,
)

print(status_result)

# Output:
#
# Not Found


# =============================================================================
# 93. Lambda With sorted() and Dictionary Lookup
# =============================================================================

status_items: list[tuple[int, str]] = list(
    status_codes.items()
)

status_items_sorted: list[tuple[int, str]] = sorted(
    status_items,
    key=lambda item: item[0],
)

print(status_items_sorted)


# =============================================================================
# 94. Lambda as a Function Argument
# =============================================================================

def execute(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Execute a supplied function.
    """
    return function(value)


execute_result: int = execute(
    lambda number: number * 10,
    5,
)

print(execute_result)

# Output:
#
# 50


# =============================================================================
# 95. Multiple Lambda Callbacks
# =============================================================================

operations_list: list[Callable[[int], int]] = [
    lambda number: number + 10,
    lambda number: number * 2,
    lambda number: number ** 2,
]

operation_results: list[int] = [
    operation(5)
    for operation in operations_list
]

print(operation_results)

# Output:
#
# [15, 10, 25]


# =============================================================================
# 96. Lambda and Function Composition
# =============================================================================

double_value: Callable[[int], int] = (
    lambda number: number * 2
)

add_ten: Callable[[int], int] = (
    lambda number: number + 10
)

composition_result: int = add_ten(
    double_value(
        5,
    ),
)

print(composition_result)

# Calculation:
#
# 5
# ↓
# double
# ↓
# 10
# ↓
# add 10
# ↓
# 20


# =============================================================================
# 97. Lambda With Nested Expression
# =============================================================================

calculate_average = lambda first, second: (
    first + second
) / 2

average_result: float = calculate_average(
    10,
    20,
)

print(average_result)

# Output:
#
# 15.0


# =============================================================================
# 98. Lambda With a Nested Conditional Expression
# =============================================================================

classify_score = lambda score: (
    "excellent"
    if score >= 90
    else "good"
    if score >= 70
    else "needs improvement"
)

print(classify_score(95))
print(classify_score(80))
print(classify_score(50))


# =============================================================================
# 99. Lambda With String Sorting
# =============================================================================

file_names: list[str] = [
    "report.pdf",
    "image.png",
    "document.docx",
    "data.csv",
]

sorted_files: list[str] = sorted(
    file_names,
    key=lambda file_name: file_name.split(".")[-1],
)

print(sorted_files)


# =============================================================================
# 100. Lambda With Nested Data
# =============================================================================

orders: list[dict[str, object]] = [
    {
        "id": 1,
        "total": 500.0,
    },
    {
        "id": 2,
        "total": 200.0,
    },
    {
        "id": 3,
        "total": 800.0,
    },
]

orders_by_total: list[dict[str, object]] = sorted(
    orders,
    key=lambda order: float(order["total"]),
)

print(orders_by_total)


# =============================================================================
# 101. Lambda With reversed Sorting
# =============================================================================

orders_descending: list[dict[str, object]] = sorted(
    orders,
    key=lambda order: float(order["total"]),
    reverse=True,
)

print(orders_descending)


# =============================================================================
# 102. Lambda With min() and Dictionaries
# =============================================================================

cheapest_order: dict[str, object] = min(
    orders,
    key=lambda order: float(order["total"]),
)

print(cheapest_order)


# =============================================================================
# 103. Lambda With max() and Dictionaries
# =============================================================================

largest_order: dict[str, object] = max(
    orders,
    key=lambda order: float(order["total"]),
)

print(largest_order)


# =============================================================================
# 104. Lambda and any()
# =============================================================================

contains_large_order: bool = any(
    map(
        lambda order: float(order["total"]) > 700,
        orders,
    )
)

print(contains_large_order)


# =============================================================================
# 105. Lambda and all()
# =============================================================================

all_orders_positive: bool = all(
    map(
        lambda order: float(order["total"]) > 0,
        orders,
    )
)

print(all_orders_positive)


# =============================================================================
# 106. Lambda and enumerate()
# =============================================================================

indexed_words: list[tuple[int, str]] = list(
    enumerate(words)
)

sorted_indexed_words: list[tuple[int, str]] = sorted(
    indexed_words,
    key=lambda item: len(item[1]),
)

print(sorted_indexed_words)


# =============================================================================
# 107. Lambda With zip()
# =============================================================================

names: list[str] = [
    "Alex",
    "Maria",
    "John",
]

scores: list[int] = [
    80,
    95,
    70,
]

student_pairs: list[tuple[str, int]] = list(
    zip(
        names,
        scores,
    )
)

sorted_student_pairs: list[tuple[str, int]] = sorted(
    student_pairs,
    key=lambda pair: pair[1],
)

print(sorted_student_pairs)


# =============================================================================
# 108. Lambda With reversed()
# =============================================================================

reverse_sorted_numbers: list[int] = list(
    reversed(
        sorted(
            original_numbers,
            key=lambda number: number,
        )
    )
)

print(reverse_sorted_numbers)


# =============================================================================
# 109. Lambda With map() and String Conversion
# =============================================================================

number_strings: list[str] = list(
    map(
        lambda number: str(number),
        original_numbers,
    )
)

print(number_strings)


# =============================================================================
# 110. Lambda With filter() and String Matching
# =============================================================================

python_related_words: list[str] = list(
    filter(
        lambda word: "py" in word.lower(),
        [
            "Python",
            "Java",
            "PyTorch",
            "Rust",
        ],
    )
)

print(python_related_words)


# =============================================================================
# 111. Lambda With filter() and None
# =============================================================================

values_with_none: list[int | None] = [
    10,
    None,
    20,
    None,
    30,
]

non_none_values: list[int] = [
    value
    for value in values_with_none
    if value is not None
]

print(non_none_values)

# A comprehension is often clearer than:
#
# filter(
#     lambda value: value is not None,
#     values_with_none,
# )
#
# Especially when type narrowing matters.


# =============================================================================
# 112. Lambda With Optional Values
# =============================================================================

optional_values: list[int | None] = [
    10,
    None,
    5,
]

sorted_optional_values: list[int | None] = sorted(
    optional_values,
    key=lambda value: (
        value is None,
        value if value is not None else 0,
    ),
)

print(sorted_optional_values)


# =============================================================================
# 113. Lambda With Case-Insensitive Sorting
# =============================================================================

case_words: list[str] = [
    "banana",
    "Apple",
    "cherry",
    "Apricot",
]

case_sorted_words: list[str] = sorted(
    case_words,
    key=lambda word: word.casefold(),
)

print(case_sorted_words)


# =============================================================================
# 114. Lambda With String Extraction
# =============================================================================

email_addresses: list[str] = [
    "alex@example.com",
    "maria@example.org",
    "john@example.net",
]

sorted_emails: list[str] = sorted(
    email_addresses,
    key=lambda email: email.split("@")[1],
)

print(sorted_emails)


# =============================================================================
# 115. Lambda With Dictionary get()
# =============================================================================

users: list[dict[str, object]] = [
    {
        "name": "Alex",
        "age": 30,
    },
    {
        "name": "Maria",
    },
    {
        "name": "John",
        "age": 25,
    },
]

users_by_age: list[dict[str, object]] = sorted(
    users,
    key=lambda user: int(user.get("age", 0)),
)

print(users_by_age)


# =============================================================================
# 116. Lambda With Multiple Sort Conditions
# =============================================================================

people: list[tuple[str, int]] = [
    ("Alex", 30),
    ("Maria", 25),
    ("John", 30),
    ("David", 25),
]

people_sorted: list[tuple[str, int]] = sorted(
    people,
    key=lambda person: (
        person[1],
        person[0],
    ),
)

print(people_sorted)

# First sort by age.
#
# If ages are equal, sort by name.


# =============================================================================
# 117. Lambda With Descending Primary Criterion
# =============================================================================

people_sorted_descending: list[tuple[str, int]] = sorted(
    people,
    key=lambda person: (
        -person[1],
        person[0],
    ),
)

print(people_sorted_descending)

# Age is descending.
#
# Name is ascending.


# =============================================================================
# 118. Lambda With a Boolean Sort Key
# =============================================================================

tasks: list[tuple[str, bool]] = [
    ("Write documentation", False),
    ("Fix bug", True),
    ("Review code", False),
    ("Deploy application", True),
]

completed_first: list[tuple[str, bool]] = sorted(
    tasks,
    key=lambda task: not task[1],
)

print(completed_first)


# =============================================================================
# 119. Lambda and Closure State
# =============================================================================

def create_offset_function(
    offset: int,
) -> Callable[[int], int]:
    """
    Create a function that remembers an offset.
    """
    return lambda number: number + offset


add_five: Callable[[int], int] = create_offset_function(
    5,
)

add_ten_offset: Callable[[int], int] = create_offset_function(
    10,
)

print(
    add_five(10)
)

print(
    add_ten_offset(10)
)

# Output:
#
# 15
# 20


# =============================================================================
# 120. Lambda With Closure and Default Argument
# =============================================================================

def create_power_function(
    exponent: int,
) -> Callable[[int], int]:
    """
    Create a function that raises a number to an exponent.
    """
    return lambda number: number ** exponent


square_lambda_function: Callable[[int], int] = (
    create_power_function(2)
)

cube_lambda_function: Callable[[int], int] = (
    create_power_function(3)
)

print(
    square_lambda_function(5)
)

print(
    cube_lambda_function(5)
)


# =============================================================================
# 121. Lambda Functions and __name__
# =============================================================================
"""
Lambda functions are anonymous.

When inspecting a lambda function, its __name__ is usually:

    <lambda>

Named functions created with def normally have a meaningful function name.
"""


# =============================================================================
# 122. Inspect Lambda Name
# =============================================================================

named_lambda = lambda number: number * 2

print(named_lambda.__name__)

# Output:
#
# <lambda>


# =============================================================================
# 123. Lambda Functions Are Function Objects
# =============================================================================
"""
A lambda creates a normal function object.

It can therefore be:

    - assigned to a variable
    - passed as an argument
    - returned from another function
    - stored in a collection
    - called
    - used as a callback
    - used to create closures
"""


# =============================================================================
# 124. Lambda Passed to Another Function
# =============================================================================

def execute_twice(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Execute a function twice.
    """
    first_result: int = function(value)
    second_result: int = function(first_result)

    return second_result


twice_result: int = execute_twice(
    lambda number: number + 10,
    5,
)

print(twice_result)

# Calculation:
#
# 5
# ↓
# +10
# ↓
# 15
# ↓
# +10
# ↓
# 25


# =============================================================================
# 125. Lambda Returned From a Function
# =============================================================================

def create_incrementer(
    amount: int,
) -> Callable[[int], int]:
    """
    Return a lambda that increments a number.
    """
    return lambda number: number + amount


increment_by_five: Callable[[int], int] = create_incrementer(
    5,
)

increment_result: int = increment_by_five(
    10,
)

print(increment_result)

# Output:
#
# 15


# =============================================================================
# 126. Lambda Stored in a List
# =============================================================================

transformers: list[Callable[[int], int]] = [
    lambda number: number + 1,
    lambda number: number * 2,
    lambda number: number ** 2,
]

for transformer in transformers:
    print(
        transformer(5)
    )


# =============================================================================
# 127. Lambda Stored in a Tuple
# =============================================================================

math_operations: tuple[
    Callable[[int, int], int],
    Callable[[int, int], int],
] = (
    lambda first, second: first + second,
    lambda first, second: first * second,
)

print(
    math_operations[0](
        5,
        3,
    )
)

print(
    math_operations[1](
        5,
        3,
    )
)


# =============================================================================
# 128. Lambda Stored in a Set
# =============================================================================
"""
Function objects can be stored in sets because function objects are
hashable by identity.

This is rarely necessary in normal application code, but it demonstrates
that lambdas are regular function objects.
"""


# =============================================================================
# 129. Lambda as a Dictionary Value
# =============================================================================

calculator: dict[
    str,
    Callable[[float, float], float],
] = {
    "add": lambda first, second: first + second,
    "subtract": lambda first, second: first - second,
    "multiply": lambda first, second: first * second,
    "divide": lambda first, second: first / second,
}

print(
    calculator["add"](
        10.0,
        5.0,
    )
)

print(
    calculator["subtract"](
        10.0,
        5.0,
    )
)

print(
    calculator["multiply"](
        10.0,
        5.0,
    )
)

print(
    calculator["divide"](
        10.0,
        5.0,
    )
)


# =============================================================================
# 130. Lambda and Dictionary Dispatch
# =============================================================================
"""
Dictionary dispatch can replace a long chain of if/elif statements when
the operation can be represented by simple functions.
"""


# =============================================================================
# 131. Dictionary Dispatch Example
# =============================================================================

def calculate_operation(
operation: str,
first: int,
second: int,
) -> int:
    """
    Perform an arithmetic operation using dictionary dispatch.
    """
    operations_map: dict[
        str,
        Callable[[int, int], int],
    ] = {
        "add": lambda left, right: left + right,
        "subtract": lambda left, right: left - right,
        "multiply": lambda left, right: left * right,
    }

    selected_operation: Callable[[int, int], int] = (
        operations_map.get(
            operation,
            lambda left, right: left,
        )
    )

    return selected_operation(
        first,
        second,
    )


print(
    calculate_operation(
        "add",
        10,
        5,
    )
)

print(
    calculate_operation(
        "multiply",
        10,
        5,
    )
)


# =============================================================================
# 132. Lambda and Readability
# =============================================================================
"""
Lambda functions are useful when the function is:

    - short
    - simple
    - used once
    - used as a callback
    - used as a sorting key
    - used as a small transformation

For example:

    sorted(
        students,
        key=lambda student: student.score,
    )

This is concise and readable.

A lambda becomes less useful when the logic needs several operations,
conditions, comments, or detailed documentation.

In those cases, use def.
"""


# =============================================================================
# 133. Prefer Named Functions for Complex Logic
# =============================================================================

def classify_number(
    number: int,
) -> str:
    """
    Classify an integer according to its sign and parity.
    """
    if number == 0:
        return "zero"

    if number > 0:
        if number % 2 == 0:
            return "positive even"

        return "positive odd"

    if number % 2 == 0:
        return "negative even"

    return "negative odd"


classified_number: str = classify_number(
    -7,
)

print(classified_number)

# A named function is clearer here than attempting to express all of
# this logic in a lambda.


# =============================================================================
# 134. Lambda Should Not Replace Every Function
# =============================================================================
"""
This is technically possible:

    classify = lambda number: (
        "zero"
        if number == 0
        else "positive"
        if number > 0
        else "negative"
    )

But if the logic becomes complicated, a normal def is usually easier
to read, test, debug, document, and maintain.
"""


# =============================================================================
# 135. Lambda Debugging
# =============================================================================
"""
Lambda functions have no useful custom name by default.

This can make debugging and stack traces less descriptive.

Compare:

    lambda number: number * 2

with:

    def double(number):
        return number * 2

The named function communicates its purpose more clearly.

For reusable or important logic, prefer def.
"""


# =============================================================================
# 136. Lambda and Documentation
# =============================================================================
"""
Lambda functions do not support normal multi-line function bodies or
normal docstrings in the same way as functions created with def.

If a function needs substantial documentation, that is often a sign
that a named function should be used instead.
"""


# =============================================================================
# 137. Lambda and Testing
# =============================================================================
"""
A small lambda used as a temporary callback usually does not need its own
test.

A reusable business rule should normally be implemented as a named
function so that it can be tested independently.

For example, prefer:

    def calculate_discount(...):
        ...

over hiding an important business rule inside:

    lambda value: ...

when the logic is reused or significant.
"""


# =============================================================================
# 138. Lambda With a Generator
# =============================================================================

generate_squares = lambda values: (
    number ** 2
    for number in values
)

square_generator = generate_squares(
    [1, 2, 3, 4],
)

generated_squares: list[int] = list(
    square_generator
)

print(generated_squares)


# =============================================================================
# 139. Lambda Returning an Iterator
# =============================================================================

create_numbers = lambda start, end: iter(
    range(
        start,
        end,
    )
)

number_iterator = create_numbers(
    1,
    5,
)

print(
    list(number_iterator)
)


# =============================================================================
# 140. Lambda With Membership in a Tuple
# =============================================================================

is_weekend = lambda day: day in (
    "Saturday",
    "Sunday",
)

print(
    is_weekend("Saturday")
)

print(
    is_weekend("Monday")
)


# =============================================================================
# 141. Lambda With Dictionary get()
# =============================================================================

get_role = lambda user: str(
    user.get(
        "role",
        "guest",
    )
)

role_result: str = get_role(
    {
        "name": "Alex",
        "role": "admin",
    }
)

print(role_result)


# =============================================================================
# 142. Lambda With Nested Dictionary Data
# =============================================================================

accounts: list[dict[str, object]] = [
    {
        "name": "Alex",
        "profile": {
            "age": 30,
        },
    },
    {
        "name": "Maria",
        "profile": {
            "age": 25,
        },
    },
]

accounts_by_age: list[dict[str, object]] = sorted(
    accounts,
    key=lambda account: int(
        account["profile"]["age"]  # type: ignore[index]
    ),
)

print(accounts_by_age)


# =============================================================================
# 143. Lambda With object Attribute
# =============================================================================

student_names_sorted: list[Student] = sorted(
    student_objects,
    key=lambda student: student.name,
)

for student in student_names_sorted:
    print(student.name)


# =============================================================================
# 144. Lambda With Dataclass Multiple Fields
# =============================================================================

student_objects_sorted: list[Student] = sorted(
    student_objects,
    key=lambda student: (
        -student.score,
        student.name,
    ),
)

for student in student_objects_sorted:
    print(
        student.name,
        student.score,
    )


# =============================================================================
# 145. Lambda With Callable Type
# =============================================================================

def apply_transform(
    value: int,
    transform: Callable[[int], int],
) -> int:
    """
    Apply a callable transformation.
    """
    return transform(value)


transform_result: int = apply_transform(
    10,
    lambda number: number + 100,
)

print(transform_result)


# =============================================================================
# 146. Lambda With Nested Calls
# =============================================================================

nested_lambda_result: str = (
    lambda text: text.upper()
)(
    "hello",
)

print(nested_lambda_result)


# =============================================================================
# 147. Lambda With String Strip
# =============================================================================

clean_text = lambda text: text.strip()

cleaned_result: str = clean_text(
    "   Python   ",
)

print(cleaned_result)


# =============================================================================
# 148. Lambda With String Replacement
# =============================================================================

replace_spaces = lambda text: text.replace(
    " ",
    "_",
)

replacement_result: str = replace_spaces(
    "hello world",
)

print(replacement_result)


# =============================================================================
# 149. Lambda With String Split
# =============================================================================

split_words = lambda text: text.split()

split_result: list[str] = split_words(
    "Python is powerful",
)

print(split_result)


# =============================================================================
# 150. Lambda With String Join
# =============================================================================

join_words = lambda words: ", ".join(words)

joined_result: str = join_words(
    [
        "Python",
        "Go",
        "Rust",
    ]
)

print(joined_result)


# =============================================================================
# 151. Lambda With Numeric Conversion
# =============================================================================

to_integer = lambda value: int(value)

integer_result: int = to_integer(
    "100",
)

print(integer_result)


# =============================================================================
# 152. Lambda With Floating-Point Conversion
# =============================================================================

to_float = lambda value: float(value)

float_result: float = to_float(
    "12.50",
)

print(float_result)


# =============================================================================
# 153. Lambda With Boolean Conversion
# =============================================================================

to_boolean = lambda value: bool(value)

boolean_result: bool = to_boolean(
    1,
)

print(boolean_result)


# =============================================================================
# 154. Lambda With Comparison
# =============================================================================

is_greater_than_ten = lambda value: value > 10

print(
    is_greater_than_ten(20)
)

print(
    is_greater_than_ten(5)
)


# =============================================================================
# 155. Lambda With Multiple Conditions
# =============================================================================

is_valid_score = lambda score: (
    0 <= score <= 100
)

print(
    is_valid_score(85)
)

print(
    is_valid_score(120)
)


# =============================================================================
# 156. Lambda With Arithmetic Expression
# =============================================================================

calculate_percentage = lambda value, total: (
    value / total * 100
)

percentage_result: float = calculate_percentage(
    25,
    50,
)

print(percentage_result)

# Output:
#
# 50.0


# =============================================================================
# 157. Lambda With Rounding
# =============================================================================

calculate_percentage_rounded = lambda value, total: round(
    value / total * 100,
    2,
)

rounded_percentage: float = calculate_percentage_rounded(
    1,
    3,
)

print(rounded_percentage)

# Output:
#
# 33.33


# =============================================================================
# 158. Lambda With Absolute Difference
# =============================================================================

absolute_difference = lambda first, second: abs(
    first - second
)

difference_result: int = absolute_difference(
    10,
    25,
)

print(difference_result)

# Output:
#
# 15


# =============================================================================
# 159. Lambda With Maximum of Two Values
# =============================================================================

maximum_value = lambda first, second: max(
    first,
    second,
)

print(
    maximum_value(
        10,
        25,
    )
)


# =============================================================================
# 160. Lambda With Minimum of Two Values
# =============================================================================

minimum_value = lambda first, second: min(
    first,
    second,
)

print(
    minimum_value(
        10,
        25,
    )
)


# =============================================================================
# 161. Lambda With Tuple Unpacking
# =============================================================================
"""
Lambda parameters can unpack values indirectly through indexing or
through a single iterable parameter.

For clarity, direct tuple unpacking in lambda parameters is not supported
using the old Python syntax.

Use:

    lambda pair: pair[0] + pair[1]

instead.
"""


# =============================================================================
# 162. Lambda With a Pair
# =============================================================================

sum_pair = lambda pair: pair[0] + pair[1]

pair_sum_result: int = sum_pair(
    (10, 20),
)

print(pair_sum_result)


# =============================================================================
# 163. Lambda With a Record
# =============================================================================

get_record_name = lambda record: record["name"]

record_name: str = str(
    get_record_name(
        {
            "name": "Alex",
            "age": 30,
        }
    )
)

print(record_name)


# =============================================================================
# 164. Lambda With a Record Field
# =============================================================================

record_age = lambda record: int(
    record["age"]
)

age_result: int = record_age(
    {
        "name": "Alex",
        "age": 30,
    }
)

print(age_result)


# =============================================================================
# 165. Lambda With sorted() Key Function
# =============================================================================

records: list[tuple[str, int, float]] = [
    ("A", 2, 50.0),
    ("B", 1, 80.0),
    ("C", 2, 20.0),
]

records_sorted: list[tuple[str, int, float]] = sorted(
    records,
    key=lambda record: (
        record[1],
        record[2],
    ),
)

print(records_sorted)


# =============================================================================
# 166. Lambda With Custom Priority
# =============================================================================

priority_order: dict[str, int] = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
}

issues: list[tuple[str, str]] = [
    ("Fix documentation", "low"),
    ("Database failure", "critical"),
    ("UI issue", "medium"),
    ("API timeout", "high"),
]

issues_sorted: list[tuple[str, str]] = sorted(
    issues,
    key=lambda issue: priority_order[issue[1]],
)

print(issues_sorted)


# =============================================================================
# 167. Lambda With Custom Priority and Name
# =============================================================================

issues_sorted_full: list[tuple[str, str]] = sorted(
    issues,
    key=lambda issue: (
        priority_order[issue[1]],
        issue[0],
    ),
)

print(issues_sorted_full)


# =============================================================================
# 168. Lambda With map() and Enumerate
# =============================================================================

indexed_numbers: list[tuple[int, int]] = list(
    map(
        lambda item: (
            item[0],
            item[1] ** 2,
        ),
        enumerate(original_numbers),
    )
)

print(indexed_numbers)


# =============================================================================
# 169. Lambda With filter() and enumerate
# =============================================================================

indexed_even_numbers: list[tuple[int, int]] = list(
    filter(
        lambda item: item[1] % 2 == 0,
        enumerate(original_numbers),
    )
)

print(indexed_even_numbers)


# =============================================================================
# 170. Lambda With reduce() for Maximum
# =============================================================================

maximum_reduced: int = reduce(
    lambda first, second: (
        first
        if first > second
        else second
    ),
    original_numbers,
)

print(maximum_reduced)


# =============================================================================
# 171. Lambda With reduce() for Minimum
# =============================================================================

minimum_reduced: int = reduce(
    lambda first, second: (
        first
        if first < second
        else second
    ),
    original_numbers,
)

print(minimum_reduced)


# =============================================================================
# 172. Lambda With reduce() for String Concatenation
# =============================================================================

concatenated_words: str = reduce(
    lambda first, second: f"{first} {second}",
    [
        "Python",
        "is",
        "powerful",
    ],
)

print(concatenated_words)


# =============================================================================
# 173. Lambda and Side Effects
# =============================================================================
"""
Lambda functions should generally be used for expressions without side
effects.

Avoid using lambdas to hide complicated side effects.

For example, code such as:

    lambda value: print(value)

is technically possible, but a normal function is often clearer if
the operation is meaningful or reused.
"""


# =============================================================================
# 174. Simple Lambda Callback
# =============================================================================

def display_value(
    value: int,
    callback: Callable[[int], int],
) -> int:
    """
    Transform a value through a callback.
    """
    return callback(value)


display_result: int = display_value(
    10,
    lambda number: number * 3,
)

print(display_result)


# =============================================================================
# 175. Lambda With a Predicate
# =============================================================================
"""
A predicate is a function that returns True or False.

Lambda functions are commonly used as predicates.

Examples:

    lambda number: number > 10

    lambda word: word.startswith("P")
"""


# =============================================================================
# 176. Predicate Example
# =============================================================================

is_large = lambda number: number > 100

large_values: list[int] = list(
    filter(
        is_large,
        [
            50,
            100,
            150,
            200,
        ],
    )
)

print(large_values)


# =============================================================================
# 177. Lambda With startswith()
# =============================================================================

starts_with_p = lambda word: word.lower().startswith("p")

p_words: list[str] = list(
    filter(
        starts_with_p,
        [
            "Python",
            "Java",
            "PyTorch",
            "Rust",
        ],
    )
)

print(p_words)


# =============================================================================
# 178. Lambda With endswith()
# =============================================================================

ends_with_n = lambda word: word.lower().endswith("n")

n_words: list[str] = list(
    filter(
        ends_with_n,
        words,
    )
)

print(n_words)


# =============================================================================
# 179. Lambda With Character Count
# =============================================================================

count_a = lambda text: text.lower().count("a")

a_count: int = count_a(
    "Banana",
)

print(a_count)


# =============================================================================
# 180. Lambda With a Nested Function
# =============================================================================

def create_formatter(
    prefix: str,
) -> Callable[[str], str]:
    """
    Return a lambda formatter.
    """
    formatter: Callable[[str], str] = (
        lambda message: f"{prefix}: {message}"
    )

    return formatter


formatter: Callable[[str], str] = create_formatter(
    "DEBUG"
)

formatted_message: str = formatter(
    "Value loaded",
)

print(formatted_message)


# =============================================================================
# 181. Lambda With a Closure Capturing Multiple Values
# =============================================================================

def create_calculator(
    multiplier: int,
    offset: int,
) -> Callable[[int], int]:
    """
    Create a calculator using captured values.
    """
    return lambda number: (
        number * multiplier
        + offset
    )


calculator_function: Callable[[int], int] = create_calculator(
    2,
    10,
)

calculator_result: int = calculator_function(
    5,
)

print(calculator_result)

# Calculation:
#
# 5 * 2 + 10
#
# 20


# =============================================================================
# 182. Lambda With Closure and Default Value
# =============================================================================

def create_greeter(
    default_name: str,
) -> Callable[[str], str]:
    """
    Create a greeting function.
    """
    return lambda name=default_name: (
        f"Hello, {name}!"
    )


default_greeter: Callable[[str], str] = create_greeter(
    "Guest"
)

print(
    default_greeter()
)

print(
    default_greeter("Alex")
)


# =============================================================================
# 183. Lambda and Assignment Expressions
# =============================================================================
"""
A lambda can technically use an assignment expression with the walrus
operator in contexts where the expression is valid.

Example:

    lambda value: (
        doubled := value * 2
    )

However, this can reduce readability.

Prefer a normal named function if intermediate values are needed.
"""


# =============================================================================
# 184. Simple Assignment Expression Lambda
# =============================================================================

double_with_assignment = lambda value: (
    doubled := value * 2
)

assignment_expression_result: int = (
    double_with_assignment(10)
)

print(assignment_expression_result)


# =============================================================================
# 185. Lambda With Nested Function Call
# =============================================================================

normalize_name = lambda name: name.strip().title()

normalized_name: str = normalize_name(
    "   alex smith   ",
)

print(normalized_name)


# =============================================================================
# 186. Lambda With Data Normalization
# =============================================================================

normalize_email = lambda email: email.strip().lower()

normalized_email: str = normalize_email(
    "  ALEX@EXAMPLE.COM  ",
)

print(normalized_email)


# =============================================================================
# 187. Lambda With URL Normalization
# =============================================================================

normalize_url = lambda url: url.strip().rstrip("/")

normalized_url: str = normalize_url(
    "https://example.com///",
)

print(normalized_url)


# =============================================================================
# 188. Lambda With File Extension
# =============================================================================

get_extension = lambda filename: filename.rsplit(
    ".",
    1,
)[-1]

extension_result: str = get_extension(
    "report.pdf",
)

print(extension_result)


# =============================================================================
# 189. Lambda With File Name
# =============================================================================

get_filename = lambda path: path.rsplit(
    "/",
    1,
)[-1]

filename_result: str = get_filename(
    "/home/user/report.pdf",
)

print(filename_result)


# =============================================================================
# 190. Lambda With Data Transformation
# =============================================================================

raw_values: list[str] = [
    "10",
    "20",
    "30",
]

integer_values: list[int] = list(
    map(
        lambda value: int(value),
        raw_values,
    )
)

print(integer_values)


# =============================================================================
# 191. Lambda With Filtering Empty Strings
# =============================================================================

raw_text_values: list[str] = [
    "Python",
    "",
    "Go",
    "",
    "Rust",
]

non_empty_values: list[str] = list(
    filter(
        lambda value: bool(value),
        raw_text_values,
    )
)

print(non_empty_values)


# =============================================================================
# 192. Lambda With Filtering Whitespace
# =============================================================================

raw_text_values_with_spaces: list[str] = [
    "Python",
    "   ",
    "Go",
    "",
    "Rust",
]

non_blank_values: list[str] = list(
    filter(
        lambda value: bool(value.strip()),
        raw_text_values_with_spaces,
    )
)

print(non_blank_values)


# =============================================================================
# 193. Lambda With Case Conversion
# =============================================================================

lowercase_words: list[str] = list(
    map(
        lambda word: word.lower(),
        words,
    )
)

print(lowercase_words)


# =============================================================================
# 194. Lambda With Title Conversion
# =============================================================================

title_words: list[str] = list(
    map(
        lambda word: word.title(),
        words,
    )
)

print(title_words)


# =============================================================================
# 195. Lambda With Numeric Transformation
# =============================================================================

percentage_values: list[float] = list(
    map(
        lambda number: number / 100,
        [
            10,
            25,
            50,
        ],
    )
)

print(percentage_values)


# =============================================================================
# 196. Lambda With Filtering Ranges
# =============================================================================

range_values: list[int] = list(
    filter(
        lambda number: 10 <= number <= 20,
        range(
            1,
            31,
        ),
    )
)

print(range_values)


# =============================================================================
# 197. Lambda With Sorting by Absolute Difference
# =============================================================================

target: int = 50

closest_numbers: list[int] = sorted(
    [
        10,
        45,
        70,
        55,
        20,
    ],
    key=lambda number: abs(
        number - target
    ),
)

print(closest_numbers)


# =============================================================================
# 198. Lambda With Sorting by Digit Count
# =============================================================================

digit_sorted_numbers: list[int] = sorted(
    [
        1,
        100,
        20,
        5000,
        30,
    ],
    key=lambda number: len(
        str(number)
    ),
)

print(digit_sorted_numbers)


# =============================================================================
# 199. Lambda With Sorting by String Representation
# =============================================================================

string_sorted_numbers: list[int] = sorted(
    [
        10,
        2,
        1,
        20,
    ],
    key=lambda number: str(number),
)

print(string_sorted_numbers)


# =============================================================================
# 200. Lambda Core Exercise
# =============================================================================
"""
Exercise:

Create a lambda function that accepts a number and returns its cube.

Expected behaviour:

    cube(3) -> 27
    cube(4) -> 64
"""


# =============================================================================
# 201. Exercise Solution: Cube
# =============================================================================

cube = lambda number: number ** 3

cube_exercise_result: int = cube(
    3,
)

print(cube_exercise_result)

# Output:
#
# 27


# =============================================================================
# 202. Lambda Exercise: Even Check
# =============================================================================
"""
Exercise:

Create a lambda that returns True when a number is even.
"""


# =============================================================================
# 203. Exercise Solution: Even Check
# =============================================================================

is_even = lambda number: number % 2 == 0

print(
    is_even(10)
)

print(
    is_even(7)
)


# =============================================================================
# 204. Lambda Exercise: Larger Number
# =============================================================================
"""
Exercise:

Create a lambda that returns the larger of two numbers.
"""


# =============================================================================
# 205. Exercise Solution: Larger Number
# =============================================================================

larger = lambda first, second: max(
    first,
    second,
)

print(
    larger(
        10,
        20,
    )
)


# =============================================================================
# 206. Lambda Exercise: String Length
# =============================================================================
"""
Exercise:

Create a lambda that returns the length of a string.
"""


# =============================================================================
# 207. Exercise Solution: String Length
# =============================================================================

string_length = lambda text: len(text)

print(
    string_length("Python")
)


# =============================================================================
# 208. Lambda Exercise: Sort by Length
# =============================================================================
"""
Exercise:

Sort a list of words by length using a lambda.
"""


# =============================================================================
# 209. Exercise Solution: Sort by Length
# =============================================================================

exercise_words: list[str] = [
    "Python",
    "Go",
    "JavaScript",
    "Rust",
]

exercise_sorted_words: list[str] = sorted(
    exercise_words,
    key=lambda word: len(word),
)

print(exercise_sorted_words)


# =============================================================================
# 210. Lambda Exercise: Filter Even Numbers
# =============================================================================
"""
Exercise:

Filter a list so that only even numbers remain.
"""


# =============================================================================
# 211. Exercise Solution: Filter Even Numbers
# =============================================================================

exercise_numbers: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
]

exercise_even_numbers: list[int] = list(
    filter(
        lambda number: number % 2 == 0,
        exercise_numbers,
    )
)

print(exercise_even_numbers)


# =============================================================================
# 212. Lambda Exercise: Double Values
# =============================================================================
"""
Exercise:

Use map() and lambda to double every number.
"""


# =============================================================================
# 213. Exercise Solution: Double Values
# =============================================================================

exercise_doubled_numbers: list[int] = list(
    map(
        lambda number: number * 2,
        exercise_numbers,
    )
)

print(exercise_doubled_numbers)


# =============================================================================
# 214. Lambda Exercise: Square Even Numbers
# =============================================================================
"""
Exercise:

Use filter() and map() with lambda to produce the squares of even numbers.
"""


# =============================================================================
# 215. Exercise Solution: Square Even Numbers
# =============================================================================

square_even_numbers: list[int] = list(
    map(
        lambda number: number ** 2,
        filter(
            lambda number: number % 2 == 0,
            exercise_numbers,
        ),
    )
)

print(square_even_numbers)


# =============================================================================
# 216. Lambda Exercise: Sort Students by Score
# =============================================================================
"""
Exercise:

Sort Student objects by their score.
"""


# =============================================================================
# 217. Exercise Solution: Sort Students by Score
# =============================================================================

exercise_students_by_score: list[Student] = sorted(
    student_objects,
    key=lambda student: student.score,
)

for student in exercise_students_by_score:
    print(
        student.name,
        student.score,
    )


# =============================================================================
# 218. Lambda Exercise: Sort by Score Descending
# =============================================================================

exercise_students_descending: list[Student] = sorted(
    student_objects,
    key=lambda student: student.score,
    reverse=True,
)

for student in exercise_students_descending:
    print(
        student.name,
        student.score,
    )


# =============================================================================
# 219. Lambda Exercise: Find Highest Score
# =============================================================================

highest_score_student: Student = max(
    student_objects,
    key=lambda student: student.score,
)

print(
    highest_score_student.name,
    highest_score_student.score,
)


# =============================================================================
# 220. Lambda Exercise: Find Lowest Score
# =============================================================================

lowest_score_student: Student = min(
    student_objects,
    key=lambda student: student.score,
)

print(
    lowest_score_student.name,
    lowest_score_student.score,
)


# =============================================================================
# 221. Lambda Exercise: Create a Multiplier
# =============================================================================

def create_multiplier_exercise(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Return a lambda that multiplies a number.
    """
    return lambda number: number * multiplier


exercise_double: Callable[[int], int] = (
    create_multiplier_exercise(2)
)

exercise_triple: Callable[[int], int] = (
    create_multiplier_exercise(3)
)

print(
    exercise_double(10)
)

print(
    exercise_triple(10)
)


# =============================================================================
# 222. Lambda Exercise: Create a Prefixer
# =============================================================================

def create_prefixer(
    prefix: str,
) -> Callable[[str], str]:
    """
    Return a lambda that adds a prefix.
    """
    return lambda text: f"{prefix}{text}"


error_prefixer: Callable[[str], str] = create_prefixer(
    "ERROR: "
)

print(
    error_prefixer("Something went wrong")
)


# =============================================================================
# 223. Lambda Exercise: Dictionary Dispatch
# =============================================================================

def execute_math_operation(
    operation: str,
    first: int,
    second: int,
) -> int:
    """
    Execute a simple math operation.
    """
    operation_map: dict[
        str,
        Callable[[int, int], int],
    ] = {
        "add": lambda left, right: left + right,
        "subtract": lambda left, right: left - right,
        "multiply": lambda left, right: left * right,
    }

    operation_function: Callable[[int, int], int] = (
        operation_map.get(
            operation,
            lambda left, right: 0,
        )
    )

    return operation_function(
        first,
        second,
    )


print(
    execute_math_operation(
        "add",
        10,
        20,
    )
)

print(
    execute_math_operation(
        "multiply",
        10,
        20,
    )
)


# =============================================================================
# 224. Lambda Best Practices
# =============================================================================
"""
Best practices:

1. Use lambda for short expressions.

2. Use lambda when a small function is needed temporarily.

3. Lambda is especially useful with:
       - sorted()
       - min()
       - max()
       - map()
       - filter()

4. Prefer def for reusable functions.

5. Prefer def for complex logic.

6. Prefer def when documentation is important.

7. Prefer def when meaningful function names improve readability.

8. Avoid deeply nested lambda expressions.

9. Avoid hiding important business logic inside lambdas.

10. Be careful with lambda functions created inside loops because of
    late binding.

11. Use a default parameter when you intentionally need to capture the
    current loop value.

12. Prefer comprehensions when they are clearer than map() and filter().

13. Use Callable type annotations when a lambda is stored in a typed
    variable or passed as a callback.

14. Do not use lambda merely because it is shorter.

15. Choose the clearest implementation.
"""


# =============================================================================
# 225. Lambda Versus Comprehension
# =============================================================================
"""
These two approaches can produce the same result.

Using map():

    list(
        map(
            lambda number: number * 2,
            numbers,
        )
    )

Using a comprehension:

    [
        number * 2
        for number in numbers
    ]

The comprehension is often considered more readable for simple
transformations.

Both approaches are valid.
"""


# =============================================================================
# 226. Lambda Versus def: Quick Comparison
# =============================================================================
"""
Lambda:

    double = lambda number: number * 2

def:

    def double(number):
        return number * 2

Lambda characteristics:

    - anonymous
    - one expression
    - concise
    - useful for callbacks
    - useful for key functions

def characteristics:

    - named
    - supports multiple statements
    - supports normal documentation
    - easier to debug
    - better for reusable logic
"""


# =============================================================================
# 227. Lambda Syntax Summary
# =============================================================================
"""
Basic:

    lambda: expression

One parameter:

    lambda value: expression

Multiple parameters:

    lambda first, second: expression

Default parameter:

    lambda value=10: expression

Variable positional arguments:

    lambda *values: expression

Variable keyword arguments:

    lambda **kwargs: expression

Conditional expression:

    lambda value: (
        result_if_true
        if condition
        else result_if_false
    )

Immediately called:

    (lambda value: value * 2)(10)
"""


# =============================================================================
# 228. Lambda and LEGB
# =============================================================================
"""
Lambda functions follow the same normal Python name-resolution rules.

A lambda can access:

    - its local parameters
    - enclosing variables
    - global variables
    - built-in names

Example:

    multiplier = 2

    multiply = lambda number: number * multiplier

The lambda reads multiplier from global scope.

Nested lambdas can also capture enclosing variables.
"""


# =============================================================================
# 229. Lambda With Global Variable
# =============================================================================

global_multiplier: int = 10

multiply_by_global = lambda number: (
    number * global_multiplier
)

global_lambda_result: int = multiply_by_global(
    5,
)

print(global_lambda_result)

# Output:
#
# 50


# =============================================================================
# 230. Lambda With Enclosing Variable
# =============================================================================

def create_global_style_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a lambda using an enclosing variable.
    """
    return lambda number: number * multiplier


enclosing_multiplier: Callable[[int], int] = (
    create_global_style_multiplier(10)
)

print(
    enclosing_multiplier(5)
)


# =============================================================================
# 231. Lambda Name Shadowing
# =============================================================================
"""
A lambda parameter can shadow an outer variable.

For example:

    value = 100

    function = lambda value: value * 2

The lambda parameter value is local to the lambda invocation.

It shadows the outer value while the lambda executes.
"""


# =============================================================================
# 232. Lambda Parameter Shadowing
# =============================================================================

value: int = 100

double_shadowed = lambda value: value * 2

shadowing_result: int = double_shadowed(
    5,
)

print(shadowing_result)
print(value)

# Output:
#
# 10
# 100


# =============================================================================
# 233. Lambda and Default Evaluation
# =============================================================================
"""
Default parameter expressions are evaluated when the lambda is created,
just like default parameters in normal functions.
"""


# =============================================================================
# 234. Lambda Default Evaluation Example
# =============================================================================

default_multiplier: int = 10

multiply_with_default = lambda number, multiplier=default_multiplier:\
      number * multiplier

default_multiplier = 20

default_evaluation_result: int = multiply_with_default(
    5,
)

print(default_evaluation_result)

# Output:
#
# 50


# =============================================================================
# 235. Lambda With a Mutable Default
# =============================================================================
"""
Lambda functions follow the same default-argument behaviour as normal
functions.

Mutable default arguments should generally be avoided when the object
is intended to be fresh for each call.

Prefer immutable defaults or explicit initialization.
"""


# =============================================================================
# 236. Lambda With None Default
# =============================================================================

create_message_with_default = lambda message=None: (
    "No message"
    if message is None
    else message
)

print(
    create_message_with_default()
)

print(
    create_message_with_default(
        "Hello"
    )
)


# =============================================================================
# 237. Lambda With Exception-Producing Expression
# =============================================================================
"""
A lambda can contain an expression that raises an exception.

The lambda itself is created successfully, but calling it may raise the
exception.
"""


# =============================================================================
# 238. Lambda Division Example
# =============================================================================

safe_divide = lambda first, second: first / second

safe_division_result: float = safe_divide(
    10,
    2,
)

print(safe_division_result)

# Do not call:
#
# safe_divide(10, 0)
#
# because that would raise ZeroDivisionError.


# =============================================================================
# 239. Lambda With Safe Conditional
# =============================================================================

safe_divide_with_check = lambda first, second: (
    first / second
    if second != 0
    else 0.0
)

print(
    safe_divide_with_check(
        10,
        2,
    )
)

print(
    safe_divide_with_check(
        10,
        0,
    )
)


# =============================================================================
# 240. Lambda With Boolean Logic
# =============================================================================

is_valid_user = lambda name, age: (
    bool(name.strip())
    and age >= 18
)

print(
    is_valid_user(
        "Alex",
        30,
    )
)

print(
    is_valid_user(
        "",
        30,
    )
)


# =============================================================================
# 241. Lambda With Multiple Boolean Conditions
# =============================================================================

can_access = lambda is_active, is_admin: (
    is_active
    and is_admin
)

print(
    can_access(
        True,
        True,
    )
)

print(
    can_access(
        True,
        False,
    )
)


# =============================================================================
# 242. Lambda With Membership Conditions
# =============================================================================

is_supported_language = lambda language: (
    language.lower()
    in {
        "python",
        "go",
        "rust",
    }
)

print(
    is_supported_language("Python")
)

print(
    is_supported_language("Java")
)


# =============================================================================
# 243. Lambda With a Set as a Closure
# =============================================================================

def create_membership_checker(
    allowed_values: set[str],
) -> Callable[[str], bool]:
    """
    Create a membership-checking lambda.
    """
    return lambda value: value in allowed_values


is_allowed_language: Callable[[str], bool] = (
    create_membership_checker(
        {
            "Python",
            "Go",
            "Rust",
        }
    )
)

print(
    is_allowed_language("Python")
)

print(
    is_allowed_language("Java")
)


# =============================================================================
# 244. Lambda With a Dictionary as a Closure
# =============================================================================

def create_status_lookup(
    statuses: dict[int, str],
) -> Callable[[int], str]:
    """
    Create a status lookup function.
    """
    return lambda code: statuses.get(
        code,
        "Unknown",
    )


status_lookup: Callable[[int], str] = (
    create_status_lookup(
        {
            200: "OK",
            404: "Not Found",
        }
    )
)

print(
    status_lookup(200)
)

print(
    status_lookup(500)
)


# =============================================================================
# 245. Lambda With a List as a Closure
# =============================================================================

def create_length_checker(
    minimum_length: int,
) -> Callable[[str], bool]:
    """
    Create a string length checker.
    """
    return lambda text: len(text) >= minimum_length


is_long_enough: Callable[[str], bool] = (
    create_length_checker(5)
)

print(
    is_long_enough("Python")
)

print(
    is_long_enough("Go")
)


# =============================================================================
# 246. Lambda Function Factory
# =============================================================================

def create_comparison(
    threshold: int,
) -> Callable[[int], bool]:
    """
    Create a predicate that compares against a threshold.
    """
    return lambda value: value >= threshold


at_least_10: Callable[[int], bool] = create_comparison(
    10
)

at_least_100: Callable[[int], bool] = create_comparison(
    100
)

print(
    at_least_10(20)
)

print(
    at_least_100(20)
)


# =============================================================================
# 247. Lambda and Functional Programming
# =============================================================================
"""
Lambda functions are commonly associated with functional programming
patterns.

Common functional-style operations include:

    map()
        transform each item

    filter()
        select items

    reduce()
        combine items into one result

    sorted()
        transform comparison through a key function

Python also provides comprehensions, generator expressions, and normal
functions, which are often preferable depending on the situation.
"""


# =============================================================================
# 248. map() Concept
# =============================================================================
"""
map():

    input values
        ↓
    transformation
        ↓
    output values

Example:

    map(
        lambda number: number * 2,
        numbers,
    )
"""


# =============================================================================
# 249. filter() Concept
# =============================================================================
"""
filter():

    input values
        ↓
    predicate
        ↓
    keep matching values

Example:

    filter(
        lambda number: number > 10,
        numbers,
    )
"""


# =============================================================================
# 250. reduce() Concept
# =============================================================================
"""
reduce():

    value 1
       +
    value 2
       ↓
    intermediate result
       +
    value 3
       ↓
    final result

Example:

    reduce(
        lambda first, second: first + second,
        numbers,
    )
"""


# =============================================================================
# 251. sorted() Key Concept
# =============================================================================
"""
sorted():

    original object
        ↓
    key function
        ↓
    comparison value
        ↓
    sorted result

Example:

    sorted(
        students,
        key=lambda student: student.score,
    )
"""


# =============================================================================
# 252. Lambda Core Example
# =============================================================================

numbers_252: list[int] = [
    5,
    2,
    8,
    1,
    9,
]

result_252: list[int] = sorted(
    numbers_252,
    key=lambda number: number,
)

print(result_252)


# =============================================================================
# 253. Lambda With reverse=True
# =============================================================================

descending_numbers_253: list[int] = sorted(
    numbers_252,
    key=lambda number: number,
    reverse=True,
)

print(descending_numbers_253)


# =============================================================================
# 254. Lambda With Absolute Value Sorting
# =============================================================================

absolute_sorted_numbers: list[int] = sorted(
    [
        -20,
        5,
        -3,
        10,
        -1,
    ],
    key=lambda number: abs(number),
)

print(absolute_sorted_numbers)


# =============================================================================
# 255. Lambda With String Length Sorting
# =============================================================================

length_sorted_words: list[str] = sorted(
    [
        "Python",
        "Go",
        "Java",
        "Rust",
        "JavaScript",
    ],
    key=lambda word: len(word),
)

print(length_sorted_words)


# =============================================================================
# 256. Lambda With Object Sorting
# =============================================================================

age_sorted_people: list[tuple[str, int]] = sorted(
    people,
    key=lambda person: person[1],
)

print(age_sorted_people)


# =============================================================================
# 257. Lambda With Nested Object Sorting
# =============================================================================

nested_records: list[dict[str, object]] = [
    {
        "name": "Alex",
        "details": {
            "score": 80,
        },
    },
    {
        "name": "Maria",
        "details": {
            "score": 95,
        },
    },
]

nested_records_sorted: list[dict[str, object]] = sorted(
    nested_records,
    key=lambda record: int(
        record["details"]["score"]  # type: ignore[index]
    ),
)

print(nested_records_sorted)


# =============================================================================
# 258. Lambda With a Custom Class
# =============================================================================

@dataclass
class Product:
    """
    Represent a product.
    """

    name: str
    price: float
    quantity: int


product_objects: list[Product] = [
    Product(
        name="Keyboard",
        price=50.0,
        quantity=5,
    ),
    Product(
        name="Mouse",
        price=25.0,
        quantity=10,
    ),
    Product(
        name="Monitor",
        price=300.0,
        quantity=2,
    ),
]

products_by_price: list[Product] = sorted(
    product_objects,
    key=lambda product: product.price,
)

for product in products_by_price:
    print(
        product.name,
        product.price,
    )


# =============================================================================
# 259. Lambda With Calculated Object Key
# =============================================================================

products_by_total_value: list[Product] = sorted(
    product_objects,
    key=lambda product: (
        product.price * product.quantity
    ),
)

for product in products_by_total_value:
    print(
        product.name,
        product.price * product.quantity,
    )


# =============================================================================
# 260. Lambda With max() and Calculated Key
# =============================================================================

highest_inventory_value: Product = max(
    product_objects,
    key=lambda product: (
        product.price * product.quantity
    ),
)

print(
    highest_inventory_value.name
)


# =============================================================================
# 261. Lambda With min() and Calculated Key
# =============================================================================

lowest_inventory_value: Product = min(
    product_objects,
    key=lambda product: (
        product.price * product.quantity
    ),
)

print(
    lowest_inventory_value.name
)


# =============================================================================
# 262. Lambda With map() Over Objects
# =============================================================================

product_names: list[str] = list(
    map(
        lambda product: product.name,
        product_objects,
    )
)

print(product_names)


# =============================================================================
# 263. Lambda With map() Calculating Values
# =============================================================================

product_values: list[float] = list(
    map(
        lambda product: (
            product.price * product.quantity
        ),
        product_objects,
    )
)

print(product_values)


# =============================================================================
# 264. Lambda With filter() Over Objects
# =============================================================================

expensive_products: list[Product] = list(
    filter(
        lambda product: product.price >= 50.0,
        product_objects,
    )
)

for product in expensive_products:
    print(product.name)


# =============================================================================
# 265. Lambda With filter() and Multiple Conditions
# =============================================================================

high_value_products: list[Product] = list(
    filter(
        lambda product: (
            product.price >= 50.0
            and product.quantity >= 2
        ),
        product_objects,
    )
)

for product in high_value_products:
    print(product.name)


# =============================================================================
# 266. Lambda With map/filter Pipeline
# =============================================================================

high_value_product_names: list[str] = list(
    map(
        lambda product: product.name,
        filter(
            lambda product: product.price >= 50.0,
            product_objects,
        ),
    )
)

print(high_value_product_names)


# =============================================================================
# 267. Comprehension Alternative
# =============================================================================

high_value_product_names_comprehension: list[str] = [
    product.name
    for product in product_objects
    if product.price >= 50.0
]

print(high_value_product_names_comprehension)

# This may be easier to read than nested map() and filter() calls.


# =============================================================================
# 268. Lambda and Generator Alternative
# =============================================================================

high_value_product_generator = (
    product.name
    for product in product_objects
    if product.price >= 50.0
)

print(
    list(high_value_product_generator)
)


# =============================================================================
# 269. Lambda and Scope
# =============================================================================
"""
A lambda creates a function scope.

Its parameters are local to the lambda invocation.

For example:

    lambda number: number * 2

The name:

    number

is local to that lambda function.

A lambda can also access enclosing variables through closures.
"""


# =============================================================================
# 270. Lambda Scope Example
# =============================================================================

outer_value: int = 100

multiply_outer = lambda number: (
    number * outer_value
)

outer_scope_lambda_result: int = multiply_outer(
    5,
)

print(outer_scope_lambda_result)

# number is local to the lambda.
#
# outer_value is found in global scope.


# =============================================================================
# 271. Lambda Enclosing Scope Example
# =============================================================================

def create_scope_lambda(
    multiplier: int,
) -> Callable[[int], int]:
    """
    Create a lambda using an enclosing value.
    """
    return lambda number: number * multiplier


scope_lambda: Callable[[int], int] = (
    create_scope_lambda(5)
)

print(
    scope_lambda(10)
)


# =============================================================================
# 272. Lambda and Late Binding Reminder
# =============================================================================
"""
When lambdas are created in a loop, remember that closures capture the
variable, not necessarily the current value.

Problem:

    functions = []

    for number in range(3):
        functions.append(
            lambda: number
        )

All functions eventually use the final value of number.

Solution:

    functions.append(
        lambda number=number: number
    )

The default parameter captures the current value.
"""


# =============================================================================
# 273. Correct Late-Binding Pattern
# =============================================================================

multipliers_273: list[Callable[[], int]] = []

for value in range(1, 4):
    multipliers_273.append(
        lambda value=value: value * 10,
    )

multiplier_results_273: list[int] = [
    function()
    for function in multipliers_273
]

print(multiplier_results_273)

# Output:
#
# [10, 20, 30]


# =============================================================================
# 274. Lambda With a Callback Pipeline
# =============================================================================

def pipeline(
    value: int,
    first: Callable[[int], int],
    second: Callable[[int], int],
) -> int:
    """
    Apply two transformations in sequence.
    """
    first_result: int = first(value)

    return second(first_result)


pipeline_result: int = pipeline(
    5,
    lambda number: number * 2,
    lambda number: number + 10,
)

print(pipeline_result)

# Calculation:
#
# 5
# ↓
# * 2
# ↓
# 10
# ↓
# + 10
# ↓
# 20


# =============================================================================
# 275. Lambda With Three-Step Pipeline
# =============================================================================

def three_step_pipeline(
    value: int,
    first: Callable[[int], int],
    second: Callable[[int], int],
    third: Callable[[int], int],
) -> int:
    """
    Apply three transformations.
    """
    first_result: int = first(value)
    second_result: int = second(first_result)

    return third(second_result)


three_step_result: int = three_step_pipeline(
    5,
    lambda number: number * 2,
    lambda number: number + 10,
    lambda number: number ** 2,
)

print(three_step_result)

# Calculation:
#
# 5
# ↓
# 10
# ↓
# 20
# ↓
# 400


# =============================================================================
# 276. Lambda With Predicate Callback
# =============================================================================

def find_matching_values(
    values: list[int],
    predicate: Callable[[int], bool],
) -> list[int]:
    """
    Return values satisfying a predicate.
    """
    return [
        value
        for value in values
        if predicate(value)
    ]


matching_values: list[int] = find_matching_values(
    [
        5,
        10,
        15,
        20,
        25,
    ],
    lambda number: number >= 15,
)

print(matching_values)


# =============================================================================
# 277. Lambda With Transformer Callback
# =============================================================================

def transform_values(
    values: list[int],
    transformer: Callable[[int], int],
) -> list[int]:
    """
    Transform all values using a callback.
    """
    return [
        transformer(value)
        for value in values
    ]


transformed_values: list[int] = transform_values(
    [
        1,
        2,
        3,
    ],
    lambda number: number ** 2,
)

print(transformed_values)


# =============================================================================
# 278. Lambda With Sort Callback
# =============================================================================

def sort_values(
    values: list[int],
    key_function: Callable[[int], int],
) -> list[int]:
    """
    Sort values using a key function.
    """
    return sorted(
        values,
        key=key_function,
    )


sorted_by_distance: list[int] = sort_values(
    [
        -10,
        2,
        -3,
        7,
    ],
    lambda number: abs(number),
)

print(sorted_by_distance)


# =============================================================================
# 279. Lambda and Type-Safe Callback
# =============================================================================

def apply_integer_function(
    value: int,
    function: Callable[[int], int],
) -> int:
    """
    Apply a typed integer function.
    """
    return function(value)


typed_callback_result: int = apply_integer_function(
    20,
    lambda number: number // 2,
)

print(typed_callback_result)


# =============================================================================
# 280. Lambda and Type-Safe String Callback
# =============================================================================

def apply_string_function(
    value: str,
    function: Callable[[str], str],
) -> str:
    """
    Apply a typed string function.
    """
    return function(value)


typed_string_result: str = apply_string_function(
    "python",
    lambda text: text.upper(),
)

print(typed_string_result)


# =============================================================================
# 281. Lambda and Type-Safe Predicate
# =============================================================================

def count_matching(
    values: list[int],
    predicate: Callable[[int], bool],
) -> int:
    """
    Count values satisfying a predicate.
    """
    return sum(
        1
        for value in values
        if predicate(value)
    )


matching_count: int = count_matching(
    [
        1,
        2,
        3,
        4,
        5,
    ],
    lambda number: number % 2 == 0,
)

print(matching_count)


# =============================================================================
# 282. Lambda and Type-Safe Sort Key
# =============================================================================

def sort_students(
    values: list[Student],
    key_function: Callable[[Student], int],
) -> list[Student]:
    """
    Sort students using a typed key function.
    """
    return sorted(
        values,
        key=key_function,
    )


typed_sorted_students: list[Student] = sort_students(
    student_objects,
    lambda student: student.score,
)

for student in typed_sorted_students:
    print(student.name)


# =============================================================================
# 283. Lambda With Named Callable Variable
# =============================================================================

calculate_tax: Callable[[float], float] = (
    lambda price: price * 0.18
)

tax_result: float = calculate_tax(
    1000.0,
)

print(tax_result)


# =============================================================================
# 284. Lambda With Named Callable Variable
# =============================================================================

calculate_discount: Callable[[float], float] = (
    lambda price: price * 0.10
)

discount_result: float = calculate_discount(
    1000.0,
)

print(discount_result)


# =============================================================================
# 285. Lambda Combining Calculations
# =============================================================================

calculate_final_price: Callable[[float], float] = (
    lambda price: (
        price
        + price * 0.18
        - price * 0.10
    )
)

final_price_result: float = calculate_final_price(
    1000.0,
)

print(final_price_result)


# =============================================================================
# 286. Lambda With a Conditional Discount
# =============================================================================

calculate_discounted_total: Callable[[float], float] = (
    lambda price: (
        price * 0.90
        if price >= 1000
        else price
    )
)

print(
    calculate_discounted_total(
        1500.0
    )
)

print(
    calculate_discounted_total(
        500.0
    )
)


# =============================================================================
# 287. Lambda With Multiple Conditions
# =============================================================================

calculate_discount_rate = lambda price: (
    0.20
    if price >= 5000
    else 0.10
    if price >= 1000
    else 0.0
)

print(
    calculate_discount_rate(
        6000
    )
)

print(
    calculate_discount_rate(
        2000
    )
)

print(
    calculate_discount_rate(
        500
    )
)


# =============================================================================
# 288. Lambda and Anonymous Functions
# =============================================================================
"""
The term "anonymous" means that a lambda function does not require a
normal function name.

For example:

    lambda number: number * 2

The function itself has no descriptive name.

When assigned:

    double = lambda number: number * 2

the variable double refers to the function object.

Even though this is allowed, a normal def can be clearer when the
function is reusable.
"""


# =============================================================================
# 289. Lambda Assigned to a Variable
# =============================================================================

anonymous_example = lambda value: value + 1

anonymous_result: int = anonymous_example(
    10,
)

print(anonymous_result)


# =============================================================================
# 290. Lambda Used Without Assignment
# =============================================================================

direct_lambda_result: int = (
    lambda value: value + 1
)(
    10,
)

print(direct_lambda_result)


# =============================================================================
# 291. Lambda With sorted() Is a Common Pattern
# =============================================================================

sorted_by_length: list[str] = sorted(
    [
        "Python",
        "Go",
        "JavaScript",
        "C",
    ],
    key=lambda value: len(value),
)

print(sorted_by_length)


# =============================================================================
# 292. Lambda With min() Is a Common Pattern
# =============================================================================

shortest: str = min(
    [
        "Python",
        "Go",
        "Rust",
    ],
    key=lambda value: len(value),
)

print(shortest)


# =============================================================================
# 293. Lambda With max() Is a Common Pattern
# =============================================================================

longest: str = max(
    [
        "Python",
        "Go",
        "JavaScript",
    ],
    key=lambda value: len(value),
)

print(longest)


# =============================================================================
# 294. Lambda With map() Is a Common Pattern
# =============================================================================

doubled: list[int] = list(
    map(
        lambda value: value * 2,
        [
            1,
            2,
            3,
        ],
    )
)

print(doubled)


# =============================================================================
# 295. Lambda With filter() Is a Common Pattern
# =============================================================================

filtered: list[int] = list(
    filter(
        lambda value: value > 2,
        [
            1,
            2,
            3,
            4,
        ],
    )
)

print(filtered)


# =============================================================================
# 296. Lambda With reduce() Is a Common Pattern
# =============================================================================

reduced: int = reduce(
    lambda first, second: first + second,
    [
        1,
        2,
        3,
        4,
    ],
)

print(reduced)


# =============================================================================
# 297. Lambda Common Mistake: Too Much Logic
# =============================================================================
"""
Avoid writing very complicated lambdas.

Bad style:

    lambda value: (
        complicated_condition
        if another_condition
        else another_result
        if something_else
        else final_result
    )

If understanding the lambda requires significant effort, use def.
"""


# =============================================================================
# 298. Lambda Common Mistake: Reusing Complex Lambda
# =============================================================================
"""
If the same lambda is used repeatedly, consider creating a named function.

Instead of repeatedly writing:

    lambda student: student.score

you can use:

    def get_student_score(student):
        return student.score

For very small key functions, lambda is still perfectly reasonable.
"""


# =============================================================================
# 299. Lambda Common Mistake: Late Binding
# =============================================================================
"""
Be careful with:

    functions = []

    for value in values:
        functions.append(
            lambda: value
        )

The lambda captures the variable value.

It does not automatically freeze the current value.

Use:

    lambda value=value: value

when a snapshot of the current loop value is required.
"""


# =============================================================================
# 300. Lambda Common Mistake: Shadowing Names
# =============================================================================
"""
Avoid confusing parameter names.

For example:

    lambda list: ...

is legal, but list is also a built-in type.

Prefer:

    lambda values: ...

Similarly, avoid unnecessarily shadowing:

    str
    int
    list
    dict
    sum
    max
    min
    input
"""


# =============================================================================
# 301. Lambda Common Mistake: Ignoring Readability
# =============================================================================
"""
The shortest code is not always the clearest code.

Use lambda when it makes the code clearer or more concise.

Use def when a name, documentation, multiple statements, or complex logic
would improve the code.
"""


# =============================================================================
# 302. Lambda Practical Pattern: Sorting
# =============================================================================

def demonstrate_sorting_with_lambda() -> None:
    """
    Demonstrate a practical lambda sorting pattern.
    """
    values: list[tuple[str, int]] = [
        ("Python", 1991),
        ("Go", 2009),
        ("Rust", 2010),
    ]

    sorted_values: list[tuple[str, int]] = sorted(
        values,
        key=lambda item: item[1],
    )

    print(sorted_values)


demonstrate_sorting_with_lambda()


# =============================================================================
# 303. Lambda Practical Pattern: Filtering
# =============================================================================

def demonstrate_filtering_with_lambda() -> None:
    """
    Demonstrate a practical lambda filtering pattern.
    """
    values: list[int] = [
        5,
        10,
        15,
        20,
    ]

    filtered_values: list[int] = list(
        filter(
            lambda value: value >= 10,
            values,
        )
    )

    print(filtered_values)


demonstrate_filtering_with_lambda()


# =============================================================================
# 304. Lambda Practical Pattern: Mapping
# =============================================================================

def demonstrate_mapping_with_lambda() -> None:
    """
    Demonstrate a practical lambda mapping pattern.
    """
    values: list[int] = [
        1,
        2,
        3,
    ]

    mapped_values: list[int] = list(
        map(
            lambda value: value * 10,
            values,
        )
    )

    print(mapped_values)


demonstrate_mapping_with_lambda()


# =============================================================================
# 305. Lambda Practical Pattern: Callback
# =============================================================================

def demonstrate_callback_with_lambda() -> None:
    """
    Demonstrate a lambda callback.
    """

    def execute(
        value: int,
        callback: Callable[[int], int],
    ) -> int:
        """
        Execute a callback.
        """
        return callback(value)

    result: int = execute(
        10,
        lambda value: value + 5,
    )

    print(result)


demonstrate_callback_with_lambda()


# =============================================================================
# 306. Lambda Practical Pattern: Closure
# =============================================================================

def demonstrate_lambda_closure() -> None:
    """
    Demonstrate a lambda closure.
    """

    def create_multiplier(
        multiplier: int,
    ) -> Callable[[int], int]:
        """
        Create a multiplier lambda.
        """
        return lambda value: value * multiplier

    double_function: Callable[[int], int] = (
        create_multiplier(2)
    )

    result: int = double_function(
        10
    )

    print(result)


demonstrate_lambda_closure()


# =============================================================================
# 307. Lambda Practical Pattern: Data Pipeline
# =============================================================================

def demonstrate_lambda_pipeline() -> None:
    """
    Demonstrate a simple lambda-based data pipeline.
    """
    values: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    even_values: list[int] = list(
        filter(
            lambda value: value % 2 == 0,
            values,
        )
    )

    squared_values: list[int] = list(
        map(
            lambda value: value ** 2,
            even_values,
        )
    )

    print(squared_values)


demonstrate_lambda_pipeline()


# =============================================================================
# 308. Lambda Practical Pattern: Sort and Select
# =============================================================================

def demonstrate_lambda_selection() -> None:
    """
    Demonstrate sorting and selecting data with lambdas.
    """
    values: list[int] = [
        -20,
        5,
        -3,
        10,
        -1,
    ]

    closest_to_zero: int = min(
        values,
        key=lambda value: abs(value),
    )

    print(closest_to_zero)


demonstrate_lambda_selection()


# =============================================================================
# 309. Lambda Practical Pattern: Object Filtering
# =============================================================================

def demonstrate_object_filtering() -> None:
    """
    Filter objects using a lambda predicate.
    """
    products: list[Product] = [
        Product(
            name="Keyboard",
            price=50.0,
            quantity=5,
        ),
        Product(
            name="Mouse",
            price=25.0,
            quantity=10,
        ),
        Product(
            name="Monitor",
            price=300.0,
            quantity=2,
        ),
    ]

    expensive_products: list[Product] = list(
        filter(
            lambda product: product.price >= 50.0,
            products,
        )
    )

    for product in expensive_products:
        print(product.name)


demonstrate_object_filtering()


# =============================================================================
# 310. Lambda Practical Pattern: Object Transformation
# =============================================================================

def demonstrate_object_transformation() -> None:
    """
    Transform objects into another representation.
    """
    products: list[Product] = [
        Product(
            name="Keyboard",
            price=50.0,
            quantity=5,
        ),
        Product(
            name="Mouse",
            price=25.0,
            quantity=10,
        ),
    ]

    product_names: list[str] = list(
        map(
            lambda product: product.name,
            products,
        )
    )

    print(product_names)


demonstrate_object_transformation()


# =============================================================================
# 311. Lambda Practical Pattern: Object Sorting
# =============================================================================

def demonstrate_object_sorting() -> None:
    """
    Sort objects using a lambda key.
    """
    products: list[Product] = [
        Product(
            name="Keyboard",
            price=50.0,
            quantity=5,
        ),
        Product(
            name="Mouse",
            price=25.0,
            quantity=10,
        ),
        Product(
            name="Monitor",
            price=300.0,
            quantity=2,
        ),
    ]

    sorted_products: list[Product] = sorted(
        products,
        key=lambda product: product.price,
    )

    for product in sorted_products:
        print(
            product.name,
            product.price,
        )


demonstrate_object_sorting()


# =============================================================================
# 312. Lambda Practical Pattern: Grouping Key
# =============================================================================
"""
A lambda can be used as a key when preparing data for grouping or sorting.

The lambda itself does not perform grouping; it provides the value used
to organize the data.
"""


# =============================================================================
# 313. Lambda With sorted() for Grouping Preparation
# =============================================================================

transactions: list[tuple[str, float]] = [
    ("food", 20.0),
    ("travel", 100.0),
    ("food", 50.0),
    ("travel", 30.0),
]

transactions_sorted: list[tuple[str, float]] = sorted(
    transactions,
    key=lambda transaction: transaction[0],
)

print(transactions_sorted)


# =============================================================================
# 314. Lambda and Stable Sorting
# =============================================================================
"""
Python's sorted() is stable.

When two elements have the same key, their original relative order is
preserved.

A lambda can therefore define one sorting criterion while preserving
the original order of equal-key elements.
"""


# =============================================================================
# 315. Stable Sorting Example
# =============================================================================

stable_values: list[tuple[str, int]] = [
    ("A", 2),
    ("B", 1),
    ("C", 2),
    ("D", 1),
]

stable_sorted_values: list[tuple[str, int]] = sorted(
    stable_values,
    key=lambda value: value[1],
)

print(stable_sorted_values)

# The relative order of A and C is preserved.
#
# The relative order of B and D is preserved.


# =============================================================================
# 316. Lambda and Reverse Order
# =============================================================================

reverse_values: list[int] = sorted(
    [
        5,
        1,
        8,
        3,
    ],
    key=lambda value: value,
    reverse=True,
)

print(reverse_values)


# =============================================================================
# 317. Lambda and None Handling
# =============================================================================
"""
When sorting data containing None, the key function can normalize the
values into comparable values.
"""


# =============================================================================
# 318. None Sorting Example
# =============================================================================

optional_scores: list[int | None] = [
    80,
    None,
    95,
    70,
    None,
]

optional_scores_sorted: list[int | None] = sorted(
    optional_scores,
    key=lambda value: (
        value is None,
        value if value is not None else 0,
    ),
)

print(optional_scores_sorted)


# =============================================================================
# 319. Lambda With Decimal-Like Data
# =============================================================================
"""
For financial calculations, use Decimal instead of float when appropriate.

A lambda can still be used as a key or transformation.
"""


# =============================================================================
# 320. Lambda With Decimal
# =============================================================================

from decimal import Decimal


prices_decimal: list[Decimal] = [
    Decimal("10.50"),
    Decimal("5.25"),
    Decimal("20.00"),
]

sorted_decimal_prices: list[Decimal] = sorted(
    prices_decimal,
    key=lambda price: price,
)

print(sorted_decimal_prices)


# =============================================================================
# 321. Lambda With Callable Return
# =============================================================================

def create_operation(
    operation: str,
) -> Callable[[int, int], int]:
    """
    Return a lambda based on the requested operation.
    """
    if operation == "add":
        return lambda first, second: first + second

    if operation == "multiply":
        return lambda first, second: first * second

    return lambda first, second: first - second


operation_function: Callable[[int, int], int] = (
    create_operation("add")
)

print(
    operation_function(
        10,
        20,
    )
)


# =============================================================================
# 322. Lambda With Closures and Multiple Functions
# =============================================================================

def create_operations(
    multiplier: int,
) -> tuple[
    Callable[[int], int],
    Callable[[int], int],
]:
    """
    Create two lambda functions sharing an enclosing value.
    """
    multiply: Callable[[int], int] = (
        lambda value: value * multiplier
    )

    add: Callable[[int], int] = (
        lambda value: value + multiplier
    )

    return (
        multiply,
        add,
    )


multiply_operation: Callable[[int], int]
add_operation: Callable[[int], int]

(
    multiply_operation,
    add_operation,
) = create_operations(10)

print(
    multiply_operation(5)
)

print(
    add_operation(5)
)


# =============================================================================
# 323. Lambda and Function Identity
# =============================================================================
"""
Every lambda expression creates a function object.

Two separate lambda expressions are separate function objects even if
their code is identical.
"""


# =============================================================================
# 324. Separate Lambda Objects
# =============================================================================

first_lambda = lambda value: value * 2
second_lambda = lambda value: value * 2

print(
    first_lambda is second_lambda
)

# Output:
#
# False


# =============================================================================
# 325. Same Lambda Object Through Assignment
# =============================================================================

original_lambda = lambda value: value * 2
another_reference = original_lambda

print(
    original_lambda is another_reference
)

# Output:
#
# True


# =============================================================================
# 326. Lambda Can Be Called Normally
# =============================================================================

callable_lambda = lambda value: value + 100

print(
    callable_lambda(5)
)


# =============================================================================
# 327. Lambda With Keyword-Only Parameters
# =============================================================================
"""
Lambda functions can use the * marker to make parameters keyword-only.

Example:

    lambda value, *, multiplier=2: value * multiplier
"""


# =============================================================================
# 328. Keyword-Only Lambda Parameter
# =============================================================================

keyword_only_multiplier = lambda value, *, multiplier=2: (
    value * multiplier
)

print(
    keyword_only_multiplier(
        10,
        multiplier=3,
    )
)


# =============================================================================
# 329. Lambda With Positional-Only Parameters
# =============================================================================
"""
Lambda functions can use / in the parameter list for positional-only
parameters.

Example:

    lambda value, /: value * 2

The parameter cannot then be passed by keyword.
"""


# =============================================================================
# 330. Positional-Only Lambda Parameter
# =============================================================================

positional_only_double = lambda value, /: value * 2

print(
    positional_only_double(
        10
    )
)


# =============================================================================
# 331. Lambda With Positional-Only and Keyword-Only Parameters
# =============================================================================

advanced_lambda = lambda value, /, *, multiplier=2: (
    value * multiplier
)

print(
    advanced_lambda(
        10,
        multiplier=3,
    )
)


# =============================================================================
# 332. Lambda Parameter Rules
# =============================================================================
"""
Lambda parameters follow normal function parameter rules.

Examples:

    lambda value: value

    lambda first, second: first + second

    lambda value=10: value * 2

    lambda *values: sum(values)

    lambda **values: len(values)

    lambda value, *, multiplier=2: value * multiplier

    lambda value, /: value * 2
"""


# =============================================================================
# 333. Lambda With *args and Keyword-Only Parameter
# =============================================================================

sum_with_multiplier = (
    lambda *values, multiplier=1: (
        sum(values) * multiplier
    )
)

print(
    sum_with_multiplier(
        1,
        2,
        3,
        multiplier=10,
    )
)


# =============================================================================
# 334. Lambda With **kwargs Access
# =============================================================================

get_name_from_kwargs = lambda **kwargs: str(
    kwargs.get(
        "name",
        "Unknown",
    )
)

print(
    get_name_from_kwargs(
        name="Alex"
    )
)


# =============================================================================
# 335. Lambda With args and kwargs
# =============================================================================

describe = lambda *args, **kwargs: {
    "positional_count": len(args),
    "keyword_count": len(kwargs),
}

description: dict[str, int] = describe(
    1,
    2,
    3,
    name="Alex",
)

print(description)


# =============================================================================
# 336. Lambda and Return Type Concept
# =============================================================================
"""
Lambda functions always return the value of their single expression.

Examples:

    lambda value: value * 2
        -> int

    lambda value: str(value)
        -> str

    lambda value: value > 10
        -> bool

The return type depends on the expression.
"""


# =============================================================================
# 337. Lambda Returning bool
# =============================================================================

check_even = lambda value: value % 2 == 0

check_even_result: bool = check_even(
    10
)

print(check_even_result)


# =============================================================================
# 338. Lambda Returning str
# =============================================================================

convert_to_text = lambda value: str(value)

text_result: str = convert_to_text(
    100
)

print(text_result)


# =============================================================================
# 339. Lambda Returning float
# =============================================================================

calculate_ratio = lambda first, second: first / second

ratio_result: float = calculate_ratio(
    10,
    4,
)

print(ratio_result)


# =============================================================================
# 340. Lambda Returning tuple
# =============================================================================

create_pair = lambda first, second: (
    first,
    second,
)

pair_result: tuple[int, int] = create_pair(
    10,
    20,
)

print(pair_result)


# =============================================================================
# 341. Lambda Returning dict
# =============================================================================

create_record = lambda name, score: {
    "name": name,
    "score": score,
}

record_result: dict[str, object] = create_record(
    "Alex",
    90,
)

print(record_result)


# =============================================================================
# 342. Lambda Returning list
# =============================================================================

create_values = lambda value: [
    value,
    value * 2,
    value * 3,
]

values_result: list[int] = create_values(
    5
)

print(values_result)


# =============================================================================
# 343. Lambda With Arithmetic Precedence
# =============================================================================

calculate_expression = lambda value: (
    value + 10 * 2
)

expression_result: int = calculate_expression(
    5
)

print(expression_result)

# Multiplication happens before addition:
#
# 5 + (10 * 2)
#
# = 25


# =============================================================================
# 344. Lambda With Explicit Parentheses
# =============================================================================

calculate_grouped_expression = lambda value: (
    (value + 10) * 2
)

grouped_expression_result: int = (
    calculate_grouped_expression(5)
)

print(grouped_expression_result)

# (5 + 10) * 2
#
# = 30


# =============================================================================
# 345. Lambda and Operator Precedence
# =============================================================================
"""
Lambda expressions obey normal Python operator precedence rules.

Use parentheses when they improve readability.
"""


# =============================================================================
# 346. Lambda With Logical Operators
# =============================================================================

valid_range = lambda value: (
    value >= 10
    and value <= 100
)

print(
    valid_range(50)
)

print(
    valid_range(150)
)


# =============================================================================
# 347. Lambda With or
# =============================================================================

default_text = lambda text: (
    text
    or "No value"
)

print(
    default_text("")
)

print(
    default_text("Python")
)


# =============================================================================
# 348. Lambda With not
# =============================================================================

is_not_empty = lambda text: not text.strip() == ""

print(
    is_not_empty("Python")
)

print(
    is_not_empty("   ")
)


# =============================================================================
# 349. Lambda With in
# =============================================================================

is_admin_role = lambda role: role in {
    "admin",
    "superadmin",
}

print(
    is_admin_role("admin")
)

print(
    is_admin_role("guest")
)


# =============================================================================
# 350. Lambda With is
# =============================================================================

is_none = lambda value: value is None

print(
    is_none(None)
)

print(
    is_none(10)
)


# =============================================================================
# 351. Lambda With Attribute Access
# =============================================================================

student_score = lambda student: student.score

score_from_lambda: int = student_score(
    student_objects[0]
)

print(score_from_lambda)


# =============================================================================
# 352. Lambda With Method Call
# =============================================================================

student_name_upper = lambda student: (
    student.name.upper()
)

upper_student_name: str = student_name_upper(
    student_objects[0]
)

print(upper_student_name)


# =============================================================================
# 353. Lambda With Dataclass Computation
# =============================================================================

student_passed = lambda student: student.score >= 50

print(
    student_passed(
        student_objects[0]
    )
)


# =============================================================================
# 354. Lambda With Calculated Dataclass Key
# =============================================================================

student_grade_key = lambda student: (
    student.score // 10
)

students_by_grade_group: list[Student] = sorted(
    student_objects,
    key=student_grade_key,
)

for student in students_by_grade_group:
    print(
        student.name,
        student.score,
    )


# =============================================================================
# 355. Lambda and Assignment to Variable
# =============================================================================
"""
Assigning a lambda to a variable is valid.

However, if the function is intended to be reused and has a meaningful
purpose, a def statement is often clearer.

For example:

    double = lambda value: value * 2

is valid.

But:

    def double(value):
        return value * 2

is generally more descriptive.
"""


# =============================================================================
# 356. Lambda Practical Recommendation
# =============================================================================
"""
Prefer lambda:

    sorted(
        values,
        key=lambda value: value.score,
    )

Prefer def:

    def calculate_invoice_total(
        ...
    ):
        ...
"""


# =============================================================================
# 357. Lambda Summary: Syntax
# =============================================================================
"""
lambda parameters: expression
"""


# =============================================================================
# 358. Lambda Summary: One Parameter
# =============================================================================
"""
lambda value: value * 2
"""


# =============================================================================
# 359. Lambda Summary: Multiple Parameters
# =============================================================================
"""
lambda first, second: first + second
"""


# =============================================================================
# 360. Lambda Summary: Default Parameter
# =============================================================================
"""
lambda value=10: value * 2
"""


# =============================================================================
# 361. Lambda Summary: Variable Positional Arguments
# =============================================================================
"""
lambda *values: sum(values)
"""


# =============================================================================
# 362. Lambda Summary: Variable Keyword Arguments
# =============================================================================
"""
lambda **values: len(values)
"""


# =============================================================================
# 363. Lambda Summary: Conditional Expression
# =============================================================================
"""
lambda value: (
    "positive"
    if value > 0
    else "non-positive"
)
"""


# =============================================================================
# 364. Lambda Summary: sorted()
# =============================================================================
"""
sorted(
    values,
    key=lambda value: value.score,
)
"""


# =============================================================================
# 365. Lambda Summary: min()
# =============================================================================
"""
min(
    values,
    key=lambda value: abs(value),
)
"""


# =============================================================================
# 366. Lambda Summary: max()
# =============================================================================
"""
max(
    values,
    key=lambda value: value.score,
)
"""


# =============================================================================
# 367. Lambda Summary: map()
# =============================================================================
"""
list(
    map(
        lambda value: value * 2,
        values,
    )
)
"""


# =============================================================================
# 368. Lambda Summary: filter()
# =============================================================================
"""
list(
    filter(
        lambda value: value > 10,
        values,
    )
)
"""


# =============================================================================
# 369. Lambda Summary: reduce()
# =============================================================================
"""
reduce(
    lambda first, second: first + second,
    values,
)
"""


# =============================================================================
# 370. Lambda Summary: Closure
# =============================================================================
"""
def create_multiplier(
    multiplier: int,
) -> Callable[[int], int]:
    return lambda value: value * multiplier
"""


# =============================================================================
# 371. Lambda Summary: Callback
# =============================================================================
"""
def execute(
    value: int,
    callback: Callable[[int], int],
) -> int:
    return callback(value)

execute(
    10,
    lambda value: value * 2,
)
"""


# =============================================================================
# 372. Lambda Summary: Late Binding
# =============================================================================
"""
Problem:

    functions = []

    for value in range(3):
        functions.append(
            lambda: value
        )

Solution:

    functions = []

    for value in range(3):
        functions.append(
            lambda value=value: value
        )
"""


# =============================================================================
# 373. Lambda Summary: When to Use
# =============================================================================
"""
Use lambda when:

    - The operation is short.
    - The operation is simple.
    - A callback is required.
    - sorted() needs a key.
    - min() needs a key.
    - max() needs a key.
    - map() needs a small transformation.
    - filter() needs a small predicate.
    - A temporary function is useful.
"""


# =============================================================================
# 374. Lambda Summary: When Not to Use
# =============================================================================
"""
Prefer def when:

    - The logic is complex.
    - The function has multiple steps.
    - The function needs a descriptive name.
    - The function needs substantial documentation.
    - The function is reused frequently.
    - The function needs complicated error handling.
    - The lambda becomes difficult to read.
    - A comprehension is clearer.
"""


# =============================================================================
# 375. Lambda Core Rules
# =============================================================================
"""
Important rules:

    1. lambda creates a function object.

    2. Lambda functions are anonymous.

    3. Lambda syntax is:

           lambda parameters: expression

    4. A lambda body contains one expression.

    5. The expression's value is automatically returned.

    6. Lambda functions can accept parameters.

    7. Lambda functions can use default parameters.

    8. Lambda functions can use *args.

    9. Lambda functions can use **kwargs.

    10. Lambda functions can be passed as callbacks.

    11. Lambda functions can be stored in variables.

    12. Lambda functions can be stored in collections.

    13. Lambda functions can be returned from functions.

    14. Lambda functions can create closures.

    15. Lambda functions follow normal Python scope rules.

    16. Lambda functions can be used as sorted() key functions.

    17. Lambda functions can be used with min() and max().

    18. Lambda functions can be used with map().

    19. Lambda functions can be used with filter().

    20. Lambda functions can be used with reduce().

    21. Lambda functions should generally remain simple.

    22. Use def for complex or reusable logic.
"""


# =============================================================================
# 376. Final Practical Example
# =============================================================================

def process_students(
    values: list[Student],
) -> list[str]:
    """
    Process students using several lambda functions.
    """
    passing_students: list[Student] = list(
        filter(
            lambda student: student.score >= 50,
            values,
        )
    )

    sorted_students: list[Student] = sorted(
        passing_students,
        key=lambda student: student.score,
        reverse=True,
    )

    student_names: list[str] = list(
        map(
            lambda student: student.name,
            sorted_students,
        )
    )

    return student_names


processed_student_names: list[str] = process_students(
    student_objects,
)

print(processed_student_names)


# =============================================================================
# 377. Final Lambda Example
# =============================================================================
"""
Complete flow:

    data
      ↓
    filter()
      ↓
    lambda predicate
      ↓
    selected data
      ↓
    sorted()
      ↓
    lambda key
      ↓
    sorted data
      ↓
    map()
      ↓
    lambda transformation
      ↓
    final result

Example:

    student_objects
        ↓
    filter(
        lambda student: student.score >= 50
    )
        ↓
    sorted(
        key=lambda student: student.score
    )
        ↓
    map(
        lambda student: student.name
    )
        ↓
    student names
"""


# =============================================================================
# 378. Key Takeaways
# =============================================================================
"""
✓ A lambda function is a small anonymous function.

✓ Lambda syntax is:

    lambda parameters: expression

✓ A lambda contains one expression.

✓ The expression's result is automatically returned.

✓ Lambda functions do not use an explicit return statement.

✓ Lambda functions can accept zero or more parameters.

✓ Lambda functions support default parameters.

✓ Lambda functions support *args.

✓ Lambda functions support **kwargs.

✓ Lambda functions can be assigned to variables.

✓ Lambda functions can be passed as arguments.

✓ Lambda functions can be returned from functions.

✓ Lambda functions can be stored in collections.

✓ Lambda functions are commonly used as callbacks.

✓ Lambda functions are commonly used with sorted().

✓ Lambda functions are commonly used with min().

✓ Lambda functions are commonly used with max().

✓ Lambda functions are commonly used with map().

✓ Lambda functions are commonly used with filter().

✓ Lambda functions can be used with reduce().

✓ Lambda functions can create closures.

✓ Lambda functions follow normal LEGB scope rules.

✓ Lambda functions can capture enclosing variables.

✓ Lambdas created inside loops can demonstrate late binding.

✓ Default parameters can be used to capture loop values.

✓ Lambda functions should generally remain simple.

✓ Complex logic is usually better implemented using def.

✓ Named functions are usually easier to document and debug.

✓ Comprehensions are often clearer than map() and filter() for simple
  transformations.

✓ The shortest implementation is not always the clearest implementation.

Core model:

    lambda
       ↓
    parameters
       ↓
    one expression
       ↓
    automatic result

Common usage:

    sorted()
       ↓
    key=lambda ...

    min()
       ↓
    key=lambda ...

    max()
       ↓
    key=lambda ...

    map()
       ↓
    lambda ...

    filter()
       ↓
    lambda ...

    reduce()
       ↓
    lambda ...

Core distinction:

    lambda
        ↓
    short temporary function

    def
        ↓
    named reusable function

Most important idea:

    Use lambda when it makes a small operation
    concise and readable.

    Use def when the logic deserves
    a meaningful name, documentation,
    testing, or multiple statements.
"""


# =============================================================================
# End of 16_lambda_functions.py
# =============================================================================