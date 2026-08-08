"""
==============================================================================
Python Copy Operations
==============================================================================

Module
------
Shallow Copy

Overview
--------
A shallow copy creates a new outer object while keeping references to the
objects contained inside it.

For a nested mutable object, this means:

    • The outer object is independent.
    • Nested mutable objects are still shared.

Python provides several ways to create a shallow copy. The `copy()` method
used in this module creates a new list containing references to the original
list's elements.

Key Concept
-----------
    copied_numbers = original_numbers.copy()

This creates a new outer list object.

Therefore:

    original_numbers is copied_numbers

evaluates to False.

However, if the original list contains another mutable object such as a
nested list, both outer lists can still contain a reference to that same
nested object.

References
----------
Python Official Documentation

https://docs.python.org/3/library/copy.html
"""

from typing import cast


# =============================================================================
# Example 1: Creating a Shallow Copy
# =============================================================================

original_numbers: list[int | list[int]] = [
    1,
    2,
    3,
    4,
    5,
    [1, 2, 3]
]

copied_numbers: list[int | list[int]] = original_numbers.copy()


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
# Example 3: Modifying the Outer List
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
# Example 4: Nested Objects Are Still Shared
# =============================================================================

# The list contains both integers and a nested list, so mypy correctly
# considers original_numbers[5] to be `int | list[int]`.
#
# We know from the structure of this example that index 5 contains the
# nested list. `cast()` tells mypy to treat that value specifically as
# `list[int]` without changing the object at runtime.
nested_original: list[int] = cast(
    list[int],
    original_numbers[5]
)

nested_copied: list[int] = cast(
    list[int],
    copied_numbers[5]
)


print(
    f"Same nested object: "
    f"{nested_original is nested_copied}"
)


# =============================================================================
# Example 5: Modifying the Shared Nested Object
# =============================================================================

nested_copied[0] = 0


# The nested modification is visible through both outer lists because both
# outer lists contain a reference to the same nested list.
print(
    f"Original list after nested modification: {original_numbers}"
)

print(
    f"Copied list after nested modification:   {copied_numbers}"
)


# =============================================================================
# Example 6: Shallow Copy Structure
# =============================================================================

"""
The structure can be visualized as:

original_numbers ──────> [1, 2, 3, 4, 5, ──────┐
                         ]                        │
                                                  ▼
                                            [0, 2, 3]
                                                  ▲
copied_numbers ────────> [1, 2, 3, 4, 5, ───────┘
                         6]

The outer lists are different objects.

The nested list is the same object in both outer lists.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A shallow copy creates a new outer object.

✓ `list.copy()` creates a shallow copy of a list.

✓ The original and copied outer lists have different identities.

✓ Changes to the outer list do not affect the other outer list.

✓ Nested mutable objects are still shared.

✓ Changes to a shared nested object affect both outer lists.

✓ `cast()` can be used when the programmer knows a more specific type than
  static type inference can determine.

✓ `cast()` does not perform a runtime conversion or create a new object.

✓ Shallow copying is suitable when nested objects do not need to be
  independently copied.
"""


# =============================================================================
# End of File
# =============================================================================