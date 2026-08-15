# type: ignore

"""
09_comprehension_best_practices.py

Presents best practices for writing clean and maintainable comprehensions
in Python.

This file focuses on:

    - Using comprehensions when they improve readability
    - Keeping comprehensions simple
    - Choosing descriptive variable names
    - Avoiding unnecessary nesting
    - Avoiding side effects
    - Avoiding overly complex expressions
    - Separating preprocessing from comprehension logic
    - Choosing loops when they communicate intent better
    - Understanding performance considerations
    - Avoiding unnecessary repeated calculations
    - Preserving static type clarity
    - Applying practical comprehension guidelines

This is the final file in the comprehensions section.
"""


# ---------------------------------------------------------------------------
# 1. Prefer Comprehensions for Simple Transformations
# ---------------------------------------------------------------------------
#
# A comprehension is a good choice when the operation is straightforward.


numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers: list[int] = [
    number**2
    for number in numbers
]

print(squared_numbers)
# [1, 4, 9, 16, 25]


# The intention is immediately clear:
#
#     "Create a list containing the square of every number."


# ---------------------------------------------------------------------------
# 2. Use Comprehensions for Simple Filtering
# ---------------------------------------------------------------------------


numbers: list[int] = list(range(1, 11))

even_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
# [2, 4, 6, 8, 10]


# This is concise without sacrificing readability.


# ---------------------------------------------------------------------------
# 3. Use Descriptive Variable Names
# ---------------------------------------------------------------------------
#
# Short variable names are acceptable when the context is obvious.
#
# However, meaningful names are preferable when the data has a specific
# meaning.


company_names: list[str] = [
    "Apple",
    "Google",
    "Microsoft",
]

company_name_lengths: list[int] = [
    len(company_name)
    for company_name in company_names
]

print(company_name_lengths)
# [5, 6, 9]


# Compare with:


companies: list[str] = [
    "Apple",
    "Google",
    "Microsoft",
]

lengths: list[int] = [
    len(x)
    for x in companies
]

print(lengths)
# [5, 6, 9]


# Both are valid.
#
# However, descriptive names become increasingly valuable as the logic
# becomes more complicated.


# ---------------------------------------------------------------------------
# 4. Avoid Unnecessary Nesting
# ---------------------------------------------------------------------------
#
# A nested comprehension can be useful for simple structures.


matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
]

flat_matrix: list[int] = [
    number
    for row in matrix
    for number in row
]

print(flat_matrix)
# [1, 2, 3, 4, 5, 6]


# This is still readable because the operation is simple.


# But deeply nested comprehensions can become difficult to understand.
#
# When multiple levels of nesting and conditions are involved,
# prefer a normal loop or separate the operation into smaller steps.


# ---------------------------------------------------------------------------
# 5. Avoid Side Effects
# ---------------------------------------------------------------------------
#
# Comprehensions should primarily be used to construct collections.
#
# Avoid using them only to execute an operation.


companies: list[str] = [
    "Apple",
    "Google",
    "Microsoft",
]


# Good:


uppercase_companies: list[str] = [
    company.upper()
    for company in companies
]

print(uppercase_companies)
# ['APPLE', 'GOOGLE', 'MICROSOFT']


# Avoid:
#
#     [print(company) for company in companies]
#
# The purpose of that comprehension is not to create a useful collection.
#
# Use a normal loop for side effects instead:
#
#     for company in companies:
#         print(company)


# ---------------------------------------------------------------------------
# 6. Do Not Force a Comprehension
# ---------------------------------------------------------------------------
#
# A comprehension is not automatically better just because it is shorter.


numbers: list[int] = [1, 2, 3, 4, 5]

processed_numbers: list[int] = []

for number in numbers:

    squared_number: int = number**2

    if squared_number > 10:

        adjusted_number: int = squared_number + 100

        processed_numbers.append(adjusted_number)

print(processed_numbers)
# [116, 125]


# A heavily compressed version would be harder to understand.
#
# The loop clearly communicates the multiple processing steps.
#
# Prefer clarity over cleverness.


# ---------------------------------------------------------------------------
# 7. Avoid Deeply Nested Conditional Expressions
# ---------------------------------------------------------------------------
#
# Python does allow nested conditional expressions:


numbers: list[int] = [2, 7, 12, 20]

number_categories: list[str] = [
    "Large" if number > 10
    else "Medium" if number > 5
    else "Small"
    for number in numbers
]

print(number_categories)
# ['Small', 'Medium', 'Large', 'Large']


# This works, but adding more branches would make the expression difficult
# to read.
#
# For several branches, use a normal loop:


number_categories_loop: list[str] = []

for number in numbers:

    if number > 10:
        number_categories_loop.append("Large")

    elif number > 5:
        number_categories_loop.append("Medium")

    else:
        number_categories_loop.append("Small")

print(number_categories_loop)
# ['Small', 'Medium', 'Large', 'Large']


# The loop is more readable here.


# ---------------------------------------------------------------------------
# 8. Separate Preprocessing from the Comprehension
# ---------------------------------------------------------------------------
#
# Avoid repeating expensive or complicated expressions inside a
# comprehension.


statement: str = (
    "Python Python SQL Java Python SQL"
)


import re


capitalized_clean_words: list[str] = [
    word.capitalize()
    for word in re.findall(r"\w+[']?\w+", statement)
]

print(capitalized_clean_words)
# ['Python', 'Python', 'Sql', 'Java', 'Python', 'Sql']


# Now the processed data can be reused:


unique_words: set[str] = {
    word
    for word in capitalized_clean_words
}

print(unique_words)
# {'Python', 'Sql', 'Java'}


# This is clearer than repeating the complete regular-expression
# processing operation inside multiple comprehensions.


# ---------------------------------------------------------------------------
# 9. Avoid Unnecessary Repeated Work
# ---------------------------------------------------------------------------
#
# Consider this word-frequency example:


word_count: dict[str, int] = {
    word: capitalized_clean_words.count(word)
    for word in capitalized_clean_words
}

print(word_count)


# This is a valid dictionary-comprehension exercise.
#
# However, count() scans the list each time it is called.
#
# For a large collection, a counting approach is more appropriate.


from collections import defaultdict


efficient_word_count: defaultdict[str, int] = defaultdict(int)

for word in capitalized_clean_words:
    efficient_word_count[word] += 1

print(efficient_word_count)


# The lesson:
#
#     A comprehension can be syntactically elegant
#     without necessarily being the most efficient algorithm.
#
# Always consider what the operations inside the comprehension actually do.


# ---------------------------------------------------------------------------
# 10. Prefer Built-in Operations When Appropriate
# ---------------------------------------------------------------------------
#
# Many transformations can be expressed naturally using comprehensions,
# but sometimes a dedicated built-in is clearer.


numbers: list[int] = [1, 2, 3, 4, 5]


# Comprehension:


string_numbers: list[str] = [
    str(number)
    for number in numbers
]

print(string_numbers)
# ['1', '2', '3', '4', '5']


# For simple transformations like this, the comprehension is perfectly
# readable.
#
# Depending on the surrounding context, map() could also express the
# operation:
#
#     map(str, numbers)
#
# The important principle is not "always use comprehensions".
#
# The important principle is:
#
#     Choose the clearest expression of the operation.


# ---------------------------------------------------------------------------
# 11. Preserve Type Clarity
# ---------------------------------------------------------------------------
#
# Type annotations should describe the resulting collection accurately.


numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers: list[int] = [
    number**2
    for number in numbers
]

print(squared_numbers)
# [1, 4, 9, 16, 25]


company_lengths: dict[str, int] = {
    company: len(company)
    for company in ["Apple", "Google", "Microsoft"]
}

print(company_lengths)
# {
#     'Apple': 5,
#     'Google': 6,
#     'Microsoft': 9
# }


unique_lengths: set[int] = {
    len(company)
    for company in ["Apple", "Google", "Microsoft"]
}

print(unique_lengths)
# {5, 6, 9}


# The annotation should match the actual collection:
#
#     list[int]
#     set[int]
#     dict[str, int]
#
# This makes the code easier to understand and keeps static type checkers
# useful.


# ---------------------------------------------------------------------------
# 12. Do Not Confuse Filtering with if/else
# ---------------------------------------------------------------------------
#
# Filtering:
#
#     [number for number in numbers if number % 2 == 0]
#
# removes values that do not satisfy the condition.
#
#
# Conditional value selection:
#
#     [
#         "Even" if number % 2 == 0 else "Odd"
#         for number in numbers
#     ]
#
# produces a value for every input item.


numbers: list[int] = [1, 2, 3, 4]

filtered_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

number_labels: list[str] = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(filtered_numbers)
# [2, 4]

print(number_labels)
# ['Odd', 'Even', 'Odd', 'Even']


# Choose the form that matches the intended behavior.


# ---------------------------------------------------------------------------
# 13. Use Parentheses and Formatting for Readability
# ---------------------------------------------------------------------------
#
# Long comprehensions should be formatted vertically rather than forced
# onto one line.


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


# Good formatting makes the structure visible:
#
#     {
#         key: value
#         for ...
#         if ...
#     }


# ---------------------------------------------------------------------------
# 14. Do Not Sacrifice Debuggability
# ---------------------------------------------------------------------------
#
# A normal loop allows intermediate values to be inspected easily.


numbers: list[int] = [1, 2, 3, 4, 5]

processed_numbers: list[int] = []

for number in numbers:

    squared_number: int = number**2

    print(f"number={number}, squared_number={squared_number}")

    if squared_number > 10:
        processed_numbers.append(squared_number)

print(processed_numbers)
# [16, 25]


# During debugging, this structure can be much easier to inspect than a
# complex comprehension.
#
# Once the logic is stable and simple, it may be possible to convert it
# into a comprehension if doing so improves readability.


# ---------------------------------------------------------------------------
# 15. Comprehension Decision Guide
# ---------------------------------------------------------------------------
#
# Prefer a comprehension when:
#
#     - You are creating a collection.
#     - The transformation is simple.
#     - The filtering condition is simple.
#     - The expression remains easy to read.
#     - The resulting code is clearer than the equivalent loop.
#
#
# Prefer a normal loop when:
#
#     - Multiple statements are required.
#     - There are several branches.
#     - There are many nested levels.
#     - Intermediate values need names.
#     - Debugging requires inspecting intermediate states.
#     - The loop exists primarily for side effects.
#     - The comprehension becomes difficult to understand.
#
#
# The goal is not:
#
#     "Use comprehensions everywhere."
#
# The goal is:
#
#     "Use comprehensions where they express collection construction
#      clearly and naturally."


# ---------------------------------------------------------------------------
# 16. Final Example
# ---------------------------------------------------------------------------
#
# A clean comprehension:


numbers: list[int] = list(range(1, 11))

squared_even_numbers: list[int] = [
    number**2
    for number in numbers
    if number % 2 == 0
]

print(squared_even_numbers)
# [4, 16, 36, 64, 100]


# This is a strong comprehension because:
#
#     - The input is obvious.
#     - The transformation is simple.
#     - The filtering condition is simple.
#     - There is only one level of iteration.
#     - The resulting collection is immediately understandable.


# ---------------------------------------------------------------------------
# 17. Final Principle
# ---------------------------------------------------------------------------
#
# A comprehension is good Python when it makes the code easier to read.
#
# A comprehension is bad Python when it makes the reader decode the code
# just to understand what it does.
#
#
# Remember:
#
#     Readability > cleverness
#
#     Clarity > unnecessary brevity
#
#     Correctness > clever syntax
#
#     Appropriate algorithm > forced comprehension
#
#
# This completes the comprehensions section.
