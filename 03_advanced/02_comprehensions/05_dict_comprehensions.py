# type: ignore
"""
05_dict_comprehensions.py

Introduces dictionary comprehensions in Python.

This file focuses on:

    - What a dictionary comprehension is
    - The basic dictionary comprehension syntax
    - Creating key-value pairs with comprehensions
    - Transforming existing dictionaries
    - Using expressions for keys and values
    - Using enumerate() with dictionary comprehensions
    - Using zip() with dictionary comprehensions
    - Creating dictionaries from sequences
    - Inverting simple key-value mappings
    - Understanding duplicate-key behavior
    - Counting word frequencies
    - Using functions inside dictionary comprehensions
    - Comparing dictionary comprehensions with traditional for loops
    - Using defaultdict for frequency counting

The following topics are covered separately:

    06_conditional_comprehensions.py
    07_nested_comprehensions.py
    08_comprehension_vs_loop.py
    09_comprehension_best_practices.py
"""


# ---------------------------------------------------------------------------
# 1. Basic Dictionary Comprehension
# ---------------------------------------------------------------------------
#
# Basic syntax:
#
#     {key: value for item in iterable}
#
# Unlike a list comprehension:
#
#     [expression for item in iterable]
#
# a dictionary comprehension produces both a key and a value.


numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers: dict[int, int] = {
    number: number**2
    for number in numbers
}

print(squared_numbers)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ---------------------------------------------------------------------------
# 2. Understanding Key and Value Expressions
# ---------------------------------------------------------------------------
#
# In:
#
#     {number: number**2 for number in numbers}
#
# the first expression:
#
#     number
#
# becomes the key.
#
# The second expression:
#
#     number**2
#
# becomes the value.


numbers: list[int] = [1, 2, 3, 4]

number_labels: dict[int, str] = {
    number: f"Number {number}"
    for number in numbers
}

print(number_labels)
# {
#     1: 'Number 1',
#     2: 'Number 2',
#     3: 'Number 3',
#     4: 'Number 4'
# }


# ---------------------------------------------------------------------------
# 3. Creating a Dictionary from a List of Strings
# ---------------------------------------------------------------------------

companies: list[str] = [
    "apple",
    "google",
    "microsoft",
    "amazon",
]

company_lengths: dict[str, int] = {
    company: len(company)
    for company in companies
}

print(company_lengths)
# {
#     'apple': 5,
#     'google': 6,
#     'microsoft': 9,
#     'amazon': 6
# }


# ---------------------------------------------------------------------------
# 4. Using enumerate() with Dictionary Comprehensions
# ---------------------------------------------------------------------------
#
# enumerate() provides both an index and an item.


languages: list[str] = [
    "Python",
    "SQL",
    "Java",
    "C++",
]

numbered_languages: dict[int, str] = {
    index: language
    for index, language in enumerate(languages, start=1)
}

print(numbered_languages)
# {
#     1: 'Python',
#     2: 'SQL',
#     3: 'Java',
#     4: 'C++'
# }


# ---------------------------------------------------------------------------
# 5. Using zip() with Dictionary Comprehensions
# ---------------------------------------------------------------------------
#
# zip() can combine two related sequences.


first_names: list[str] = [
    "Shreyas",
    "Pranay",
    "Rajeshwari",
]

ages: list[int] = [
    29,
    28,
    27,
]

name_age_mapping: dict[str, int] = {
    name: age
    for name, age in zip(first_names, ages)
}

print(name_age_mapping)
# {
#     'Shreyas': 29,
#     'Pranay': 28,
#     'Rajeshwari': 27
# }


# ---------------------------------------------------------------------------
# 6. Transforming an Existing Dictionary
# ---------------------------------------------------------------------------


employee_salaries: dict[str, int] = {
    "Alice": 50000,
    "Bob": 60000,
    "Charlie": 70000,
}

updated_salaries: dict[str, int] = {
    employee: salary + 5000
    for employee, salary in employee_salaries.items()
}

print(updated_salaries)
# {
#     'Alice': 55000,
#     'Bob': 65000,
#     'Charlie': 75000
# }


# ---------------------------------------------------------------------------
# 7. Transforming Both Keys and Values
# ---------------------------------------------------------------------------


company_codes: dict[str, int] = {
    "apple": 101,
    "google": 102,
    "amazon": 103,
}

transformed_company_codes: dict[str, int] = {
    company.upper(): code + 1000
    for company, code in company_codes.items()
}

print(transformed_company_codes)
# {
#     'APPLE': 1101,
#     'GOOGLE': 1102,
#     'AMAZON': 1103
# }


# ---------------------------------------------------------------------------
# 8. Inverting a Dictionary
# ---------------------------------------------------------------------------
#
# When the original values are unique and hashable, a dictionary can be
# inverted by making the original values the new keys.


country_codes: dict[str, str] = {
    "India": "IN",
    "United States": "US",
    "Japan": "JP",
    "Germany": "DE",
}

inverted_country_codes: dict[str, str] = {
    code: country
    for country, code in country_codes.items()
}

print(inverted_country_codes)
# {
#     'IN': 'India',
#     'US': 'United States',
#     'JP': 'Japan',
#     'DE': 'Germany'
# }


# ---------------------------------------------------------------------------
# 9. Duplicate-Key Behavior
# ---------------------------------------------------------------------------
#
# Dictionary keys must be unique.
#
# If a dictionary comprehension produces the same key more than once,
# the later value replaces the earlier value.


words: list[str] = [
    "apple",
    "ant",
    "banana",
]

first_letter_mapping: dict[str, str] = {
    word[0]: word
    for word in words
}

print(first_letter_mapping)
# {'a': 'ant', 'b': 'banana'}


# Both "apple" and "ant" produce the key "a".
#
# The later value:
#
#     'ant'
#
# replaces:
#
#     'apple'


# ---------------------------------------------------------------------------
# 10. Creating a Dictionary from Two Lists
# ---------------------------------------------------------------------------

subjects: list[str] = [
    "Python",
    "SQL",
    "Spark",
]

ratings: list[int] = [
    9,
    8,
    7,
]

subject_ratings: dict[str, int] = {
    subject: rating
    for subject, rating in zip(subjects, ratings)
}

print(subject_ratings)
# {
#     'Python': 9,
#     'SQL': 8,
#     'Spark': 7
# }


# ---------------------------------------------------------------------------
# 11. Dictionary Comprehension with a Function Call
# ---------------------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4, 5]

factorials: dict[int, int] = {
    number: __import__("math").factorial(number)
    for number in numbers
}

print(factorials)
# {
#     1: 1,
#     2: 2,
#     3: 6,
#     4: 24,
#     5: 120
# }


# The expression can contain normal function calls.
#
# In production code, a normal import is clearer:
#
#     import math
#
#     factorials = {
#         number: math.factorial(number)
#         for number in numbers
#     }


# ---------------------------------------------------------------------------
# 12. Word Frequency with Dictionary Comprehension
# ---------------------------------------------------------------------------
#
# A dictionary comprehension can calculate a value for every generated key.
#
# Here:
#
#     key   -> word
#     value -> number of occurrences of that word
#
# The words are normalized with capitalize() before counting.


import re


statement: str = (
    "You are most welcome. And honestly, thank you for correcting me so "
    "sharply—that wasn't just a casual catch. In Vedic astrology, when a "
    "person accurately spots an astrological error like that, it is a clear "
    "sign that their 3rd house (intellect and discernment) and Ketu "
    "(intuition) are highly active and protective. Your dream-self saved "
    "that kitten, and your waking-self just saved yourself from a bad "
    "remedy. You are clearly in tune with your own energy."
)


capitalized_clean_words: list[str] = [
    word.capitalize()
    for word in re.findall(r"\w+[']?\w+", statement)
]


# Version 1:
# Dictionary comprehension.


word_count: dict[str, int] = {
    word: capitalized_clean_words.count(word)
    for word in capitalized_clean_words
}

print(word_count)


# The comprehension is concise, but list.count() scans the entire list
# every time a word is processed.
#
# Therefore, this approach can perform unnecessary repeated work when
# the input becomes large.


# ---------------------------------------------------------------------------
# 13. Word Frequency with a Traditional for Loop
# ---------------------------------------------------------------------------
#
# The same problem can be solved explicitly using a dictionary.
#
# For every word:
#
#     1. Check whether the word already exists.
#     2. If it exists, increment its count.
#     3. Otherwise, create the key with a count of 1.


word_count_2: dict[str, int] = {}

for word in capitalized_clean_words:

    if word in word_count_2:
        word_count_2[word] += 1
    else:
        word_count_2[word] = 1

print(word_count_2)


# This approach avoids repeatedly scanning the complete list.
#
# Dictionary membership testing is efficient on average because dictionaries
# are hash-table based.


# ---------------------------------------------------------------------------
# 14. Word Frequency with defaultdict
# ---------------------------------------------------------------------------
#
# defaultdict automatically creates a default value when a key does not
# already exist.
#
# defaultdict(int) means:
#
#     missing key -> int() -> 0
#
# Therefore:
#
#     word_count_3[word] += 1
#
# works even when the word has not been encountered before.


from collections import defaultdict


word_count_3: defaultdict[str, int] = defaultdict(int)

for word in capitalized_clean_words:
    word_count_3[word] += 1

print(word_count_3)


# The resulting object is a defaultdict rather than a normal dict.
#
# It can be converted into a normal dictionary when required:
#
#     normal_word_count: dict[str, int] = dict(word_count_3)


# ---------------------------------------------------------------------------
# 15. Equivalent Traditional for Loop
# ---------------------------------------------------------------------------


numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers_comprehension: dict[int, int] = {
    number: number**2
    for number in numbers
}

squared_numbers_loop: dict[int, int] = {}

for number in numbers:
    squared_numbers_loop[number] = number**2

print(squared_numbers_comprehension)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squared_numbers_loop)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ---------------------------------------------------------------------------
# 16. Dictionary Comprehension Mental Model
# ---------------------------------------------------------------------------
#
# A dictionary comprehension:
#
#     {key_expression: value_expression for item in iterable}
#
# can be read as:
#
#     "For every item in the iterable,
#      calculate a key,
#      calculate a value,
#      and store the key-value pair in the resulting dictionary."
#
#
# Compare:
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
#
# The colon ':' separates the key expression from the value expression
# in a dictionary comprehension.