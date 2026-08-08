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
Mutability

Overview
--------
Mutability describes whether an existing object can be changed after it
has been created.

Python objects can broadly be classified as:

    Immutable
        The existing object cannot be modified.

    Mutable
        The existing object can be modified.

Common immutable types:

    - int
    - float
    - complex
    - bool
    - str
    - tuple
    - frozenset
    - bytes
    - NoneType
    - range

Common mutable types:

    - list
    - set
    - dict
    - bytearray
    - memoryview (depending on the underlying writable buffer)

This file covers:

    - Meaning of mutability
    - Immutable objects
    - Mutable objects
    - Reassignment vs mutation
    - Object identity using id()
    - Strings
    - Integers
    - Floats
    - Tuples
    - Frozensets
    - Bytes
    - Lists
    - Sets
    - Dictionaries
    - Bytearray
    - Nested mutable objects
    - Mutable objects inside immutable containers
    - Immutable objects inside mutable containers
    - Function arguments
    - Why mutable default arguments are dangerous
    - Copying mutable objects
    - Shallow copies
    - Deep copies
    - is vs ==
    - Practical rules
"""


# =============================================================================
# 01. What Is Mutability?
# =============================================================================

"""
Mutability answers this question:

    Can the existing object itself be changed?

Example:

    list
        ↓
    existing list
        ↓
    append()
        ↓
    same list object
        ↓
    contents changed

This is mutation.


For an immutable object:

    existing object
        ↓
    attempted modification
        ↓
    not allowed

A new object must be created instead.
"""


# =============================================================================
# 02. Mutable vs Immutable
# =============================================================================

mutable_example_values: list[int] = [
    10,
    20,
]

immutable_example_text: str = "Python"

print(
    f"Mutable type: "
    f"{type(mutable_example_values).__name__!r}"
)

print(
    f"Immutable type: "
    f"{type(immutable_example_text).__name__!r}"
)


# =============================================================================
# 03. Immutable String
# =============================================================================

immutability_string_value: str = "Python"

print(
    f"Original string: "
    f"{immutability_string_value!r}"
)

print(
    f"Original id: "
    f"{id(immutability_string_value)}"
)


# A string cannot be modified in place.


# =============================================================================
# 04. String Reassignment Is Not Mutation
# =============================================================================

immutability_reassignment_text: str = "Python"

immutability_reassignment_before: int = (
    id(immutability_reassignment_text)
)

immutability_reassignment_text = "Java"

immutability_reassignment_after: int = (
    id(immutability_reassignment_text)
)

print(
    f"Before id: "
    f"{immutability_reassignment_before}"
)

print(
    f"After id: "
    f"{immutability_reassignment_after}"
)

print(
    f"New value: "
    f"{immutability_reassignment_text!r}"
)


# The variable was reassigned.
#
# The original string object was not modified.
#
# A different string object can now be referenced by the variable.


# =============================================================================
# 05. String Operation Creates a New Object
# =============================================================================

immutability_string_original: str = "Data"

immutability_string_transformed: str = (
    immutability_string_original + " Engineering"
)

print(
    f"Original: "
    f"{immutability_string_original!r}"
)

print(
    f"Transformed: "
    f"{immutability_string_transformed!r}"
)

print(
    f"Original id: "
    f"{id(immutability_string_original)}"
)

print(
    f"Transformed id: "
    f"{id(immutability_string_transformed)}"
)


# String concatenation does not modify the original string.
#
# It produces another string object.


# =============================================================================
# 06. Immutable Integer
# =============================================================================

immutability_integer_value: int = 100

immutability_integer_before: int = (
    id(immutability_integer_value)
)

immutability_integer_value += 50

immutability_integer_after: int = (
    id(immutability_integer_value)
)

print(
    f"New integer value: "
    f"{immutability_integer_value}"
)

print(
    f"Before id: "
    f"{immutability_integer_before}"
)

print(
    f"After id: "
    f"{immutability_integer_after}"
)


# Integer arithmetic does not modify an existing integer object.
#
# A new integer object represents the resulting value.


# =============================================================================
# 07. Immutable Float
# =============================================================================

immutability_float_value: float = 10.5

immutability_float_before: int = (
    id(immutability_float_value)
)

immutability_float_value *= 2

immutability_float_after: int = (
    id(immutability_float_value)
)

print(
    f"Float value: "
    f"{immutability_float_value}"
)

print(
    f"Before id: "
    f"{immutability_float_before}"
)

print(
    f"After id: "
    f"{immutability_float_after}"
)


# Floats are immutable.


# =============================================================================
# 08. Immutable Complex Number
# =============================================================================

immutability_complex_value: complex = 2 + 3j

immutability_complex_before: int = (
    id(immutability_complex_value)
)

immutability_complex_value += 1 + 2j

immutability_complex_after: int = (
    id(immutability_complex_value)
)

print(
    f"Complex value: "
    f"{immutability_complex_value!r}"
)

print(
    f"Before id: "
    f"{immutability_complex_before}"
)

print(
    f"After id: "
    f"{immutability_complex_after}"
)


# Complex numbers are immutable.


# =============================================================================
# 09. Immutable Tuple
# =============================================================================

immutability_tuple_value: tuple[int, ...] = (
    10,
    20,
    30,
)

print(
    f"Tuple: "
    f"{immutability_tuple_value!r}"
)

print(
    f"Tuple id: "
    f"{id(immutability_tuple_value)}"
)


# A tuple does not provide operations that modify its own structure.


# =============================================================================
# 10. Tuple Does Not Support Item Assignment
# =============================================================================

immutability_tuple_fixed: tuple[str, ...] = (
    "Python",
    "SQL",
    "AWS",
)

print(
    f"Tuple remains: "
    f"{immutability_tuple_fixed!r}"
)


# The following would fail:
#
#     immutability_tuple_fixed[0] = "Java"
#
# because tuple objects are immutable.


# =============================================================================
# 11. Immutable Frozenset
# =============================================================================

immutability_frozenset_value: frozenset[int] = frozenset(
    {10, 20, 30}
)

print(
    f"Frozenset: "
    f"{immutability_frozenset_value!r}"
)


# A frozenset cannot be modified after creation.


# =============================================================================
# 12. Immutable Bytes
# =============================================================================

immutability_bytes_value: bytes = b"Python"

print(
    f"Bytes: "
    f"{immutability_bytes_value!r}"
)

print(
    f"Bytes id: "
    f"{id(immutability_bytes_value)}"
)


# bytes objects are immutable.


# =============================================================================
# 13. Mutable List
# =============================================================================

immutability_list_values: list[int] = [
    10,
    20,
]

immutability_list_before: int = (
    id(immutability_list_values)
)

immutability_list_values.append(30)

immutability_list_after: int = (
    id(immutability_list_values)
)

print(
    f"List: "
    f"{immutability_list_values!r}"
)

print(
    f"Before id: "
    f"{immutability_list_before}"
)

print(
    f"After id: "
    f"{immutability_list_after}"
)


# The list contents changed.
#
# The list object itself remained the same object.
#
# This is mutation.


# =============================================================================
# 14. Mutation vs Reassignment
# =============================================================================

mutability_operation_list: list[int] = [
    1,
    2,
]

mutability_operation_before: int = (
    id(mutability_operation_list)
)

mutability_operation_list.append(3)

mutability_operation_after: int = (
    id(mutability_operation_list)
)

print(
    f"After mutation: "
    f"{mutability_operation_list!r}"
)

print(
    f"Same object: "
    f"{mutability_operation_before == mutability_operation_after}"
)


# append() mutates the existing list.


# =============================================================================
# 15. List Reassignment
# =============================================================================

mutability_reassignment_list: list[int] = [
    1,
    2,
]

mutability_reassignment_list_id_before: int = (
    id(mutability_reassignment_list)
)

mutability_reassignment_list = [
    3,
    4,
]

mutability_reassignment_list_id_after: int = (
    id(mutability_reassignment_list)
)

print(
    f"New list: "
    f"{mutability_reassignment_list!r}"
)

print(
    f"Same object after reassignment: "
    f"{mutability_reassignment_list_id_before == mutability_reassignment_list_id_after}"
)


# Reassignment points the variable to another object.
#
# It is different from mutation.


# =============================================================================
# 16. Mutable Set
# =============================================================================

mutability_set_values: set[int] = {
    10,
    20,
}

mutability_set_before: int = (
    id(mutability_set_values)
)

mutability_set_values.add(30)

mutability_set_after: int = (
    id(mutability_set_values)
)

print(
    f"Set: "
    f"{mutability_set_values!r}"
)

print(
    f"Same object: "
    f"{mutability_set_before == mutability_set_after}"
)


# set.add() mutates the existing set.


# =============================================================================
# 17. Mutable Dictionary
# =============================================================================

mutability_dictionary_data: dict[str, int] = {
    "Python": 90,
}

mutability_dictionary_before: int = (
    id(mutability_dictionary_data)
)

mutability_dictionary_data["SQL"] = 85

mutability_dictionary_after: int = (
    id(mutability_dictionary_data)
)

print(
    f"Dictionary: "
    f"{mutability_dictionary_data!r}"
)

print(
    f"Same object: "
    f"{mutability_dictionary_before == mutability_dictionary_after}"
)


# Adding a key mutates the existing dictionary.


# =============================================================================
# 18. Mutable Bytearray
# =============================================================================

mutability_bytearray_data: bytearray = bytearray(
    b"ABC"
)

mutability_bytearray_before: int = (
    id(mutability_bytearray_data)
)

mutability_bytearray_data[0] = ord("Z")

mutability_bytearray_after: int = (
    id(mutability_bytearray_data)
)

print(
    f"Bytearray: "
    f"{mutability_bytearray_data!r}"
)

print(
    f"Same object: "
    f"{mutability_bytearray_before == mutability_bytearray_after}"
)


# bytearray supports in-place modification.


# =============================================================================
# 19. Immutable Container Can Contain Mutable Objects
# =============================================================================

mutability_nested_list: list[int] = [
    10,
    20,
]

mutability_tuple_with_list: tuple[list[int], ...] = (
    mutability_nested_list,
)

mutability_tuple_before: int = (
    id(mutability_tuple_with_list)
)

mutability_tuple_with_list[0].append(30)

mutability_tuple_after: int = (
    id(mutability_tuple_with_list)
)

print(
    f"Tuple: "
    f"{mutability_tuple_with_list!r}"
)

print(
    f"Tuple id unchanged: "
    f"{mutability_tuple_before == mutability_tuple_after}"
)


# Important:
#
# The tuple itself is immutable.
#
# But the list stored inside the tuple is mutable.
#
# Therefore the list can still change.


# =============================================================================
# 20. Immutable Container Does Not Mean Deeply Immutable
# =============================================================================

mutability_nested_dictionary: dict[str, int] = {
    "score": 100,
}

mutability_nested_tuple: tuple[dict[str, int], ...] = (
    mutability_nested_dictionary,
)

mutability_nested_tuple[0]["score"] = 200

print(
    f"Tuple containing dictionary: "
    f"{mutability_nested_tuple!r}"
)


# The tuple structure did not change.
#
# The dictionary object inside it changed.


# =============================================================================
# 21. Mutable Container Can Contain Immutable Objects
# =============================================================================

mutability_integer_list: list[int] = [
    10,
    20,
]

mutability_integer_list[0] = 500

print(
    f"Modified list: "
    f"{mutability_integer_list!r}"
)


# The list is mutable.
#
# Replacing one immutable integer object with another
# is a mutation of the list.


# =============================================================================
# 22. Identity Shows Object Replacement
# =============================================================================

mutability_identity_text: str = "Python"

mutability_identity_before: int = (
    id(mutability_identity_text)
)

mutability_identity_text += " 3"

mutability_identity_after: int = (
    id(mutability_identity_text)
)

print(
    f"Before id: "
    f"{mutability_identity_before}"
)

print(
    f"After id: "
    f"{mutability_identity_after}"
)

print(
    f"Value: "
    f"{mutability_identity_text!r}"
)


# The string was not modified in place.
#
# The variable now refers to another string object.


# =============================================================================
# 23. Mutable Object Passed to a Function
# =============================================================================

def mutate_list_values(
    function_list_values: list[int],
) -> None:
    function_list_values.append(40)


mutability_function_list: list[int] = [
    10,
    20,
]

mutability_function_before: int = (
    id(mutability_function_list)
)

mutate_list_values(
    mutability_function_list
)

mutability_function_after: int = (
    id(mutability_function_list)
)

print(
    f"List after function call: "
    f"{mutability_function_list!r}"
)

print(
    f"Same object: "
    f"{mutability_function_before == mutability_function_after}"
)


# The function received a reference to the same list object.
#
# Mutating that list is visible outside the function.


# =============================================================================
# 24. Immutable Object Passed to a Function
# =============================================================================

def reassign_integer_value(
    function_integer_value: int,
) -> None:
    function_integer_value += 100


mutability_function_integer: int = 50

mutability_function_integer_before: int = (
    id(mutability_function_integer)
)

reassign_integer_value(
    mutability_function_integer
)

mutability_function_integer_after: int = (
    id(mutability_function_integer)
)

print(
    f"Integer after function call: "
    f"{mutability_function_integer}"
)

print(
    f"Same object: "
    f"{mutability_function_integer_before == mutability_function_integer_after}"
)


# The integer outside the function is unchanged.
#
# The local variable inside the function was reassigned.


# =============================================================================
# 25. Mutable Default Argument Problem
# =============================================================================

def append_default_value(
    default_values: list[int] = [],
) -> list[int]:
    default_values.append(1)
    return default_values


mutability_default_first: list[int] = (
    append_default_value()
)

mutability_default_second: list[int] = (
    append_default_value()
)

print(
    f"First call: "
    f"{mutability_default_first!r}"
)

print(
    f"Second call: "
    f"{mutability_default_second!r}"
)


# The default list is created once when the function is defined.
#
# It is reused across calls.
#
# This is a classic mutable-default-argument problem.


# =============================================================================
# 26. Safe Mutable Default Pattern
# =============================================================================

def append_safe_value(
    safe_values: list[int] | None = None,
) -> list[int]:
    if safe_values is None:
        safe_values = []

    safe_values.append(1)

    return safe_values


mutability_safe_first: list[int] = (
    append_safe_value()
)

mutability_safe_second: list[int] = (
    append_safe_value()
)

print(
    f"First safe call: "
    f"{mutability_safe_first!r}"
)

print(
    f"Second safe call: "
    f"{mutability_safe_second!r}"
)


# A new list is created for each call when None is supplied.


# =============================================================================
# 27. Shallow Copy
# =============================================================================

mutability_shallow_original: list[list[int]] = [
    [10, 20],
    [30, 40],
]

mutability_shallow_copy: list[list[int]] = (
    mutability_shallow_original.copy()
)

mutability_shallow_copy[0].append(50)

print(
    f"Original: "
    f"{mutability_shallow_original!r}"
)

print(
    f"Copy: "
    f"{mutability_shallow_copy!r}"
)


# The outer lists are different objects.
#
# But their nested lists are still shared.


# =============================================================================
# 28. Shallow Copy Identity
# =============================================================================

mutability_shallow_source: list[int] = [
    10,
    20,
]

mutability_shallow_duplicate: list[int] = (
    mutability_shallow_source.copy()
)

print(
    f"Different outer objects: "
    f"{mutability_shallow_source is not mutability_shallow_duplicate}"
)

print(
    f"Equal contents: "
    f"{mutability_shallow_source == mutability_shallow_duplicate}"
)


# copy() creates a new outer list.


# =============================================================================
# 29. Deep Copy
# =============================================================================

from copy import deepcopy


mutability_deep_original: list[list[int]] = [
    [10, 20],
    [30, 40],
]

mutability_deep_copy: list[list[int]] = deepcopy(
    mutability_deep_original
)

mutability_deep_copy[0].append(50)

print(
    f"Original: "
    f"{mutability_deep_original!r}"
)

print(
    f"Deep copy: "
    f"{mutability_deep_copy!r}"
)


# deepcopy() recursively creates independent copies
# of nested mutable objects.


# =============================================================================
# 30. Shallow Copy vs Deep Copy
# =============================================================================

mutability_copy_source: list[list[int]] = [
    [1, 2],
]

mutability_copy_shallow: list[list[int]] = (
    mutability_copy_source.copy()
)

mutability_copy_deep: list[list[int]] = deepcopy(
    mutability_copy_source
)

print(
    f"Outer shallow same: "
    f"{mutability_copy_source is mutability_copy_shallow}"
)

print(
    f"Inner shallow same: "
    f"{mutability_copy_source[0] is mutability_copy_shallow[0]}"
)

print(
    f"Outer deep same: "
    f"{mutability_copy_source is mutability_copy_deep}"
)

print(
    f"Inner deep same: "
    f"{mutability_copy_source[0] is mutability_copy_deep[0]}"
)


# Typical result:
#
#     Outer shallow same -> False
#     Inner shallow same -> True
#     Outer deep same    -> False
#     Inner deep same    -> False


# =============================================================================
# 31. Equality vs Identity in Mutable Objects
# =============================================================================

mutability_equality_left: list[int] = [
    10,
    20,
]

mutability_equality_right: list[int] = [
    10,
    20,
]

print(
    f"Equal values: "
    f"{mutability_equality_left == mutability_equality_right}"
)

print(
    f"Same object: "
    f"{mutability_equality_left is mutability_equality_right}"
)


# == checks equality of values.
#
# is checks object identity.


# =============================================================================
# 32. Same Object Through Two References
# =============================================================================

mutability_alias_original: list[int] = [
    10,
    20,
]

mutability_alias_reference: list[int] = (
    mutability_alias_original
)

mutability_alias_reference.append(30)

print(
    f"Original reference: "
    f"{mutability_alias_original!r}"
)

print(
    f"Second reference: "
    f"{mutability_alias_reference!r}"
)

print(
    f"Same object: "
    f"{mutability_alias_original is mutability_alias_reference}"
)


# Both variables refer to the same list object.


# =============================================================================
# 33. Aliasing
# =============================================================================

mutability_alias_source: dict[str, int] = {
    "Python": 100,
}

mutability_alias_target: dict[str, int] = (
    mutability_alias_source
)

mutability_alias_target["SQL"] = 90

print(
    f"Source: "
    f"{mutability_alias_source!r}"
)

print(
    f"Target: "
    f"{mutability_alias_target!r}"
)


# Both variables point to the same dictionary.


# =============================================================================
# 34. Immutable Object Aliasing
# =============================================================================

mutability_immutable_alias_value: str = (
    "Python"
)

mutability_immutable_alias_reference: str = (
    mutability_immutable_alias_value
)

print(
    f"Same object: "
    f"{mutability_immutable_alias_value is mutability_immutable_alias_reference}"
)


# Even immutable objects can have multiple references.
#
# Immutability means the object cannot be changed,
# not that it can have only one reference.


# =============================================================================
# 35. Mutability Is a Property of the Object
# =============================================================================

mutability_property_list: list[int] = [
    10,
    20,
]

mutability_property_reference: list[int] = (
    mutability_property_list
)

mutability_property_reference.append(30)

print(
    f"Original: "
    f"{mutability_property_list!r}"
)

print(
    f"Reference: "
    f"{mutability_property_reference!r}"
)


# Mutability belongs to the object.
#
# Variables are simply references to objects.


# =============================================================================
# 36. Important Conceptual Model
# =============================================================================

"""
Think of Python variables like labels.

Example:

    values = [10, 20]

Conceptually:

    values
      │
      ▼
    ┌─────────────┐
    │ list object │
    │ 10, 20      │
    └─────────────┘


After:

    values.append(30)

    values
      │
      ▼
    ┌─────────────┐
    │ list object │
    │ 10, 20, 30  │
    └─────────────┘

Same object.
Changed contents.

That is mutation.


For an immutable object:

    name = "Python"

    name = "Java"

Conceptually:

    name
      │
      ▼
    "Java"

The variable was reassigned.

The original "Python" object was not modified.


Therefore:

    mutation
        =
    changing an existing object

    reassignment
        =
    making a variable refer to another object
"""


# =============================================================================
# 37. Default Mutable and Immutable Behaviour
# =============================================================================

"""
Immutable objects:

    int
    float
    complex
    bool
    str
    tuple
    frozenset
    bytes
    NoneType
    range

Mutable objects:

    list
    set
    dict
    bytearray

Important:

    Mutability belongs to the object type,
    not to the variable name.

Example:

    values = [1, 2, 3]

`values` is not "mutable".

The list object referenced by `values` is mutable.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Mutable objects can be changed in place.

✓ Immutable objects cannot be changed in place.

✓ Common immutable types:

      int
      float
      complex
      bool
      str
      tuple
      frozenset
      bytes
      NoneType
      range

✓ Common mutable types:

      list
      set
      dict
      bytearray

✓ Mutation changes an existing object.

✓ Reassignment changes what a variable refers to.

✓ `id()` can help observe object identity.

✓ Example:

      my_list.append(10)

  usually keeps the same object identity.

✓ Example:

      my_text += "Python"

  produces a new string because strings are immutable.

✓ `==` compares equality.

✓ `is` compares identity.

✓ Two different objects can contain equal values.

✓ Multiple variables can reference the same mutable object.

✓ Mutating through one reference is visible through another reference.

✓ An immutable container can contain mutable objects.

      tuple[list[int], ...]

  The tuple structure is immutable,
  but the nested list can still change.

✓ A mutable container can contain immutable objects.

      list[int]

  The list can change even though individual integers are immutable.

✓ Mutable default arguments can preserve state between function calls.

✓ Prefer:

      def function(values: list[int] | None = None):

  when a fresh list should be created for each call.

✓ `.copy()` creates a shallow copy.

✓ `deepcopy()` recursively copies nested mutable objects.

✓ Variables are references to objects.

✓ Mutability is a property of the object,
  not of the variable name.

Conceptual model:

      variable
         │
         ▼
       object
         │
         ├── mutable
         │      ↓
         │   can change in place
         │
         └── immutable
                ↓
             cannot change
                ↓
             new object
             required
"""


# =============================================================================
# End of File
# =============================================================================