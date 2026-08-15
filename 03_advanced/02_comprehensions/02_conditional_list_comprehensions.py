# type: ignore

"""
03_conditional_list_comprehension.py

Introduces conditional filtering in list comprehensions.

This file focuses on:

    - Adding an if condition to a list comprehension
    - Filtering items from an iterable
    - Separating the expression from the filtering condition
    - Using string methods in a filtering condition
    - Using isinstance() for type-based filtering
    - Using all() inside a filtering condition
    - Using generator expressions inside all()
    - Combining list comprehensions with functions
    - Using a recursive lambda expression inside a comprehension
    - Understanding that the if condition controls which items are included

The following topics are covered separately:

    04_if_else_list_comprehension.py
    05_nested_list_comprehension.py
    06_multiple_iterables.py
    07_comprehension_vs_for_loop.py
    08_practical_patterns.py
"""


# ---------------------------------------------------------------------------
# 1. Basic Conditional List Comprehension
# ---------------------------------------------------------------------------
#
# Basic syntax:
#
#     [expression for item in iterable if condition]
#
# The condition is evaluated for every item.
#
# If the condition is True:
#
#     expression is evaluated
#     result is added to the new list
#
# If the condition is False:
#
#     the item is skipped
#
# Example:
#
#     [number for number in numbers if number > 3]


numbers: list[int] = [1, 2, 3, 4, 5]

greater_than_three: list[int] = [
    number
    for number in numbers
    if number > 3
]

print(greater_than_three)
# [4, 5]


# ---------------------------------------------------------------------------
# 2. Filtering Strings Based on a Condition
# ---------------------------------------------------------------------------

lang_string_list: list[str] = [
    "Python",
    "Perl",
    "Java",
    "php",
    "C++",
]

p_filtered_string_list: list[str] = [
    string
    for string in lang_string_list
    if string.capitalize().startswith("P")
]

print(p_filtered_string_list)
# ['Python', 'Perl', 'php']


# The expression is:
#
#     string
#
# The condition is:
#
#     string.capitalize().startswith("P")
#
# The expression determines what gets added to the result.
# The condition determines whether the item is included.


# ---------------------------------------------------------------------------
# 3. Filtering Even Numbers
# ---------------------------------------------------------------------------

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
# [2, 4, 6, 8, 10]


# ---------------------------------------------------------------------------
# 4. Filtering Using isinstance()
# ---------------------------------------------------------------------------
#
# isinstance() can be used when the filtering condition depends on the
# runtime type of an object.


from typing import Any


names_and_values: list[Any] = [
    "Shreyas",
    10,
    11.4,
    "Pranay",
    3 + 8j,
    ["xyz"],
]

filtered_names: list[str] = [
    item
    for item in names_and_values
    if isinstance(item, str)
]

print(filtered_names)
# ['Shreyas', 'Pranay']


# A more general type annotation can also be used:
#
#     list[object]
#
# instead of list[Any].
#
# Any is retained here because the example intentionally demonstrates
# filtering values of different runtime types.


# ---------------------------------------------------------------------------
# 5. Filtering Prime Numbers Using all()
# ---------------------------------------------------------------------------
#
# A number is prime when it has no divisor other than 1 and itself.
#
# For every candidate number:
#
#     range(2, number)
#
# generates all possible divisors between 2 and number - 1.
#
# all() returns True only when every condition in the iterable is True.


stop_range: int = 100

prime_numbers: list[int] = [
    number
    for number in range(2, stop_range + 1)
    if all(
        number % divisor != 0
        for divisor in range(2, number)
    )
]

print(prime_numbers)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ... 97]


# The inner expression:
#
#     number % divisor != 0
#
# checks whether the current number is NOT divisible by divisor.
#
# The outer condition:
#
#     all(...)
#
# requires every generated condition to be True.


# ---------------------------------------------------------------------------
# 6. Using a Generator Expression Inside all()
# ---------------------------------------------------------------------------
#
# The inner expression:
#
#     (number % divisor != 0 for divisor in range(2, number))
#
# is a generator expression.
#
# It does not immediately create a list.
#
# all() consumes the generated values and stops as soon as it encounters
# False.


number: int = 13

is_prime: bool = all(
    number % divisor != 0
    for divisor in range(2, number)
)

print(is_prime)
# True


# For number = 12:
#
#     12 % 2 != 0
#
# becomes False.
#
# Therefore all() immediately knows that 12 is not prime.


# ---------------------------------------------------------------------------
# 7. Factorials Using a Recursive Lambda Expression
# ---------------------------------------------------------------------------
#
# The following example demonstrates how a list comprehension can contain
# a complex expression involving lambda functions and recursion.
#
# The underlying recursive logic is equivalent to:
#
#     def worker(f, n, acc):
#         if n == 0:
#             return acc
#         return f(f, n - 1, acc * n)
#
#
#     def factorial(n):
#         return worker(worker, n, 1)
#
#
# This is intentionally included as an advanced experiment.
#
# It is NOT the recommended way to calculate factorials in normal Python.
# math.factorial() is clearer and more appropriate for that task.


factorialize_numbers: list[int] = [1, 2, 3, 4, 5]


factorialized_numbers_recursive: list[int] = [
    (
        lambda function: function(function, current_number, 1)
    )(
        lambda function, current_number, accumulator: (
            accumulator
            if current_number == 0
            else function(
                function,
                current_number - 1,
                accumulator * current_number,
            )
        )
    )
    for current_number in factorialize_numbers
]

print(factorialized_numbers_recursive)
# [1, 2, 6, 24, 120]


# The important list-comprehension structure is still:
#
#     [
#         expression
#         for current_number in factorialize_numbers
#     ]
#
# The expression simply happens to be a more complicated lambda-based
# calculation.


# ---------------------------------------------------------------------------
# 8. Conditional List Comprehension vs. Conditional Expression
# ---------------------------------------------------------------------------
#
# A filtering condition:
#
#     [number for number in numbers if number > 3]
#
# decides whether an item is included.
#
# It does NOT provide an alternative value.
#
# The following concept is different:
#
#     [number if number > 3 else 0 for number in numbers]
#
# Here every item is included, but the resulting value changes depending
# on the condition.
#
# The if/else form is covered separately in:
#
#     04_if_else_list_comprehension.py


# ---------------------------------------------------------------------------
# 9. Equivalent Traditional for Loop
# ---------------------------------------------------------------------------

numbers: list[int] = [1, 2, 3, 4, 5]

even_numbers_comprehension: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

even_numbers_loop: list[int] = []

for number in numbers:
    if number % 2 == 0:
        even_numbers_loop.append(number)

print(even_numbers_comprehension)
# [2, 4]

print(even_numbers_loop)
# [2, 4]


# The list comprehension combines:
#
#     iteration
#     filtering
#     result creation
#
# into one expression.


# ---------------------------------------------------------------------------
# 10. Core Mental Model
# ---------------------------------------------------------------------------
#
# A conditional list comprehension:
#
#     [expression for item in iterable if condition]
#
# can be mentally read as:
#
#     "For every item in iterable,
#      if condition is True,
#      put expression into the resulting list."
#
#
# Example:
#
#     [number**2 for number in numbers if number % 2 == 0]
#
# means:
#
#     1. Take every number from numbers.
#     2. Check whether the number is even.
#     3. Skip it if it is not even.
#     4. Square it if it is even.
#     5. Add the squared value to the resulting list.