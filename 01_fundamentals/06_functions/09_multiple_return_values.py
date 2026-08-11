# =============================================================================
#
# Python Functions
#
# File
#
# 09_multiple_return_values.py
#
# Topic
#
# Multiple Return Values
#
# Overview
#
# Python functions can return multiple values from a single return statement.
#
# Python does not technically return several independent values. Instead,
# Python creates a single tuple containing the returned values.
#
# For example:
#
# def get_coordinates() -> tuple[int, int]:
#     return 10, 20
#
# The expression:
#
# return 10, 20
#
# creates:
#
# (10, 20)
#
# and returns that tuple.
#
# The caller can receive the complete tuple:
#
# coordinates = get_coordinates()
#
# or unpack the returned values:
#
# x, y = get_coordinates()
#
# Multiple return values are useful when a function needs to produce several
# related results together.
#
# Topics covered:
#
# - What multiple return values mean
# - Returning multiple values
# - Multiple values are returned as a tuple
# - Receiving the complete returned tuple
# - Tuple unpacking
# - Positional unpacking
# - Assigning returned values to separate variables
# - Returning values of different types
# - Returning calculated values
# - Returning multiple values with annotations
# - Tuple type annotations
# - Fixed-length tuple annotations
# - Returning an empty tuple
# - Returning one value versus multiple values
# - Parentheses are optional in tuple return expressions
# - Explicit tuple construction
# - Unpacking requires the correct number of variables
# - Using underscore for an intentionally ignored value
# - Extended unpacking with *
# - Multiple return values and function calls
# - Returning multiple values from conditional branches
# - Returning multiple values from loops
# - Returning named related values
# - Returning mutable objects together
# - Multiple return values and object identity
# - Multiple return values versus lists
# - Multiple return values versus dictionaries
# - Multiple return values and keyword arguments
# - Multiple return values with default arguments
# - Multiple return values and positional-only parameters
# - Multiple return values and keyword-only parameters
# - Nested tuple returns
# - Chained unpacking
# - Starred unpacking
# - Common unpacking mistakes
# - Returning too many or too few values
# - Returning multiple values with None
# - Designing useful return values
# - Multiple return values and type safety
# - Core mental model
#
# =============================================================================


# =============================================================================
# 01. Basic Multiple Return Values
# =============================================================================

def get_coordinates() -> tuple[int, int]:
    """
    Return two coordinate values.
    """
    return (
        10,
        20,
    )


coordinates: tuple[int, int] = get_coordinates()

print(
    coordinates
)

# The function appears to return two values:
#
# 10
#
# and:
#
# 20
#
# But Python actually creates one tuple:
#
# (10, 20)
#
# and returns that tuple.
#
# Therefore:
#
# type(coordinates)
#
# is:
#
# tuple
#
# The important idea is:
#
# multiple expressions after return
#             ↓
#         tuple object
#             ↓
#          returned
#
# =============================================================================


# =============================================================================
# 02. Multiple Return Values Are Actually A Tuple
# =============================================================================

def get_user_information() -> tuple[str, int]:
    """
    Return a user's name and age.
    """
    return (
        "Alex",
        30,
    )


user_information: tuple[str, int] = (
    get_user_information()
)

print(
    user_information
)

print(
    type(user_information)
)

# The function:
#
# return "Alex", 30
#
# behaves as though it returned:
#
# ("Alex", 30)
#
# Therefore multiple return values are implemented using tuple creation.
#
# Python does not have a special syntax for returning several independent
# values.
#
# Instead:
#
# return value_1, value_2, value_3
#
# creates:
#
# (value_1, value_2, value_3)
#
# and returns that tuple.
#
# =============================================================================


# =============================================================================
# 03. Receiving The Complete Returned Tuple
# =============================================================================

def get_dimensions() -> tuple[int, int]:
    """
    Return width and height.
    """
    return (
        1920,
        1080,
    )


dimensions: tuple[int, int] = get_dimensions()

print(
    dimensions
)

# The complete tuple can be stored in one variable.
#
# dimensions contains:
#
# (1920, 1080)
#
# No unpacking has occurred yet.
#
# =============================================================================


# =============================================================================
# 04. Unpacking Multiple Return Values
# =============================================================================

def get_dimensions_for_unpacking() -> tuple[int, int]:
    """
    Return width and height.
    """
    return (
        1920,
        1080,
    )


width: int
height: int

width, height = get_dimensions_for_unpacking()

print(
    width
)

print(
    height
)

# Python first receives:
#
# (1920, 1080)
#
# Then tuple unpacking assigns:
#
# width = 1920
#
# height = 1080
#
# Therefore:
#
# width, height = function()
#
# does not mean the function itself accepts two variables.
#
# The function returns one tuple.
#
# The assignment then unpacks that tuple.
#
# =============================================================================


# =============================================================================
# 05. Understanding The Unpacking Process
# =============================================================================

def get_values() -> tuple[int, int, int]:
    """
    Return three values.
    """
    return (
        10,
        20,
        30,
    )


values: tuple[int, int, int] = get_values()

first_value: int
second_value: int
third_value: int

first_value, second_value, third_value = values

print(
    first_value
)

print(
    second_value
)

print(
    third_value
)

# Conceptually:
#
# get_values()
#
# produces:
#
# (10, 20, 30)
#
# Then:
#
# first_value, second_value, third_value = values
#
# performs:
#
# first_value = 10
#
# second_value = 20
#
# third_value = 30
#
# =============================================================================


# =============================================================================
# 06. Directly Unpacking A Function Result
# =============================================================================

def get_name_and_age() -> tuple[str, int]:
    """
    Return a name and age.
    """
    return (
        "Shreyas",
        25,
    )


name: str
age: int

name, age = get_name_and_age()

print(
    name
)

print(
    age
)

# The tuple does not need to be stored first.
#
# Python can directly unpack the function's return value.
#
# This:
#
# name, age = get_name_and_age()
#
# is conceptually:
#
# returned_tuple = get_name_and_age()
#
# name, age = returned_tuple
#
# =============================================================================


# =============================================================================
# 07. Parentheses Are Not Required Around Multiple Return Values
# =============================================================================

def get_point() -> tuple[int, int]:
    """
    Return a point without explicit tuple parentheses.
    """
    return 10, 20


point: tuple[int, int] = get_point()

print(
    point
)

# These are equivalent:
#
# return 10, 20
#
# and:
#
# return (
#     10,
#     20,
# )
#
# Both create and return:
#
# (10, 20)
#
# Parentheses are often used for readability, especially when the values
# are written across multiple lines.
#
# =============================================================================


# =============================================================================
# 08. Explicit Tuple Construction
# =============================================================================

def get_point_explicitly() -> tuple[int, int]:
    """
    Explicitly construct and return a tuple.
    """
    return (
        10,
        20,
    )


point_explicit: tuple[int, int] = (
    get_point_explicitly()
)

print(
    point_explicit
)

# Multiple return expressions and explicit tuple construction produce the
# same basic result.
#
# Example:
#
# return 10, 20
#
# creates:
#
# (10, 20)
#
# While:
#
# return (10, 20)
#
# explicitly writes the tuple.
#
# =============================================================================


# =============================================================================
# 09. Returning Values Of Different Types
# =============================================================================

def get_profile_summary() -> tuple[str, int, bool]:
    """
    Return values of different types.
    """
    return (
        "Alex",
        30,
        True,
    )


profile_summary: tuple[str, int, bool] = (
    get_profile_summary()
)

print(
    profile_summary
)

# A returned tuple can contain different types.
#
# Here:
#
# first value
# ↓
# str
#
# second value
# ↓
# int
#
# third value
# ↓
# bool
#
# The annotation:
#
# tuple[str, int, bool]
#
# means:
#
# a tuple containing:
#
# str
# int
# bool
#
# in that exact positional structure.
#
# =============================================================================


# =============================================================================
# 10. Returning Calculated Values
# =============================================================================

def calculate_rectangle(
    width: float,
    height: float,
) -> tuple[float, float]:
    """
    Return the area and perimeter of a rectangle.
    """
    area: float = (
        width
        * height
    )

    perimeter: float = (
        2
        * (width + height)
    )

    return (
        area,
        perimeter,
    )


rectangle_results: tuple[float, float] = (
    calculate_rectangle(
        10.0,
        5.0,
    )
)

print(
    rectangle_results
)

# The function returns two related calculations:
#
# area
#
# and:
#
# perimeter
#
# The result is:
#
# (50.0, 30.0)
#
# =============================================================================


# =============================================================================
# 11. Unpacking Calculated Results
# =============================================================================

def calculate_rectangle_values(
    width: float,
    height: float,
) -> tuple[float, float]:
    """
    Return the area and perimeter of a rectangle.
    """
    area: float = (
        width
        * height
    )

    perimeter: float = (
        2
        * (width + height)
    )

    return (
        area,
        perimeter,
    )


area: float
perimeter: float

area, perimeter = calculate_rectangle_values(
    10.0,
    5.0,
)

print(
    area
)

print(
    perimeter
)

# Returning related values together can make the function easier to use.
#
# The caller can choose:
#
# store the complete tuple
#
# or:
#
# unpack the individual values.
#
# =============================================================================


# =============================================================================
# 12. Returning Three Calculated Values
# =============================================================================

def calculate_circle(
    radius: float,
) -> tuple[float, float, float]:
    """
    Return diameter, circumference, and area.
    """
    diameter: float = (
        2
        * radius
    )

    circumference: float = (
        2
        * 3.141592653589793
        * radius
    )

    area: float = (
        3.141592653589793
        * radius
        * radius
    )

    return (
        diameter,
        circumference,
        area,
    )


circle_results: tuple[float, float, float] = (
    calculate_circle(
        10.0,
    )
)

print(
    circle_results
)

# A function can return any number of related values.
#
# For example:
#
# return value_1, value_2, value_3
#
# creates a three-element tuple.
#
# =============================================================================


# =============================================================================
# 13. Returning And Unpacking Three Values
# =============================================================================

def get_student_record() -> tuple[str, int, float]:
    """
    Return a student's name, age, and score.
    """
    return (
        "Alex",
        21,
        91.5,
    )


student_name: str
student_age: int
student_score: float

student_name, student_age, student_score = (
    get_student_record()
)

print(
    student_name
)

print(
    student_age
)

print(
    student_score
)

# Each returned position maps to one variable:
#
# first returned value
# ↓
# student_name
#
# second returned value
# ↓
# student_age
#
# third returned value
# ↓
# student_score
#
# =============================================================================


# =============================================================================
# 14. Unpacking Requires Matching Number Of Values
# =============================================================================

def return_three_values() -> tuple[int, int, int]:
    """
    Return three integers.
    """
    return (
        10,
        20,
        30,
    )


# The following examples are intentionally not executed:
#
# first, second = return_three_values()
#
# This raises:
#
# ValueError
#
# because three values are being unpacked into two variables.
#
#
# first, second, third, fourth = return_three_values()
#
# This also raises:
#
# ValueError
#
# because four variables are being used for three returned values.
#
# The basic rule is:
#
# number of variables
#        must match
# number of unpacked values
#
# unless extended unpacking using * is used.
#
# =============================================================================


# =============================================================================
# 15. Ignoring A Returned Value Using Underscore
# =============================================================================

def get_report_data() -> tuple[str, int, float]:
    """
    Return report information.
    """
    return (
        "Sales",
        100,
        95.5,
    )


report_name: str
report_count: int
_ignored_score: float

report_name, report_count, _ignored_score = (
    get_report_data()
)

print(
    report_name
)

print(
    report_count
)

# A common convention is to use underscore:
#
# report_name, report_count, _ = get_report_data()
#
# to indicate that a value is intentionally ignored.
#
# Example:
#
# first_value, _, third_value = (
#     return_three_values()
# )
#
# The underscore is simply a normal variable name in Python.
#
# Its special meaning is a convention:
#
# "I intentionally do not care about this value."
#
# =============================================================================


# =============================================================================
# 16. Ignoring Multiple Values
# =============================================================================

def get_four_values() -> tuple[int, int, int, int]:
    """
    Return four values.
    """
    return (
        10,
        20,
        30,
        40,
    )


first: int
fourth: int

first, _, _, fourth = get_four_values()

print(
    first
)

print(
    fourth
)

# This keeps only:
#
# first
#
# and:
#
# fourth
#
# while the middle values are intentionally ignored.
#
# =============================================================================


# =============================================================================
# 17. Extended Unpacking With *
# =============================================================================

def get_many_values() -> tuple[int, int, int, int, int]:
    """
    Return several values.
    """
    return (
        10,
        20,
        30,
        40,
        50,
    )


first_value_extended: int
middle_values: list[int]
last_value_extended: int

(
    first_value_extended,
    *middle_values,
    last_value_extended,
) = get_many_values()

print(
    first_value_extended
)

print(
    middle_values
)

print(
    last_value_extended
)

# The starred variable receives all remaining values.
#
# Result:
#
# first_value_extended = 10
#
# middle_values = [20, 30, 40]
#
# last_value_extended = 50
#
# Important:
#
# the starred target receives a list.
#
# Even though the original returned object is a tuple,
# the starred unpacking target becomes a list.
#
# =============================================================================


# =============================================================================
# 18. Starred Unpacking At The Beginning
# =============================================================================

def get_numbers() -> tuple[int, int, int, int]:
    """
    Return four numbers.
    """
    return (
        10,
        20,
        30,
        40,
    )


remaining_numbers: list[int]
last_number: int

(
    *remaining_numbers,
    last_number,
) = get_numbers()

print(
    remaining_numbers
)

print(
    last_number
)

# Result:
#
# remaining_numbers = [10, 20, 30]
#
# last_number = 40
#
# =============================================================================


# =============================================================================
# 19. Starred Unpacking At The End
# =============================================================================

first_number: int
remaining_numbers_at_end: list[int]

(
    first_number,
    *remaining_numbers_at_end,
) = get_numbers()

print(
    first_number
)

print(
    remaining_numbers_at_end
)

# Result:
#
# first_number = 10
#
# remaining_numbers_at_end = [20, 30, 40]
#
# =============================================================================


# =============================================================================
# 20. Starred Unpacking Can Capture Zero Values
# =============================================================================

def return_two_values() -> tuple[int, int]:
    """
    Return two values.
    """
    return (
        10,
        20,
    )


first_two: int
remaining_two: list[int]

(
    first_two,
    *remaining_two,
) = return_two_values()

print(
    first_two
)

print(
    remaining_two
)

# The starred target may receive:
#
# zero values
#
# or:
#
# one value
#
# or:
#
# many values
#
# depending on the number of values available.
#
# =============================================================================


# =============================================================================
# 21. Multiple Return Values From Conditional Branches
# =============================================================================

def analyze_number(
    number: int,
) -> tuple[str, bool]:
    """
    Return a description and whether the number is positive.
    """
    if number > 0:
        return (
            "positive",
            True,
        )

    if number < 0:
        return (
            "negative",
            False,
        )

    return (
        "zero",
        False,
    )


positive_result: tuple[str, bool] = analyze_number(
    10
)

negative_result: tuple[str, bool] = analyze_number(
    -5
)

zero_result: tuple[str, bool] = analyze_number(
    0
)

print(
    positive_result
)

print(
    negative_result
)

print(
    zero_result
)

# Every branch returns the same tuple structure:
#
# tuple[str, bool]
#
# This is important for predictable function behaviour.
#
# =============================================================================


# =============================================================================
# 22. Multiple Return Values From A Loop
# =============================================================================

def find_first_even(
    numbers: list[int],
) -> tuple[int | None, bool]:
    """
    Return the first even number and whether one was found.
    """
    for number in numbers:
        if number % 2 == 0:
            return (
                number,
                True,
            )

    return (
        None,
        False,
    )


even_number: int | None
was_found: bool

even_number, was_found = find_first_even(
    [
        1,
        3,
        7,
        8,
        11,
    ]
)

print(
    even_number
)

print(
    was_found
)

# The function communicates two pieces of information:
#
# the value found
#
# and:
#
# whether a value was found.
#
# Returning multiple values can be useful when one result alone does not
# provide enough information.
#
# =============================================================================


# =============================================================================
# 23. Returning None As One Of Multiple Values
# =============================================================================

def find_user(
    user_id: int,
) -> tuple[str | None, bool]:
    """
    Return a username and whether the user exists.
    """
    if user_id == 1:
        return (
            "Alex",
            True,
        )

    return (
        None,
        False,
    )


username: str | None
user_exists: bool

username, user_exists = find_user(
    2
)

print(
    username
)

print(
    user_exists
)

# A tuple can contain None.
#
# Here:
#
# username
#
# may be:
#
# str
#
# or:
#
# None
#
# Therefore:
#
# str | None
#
# correctly represents that possibility.
#
# =============================================================================


# =============================================================================
# 24. Multiple Return Values With Default Arguments
# =============================================================================

def calculate_price(
    price: float,
    tax_percentage: float = 18.0,
) -> tuple[float, float]:
    """
    Return tax amount and final price.
    """
    tax_amount: float = (
        price
        * tax_percentage
        / 100
    )

    final_price: float = (
        price
        + tax_amount
    )

    return (
        tax_amount,
        final_price,
    )


default_tax_amount: float
default_final_price: float

default_tax_amount, default_final_price = (
    calculate_price(
        1000.0,
    )
)

custom_tax_amount: float
custom_final_price: float

custom_tax_amount, custom_final_price = (
    calculate_price(
        1000.0,
        10.0,
    )
)

print(
    default_tax_amount
)

print(
    default_final_price
)

print(
    custom_tax_amount
)

print(
    custom_final_price
)

# The function has:
#
# price
# ↓
# required
#
# tax_percentage
# ↓
# default value
#
# It returns:
#
# tax_amount
#
# and:
#
# final_price
#
# =============================================================================


# =============================================================================
# 25. Multiple Return Values With Positional-Only Parameters
# =============================================================================

def calculate_statistics(
    first_number: float,
    second_number: float,
    /,
) -> tuple[float, float]:
    """
    Return the sum and difference of two numbers.
    """
    total: float = (
        first_number
        + second_number
    )

    difference: float = (
        first_number
        - second_number
    )

    return (
        total,
        difference,
    )


statistics_result: tuple[float, float] = (
    calculate_statistics(
        20.0,
        5.0,
    )
)

print(
    statistics_result
)

# The parameters before / are positional-only.
#
# The return value is still completely independent of the argument-passing
# convention.
#
# The function:
#
# accepts positional arguments
#
# and:
#
# returns a tuple.
#
# =============================================================================


# =============================================================================
# 26. Multiple Return Values With Keyword-Only Parameters
# =============================================================================

def calculate_discounted_price(
    price: float,
    *,
    discount_percentage: float = 10.0,
) -> tuple[float, float]:
    """
    Return discount amount and final price.
    """
    discount_amount: float = (
        price
        * discount_percentage
        / 100
    )

    final_price: float = (
        price
        - discount_amount
    )

    return (
        discount_amount,
        final_price,
    )


discount_amount: float
final_discounted_price: float

discount_amount, final_discounted_price = (
    calculate_discounted_price(
        1000.0,
        discount_percentage=20.0,
    )
)

print(
    discount_amount
)

print(
    final_discounted_price
)

# discount_percentage is keyword-only.
#
# This affects how the input is supplied.
#
# It does NOT affect how the output is returned.
#
# The function still returns:
#
# tuple[float, float]
#
# =============================================================================


# =============================================================================
# 27. Returning A Tuple Of Strings
# =============================================================================

def get_full_name() -> tuple[str, str]:
    """
    Return first name and last name.
    """
    return (
        "Alex",
        "Sharma",
    )


first_name: str
last_name: str

first_name, last_name = get_full_name()

print(
    first_name
)

print(
    last_name
)

# Multiple return values are not restricted to calculations.
#
# They can represent related textual information as well.
#
# =============================================================================


# =============================================================================
# 28. Returning Mutable Objects Together
# =============================================================================

def create_collections() -> tuple[list[int], dict[str, int]]:
    """
    Return a list and a dictionary together.
    """
    numbers: list[int] = [
        10,
        20,
        30,
    ]

    scores: dict[str, int] = {
        "Alex": 90,
    }

    return (
        numbers,
        scores,
    )


numbers: list[int]
scores: dict[str, int]

numbers, scores = create_collections()

print(
    numbers
)

print(
    scores
)

# A tuple can contain mutable objects.
#
# The tuple itself is immutable.
#
# But the objects stored inside it can still be mutable.
#
# Therefore:
#
# tuple[list[int], dict[str, int]]
#
# is valid.
#
# =============================================================================


# =============================================================================
# 29. Returning Existing Objects Does Not Copy Them
# =============================================================================

def return_existing_objects(
    numbers: list[int],
) -> tuple[list[int], list[int]]:
    """
    Return the same list object twice.
    """
    return (
        numbers,
        numbers,
    )


original_numbers: list[int] = [
    1,
    2,
    3,
]

first_reference: list[int]
second_reference: list[int]

first_reference, second_reference = (
    return_existing_objects(
        original_numbers,
    )
)

print(
    first_reference
)

print(
    second_reference
)

print(
    first_reference is second_reference
)

# The function returns the same list object twice.
#
# It does NOT automatically create two copies.
#
# Therefore:
#
# first_reference is second_reference
#
# is:
#
# True
#
# Returning multiple values does not imply copying the objects.
#
# =============================================================================


# =============================================================================
# 30. Returning An Empty Tuple
# =============================================================================

def return_nothing_as_tuple() -> tuple[()]:
    """
    Return an empty tuple.
    """
    return ()


empty_result: tuple[()] = (
    return_nothing_as_tuple()
)

print(
    empty_result
)

# An empty tuple contains zero values.
#
# The syntax:
#
# return ()
#
# returns an empty tuple.
#
# This is different from:
#
# return None
#
# None is a single object representing the absence of a value.
#
# () is an empty tuple.
#
# =============================================================================


# =============================================================================
# 31. Returning One Value Is Not The Same As Returning A One-Element Tuple
# =============================================================================

def return_one_value() -> int:
    """
    Return one integer.
    """
    return 10


def return_one_element_tuple() -> tuple[int]:
    """
    Return a one-element tuple.
    """
    return (
        10,
    )


single_value: int = return_one_value()

single_element_tuple: tuple[int] = (
    return_one_element_tuple()
)

print(
    single_value
)

print(
    single_element_tuple
)

print(
    type(single_value)
)

print(
    type(single_element_tuple)
)

# These are different:
#
# return 10
#
# and:
#
# return 10,
#
# The comma creates the tuple.
#
# A one-element tuple requires the comma:
#
# (10,)
#
# not:
#
# (10)
#
# because:
#
# (10)
#
# is simply the integer 10 surrounded by parentheses.
#
# =============================================================================


# =============================================================================
# 32. One Value Versus One-Element Tuple
# =============================================================================

single_value_expression: int = (
    10
)

single_tuple_expression: tuple[int] = (
    10,
)

print(
    single_value_expression
)

print(
    single_tuple_expression
)

print(
    type(single_value_expression)
)

print(
    type(single_tuple_expression)
)

# Parentheses alone do not create a tuple.
#
# The comma creates a tuple.
#
# Therefore:
#
# (10)
#
# means:
#
# 10
#
# while:
#
# (10,)
#
# means:
#
# tuple containing 10
#
# =============================================================================


# =============================================================================
# 33. Returning Nested Tuples
# =============================================================================

def get_nested_coordinates() -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Return two coordinate pairs.
    """
    return (
        (
            10,
            20,
        ),
        (
            30,
            40,
        ),
    )


nested_coordinates: tuple[tuple[int, int], tuple[int, int]] = (
    get_nested_coordinates()
)

print(
    nested_coordinates
)

# The return value is:
#
# (
#     (10, 20),
#     (30, 40),
# )
#
# The outer tuple contains two inner tuples.
#
# Therefore tuple structures can be nested.
#
# =============================================================================


# =============================================================================
# 34. Nested Tuple Unpacking
# =============================================================================

def get_nested_point_data() -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Return two coordinate pairs.
    """
    return (
        (
            10,
            20,
        ),
        (
            30,
            40,
        ),
    )


(
    (
        x1,
        y1,
    ),
    (
        x2,
        y2,
    ),
) = get_nested_point_data()

print(
    x1
)

print(
    y1
)

print(
    x2
)

print(
    y2
)

# Python can unpack nested tuple structures recursively.
#
# Returned value:
#
# (
#     (10, 20),
#     (30, 40),
# )
#
# becomes:
#
# x1 = 10
# y1 = 20
# x2 = 30
# y2 = 40
#
# =============================================================================


# =============================================================================
# 35. Chained Unpacking
# =============================================================================

def get_pair() -> tuple[int, int]:
    """
    Return a pair of numbers.
    """
    return (
        10,
        20,
    )


first_pair: tuple[int, int]
second_pair: tuple[int, int]

first_pair = get_pair()
second_pair = get_pair()

print(
    first_pair
)

print(
    second_pair
)

# A function can be called multiple times and each returned tuple can be
# stored independently.
#
# =============================================================================


# =============================================================================
# 36. Returning Related Results Together
# =============================================================================

def parse_name(
    full_name: str,
) -> tuple[str, str]:
    """
    Return first name and last name.
    """
    first_name: str
    last_name: str

    first_name, last_name = (
        full_name.split(
            " ",
            1,
        )
    )

    return (
        first_name,
        last_name,
    )


parsed_first_name: str
parsed_last_name: str

parsed_first_name, parsed_last_name = parse_name(
    "Alex Sharma"
)

print(
    parsed_first_name
)

print(
    parsed_last_name
)

# Multiple return values are particularly useful when several values are
# naturally produced by one operation.
#
# Here the parsing operation produces:
#
# first_name
#
# and:
#
# last_name
#
# =============================================================================


# =============================================================================
# 37. Returning Success And Result
# =============================================================================

def divide_safely(
    dividend: float,
    divisor: float,
) -> tuple[float | None, bool]:
    """
    Return the division result and whether division succeeded.
    """
    if divisor == 0:
        return (
            None,
            False,
        )

    result: float = (
        dividend
        / divisor
    )

    return (
        result,
        True,
    )


division_result: float | None
division_succeeded: bool

division_result, division_succeeded = divide_safely(
    100.0,
    5.0,
)

print(
    division_result
)

print(
    division_succeeded
)

# This pattern is sometimes useful:
#
# (
#     result,
#     success,
# )
#
# The caller receives both the result and information about whether the
# operation succeeded.
#
# =============================================================================


# =============================================================================
# 38. Multiple Return Values And Conditional Unpacking
# =============================================================================

def get_status() -> tuple[int, str]:
    """
    Return a status code and description.
    """
    return (
        200,
        "OK",
    )


status_code: int
status_message: str

status_code, status_message = get_status()

if status_code == 200:
    print(
        status_message
    )

# The returned values can immediately participate in normal control flow.
#
# =============================================================================


# =============================================================================
# 39. Multiple Return Values Can Be Passed To Another Function
# =============================================================================

def get_min_max() -> tuple[int, int]:
    """
    Return minimum and maximum values.
    """
    return (
        10,
        100,
    )


def display_range(
    minimum: int,
    maximum: int,
) -> str:
    """
    Return a formatted range.
    """
    return (
        f"Range: {minimum} -> {maximum}"
    )


range_description: str = display_range(
    *get_min_max()
)

print(
    range_description
)

# The * operator here performs argument unpacking.
#
# get_min_max()
#
# returns:
#
# (10, 100)
#
# Then:
#
# *get_min_max()
#
# expands it into positional arguments:
#
# 10, 100
#
# Therefore:
#
# display_range(
#     *get_min_max()
# )
#
# behaves like:
#
# display_range(
#     10,
#     100,
# )
#
# This is different from assignment unpacking, but both use the * syntax
# for unpacking.
#
# =============================================================================


# =============================================================================
# 40. Returning Multiple Values Does Not Require Tuple Syntax In The Caller
# =============================================================================

def get_version() -> tuple[int, int, int]:
    """
    Return a software version.
    """
    return (
        3,
        11,
        7,
    )


major: int
minor: int
patch: int

major, minor, patch = get_version()

print(
    major
)

print(
    minor
)

print(
    patch
)

# The caller does not need to manually construct or access a tuple.
#
# Python automatically performs unpacking when the assignment target contains
# multiple names.
#
# =============================================================================


# =============================================================================
# 41. Common Mistake: Treating Multiple Return Values As Separate Objects
# =============================================================================

def get_two_values() -> tuple[int, int]:
    """
    Return two values.
    """
    return (
        10,
        20,
    )


result: tuple[int, int] = get_two_values()

print(
    result
)

# A common mental model is:
#
# "The function returned two separate objects."
#
# A more accurate model is:
#
# "The function returned one tuple containing two objects."
#
# Therefore:
#
# result
#
# refers to:
#
# (10, 20)
#
# =============================================================================


# =============================================================================
# 42. Common Mistake: Wrong Unpacking Count
# =============================================================================

def get_three_values() -> tuple[int, int, int]:
    """
    Return three values.
    """
    return (
        10,
        20,
        30,
    )


# The following is intentionally not executed:
#
# first, second = get_three_values()
#
# Python raises:
#
# ValueError:
# too many values to unpack
#
#
# Another invalid example:
#
# first, second, third, fourth = get_three_values()
#
# Python raises:
#
# ValueError:
# not enough values to unpack
#
# The number of targets must normally match the number of returned values.
#
# =============================================================================


# =============================================================================
# 43. Common Mistake: Forgetting The Comma In A One-Element Tuple
# =============================================================================

one_element_tuple: tuple[int] = (
    10,
)

print(
    one_element_tuple
)

# Correct:
#
# (10,)
#
# Incorrect if the intention is a tuple:
#
# (10)
#
# The comma is what makes the tuple.
#
# =============================================================================


# =============================================================================
# 44. Returning Multiple Values From Different Branches
# =============================================================================

def classify_score(
    score: float,
) -> tuple[str, bool]:
    """
    Return a classification and whether the score is passing.
    """
    if score >= 90:
        return (
            "excellent",
            True,
        )

    if score >= 50:
        return (
            "pass",
            True,
        )

    return (
        "fail",
        False,
    )


classification: str
passing: bool

classification, passing = classify_score(
    75.0
)

print(
    classification
)

print(
    passing
)

# All branches maintain the same return structure:
#
# tuple[str, bool]
#
# Keeping return shapes consistent makes functions easier to reason about.
#
# =============================================================================


# =============================================================================
# 45. Multiple Return Values With Boolean Information
# =============================================================================

def validate_age(
    age: int,
) -> tuple[bool, str]:
    """
    Return validation status and an explanatory message.
    """
    if age < 0:
        return (
            False,
            "Age cannot be negative.",
        )

    return (
        True,
        "Age is valid.",
    )


is_valid: bool
validation_message: str

is_valid, validation_message = validate_age(
    25
)

print(
    is_valid
)

print(
    validation_message
)

# Returning:
#
# status
#
# and:
#
# explanation
#
# can make a function's result more informative than returning only True or
# False.
#
# =============================================================================


# =============================================================================
# 46. Multiple Return Values And Lists
# =============================================================================

def return_fixed_values() -> tuple[int, int, int]:
    """
    Return three fixed-position values.
    """
    return (
        10,
        20,
        30,
    )


def return_list_values() -> list[int]:
    """
    Return a list of values.
    """
    return [
        10,
        20,
        30,
    ]


fixed_values: tuple[int, int, int] = (
    return_fixed_values()
)

list_values: list[int] = (
    return_list_values()
)

print(
    fixed_values
)

print(
    list_values
)

# Both can contain multiple values, but their meanings differ.
#
# tuple:
#
# usually represents a fixed collection of related values.
#
# list:
#
# usually represents a variable-size collection of values.
#
# A tuple can communicate:
#
# position 1 = name
# position 2 = age
# position 3 = score
#
# A list generally communicates:
#
# a sequence of similar or interchangeable items.
#
# =============================================================================


# =============================================================================
# 47. Multiple Return Values And Dictionaries
# =============================================================================

def return_profile_tuple() -> tuple[str, int]:
    """
    Return a name and age as a tuple.
    """
    return (
        "Alex",
        30,
    )


def return_profile_dictionary() -> dict[str, str | int]:
    """
    Return a profile as a dictionary.
    """
    return {
        "name": "Alex",
        "age": 30,
    }


profile_tuple: tuple[str, int] = (
    return_profile_tuple()
)

profile_dictionary: dict[str, str | int] = (
    return_profile_dictionary()
)

print(
    profile_tuple
)

print(
    profile_dictionary
)

# Tuples are position-based:
#
# profile_tuple[0]
# ↓
# name
#
# profile_tuple[1]
# ↓
# age
#
# Dictionaries are key-based:
#
# profile_dictionary["name"]
#
# profile_dictionary["age"]
#
# If the values have a fixed positional meaning, a tuple can be appropriate.
#
# If named access is more important, a dictionary may be clearer.
#
# =============================================================================


# =============================================================================
# 48. Returning A Named Tuple-Like Structure
# =============================================================================

from typing import NamedTuple


class UserSummary(NamedTuple):
    """
    Represent a user's summary using named fields.
    """
    name: str
    age: int


def get_user_summary() -> UserSummary:
    """
    Return a named user summary.
    """
    return UserSummary(
        name="Alex",
        age=30,
    )


user_summary: UserSummary = (
    get_user_summary()
)

print(
    user_summary
)

print(
    user_summary.name
)

print(
    user_summary.age
)

# A NamedTuple provides:
#
# tuple behaviour
#
# together with:
#
# named attribute access.
#
# This can be useful when returning several related values whose positions
# might otherwise be difficult to remember.
#
# =============================================================================


# =============================================================================
# 49. Multiple Return Values And Type Annotations
# =============================================================================

def get_measurements() -> tuple[int, float, str]:
    """
    Return measurements with different types.
    """
    return (
        10,
        25.5,
        "cm",
    )


measurements: tuple[int, float, str] = (
    get_measurements()
)

print(
    measurements
)

# The return annotation describes the complete returned tuple.
#
# tuple[int, float, str]
#
# means:
#
# first element
# ↓
# int
#
# second element
# ↓
# float
#
# third element
# ↓
# str
#
# =============================================================================


# =============================================================================
# 50. Fixed-Length Tuple Annotation
# =============================================================================

def get_fixed_record() -> tuple[str, int, bool]:
    """
    Return a fixed-length typed tuple.
    """
    return (
        "Alex",
        30,
        True,
    )


fixed_record: tuple[str, int, bool] = (
    get_fixed_record()
)

print(
    fixed_record
)

# This is a fixed-length tuple annotation.
#
# tuple[str, int, bool]
#
# specifically describes three positions.
#
# It is different from:
#
# tuple[str]
#
# which represents a tuple whose elements are all strings, rather than a
# fixed three-element tuple containing different types.
#
# =============================================================================


# =============================================================================
# 51. Variable-Length Homogeneous Tuple
# =============================================================================

def get_scores() -> tuple[float, ...]:
    """
    Return a variable-length tuple of floats.
    """
    return (
        85.5,
        90.0,
        92.5,
        88.0,
    )


scores_51: tuple[float, ...] = (
    get_scores()
)

print(
    scores
)

# The annotation:
#
# tuple[float, ...]
#
# means:
#
# a tuple containing zero or more float values.
#
# The three dots are important.
#
# Compare:
#
# tuple[float]
#
# versus:
#
# tuple[float, ...]
#
# The second form represents a variable-length tuple.
#
# =============================================================================


# =============================================================================
# 52. Returning A Variable Number Of Results
# =============================================================================

def collect_even_numbers(
    numbers: list[int],
) -> tuple[int, ...]:
    """
    Return all even numbers as a tuple.
    """
    even_numbers: list[int] = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(
                number
            )

    return tuple(
        even_numbers
    )


even_numbers: tuple[int, ...] = (
    collect_even_numbers(
        [
            1,
            2,
            3,
            4,
            5,
            6,
        ]
    )
)

print(
    even_numbers
)

# The number of returned values can vary.
#
# But the return object is still one tuple.
#
# Example:
#
# ()
#
# or:
#
# (2,)
#
# or:
#
# (2, 4, 6)
#
# The annotation:
#
# tuple[int, ...]
#
# represents this variable-length structure.
#
# =============================================================================


# =============================================================================
# 53. Returning Multiple Values And Argument Unpacking
# =============================================================================

def add_three_numbers(
    first: int,
    second: int,
    third: int,
) -> int:
    """
    Add three numbers.
    """
    return (
        first
        + second
        + third
    )


def get_three_numbers() -> tuple[int, int, int]:
    """
    Return three numbers.
    """
    return (
        10,
        20,
        30,
    )


sum_of_numbers: int = add_three_numbers(
    *get_three_numbers()
)

print(
    sum_of_numbers
)

# The returned tuple:
#
# (10, 20, 30)
#
# is unpacked into positional arguments:
#
# add_three_numbers(
#     10,
#     20,
#     30,
# )
#
# This demonstrates an important distinction:
#
# return-value unpacking:
#
# a, b = function()
#
# and:
#
# argument unpacking:
#
# function(*tuple_value)
#
# Both involve tuples, but they occur in different contexts.
#
# =============================================================================


# =============================================================================
# 54. Returning Multiple Values From Another Function
# =============================================================================

def get_base_values() -> tuple[int, int]:
    """
    Return two base values.
    """
    return (
        10,
        20,
    )


def transform_values(
    first: int,
    second: int,
) -> tuple[int, int]:
    """
    Transform and return two values.
    """
    return (
        first * 2,
        second * 2,
    )


transformed_values: tuple[int, int] = (
    transform_values(
        *get_base_values()
    )
)

print(
    transformed_values
)

# The flow is:
#
# get_base_values()
#        ↓
# (10, 20)
#        ↓
# * unpacking
#        ↓
# transform_values(10, 20)
#        ↓
# (20, 40)
#
# =============================================================================


# =============================================================================
# 55. Returning Multiple Values Does Not Mean Multiple Return Statements
# =============================================================================

def get_name_and_score() -> tuple[str, int]:
    """
    Return a name and score from one return statement.
    """
    return (
        "Alex",
        95,
    )


name_and_score: tuple[str, int] = (
    get_name_and_score()
)

print(
    name_and_score
)

# Multiple values normally come from one return statement:
#
# return value_1, value_2
#
# This is different from having multiple return statements in a function.
#
# For example:
#
# if condition:
#     return value_1, value_2
#
# else:
#     return value_3, value_4
#
# still means each individual return statement returns one tuple.
#
# =============================================================================


# =============================================================================
# 56. Multiple Return Statements Can Have The Same Shape
# =============================================================================

def get_result(
    success: bool,
) -> tuple[bool, str]:
    """
    Return a success status and message.
    """
    if success:
        return (
            True,
            "Operation completed.",
        )

    return (
        False,
        "Operation failed.",
    )


successful_result: tuple[bool, str] = (
    get_result(
        True
    )
)

failed_result: tuple[bool, str] = (
    get_result(
        False
    )
)

print(
    successful_result
)

print(
    failed_result
)

# Multiple return statements are perfectly valid.
#
# The important point is that each branch should maintain a predictable
# return structure when the function's contract expects one.
#
# =============================================================================


# =============================================================================
# 57. Multiple Return Values And Object Identity
# =============================================================================

def return_same_object(
    value: list[int],
) -> tuple[list[int], list[int]]:
    """
    Return the same object twice.
    """
    return (
        value,
        value,
    )


values_57: list[int] = [
    1,
    2,
]

first_result: list[int]
second_result: list[int]

first_result, second_result = return_same_object(
    values_57
)

print(
    first_result is second_result
)

# The result is:
#
# True
#
# because both tuple positions contain a reference to the same list object.
#
# A tuple stores references to objects.
#
# It does not automatically copy those objects.
#
# =============================================================================


# =============================================================================
# 58. Multiple Return Values And Mutability
# =============================================================================

def create_two_lists() -> tuple[list[int], list[int]]:
    """
    Return two separate list objects.
    """
    first_list: list[int] = [
        1,
        2,
    ]

    second_list: list[int] = [
        3,
        4,
    ]

    return (
        first_list,
        second_list,
    )


first_list_result: list[int]
second_list_result: list[int]

first_list_result, second_list_result = create_two_lists()

first_list_result.append(
    5
)

print(
    first_list_result
)

print(
    second_list_result
)

# The two lists are separate objects.
#
# Modifying one does not modify the other.
#
# Multiple return values do not automatically imply shared state.
#
# The relationship depends on the objects placed inside the returned tuple.
#
# =============================================================================


# =============================================================================
# 59. Returning Computation And Metadata Together
# =============================================================================

def calculate_average(
    numbers: list[float],
) -> tuple[float, int]:
    """
    Return the average and the number of values.
    """
    count: int = len(
        numbers
    )

    total: float = sum(
        numbers
    )

    average: float = (
        total
        / count
    )

    return (
        average,
        count,
    )


average: float
count: int

average, count = calculate_average(
    [
        10.0,
        20.0,
        30.0,
    ]
)

print(
    average
)

print(
    count
)

# The function returns:
#
# calculated result
#
# and:
#
# useful metadata about the calculation.
#
# This is a common practical use of multiple return values.
#
# =============================================================================


# =============================================================================
# 60. Multiple Return Values And Empty Input
# =============================================================================

def calculate_average_safely(
    numbers: list[float],
) -> tuple[float | None, bool]:
    """
    Return the average and whether calculation was possible.
    """
    if not numbers:
        return (
            None,
            False,
        )

    average: float = (
        sum(numbers)
        / len(numbers)
    )

    return (
        average,
        True,
    )


safe_average: float | None
average_available: bool

safe_average, average_available = (
    calculate_average_safely(
        []
    )
)

print(
    safe_average
)

print(
    average_available
)

# Returning multiple values can allow a function to represent both:
#
# result
#
# and:
#
# whether the result is meaningful.
#
# =============================================================================


# =============================================================================
# 61. Returning A Tuple From A Conditional Expression
# =============================================================================

def get_coordinates_by_status(
    valid: bool,
) -> tuple[int, int]:
    """
    Return one of two coordinate pairs.
    """
    if valid:
        return (
            10,
            20,
        )

    return (
        0,
        0,
    )


valid_coordinates: tuple[int, int] = (
    get_coordinates_by_status(
        True
    )
)

print(
    valid_coordinates
)

# Both branches return:
#
# tuple[int, int]
#
# This keeps the function's output predictable.
#
# =============================================================================


# =============================================================================
# 62. Multiple Return Values And Scope
# =============================================================================

def calculate_values() -> tuple[int, int]:
    """
    Return locally calculated values.
    """
    first: int = 10
    second: int = 20

    return (
        first,
        second,
    )


first_calculated: int
second_calculated: int

first_calculated, second_calculated = calculate_values()

print(
    first_calculated
)

print(
    second_calculated
)

# Local variables:
#
# first
#
# and:
#
# second
#
# belong to the function.
#
# Their values are placed into the returned tuple.
#
# The caller receives the values through the tuple.
#
# The local variable names themselves are not returned.
#
# =============================================================================


# =============================================================================
# 63. Returning Values Does Not Return Local Variable Names
# =============================================================================

def get_local_data() -> tuple[int, int]:
    """
    Return values stored in local variables.
    """
    internal_width: int = 100
    internal_height: int = 200

    return (
        internal_width,
        internal_height,
    )


width_value: int
height_value: int

width_value, height_value = get_local_data()

print(
    width_value
)

print(
    height_value
)

# The caller does not receive:
#
# internal_width
#
# or:
#
# internal_height
#
# Those names disappear with the function's local scope.
#
# The caller receives their values through the returned tuple.
#
# =============================================================================


# =============================================================================
# 64. Multiple Return Values And Assignment Order
# =============================================================================

def get_ordered_values() -> tuple[str, str, str]:
    """
    Return values in a specific order.
    """
    return (
        "first",
        "second",
        "third",
    )


first_text: str
second_text: str
third_text: str

first_text, second_text, third_text = (
    get_ordered_values()
)

print(
    first_text
)

print(
    second_text
)

print(
    third_text
)

# Unpacking is positional.
#
# Position 1 goes to target 1.
#
# Position 2 goes to target 2.
#
# Position 3 goes to target 3.
#
# The names of the variables do not affect the mapping.
#
# =============================================================================


# =============================================================================
# 65. Reordering Values During Unpacking
# =============================================================================

def get_coordinates_for_reordering() -> tuple[int, int]:
    """
    Return x and y coordinates.
    """
    return (
        100,
        200,
    )


x_coordinate: int
y_coordinate: int

x_coordinate, y_coordinate = (
    get_coordinates_for_reordering()
)

print(
    x_coordinate
)

print(
    y_coordinate
)

# If the caller wants a different arrangement, the caller can explicitly
# assign the returned positions to different variable names.
#
# For example:
#
# second, first = get_coordinates_for_reordering()
#
# would assign:
#
# second = 100
#
# first = 200
#
# The tuple itself remains unchanged.
#
# =============================================================================


# =============================================================================
# 66. Swapping Values Uses Tuple Unpacking
# =============================================================================

first_number_to_swap: int = 10
second_number_to_swap: int = 20

(
    first_number_to_swap,
    second_number_to_swap,
) = (
    second_number_to_swap,
    first_number_to_swap,
)

print(
    first_number_to_swap
)

print(
    second_number_to_swap
)

# Tuple packing and unpacking are also used by Python for swapping values.
#
# Conceptually:
#
# right side:
#
# (20, 10)
#
# is created first.
#
# Then it is unpacked into:
#
# first_number_to_swap
#
# and:
#
# second_number_to_swap
#
# This is related to multiple return value unpacking because both rely on
# tuple packing and unpacking.
#
# =============================================================================


# =============================================================================
# 67. Multiple Return Values And Function Composition
# =============================================================================

def get_pair_for_composition() -> tuple[int, int]:
    """
    Return two numbers.
    """
    return (
        10,
        20,
    )


def multiply_pair(
    first: int,
    second: int,
) -> int:
    """
    Multiply two numbers.
    """
    return (
        first
        * second
    )


first_composition: int
second_composition: int

(
    first_composition,
    second_composition,
) = get_pair_for_composition()

composition_result: int = multiply_pair(
    first_composition,
    second_composition,
)

print(
    composition_result
)

# Multiple returned values can become inputs to later operations.
#
# The returned tuple acts as a small package of related results.
#
# =============================================================================


# =============================================================================
# 68. Multiple Return Values And *args
# =============================================================================

def sum_values(
    *numbers: int,
) -> int:
    """
    Return the sum of all supplied numbers.
    """
    return sum(
        numbers
    )


def get_values_for_sum() -> tuple[int, int, int]:
    """
    Return values that can be passed to *args.
    """
    return (
        10,
        20,
        30,
    )


sum_result: int = sum_values(
    *get_values_for_sum()
)

print(
    sum_result
)

# get_values_for_sum()
#
# returns:
#
# (10, 20, 30)
#
# The * operator expands the tuple into positional arguments.
#
# sum_values(
#     10,
#     20,
#     30,
# )
#
# =============================================================================


# =============================================================================
# 69. Multiple Return Values And Keyword Arguments
# =============================================================================

def get_named_values() -> tuple[int, int]:
    """
    Return two values.
    """
    return (
        10,
        20,
    )


def calculate_total_named(
    first: int,
    second: int,
) -> int:
    """
    Return the total of two values.
    """
    return (
        first
        + second
    )


first_named: int
second_named: int

first_named, second_named = get_named_values()

named_total: int = calculate_total_named(
    first=first_named,
    second=second_named,
)

print(
    named_total
)

# The returned tuple itself is positional.
#
# After unpacking, the resulting variables can be passed as positional or
# keyword arguments.
#
# =============================================================================


# =============================================================================
# 70. Multiple Return Values And Strict Calling Conventions
# =============================================================================

def process_result(
    value: int,
    /,
    *,
    double: bool = False,
) -> tuple[int, bool]:
    """
    Return a processed value and whether doubling was applied.
    """
    if double:
        return (
            value * 2,
            True,
        )

    return (
        value,
        False,
    )


processed_value: int
was_doubled: bool

processed_value, was_doubled = process_result(
    10,
    double=True,
)

print(
    processed_value
)

print(
    was_doubled
)

# Input parameter rules:
#
# value
# ↓
# positional-only
#
# double
# ↓
# keyword-only
#
# Output:
#
# tuple[int, bool]
#
# Input argument rules and output return structure are separate concepts.
#
# =============================================================================


# =============================================================================
# 71. Multiple Return Values And Object Packing
# =============================================================================

def pack_values(
    name: str,
    age: int,
    active: bool,
) -> tuple[str, int, bool]:
    """
    Pack several values into one returned tuple.
    """
    return (
        name,
        age,
        active,
    )


packed_values: tuple[str, int, bool] = pack_values(
    "Alex",
    30,
    True,
)

print(
    packed_values
)

# The return statement performs tuple packing:
#
# name, age, active
#
# becomes:
#
# (name, age, active)
#
# before it is returned.
#
# =============================================================================


# =============================================================================
# 72. Packing And Unpacking Together
# =============================================================================

def pack_user() -> tuple[str, int]:
    """
    Pack user data into a tuple.
    """
    return (
        "Alex",
        30,
    )


user_name_value: str
user_age_value: int

user_name_value, user_age_value = pack_user()

print(
    user_name_value
)

print(
    user_age_value
)

# Function return:
#
# packing
# ↓
# ("Alex", 30)
#
# Assignment:
#
# unpacking
# ↓
# user_name_value = "Alex"
# user_age_value = 30
#
# This is the core mechanism behind multiple return values.
#
# =============================================================================


# =============================================================================
# 73. Multiple Return Values Are A Convenience Feature
# =============================================================================

def get_dimensions_for_convenience() -> tuple[int, int]:
    """
    Return two dimensions.
    """
    return (
        100,
        200,
    )


dimensions_tuple: tuple[int, int] = (
    get_dimensions_for_convenience()
)

print(
    dimensions_tuple
)

# Python's multiple return syntax is convenient because:
#
# return width, height
#
# is shorter than:
#
# result = (width, height)
# return result
#
# But both ultimately return one tuple object.
#
# =============================================================================


# =============================================================================
# 74. Multiple Return Values And Temporary Variables
# =============================================================================

def calculate_metrics(
    value: float,
) -> tuple[float, float]:
    """
    Return two metrics calculated from one value.
    """
    doubled: float = (
        value
        * 2
    )

    squared: float = (
        value
        ** 2
    )

    return (
        doubled,
        squared,
    )


doubled_value: float
squared_value: float

doubled_value, squared_value = calculate_metrics(
    5.0
)

print(
    doubled_value
)

print(
    squared_value
)

# Temporary local variables make the meaning of each returned value clear.
#
# The return tuple then packages those values together.
#
# =============================================================================


# =============================================================================
# 75. Multiple Return Values And Documentation
# =============================================================================

def get_server_configuration() -> tuple[str, int, bool]:
    """
    Return the server host, port, and debug state.

    Returns:
        tuple[str, int, bool]:
            The host, port, and debug state in that order.
    """
    return (
        "localhost",
        8080,
        True,
    )


server_host: str
server_port: int
server_debug: bool

server_host, server_port, server_debug = (
    get_server_configuration()
)

print(
    server_host
)

print(
    server_port
)

print(
    server_debug
)

# When returning several positional values, documenting their order can make
# the function easier to understand.
#
# =============================================================================


# =============================================================================
# 76. Returning Multiple Values With A NamedTuple
# =============================================================================

class CalculationResult(NamedTuple):
    """
    Represent a calculation result.
    """
    total: float
    average: float


def calculate_result(
    first: float,
    second: float,
) -> CalculationResult:
    """
    Return named calculation results.
    """
    total: float = (
        first
        + second
    )

    average: float = (
        total
        / 2
    )

    return CalculationResult(
        total=total,
        average=average,
    )


calculation_result: CalculationResult = (
    calculate_result(
        10.0,
        20.0,
    )
)

print(
    calculation_result.total
)

print(
    calculation_result.average
)

# This demonstrates an alternative when positional tuple fields become
# difficult to understand.
#
# A NamedTuple retains tuple behaviour while providing named attributes.
#
# =============================================================================


# =============================================================================
# 77. Multiple Return Values Versus A Custom Object
# =============================================================================

class ProductResult:
    """
    Represent product calculation results.
    """

    def __init__(
        self,
        subtotal: float,
        total: float,
    ) -> None:
        self.subtotal: float = subtotal
        self.total: float = total


def calculate_product(
    price: float,
    quantity: int,
) -> ProductResult:
    """
    Return a custom result object.
    """
    subtotal: float = (
        price
        * quantity
    )

    total: float = (
        subtotal
        * 1.18
    )

    return ProductResult(
        subtotal,
        total,
    )


product_result: ProductResult = calculate_product(
    100.0,
    2,
)

print(
    product_result.subtotal
)

print(
    product_result.total
)

# Multiple return values are not always the best design.
#
# If many values need meaningful names, a custom class, dataclass,
# NamedTuple, or dictionary can sometimes be clearer.
#
# The choice depends on the structure and purpose of the result.
#
# =============================================================================


# =============================================================================
# 78. Returning Multiple Values From A Generator-Like Pattern
# =============================================================================

def get_pairs() -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Return two coordinate pairs.
    """
    first_pair: tuple[int, int] = (
        10,
        20,
    )

    second_pair: tuple[int, int] = (
        30,
        40,
    )

    return (
        first_pair,
        second_pair,
    )


first_coordinate_pair: tuple[int, int]
second_coordinate_pair: tuple[int, int]

first_coordinate_pair, second_coordinate_pair = (
    get_pairs()
)

print(
    first_coordinate_pair
)

print(
    second_coordinate_pair
)

# This is still one returned tuple.
#
# Its elements happen to be tuples themselves.
#
# =============================================================================


# =============================================================================
# 79. Multiple Return Values And Function Contracts
# =============================================================================

def get_application_state() -> tuple[str, bool, int]:
    """
    Return application state.

    The return structure is:

    (
        application_name,
        running,
        process_count,
    )
    """
    return (
        "DataPipeline",
        True,
        4,
    )


application_name: str
application_running: bool
process_count: int

application_name, application_running, process_count = (
    get_application_state()
)

print(
    application_name
)

print(
    application_running
)

print(
    process_count
)

# A multiple-value return creates a small positional contract.
#
# The caller needs to know:
#
# position 1 -> application name
#
# position 2 -> running state
#
# position 3 -> process count
#
# As the number of returned values increases, named structures can become
# easier to maintain.
#
# =============================================================================


# =============================================================================
# 80. Multiple Return Values And Readability
# =============================================================================

def get_dimensions_readable() -> tuple[int, int]:
    """
    Return width and height.
    """
    width: int = 1920
    height: int = 1080

    return (
        width,
        height,
    )


screen_width: int
screen_height: int

screen_width, screen_height = (
    get_dimensions_readable()
)

print(
    screen_width
)

print(
    screen_height
)

# Meaningful variable names at the call site can make tuple unpacking very
# readable.
#
# Compare:
#
# a, b = get_dimensions()
#
# with:
#
# screen_width, screen_height = get_dimensions()
#
# The second form communicates the meaning of each returned position.
#
# =============================================================================


# =============================================================================
# 81. Common Mistake: Assuming The Caller Receives Separate Return Objects
# =============================================================================

def return_pair_for_model() -> tuple[int, int]:
    """
    Return a pair of values.
    """
    return (
        10,
        20,
    )


pair: tuple[int, int] = return_pair_for_model()

print(
    pair
)

# The function returns:
#
# one object
#
# whose value is:
#
# (10, 20)
#
# It is then possible to unpack that object into:
#
# first
#
# and:
#
# second
#
# Multiple return values are therefore best understood as:
#
# tuple packing
#       ↓
# tuple returned
#       ↓
# optional tuple unpacking
#
# =============================================================================


# =============================================================================
# 82. Common Mistake: Confusing Return Unpacking With Function Arguments
# =============================================================================

def create_pair() -> tuple[int, int]:
    """
    Return a pair.
    """
    return (
        10,
        20,
    )


def consume_pair(
    first: int,
    second: int,
) -> int:
    """
    Consume two positional arguments.
    """
    return (
        first
        + second
    )


pair_result: tuple[int, int] = create_pair()

sum_result_82: int = consume_pair(
    *pair_result
)

print(
    sum_result
)

# These are two separate operations:
#
# create_pair()
# ↓
# returns one tuple
#
# *pair_result
# ↓
# unpacks the tuple into arguments
#
# consume_pair(
#     10,
#     20,
# )
#
# Therefore returning multiple values and passing multiple arguments are
# related through tuple unpacking, but they are not the same operation.
#
# =============================================================================


# =============================================================================
# 83. Multiple Return Values And Optional Values
# =============================================================================

def get_configuration(
    enabled: bool,
) -> tuple[str, int | None]:
    """
    Return configuration name and optional timeout.
    """
    if enabled:
        return (
            "production",
            60,
        )

    return (
        "disabled",
        None,
    )


configuration_name: str
configuration_timeout: int | None

configuration_name, configuration_timeout = (
    get_configuration(
        True
    )
)

print(
    configuration_name
)

print(
    configuration_timeout
)

# Individual positions can have union types.
#
# Here:
#
# first position:
# str
#
# second position:
# int | None
#
# The tuple annotation describes each position independently.
#
# =============================================================================


# =============================================================================
# 84. Multiple Return Values And Type Safety
# =============================================================================

def get_typed_result() -> tuple[str, int]:
    """
    Return a strongly typed pair.
    """
    return (
        "completed",
        200,
    )


typed_status: str
typed_code: int

typed_status, typed_code = get_typed_result()

print(
    typed_status
)

print(
    typed_code
)

# Type annotations help communicate the expected structure.
#
# tuple[str, int]
#
# tells the reader and static type checker:
#
# position 1 -> str
#
# position 2 -> int
#
# This makes multiple return values more predictable.
#
# =============================================================================


# =============================================================================
# 85. Multiple Return Values And Intentional Ignoring
# =============================================================================

def get_status_and_message() -> tuple[int, str]:
    """
    Return a status code and message.
    """
    return (
        200,
        "Success",
    )


status: int
_ignored_message: str

status, _ignored_message = get_status_and_message()

print(
    status
)

# If only one returned value matters, the other can be intentionally ignored.
#
# A common convention is:
#
# status, _ = get_status_and_message()
#
# This communicates:
#
# "The second returned value is intentionally not being used."
#
# =============================================================================


# =============================================================================
# 86. Extended Unpacking And Ignoring A Middle Section
# =============================================================================

def get_sequence() -> tuple[int, int, int, int, int]:
    """
    Return a sequence of numbers.
    """
    return (
        10,
        20,
        30,
        40,
        50,
    )


first_sequence_value: int
middle_sequence_values: list[int]
last_sequence_value: int

(
    first_sequence_value,
    *middle_sequence_values,
    last_sequence_value,
) = get_sequence()

print(
    first_sequence_value
)

print(
    middle_sequence_values
)

print(
    last_sequence_value
)

# Extended unpacking is useful when the number of middle values is not
# important.
#
# =============================================================================


# =============================================================================
# 87. Multiple Return Values And Tuple Indexing
# =============================================================================

def get_indexed_values() -> tuple[str, int, bool]:
    """
    Return values that can be accessed by index.
    """
    return (
        "Alex",
        30,
        True,
    )


indexed_result: tuple[str, int, bool] = (
    get_indexed_values()
)

print(
    indexed_result[0]
)

print(
    indexed_result[1]
)

print(
    indexed_result[2]
)

# A returned tuple can be accessed directly by index.
#
# position 0:
# "Alex"
#
# position 1:
# 30
#
# position 2:
# True
#
# However, unpacking can often make the meaning clearer:
#
# name, age, active = get_indexed_values()
#
# =============================================================================


# =============================================================================
# 88. Multiple Return Values And Slicing
# =============================================================================

def get_numbers_for_slicing() -> tuple[int, int, int, int]:
    """
    Return four numbers.
    """
    return (
        10,
        20,
        30,
        40,
    )


numbers_for_slicing: tuple[int, int, int, int] = (
    get_numbers_for_slicing()
)

first_two_numbers: tuple[int, int] = (
    numbers_for_slicing[:2]
)

print(
    first_two_numbers
)

# Because the return value is a tuple, normal tuple operations are available.
#
# Multiple return values therefore produce a normal tuple object with all
# normal tuple behaviour.
#
# =============================================================================


# =============================================================================
# 89. Returning A Tuple Does Not Make Its Elements Immutable
# =============================================================================

def get_mutable_result() -> tuple[list[int], list[int]]:
    """
    Return two mutable lists inside a tuple.
    """
    return (
        [
            1,
            2,
        ],
        [
            3,
            4,
        ],
    )


mutable_result: tuple[list[int], list[int]] = (
    get_mutable_result()
)

mutable_result[0].append(
    5
)

print(
    mutable_result
)

# The tuple structure itself cannot have its elements replaced:
#
# mutable_result[0] = [...]
#
# would raise TypeError.
#
# But the list object at position 0 can be mutated:
#
# mutable_result[0].append(5)
#
# This distinction is important when returning mutable objects.
#
# =============================================================================


# =============================================================================
# 90. Multiple Return Values Core Model
# =============================================================================

"""
Multiple return values:
"""