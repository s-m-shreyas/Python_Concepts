# type: ignore
"""
04_set_comprehensions.py

Introduces set comprehensions in Python.

This file focuses on:

    - What a set comprehension is
    - The basic set comprehension syntax
    - Creating sets from iterables
    - Transforming values with set comprehensions
    - Automatic duplicate removal
    - Using expressions inside set comprehensions
    - Using functions and methods inside set comprehensions
    - Filtering values with a set comprehension
    - Understanding the difference between list and set comprehensions
    - Using set comprehensions with strings

The following topics are covered separately:

    05_dict_comprehensions.py
    06_conditional_comprehensions.py
    07_nested_comprehensions.py
    08_comprehension_vs_loop.py
    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Basic Set Comprehension
# ---------------------------------------------------------------------------
#
# Basic syntax:
#
#     {expression for item in iterable}
#
# The syntax looks similar to a list comprehension.
#
# List comprehension:
#
#     [expression for item in iterable]
#
# Set comprehension:
#
#     {expression for item in iterable}


numbers: list[int] = [1, 2, 3, 4, 5]

squared_number_set: set[int] = {
    number**2
    for number in numbers
}

print(squared_number_set)
# {1, 4, 9, 16, 25}


# ---------------------------------------------------------------------------
# 2. Set Comprehension Removes Duplicates
# ---------------------------------------------------------------------------
#
# A set can contain each value only once.
#
# Therefore, if a set comprehension produces duplicate values,
# only one copy is retained.


numbers_with_duplicates: list[int] = [
    1,
    2,
    2,
    3,
    3,
    3,
    4,
    4,
]

squared_numbers: set[int] = {
    number**2
    for number in numbers_with_duplicates
}

print(squared_numbers)
# {1, 4, 9, 16}


# Compare with a list comprehension:


squared_number_list: list[int] = [
    number**2
    for number in numbers_with_duplicates
]

print(squared_number_list)
# [1, 4, 4, 9, 9, 9, 16, 16]


# The list preserves every generated value.
# The set retains only unique values.


# ---------------------------------------------------------------------------
# 3. Converting Strings to Uppercase
# ---------------------------------------------------------------------------

languages: list[str] = [
    "python",
    "java",
    "sql",
    "python",
    "spark",
]

uppercase_languages: set[str] = {
    language.upper()
    for language in languages
}

print(uppercase_languages)
# {'PYTHON', 'JAVA', 'SQL', 'SPARK'}


# Duplicate "python" values produce only one "PYTHON" in the set.


# ---------------------------------------------------------------------------
# 4. Extracting String Lengths
# ---------------------------------------------------------------------------

companies: list[str] = [
    "apple",
    "google",
    "microsoft",
    "meta",
    "amazon",
]

company_lengths: set[int] = {
    len(company)
    for company in companies
}

print(company_lengths)
# {4, 5, 6, 7, 9}


# The resulting set contains unique string lengths rather than one length
# for every company.


# ---------------------------------------------------------------------------
# 5. Using a Function Inside a Set Comprehension
# ---------------------------------------------------------------------------

numbers: list[int] = [
    -10,
    -5,
    -2,
    0,
    2,
    5,
    10,
]

absolute_values: set[int] = {
    abs(number)
    for number in numbers
}

print(absolute_values)
# {0, 2, 5, 10}


# Both -5 and 5 produce 5.
# The set therefore stores 5 only once.


# ---------------------------------------------------------------------------
# 6. Filtering with a Set Comprehension
# ---------------------------------------------------------------------------
#
# A set comprehension can also contain a filtering condition:
#
#     {expression for item in iterable if condition}


numbers: list[int] = list(range(1, 11))

even_numbers: set[int] = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)
# {2, 4, 6, 8, 10}


# Conditional comprehensions are covered more systematically in:
#
#     06_conditional_comprehensions.py


# ---------------------------------------------------------------------------
# 7. Extracting Unique Initial Characters
# ---------------------------------------------------------------------------

company_names: list[str] = [
    "apple",
    "amazon",
    "google",
    "microsoft",
    "meta",
    "oracle",
]

initial_characters: set[str] = {
    company[0].upper()
    for company in company_names
}

print(initial_characters)
# {'A', 'G', 'M', 'O'}


# Multiple companies can produce the same initial character.
# The set automatically removes those duplicates.


# ---------------------------------------------------------------------------
# 8. Set Comprehension from a Range
# ---------------------------------------------------------------------------

multiples_of_three: set[int] = {
    number
    for number in range(1, 21)
    if number % 3 == 0
}

print(multiples_of_three)
# {3, 6, 9, 12, 15, 18}


# ---------------------------------------------------------------------------
# 9. List Comprehension vs. Set Comprehension
# ---------------------------------------------------------------------------

numbers: list[int] = [
    1,
    2,
    2,
    3,
    3,
    3,
]

list_result: list[int] = [
    number
    for number in numbers
]

set_result: set[int] = {
    number
    for number in numbers
}

print(list_result)
# [1, 2, 2, 3, 3, 3]

print(set_result)
# {1, 2, 3}


# The expression and iteration are the same.
#
# The collection type is different:
#
#     [...] -> list
#
#     {...} -> set


# ---------------------------------------------------------------------------
# 10. Set Comprehension Does Not Create an Indexed Collection
# ---------------------------------------------------------------------------

numbers: list[int] = [10, 20, 30, 40]

number_set: set[int] = {
    number
    for number in numbers
}

print(number_set)
# {10, 20, 30, 40}


# A set does not support positional indexing like a list.
#
# For example, this is valid:
#
#     numbers[0]
#
# but this is not:
#
#     number_set[0]
#
# Sets are designed for membership testing and uniqueness rather than
# positional access.


# ---------------------------------------------------------------------------
# 11. Creating a Set of String Lengths
# ---------------------------------------------------------------------------

words: list[str] = [
    "python",
    "sql",
    "java",
    "spark",
    "airflow",
    "go",
]

word_lengths: set[int] = {
    len(word)
    for word in words
}

print(word_lengths)
# {2, 3, 4, 6, 7}


# ---------------------------------------------------------------------------
# 12. Equivalent for Loop
# ---------------------------------------------------------------------------

numbers: list[int] = [
    1,
    2,
    2,
    3,
    3,
]

squared_numbers_comprehension: set[int] = {
    number**2
    for number in numbers
}

squared_numbers_loop: set[int] = set()

for number in numbers:
    squared_numbers_loop.add(number**2)

print(squared_numbers_comprehension)
# {1, 4, 9}

print(squared_numbers_loop)
# {1, 4, 9}


# A set comprehension is therefore a concise way of constructing a set
# through iteration.


# ---------------------------------------------------------------------------
# 13. Important Syntax Difference
# ---------------------------------------------------------------------------
#
# List:
#
#     [expression for item in iterable]
#
# Set:
#
#     {expression for item in iterable}
#
# Dictionary:
#
#     {key: value for item in iterable}
#
# The dictionary form is covered separately in:
#
#     05_dict_comprehensions.py
#
#
# Important:
#
#     {}
#
# by itself creates an empty dictionary, not an empty set.
#
# To create an empty set:
#
#     set()


empty_set: set[int] = set()

print(empty_set)
# set()

