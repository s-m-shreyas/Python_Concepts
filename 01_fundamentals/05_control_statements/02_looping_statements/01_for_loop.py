"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
For Loop

Overview
--------
The `for` loop is Python's primary iteration construct used to traverse
iterable objects such as strings, lists, tuples, dictionaries, sets, and
many other iterable types.

Unlike some programming languages that rely heavily on index-based loops,
Python directly iterates over the elements of an iterable, resulting in
cleaner, safer, and more readable code.

Syntax
------
for variable in iterable:
    statement(s)

Flow
----
Iterable
    │
    ▼
Retrieve Next Element
    │
    ▼
Assign to Loop Variable
    │
    ▼
Execute Loop Body
    │
    ▼
More Elements?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
 ▼      ▼
Repeat  Exit Loop

Characteristics
---------------
• Iterates over iterable objects.
• Automatically retrieves each element.
• Eliminates manual index management.
• Improves code readability.
• Commonly used for collection traversal.

Time Complexity
---------------
O(n)

where n is the number of elements in the iterable.

Supported Iterables
-------------------
• Strings
• Lists
• Tuples
• Sets
• Dictionaries
• range()

Common Use Cases
----------------
• Traversing collections
• Processing datasets
• Displaying records
• Data validation
• Searching
• Aggregation

Best Practices
--------------
• Prefer direct iteration over manual indexing.
• Use meaningful loop variable names.
• Keep loop bodies concise.
• Avoid modifying collections while iterating over them.

References
----------
Python Official Documentation
https://docs.python.org/3/tutorial/controlflow.html#for-statements
"""


# =============================================================================
# Example 1
# Iterate Over a List
# =============================================================================

programming_languages: list[str] = [
    "Python",
    "Java",
    "Go",
    "Rust"
]

for programming_language in programming_languages:
    print(f"Programming Language -> {programming_language}")


# =============================================================================
# Example 2
# Iterate Over a Tuple
# =============================================================================

rgb_color: tuple[int, int, int] = (
    255,
    128,
    64
)

for color_value in rgb_color:
    print(f"RGB Value -> {color_value}")


# =============================================================================
# Example 3
# Iterate Over a String
# =============================================================================

course_name: str = "Python"

for character in course_name:
    print(f"Character -> {character}")


# =============================================================================
# Example 4
# Iterate Over a Set
# =============================================================================

unique_numbers: set[int] = {
    10,
    20,
    30,
    40
}

for unique_number in unique_numbers:
    print(f"Unique Number -> {unique_number}")


# =============================================================================
# Example 5
# Iterate Over Dictionary Keys
# =============================================================================

student_marks: dict[str, int] = {
    "Alice": 91,
    "Bob": 84,
    "Charlie": 96
}

for student_name in student_marks:
    print(f"Student -> {student_name}")


# =============================================================================
# Example 6
# Iterate Over Dictionary Values
# =============================================================================

for marks in student_marks.values():
    print(f"Marks -> {marks}")


# =============================================================================
# Example 7
# Iterate Over Dictionary Items
# =============================================================================

for student_name, marks in student_marks.items():
    print(f"{student_name} -> {marks}")


# =============================================================================
# Example 8
# Iterate Using range()
# =============================================================================

for number in range(1, 6):
    print(f"Number -> {number}")


# =============================================================================
# End of Module
# =============================================================================