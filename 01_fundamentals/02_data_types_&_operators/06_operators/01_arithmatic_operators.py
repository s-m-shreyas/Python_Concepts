# =============================================================================
# 01. Arithmetic Operators
# =============================================================================
# type: ignore
"""
Python Operators

File:
01_arithmetic_operators.py

Topic:
Arithmetic Operators

Overview:
Arithmetic operators are used to perform mathematical calculations.

Python provides the following arithmetic operators:

    +     Addition
    -     Subtraction
    *     Multiplication
    /     True division
    //    Floor division
    %     Modulo
    **    Exponentiation

Arithmetic operators can be used with:

    - integers
    - floating-point numbers
    - complex numbers
    - numeric variables
    - expressions

This file demonstrates arithmetic operators from basic usage to
practical examples.
"""

# =============================================================================
# 01. Addition Operator (+)
# =============================================================================

"""
The addition operator:

    +

adds two values together.

Example:

    10 + 5

produces:

    15
"""

first_number: int = 10
second_number: int = 5

addition_result: int = first_number + second_number

print(addition_result)

# Output:
#
# 15


# =============================================================================
# 02. Addition With Integer Literals
# =============================================================================

addition_literal_result: int = 20 + 30

print(addition_literal_result)

# Output:
#
# 50


# =============================================================================
# 03. Addition With Floating-Point Numbers
# =============================================================================

first_price: float = 10.5
second_price: float = 5.25

total_price: float = first_price + second_price

print(total_price)

# Output:
#
# 15.75


# =============================================================================
# 04. Addition With Negative Numbers
# =============================================================================

positive_number: int = 10
negative_number: int = -3

addition_with_negative: int = positive_number + negative_number

print(addition_with_negative)

# Output:
#
# 7


# =============================================================================
# 05. Addition With Multiple Values
# =============================================================================

number_a: int = 10
number_b: int = 20
number_c: int = 30

multiple_addition: int = (
    number_a
    + number_b
    + number_c
)

print(multiple_addition)

# Output:
#
# 60


# =============================================================================
# 06. Addition With Strings
# =============================================================================

"""
The + operator can also concatenate strings.

For strings:

    "Hello" + "World"

produces:

    "HelloWorld"
"""

first_name: str = "Python"
last_name: str = "Developer"

full_name: str = (
    first_name
    + " "
    + last_name
)

print(full_name)

# Output:
#
# Python Developer


# =============================================================================
# 07. Addition With Lists
# =============================================================================

"""
The + operator can concatenate lists.

Example:

    [1, 2] + [3, 4]

produces:

    [1, 2, 3, 4]
"""

first_list: list[int] = [
    1,
    2,
]

second_list: list[int] = [
    3,
    4,
]

combined_list: list[int] = (
    first_list
    + second_list
)

print(combined_list)

# Output:
#
# [1, 2, 3, 4]


# =============================================================================
# 08. Subtraction Operator (-)
# =============================================================================

"""
The subtraction operator:

    -

subtracts the right-hand value from the left-hand value.

Example:

    10 - 5

produces:

    5
"""

total_amount: int = 100
spent_amount: int = 35

remaining_amount: int = (
    total_amount
    - spent_amount
)

print(remaining_amount)

# Output:
#
# 65


# =============================================================================
# 09. Subtraction With Floating-Point Numbers
# =============================================================================

original_price: float = 99.99
discount_amount: float = 15.50

discounted_amount: float = (
    original_price
    - discount_amount
)

print(discounted_amount)

# Output:
#
# 84.49


# =============================================================================
# 10. Subtraction Resulting In A Negative Number
# =============================================================================

available_balance: int = 50
withdrawal_amount: int = 75

balance_after_withdrawal: int = (
    available_balance
    - withdrawal_amount
)

print(balance_after_withdrawal)

# Output:
#
# -25


# =============================================================================
# 11. Multiplication Operator (*)
# =============================================================================

"""
The multiplication operator:

    *

multiplies two values.

Example:

    10 * 5

produces:

    50
"""

quantity: int = 5
unit_price: int = 20

purchase_total: int = (
    quantity
    * unit_price
)

print(purchase_total)

# Output:
#
# 100


# =============================================================================
# 12. Multiplication With Floating-Point Numbers
# =============================================================================

hourly_rate: float = 25.50
hours_worked: float = 8.0

daily_income: float = (
    hourly_rate
    * hours_worked
)

print(daily_income)

# Output:
#
# 204.0


# =============================================================================
# 13. Multiplication By Zero
# =============================================================================

number: int = 100

zero_result: int = number * 0

print(zero_result)

# Output:
#
# 0


# =============================================================================
# 14. Multiplication By One
# =============================================================================

number_to_preserve: int = 100

same_number: int = number_to_preserve * 1

print(same_number)

# Output:
#
# 100


# =============================================================================
# 15. String Repetition With (*)
# =============================================================================

"""
The * operator can repeat strings.

Example:

    "Python" * 3

produces:

    "PythonPythonPython"
"""

word: str = "Python"

repeated_word: str = word * 3

print(repeated_word)

# Output:
#
# PythonPythonPython


# =============================================================================
# 16. List Repetition With (*)
# =============================================================================

values: list[int] = [
    1,
    2,
]

repeated_values: list[int] = values * 3

print(repeated_values)

# Output:
#
# [1, 2, 1, 2, 1, 2]


# =============================================================================
# 17. Division Operator (/)
# =============================================================================

"""
The division operator:

    /

performs true division.

The result of / is always a float.

Example:

    10 / 2

produces:

    5.0
"""

dividend: int = 10
divisor: int = 2

division_result: float = (
    dividend
    / divisor
)

print(division_result)

# Output:
#
# 5.0


# =============================================================================
# 18. Division Produces A Float
# =============================================================================

division_value: float = 20 / 4

print(division_value)

# Output:
#
# 5.0


# =============================================================================
# 19. Division With A Remainder
# =============================================================================

division_with_remainder: float = 10 / 3

print(division_with_remainder)

# Output:
#
# 3.3333333333333335


# =============================================================================
# 20. Division By One
# =============================================================================

number_to_divide: float = 100.0

division_by_one: float = number_to_divide / 1

print(division_by_one)

# Output:
#
# 100.0


# =============================================================================
# 21. Division By Zero
# =============================================================================

"""
Division by zero is not allowed.

The following code would raise:

    ZeroDivisionError

It is intentionally kept inside a comment so this complete file can
execute successfully.

Example:

    result = 10 / 0

Do not execute that expression unless you are specifically demonstrating
exception handling.
"""


# =============================================================================
# 22. Floor Division Operator (//)
# =============================================================================

"""
The floor division operator:

    //

divides two values and returns the floor of the result.

Example:

    10 // 3

produces:

    3

Unlike /, floor division does not return the fractional part.
"""

floor_division_result: int = 10 // 3

print(floor_division_result)

# Output:
#
# 3


# =============================================================================
# 23. Floor Division With Exact Division
# =============================================================================

exact_floor_division: int = 20 // 5

print(exact_floor_division)

# Output:
#
# 4


# =============================================================================
# 24. Floor Division With Floating-Point Values
# =============================================================================

floating_floor_division: float = 10.0 // 3.0

print(floating_floor_division)

# Output:
#
# 3.0


# =============================================================================
# 25. Floor Division And Negative Numbers
# =============================================================================

"""
Floor division rounds toward negative infinity.

Therefore:

    -10 // 3

produces:

    -4

It does not simply truncate toward zero.
"""

negative_floor_division: int = -10 // 3

print(negative_floor_division)

# Output:
#
# -4


# =============================================================================
# 26. Difference Between / And //
# =============================================================================

dividend_value: int = 17
divisor_value: int = 5

true_division: float = (
    dividend_value
    / divisor_value
)

floor_division: int = (
    dividend_value
    // divisor_value
)

print(true_division)
print(floor_division)

# Output:
#
# 3.4
# 3


# =============================================================================
# 27. Modulo Operator (%)
# =============================================================================

"""
The modulo operator:

    %

returns the remainder after division.

Example:

    10 % 3

produces:

    1

because:

    10 = (3 * 3) + 1
"""

modulo_result: int = 10 % 3

print(modulo_result)

# Output:
#
# 1


# =============================================================================
# 28. Modulo With Exact Division
# =============================================================================

exact_modulo: int = 20 % 5

print(exact_modulo)

# Output:
#
# 0


# =============================================================================
# 29. Checking Whether A Number Is Even
# =============================================================================

even_number: int = 24

even_remainder: int = even_number % 2

print(even_remainder)

# Output:
#
# 0


# =============================================================================
# 30. Checking Whether A Number Is Odd
# =============================================================================

odd_number: int = 25

odd_remainder: int = odd_number % 2

print(odd_remainder)

# Output:
#
# 1


# =============================================================================
# 31. Practical Even Number Check
# =============================================================================

number_to_check: int = 42

is_even: bool = (
    number_to_check % 2 == 0
)

print(is_even)

# Output:
#
# True


# =============================================================================
# 32. Practical Odd Number Check
# =============================================================================

number_to_check_odd: int = 43

is_odd: bool = (
    number_to_check_odd % 2 != 0
)

print(is_odd)

# Output:
#
# True


# =============================================================================
# 33. Modulo With Larger Numbers
# =============================================================================

large_number: int = 157
modulo_base: int = 10

last_digit: int = (
    large_number
    % modulo_base
)

print(last_digit)

# Output:
#
# 7


# =============================================================================
# 34. Modulo For Cyclic Values
# =============================================================================

"""
Modulo is useful when values repeat in cycles.

For example, a clock has 24 hours.

The expression:

    27 % 24

produces:

    3
"""

hour_value: int = 27
hours_in_day: int = 24

normalized_hour: int = (
    hour_value
    % hours_in_day
)

print(normalized_hour)

# Output:
#
# 3


# =============================================================================
# 35. Exponentiation Operator (**)
# =============================================================================

"""
The exponentiation operator:

    **

raises the left-hand value to the power of the right-hand value.

Example:

    2 ** 3

produces:

    8
"""

base: int = 2
exponent: int = 3

power_result: int = (
    base
    ** exponent
)

print(power_result)

# Output:
#
# 8


# =============================================================================
# 36. Squaring A Number
# =============================================================================

number_to_square: int = 5

square_result: int = (
    number_to_square
    ** 2
)

print(square_result)

# Output:
#
# 25


# =============================================================================
# 37. Cubing A Number
# =============================================================================

number_to_cube: int = 4

cube_result: int = (
    number_to_cube
    ** 3
)

print(cube_result)

# Output:
#
# 64


# =============================================================================
# 38. Exponentiation With Floating-Point Numbers
# =============================================================================

decimal_base: float = 2.5
decimal_exponent: float = 2.0

decimal_power: float = (
    decimal_base
    ** decimal_exponent
)

print(decimal_power)

# Output:
#
# 6.25


# =============================================================================
# 39. Exponentiation With Zero
# =============================================================================

zero_exponent_result: int = 100 ** 0

print(zero_exponent_result)

# Output:
#
# 1


# =============================================================================
# 40. Exponentiation With One
# =============================================================================

one_exponent_result: int = 100 ** 1

print(one_exponent_result)

# Output:
#
# 100


# =============================================================================
# 41. Negative Exponents
# =============================================================================

"""
A negative exponent produces a reciprocal.

Example:

    2 ** -1

produces:

    0.5
"""

negative_exponent_result: float = 2 ** -1

print(negative_exponent_result)

# Output:
#
# 0.5


# =============================================================================
# 42. Arithmetic Operators Together
# =============================================================================

"""
Arithmetic operators can be combined in a single expression.

Example:

    10 + 5 * 2

The multiplication is performed before the addition.
"""

combined_expression: int = (
    10
    + 5 * 2
)

print(combined_expression)

# Output:
#
# 20


# =============================================================================
# 43. Parentheses Change Evaluation Order
# =============================================================================

expression_without_parentheses: int = (
    10
    + 5 * 2
)

expression_with_parentheses: int = (
    (10 + 5)
    * 2
)

print(expression_without_parentheses)
print(expression_with_parentheses)

# Output:
#
# 20
# 30


# =============================================================================
# 44. Arithmetic Expression With Multiple Operators
# =============================================================================

arithmetic_expression: float = (
    100
    + 50
    - 20
    * 2
    / 5
)

print(arithmetic_expression)

# Output:
#
# 142.0


# =============================================================================
# 45. Parentheses For Readability
# =============================================================================

price: float = 100.0
quantity: int = 3
discount: float = 20.0

subtotal: float = (
    price
    * quantity
)

discounted_total: float = (
    subtotal
    - discount
)

print(discounted_total)

# Output:
#
# 280.0


# =============================================================================
# 46. Arithmetic With Variables
# =============================================================================

length: float = 10.0
width: float = 5.0

rectangle_area: float = (
    length
    * width
)

print(rectangle_area)

# Output:
#
# 50.0


# =============================================================================
# 47. Rectangle Perimeter
# =============================================================================

rectangle_length: float = 10.0
rectangle_width: float = 5.0

rectangle_perimeter: float = (
    2
    * (
        rectangle_length
        + rectangle_width
    )
)

print(rectangle_perimeter)

# Output:
#
# 30.0


# =============================================================================
# 48. Circle Area
# =============================================================================

"""
The area of a circle is:

    pi * radius ** 2
"""

import math

radius: float = 5.0

circle_area: float = (
    math.pi
    * radius
    ** 2
)

print(circle_area)


# =============================================================================
# 49. Circle Circumference
# =============================================================================

circle_radius: float = 5.0

circle_circumference: float = (
    2
    * math.pi
    * circle_radius
)

print(circle_circumference)


# =============================================================================
# 50. Average Calculation
# =============================================================================

score_one: float = 80.0
score_two: float = 90.0
score_three: float = 70.0

average_score: float = (
    score_one
    + score_two
    + score_three
) / 3

print(average_score)

# Output:
#
# 80.0


# =============================================================================
# 51. Percentage Calculation
# =============================================================================

obtained_marks: float = 450.0
total_marks: float = 500.0

percentage: float = (
    obtained_marks
    / total_marks
    * 100
)

print(percentage)

# Output:
#
# 90.0


# =============================================================================
# 52. Simple Interest Calculation
# =============================================================================

"""
Simple interest formula:

    SI = (P * R * T) / 100

where:

    P = principal
    R = annual interest rate
    T = time
"""

principal: float = 10_000.0
interest_rate: float = 5.0
time_years: float = 2.0

simple_interest: float = (
    principal
    * interest_rate
    * time_years
    / 100
)

print(simple_interest)

# Output:
#
# 1000.0


# =============================================================================
# 53. Total Amount Using Simple Interest
# =============================================================================

principal_amount: float = 10_000.0
interest_amount: float = 1_000.0

total_amount: float = (
    principal_amount
    + interest_amount
)

print(total_amount)

# Output:
#
# 11000.0


# =============================================================================
# 54. Unit Price Calculation
# =============================================================================

total_cost: float = 500.0
item_count: int = 10

unit_cost: float = (
    total_cost
    / item_count
)

print(unit_cost)

# Output:
#
# 50.0


# =============================================================================
# 55. Remaining Items
# =============================================================================

total_items: int = 100
processed_items: int = 65

remaining_items: int = (
    total_items
    - processed_items
)

print(remaining_items)

# Output:
#
# 35


# =============================================================================
# 56. Quotient And Remainder Together
# =============================================================================

total_items_for_groups: int = 17
group_size: int = 5

number_of_complete_groups: int = (
    total_items_for_groups
    // group_size
)

remaining_items_incomplete_group: int = (
    total_items_for_groups
    % group_size
)

print(number_of_complete_groups)
print(remaining_items_incomplete_group)

# Output:
#
# 3
# 2


# =============================================================================
# 57. Converting Seconds To Minutes
# =============================================================================

total_seconds: int = 367

minutes: int = (
    total_seconds
    // 60
)

remaining_seconds: int = (
    total_seconds
    % 60
)

print(minutes)
print(remaining_seconds)

# Output:
#
# 6
# 7


# =============================================================================
# 58. Converting Minutes To Hours
# =============================================================================

total_minutes: int = 135

hours: int = (
    total_minutes
    // 60
)

remaining_minutes: int = (
    total_minutes
    % 60
)

print(hours)
print(remaining_minutes)

# Output:
#
# 2
# 15


# =============================================================================
# 59. Converting Days To Weeks
# =============================================================================

total_days: int = 17

weeks: int = (
    total_days
    // 7
)

remaining_days: int = (
    total_days
    % 7
)

print(weeks)
print(remaining_days)

# Output:
#
# 2
# 3


# =============================================================================
# 60. Arithmetic Assignment
# =============================================================================

"""
Arithmetic operations can be combined with assignment operators.

Examples:

    +=
    -=
    *=
    /=
    //=
    %=
    **=

These are called augmented assignment operators.

They are closely related to arithmetic operators.
"""

counter: int = 10

counter += 5

print(counter)

# Output:
#
# 15


# =============================================================================
# 61. Addition Assignment (+=)
# =============================================================================

score: int = 100

score += 25

print(score)

# Output:
#
# 125


# =============================================================================
# 62. Subtraction Assignment (-=)
# =============================================================================

balance: int = 1000

balance -= 250

print(balance)

# Output:
#
# 750


# =============================================================================
# 63. Multiplication Assignment (*=)
# =============================================================================

quantity_value: int = 5

quantity_value *= 4

print(quantity_value)

# Output:
#
# 20


# =============================================================================
# 64. Division Assignment (/=)
# =============================================================================

division_value: float = 100.0

division_value /= 4

print(division_value)

# Output:
#
# 25.0


# =============================================================================
# 65. Floor Division Assignment (//=)
# =============================================================================

floor_value: int = 17

floor_value //= 5

print(floor_value)

# Output:
#
# 3


# =============================================================================
# 66. Modulo Assignment (%=)
# =============================================================================

remainder_value: int = 17

remainder_value %= 5

print(remainder_value)

# Output:
#
# 2


# =============================================================================
# 67. Exponentiation Assignment (**=)
# =============================================================================

power_value: int = 2

power_value **= 3

print(power_value)

# Output:
#
# 8


# =============================================================================
# 68. Arithmetic With Parentheses
# =============================================================================

"""
Parentheses can be used to explicitly control the order of arithmetic
operations.

Prefer parentheses when they make an expression easier to understand.
"""

base_price: float = 100.0
quantity_purchased: int = 3
tax_rate: float = 0.18

subtotal_value: float = (
    base_price
    * quantity_purchased
)

tax_amount: float = (
    subtotal_value
    * tax_rate
)

final_price: float = (
    subtotal_value
    + tax_amount
)

print(final_price)


# =============================================================================
# 69. Operator Precedence
# =============================================================================

"""
Python generally evaluates arithmetic operators according to precedence.

A simplified order is:

    1. Parentheses
    2. Exponentiation **
    3. Unary + and -
    4. Multiplication, division, floor division, modulo
    5. Addition and subtraction

Example:

    2 + 3 * 4

is evaluated as:

    2 + (3 * 4)

which produces:

    14
"""

precedence_result: int = (
    2
    + 3 * 4
)

print(precedence_result)

# Output:
#
# 14


# =============================================================================
# 70. Parentheses Override Precedence
# =============================================================================

precedence_with_parentheses: int = (
    (2 + 3)
    * 4
)

print(precedence_with_parentheses)

# Output:
#
# 20


# =============================================================================
# 71. Exponentiation Has Higher Precedence
# =============================================================================

power_precedence: int = (
    2
    + 3
    ** 2
)

print(power_precedence)

# Output:
#
# 11


# =============================================================================
# 72. Explicit Parentheses Improve Clarity
# =============================================================================

clear_power_expression: int = (
    2
    + (
        3
        ** 2
    )
)

print(clear_power_expression)

# Output:
#
# 11


# =============================================================================
# 73. Arithmetic With Boolean Values
# =============================================================================

"""
In Python, bool is a subclass of int.

Therefore:

    True  behaves numerically like 1
    False behaves numerically like 0

Example:

    True + True

produces:

    2

Although this is valid Python, explicit numeric values are generally
clearer when performing mathematical calculations.
"""

true_value: bool = True
false_value: bool = False

boolean_arithmetic_result: int = (
    int(true_value)
    + int(false_value)
)

print(boolean_arithmetic_result)

# Output:
#
# 1


# =============================================================================
# 74. Arithmetic With Complex Numbers
# =============================================================================

"""
Python supports complex numbers.

A complex number can be written as:

    a + bj

where:

    a = real part
    b = imaginary part
"""

first_complex: complex = 2 + 3j
second_complex: complex = 1 + 4j

complex_addition: complex = (
    first_complex
    + second_complex
)

complex_subtraction: complex = (
    first_complex
    - second_complex
)

complex_multiplication: complex = (
    first_complex
    * second_complex
)

print(complex_addition)
print(complex_subtraction)
print(complex_multiplication)


# =============================================================================
# 75. Complex Number Exponentiation
# =============================================================================

complex_number: complex = 2 + 1j

complex_power: complex = (
    complex_number
    ** 2
)

print(complex_power)


# =============================================================================
# 76. Arithmetic Functions
# =============================================================================

def add_numbers(
    first: int,
    second: int,
) -> int:
    """
    Return the sum of two integers.
    """
    return first + second


def subtract_numbers(
    first: int,
    second: int,
) -> int:
    """
    Return the difference between two integers.
    """
    return first - second


def multiply_numbers(
    first: int,
    second: int,
) -> int:
    """
    Return the product of two integers.
    """
    return first * second


def divide_numbers(
    first: float,
    second: float,
) -> float:
    """
    Return the true division result.
    """
    return first / second


addition_function_result: int = add_numbers(
    10,
    5,
)

subtraction_function_result: int = subtract_numbers(
    10,
    5,
)

multiplication_function_result: int = multiply_numbers(
    10,
    5,
)

division_function_result: float = divide_numbers(
    10.0,
    5.0,
)

print(addition_function_result)
print(subtraction_function_result)
print(multiplication_function_result)
print(division_function_result)


# =============================================================================
# 77. Arithmetic Function For Remainder
# =============================================================================

def get_remainder(
    dividend: int,
    divisor: int,
) -> int:
    """
    Return the remainder after division.
    """
    return dividend % divisor


remainder_result: int = get_remainder(
    17,
    5,
)

print(remainder_result)

# Output:
#
# 2


# =============================================================================
# 78. Arithmetic Function For Floor Division
# =============================================================================

def get_quotient(
    dividend: int,
    divisor: int,
) -> int:
    """
    Return the floor-division quotient.
    """
    return dividend // divisor


quotient_result: int = get_quotient(
    17,
    5,
)

print(quotient_result)

# Output:
#
# 3


# =============================================================================
# 79. Arithmetic Function For Power
# =============================================================================

def calculate_power(
    base_value: int,
    exponent_value: int,
) -> int:
    """
    Raise base_value to exponent_value.
    """
    return base_value ** exponent_value


power_function_result: int = calculate_power(
    2,
    5,
)

print(power_function_result)

# Output:
#
# 32


# =============================================================================
# 80. Arithmetic Operators In A Function
# =============================================================================

def calculate_rectangle(
    length_value: float,
    width_value: float,
) -> tuple[float, float]:
    """
    Return the area and perimeter of a rectangle.
    """
    area: float = (
        length_value
        * width_value
    )

    perimeter: float = (
        2
        * (
            length_value
            + width_value
        )
    )

    return area, perimeter


rectangle_area_result: float
rectangle_perimeter_result: float

(
    rectangle_area_result,
    rectangle_perimeter_result,
) = calculate_rectangle(
    10.0,
    5.0,
)

print(rectangle_area_result)
print(rectangle_perimeter_result)


# =============================================================================
# 81. Arithmetic Operators With User Input
# =============================================================================

"""
input() returns a string.

Therefore numeric input must be converted before performing arithmetic.

Example:

    first_input = int(input("Enter first number: "))

For this educational file, interactive input is kept as a function so
the main examples above remain deterministic.
"""


def calculate_from_input_values(
    first_value: float,
    second_value: float,
) -> tuple[float, float, float, float]:
    """
    Perform common arithmetic operations on two numbers.
    """
    addition: float = first_value + second_value
    subtraction: float = first_value - second_value
    multiplication: float = first_value * second_value
    division: float = first_value / second_value

    return (
        addition,
        subtraction,
        multiplication,
        division,
    )


(
    input_addition,
    input_subtraction,
    input_multiplication,
    input_division,
) = calculate_from_input_values(
    20.0,
    4.0,
)

print(input_addition)
print(input_subtraction)
print(input_multiplication)
print(input_division)


# =============================================================================
# 82. Temperature Conversion
# =============================================================================

"""
Celsius to Fahrenheit:

    F = (C * 9 / 5) + 32
"""

celsius: float = 25.0

fahrenheit: float = (
    celsius
    * 9
    / 5
    + 32
)

print(fahrenheit)

# Output:
#
# 77.0


# =============================================================================
# 83. Fahrenheit To Celsius
# =============================================================================

"""
Fahrenheit to Celsius:

    C = (F - 32) * 5 / 9
"""

fahrenheit_value: float = 77.0

celsius_value: float = (
    (
        fahrenheit_value
        - 32
    )
    * 5
    / 9
)

print(celsius_value)

# Output:
#
# 25.0


# =============================================================================
# 84. Distance Conversion
# =============================================================================

"""
Kilometers to meters:

    meters = kilometers * 1000
"""

kilometers: float = 5.5

meters: float = (
    kilometers
    * 1000
)

print(meters)

# Output:
#
# 5500.0


# =============================================================================
# 85. Compound Interest
# =============================================================================

"""
Compound interest formula:

    A = P * (1 + r / n) ** (n * t)

where:

    P = principal
    r = annual interest rate as a decimal
    n = number of compounding periods per year
    t = number of years
"""

compound_principal: float = 10_000.0
annual_rate: float = 0.05
compounds_per_year: int = 12
compound_years: float = 2.0

compound_amount: float = (
    compound_principal
    * (
        1
        + annual_rate
        / compounds_per_year
    )
    ** (
        compounds_per_year
        * compound_years
    )
)

print(compound_amount)


# =============================================================================
# 86. Arithmetic With Numeric Separators
# =============================================================================

"""
Underscores can improve readability of large numeric literals.

Example:

    1_000_000

has the same numeric value as:

    1000000
"""

population: int = 1_000_000
growth: int = 50_000

new_population: int = (
    population
    + growth
)

print(new_population)

# Output:
#
# 1050000


# =============================================================================
# 87. Floating-Point Arithmetic
# =============================================================================

"""
Floating-point calculations can sometimes produce small representation
differences because floating-point numbers are represented in binary.

For example:

    0.1 + 0.2

does not always display exactly as:

    0.3
"""

floating_result: float = (
    0.1
    + 0.2
)

print(floating_result)


# =============================================================================
# 88. Decimal Arithmetic
# =============================================================================

"""
For financial calculations where decimal precision matters, Python's
decimal.Decimal can be useful.

Decimal values should generally be constructed from strings rather than
from floating-point values.
"""

from decimal import Decimal

decimal_first: Decimal = Decimal("0.1")
decimal_second: Decimal = Decimal("0.2")

decimal_sum: Decimal = (
    decimal_first
    + decimal_second
)

print(decimal_sum)

# Output:
#
# 0.3


# =============================================================================
# 89. Arithmetic Comparison Example
# =============================================================================

"""
Arithmetic operators can be combined with comparison operators.

Example:

    remainder == 0

can be used to determine whether a number divides evenly.
"""

dividend_for_check: int = 20
divisor_for_check: int = 5

divides_evenly: bool = (
    dividend_for_check
    % divisor_for_check
    == 0
)

print(divides_evenly)

# Output:
#
# True


# =============================================================================
# 90. Arithmetic Operators In Conditional Logic
# =============================================================================

age: int = 21

is_adult: bool = age >= 18

print(is_adult)

# Output:
#
# True


# =============================================================================
# 91. Arithmetic Expression With Multiple Variables
# =============================================================================

base_salary: float = 50_000.0
bonus: float = 5_000.0
tax_rate: float = 0.10

gross_income: float = (
    base_salary
    + bonus
)

tax_amount_for_income: float = (
    gross_income
    * tax_rate
)

net_income: float = (
    gross_income
    - tax_amount_for_income
)

print(gross_income)
print(tax_amount_for_income)
print(net_income)


# =============================================================================
# 92. Arithmetic With Negative Values
# =============================================================================

temperature_change: float = -5.0
current_temperature: float = 20.0

new_temperature: float = (
    current_temperature
    + temperature_change
)

print(new_temperature)

# Output:
#
# 15.0


# =============================================================================
# 93. Absolute Difference
# =============================================================================

first_value: float = 100.0
second_value: float = 135.0

difference: float = (
    first_value
    - second_value
)

absolute_difference: float = abs(
    difference
)

print(absolute_difference)

# Output:
#
# 35.0


# =============================================================================
# 94. Arithmetic With round()
# =============================================================================

"""
round() is a built-in function rather than an arithmetic operator.

It is commonly used together with arithmetic calculations.
"""

raw_price: float = 19.98765

rounded_price: float = round(
    raw_price,
    2,
)

print(rounded_price)

# Output:
#
# 19.99


# =============================================================================
# 95. Arithmetic With min() And max()
# =============================================================================

"""
min() and max() are built-in functions, not arithmetic operators.

They can nevertheless be useful when working with calculated values.
"""

first_score: int = 80
second_score: int = 95
third_score: int = 75

lowest_score: int = min(
    first_score,
    second_score,
    third_score,
)

highest_score: int = max(
    first_score,
    second_score,
    third_score,
)

print(lowest_score)
print(highest_score)

# Output:
#
# 75
# 95


# =============================================================================
# 96. Arithmetic Operator Summary
# =============================================================================

"""
Arithmetic operators:

    +       Addition

    -       Subtraction

    *       Multiplication

    /       True division

    //      Floor division

    %       Modulo / remainder

    **      Exponentiation


Examples:

    10 + 5
        -> 15

    10 - 5
        -> 5

    10 * 5
        -> 50

    10 / 5
        -> 2.0

    10 // 3
        -> 3

    10 % 3
        -> 1

    2 ** 3
        -> 8
"""


# =============================================================================
# 97. Arithmetic Operator Quick Reference
# =============================================================================

"""
+   Addition

    10 + 5
    15


-   Subtraction

    10 - 5
    5


*   Multiplication

    10 * 5
    50


/   True division

    10 / 5
    2.0


//  Floor division

    10 // 3
    3


%   Modulo

    10 % 3
    1


**  Exponentiation

    2 ** 3
    8
"""


# =============================================================================
# 98. Arithmetic Operator Rules
# =============================================================================

"""
Important rules:

1. + performs addition for numeric values.

2. + can concatenate compatible sequences such as strings and lists.

3. - performs subtraction.

4. * performs multiplication.

5. * can repeat strings and lists.

6. / performs true division and produces a float.

7. Division by zero raises ZeroDivisionError.

8. // performs floor division.

9. Floor division rounds toward negative infinity.

10. % returns the remainder.

11. ** performs exponentiation.

12. Parentheses can be used to control evaluation order.

13. Arithmetic operators can be combined in expressions.

14. Arithmetic operators can be combined with assignment operators.

15. Numeric literals can contain underscores for readability.

16. Floating-point arithmetic can have representation limitations.

17. Decimal can be used when exact decimal arithmetic is required.

18. Arithmetic expressions can be used inside functions.

19. Arithmetic expressions can be combined with comparison operators.

20. Arithmetic expressions can be used in conditional logic.
"""


# =============================================================================
# 99. Common Arithmetic Mistakes
# =============================================================================

"""
Common mistakes include:

    - Confusing / with //.

    - Assuming / returns an integer.

    - Forgetting that division by zero raises ZeroDivisionError.

    - Confusing % with percentage calculation.

    - Forgetting that % returns a remainder.

    - Using ** when * was intended.

    - Forgetting operator precedence.

    - Using complicated expressions without parentheses.

    - Assuming floating-point arithmetic is always exact.

    - Accidentally mixing incompatible data types.

    - Forgetting that + behaves differently for different object types.

    - Confusing mutation/repetition behavior of * with numeric multiplication.
"""


# =============================================================================
# 100. Complete Arithmetic Example
# =============================================================================

"""
This example combines several arithmetic operators in one practical
calculation.
"""

item_price: float = 250.0
item_quantity: int = 4
discount_percentage: float = 10.0
tax_percentage: float = 18.0

subtotal_amount: float = (
    item_price
    * item_quantity
)

discount_amount: float = (
    subtotal_amount
    * discount_percentage
    / 100
)

price_after_discount: float = (
    subtotal_amount
    - discount_amount
)

tax_amount: float = (
    price_after_discount
    * tax_percentage
    / 100
)

final_amount: float = (
    price_after_discount
    + tax_amount
)

print("Subtotal:", subtotal_amount)
print("Discount:", discount_amount)
print("After discount:", price_after_discount)
print("Tax:", tax_amount)
print("Final amount:", final_amount)


# =============================================================================
# 101. Arithmetic Operators Key Takeaways
# =============================================================================

"""
✓ + performs addition.

✓ - performs subtraction.

✓ * performs multiplication.

✓ / performs true division.

✓ // performs floor division.

✓ % returns the remainder.

✓ ** performs exponentiation.

✓ / returns a floating-point result for numeric operands.

✓ // rounds toward negative infinity.

✓ % is useful for checking divisibility and extracting remainders.

✓ ** can be used for squares, cubes, and other powers.

✓ Parentheses can explicitly control evaluation order.

✓ Arithmetic operators can be combined in expressions.

✓ Arithmetic operators can be combined with augmented assignment operators.

✓ Arithmetic operators work with integers and floating-point numbers.

✓ Python also supports arithmetic with complex numbers.

✓ + and * can have additional behavior for sequences such as strings
  and lists.

✓ Floating-point calculations may contain small representation errors.

✓ Decimal can be used for exact decimal arithmetic when appropriate.

Core model:

    +       ADD
    -       SUBTRACT
    *       MULTIPLY
    /       TRUE DIVIDE
    //      FLOOR DIVIDE
    %       REMAINDER
    **      POWER


Arithmetic expression:

    OPERAND
       ↓
    OPERATOR
       ↓
    OPERAND
       ↓
    RESULT


Example:

    10 + 5 * 2

Operator precedence:

    5 * 2
       ↓
      10
       ↓
    10 + 10
       ↓
      20
"""


# =============================================================================
# End of 01_arithmetic_operators.py
# =============================================================================