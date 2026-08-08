"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
Dictionary (`dict`)

Overview
--------
A dictionary is a mutable mapping of unique keys to values.

A dictionary stores data as:

    key -> value

Example:

    {
        "name": "Shreyas",
        "age": 29,
        "role": "Data Engineer",
    }

Dictionaries are:

    - Mutable
    - Ordered by insertion order
    - Iterable
    - Key-based
    - Not indexable by integer position
    - Not sliceable
    - Capable of storing heterogeneous values
    - Designed around key-value relationships
    - Required to have unique keys
    - Required to have hashable keys

Values can be of almost any Python type.

Keys must be hashable.

This module covers:

    - Dictionary literals
    - Default and non-default values
    - Empty dictionaries
    - Key-value pairs
    - Duplicate keys
    - Type identification
    - Runtime type checking
    - Length
    - Key lookup
    - get()
    - Adding elements
    - Updating elements
    - Removing elements
    - pop()
    - popitem()
    - clear()
    - keys()
    - values()
    - items()
    - Iteration
    - Membership testing
    - Dictionary copying
    - Dictionary merging
    - Dictionary unpacking
    - Nested dictionaries
    - Heterogeneous values
    - Hashable keys
    - Dictionary comprehensions
    - Equality
    - Identity

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: Dictionary Literals
# =============================================================================

empty_dictionary_value: dict[str, int] = {}

employee_dictionary_value: dict[str, object] = {
    "name": "Shreyas",
    "age": 29,
    "experience": 1.5,
}

technical_dictionary_value: dict[str, str] = {
    "language": "Python",
    "database": "Oracle",
    "workflow": "Airflow",
}

print(
    f"Empty dictionary:    {empty_dictionary_value}"
)

print(
    f"Employee dictionary: {employee_dictionary_value}"
)

print(
    f"Technical dictionary:"
    f" {technical_dictionary_value}"
)


# =============================================================================
# Example 2: Default and Non-Default Dictionary Values
# =============================================================================

default_like_dictionary: dict[str, int] = {}

non_default_dictionary_primary: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

non_default_dictionary_secondary: dict[str, str] = {
    "language": "Python",
    "database": "Oracle",
}

print(
    f"Default-like dictionary: "
    f"{default_like_dictionary}"
)

print(
    f"First dictionary:        "
    f"{non_default_dictionary_primary}"
)

print(
    f"Second dictionary:       "
    f"{non_default_dictionary_secondary}"
)


# Python does NOT automatically assign {} to an annotated dictionary.
#
# This:
#
#     values: dict[str, int]
#
# is only a type annotation.
#
# It does NOT initialize `values`.
#
# Explicit initialization is required:
#
#     values: dict[str, int] = {}


# =============================================================================
# Example 3: Empty Dictionary
# =============================================================================

empty_dictionary_literal: dict[object, object] = {}

print(
    f"Empty dictionary: {empty_dictionary_literal}"
)

print(
    f"Type: {type(empty_dictionary_literal)}"
)


# Important:
#
#     {}
#
# creates an empty dictionary.
#
# This differs from sets:
#
#     {}     -> dict
#     set()  -> empty set


# =============================================================================
# Example 4: Key-Value Structure
# =============================================================================

key_value_dictionary_sample: dict[str, object] = {
    "name": "Python",
    "version": 3.14,
    "compiled": False,
}

print(
    f"Dictionary: {key_value_dictionary_sample}"
)


# Each entry has the structure:
#
#     key: value
#
# Example:
#
#     "name": "Python"
#
# Here:
#
#     "name"  -> key
#     "Python" -> value


# =============================================================================
# Example 5: Duplicate Keys
# =============================================================================

duplicate_key_dictionary: dict[str, int] = {
    "score": 50,
    "score": 80,
}

print(
    f"Dictionary: {duplicate_key_dictionary}"
)


# Dictionary keys must be unique.
#
# If the same key appears multiple times, the later value replaces the
# earlier value.
#
# Result:
#
#     {"score": 80}


# =============================================================================
# Example 6: Type Identification
# =============================================================================

dictionary_type_sample: dict[str, int] = {
    "Python": 10,
    "SQL": 20,
}

print(
    f"Value: {dictionary_type_sample}"
)

print(
    f"Type:  {type(dictionary_type_sample)}"
)


# Expected:
#
#     <class 'dict'>


# =============================================================================
# Example 7: Runtime Dictionary Type Checking
# =============================================================================

dictionary_runtime_candidate: object = {
    "Python": 1,
    "SQL": 2,
}

list_runtime_candidate_for_dictionary: object = [
    "Python",
    "SQL",
]

dictionary_runtime_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    dictionary_runtime_candidate,
    dict,
)

list_dictionary_check: bool = isinstance(  # pyright: ignore[reportUnnecessaryIsInstance]
    list_runtime_candidate_for_dictionary,
    dict,
)

print(
    f"Dictionary candidate is dict: "
    f"{dictionary_runtime_check}"
)

print(
    f"List candidate is dict: "
    f"{list_dictionary_check}"
)


# The candidates are intentionally typed as `object`.
#
# The Pyright suppression is used because this example intentionally
# demonstrates runtime isinstance() behaviour.


# =============================================================================
# Example 8: Dictionary Length
# =============================================================================

dictionary_length_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_length_result: int = len(
    dictionary_length_sample
)

print(
    f"Dictionary length: {dictionary_length_result}"
)


# `len()` returns the number of key-value pairs.


# =============================================================================
# Example 9: Key Lookup
# =============================================================================

direct_lookup_dictionary: dict[str, str] = {
    "language": "Python",
    "database": "Oracle",
    "workflow": "Airflow",
}

direct_language_value: str = (
    direct_lookup_dictionary["language"]
)

print(
    f"Language: {direct_language_value}"
)


# Dictionary lookup uses the key:
#
#     dictionary[key]


# =============================================================================
# Example 10: Missing Key With Direct Lookup
# =============================================================================

missing_key_dictionary: dict[str, str] = {
    "language": "Python",
}

# The following operation is invalid at runtime:
#
#     missing_key_dictionary["database"]
#
# If the key does not exist, direct lookup raises:
#
#     KeyError


# =============================================================================
# Example 11: get()
# =============================================================================

safe_lookup_dictionary: dict[str, str] = {
    "language": "Python",
}

safe_existing_value: str | None = (
    safe_lookup_dictionary.get("language")
)

safe_missing_value: str | None = (
    safe_lookup_dictionary.get("database")
)

print(
    f"Existing value: {safe_existing_value}"
)

print(
    f"Missing value:  {safe_missing_value}"
)


# `get()` returns None by default when the key does not exist.


# =============================================================================
# Example 12: get() With a Default Value
# =============================================================================

default_lookup_dictionary: dict[str, str] = {
    "language": "Python",
}

default_existing_result: str = (
    default_lookup_dictionary.get(
        "language",
        "Unknown",
    )
)

default_missing_result: str = (
    default_lookup_dictionary.get(
        "database",
        "Unknown",
    )
)

print(
    f"Existing result: {default_existing_result}"
)

print(
    f"Missing result:  {default_missing_result}"
)


# The second argument to get() specifies the fallback value.


# =============================================================================
# Example 13: Adding a New Key
# =============================================================================

dictionary_addition_sample: dict[str, object] = {
    "name": "Python",
}

dictionary_addition_sample["version"] = 3.14

print(
    f"After addition: {dictionary_addition_sample}"
)


# Assigning a value to a non-existing key creates a new key-value pair.


# =============================================================================
# Example 14: Updating an Existing Key
# =============================================================================

dictionary_update_sample: dict[str, int] = {
    "score": 50,
}

dictionary_update_sample["score"] = 90

print(
    f"Updated dictionary: {dictionary_update_sample}"
)


# Assigning to an existing key replaces its previous value.


# =============================================================================
# Example 15: update()
# =============================================================================

dictionary_update_method_sample: dict[str, object] = {
    "language": "Python",
}

dictionary_update_method_sample.update(
    {
        "database": "Oracle",
        "workflow": "Airflow",
    }
)

print(
    f"After update(): "
    f"{dictionary_update_method_sample}"
)


# `update()` adds new keys and replaces existing keys.


# =============================================================================
# Example 16: update() Replacing Existing Values
# =============================================================================

dictionary_replace_update: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_replace_update.update(
    {
        "SQL": 20,
        "Airflow": 3,
    }
)

print(
    f"Updated values: {dictionary_replace_update}"
)


# Existing "SQL" is replaced.
# New "Airflow" is added.


# =============================================================================
# Example 17: Membership Testing
# =============================================================================

dictionary_membership_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_python_key_present: bool = (
    "Python" in dictionary_membership_sample
)

dictionary_value_present_as_key: bool = (
    1 in dictionary_membership_sample
) # pyright: ignore[reportUnnecessaryContains]

print(
    f"'Python' is a key: "
    f"{dictionary_python_key_present}"
)

print(
    f"1 is a key: "
    f"{dictionary_value_present_as_key}"
)


# IMPORTANT:
#
#     value in dictionary
#
# checks KEYS, not values.


# =============================================================================
# Example 18: Membership Testing in Values
# =============================================================================

dictionary_value_membership_sample: dict[str, str] = {
    "language": "Python",
    "database": "Oracle",
}

python_value_present: bool = (
    "Python"
    in dictionary_value_membership_sample.values()
)

print(
    f"'Python' is a value: "
    f"{python_value_present}"
)


# `.values()` can be used when value membership needs to be checked.


# =============================================================================
# Example 19: keys()
# =============================================================================

dictionary_keys_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_keys_view = (
    dictionary_keys_sample.keys()
)

print(
    f"Keys: {dictionary_keys_view}"
)


# `keys()` returns a dynamic dictionary view.


# =============================================================================
# Example 20: values()
# =============================================================================

dictionary_values_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_values_view = (
    dictionary_values_sample.values()
)

print(
    f"Values: {dictionary_values_view}"
)


# `values()` returns a dynamic dictionary view.


# =============================================================================
# Example 21: items()
# =============================================================================

dictionary_items_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_items_view = (
    dictionary_items_sample.items()
)

print(
    f"Items: {dictionary_items_view}"
)


# `items()` provides key-value pairs.


# =============================================================================
# Example 22: Iterating Over Keys
# =============================================================================

dictionary_key_iteration: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

for dictionary_key_item in dictionary_key_iteration:
    print(
        dictionary_key_item
    )


# Iterating directly over a dictionary iterates over its keys.


# =============================================================================
# Example 23: Iterating Over Values
# =============================================================================

dictionary_value_iteration: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

for dictionary_value_item in (
    dictionary_value_iteration.values()
):
    print(
        dictionary_value_item
    )


# =============================================================================
# Example 24: Iterating Over Key-Value Pairs
# =============================================================================

dictionary_pair_iteration: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

for (
    dictionary_pair_key,
    dictionary_pair_value,
) in dictionary_pair_iteration.items():
    print(
        f"{dictionary_pair_key}: "
        f"{dictionary_pair_value}"
    )


# =============================================================================
# Example 25: pop()
# =============================================================================

dictionary_pop_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_popped_value: int = (
    dictionary_pop_sample.pop(
        "SQL"
    )
)

print(
    f"Popped value: {dictionary_popped_value}"
)

print(
    f"Remaining dictionary: "
    f"{dictionary_pop_sample}"
)


# `pop(key)` removes the key and returns its value.


# =============================================================================
# Example 26: pop() With a Default
# =============================================================================

dictionary_pop_default_sample: dict[str, int] = {
    "Python": 1,
}

dictionary_safe_pop_result: int = (
    dictionary_pop_default_sample.pop(
        "SQL",
        0,
    )
)

print(
    f"Safe pop result: "
    f"{dictionary_safe_pop_result}"
)


# Without a default value, pop() raises KeyError for a missing key.
#
# Providing a default avoids the error.


# =============================================================================
# Example 27: popitem()
# =============================================================================

dictionary_popitem_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_removed_pair: tuple[str, int] = (
    dictionary_popitem_sample.popitem()
)

print(
    f"Removed pair: {dictionary_removed_pair}"
)

print(
    f"Remaining dictionary: "
    f"{dictionary_popitem_sample}"
)


# popitem() removes and returns the last inserted key-value pair.


# =============================================================================
# Example 28: clear()
# =============================================================================

dictionary_clear_sample: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
    "Airflow": 3,
}

dictionary_clear_sample.clear()

print(
    f"After clear(): "
    f"{dictionary_clear_sample}"
)


# `clear()` removes all key-value pairs.


# =============================================================================
# Example 29: copy()
# =============================================================================

dictionary_copy_source: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_shallow_copy: dict[str, int] = (
    dictionary_copy_source.copy()
)

dictionary_shallow_copy["Airflow"] = 3

print(
    f"Original: {dictionary_copy_source}"
)

print(
    f"Copy:     {dictionary_shallow_copy}"
)


# `copy()` creates a shallow copy of the dictionary.


# =============================================================================
# Example 30: Nested Dictionary
# =============================================================================

nested_dictionary_structure: dict[str, dict[str, object]] = {
    "employee": {
        "name": "Shreyas",
        "role": "Data Engineer",
    },
    "skills": {
        "language": "Python",
        "database": "Oracle",
    },
}

nested_employee_name: object = (
    nested_dictionary_structure[
        "employee"
    ]["name"]
)

print(
    f"Nested employee name: "
    f"{nested_employee_name}"
)


# Dictionaries can contain other dictionaries as values.


# =============================================================================
# Example 31: Heterogeneous Values
# =============================================================================

heterogeneous_dictionary_values: dict[str, object] = {
    "integer": 100,
    "float": 3.14,
    "text": "Python",
    "boolean": True,
    "tuple": (1, 2),
    "list": [10, 20],
}

print(
    heterogeneous_dictionary_values
)


# Dictionary values can contain different Python data types.


# =============================================================================
# Example 32: Hashable Keys
# =============================================================================

hashable_key_dictionary: dict[object, str] = {
    100: "integer key",
    "Python": "string key",
    (1, 2): "tuple key",
}

print(
    hashable_key_dictionary
)


# Dictionary keys must be hashable.
#
# Common hashable keys include:
#
#     int
#     float
#     complex
#     str
#     tuple (when its elements are hashable)
#     frozenset
#
# Mutable types such as list, set, and dictionary cannot be keys.


# =============================================================================
# Example 33: Mutable Key Is Not Allowed
# =============================================================================

invalid_mutable_key_dictionary: dict[object, str] = {}

# The following operation is invalid:
#
#     invalid_mutable_key_dictionary[[1, 2]] = "value"
#
# Lists are unhashable and therefore cannot be dictionary keys.


# =============================================================================
# Example 34: Frozenset as a Dictionary Key
# =============================================================================

frozenset_dictionary_key: frozenset[str] = frozenset({
    "read",
    "write",
})

frozenset_key_mapping: dict[frozenset[str], str] = {
    frozenset_dictionary_key: "Permissions"
}

print(
    frozenset_key_mapping
)


# Frozensets are hashable and can therefore be dictionary keys.


# =============================================================================
# Example 35: Dictionary Merging With |
# =============================================================================

dictionary_merge_left: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_merge_right: dict[str, int] = {
    "SQL": 20,
    "Airflow": 3,
}

dictionary_merge_result: dict[str, int] = (
    dictionary_merge_left
    | dictionary_merge_right
)

print(
    f"Merged dictionary: "
    f"{dictionary_merge_result}"
)


# When duplicate keys exist, the right-hand dictionary wins.


# =============================================================================
# Example 36: Dictionary Update With |=
# =============================================================================

dictionary_inplace_merge: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_inplace_merge |= {
    "SQL": 20,
    "Airflow": 3,
}

print(
    f"After |= : {dictionary_inplace_merge}"
)


# `|=` updates the existing dictionary in place.


# =============================================================================
# Example 37: Dictionary Unpacking
# =============================================================================

dictionary_unpacking_first: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_unpacking_second: dict[str, int] = {
    "Airflow": 3,
    "Spark": 4,
}

dictionary_unpacking_result: dict[str, int] = {
    **dictionary_unpacking_first,
    **dictionary_unpacking_second,
}

print(
    f"Unpacked dictionary: "
    f"{dictionary_unpacking_result}"
)


# `**` unpacks key-value pairs from a dictionary into another dictionary.


# =============================================================================
# Example 38: Dictionary Unpacking With Duplicate Keys
# =============================================================================

dictionary_unpacking_override_first: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_unpacking_override_second: dict[str, int] = {
    "SQL": 20,
    "Airflow": 3,
}

dictionary_unpacking_override_result: dict[str, int] = {
    **dictionary_unpacking_override_first,
    **dictionary_unpacking_override_second,
}

print(
    f"Override result: "
    f"{dictionary_unpacking_override_result}"
)


# Later unpacked dictionaries override earlier duplicate keys.


# =============================================================================
# Example 39: Dictionary Comprehension
# =============================================================================

dictionary_comprehension_result: dict[int, int] = {
    dictionary_square_number: (
        dictionary_square_number
        ** 2
    )
    for dictionary_square_number in range(1, 6)
}

print(
    f"Dictionary comprehension: "
    f"{dictionary_comprehension_result}"
)


# General structure:
#
#     {key: value for item in iterable}


# =============================================================================
# Example 40: Dictionary From Two Iterables
# =============================================================================

dictionary_key_source: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

dictionary_value_source: list[int] = [
    1,
    2,
    3,
]

dictionary_from_pairs: dict[str, int] = dict(
    zip(
        dictionary_key_source,
        dictionary_value_source,
    )
)

print(
    f"Dictionary from zip(): "
    f"{dictionary_from_pairs}"
)


# `zip()` pairs corresponding elements.
#
# `dict()` converts those pairs into a dictionary.


# =============================================================================
# Example 41: Dictionary Equality
# =============================================================================

dictionary_equality_left: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_equality_right: dict[str, int] = {
    "SQL": 2,
    "Python": 1,
}

dictionary_equality_result: bool = (
    dictionary_equality_left
    == dictionary_equality_right
)

print(
    f"Equal dictionaries: "
    f"{dictionary_equality_result}"
)


# Dictionary equality compares key-value mappings.
#
# Insertion order does not affect equality.


# =============================================================================
# Example 42: Dictionary Identity
# =============================================================================

dictionary_identity_source: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

dictionary_identity_copy: dict[str, int] = dict(
    dictionary_identity_source
)

dictionary_identity_result: bool = (
    dictionary_identity_source
    is dictionary_identity_copy
)

print(
    f"Same dictionary object: "
    f"{dictionary_identity_result}"
)


# `==` compares dictionary contents.
#
# `is` compares object identity.


# =============================================================================
# Example 43: Dictionary Mutability
# =============================================================================

mutable_dictionary_example: dict[str, int] = {
    "Python": 1,
    "SQL": 2,
}

mutable_dictionary_example["Airflow"] = 3

print(
    f"Modified dictionary: "
    f"{mutable_dictionary_example}"
)


# Dictionaries are mutable.
#
# Key-value pairs can be added, modified, or removed after creation.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `dict` represents a mutable mapping of unique keys to values.

✓ Dictionaries preserve insertion order.

✓ `{}` creates an empty dictionary.

✓ A type annotation alone does not initialize a dictionary.

✓ Dictionary keys must be unique.

✓ If a key is repeated, the later value replaces the earlier value.

✓ Dictionary keys must be hashable.

✓ Dictionary values can be of almost any Python type.

✓ Dictionaries can contain heterogeneous values.

✓ Dictionaries support nested dictionaries.

✓ `type()` identifies the concrete type.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of key-value pairs.

✓ Direct lookup uses:
      dictionary[key]

✓ Missing keys cause KeyError during direct lookup.

✓ `get()` provides safer key lookup.

✓ `get(key, default)` provides a fallback value.

✓ Assignment to a new key creates a new entry.

✓ Assignment to an existing key replaces its value.

✓ `update()` adds or replaces key-value pairs.

✓ `in` checks dictionary keys.

✓ `.values()` can be used to check dictionary values.

✓ `.keys()` returns a dynamic keys view.

✓ `.values()` returns a dynamic values view.

✓ `.items()` provides key-value pairs.

✓ Iterating directly over a dictionary iterates over keys.

✓ `pop()` removes a specified key and returns its value.

✓ `popitem()` removes and returns the last inserted key-value pair.

✓ `clear()` removes all entries.

✓ `copy()` creates a shallow copy.

✓ Dictionaries support nested structures.

✓ `|` merges dictionaries.

✓ `|=` updates a dictionary in place.

✓ `**` performs dictionary unpacking.

✓ Dictionary comprehensions create dictionaries dynamically.

✓ `zip()` can combine corresponding keys and values.

✓ Dictionaries are mutable.

✓ `==` compares key-value contents.

✓ `is` compares object identity.

✓ Lists, sets, and dictionaries cannot be dictionary keys because they
  are unhashable.

✓ Tuples can be dictionary keys when all of their elements are hashable.

✓ Frozensets can be dictionary keys.

✓ Hashability, mutability, equality, identity, and conversion are covered
  separately under Type Behaviour.
"""


# =============================================================================
# End of File
# =============================================================================