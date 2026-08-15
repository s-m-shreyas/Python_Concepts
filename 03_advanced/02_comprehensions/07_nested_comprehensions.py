# type: ignore

"""
07_nested_comprehensions.py

Introduces nested comprehensions in Python.

This file focuses on:

    - Understanding nested for clauses
    - Understanding the execution order of nested comprehensions
    - Flattening nested lists
    - Flattening matrices
    - Transforming nested data
    - Creating Cartesian products
    - Using conditions inside nested comprehensions
    - Creating nested lists
    - Creating nested dictionaries
    - Comparing nested comprehensions with nested for loops

The following topics are covered separately:

    08_comprehension_vs_loop.py
    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Basic Nested List Comprehension
# ---------------------------------------------------------------------------
#
# A nested comprehension can contain multiple for clauses.
#
# Syntax:
#
#     [expression
#      for outer_item in outer_iterable
#      for inner_item in inner_iterable]
#
# The second for loop runs completely for every iteration of the first
# for loop.


numbers: list[int] = [1, 2, 3]
letters: list[str] = ["A", "B", "C"]

number_letter_pairs: list[str] = [
    f"{number}{letter}"
    for number in numbers
    for letter in letters
]

print(number_letter_pairs)
# [
#     '1A', '1B', '1C',
#     '2A', '2B', '2C',
#     '3A', '3B', '3C'
# ]


# The execution order is equivalent to:
#
# for number in numbers:
#     for letter in letters:
#         ...


# ---------------------------------------------------------------------------
# 2. Nested for Loop Equivalent
# ---------------------------------------------------------------------------


number_letter_pairs_loop: list[str] = []

for number in numbers:
    for letter in letters:
        number_letter_pairs_loop.append(f"{number}{letter}")

print(number_letter_pairs_loop)
# [
#     '1A', '1B', '1C',
#     '2A', '2B', '2C',
#     '3A', '3B', '3C'
# ]


# ---------------------------------------------------------------------------
# 3. Flattening a Nested List
# ---------------------------------------------------------------------------
#
# One of the most common uses of a nested comprehension is flattening
# one level of nested lists.
#
# Syntax:
#
#     [item for sublist in nested_list for item in sublist]


matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10],
]

flat_list: list[int] = [
    number
    for row in matrix
    for number in row
]

print(flat_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 10]


# Read the comprehension from left to right:
#
#     for row in matrix
#         for number in row
#             number


# ---------------------------------------------------------------------------
# 4. Flattening a Nested List with a Condition
# ---------------------------------------------------------------------------


even_numbers_from_matrix: list[int] = [
    number
    for row in matrix
    for number in row
    if number % 2 == 0
]

print(even_numbers_from_matrix)
# [2, 4, 6, 8, 10]


# ---------------------------------------------------------------------------
# 5. Transforming a Matrix
# ---------------------------------------------------------------------------
#
# The expression can transform every individual element.


squared_matrix_values: list[int] = [
    number**2
    for row in matrix
    for number in row
]

print(squared_matrix_values)
# [1, 4, 9, 16, 25, 36, 49, 64, 100]


# Notice:
#
# The result above is flat.
#
# A nested result requires the outer expression to itself produce a list.


# ---------------------------------------------------------------------------
# 6. Creating a New Matrix
# ---------------------------------------------------------------------------
#
# Here the outer comprehension creates rows.
# The inner comprehension creates the values inside each row.


matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10],
]

squared_matrix: list[list[int]] = [
    [
        number**2
        for number in row
    ]
    for row in matrix
]

print(squared_matrix)
# [
#     [1, 4, 9],
#     [16, 25, 36],
#     [49, 64, 100]
# ]


# ---------------------------------------------------------------------------
# 7. Matrix Transformation with enumerate()
# ---------------------------------------------------------------------------
#
# enumerate() can be used inside nested comprehensions when the position
# of an element is required.


matrix: list[list[int]] = [
    [1, 2],
    [3, 4],
]

indexed_matrix: list[list[str]] = [
    [
        f"row={row_index}, col={column_index}, value={value}"
        for column_index, value in enumerate(row)
    ]
    for row_index, row in enumerate(matrix)
]

print(indexed_matrix)


# ---------------------------------------------------------------------------
# 8. Cartesian Product
# ---------------------------------------------------------------------------
#
# A nested comprehension can generate every possible combination between
# two collections.


colors: list[str] = [
    "Red",
    "Green",
    "Blue",
]

sizes: list[str] = [
    "S",
    "M",
    "L",
]

products: list[str] = [
    f"{color}-{size}"
    for color in colors
    for size in sizes
]

print(products)
# [
#     'Red-S', 'Red-M', 'Red-L',
#     'Green-S', 'Green-M', 'Green-L',
#     'Blue-S', 'Blue-M', 'Blue-L'
# ]


# ---------------------------------------------------------------------------
# 9. Cartesian Product with a Condition
# ---------------------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ["A", "B", "C", "D"]

even_number_pairs: list[str] = [
    f"{number}{letter}"
    for number in numbers
    for letter in letters
    if number % 2 == 0
]

print(even_number_pairs)
# [
#     '2A', '2B', '2C', '2D',
#     '4A', '4B', '4C', '4D'
# ]


# ---------------------------------------------------------------------------
# 10. Nested Comprehension with Multiple Conditions
# ---------------------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4, 5]
letters: list[str] = ["A", "B", "C"]

filtered_pairs: list[str] = [
    f"{number}{letter}"
    for number in numbers
    for letter in letters
    if number % 2 == 0
    if letter != "B"
]

print(filtered_pairs)
# ['2A', '2C', '4A', '4C']


# Multiple trailing if clauses act as additional filtering conditions.


# ---------------------------------------------------------------------------
# 11. Flattening Nested Strings
# ---------------------------------------------------------------------------


company_groups: list[list[str]] = [
    ["Apple", "Google"],
    ["Microsoft", "Amazon"],
    ["Meta", "Oracle"],
]

companies: list[str] = [
    company
    for group in company_groups
    for company in group
]

print(companies)
# [
#     'Apple',
#     'Google',
#     'Microsoft',
#     'Amazon',
#     'Meta',
#     'Oracle'
# ]


# ---------------------------------------------------------------------------
# 12. Transforming Nested Strings
# ---------------------------------------------------------------------------


uppercase_companies: list[str] = [
    company.upper()
    for group in company_groups
    for company in group
]

print(uppercase_companies)
# [
#     'APPLE',
#     'GOOGLE',
#     'MICROSOFT',
#     'AMAZON',
#     'META',
#     'ORACLE'
# ]


# ---------------------------------------------------------------------------
# 13. Nested Set Comprehension
# ---------------------------------------------------------------------------
#
# A set comprehension can also contain nested loops.


numbers: list[int] = [1, 2, 3]
letters: list[str] = ["A", "B"]

unique_pairs: set[str] = {
    f"{number}{letter}"
    for number in numbers
    for letter in letters
}

print(unique_pairs)
# {'1A', '1B', '2A', '2B', '3A', '3B'}


# The result is a set, so duplicate generated values would automatically
# be removed.


# ---------------------------------------------------------------------------
# 14. Nested Dictionary Comprehension
# ---------------------------------------------------------------------------
#
# Dictionary comprehensions can also contain nested loops.


numbers: list[int] = [1, 2, 3]

number_squares: dict[int, dict[str, int]] = {
    number: {
        "square": number**2,
        "cube": number**3,
    }
    for number in numbers
}

print(number_squares)
# {
#     1: {'square': 1, 'cube': 1},
#     2: {'square': 4, 'cube': 8},
#     3: {'square': 9, 'cube': 27}
# }


# ---------------------------------------------------------------------------
# 15. Nested Dictionary Comprehension with Two Iterables
# ---------------------------------------------------------------------------


departments: list[str] = [
    "Engineering",
    "Analytics",
]

levels: list[str] = [
    "Junior",
    "Senior",
]

department_levels: dict[str, list[str]] = {
    department: [
        level
        for level in levels
    ]
    for department in departments
}

print(department_levels)
# {
#     'Engineering': ['Junior', 'Senior'],
#     'Analytics': ['Junior', 'Senior']
# }


# ---------------------------------------------------------------------------
# 16. Nested Comprehension vs. Nested Loops
# ---------------------------------------------------------------------------


matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
]

flat_comprehension: list[int] = [
    number
    for row in matrix
    for number in row
]

flat_loop: list[int] = []

for row in matrix:
    for number in row:
        flat_loop.append(number)

print(flat_comprehension)
# [1, 2, 3, 4, 5, 6]

print(flat_loop)
# [1, 2, 3, 4, 5, 6]


# ---------------------------------------------------------------------------
# 17. Important Execution Order
# ---------------------------------------------------------------------------
#
# Consider:
#
#     [
#         f"{number}{letter}"
#         for number in numbers
#         for letter in letters
#     ]
#
# Python processes it conceptually as:
#
#     for number in numbers:
#         for letter in letters:
#             f"{number}{letter}"
#
#
# Therefore, the LEFTMOST for loop is the OUTER loop,
# and the next for loop is the INNER loop.


numbers: list[int] = [1, 2]
letters: list[str] = ["A", "B"]

result: list[str] = [
    f"{number}{letter}"
    for number in numbers
    for letter in letters
]

print(result)
# ['1A', '1B', '2A', '2B']


# ---------------------------------------------------------------------------
# 18. Important Readability Note
# ---------------------------------------------------------------------------
#
# Nested comprehensions can become difficult to understand when too many
# levels, conditions, or transformations are combined.
#
# For example, a deeply nested comprehension may technically be valid
# Python but still be poor code if the logic becomes difficult to read.
#
# Prefer a normal loop when the comprehension no longer communicates the
# logic clearly.
#
# The next file:
#
#     08_comprehension_vs_loop.py
#
# focuses specifically on this trade-off.