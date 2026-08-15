# type: ignore

"""
03_nested_list_comprehensions.py

Introduces nested list comprehensions in Python.

This file focuses on:

    - What a nested list comprehension is
    - The syntax of nested list comprehensions
    - Understanding multiple for clauses
    - Translating nested for loops into list comprehensions
    - Flattening nested lists
    - Iterating over rows and elements of a matrix
    - Understanding the execution order of nested for clauses
    - Transforming values while flattening nested lists
    - Using nested comprehensions with strings
    - Using multiple levels of nested iteration
    - Producing combinations using nested comprehensions
    - Understanding when a nested comprehension improves readability

The following topics are covered separately:

    04_set_comprehensions.py
    05_dict_comprehensions.py
    06_conditional_comprehensions.py
    07_nested_comprehensions.py
    08_comprehension_vs_loop.py
    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Basic Nested List Comprehension
# ---------------------------------------------------------------------------
#
# A nested list comprehension contains more than one for clause.
#
# Syntax:
#
#     [
#         expression
#         for outer_item in outer_iterable
#         for inner_item in inner_iterable
#     ]
#
# The second for clause is executed for every iteration of the first
# for clause.


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


# ---------------------------------------------------------------------------
# 2. Equivalent Nested for Loop
# ---------------------------------------------------------------------------
#
# The comprehension above is equivalent to:
#
#     for sublist in matrix:
#         for number in sublist:
#             flat_list_loop.append(number)
#
# The outer for clause appears first in the comprehension.
# The inner for clause appears second.


flat_list_loop: list[int] = []

for sublist in matrix:
    for number in sublist:
        flat_list_loop.append(number)

print(flat_list_loop)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# ---------------------------------------------------------------------------
# 3. Understanding Execution Order
# ---------------------------------------------------------------------------
#
# Given:
#
#     [
#         number
#         for sublist in matrix
#         for number in sublist
#     ]
#
# Python conceptually processes it as:
#
#     sublist = [1, 2, 3]
#         number = 1
#         number = 2
#         number = 3
#
#     sublist = [4, 5, 6]
#         number = 4
#         number = 5
#         number = 6
#
#     sublist = [7, 8, 10]
#         number = 7
#         number = 8
#         number = 10
#
# Therefore, the resulting list preserves the iteration order.


# ---------------------------------------------------------------------------
# 4. Transforming Values While Flattening
# ---------------------------------------------------------------------------

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

squared_flat_list: list[int] = [
    number**2
    for sublist in matrix
    for number in sublist
]

print(squared_flat_list)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]


# The nested iteration determines which values are visited.
#
# The expression:
#
#     number**2
#
# determines what gets placed into the resulting list.


# ---------------------------------------------------------------------------
# 5. Nested List Comprehension with Strings
# ---------------------------------------------------------------------------

word_groups: list[list[str]] = [
    ["python", "sql"],
    ["airflow", "spark"],
    ["kafka", "snowflake"],
]

uppercase_words: list[str] = [
    word.upper()
    for group in word_groups
    for word in group
]

print(uppercase_words)
# ['PYTHON', 'SQL', 'AIRFLOW', 'SPARK', 'KAFKA', 'SNOWFLAKE']


# ---------------------------------------------------------------------------
# 6. Flattening Three Levels of Nesting
# ---------------------------------------------------------------------------
#
# More than two for clauses can be used.
#
# Each additional for clause represents another level of iteration.


nested_numbers: list[list[list[int]]] = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
]

flat_three_level_list: list[int] = [
    number
    for outer_group in nested_numbers
    for middle_group in outer_group
    for number in middle_group
]

print(flat_three_level_list)
# [1, 2, 3, 4, 5, 6, 7, 8]


# Equivalent nested loop structure:
#
#     for outer_group in nested_numbers:
#         for middle_group in outer_group:
#             for number in middle_group:
#                 flat_three_level_list.append(number)


# ---------------------------------------------------------------------------
# 7. Nested Comprehension Does Not Necessarily Mean Flattening
# ---------------------------------------------------------------------------
#
# A nested comprehension can produce any expression.
#
# The nested for clauses determine which combinations of values are
# processed, while the expression determines what is placed into the
# resulting list.


numbers_a: list[int] = [1, 2, 3]
numbers_b: list[int] = [10, 20, 30]

sum_pairs: list[int] = [
    number_a + number_b
    for number_a in numbers_a
    for number_b in numbers_b
]

print(sum_pairs)
# [11, 21, 31, 12, 22, 32, 13, 23, 33]


# ---------------------------------------------------------------------------
# 8. Creating Coordinate Pairs
# ---------------------------------------------------------------------------
#
# The expression can produce tuples instead of individual primitive values.


rows: list[int] = [1, 2, 3]
columns: list[str] = ["A", "B", "C"]

coordinates: list[tuple[int, str]] = [
    (row, column)
    for row in rows
    for column in columns
]

print(coordinates)
# [
#     (1, 'A'),
#     (1, 'B'),
#     (1, 'C'),
#     (2, 'A'),
#     (2, 'B'),
#     (2, 'C'),
#     (3, 'A'),
#     (3, 'B'),
#     (3, 'C')
# ]


# Execution order:
#
#     row = 1 -> every column
#     row = 2 -> every column
#     row = 3 -> every column


# ---------------------------------------------------------------------------
# 9. Nested Comprehension with a Function Call
# ---------------------------------------------------------------------------

word_groups: list[list[str]] = [
    ["apple", "google"],
    ["microsoft", "meta"],
]

word_lengths: list[int] = [
    len(word)
    for group in word_groups
    for word in group
]

print(word_lengths)
# [5, 6, 9, 4]


# ---------------------------------------------------------------------------
# 10. Three Approaches to Flattening a List
# ---------------------------------------------------------------------------

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10],
]


# Version 1:
# Converting the matrix to a string and parsing it back into integers.
#
# This works for this particular simple structure, but it is not a robust
# general-purpose approach to flattening nested lists.


flat_list_string_method: list[int] = [
    int(value)
    for value in str(matrix)
    .strip("[]")
    .replace(" ", "")
    .replace("[", "")
    .replace("]", "")
    .split(",")
]

print(flat_list_string_method)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# Version 2:
# Using extend() inside a list comprehension.
#
# This is intentionally shown as an anti-pattern.
#
# extend() modifies the existing list and returns None.
# Therefore, using it inside a comprehension creates a list of None values.
#
# A normal for loop is preferable when the purpose is mutation.


flat_list_extend: list[int] = []

for sublist in matrix:
    flat_list_extend.extend(sublist)

print(flat_list_extend)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# Avoid:
#
#     [flat_list_extend.extend(sublist) for sublist in matrix]
#
# The purpose of a list comprehension should normally be to construct
# a new list, not to perform side effects.


# Version 3:
# The cleanest approach for this particular problem.


flat_list_nested_comprehension: list[int] = [
    number
    for sublist in matrix
    for number in sublist
]

print(flat_list_nested_comprehension)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# ---------------------------------------------------------------------------
# 11. Nested Comprehension vs. Readability
# ---------------------------------------------------------------------------
#
# Nested comprehensions can become difficult to understand when too many
# levels of iteration or complex expressions are introduced.
#
# For example, this is technically valid:
#
#     result = [
#         value
#         for group in data
#         for row in group
#         for value in row
#         if value > 10
#     ]
#
# However, if the logic becomes substantially more complicated, a normal
# for loop may communicate the intention more clearly.
#
# Readability and maintainability are covered in:
#
#     08_comprehension_vs_loop.py
#     09_comprehension_best_practices.py

