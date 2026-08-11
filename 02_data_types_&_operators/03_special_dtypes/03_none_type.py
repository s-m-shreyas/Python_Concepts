"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Special Data Types

Data Type
---------
NoneType (`None`)

Overview
--------
`None` represents the absence of a value.

It is commonly used when:

    - A value is intentionally absent.
    - A function has no meaningful return value.
    - A variable has no value yet.
    - A value is unavailable.
    - A special "no result" state needs to be represented.
    - A sentinel value is required.

Important distinction:

    None
        -> the actual singleton object

    NoneType
        -> the type of the None object

Python has exactly one None object.

This file covers:

    - None value
    - Default and non-default values
    - NoneType
    - type()
    - Identity
    - Boolean behaviour
    - Functions returning None
    - None as a variable value
    - None inside collections
    - Falsy values
    - None as a sentinel
    - Function parameters
    - str()
    - repr()
    - Hashability
    - id()
"""


# =============================================================================
# 01. None Value
# =============================================================================

none_basic_value: None = None

print(
    f"Value: {none_basic_value!r}"
)


# None represents the absence of a value.


# =============================================================================
# 02. Default and Non-Default Values
# =============================================================================

none_default_value: None = None
none_non_default_value: str = "Python"

print(
    f"Default None value: "
    f"{none_default_value!r}"
)

print(
    f"Non-default value: "
    f"{none_non_default_value!r}"
)


# None itself represents the absence of a value.
#
# A non-None value represents an actual value being present.


# =============================================================================
# 03. Type of None
# =============================================================================

none_type_example: None = None

print(
    f"Value: "
    f"{none_type_example!r}"
)

print(
    f"Type: "
    f"{type(none_type_example)}"
)


# Expected:
#
#     <class 'NoneType'>


# =============================================================================
# 04. NoneType Class
# =============================================================================

none_type_class: type[None] = type(None)

print(
    f"NoneType: "
    f"{none_type_class}"
)

print(
    f"Type name: "
    f"{none_type_class.__name__!r}"
)


# `type(None)` gives the class representing NoneType.


# =============================================================================
# 05. None Is a Singleton
# =============================================================================

none_singleton_reference_a: None = None
none_singleton_reference_b: None = None
none_singleton_reference_c: None = None

print(
    f"A is B: "
    f"{none_singleton_reference_a is none_singleton_reference_b}"
)

print(
    f"B is C: "
    f"{none_singleton_reference_b is none_singleton_reference_c}"
)

print(
    f"A is C: "
    f"{none_singleton_reference_a is none_singleton_reference_c}"
)


# Python has only one None object.
#
# Multiple variables can reference that same object.


# =============================================================================
# 06. Explicit None Check
# =============================================================================

none_explicit_check_value: None = None

if none_explicit_check_value is None:
    print(
        "Value is None"
    )
else:
    print(
        "Value is not None"
    )


# `is None` is the standard Python pattern for checking None.


# =============================================================================
# 07. None and id()
# =============================================================================

none_id_reference_one: None = None
none_id_reference_two: None = None

none_first_id: int = id(
    none_id_reference_one
)

none_second_id: int = id(
    none_id_reference_two
)

print(
    f"First id: "
    f"{none_first_id}"
)

print(
    f"Second id: "
    f"{none_second_id}"
)

print(
    f"Same id: "
    f"{none_first_id == none_second_id}"
)


# Both references point to the same None object.


# =============================================================================
# 08. None and Boolean Behaviour
# =============================================================================

none_boolean_value: None = None

none_boolean_result: bool = bool(
    none_boolean_value
)

print(
    f"bool(None): "
    f"{none_boolean_result}"
)


# None is falsy.


# =============================================================================
# 09. None and Other Falsy Values
# =============================================================================

none_falsy_integer: int = 0
none_falsy_boolean: bool = False
none_falsy_string: str = ""
none_falsy_list: list[object] = []
none_falsy_tuple: tuple[()] = ()
none_falsy_set: set[object] = set()
none_falsy_dictionary: dict[object, object] = {}

print(
    f"None:          {bool(None)}"
)

print(
    f"0:             {bool(none_falsy_integer)}"
)

print(
    f"False:         {bool(none_falsy_boolean)}"
)

print(
    f"Empty string:  {bool(none_falsy_string)}"
)

print(
    f"Empty list:    {bool(none_falsy_list)}"
)

print(
    f"Empty tuple:   {bool(none_falsy_tuple)}"
)

print(
    f"Empty set:     {bool(none_falsy_set)}"
)

print(
    f"Empty dict:    {bool(none_falsy_dictionary)}"
)


# All of these are falsy.
#
# However, falsy does NOT mean None.
#
# They are different values with different types.


# =============================================================================
# 10. None and Numeric Zero
# =============================================================================

none_numeric_zero: int = 0

print(
    f"None: "
    f"{None!r}"
)

print(
    f"Zero: "
    f"{none_numeric_zero!r}"
)

print(
    f"None type: "
    f"{type(None).__name__!r}"
)

print(
    f"Zero type: "
    f"{type(none_numeric_zero).__name__!r}"
)


# None:
#     absence of a value
#
# 0:
#     numeric value equal to zero


# =============================================================================
# 11. None and Boolean False
# =============================================================================

none_false_value: bool = False

print(
    f"None: "
    f"{None!r}"
)

print(
    f"False: "
    f"{none_false_value!r}"
)

print(
    f"None type: "
    f"{type(None).__name__!r}"
)

print(
    f"False type: "
    f"{type(none_false_value).__name__!r}"
)


# None:
#     absence of a value
#
# False:
#     Boolean false


# =============================================================================
# 12. None and Empty String
# =============================================================================

none_empty_text_value: str = ""

print(
    f"None: "
    f"{None!r}"
)

print(
    f"Empty string: "
    f"{none_empty_text_value!r}"
)

print(
    f"None type: "
    f"{type(None).__name__!r}"
)

print(
    f"String type: "
    f"{type(none_empty_text_value).__name__!r}"
)


# Empty string:
#     a string containing zero characters
#
# None:
#     absence of a value


# =============================================================================
# 13. None and Empty Collections
# =============================================================================

none_empty_list_value: list[object] = []
none_empty_tuple_value: tuple[()] = ()
none_empty_set_value: set[object] = set()
none_empty_dictionary_value: dict[object, object] = {}

print(
    f"Empty list: "
    f"{none_empty_list_value!r}"
)

print(
    f"Empty tuple: "
    f"{none_empty_tuple_value!r}"
)

print(
    f"Empty set: "
    f"{none_empty_set_value!r}"
)

print(
    f"Empty dictionary: "
    f"{none_empty_dictionary_value!r}"
)


# Empty collections are actual objects containing zero elements.
#
# None represents the absence of a value.


# =============================================================================
# 14. None Inside a List
# =============================================================================

none_list_container: list[object] = [
    "Python",
    None,
    100,
]

print(
    f"List: "
    f"{none_list_container!r}"
)


# None can exist as an element inside a list.


# =============================================================================
# 15. None Inside a Tuple
# =============================================================================

none_tuple_container: tuple[object, ...] = (
    "Python",
    None,
    100,
)

print(
    f"Tuple: "
    f"{none_tuple_container!r}"
)


# None can exist as an element inside a tuple.


# =============================================================================
# 16. None Inside a Set
# =============================================================================

none_set_container: set[object] = {
    None,
    "Python",
    100,
}

print(
    f"Set: "
    f"{none_set_container!r}"
)


# None is hashable and can therefore be stored in a set.


# =============================================================================
# 17. None as a Dictionary Value
# =============================================================================

none_dictionary_value_container: dict[str, object] = {
    "name": "Python",
    "version": None,
}

print(
    f"Dictionary: "
    f"{none_dictionary_value_container!r}"
)


# None is commonly used as a dictionary value when information is absent.


# =============================================================================
# 18. None as a Dictionary Key
# =============================================================================

none_dictionary_key_container: dict[None, str] = {
    None: "No value supplied",
}

print(
    f"Dictionary: "
    f"{none_dictionary_key_container!r}"
)


# None is hashable, so it can be used as a dictionary key.


# =============================================================================
# 19. None Hashability
# =============================================================================

none_hashable_value: None = None

none_hash_result: int = hash(
    none_hashable_value
)

print(
    f"Hash: "
    f"{none_hash_result}"
)


# None is hashable.


# =============================================================================
# 20. Function Without Explicit Return
# =============================================================================

def function_without_explicit_return():
    print(
        "Function executed"
    )


none_implicit_return_result: None = (
    function_without_explicit_return()
)

print(
    f"Returned value: "
    f"{none_implicit_return_result!r}"
)


# A function that reaches the end without an explicit return statement
# returns None.


# =============================================================================
# 21. Function With Explicit return None
# =============================================================================

def function_with_explicit_none():
    return None


none_explicit_return_result: None = (
    function_with_explicit_none()
)

print(
    f"Returned value: "
    f"{none_explicit_return_result!r}"
)


# A function can explicitly return None.


# =============================================================================
# 22. None as an Initial Placeholder
# =============================================================================

none_initial_placeholder: None | str = None

print(
    f"Initial value: "
    f"{none_initial_placeholder!r}"
)

none_initial_placeholder = "Available"

print(
    f"Updated value: "
    f"{none_initial_placeholder!r}"
)


# The type hint reflects that the variable can contain:
#
#     None
#     str


# =============================================================================
# 23. None as a Function Parameter
# =============================================================================

def display_optional_value(
    optional_parameter: str | None = None,
) -> None:
    print(
        f"Value: "
        f"{optional_parameter!r}"
    )


display_optional_value()

display_optional_value(
    "Python"
)


# None is commonly used as a default value for optional parameters.


# =============================================================================
# 24. None as a Sentinel
# =============================================================================

none_sentinel_marker: None = None

if none_sentinel_marker is None:
    print(
        "No value is available"
    )


# None can be used as a sentinel to represent a special state such as:
#
#     no value
#     not available
#     not supplied
#     not calculated


# =============================================================================
# 25. str(None)
# =============================================================================

none_string_conversion_source: None = None

none_string_conversion_result: str = str(
    none_string_conversion_source
)

print(
    f"str(None): "
    f"{none_string_conversion_result!r}"
)


# str(None) produces:
#
#     "None"
#
# This is a string containing the characters N-o-n-e.
#
# It is not the None object.


# =============================================================================
# 26. repr(None)
# =============================================================================

none_representation_example: None = None

none_repr_result: str = repr(
    none_representation_example
)

print(
    f"repr(None): "
    f"{none_repr_result!r}"
)


# repr(None) produces:
#
#     'None'


# =============================================================================
# 27. None and Variable Definition
# =============================================================================

none_defined_reference: None = None

print(
    f"Value: "
    f"{none_defined_reference!r}"
)


# A variable containing None is still defined.
#
# This differs from a variable that has never been created.


# =============================================================================
# 28. None and Methods
# =============================================================================

none_method_reference: None = None

print(
    f"Type: "
    f"{type(none_method_reference)}"
)


# None does not provide arbitrary methods.
#
# Attempting something such as:
#
#     none_method_reference.some_method()
#
# would raise AttributeError.


# =============================================================================
# 29. None in Conditional Assignment
# =============================================================================

none_conditional_value: str | None = None

none_status_message: str = (
    "Available"
    if none_conditional_value is not None
    else "Unavailable"
)

print(
    f"Status: "
    f"{none_status_message!r}"
)


# `is not None` is useful when a value should be processed only when
# it actually exists.


# =============================================================================
# 30. None and Identity
# =============================================================================

none_identity_candidate_a: None = None
none_identity_candidate_b: None = None

none_identity_result: bool = (
    none_identity_candidate_a is none_identity_candidate_b
)

print(
    f"Same object: "
    f"{none_identity_result}"
)


# `is` checks object identity.
#
# Since None is a singleton, references to None point to the same object.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `None` represents the absence of a value.

✓ The type of None is `NoneType`.

✓ `type(None)` gives the NoneType class.

✓ Python has exactly one None singleton object.

✓ `is None` is the standard way to check whether a value is None.

✓ `is not None` is the standard way to check that a value is not None.

✓ `is` checks object identity.

✓ None is falsy:

      bool(None) -> False

✓ Falsy does NOT mean None.

✓ Other falsy values include:

      0
      False
      ""
      []
      ()
      set()
      {}

✓ These are different values with different types.

✓ None can be stored inside:

      list
      tuple
      set
      dictionary

✓ None is hashable.

✓ None can therefore be:

      a set element
      a dictionary key
      a dictionary value

✓ A function without an explicit return statement returns None.

✓ A function can explicitly return None.

✓ None is commonly used as:

      an initial placeholder
      an optional parameter default
      a sentinel
      an unavailable value
      a missing value
      a "no result" value

✓ `str(None)` produces:

      "None"

✓ `repr(None)` produces:

      "None"

Main conceptual distinction:

      None
          absence of a value

      0
          numeric zero

      False
          Boolean false

      ""
          empty string

      []
          empty list

      ()
          empty tuple

      set()
          empty set

      {}
          empty dictionary

These values can all be falsy while representing completely different
concepts.
"""


# =============================================================================
# End of File
# =============================================================================