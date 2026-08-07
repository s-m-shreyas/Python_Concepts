"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
enumerate() Function

Overview
--------
The `enumerate()` function adds a counter to an iterable and returns an
enumerate object.

It is commonly used when both the index and the corresponding value are
required during iteration.

Using `enumerate()` is generally preferred over manually maintaining an
index variable because it produces cleaner and more readable code.

Syntax
------
enumerate(iterable)

enumerate(iterable, start)

Flow
----
Iterable
    │
    ▼
Add Counter
    │
    ▼
Return (index, value)
    │
    ▼
Next Iteration

Characteristics
---------------
• Returns an enumerate object.
• Produces index-value pairs.
• Supports a custom starting index.
• Improves readability over manual indexing.
• Frequently used with for loops.

Time Complexity
---------------
Creating an enumerate object:
O(1)

Iterating through n elements:
O(n)

Common Use Cases
----------------
• Displaying serial numbers.
• Processing indexed data.
• Printing menus.
• Reading files line by line.
• Reporting positions of values.

Best Practices
--------------
• Prefer enumerate() over manually incrementing counters.
• Use descriptive variable names for index and value.
• Use the start parameter when numbering should begin from a value other
  than zero.

Common Mistakes
---------------
• Forgetting that enumerate returns (index, value).
• Confusing enumerate() with range().
• Using manual counters instead of enumerate().

References
----------
Python Official Documentation

https://docs.python.org/3/library/functions.html#enumerate
"""


# =============================================================================
# Example 1: Basic enumerate()
# =============================================================================

programming_languages: list[str] = [
    "Python",
    "Java",
    "C++"
]

for language_index, programming_language in enumerate(programming_languages):

    print(
        f"Index: {language_index}"
        f" -> Language: {programming_language}"
    )


# =============================================================================
# Example 2: Custom Starting Index
# =============================================================================

employee_names: list[str] = [
    "Alice",
    "Bob",
    "Charlie"
]

SERIAL_NUMBER_START: int = 1

for employee_serial_number, employee_name in enumerate(
    employee_names,
    start=SERIAL_NUMBER_START
):

    print(
        f"{employee_serial_number}. "
        f"{employee_name}"
    )


# =============================================================================
# Example 3: Student Marks Report
# =============================================================================

student_marks: list[int] = [
    91,
    86,
    95,
    88
]

REPORT_START_NUMBER: int = 1

for student_number, student_mark in enumerate(
    student_marks,
    start=REPORT_START_NUMBER
):

    print(
        f"Student {student_number}"
        f" -> Marks: {student_mark}"
    )


# =============================================================================
# Example 4: Finding the Position of an Item
# =============================================================================

fruit_names: list[str] = [
    "Apple",
    "Orange",
    "Mango",
    "Banana"
]

SEARCH_FRUIT: str = "Mango"

for fruit_position, fruit_name in enumerate(fruit_names):

    if fruit_name == SEARCH_FRUIT:

        print(
            f"{SEARCH_FRUIT}"
            f" found at index {fruit_position}."
        )

        break


# =============================================================================
# Example 5: Menu Display
# =============================================================================

menu_options: list[str] = [
    "View Profile",
    "Settings",
    "Logout"
]

MENU_START_NUMBER: int = 1

for menu_number, menu_option in enumerate(
    menu_options,
    start=MENU_START_NUMBER
):

    print(
        f"{menu_number}. "
        f"{menu_option}"
    )


# =============================================================================
# Example 6: Reading Characters with Positions
# =============================================================================

sample_word: str = "Python"

for character_position, current_character in enumerate(sample_word):

    print(
        f"Position: {character_position}"
        f" -> Character: {current_character}"
    )


# =============================================================================
# Example 7: enumerate() Object
# =============================================================================

city_names: list[str] = [
    "Bengaluru",
    "Mysuru",
    "Hubballi"
]

city_enumerator = enumerate(city_names)

print(city_enumerator)

print(list(city_enumerator))


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ enumerate() returns index-value pairs.

✓ It eliminates the need for manual counters.

✓ Supports a custom starting index.

✓ Improves readability and maintainability.

✓ Commonly used with for loops.

✓ Returns an enumerate object, not a list.
"""


# =============================================================================
# End of File
# =============================================================================