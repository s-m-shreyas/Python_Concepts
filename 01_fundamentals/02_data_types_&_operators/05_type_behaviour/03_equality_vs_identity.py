"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Special Data Types

Subcategory
-----------
Type Behaviour

Topic
-----
Equality vs Identity

Overview
--------
Python provides two different concepts for comparing objects:

    Equality
        `==`

        Checks whether two objects have equal values or contents.

    Identity
        `is`

        Checks whether two variables refer to the exact same object.

These are NOT the same concept.

Example:

    first_values = [10, 20]
    second_values = [10, 20]

    first_values == second_values
        -> True

    first_values is second_values
        -> False

The lists contain equal values, but they are two different objects.

This file covers:

    - Equality using ==
    - Identity using is
    - Equality vs identity
    - Object identity using id()
    - Different objects with equal values
    - Same object through multiple references
    - Mutable objects
    - Immutable objects
    - Strings
    - Integers
    - Lists
    - Tuples
    - Dictionaries
    - Sets
    - None
    - Why `is` should not normally be used for value comparison
    - Why `is None` is correct
    - Aliasing
    - Copying
    - Nested objects
    - Equality and hashing
"""


# =============================================================================
# 01. Basic Equality
# =============================================================================

equality_basic_left: int = 100
equality_basic_right: int = 100

print(
    f"Values equal: "
    f"{equality_basic_left == equality_basic_right}"
)


# `==` asks:
#
#     Do these objects compare as equal?


# =============================================================================
# 02. Basic Identity
# =============================================================================

identity_basic_source: list[int] = [
    10,
    20,
]

identity_basic_reference: list[int] = (
    identity_basic_source
)

print(
    f"Same object: "
    f"{identity_basic_source is identity_basic_reference}"
)


# Both variables refer to the same list object.


# =============================================================================
# 03. Equality and Identity Together
# =============================================================================

comparison_list_left: list[int] = [
    10,
    20,
]

comparison_list_right: list[int] = [
    10,
    20,
]

print(
    f"Equal values: "
    f"{comparison_list_left == comparison_list_right}"
)

print(
    f"Same object: "
    f"{comparison_list_left is comparison_list_right}"
)


# Result:
#
#     Equal values -> True
#     Same object   -> False
#
# Two different list objects contain the same values.


# =============================================================================
# 04. id() Shows Object Identity
# =============================================================================

identity_id_first: list[int] = [
    1,
    2,
]

identity_id_second: list[int] = [
    1,
    2,
]

print(
    f"First id: "
    f"{id(identity_id_first)}"
)

print(
    f"Second id: "
    f"{id(identity_id_second)}"
)

print(
    f"Same identity: "
    f"{id(identity_id_first) == id(identity_id_second)}"
)


# Different list objects normally have different identities.


# =============================================================================
# 05. is and id() Relationship
# =============================================================================

identity_relationship_object: list[str] = [
    "Python",
    "SQL",
]

identity_relationship_reference: list[str] = (
    identity_relationship_object
)

print(
    f"is comparison: "
    f"{identity_relationship_object is identity_relationship_reference}"
)

print(
    f"id comparison: "
    f"{id(identity_relationship_object) == id(identity_relationship_reference)}"
)


# For object identity:
#
#     a is b
#
# corresponds conceptually to:
#
#     id(a) == id(b)


# =============================================================================
# 06. Different Objects Can Be Equal
# =============================================================================

equality_different_objects_a: dict[str, int] = {
    "Python": 100,
}

equality_different_objects_b: dict[str, int] = {
    "Python": 100,
}

print(
    f"Equal dictionaries: "
    f"{equality_different_objects_a == equality_different_objects_b}"
)

print(
    f"Same dictionary object: "
    f"{equality_different_objects_a is equality_different_objects_b}"
)


# Same contents.
# Different objects.


# =============================================================================
# 07. Same Object Can Be Equal to Itself
# =============================================================================

identity_self_list: list[int] = [
    10,
    20,
]

print(
    f"Equal to itself: "
    f"{identity_self_list == identity_self_list}"
)

print(
    f"Identical to itself: "
    f"{identity_self_list is identity_self_list}"
)


# An object is always identical to itself.


# =============================================================================
# 08. Aliasing
# =============================================================================

alias_original_values: list[int] = [
    10,
    20,
]

alias_second_reference: list[int] = (
    alias_original_values
)

print(
    f"Equal: "
    f"{alias_original_values == alias_second_reference}"
)

print(
    f"Identical: "
    f"{alias_original_values is alias_second_reference}"
)


# Both variables point to the same object.
#
# This is called aliasing.


# =============================================================================
# 09. Mutation Through an Alias
# =============================================================================

alias_mutation_source: list[int] = [
    10,
    20,
]

alias_mutation_reference: list[int] = (
    alias_mutation_source
)

alias_mutation_reference.append(30)

print(
    f"Source: "
    f"{alias_mutation_source!r}"
)

print(
    f"Reference: "
    f"{alias_mutation_reference!r}"
)

print(
    f"Same object: "
    f"{alias_mutation_source is alias_mutation_reference}"
)


# Because both variables reference the same mutable object,
# mutation through one reference is visible through the other.


# =============================================================================
# 10. Copy Creates Different Identity
# =============================================================================

copy_identity_source: list[int] = [
    10,
    20,
]

copy_identity_result: list[int] = (
    copy_identity_source.copy()
)

print(
    f"Equal values: "
    f"{copy_identity_source == copy_identity_result}"
)

print(
    f"Same object: "
    f"{copy_identity_source is copy_identity_result}"
)


# copy() creates a different list object
# containing equal values.


# =============================================================================
# 11. Equality After Copy
# =============================================================================

copy_equality_source: dict[str, int] = {
    "Python": 100,
    "SQL": 90,
}

copy_equality_result: dict[str, int] = (
    copy_equality_source.copy()
)

print(
    f"Equal dictionaries: "
    f"{copy_equality_source == copy_equality_result}"
)

print(
    f"Identical dictionaries: "
    f"{copy_equality_source is copy_equality_result}"
)


# Different objects can still be equal.


# =============================================================================
# 12. String Equality
# =============================================================================

equality_string_first: str = "Python"
equality_string_second: str = "Python"

print(
    f"Equal strings: "
    f"{equality_string_first == equality_string_second}"
)


# `==` is the appropriate operator for comparing string values.


# =============================================================================
# 13. String Identity
# =============================================================================

identity_string_first: str = "".join(
    ["Py", "thon"]
)

identity_string_second: str = "Python"

print(
    f"Equal strings: "
    f"{identity_string_first == identity_string_second}"
)

print(
    f"Same string object: "
    f"{identity_string_first is identity_string_second}"
)


# Important:
#
# Never rely on `is` for normal string value comparison.
#
# Use:
#
#     ==
#
# instead.


# =============================================================================
# 14. Integer Equality
# =============================================================================

equality_integer_first: int = 500
equality_integer_second: int = 500

print(
    f"Equal integers: "
    f"{equality_integer_first == equality_integer_second}"
)


# `==` checks integer values.


# =============================================================================
# 15. Integer Identity
# =============================================================================

identity_integer_source: int = int(
    "500"
)

identity_integer_result: int = int(
    "500"
)

print(
    f"Equal integers: "
    f"{identity_integer_source == identity_integer_result}"
)

print(
    f"Same integer object: "
    f"{identity_integer_source is identity_integer_result}"
)


# The important lesson:
#
# Two equal integers do not need to be the same object.
#
# Use `==` when comparing values.


# =============================================================================
# 16. Float Equality
# =============================================================================

equality_float_left: float = 10.5
equality_float_right: float = 10.5

print(
    f"Equal floats: "
    f"{equality_float_left == equality_float_right}"
)


# `==` compares float values.


# =============================================================================
# 17. Tuple Equality
# =============================================================================

equality_tuple_left: tuple[int, ...] = (
    10,
    20,
    30,
)

equality_tuple_right: tuple[int, ...] = (
    10,
    20,
    30,
)

print(
    f"Equal tuples: "
    f"{equality_tuple_left == equality_tuple_right}"
)

print(
    f"Same tuple object: "
    f"{equality_tuple_left is equality_tuple_right}"
)


# Tuple equality compares their contents.


# =============================================================================
# 18. Set Equality
# =============================================================================

equality_set_left: set[int] = {
    10,
    20,
    30,
}

equality_set_right: set[int] = {
    30,
    20,
    10,
}

print(
    f"Equal sets: "
    f"{equality_set_left == equality_set_right}"
)

print(
    f"Same set object: "
    f"{equality_set_left is equality_set_right}"
)


# Set equality is based on elements,
# not insertion order.


# =============================================================================
# 19. Dictionary Equality
# =============================================================================

equality_dictionary_left: dict[str, int] = {
    "Python": 100,
    "SQL": 90,
}

equality_dictionary_right: dict[str, int] = {
    "SQL": 90,
    "Python": 100,
}

print(
    f"Equal dictionaries: "
    f"{equality_dictionary_left == equality_dictionary_right}"
)

print(
    f"Same dictionary object: "
    f"{equality_dictionary_left is equality_dictionary_right}"
)


# Dictionary equality compares key-value contents.


# =============================================================================
# 20. None and Identity
# =============================================================================

identity_none_value: None = None

print(
    f"None is None: "
    f"{identity_none_value is None}"
)


# `None` is a singleton object.
#
# Therefore:
#
#     value is None
#
# is the standard way to check for None.


# =============================================================================
# 21. None Equality vs Identity
# =============================================================================

none_comparison_value: None = None

print(
    f"None == None: "
    f"{none_comparison_value == None}"
)

print(
    f"None is None: "
    f"{none_comparison_value is None}"
)


# For None checks, prefer:
#
#     is None
#
# rather than:
#
#     == None


# =============================================================================
# 22. Correct None Check
# =============================================================================

def check_optional_text(
    optional_text_value: str | None,
) -> bool:
    return optional_text_value is None


equality_none_check_result: bool = (
    check_optional_text(None)
)

print(
    f"Value is None: "
    f"{equality_none_check_result}"
)


# `is None` explicitly checks object identity against the None singleton.


# =============================================================================
# 23. Not None
# =============================================================================

def has_text_value(
    possible_text_value: str | None,
) -> bool:
    return possible_text_value is not None


equality_not_none_result: bool = (
    has_text_value("Python")
)

print(
    f"Value is not None: "
    f"{equality_not_none_result}"
)


# Standard pattern:
#
#     value is None
#
#     value is not None


# =============================================================================
# 24. Boolean Equality
# =============================================================================

equality_boolean_left: bool = True
equality_boolean_right: bool = True

print(
    f"Equal booleans: "
    f"{equality_boolean_left == equality_boolean_right}"
)


# `==` compares boolean values.


# =============================================================================
# 25. Equality Does Not Mean Same Identity
# =============================================================================

comparison_numbers_left: int = 100
comparison_numbers_right: float = 100.0

print(
    f"Equal values: "
    f"{comparison_numbers_left == comparison_numbers_right}"
)

print(
    f"Same object: "
    f"{comparison_numbers_left is comparison_numbers_right}"
)


# Python considers these values equal numerically.
#
# But they are different objects and different types.


# =============================================================================
# 26. Type Can Matter During Equality
# =============================================================================

comparison_text_value: str = "100"
comparison_number_value: int = 100

print(
    f"Equal: "
    f"{comparison_text_value == comparison_number_value}")# pyright: ignore[reportUnnecessaryComparison]

print(
    f"Same object: "
    f"{comparison_text_value is comparison_number_value}")# pyright: ignore[reportUnnecessaryComparison]


# A string containing "100" is not equal to the integer 100.


# =============================================================================
# 27. Nested Equality
# =============================================================================

nested_equality_first: list[list[int]] = [
    [10, 20],
    [30, 40],
]

nested_equality_second: list[list[int]] = [
    [10, 20],
    [30, 40],
]

print(
    f"Nested values equal: "
    f"{nested_equality_first == nested_equality_second}"
)

print(
    f"Outer objects identical: "
    f"{nested_equality_first is nested_equality_second}"
)


# `==` recursively compares the contents of the lists.


# =============================================================================
# 28. Nested Identity
# =============================================================================

nested_identity_inner: list[int] = [
    10,
    20,
]

nested_identity_first: list[list[int]] = [
    nested_identity_inner,
]

nested_identity_second: list[list[int]] = [
    nested_identity_inner,
]

print(
    f"Outer lists equal: "
    f"{nested_identity_first == nested_identity_second}"
)

print(
    f"Outer lists identical: "
    f"{nested_identity_first is nested_identity_second}"
)

print(
    f"Inner lists identical: "
    f"{nested_identity_first[0] is nested_identity_second[0]}"
)


# The outer lists are different.
#
# The inner list is the same object.


# =============================================================================
# 29. Equality Can Be Customized
# =============================================================================

from typing import Any

class EqualityPerson:
    """Example class with value-based equality."""

    def __init__(
        self,
        person_name: str,
        person_age: int,
    ) -> None:
        self.person_name = person_name
        self.person_age = person_age

    def __eq__(
        self,
        other_person: Any,
    ) -> bool:
        if not isinstance(
            other_person,
            EqualityPerson,
        ):
            return NotImplemented

        return (
            self.person_name == other_person.person_name
            and self.person_age == other_person.person_age
        )


equality_person_first: EqualityPerson = (
    EqualityPerson(
        "Alex",
        30,
    )
)

equality_person_second: EqualityPerson = (
    EqualityPerson(
        "Alex",
        30,
    )
)

print(
    f"People equal: "
    f"{equality_person_first == equality_person_second}"
)

print(
    f"Same object: "
    f"{equality_person_first is equality_person_second}"
)


# `==` can be customized using __eq__.
#
# `is` cannot be customized.
#
# `is` always checks object identity.


# =============================================================================
# 30. Same Object With Custom Equality
# =============================================================================

equality_person_reference: EqualityPerson = (
    equality_person_first
)

print(
    f"Equal: "
    f"{equality_person_first == equality_person_reference}"
)

print(
    f"Identical: "
    f"{equality_person_first is equality_person_reference}"
)


# Both comparisons are True because the references point to the same object.


# =============================================================================
# 31. is Cannot Be Used for Value Equality
# =============================================================================

identity_value_left: list[str] = [
    "Python",
]

identity_value_right: list[str] = [
    "Python",
]

print(
    f"Value comparison: "
    f"{identity_value_left == identity_value_right}"
)

print(
    f"Identity comparison: "
    f"{identity_value_left is identity_value_right}"
)


# The two operators answer different questions.


# =============================================================================
# 32. Function Returning the Same Object
# =============================================================================

def return_original_list(
    function_list_value: list[int],
) -> list[int]:
    return function_list_value


identity_function_source: list[int] = [
    10,
    20,
]

identity_function_result: list[int] = (
    return_original_list(
        identity_function_source
    )
)

print(
    f"Equal: "
    f"{identity_function_source == identity_function_result}"
)

print(
    f"Identical: "
    f"{identity_function_source is identity_function_result}"
)


# The function returned the exact same object.


# =============================================================================
# 33. Function Returning a New Equal Object
# =============================================================================

def return_copied_list(
    function_source_values: list[int],
) -> list[int]:
    return function_source_values.copy()


identity_copy_source: list[int] = [
    10,
    20,
]

identity_copy_result: list[int] = (
    return_copied_list(
        identity_copy_source
    )
)

print(
    f"Equal: "
    f"{identity_copy_source == identity_copy_result}"
)

print(
    f"Identical: "
    f"{identity_copy_source is identity_copy_result}"
)


# Same contents.
# Different object.


# =============================================================================
# 34. Equality and Hashability
# =============================================================================

equality_hash_left: str = "Python"
equality_hash_right: str = "Python"

print(
    f"Equal: "
    f"{equality_hash_left == equality_hash_right}"
)

print(
    f"Equal hashes: "
    f"{hash(equality_hash_left) == hash(equality_hash_right)}"
)


# Python's hashing contract states:
#
# If:
#
#     a == b
#
# then:
#
#     hash(a) == hash(b)
#
# Identity is not required for equality.


# =============================================================================
# 35. Equality vs Identity Summary
# =============================================================================

"""
Equality:

    operator:
        ==

    question:
        Do these objects have equal values/contents?

    example:

        first_list == second_list


Identity:

    operator:
        is

    question:
        Are these references pointing to the exact same object?

    example:

        first_list is second_list


Important:

    ==

        compares equality.


    is

        compares identity.
"""


# =============================================================================
# 36. Visual Object Model
# =============================================================================

"""
Example:

    first_values = [10, 20]
    second_values = [10, 20]


The conceptual model is:

    first_values
         │
         ▼
    ┌─────────────┐
    │ list object │
    │ 10, 20      │
    └─────────────┘


    second_values
         │
         ▼
    ┌─────────────┐
    │ list object │
    │ 10, 20      │
    └─────────────┘


The objects contain equal values:

    first_values == second_values
        -> True


But they are different objects:

    first_values is second_values
        -> False


Now consider:

    third_values = first_values


Conceptually:

    first_values ─────┐
                      │
                      ▼
                 ┌─────────────┐
                 │ list object │
                 │ 10, 20      │
                 └─────────────┘
                      ▲
                      │
    third_values ─────┘


Therefore:

    first_values == third_values
        -> True

    first_values is third_values
        -> True
"""


# =============================================================================
# 37. When Should You Use ==?
# =============================================================================

"""
Use `==` when you want to compare values.

Examples:

    name == "Python"

    age == 30

    first_list == second_list

    first_dict == second_dict

    first_set == second_set


The question is:

    "Are these values equivalent?"
"""


# =============================================================================
# 38. When Should You Use is?
# =============================================================================

"""
Use `is` when you want to compare object identity.

Typical example:

    value is None

Also useful when you intentionally need to know whether
two references point to the exact same object.

Example:

    first_object is second_object


The question is:

    "Are these two references pointing to the same object?"
"""


# =============================================================================
# 39. Why `is` Is Not a General Value Comparison
# =============================================================================

"""
Incorrect mindset:

    "If the values are the same, I can use is."

No.

Correct mindset:

    ==

        value equality


    is

        object identity


Even if Python happens to reuse or intern some objects,
that behaviour should not be used as a general value-comparison rule.
"""


# =============================================================================
# 40. Important None Rule
# =============================================================================

"""
For None:

    value is None

is preferred.

For normal values:

    value == expected_value

is normally appropriate.

Examples:

    optional_value is None

    user_name == "Alex"

    number_value == 100

    records == expected_records
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `==` checks equality.

✓ `is` checks identity.

✓ Equality asks:

      "Do these objects compare as equal?"

✓ Identity asks:

      "Are these references pointing to the same object?"

✓ Two different objects can be equal.

      [10, 20] == [10, 20]
          -> True

      [10, 20] is [10, 20]
          -> False


✓ Two variables can reference the same object.

      values = [10, 20]
      other_values = values

      values == other_values
          -> True

      values is other_values
          -> True


✓ `id()` represents an object's identity during its lifetime.

✓ Conceptually:

      a is b

  corresponds to:

      id(a) == id(b)


✓ `.copy()` generally creates a new outer object.

      original == copy
          -> True

      original is copy
          -> False


✓ `is` cannot be customized.

✓ `==` can be customized using `__eq__`.

✓ `None` is normally checked using:

      value is None

  or:

      value is not None


✓ Do not use `is` for ordinary string, integer, float,
  list, tuple, set, or dictionary value comparison.

✓ Use `==` for value comparison.

✓ Use `is` for intentional identity comparison.

Core distinction:

                COMPARISON
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
        ==                    is
          │                   │
          ▼                   ▼
      Equality             Identity
          │                   │
          ▼                   ▼
   Same value/content?   Same object?
"""


# =============================================================================
# End of File
# =============================================================================