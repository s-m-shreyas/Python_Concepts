"""
01_basic_list_comprehension.py

Introduces basic list comprehensions in Python.

This file focuses on:

    - What a list comprehension is
    - The basic list comprehension syntax
    - Converting a simple for loop into a list comprehension
    - Transforming values using list comprehensions
    - Producing different object types from each iteration
    - Calling functions inside list comprehensions
    - Using enumerate() inside list comprehensions
    - Using zip() inside list comprehensions
    - A basic introduction to nested iteration
    - Flattening a simple nested list
    - Using eval() inside a list comprehension
    - Why comprehensions should not be used only for side effects

The following topics are covered separately:

    02_list_comprehension_syntax.py
    03_conditional_list_comprehension.py
    04_if_else_list_comprehension.py
    05_nested_list_comprehension.py
    06_multiple_iterables.py
    07_comprehension_vs_for_loop.py
    08_practical_patterns.py
"""
# The basic list comprehension syntax is:

# [expression for item in iterable]

# With filtering:

# [expression for item in iterable if condition]

# With if/else:

# [value_if_true if condition else value_if_false for item in iterable]

# With nested iteration:

# [expression for outer_item in outer_iterable for inner_item in inner_iterable]

# ---------------------------------------------------------------------------
# 1. Basic List Comprehension
# ---------------------------------------------------------------------------

number_list: list[int] = [1, 2, 3, 4, 5]

squared_number_list: list[int] = [
    number**2
    for number in number_list
]

print(squared_number_list)
# [1, 4, 9, 16, 25]


# The same operation using a traditional for loop:

squared_number_list_loop: list[int] = []

for number in number_list:
    squared_number_list_loop.append(number**2)

print(squared_number_list_loop)
# [1, 4, 9, 16, 25]


# ---------------------------------------------------------------------------
# 2. Producing Dictionaries from Each Iteration
# ---------------------------------------------------------------------------

companies_string_list: list[str] = [
    "apple",
    "yahoo",
    "google",
    "tech-mahindra",
    "microsoft",
    "x",
    "facebook",
    "instagram",
]

companies_string_list_length_pair: list[dict[str, int]] = [
    {company: len(company)}
    for company in companies_string_list
]

print(companies_string_list_length_pair)
# [
#     {'apple': 5},
#     {'yahoo': 5},
#     {'google': 6},
#     {'tech-mahindra': 12},
#     {'microsoft': 9},
#     {'x': 1},
#     {'facebook': 8},
#     {'instagram': 9}
# ]


# ---------------------------------------------------------------------------
# 3. Using enumerate() Inside a List Comprehension
# ---------------------------------------------------------------------------

numbered_company_string_list: list[dict[int, str]] = [
    {index: company}
    for index, company in enumerate(companies_string_list, start=1)
]

print(numbered_company_string_list)
# [
#     {1: 'apple'},
#     {2: 'yahoo'},
#     {3: 'google'},
#     {4: 'tech-mahindra'},
#     {5: 'microsoft'},
#     {6: 'x'},
#     {7: 'facebook'},
#     {8: 'instagram'}
# ]


# ---------------------------------------------------------------------------
# 4. Calling a Function Inside a List Comprehension
# ---------------------------------------------------------------------------

import math


factorialize_numbers: list[int] = [1, 2, 3, 4, 5]

factorialized_numbers: list[int] = [
    math.factorial(number)
    for number in factorialize_numbers
]

print(factorialized_numbers)
# [1, 2, 6, 24, 120]


# ---------------------------------------------------------------------------
# 5. Using eval() Inside a List Comprehension
# ---------------------------------------------------------------------------
#
# This is an experimental alternative to calculate factorials.
#
# For each number:
#
#     1. range() generates numbers from 1 through number.
#     2. str() converts each number to a string.
#     3. join() creates an arithmetic expression.
#     4. eval() evaluates that expression.
#
# Example:
#
#     number = 5
#
#     range(1, 6)
#         -> 1, 2, 3, 4, 5
#
#     [str(num) for num in range(1, 6)]
#         -> ['1', '2', '3', '4', '5']
#
#     '*'.join(...)
#         -> '1*2*3*4*5'
#
#     eval('1*2*3*4*5')
#         -> 120
#
# This demonstrates that the expression portion of a comprehension can
# contain a relatively complex expression.
#
# IMPORTANT:
# eval() executes dynamically generated Python code and should NOT be used
# for normal factorial calculations. math.factorial() is the appropriate
# implementation for this particular problem.

factorialized_numbers_eval: list[int] = [
    eval(
        "*".join(
            str(number)
            for number in range(1, current_number + 1)
        )
    )
    for current_number in factorialize_numbers
]

print(factorialized_numbers_eval)
# [1, 2, 6, 24, 120]


# ---------------------------------------------------------------------------
# 6. Using zip() Inside a List Comprehension
# ---------------------------------------------------------------------------

first_names: list[str] = [
    "arjun",
    "Pranay",
    "ramesh",
]

last_names: list[str] = [
    "pal",
    "Gharde",
    "powar",
]

full_names: list[str] = [
    f"{first_name.capitalize()} {last_name.capitalize()}"
    for first_name, last_name in zip(first_names, last_names)
]

print(full_names)
# ['S.M. Shreyas', 'Pranay Gharde', 'Rajeshwari Khot']


# ---------------------------------------------------------------------------
# 7. Basic Nested Iteration
# ---------------------------------------------------------------------------

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10],
]

flat_list: list[int] = [
    number
    for sublist in matrix
    for number in sublist
]

print(flat_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# The detailed mechanics of nested list comprehensions are covered in:
#
#     05_nested_list_comprehension.py


# ---------------------------------------------------------------------------
# 8. Do Not Use Comprehensions Only for Side Effects
# ---------------------------------------------------------------------------

flat_list_extend: list[int] = []

for sublist in matrix:
    flat_list_extend.extend(sublist)

print(flat_list_extend)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# Avoid using a list comprehension only to call extend():
#
#     [flat_list_extend.extend(sublist) for sublist in matrix]
#
# The comprehension creates a list of None values because extend() returns
# None. The actual purpose would only be the side effect of modifying
# flat_list_extend.
#
# When the purpose is to create a new list, use a list comprehension.
# When the purpose is to perform side effects, use a normal for loop.