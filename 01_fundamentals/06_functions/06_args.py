# =============================================================================
#
# Python Functions
#
# File
#
# 06_args.py
#
# Topic
#
# Variable-Length Positional Arguments (*args)
#
# =============================================================================

# """

# Overview

# A variable-length positional argument allows a function to accept any number
# of positional arguments.

# Python provides the special parameter syntax:

# *args

# The name "args" is only a conventional name.

# The important part is the "*".

# When a function contains *args, all additional positional arguments that are
# not assigned to earlier parameters are collected into a tuple.

# Variable-length positional arguments therefore allow a function to work with
# an arbitrary number of positional values without knowing in advance how many
# values the caller will provide.

# Topics covered:

# - What are variable-length positional arguments?
# - Understanding *args
# - Why *args is used
# - Calling a function with no additional positional arguments
# - Calling a function with one positional argument
# - Calling a function with multiple positional arguments
# - The collected arguments are stored in a tuple
# - Iterating over *args
# - Finding the number of arguments
# - Accessing individual arguments
# - Indexing *args
# - Slicing *args
# - Combining required parameters with *args
# - Combining normal parameters with *args
# - Positional arguments are collected after normal parameters
# - *args can collect zero or more arguments
# - *args and tuple behaviour
# - Unpacking a tuple into *args
# - Passing a list using *
# - Passing a tuple using *
# - Combining normal arguments with unpacking
# - Using *args with calculations
# - Using *args with strings
# - Using *args with mixed values
# - Using *args with loops
# - Using *args with built-in functions
# - *args with keyword arguments
# - *args does not collect keyword arguments
# - Difference between *args and **kwargs
# - Positional-only parameters with *args
# - Keyword-only parameters after *args
# - Parameter ordering rules
# - *args and strict calling conventions

# """


# =============================================================================
#
# 01. Basic *args
#
# =============================================================================

def display_arguments(
    *args: str,
) -> tuple[str, ...]:
    """
    Return all supplied positional arguments.
    """
    return (
        args
    )


arguments: tuple[str, ...] = display_arguments(
    "Python",
    "SQL",
    "Git",
)

print(
    arguments
)

# The parameter:

# *args

# collects all positional arguments supplied to the function.

#

# The collected values are stored as a tuple.

#

# Therefore:

#

# display_arguments(
#     "Python",
#     "SQL",
#     "Git",
# )

#

# produces:

#

# (
#     "Python",
#     "SQL",
#     "Git",
# )


# =============================================================================
#
# 02. *args Can Receive No Arguments
#
# =============================================================================

def collect_values(
    *args: int,
) -> tuple[int, ...]:
    """
    Collect zero or more positional arguments.
    """
    return (
        args
    )


no_values: tuple[int, ...] = collect_values()

print(
    no_values
)

# *args can receive zero positional arguments.

#

# Therefore:

#

# collect_values()

#

# produces:

#

# ()

#

# The empty tuple represents that no additional positional arguments
# were supplied.


# =============================================================================
#
# 03. *args Can Receive One Argument
#
# =============================================================================

one_value: tuple[int, ...] = collect_values(
    10
)

print(
    one_value
)

# When one positional argument is supplied:

#

# collect_values(10)

#

# args becomes:

#

# (10,)

#

# Notice that args is still a tuple.


# =============================================================================
#
# 04. *args Can Receive Multiple Arguments
#
# =============================================================================

multiple_values: tuple[int, ...] = collect_values(
    10,
    20,
    30,
    40,
)

print(
    multiple_values
)

# All positional arguments are collected.

#

# Therefore:

#

# collect_values(
#     10,
#     20,
#     30,
#     40,
# )

#

# produces:

#

# (
#     10,
#     20,
#     30,
#     40,
# )


# =============================================================================
#
# 05. *args Is Stored as a Tuple
#
# =============================================================================

def inspect_arguments(
    *args: str,
) -> str:
    """
    Return information about the collected arguments.
    """
    return (
        f"type->{type(args).__name__}; "
        f"values->{args}"
    )


argument_information: str = inspect_arguments(
    "Python",
    "SQL",
    "Git",
)

print(
    argument_information
)

# The type of args is:

#

# tuple

#

# Therefore:

#

# *args

#

# does NOT create a list.

#

# It creates a tuple containing the collected positional arguments.


# =============================================================================
#
# 06. Iterating Over *args
#
# =============================================================================

def print_arguments(
    *args: str,
) -> None:
    """
    Print each positional argument.
    """
    for argument in args:
        print(
            argument
        )


print_arguments(
    "Python",
    "SQL",
    "Git",
)

# Because args is a tuple, it can be iterated over normally.

#

# The loop:

#

# for argument in args:

#

# processes each supplied positional argument.


# =============================================================================
#
# 07. Finding the Number of Arguments
#
# =============================================================================

def count_arguments(
    *args: int,
) -> int:
    """
    Return the number of positional arguments.
    """
    return (
        len(args)
    )


argument_count: int = count_arguments(
    10,
    20,
    30,
    40,
    50,
)

print(
    argument_count
)

# len(args)

#

# returns the number of collected positional arguments.

#

# Therefore:

#

# count_arguments(
#     10,
#     20,
#     30,
#     40,
#     50,
# )

#

# returns:

#

# 5


# =============================================================================
#
# 08. Accessing Individual Arguments
#
# =============================================================================

def get_first_argument(
    *args: str,
) -> str:
    """
    Return the first collected argument.
    """
    return (
        args[0]
    )


first_argument: str = get_first_argument(
    "Python",
    "SQL",
    "Git",
)

print(
    first_argument
)

# Since args is a tuple, normal tuple indexing can be used.

#

# args[0]

#

# accesses the first argument.


# =============================================================================
#
# 09. Accessing the Last Argument
#
# =============================================================================

def get_last_argument(
    *args: str,
) -> str:
    """
    Return the last collected argument.
    """
    return (
        args[-1]
    )


last_argument: str = get_last_argument(
    "Python",
    "SQL",
    "Git",
)

print(
    last_argument
)

# Negative indexing works because args is a tuple.

#

# args[-1]

#

# accesses the final collected argument.


# =============================================================================
#
# 10. Slicing *args
#
# =============================================================================

def get_first_three(
    *args: int,
) -> tuple[int, ...]:
    """
    Return the first three collected arguments.
    """
    return (
        args[:3]
    )


first_three: tuple[int, ...] = get_first_three(
    10,
    20,
    30,
    40,
    50,
)

print(
    first_three
)

# args supports tuple slicing.

#

# Therefore:

#

# args[:3]

#

# returns the first three values.


# =============================================================================
#
# 11. Required Parameter With *args
#
# =============================================================================

def greet_people(
    greeting: str,
    *names: str,
) -> str:
    """
    Create a greeting for multiple people.
    """
    return (
        f"{greeting}: {', '.join(names)}"
    )


people_greeting: str = greet_people(
    "Hello",
    "Alice",
    "Bob",
    "Charlie",
)

print(
    people_greeting
)

# greeting is a normal required parameter.

#

# names is a variable-length positional parameter.

#

# Therefore:

#

# "Hello"

# ↓

# greeting

#

# "Alice", "Bob", "Charlie"

# ↓

# names

#

# becomes:

#

# (
#     "Alice",
#     "Bob",
#     "Charlie",
# )


# =============================================================================
#
# 12. Required Parameter Is Assigned Before *args
#
# =============================================================================

def calculate_sum(
    start: int,
    *numbers: int,
) -> int:
    """
    Add the starting value and all additional numbers.
    """
    total: int = start

    for number in numbers:
        total += number

    return (
        total
    )


sum_result: int = calculate_sum(
    10,
    20,
    30,
    40,
)

print(
    sum_result
)

# The first positional argument is assigned to:

#

# start

#

# Remaining positional arguments are collected into:

#

# numbers

#

# Therefore:

#

# start = 10

#

# numbers = (20, 30, 40)


# =============================================================================
#
# 13. *args Collects Remaining Positional Arguments
#
# =============================================================================

def describe_order(
    order_id: int,
    *items: str,
) -> str:
    """
    Describe an order containing any number of items.
    """
    return (
        f"order->{order_id}; "
        f"items->{items}"
    )


order_description: str = describe_order(
    101,
    "Keyboard",
    "Mouse",
    "Monitor",
)

print(
    order_description
)

# order_id receives the first positional argument.

#

# items receives every remaining positional argument.

#

# Therefore:

#

# order_id = 101

#

# items = (
#     "Keyboard",
#     "Mouse",
#     "Monitor",
# )


# =============================================================================
#
# 14. *args Can Represent Zero Additional Arguments
#
# =============================================================================

def describe_order_empty(
    order_id: int,
    *items: str,
) -> str:
    """
    Describe an order that may contain zero or more items.
    """
    return (
        f"order->{order_id}; "
        f"items->{items}"
    )


empty_order: str = describe_order_empty(
    101,
)

print(
    empty_order
)

# order_id is still required.

#

# items is allowed to contain zero values.

#

# Therefore:

#

# describe_order_empty(101)

#

# produces:

#

# items = ()


# =============================================================================
#
# 15. *args Can Be Used With Calculations
#
# =============================================================================

def calculate_total(
    *prices: float,
) -> float:
    """
    Calculate the total of any number of prices.
    """
    total: float = 0.0

    for price in prices:
        total += price

    return (
        total
    )


total_price: float = calculate_total(
    100.0,
    250.0,
    50.0,
    75.0,
)

print(
    total_price
)

# The function does not need to know how many prices will be supplied.

#

# The caller can provide:

#

# one price

# two prices

# ten prices

# or any other number of positional prices.


# =============================================================================
#
# 16. *args With Strings
#
# =============================================================================

def combine_words(
    *words: str,
) -> str:
    """
    Combine multiple words into one string.
    """
    return (
        " ".join(words)
    )


combined_words: str = combine_words(
    "Python",
    "is",
    "easy",
    "to",
    "learn",
)

print(
    combined_words
)

# Each word becomes one element of args.

#

# words becomes:

#

# (
#     "Python",
#     "is",
#     "easy",
#     "to",
#     "learn",
# )


# =============================================================================
#
# 17. *args With Mixed Values
#
# =============================================================================

def inspect_values(
    *values: object,
) -> tuple[str, ...]:
    """
    Return the type name of every supplied value.
    """
    return tuple(
        type(value).__name__
        for value in values
    )


value_types: tuple[str, ...] = inspect_values(
    10,
    "Python",
    3.14,
    True,
)

print(
    value_types
)

# *args does not require all supplied values to have the same type.

#

# The annotation:

#

# object

#

# indicates that arbitrary Python objects may be supplied.


# =============================================================================
#
# 18. *args With a Loop
#
# =============================================================================

def calculate_product(
    *numbers: int,
) -> int:
    """
    Multiply all supplied numbers.
    """
    product: int = 1

    for number in numbers:
        product *= number

    return (
        product
    )


product_result: int = calculate_product(
    2,
    3,
    4,
)

print(
    product_result
)

# The function processes each collected value using a loop.

#

# numbers becomes:

#

# (2, 3, 4)

#

# The loop processes:

#

# 2

# ↓

# 3

# ↓

# 4


# =============================================================================
#
# 19. *args With Built-In Functions
#
# =============================================================================

def find_largest(
    *numbers: int,
) -> int:
    """
    Return the largest supplied number.
    """
    return (
        max(numbers)
    )


largest_number: int = find_largest(
    10,
    50,
    20,
    80,
    30,
)

print(
    largest_number
)

# max() expects an iterable.

#

# Since args is a tuple, it can be passed directly to max().


# =============================================================================
#
# 20. Passing a Tuple Using *
#
# =============================================================================

numbers: tuple[int, ...] = (
    10,
    20,
    30,
    40,
)


def calculate_average(
    *values: int,
) -> float:
    """
    Calculate the average of supplied values.
    """
    return (
        sum(values)
        /
        len(values)
    )


average_result: float = calculate_average(
    *numbers,
)

print(
    average_result
)

# The * operator can unpack an existing iterable when calling a function.

#

# Therefore:

#

# calculate_average(
#     *numbers,
# )

#

# behaves as though the values were supplied individually:

#

# calculate_average(
#     10,
#     20,
#     30,
#     40,
# )


# =============================================================================
#
# 21. Passing a List Using *
#
# =============================================================================

scores: list[int] = [
    80,
    90,
    70,
    95,
]

average_score: float = calculate_average(
    *scores,
)

print(
    average_score
)

# A list can also be unpacked using *.

#

# scores:

#

# [80, 90, 70, 95]

#

# becomes positional arguments:

#

# 80,

# 90,

# 70,

# 95

#

# when passed using:

#

# *scores


# =============================================================================
#
# 22. *args and Argument Unpacking
#
# =============================================================================

def create_sentence(
    *words: str,
) -> str:
    """
    Create a sentence from supplied words.
    """
    return (
        " ".join(words)
    )


sentence_words: list[str] = [
    "Python",
    "supports",
    "argument",
    "unpacking",
]

sentence: str = create_sentence(
    *sentence_words,
)

print(
    sentence
)

# The * operator has two related but different roles.

#

# In a function definition:

#

# *args

#

# collects positional arguments.

#

# In a function call:

#

# *values

#

# unpacks an iterable into positional arguments.


# =============================================================================
#
# 23. Combining Normal Arguments With Unpacking
#
# =============================================================================

def create_message(
    prefix: str,
    *words: str,
) -> str:
    """
    Create a message using a prefix and multiple words.
    """
    return (
        f"{prefix}: {' '.join(words)}"
    )


message_words: tuple[str, ...] = (
    "Python",
    "supports",
    "*args",
)

message: str = create_message(
    "INFO",
    *message_words,
)

print(
    message
)

# The first argument:

#

# "INFO"

#

# is assigned to prefix.

#

# The unpacked tuple provides the remaining positional arguments.

#

# Therefore:

#

# prefix = "INFO"

#

# words = (
#     "Python",
#     "supports",
#     "*args",
# )


# =============================================================================
#
# 24. *args Does Not Collect Keyword Arguments
#
# =============================================================================

def display_positional_arguments(
    *args: str,
) -> tuple[str, ...]:
    """
    Return positional arguments.
    """
    return (
        args
    )


positional_values: tuple[str, ...] = display_positional_arguments(
    "Python",
    "SQL",
)

print(
    positional_values
)

# *args collects positional arguments only.

#

# It does NOT collect keyword arguments.

#

# Keyword arguments require a different parameter syntax:

#

# **kwargs

#

# Therefore:

#

# *args

# ↓

# positional arguments

#

# **kwargs

# ↓

# keyword arguments


# =============================================================================
#
# 25. *args With Keyword Arguments
#
# =============================================================================

def describe_values(
    name: str,
    *values: int,
) -> str:
    """
    Describe positional values supplied after a name.
    """
    return (
        f"name->{name}; "
        f"values->{values}"
    )


description: str = describe_values(
    "Scores",
    10,
    20,
    30,
)

print(
    description
)

# The normal parameter receives:

#

# name

#

# The remaining positional arguments are collected into:

#

# values

#

# Keyword arguments can still be used for normal parameters when the
# function's parameter rules allow them.


# =============================================================================
#
# 26. Positional-Only Parameter With *args
#
# =============================================================================

def process_records(
    source_name: str,
    /,
    *records: str,
) -> str:
    """
    Process a source name and variable number of records.
    """
    return (
        f"source->{source_name}; "
        f"records->{records}"
    )


processed_records: str = process_records(
    "sales.csv",
    "record-1",
    "record-2",
    "record-3",
)

print(
    processed_records
)

# source_name is positional-only because it appears before /.

#

# records is variable-length positional data.

#

# Therefore:

#

# source_name

# ↓

# positional-only

#

# records

# ↓

# variable-length positional


# =============================================================================
#
# 27. Keyword-Only Parameters After *args
#
# =============================================================================

def configure_report(
    report_name: str,
    *columns: str,
    include_header: bool = True,
) -> str:
    """
    Configure a report with variable columns and an optional keyword-only
    setting.
    """
    return (
        f"report->{report_name}; "
        f"columns->{columns}; "
        f"include_header->{include_header!r}"
    )


default_report: str = configure_report(
    "sales",
    "date",
    "amount",
    "customer",
)

custom_report: str = configure_report(
    "sales",
    "date",
    "amount",
    "customer",
    include_header=False,
)

print(
    default_report
)

print(
    custom_report
)

# Once *columns appears, parameters that follow it are keyword-only.

#

# Therefore:

#

# include_header

#

# must be supplied using a keyword if the caller wants to override it.


# =============================================================================
#
# 28. *args Creates a Tuple Inside the Function
#
# =============================================================================

def demonstrate_tuple(
    *args: int,
) -> str:
    """
    Demonstrate the internal tuple created by *args.
    """
    return (
        f"values->{args}; "
        f"type->{type(args).__name__}"
    )


tuple_demonstration: str = demonstrate_tuple(
    1,
    2,
    3,
)

print(
    tuple_demonstration
)

# Python effectively collects the arguments into a tuple.

#

# Conceptually:

#

# demonstrate_tuple(
#     1,
#     2,
#     3,
# )

#

# behaves inside the function like:

#

# args = (
#     1,
#     2,
#     3,
# )


# =============================================================================
#
# 29. *args Can Be Named Something Else
#
# =============================================================================

def collect_numbers(
    *numbers: int,
) -> tuple[int, ...]:
    """
    Collect positional numbers.
    """
    return (
        numbers
    )


collected_numbers: tuple[int, ...] = collect_numbers(
    10,
    20,
    30,
)

print(
    collected_numbers
)

# The name args is only a convention.

#

# Python cares about the * symbol.

#

# Therefore these are all valid concepts:

#

# *args

#

# *numbers

#

# *values

#

# *items

#

# A descriptive name is usually preferable.


# =============================================================================
#
# 30. *args Must Be Used in the Correct Parameter Position
#
# =============================================================================

def calculate_values(
    first: int,
    *remaining: int,
) -> int:
    """
    Calculate the sum of the first and remaining values.
    """
    return (
        first
        +
        sum(remaining)
    )


calculated_values: int = calculate_values(
    10,
    20,
    30,
    40,
)

print(
    calculated_values
)

# A function can have one normal positional parameter before *args.

#

# The normal parameter receives its positional argument first.

#

# *args then receives all remaining positional arguments.


# =============================================================================
#
# 31. Parameters After *args Are Keyword-Only
#
# =============================================================================

def configure_process(
    process_name: str,
    *inputs: str,
    batch_size: int = 100,
) -> str:
    """
    Configure a process with variable inputs.
    """
    return (
        f"process->{process_name}; "
        f"inputs->{inputs}; "
        f"batch_size->{batch_size}"
    )


process_configuration: str = configure_process(
    "DataPipeline",
    "sales.csv",
    "customers.csv",
    batch_size=250,
)

print(
    process_configuration
)

# Once *inputs appears:

#

# batch_size

#

# becomes keyword-only.

#

# Therefore:

#

# batch_size=250

#

# is the correct way to supply the value.


# =============================================================================
#
# 32. *args With Default Behaviour
#
# =============================================================================

def format_items(
    prefix: str = "Items",
    *items: str,
) -> str:
    """
    Format any number of items with a default prefix.
    """
    return (
        f"{prefix}: {', '.join(items)}"
    )


default_formatted_items: str = format_items(
    "Python",
    "SQL",
)

custom_formatted_items: str = format_items(
    "Languages",
    "Python",
    "SQL",
)

print(
    default_formatted_items
)

print(
    custom_formatted_items
)

# A normal parameter can have a default value before *args.

#

# The first positional argument is still assigned to prefix.

#

# Remaining positional arguments are collected into items.


# =============================================================================
#
# 33. *args and Strict Calling Conventions
#
# =============================================================================

"""
A parameter using:

*args

answers:

"What number of positional arguments may this function receive?"

It allows zero or more positional arguments.

For example:

def example(
    *args: int,
) -> tuple[int, ...]:
    return args

The following are all valid:

example()

example(10)

example(10, 20)

example(10, 20, 30, 40)

The values are collected into a tuple.

Therefore:

example(
    10,
    20,
    30,
)

produces:

args = (
    10,
    20,
    30,
)

"""


# =============================================================================
#
# 34. *args and Positional-Only Behaviour
#
# =============================================================================

"""
Consider:

def example(
    value: int,
    /,
    *args: int,
) -> tuple[int, ...]:
    ...

Here:

value

is:

- required
- positional-only

while:

args

is:

- variable-length
- positional

Therefore:

example(
    10,
    20,
    30,
)

is valid.

The values are:

value = 10

args = (
    20,
    30,
)

The / controls how value may be supplied.

The *args controls how many additional positional arguments may be supplied.
"""


# =============================================================================
#
# 35. *args and Keyword-Only Behaviour
#
# =============================================================================

"""
Consider:

def example(
    *args: int,
    limit: int = 100,
) -> tuple[int, ...]:
    ...

The parameter:

args

collects positional arguments.

The parameter:

limit

is keyword-only.

Therefore:

example(
    10,
    20,
    limit=50,
)

is valid.

Conceptually:

args = (
    10,
    20,
)

limit = 50

The *args parameter does not collect:

limit=50

because keyword arguments are handled separately.
"""


# =============================================================================
#
# 36. Difference Between *args and **kwargs
#
# =============================================================================

"""
The two special parameter forms serve different purposes.

*args

collects:

positional arguments

Example:

def example(
    *args,
):
    ...

Call:

example(
    10,
    20,
    30,
)

Produces:

args = (
    10,
    20,
    30,
)

---

**kwargs

collects:

keyword arguments

Example:

def example(
    **kwargs,
):
    ...

Call:

example(
    name="Alex",
    age=30,
)

Produces a dictionary conceptually like:

kwargs = {
    "name": "Alex",
    "age": 30,
}

Therefore:

*args
    ↓
positional arguments

**kwargs
    ↓
keyword arguments
"""


# =============================================================================
#
# 37. Unpacking With Multiple Iterables
#
# =============================================================================

def collect_all_values(
    *values: int,
) -> tuple[int, ...]:
    """
    Collect values from multiple unpacked iterables.
    """
    return (
        values
    )


first_group: tuple[int, ...] = (
    10,
    20,
)

second_group: list[int] = [
    30,
    40,
]

all_values: tuple[int, ...] = collect_all_values(
    *first_group,
    *second_group,
    50,
)

print(
    all_values
)

# Multiple iterables can be unpacked into positional arguments.

#

# Therefore:

#

# *first_group

# ↓

# 10, 20

#

# *second_group

# ↓

# 30, 40

#

# and:

#

# 50

#

# is supplied directly.


# =============================================================================
#
# 38. *args With Strings and Unpacking
#
# =============================================================================

languages: tuple[str, ...] = (
    "Python",
    "Java",
    "Go",
)


def list_languages(
    *languages: str,
) -> str:
    """
    Return a comma-separated language list.
    """
    return (
        ", ".join(languages)
    )


language_list: str = list_languages(
    *languages,
)

print(
    language_list
)

# The tuple is unpacked before the function receives the arguments.

#

# The function receives:

#

# "Python"

# "Java"

# "Go"

#

# and collects them into:

#

# languages = (
#     "Python",
#     "Java",
#     "Go",
# )


# =============================================================================
#
# 39. *args With Empty Input
#
# =============================================================================

def join_values(
    *values: str,
) -> str:
    """
    Join zero or more values.
    """
    return (
        ", ".join(values)
    )


empty_result: str = join_values()

non_empty_result: str = join_values(
    "Python",
    "SQL",
)

print(
    empty_result
)

print(
    non_empty_result
)

# With no values:

#

# values = ()

#

# Joining an empty tuple produces an empty string.

#

# With values:

#

# values = (
#     "Python",
#     "SQL",
# )


# =============================================================================
#
# 40. *args Can Be Passed to Another Function
#
# =============================================================================

def sum_numbers(
    *numbers: int,
) -> int:
    """
    Return the sum of positional numbers.
    """
    return (
        sum(numbers)
    )


def calculate_sum_from_args(
    *numbers: int,
) -> int:
    """
    Calculate a sum using another function.
    """
    return (
        sum_numbers(
            *numbers
        )
    )


forwarded_sum: int = calculate_sum_from_args(
    10,
    20,
    30,
)

print(
    forwarded_sum
)

# *args can be unpacked and forwarded to another function.

#

# The collected tuple:

#

# numbers = (
#     10,
#     20,
#     30,
# )

#

# is unpacked using:

#

# *numbers

#

# and passed to sum_numbers().


# =============================================================================
#
# 41. *args Can Be Used To Build Flexible APIs
#
# =============================================================================

def log_messages(
    level: str,
    *messages: str,
) -> str:
    """
    Create a log containing any number of messages.
    """
    formatted_messages: tuple[str, ...] = tuple(
        f"[{level}] {message}"
        for message in messages
    )

    return (
        " | ".join(
            formatted_messages
        )
    )


log_output: str = log_messages(
    "INFO",
    "Application started",
    "Database connected",
    "Server ready",
)

print(
    log_output
)

# The function does not need to know how many messages will be supplied.

#

# This is one of the primary benefits of *args.

#

# The caller determines the number of positional values.


# =============================================================================
#
# 42. *args Does Not Mean "Any Type" Automatically
#
# =============================================================================

def calculate_numeric_sum(
    *numbers: int,
) -> int:
    """
    Calculate the sum of integer values.
    """
    return (
        sum(numbers)
    )


numeric_sum: int = calculate_numeric_sum(
    10,
    20,
    30,
)

print(
    numeric_sum
)

# The annotation:

#

# *numbers: int

#

# documents that the function expects integer values.

#

# The annotation does not itself enforce the types at runtime.

#

# Python's type annotations primarily provide information to developers,
# editors, linters, and static type checkers.


# =============================================================================
#
# 43. *args Can Be Combined With Type-Specific Processing
#
# =============================================================================

def calculate_maximum_price(
    *prices: float,
) -> float:
    """
    Return the maximum price.
    """
    return (
        max(prices)
    )


maximum_price: float = calculate_maximum_price(
    100.0,
    250.0,
    175.0,
    300.0,
)

print(
    maximum_price
)

# The function accepts any number of positional prices.

#

# Each collected value is expected to be a float.

#

# The values are stored in a tuple:

#

# prices = (
#     100.0,
#     250.0,
#     175.0,
#     300.0,
# )


# =============================================================================
#
# 44. *args and Argument Count Validation
#
# =============================================================================

def require_at_least_one(
    *values: str,
) -> str:
    """
    Require at least one positional argument.
    """
    if not values:
        raise ValueError(
            "At least one value is required."
        )

    return (
        values[0]
    )


required_value: str = require_at_least_one(
    "Python",
    "SQL",
)

print(
    required_value
)

# *args itself allows zero arguments.

#

# If a particular function requires at least one value, the function
# can validate that condition explicitly.

#

# Therefore:

#

# if not values:

#

# checks whether the tuple is empty.


# =============================================================================
#
# 45. *args and Tuple Operations
#
# =============================================================================

def analyze_arguments(
    *values: int,
) -> str:
    """
    Analyze the collected tuple.
    """
    return (
        f"count->{len(values)}; "
        f"first->{values[0]}; "
        f"last->{values[-1]}"
    )


argument_analysis: str = analyze_arguments(
    10,
    20,
    30,
    40,
)

print(
    argument_analysis
)

# Because args is a tuple, normal tuple operations are available.

#

# Examples include:

#

# len(args)

# args[0]

# args[-1]

# args[:2]

# value in args


# =============================================================================
#
# 46. Membership Testing With *args
#
# =============================================================================

def contains_value(
    target: str,
    *values: str,
) -> bool:
    """
    Check whether a target exists among the positional values.
    """
    return (
        target in values
    )


contains_python: bool = contains_value(
    "Python",
    "Python",
    "SQL",
    "Git",
)

print(
    contains_python
)

# Since values is a tuple, membership testing works normally.

#

# The expression:

#

# target in values

#

# checks whether the target exists in the collected arguments.


# =============================================================================
#
# 47. *args With a Required Parameter and Keyword-Only Option
#
# =============================================================================

def process_files(
    operation: str,
    *files: str,
    recursive: bool = False,
) -> str:
    """
    Process any number of files with an optional recursive setting.
    """
    return (
        f"operation->{operation}; "
        f"files->{files}; "
        f"recursive->{recursive!r}"
    )


default_file_processing: str = process_files(
    "delete",
    "temp.txt",
    "cache.txt",
)

custom_file_processing: str = process_files(
    "delete",
    "temp.txt",
    "cache.txt",
    recursive=True,
)

print(
    default_file_processing
)

print(
    custom_file_processing
)

# Parameter categories:

#

# operation

# ↓

# required positional parameter

#

#

# files

# ↓

# variable-length positional parameter

#

#

# recursive

# ↓

# keyword-only parameter with a default


# =============================================================================
#
# 48. *args Parameter Ordering Rules
#
# =============================================================================

"""
A function definition can contain:

normal parameters

followed by:

*args

and parameters after *args become keyword-only.

For example:

def example(
    required: int,
    *values: int,
    limit: int = 100,
) -> None:
    ...

The categories are:

required
    ↓
normal positional parameter


*values
    ↓
variable-length positional parameter


limit
    ↓
keyword-only parameter

The caller can write:

example(
    10,
    20,
    30,
    limit=50,
)

The values become:

required = 10

values = (
    20,
    30,
)

limit = 50
"""


# =============================================================================
#
# 49. *args Core Model
#
# =============================================================================

"""
Variable-length positional arguments:

*args

mean:

collect zero or more positional arguments

Example:

def example(
    *args: int,
) -> tuple[int, ...]:
    return args

Call:

example(
    10,
    20,
    30,
)

Python collects:

args = (
    10,
    20,
    30,
)

The key idea is:

multiple positional arguments
            ↓
          *args
            ↓
      collected tuple

No arguments:

args = ()

One argument:

args = (10,)

Multiple arguments:

args = (
    10,
    20,
    30,
)
"""


# =============================================================================
#
# 50. *args Summary
#
# =============================================================================

"""
Variable-length positional arguments:

- Are defined using *args or another name preceded by *.
- Allow a function to accept zero or more positional arguments.
- Collect positional arguments into a tuple.
- Can collect no arguments.
- Can collect one argument.
- Can collect many arguments.
- Can be iterated over.
- Can be indexed.
- Can be sliced.
- Support normal tuple operations.
- Can be combined with required parameters.
- Collect positional arguments that remain after normal positional parameters.
- Do not collect keyword arguments.
- Can be combined with keyword-only parameters.
- Can be used with positional-only parameters.
- Can be unpacked using * when calling another function.
- Can receive values from lists, tuples, and other iterables through unpacking.
- Are useful when the number of positional arguments is not known in advance.

Important distinction:

*args
    ↓
collects positional arguments


**kwargs
    ↓
collects keyword arguments


Function definition:

def example(
    *args,
):
    ...

means:

collect positional arguments
        ↓
store them in a tuple


Function call:

example(
    *values,
)

means:

unpack iterable
      ↓
pass its elements
as positional arguments

Therefore:

*args

in a function definition means:

COLLECT

while:

*values

in a function call means:

UNPACK
"""


# =============================================================================
#
# Key Takeaways
#
# =============================================================================

"""
✓ *args allows a function to accept a variable number of positional arguments.

✓ The name args is conventional; the * symbol is what creates the
  variable-length positional parameter.

✓ *args can receive zero, one, or many positional arguments.

✓ The collected arguments are stored as a tuple.

✓ The tuple can be indexed, sliced, iterated over, and inspected normally.

✓ A normal required parameter can appear before *args.

✓ The normal parameter receives its positional argument first.

✓ *args collects the remaining positional arguments.

✓ Parameters appearing after *args are keyword-only.

✓ *args does not collect keyword arguments.

✓ **kwargs is used for collecting keyword arguments.

✓ *args can be combined with positional-only parameters.

✓ *args can be combined with keyword-only parameters.

✓ The annotation *args: int documents that the collected values are expected
  to be integers.

✓ Type annotations do not automatically enforce types at runtime.

✓ *args is useful when the number of positional arguments is unknown in
  advance.

✓ An iterable can be unpacked into positional arguments using *.

✓ A list can be unpacked using *.

✓ A tuple can be unpacked using *.

✓ Multiple iterables can be unpacked into one function call.

✓ *args can be forwarded to another function by unpacking the tuple.

✓ *args itself does not require at least one argument.

✓ If a function requires at least one value, that condition must be validated
  explicitly.

Core idea:

CALLER
  ↓
multiple positional arguments
  ↓
*args
  ↓
tuple
  ↓
function processes the values

Example:

def example(
    *args: int,
) -> tuple[int, ...]:
    return args

Call:

example(
    10,
    20,
    30,
)

Result:

args = (
    10,
    20,
    30,
)

Important distinction:

FUNCTION DEFINITION

*args
   ↓
collect positional arguments
   ↓
tuple


FUNCTION CALL

*values
   ↓
unpack iterable
   ↓
positional arguments

Parameter model:

normal parameter
       ↓
receives a specific argument


*args
       ↓
receives remaining positional arguments


keyword-only parameter
       ↓
receives a keyword argument

Final mental model:

                FUNCTION
                   │
        ┌──────────┴──────────┐
        │                     │
   normal args              *args
        │                     │
 specific values        many positional values
                              │
                              ↓
                           tuple
"""