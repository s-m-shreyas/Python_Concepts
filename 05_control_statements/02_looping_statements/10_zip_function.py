"""
==============================================================================
Python Looping Statements
==============================================================================

Module
------
zip() Function

Overview
--------
The `zip()` function combines multiple iterables into a single iterator that
produces tuples containing corresponding elements from each iterable.

Iteration stops as soon as the shortest iterable is exhausted.

The `zip()` function is commonly used when processing related collections
simultaneously.

Syntax
------
zip(iterable1, iterable2)

zip(iterable1, iterable2, iterable3, ...)

Flow
----
Iterable 1
      │
Iterable 2
      │
Iterable 3
      │
      ▼
Pair Corresponding Elements
      │
      ▼
Return Tuple
      │
      ▼
Next Iteration

Characteristics
---------------
• Combines multiple iterables.
• Returns a zip object.
• Produces tuples.
• Stops at the shortest iterable.
• Memory efficient (lazy evaluation).

Time Complexity
---------------
Creating a zip object:
O(1)

Iterating through n elements:
O(n)

where n is the length of the shortest iterable.

Common Use Cases
----------------
• Combining related data.
• Iterating through multiple lists.
• Creating dictionaries.
• Matrix operations.
• Data processing.

Best Practices
--------------
• Use zip() instead of manually indexing multiple lists.
• Ensure iterables have matching lengths when appropriate.
• Convert the zip object to a list only when necessary.

Common Mistakes
---------------
• Forgetting that zip() returns an iterator.
• Assuming iteration continues until the longest iterable.
• Forgetting to unpack tuples while iterating.

References
----------
Python Official Documentation

https://docs.python.org/3/library/functions.html#zip
"""


# =============================================================================
# Example 1: Basic zip()
# =============================================================================

student_names: list[str] = [
    "Alice",
    "Bob",
    "Charlie"
]

student_marks: list[int] = [
    91,
    85,
    96
]

for current_student_name, current_student_mark in zip(
    student_names,
    student_marks
):

    print(
        f"{current_student_name}"
        f" -> {current_student_mark}"
    )


# =============================================================================
# Example 2: Three Iterables
# =============================================================================

employee_names: list[str] = [
    "John",
    "Emma",
    "David"
]

employee_departments: list[str] = [
    "HR",
    "IT",
    "Finance"
]

employee_salaries: list[int] = [
    55_000,
    72_000,
    68_000
]

for (
    employee_name,
    employee_department,
    employee_salary
) in zip(
    employee_names,
    employee_departments,
    employee_salaries
):

    print(
        f"{employee_name}"
        f" | {employee_department}"
        f" | ₹{employee_salary}"
    )


# =============================================================================
# Example 3: Different Length Iterables
# =============================================================================

fruit_names: list[str] = [
    "Apple",
    "Orange",
    "Mango",
    "Banana"
]

fruit_prices: list[int] = [
    120,
    90
]

for fruit_name, fruit_price in zip(
    fruit_names,
    fruit_prices
):

    print(
        f"{fruit_name}"
        f" -> ₹{fruit_price}"
    )

print("Iteration stopped at the shortest iterable.")


# =============================================================================
# Example 4: Creating a Dictionary
# =============================================================================

country_names: list[str] = [
    "India",
    "Japan",
    "Canada"
]

country_capitals: list[str] = [
    "New Delhi",
    "Tokyo",
    "Ottawa"
]

country_dictionary: dict[str, str] = dict(
    zip(
        country_names,
        country_capitals
    )
)

print(country_dictionary)


# =============================================================================
# Example 5: zip() Object
# =============================================================================

subject_names: list[str] = [
    "Math",
    "Science",
    "English"
]

subject_scores: list[int] = [
    95,
    88,
    91
]

subject_zip_object = zip(
    subject_names,
    subject_scores
)

print(subject_zip_object)

print(list(subject_zip_object))


# =============================================================================
# Example 6: Unzipping Data
# =============================================================================

city_information: list[tuple[str, int]] = [
    ("Bengaluru", 13),
    ("Mysuru", 9),
    ("Hubballi", 7)
]

city_names, city_populations = zip(
    *city_information
)

print(city_names)

print(city_populations)


# =============================================================================
# Example 7: Parallel Iteration
# =============================================================================

product_names: list[str] = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

product_quantities: list[int] = [
    5,
    18,
    12
]

for product_name, product_quantity in zip(
    product_names,
    product_quantities
):

    print(
        f"{product_name}"
        f" -> Quantity: {product_quantity}"
    )


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ zip() combines multiple iterables.

✓ It returns a zip object.

✓ Corresponding elements are grouped into tuples.

✓ Iteration stops at the shortest iterable.

✓ zip() is commonly used for parallel iteration.

✓ zip() can be used to create dictionaries.

✓ The unpacking operator (*) can be used to unzip data.
"""


# =============================================================================
# End of File
# =============================================================================