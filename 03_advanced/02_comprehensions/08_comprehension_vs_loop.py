# type: ignore
"""
08_comprehension_vs_loop.py

Compares comprehensions with traditional for loops in Python.

This file focuses on:

    - Equivalent comprehension and loop implementations
    - Readability
    - Conciseness
    - Filtering
    - Transformation
    - Dictionary construction
    - Set construction
    - Nested logic
    - Side effects
    - When a comprehension is appropriate
    - When a traditional loop is preferable
    - Understanding that shorter code is not always better code

The following topic is covered separately:

    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Simple Transformation
# ---------------------------------------------------------------------------
#
# A comprehension is usually a good choice when the operation is simple
# and directly expresses the resulting collection.


numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers_comprehension: list[int] = [
    number**2
    for number in numbers
]

squared_numbers_loop: list[int] = []

for number in numbers:
    squared_numbers_loop.append(number**2)

print(squared_numbers_comprehension)
# [1, 4, 9, 16, 25]

print(squared_numbers_loop)
# [1, 4, 9, 16, 25]


# Both approaches are correct.
#
# The comprehension is more concise and still easy to understand.


# ---------------------------------------------------------------------------
# 2. Filtering
# ---------------------------------------------------------------------------
#
# Comprehensions are especially natural for simple filtering operations.


numbers: list[int] = list(range(1, 11))

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
# [2, 4, 6, 8, 10]

print(even_numbers_loop)
# [2, 4, 6, 8, 10]


# When the transformation and condition are simple,
# the comprehension communicates the intent very clearly.


# ---------------------------------------------------------------------------
# 3. Dictionary Construction
# ---------------------------------------------------------------------------


companies: list[str] = [
    "apple",
    "google",
    "microsoft",
    "amazon",
]

company_lengths_comprehension: dict[str, int] = {
    company: len(company)
    for company in companies
}

company_lengths_loop: dict[str, int] = {}

for company in companies:
    company_lengths_loop[company] = len(company)

print(company_lengths_comprehension)
# {
#     'apple': 5,
#     'google': 6,
#     'microsoft': 9,
#     'amazon': 6
# }

print(company_lengths_loop)
# {
#     'apple': 5,
#     'google': 6,
#     'microsoft': 9,
#     'amazon': 6
# }


# ---------------------------------------------------------------------------
# 4. Set Construction
# ---------------------------------------------------------------------------


numbers: list[int] = [
    1,
    2,
    2,
    3,
    3,
    4,
]

unique_squares_comprehension: set[int] = {
    number**2
    for number in numbers
}

unique_squares_loop: set[int] = set()

for number in numbers:
    unique_squares_loop.add(number**2)

print(unique_squares_comprehension)
# {1, 4, 9, 16}

print(unique_squares_loop)
# {1, 4, 9, 16}


# ---------------------------------------------------------------------------
# 5. Multiple Conditions
# ---------------------------------------------------------------------------
#
# A comprehension can remain readable when the conditions are simple.


numbers: list[int] = list(range(1, 21))

filtered_numbers_comprehension: list[int] = [
    number
    for number in numbers
    if number > 5
    if number % 2 == 0
]

filtered_numbers_loop: list[int] = []

for number in numbers:
    if number > 5:
        if number % 2 == 0:
            filtered_numbers_loop.append(number)

print(filtered_numbers_comprehension)
# [6, 8, 10, 12, 14, 16, 18, 20]

print(filtered_numbers_loop)
# [6, 8, 10, 12, 14, 16, 18, 20]


# ---------------------------------------------------------------------------
# 6. Conditional Value Selection
# ---------------------------------------------------------------------------
#
# An if/else expression can also be used inside a comprehension.


numbers: list[int] = [1, 2, 3, 4, 5]

number_types_comprehension: list[str] = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

number_types_loop: list[str] = []

for number in numbers:

    if number % 2 == 0:
        number_types_loop.append("Even")
    else:
        number_types_loop.append("Odd")

print(number_types_comprehension)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']

print(number_types_loop)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ---------------------------------------------------------------------------
# 7. Nested Comprehension vs. Nested Loop
# ---------------------------------------------------------------------------
#
# Nested comprehensions can be concise, but readability becomes important.


matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
]

flat_matrix_comprehension: list[int] = [
    number
    for row in matrix
    for number in row
]

flat_matrix_loop: list[int] = []

for row in matrix:
    for number in row:
        flat_matrix_loop.append(number)

print(flat_matrix_comprehension)
# [1, 2, 3, 4, 5, 6]

print(flat_matrix_loop)
# [1, 2, 3, 4, 5, 6]


# A single nested level is still reasonably readable.
#
# As nesting becomes deeper, a normal loop may communicate the algorithm
# more clearly.


# ---------------------------------------------------------------------------
# 8. When a Loop Is Better: Multiple Steps
# ---------------------------------------------------------------------------
#
# A comprehension is not always appropriate.
#
# If several operations are required for every item, a normal loop may
# be much easier to understand.


numbers: list[int] = [1, 2, 3, 4, 5]

processed_numbers: list[int] = []

for number in numbers:

    squared_number: int = number**2

    if squared_number > 10:
        adjusted_number: int = squared_number + 100
        processed_numbers.append(adjusted_number)

print(processed_numbers)
# [116, 125]


# Trying to compress several steps into one comprehension would make the
# logic harder to understand.
#
# The loop is therefore the better choice here.


# ---------------------------------------------------------------------------
# 9. When a Loop Is Better: Multiple Branches
# ---------------------------------------------------------------------------
#
# Multiple branches are another situation where a loop can be clearer.


numbers: list[int] = [1, 2, 3, 4, 5, 6]

classified_numbers: list[str] = []

for number in numbers:

    if number % 3 == 0:
        classified_numbers.append("Divisible by 3")

    elif number % 2 == 0:
        classified_numbers.append("Even")

    else:
        classified_numbers.append("Other")

print(classified_numbers)
# [
#     'Other',
#     'Even',
#     'Divisible by 3',
#     'Even',
#     'Other',
#     'Divisible by 3'
# ]


# A comprehension with deeply nested conditional expressions would be much
# harder to read than this straightforward loop.


# ---------------------------------------------------------------------------
# 10. When a Loop Is Better: Side Effects
# ---------------------------------------------------------------------------
#
# Comprehensions should primarily be used to BUILD collections.
#
# They should generally not be used merely to execute an operation for
# its side effect.


companies: list[str] = [
    "Apple",
    "Google",
    "Microsoft",
]


# Good:
#
#     uppercase_companies = [
#         company.upper()
#         for company in companies
#     ]


uppercase_companies: list[str] = [
    company.upper()
    for company in companies
]

print(uppercase_companies)
# ['APPLE', 'GOOGLE', 'MICROSOFT']


# Avoid code such as:
#
#     [print(company) for company in companies]
#
# This creates a list only to execute print().
#
# A normal loop is clearer for side effects:
#
#     for company in companies:
#         print(company)


# ---------------------------------------------------------------------------
# 11. A Real Example: Word Frequency
# ---------------------------------------------------------------------------
#
# Our previous dictionary-comprehension example counted word frequencies
# using list.count().
#
# That is useful for learning dictionary comprehensions, but repeated
# count() calls can become inefficient.
#
# A normal loop provides a better approach.


words: list[str] = [
    "Python",
    "SQL",
    "Python",
    "Java",
    "SQL",
    "Python",
]

word_count: dict[str, int] = {}

for word in words:

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {
#     'Python': 3,
#     'SQL': 2,
#     'Java': 1
# }


# This is a good example of why:
#
#     shorter != always better
#
# The best implementation depends on the problem.


# ---------------------------------------------------------------------------
# 12. Comprehension Readability Test
# ---------------------------------------------------------------------------
#
# A useful practical test:
#
#     Can another programmer understand the comprehension immediately?
#
# If yes:
#
#     A comprehension is probably appropriate.
#
# If understanding it requires mentally unpacking several conditions,
# nested loops, function calls, or transformations:
#
#     A normal loop may be better.


numbers: list[int] = [1, 2, 3, 4, 5, 6]

simple_result: list[int] = [
    number**2
    for number in numbers
    if number % 2 == 0
]

print(simple_result)
# [4, 16, 36]


# This is easy to read:
#
#     square every even number.


# ---------------------------------------------------------------------------
# 13. Comprehension vs. Loop: General Comparison
# ---------------------------------------------------------------------------
#
# Comprehension:
#
#     - concise
#     - expressive
#     - excellent for simple transformations
#     - excellent for straightforward filtering
#     - naturally creates a collection
#
#
# Traditional loop:
#
#     - more verbose
#     - explicit control flow
#     - easier to debug step-by-step
#     - better for multiple branches
#     - better for multiple statements
#     - better for side effects
#     - often better for complex business logic
#
#
# Neither approach is universally better.
#
# Choose the form that communicates the intention most clearly.


# ---------------------------------------------------------------------------
# 14. Important Principle
# ---------------------------------------------------------------------------
#
# Do not write a comprehension simply because Python allows it.
#
# A comprehension should make collection construction clearer.
#
# Prefer:
#
#     result = [transform(item) for item in items]
#
# when the logic is simple.
#
# Prefer:
#
#     result = []
#
#     for item in items:
#         ...
#
# when the algorithm contains several steps or branches.
#
#
# The next file:
#
#     09_comprehension_best_practices.py
#
# focuses on practical guidelines for writing clean, maintainable
# comprehensions.

"""
numbers: list[int] = [2, 7, 12, 20]

result: list[str] = [
    "A" if number > 10
    else "B" if number > 5
    else "C"
    for number in numbers
]

print(result)
# ['C', 'B', 'A', 'A']


Conceptually:

if number > 10
    → "A"

else if number > 5
    → "B"

else
    → "C"
"""

