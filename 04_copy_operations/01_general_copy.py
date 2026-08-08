"""
==============================================================================
Python Copy Operations
==============================================================================

Module
------
General Copy

Overview
--------
In Python, assigning one variable to another does not create a new copy of
the object.

Instead, both variables refer to the same object in memory.

This behavior is particularly important when working with mutable objects
such as lists, dictionaries, and sets.

Understanding object references is the foundation for understanding shallow
copying and deep copying.

Key Concept
-----------
Assignment:

    variable_b = variable_a

This creates another reference to the same object.

It does NOT create an independent copy of the object.

Example
-------
    list_a = [1, 2, 3]
    list_b = list_a

Both variables now refer to the same list object.

Therefore:

    list_a is list_b

evaluates to True.

If the object is mutable, changes made through either reference are visible
through the other reference.

References
----------
Python Official Documentation

https://docs.python.org/3/library/stdtypes.html
"""


# =============================================================================
# Example 1: Assigning a List to Another Variable
# =============================================================================

original_numbers: list[int] = [1, 2, 3, 4, 5]

referenced_numbers: list[int] = original_numbers


# =============================================================================
# Example 2: Both Variables Refer to the Same Object
# =============================================================================

print(
    f"Original object ID:   {id(original_numbers)}"
)

print(
    f"Referenced object ID: {id(referenced_numbers)}"
)

print(
    f"Same object: {original_numbers is referenced_numbers}"
)


# =============================================================================
# Example 3: Modifying Through the Second Reference
# =============================================================================

referenced_numbers.append(6)


# The modification is visible through original_numbers because both variables
# reference the same list object.
print(
    f"Original list after modification: {original_numbers}"
)

print(
    f"Referenced list after modification: {referenced_numbers}"
)


# =============================================================================
# Example 4: Equality vs Identity
# =============================================================================

first_numbers: list[int] = [10, 20, 30]

second_numbers: list[int] = first_numbers


# The == operator compares the values contained in the objects.
print(
    f"Equal values: {first_numbers == second_numbers}"
)

# The `is` operator checks whether both variables refer to the same object.
print(
    f"Same object: {first_numbers is second_numbers}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Assignment does not create a new copy of an object.

✓ Assigning one variable to another creates another reference to the same
  object.

✓ Mutable objects can be modified through either reference.

✓ `id()` can be used to inspect an object's identity.

✓ `==` compares values.

✓ `is` checks object identity.

✓ Understanding references is essential before learning shallow and deep
  copying.
"""

"""
The structure can be visualized as:

list_a ──────┐
             ▼
          [outer list]
             ▲
list_b ──────┘
"""


# =============================================================================
# End of File
# =============================================================================