"""
==============================================================================
Python Copy Operations
==============================================================================

Module
------
Deep Copy

Overview
--------
A deep copy creates a new outer object and recursively creates independent
copies of the objects contained inside it.

For nested mutable objects, this means:

    • The outer object is independent.
    • Nested mutable objects are also independent.

Python provides `deepcopy()` through the `copy` module.

Key Concept
-----------
    copied_numbers = deepcopy(original_numbers)

This creates a completely independent copy of the original object and its
nested objects.

Therefore:

    original_numbers is copied_numbers

evaluates to False.

The nested objects are also independent:

    original_numbers[5] is copied_numbers[5]

evaluates to False.

References
----------
Python Official Documentation

https://docs.python.org/3/library/copy.html
"""

from copy import deepcopy
from typing import cast


# =============================================================================
# Example 1: Creating a Deep Copy
# =============================================================================

original_numbers: list[int | list[int]] = [
    1,
    2,
    3,
    4,
    5,
    [1, 2, 3]
]

copied_numbers: list[int | list[int]] = deepcopy(
    original_numbers
)


# =============================================================================
# Example 2: Outer Lists Are Different Objects
# =============================================================================

print(
    f"Original object ID: {id(original_numbers)}"
)

print(
    f"Copied object ID:   {id(copied_numbers)}"
)

print(
    f"Same outer object: "
    f"{original_numbers is copied_numbers}"
)


# =============================================================================
# Example 3: Nested Lists Are Also Different Objects
# =============================================================================

# The list contains both integers and a nested list, so mypy correctly
# considers original_numbers[5] to be `int | list[int]`.
#
# We know from the structure of this example that index 5 contains the
# nested list. `cast()` tells mypy to treat that value specifically as
# `list[int]` without changing the object at runtime.
original_nested_numbers: list[int] = cast(
    list[int],
    original_numbers[5]
)

copied_nested_numbers: list[int] = cast(
    list[int],
    copied_numbers[5]
)


print(
    f"Same nested object: "
    f"{original_nested_numbers is copied_nested_numbers}"
)


# =============================================================================
# Example 4: Modifying the Outer List
# =============================================================================

copied_numbers.append(6)


# The modification affects only the copied outer list.
print(
    f"Original list: {original_numbers}"
)

print(
    f"Copied list:   {copied_numbers}"
)


# =============================================================================
# Example 5: Modifying the Nested List
# =============================================================================

copied_nested_numbers[0] = 0


# The modification affects only the nested list inside the deep copy because
# the nested list was also independently copied.
print(
    f"Original list after nested modification: {original_numbers}"
)

print(
    f"Copied list after nested modification:   {copied_numbers}"
)


# =============================================================================
# Example 6: Deep Copy Structure
# =============================================================================

"""
The structure can be visualized as:

original_numbers ──────> [1, 2, 3, 4, 5, ──────> [1, 2, 3]]

copied_numbers ────────> [1, 2, 3, 4, 5, ──────> [0, 2, 3]]
                           │                       │
                           │                       │
                           ▼                       ▼
                      Outer copy              Nested copy

Both the outer list and the nested list are independent objects.

Therefore, modifying either level of the deep copy does not modify the
corresponding object in the original structure.
"""


# =============================================================================
# Example 7: Deep Copy Comparison
# =============================================================================

print(
    f"Outer objects are independent: "
    f"{original_numbers is not copied_numbers}"
)

print(
    f"Nested objects are independent: "
    f"{original_nested_numbers is not copied_nested_numbers}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `deepcopy()` creates a new outer object.

✓ `deepcopy()` recursively copies nested objects.

✓ The original and copied outer objects are independent.

✓ Nested mutable objects are also independent.

✓ Changes to the outer object do not affect the original object.

✓ Changes to nested mutable objects do not affect the original nested object.

✓ `cast()` only informs the static type checker about the expected type.

✓ `cast()` does not perform a runtime conversion or create a new object.

✓ Deep copying is useful when a completely independent object structure is
  required.
"""


# =============================================================================
# End of File
# =============================================================================