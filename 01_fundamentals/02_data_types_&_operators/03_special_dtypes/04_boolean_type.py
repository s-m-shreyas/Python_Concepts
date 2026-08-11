"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Special Data Types

Data Type
---------
bool

Overview
--------
`bool` represents a logical truth value.

Python has exactly two Boolean values:

    True
    False

Boolean values are commonly used in:

    - Conditions
    - Comparisons
    - Loops
    - Logical operations
    - Filtering
    - Control flow
    - Truth-value testing

Important:

    True
    False

are instances of the `bool` type.

Boolean values are also closely related to integers:

    True  behaves like 1
    False behaves like 0

However, `bool` is a distinct type.

This file covers:

    - Boolean values
    - Default and non-default values
    - bool type
    - type()
    - True and False
    - Boolean conversion
    - Truthy and falsy values
    - Comparisons
    - Logical operators
    - Short-circuit evaluation
    - bool as integers
    - Arithmetic with Boolean values
    - Functions returning bool
    - Boolean function parameters
    - Equality vs identity
    - Hashability
    - Boolean objects and id()
"""


# =============================================================================
# 01. Boolean Values
# =============================================================================

boolean_default_value: bool = False
boolean_non_default_value: bool = True

print(
    f"Default Boolean value: "
    f"{boolean_default_value!r}"
)

print(
    f"Non-default Boolean value: "
    f"{boolean_non_default_value!r}"
)


# Python has exactly two Boolean values:
#
#     True
#     False


# =============================================================================
# 02. Type of Boolean Values
# =============================================================================

boolean_type_true: bool = True
boolean_type_false: bool = False

print(
    f"True type: "
    f"{type(boolean_type_true)}"
)

print(
    f"False type: "
    f"{type(boolean_type_false)}"
)


# Expected:
#
#     <class 'bool'>


# =============================================================================
# 03. bool Type
# =============================================================================

boolean_type_class: type[bool] = bool

print(
    f"Boolean class: "
    f"{boolean_type_class}"
)

print(
    f"Boolean type name: "
    f"{boolean_type_class.__name__!r}"
)


# =============================================================================
# 04. True and False
# =============================================================================

boolean_true_value: bool = True
boolean_false_value: bool = False

print(
    f"True:  {boolean_true_value!r}"
)

print(
    f"False: {boolean_false_value!r}"
)


# True represents a logical true condition.
#
# False represents a logical false condition.


# =============================================================================
# 05. Boolean Conversion With bool()
# =============================================================================

boolean_integer_conversion: bool = bool(10)
boolean_zero_conversion: bool = bool(0)

print(
    f"bool(10): "
    f"{boolean_integer_conversion}"
)

print(
    f"bool(0): "
    f"{boolean_zero_conversion}"
)


# Non-zero integers are truthy.
#
# Zero is falsy.


# =============================================================================
# 06. Boolean Conversion From Strings
# =============================================================================

boolean_text_present: str = "Python"
boolean_text_empty: str = ""

boolean_text_present_result: bool = bool(
    boolean_text_present
)

boolean_text_empty_result: bool = bool(
    boolean_text_empty
)

print(
    f"bool('Python'): "
    f"{boolean_text_present_result}"
)

print(
    f"bool(''): "
    f"{boolean_text_empty_result}"
)


# Important:
#
# bool("False") is True
#
# because the string contains characters.
#
# bool() checks whether the object is truthy.
# It does not interpret the textual meaning of a string.


# =============================================================================
# 07. Boolean Conversion From Collections
# =============================================================================

boolean_list_with_values: list[int] = [10, 20]
boolean_empty_list: list[int] = []

boolean_tuple_with_values: tuple[int, ...] = (10, 20)
boolean_empty_tuple: tuple[()] = ()

print(
    f"bool([10, 20]): "
    f"{bool(boolean_list_with_values)}"
)

print(
    f"bool([]): "
    f"{bool(boolean_empty_list)}"
)

print(
    f"bool((10, 20)): "
    f"{bool(boolean_tuple_with_values)}"
)

print(
    f"bool(()): "
    f"{bool(boolean_empty_tuple)}"
)


# Non-empty collections are generally truthy.
#
# Empty collections are generally falsy.


# =============================================================================
# 08. Truthy and Falsy Values
# =============================================================================

boolean_truthy_integer: int = 100
boolean_falsy_integer: int = 0

boolean_truthy_text: str = "Data"
boolean_falsy_text: str = ""

boolean_truthy_list: list[int] = [1]
boolean_falsy_list: list[int] = []

print(
    f"Truthy integer: "
    f"{bool(boolean_truthy_integer)}"
)

print(
    f"Falsy integer: "
    f"{bool(boolean_falsy_integer)}"
)

print(
    f"Truthy string: "
    f"{bool(boolean_truthy_text)}"
)

print(
    f"Falsy string: "
    f"{bool(boolean_falsy_text)}"
)

print(
    f"Truthy list: "
    f"{bool(boolean_truthy_list)}"
)

print(
    f"Falsy list: "
    f"{bool(boolean_falsy_list)}"
)


# Truthiness allows Python to evaluate objects in Boolean contexts.


# =============================================================================
# 09. Boolean in an if Statement
# =============================================================================

boolean_condition_flag: bool = True

if boolean_condition_flag:
    print(
        "Condition is True"
    )
else:
    print(
        "Condition is False"
    )


# Boolean values are commonly used to control program flow.


# =============================================================================
# 10. Comparison Produces bool
# =============================================================================

boolean_comparison_left: int = 20
boolean_comparison_right: int = 10

boolean_comparison_result: bool = (
    boolean_comparison_left
    > boolean_comparison_right
)

print(
    f"Comparison result: "
    f"{boolean_comparison_result}"
)

print(
    f"Result type: "
    f"{type(boolean_comparison_result)}"
)


# Comparison operators return Boolean values.


# =============================================================================
# 11. Equality Comparison
# =============================================================================

boolean_equality_first: str = "Python"
boolean_equality_second: str = "Python"

boolean_equality_result: bool = (
    boolean_equality_first
    == boolean_equality_second
)

print(
    f"Equality result: "
    f"{boolean_equality_result}"
)


# `==` compares values.


# =============================================================================
# 12. Identity Comparison
# =============================================================================

boolean_identity_first: bool = True
boolean_identity_second: bool = True

boolean_identity_result: bool = (
    boolean_identity_first
    is boolean_identity_second
)

print(
    f"Identity result: "
    f"{boolean_identity_result}"
)


# `is` checks whether two references point to the same object.
#
# For Boolean values, True and False are singleton objects.


# =============================================================================
# 13. Logical AND
# =============================================================================

boolean_and_left: bool = True
boolean_and_right: bool = False

boolean_and_result: bool = (
    boolean_and_left
    and boolean_and_right
)

print(
    f"True and False: "
    f"{boolean_and_result}"
)


# `and` returns a truthy result only when both operands are truthy.


# =============================================================================
# 14. Logical OR
# =============================================================================

boolean_or_left: bool = True
boolean_or_right: bool = False

boolean_or_result: bool = (
    boolean_or_left
    or boolean_or_right
)

print(
    f"True or False: "
    f"{boolean_or_result}"
)


# `or` returns a truthy result when at least one operand is truthy.


# =============================================================================
# 15. Logical NOT
# =============================================================================

boolean_not_source: bool = True

boolean_not_result: bool = not boolean_not_source

print(
    f"not True: "
    f"{boolean_not_result}"
)


# `not` reverses the truth value.


# =============================================================================
# 16. Combining Logical Operators
# =============================================================================

boolean_logic_first: bool = True
boolean_logic_second: bool = False
boolean_logic_third: bool = True

boolean_logic_result: bool = (
    boolean_logic_first
    and boolean_logic_second
    or boolean_logic_third
)

print(
    f"Logical result: "
    f"{boolean_logic_result}"
)


# Parentheses should be used when they make the intended logic clearer.


# =============================================================================
# 17. Logical Operators Return Operands
# =============================================================================

boolean_operand_text: str = "Python"
boolean_operand_empty: str = ""

boolean_and_operand_result: str = (
    boolean_operand_text
    and boolean_operand_empty
)

boolean_or_operand_result: str = (
    boolean_operand_text
    or boolean_operand_empty
)

print(
    f"'Python' and '': "
    f"{boolean_and_operand_result!r}"
)

print(
    f"'Python' or '': "
    f"{boolean_or_operand_result!r}"
)


# Important:
#
# `and` and `or` do not necessarily return True or False.
#
# They return one of their operands.
#
# Use bool(...) when an actual Boolean result is required.


# =============================================================================
# 18. Converting Logical Results to bool
# =============================================================================

boolean_operand_source_a: str = "Python"
boolean_operand_source_b: str = ""

boolean_converted_and_result: bool = bool(
    boolean_operand_source_a
    and boolean_operand_source_b
)

boolean_converted_or_result: bool = bool(
    boolean_operand_source_a
    or boolean_operand_source_b
)

print(
    f"bool(and result): "
    f"{boolean_converted_and_result}"
)

print(
    f"bool(or result): "
    f"{boolean_converted_or_result}"
)


# =============================================================================
# 19. Short-Circuit Evaluation With and
# =============================================================================

def boolean_and_first_function() -> bool:
    print(
        "First function executed"
    )
    return False


def boolean_and_second_function() -> bool:
    print(
        "Second function executed"
    )
    return True


boolean_short_circuit_and_result: bool = (
    boolean_and_first_function()
    and boolean_and_second_function()
)

print(
    f"AND result: "
    f"{boolean_short_circuit_and_result}"
)


# Because the first operand is False,
# Python does not need to evaluate the second operand.


# =============================================================================
# 20. Short-Circuit Evaluation With or
# =============================================================================

def boolean_or_first_function() -> bool:
    print(
        "OR first function executed"
    )
    return True


def boolean_or_second_function() -> bool:
    print(
        "OR second function executed"
    )
    return False


boolean_short_circuit_or_result: bool = (
    boolean_or_first_function()
    or boolean_or_second_function()
)

print(
    f"OR result: "
    f"{boolean_short_circuit_or_result}"
)


# Because the first operand is True,
# Python does not need to evaluate the second operand.


# =============================================================================
# 21. bool and int Relationship
# =============================================================================

boolean_integer_like_true: int = True
boolean_integer_like_false: int = False

print(
    f"True as integer: "
    f"{boolean_integer_like_true}"
)

print(
    f"False as integer: "
    f"{boolean_integer_like_false}"
)


# True behaves numerically like 1.
# False behaves numerically like 0.


# =============================================================================
# 22. bool Is a Subclass of int
# =============================================================================

boolean_integer_relationship: bool = (
    issubclass(bool, int)
)# pyright: ignore[reportUnnecessaryIsInstance]

print(
    f"bool is subclass of int: "
    f"{boolean_integer_relationship}"
)


# Python defines bool as a subclass of int.


# =============================================================================
# 23. isinstance() With bool
# =============================================================================

boolean_instance_value: bool = True

print(
    f"Is bool instance: "
    f"{isinstance(boolean_instance_value, bool)}") # pyright: ignore[reportUnnecessaryIsInstance]


# =============================================================================
# 24. Boolean Arithmetic
# =============================================================================

boolean_arithmetic_true: bool = True
boolean_arithmetic_false: bool = False

boolean_sum_result: int = (
    boolean_arithmetic_true
    + boolean_arithmetic_false
)

boolean_product_result: int = (
    boolean_arithmetic_true
    * boolean_arithmetic_false
)

print(
    f"True + False: "
    f"{boolean_sum_result}"
)

print(
    f"True * False: "
    f"{boolean_product_result}"
)


# Since:
#
#     True  -> 1
#     False -> 0
#
# Boolean values participate in numeric operations.


# =============================================================================
# 25. Counting Boolean Conditions
# =============================================================================

boolean_condition_results: list[bool] = [
    True,
    False,
    True,
    True,
]

boolean_true_count: int = sum(
    boolean_condition_results
)

print(
    f"True count: "
    f"{boolean_true_count}"
)


# Because True behaves like 1 and False like 0,
# sum() can count True values.


# =============================================================================
# 26. Function Returning bool
# =============================================================================

def is_positive_number(
    numeric_candidate: int,
) -> bool:
    return numeric_candidate > 0


boolean_positive_result: bool = (
    is_positive_number(25)
)

print(
    f"Is positive: "
    f"{boolean_positive_result}"
)


# A function that represents a yes/no condition commonly returns bool.


# =============================================================================
# 27. Boolean Function Parameter
# =============================================================================

def display_feature_status(
    feature_enabled: bool,
) -> None:
    if feature_enabled:
        print(
            "Feature enabled"
        )
    else:
        print(
            "Feature disabled"
        )


display_feature_status(True)

display_feature_status(False)


# Type hints make the expected parameter type explicit.


# =============================================================================
# 28. Default Boolean Parameter
# =============================================================================

def show_processing_status(
    processing_enabled: bool = False,
) -> None:
    print(
        f"Processing enabled: "
        f"{processing_enabled}"
    )


show_processing_status()

show_processing_status(True)


# Default Boolean parameters are useful for optional behaviour.


# =============================================================================
# 29. Boolean Conversion From None
# =============================================================================

boolean_none_source: None = None

boolean_none_result: bool = bool(
    boolean_none_source
)

print(
    f"bool(None): "
    f"{boolean_none_result}"
)


# None is falsy.


# =============================================================================
# 30. Boolean Conversion From Float
# =============================================================================

boolean_float_positive: float = 3.14
boolean_float_zero: float = 0.0

print(
    f"bool(3.14): "
    f"{bool(boolean_float_positive)}"
)

print(
    f"bool(0.0): "
    f"{bool(boolean_float_zero)}"
)


# Non-zero numeric values are truthy.
#
# Zero numeric values are falsy.


# =============================================================================
# 31. Boolean Conversion From Dictionary
# =============================================================================

boolean_dictionary_values: dict[str, int] = {
    "Python": 100,
}

boolean_empty_dictionary_values: dict[str, int] = {}

print(
    f"bool(non-empty dict): "
    f"{bool(boolean_dictionary_values)}"
)

print(
    f"bool(empty dict): "
    f"{bool(boolean_empty_dictionary_values)}"
)


# Non-empty dictionaries are truthy.
#
# Empty dictionaries are falsy.


# =============================================================================
# 32. Boolean Hashability
# =============================================================================

boolean_hash_true: bool = True
boolean_hash_false: bool = False

boolean_true_hash: int = hash(
    boolean_hash_true
)

boolean_false_hash: int = hash(
    boolean_hash_false
)

print(
    f"Hash of True: "
    f"{boolean_true_hash}"
)

print(
    f"Hash of False: "
    f"{boolean_false_hash}"
)


# Boolean values are hashable.


# =============================================================================
# 33. Boolean as a Set Element
# =============================================================================

boolean_set_values: set[bool] = {
    True,
    False,
}

print(
    f"Boolean set: "
    f"{boolean_set_values!r}"
)


# =============================================================================
# 34. Boolean as a Dictionary Key
# =============================================================================

boolean_dictionary_keys: dict[bool, str] = {
    True: "Enabled",
    False: "Disabled",
}

print(
    f"Boolean dictionary: "
    f"{boolean_dictionary_keys!r}"
)


# Boolean values can be used as dictionary keys because they are hashable.


# =============================================================================
# 35. Boolean id()
# =============================================================================

boolean_id_true: bool = True
boolean_id_false: bool = False

boolean_true_object_id: int = id(
    boolean_id_true
)

boolean_false_object_id: int = id(
    boolean_id_false
)

print(
    f"True id: "
    f"{boolean_true_object_id}"
)

print(
    f"False id: "
    f"{boolean_false_object_id}"
)


# True and False are singleton Boolean objects.


# =============================================================================
# 36. Boolean Representation
# =============================================================================

boolean_representation_value: bool = True

print(
    f"str(True): "
    f"{str(boolean_representation_value)!r}"
)

print(
    f"repr(True): "
    f"{repr(boolean_representation_value)!r}"
)


# str() and repr() both produce:
#
#     'True'
#
# The returned value is a string.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `bool` represents logical truth values.

✓ Python has exactly two Boolean values:

      True
      False

✓ Their type is:

      bool

✓ `bool` is a subclass of `int`.

✓ Numerically:

      True  -> 1
      False -> 0

✓ Boolean values are hashable.

✓ Boolean values can be used as:

      set elements
      dictionary keys

✓ `bool()` converts an object's truth value into True or False.

✓ Common truthy values include:

      non-zero numbers
      non-empty strings
      non-empty lists
      non-empty tuples
      non-empty sets
      non-empty dictionaries

✓ Common falsy values include:

      None
      0
      0.0
      ""
      []
      ()
      set()
      {}

✓ `==` compares values.

✓ `is` compares object identity.

✓ `and` and `or` can return operands rather than actual bool values.

✓ `not` always produces a Boolean result.

✓ `and` and `or` use short-circuit evaluation.

✓ Comparison operators produce Boolean results.

✓ Boolean values can participate in arithmetic because bool is a subclass
  of int.

✓ `sum()` can be used to count True values.

✓ Functions that answer yes/no questions commonly return bool.

✓ Boolean parameters can have default values:

      flag: bool = False

Main idea:

      bool
        ↓
      logical truth value
        ↓
      True / False

Truthiness:

      object
        ↓
      bool(object)
        ↓
      True / False
"""


# =============================================================================
# End of File
# =============================================================================