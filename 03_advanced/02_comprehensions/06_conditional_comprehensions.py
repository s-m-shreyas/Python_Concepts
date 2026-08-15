# type: ignore
"""
06_conditional_comprehensions.py

Introduces conditional comprehensions in Python.

This file focuses on:

    - Filtering values with if conditions
    - Using if conditions with list comprehensions
    - Using if conditions with set comprehensions
    - Using if conditions with dictionary comprehensions
    - Using if-else expressions inside comprehensions
    - Understanding the difference between filtering and value selection
    - Combining transformation and filtering
    - Using multiple conditions
    - Understanding conditional comprehension syntax
    - Comparing conditional comprehensions with equivalent for loops

The following topics are covered separately:

    07_nested_comprehensions.py
    08_comprehension_vs_loop.py
    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Conditional List Comprehension - Filtering
# ---------------------------------------------------------------------------
#
# Syntax:
#
#     [expression for item in iterable if condition]
#
# The if condition at the end filters items.
#
# Only items for which the condition is True are included in the result.


numbers: list[int] = [1, 2, 3, 4, 5, 6]

even_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
# [2, 4, 6]


# ---------------------------------------------------------------------------
# 2. Conditional Transformation
# ---------------------------------------------------------------------------
#
# The expression and the condition have different responsibilities:
#
#     expression -> determines WHAT goes into the result
#     condition  -> determines WHETHER the item is included


numbers: list[int] = [1, 2, 3, 4, 5, 6]

squared_even_numbers: list[int] = [
    number**2
    for number in numbers
    if number % 2 == 0
]

print(squared_even_numbers)
# [4, 16, 36]


# ---------------------------------------------------------------------------
# 3. Filtering Strings
# ---------------------------------------------------------------------------

languages: list[str] = [
    "Python",
    "Perl",
    "Java",
    "php",
    "C++",
]

P_filtered_string_list: list[str] = [
    language
    for language in languages
    if language.capitalize().startswith("P")
]

print(P_filtered_string_list)
# ['Python', 'Perl', 'php']


# The condition decides whether the original string is included.
#
# No alternative value is produced for strings that fail the condition.


# ---------------------------------------------------------------------------
# 4. Filtering with isinstance()
# ---------------------------------------------------------------------------
#
# isinstance() can be used when a collection contains multiple data types.


mixed_values: list[object] = [
    "Shreyas",
    10,
    11.4,
    "Pranay",
    3 + 8j,
    ["xyz"],
]

string_values: list[str] = [
    item
    for item in mixed_values
    if isinstance(item, str)
]

print(string_values)
# ['Shreyas', 'Pranay']


# ---------------------------------------------------------------------------
# 5. Conditional Set Comprehension
# ---------------------------------------------------------------------------
#
# Set comprehension syntax:
#
#     {expression for item in iterable if condition}
#
# The condition filters the values.
# The resulting set also automatically removes duplicates.


numbers: list[int] = [
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    5,
]

even_number_set: set[int] = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_number_set)
# {2, 4}


# ---------------------------------------------------------------------------
# 6. Conditional Dictionary Comprehension
# ---------------------------------------------------------------------------
#
# Dictionary comprehension syntax:
#
#     {key: value for item in iterable if condition}


numbers: list[int] = [1, 2, 3, 4, 5, 6]

squared_even_number_dict: dict[int, int] = {
    number: number**2
    for number in numbers
    if number % 2 == 0
}

print(squared_even_number_dict)
# {2: 4, 4: 16, 6: 36}


# ---------------------------------------------------------------------------
# 7. Conditional Dictionary Transformation
# ---------------------------------------------------------------------------

employee_salaries: dict[str, int] = {
    "Alice": 50000,
    "Bob": 75000,
    "Charlie": 60000,
    "David": 90000,
}

high_salary_employees: dict[str, int] = {
    employee: salary
    for employee, salary in employee_salaries.items()
    if salary >= 70000
}

print(high_salary_employees)
# {
#     'Bob': 75000,
#     'David': 90000
# }


# ---------------------------------------------------------------------------
# 8. Multiple Conditions
# ---------------------------------------------------------------------------
#
# Multiple conditions can be chained using and/or.


numbers: list[int] = list(range(1, 21))

numbers_between_5_and_15: list[int] = [
    number
    for number in numbers
    if number >= 5 and number <= 15
]

print(numbers_between_5_and_15)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# The same condition can be written more naturally as:


numbers_between_5_and_15: list[int] = [
    number
    for number in numbers
    if 5 <= number <= 15
]

print(numbers_between_5_and_15)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# ---------------------------------------------------------------------------
# 9. Multiple Filtering Conditions
# ---------------------------------------------------------------------------

numbers: list[int] = list(range(1, 21))

even_numbers_greater_than_10: list[int] = [
    number
    for number in numbers
    if number > 10 and number % 2 == 0
]

print(even_numbers_greater_than_10)
# [12, 14, 16, 18, 20]


# ---------------------------------------------------------------------------
# 10. Filtering with a Function Call
# ---------------------------------------------------------------------------

words: list[str] = [
    "python",
    "sql",
    "spark",
    "go",
    "airflow",
]

long_words: list[str] = [
    word
    for word in words
    if len(word) > 3
]

print(long_words)
# ['python', 'spark', 'airflow']


# ---------------------------------------------------------------------------
# 11. Filtering and Transformation Together
# ---------------------------------------------------------------------------
#
# The expression can transform a value while the condition filters it.


numbers: list[int] = list(range(1, 11))

even_number_labels: list[str] = [
    f"Even: {number}"
    for number in numbers
    if number % 2 == 0
]

print(even_number_labels)
# ['Even: 2', 'Even: 4', 'Even: 6', 'Even: 8', 'Even: 10']


# ---------------------------------------------------------------------------
# 12. Filtering vs. if-else
# ---------------------------------------------------------------------------
#
# These two forms solve different problems.
#
#
# Filtering:
#
#     [number for number in numbers if number % 2 == 0]
#
# Result:
#
#     [2, 4, 6]
#
# Odd numbers are completely excluded.
#
#
# if-else:
#
#     [
#         "Even" if number % 2 == 0 else "Odd"
#         for number in numbers
#     ]
#
# Result:
#
#     ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
#
# Every number produces a result.


numbers: list[int] = [1, 2, 3, 4, 5, 6]

even_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

number_types: list[str] = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(even_numbers)
# [2, 4, 6]

print(number_types)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


# ---------------------------------------------------------------------------
# 13. Conditional Expression vs. Filtering Condition
# ---------------------------------------------------------------------------
#
# The position of the if keyword changes its meaning.
#
#
# Filtering:
#
#     [expression for item in iterable if condition]
#
# The if comes AFTER the for clause.
#
#
# Conditional expression:
#
#     [value_if_true if condition else value_if_false
#      for item in iterable]
#
# The if/else comes BEFORE the for clause.


numbers: list[int] = [1, 2, 3, 4]

filtered_result: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

conditional_result: list[str] = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(filtered_result)
# [2, 4]

print(conditional_result)
# ['Odd', 'Even', 'Odd', 'Even']


# ---------------------------------------------------------------------------
# 14. Conditional Dictionary Comprehension with Transformation
# ---------------------------------------------------------------------------

employee_salaries: dict[str, int] = {
    "Alice": 50000,
    "Bob": 75000,
    "Charlie": 60000,
    "David": 90000,
}

salary_increase: dict[str, int] = {
    employee: salary + 5000
    for employee, salary in employee_salaries.items()
    if salary < 70000
}

print(salary_increase)
# {
#     'Alice': 55000,
#     'Charlie': 65000
# }


# ---------------------------------------------------------------------------
# 15. Equivalent Traditional for Loop
# ---------------------------------------------------------------------------
#
# Conditional comprehensions are concise representations of ordinary loops.


numbers: list[int] = [1, 2, 3, 4, 5, 6]

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
# [2, 4, 6]

print(even_numbers_loop)
# [2, 4, 6]


# ---------------------------------------------------------------------------
# 16. Conditional Dictionary Comprehension vs. for Loop
# ---------------------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4, 5]

squared_even_numbers_comprehension: dict[int, int] = {
    number: number**2
    for number in numbers
    if number % 2 == 0
}

squared_even_numbers_loop: dict[int, int] = {}

for number in numbers:
    if number % 2 == 0:
        squared_even_numbers_loop[number] = number**2

print(squared_even_numbers_comprehension)
# {2: 4, 4: 16}

print(squared_even_numbers_loop)
# {2: 4, 4: 16}


# ---------------------------------------------------------------------------
# 17. General Syntax Summary
# ---------------------------------------------------------------------------
#
# List filtering:
#
#     [expression for item in iterable if condition]
#
#
# Set filtering:
#
#     {expression for item in iterable if condition}
#
#
# Dictionary filtering:
#
#     {key: value for item in iterable if condition}
#
#
# Conditional value selection:
#
#     [
#         value_if_true if condition else value_if_false
#         for item in iterable
#     ]
#
#
# The important distinction:
#
#     if at the END
#         -> filters items
#
#     if/else BEFORE the for
#         -> chooses the value produced
#
#
# Complex nested conditions and nested comprehensions are covered separately
# to keep each concept focused.
"""
┌─────────────────────────────────────────────┐
│                 FILTERING                   │
│                                             │
│ [expression for item in iterable if cond]  │
│                                             │
│ "Should this item be included?"             │
└─────────────────────────────────────────────┘

┌──────────────────────────────────────────────────┐
│              VALUE SELECTION                     │
│                                                  │
│ [A if condition else B for item in iterable]   │
│                                                  │
│ "What value should this item produce?"           │
└──────────────────────────────────────────────────┘
"""