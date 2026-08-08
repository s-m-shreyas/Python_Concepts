"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Special Data Types

Subcategory
-----------
Type Checking

Topic
-----
type() - Basic

Overview
--------
The built-in `type()` function is used to determine the type of an object.

Basic syntax:

    type(object)

It returns the class/type of the supplied object.

Examples:

    type(10)
    type(3.14)
    type("Python")
    type(True)
    type(None)

This file covers:

    - Basic type()
    - type() return value
    - Type objects
    - __name__
    - __module__
    - Built-in data types
    - User-defined types
    - Type comparison
    - Identity of type objects
    - Type annotations
    - type() with variables
    - type() with expressions
    - type() with functions
    - type() with collections
    - type() with None
    - type() vs value
    - type() and exact type checking
"""


# =============================================================================
# 01. Basic type()
# =============================================================================

type_basic_integer: int = 100

type_basic_result: type = type(
    type_basic_integer
)

print(
    f"Value: "
    f"{type_basic_integer!r}"
)

print(
    f"Type: "
    f"{type_basic_result}"
)


# type() returns the type object of the supplied object.


# =============================================================================
# 02. type() With Different Data Types
# =============================================================================

type_integer_value: int = 100
type_float_value: float = 25.5
type_complex_value: complex = 3 + 4j
type_string_value: str = "Python"
type_boolean_value: bool = True

print(
    f"Integer: "
    f"{type(type_integer_value)}"
)

print(
    f"Float: "
    f"{type(type_float_value)}"
)

print(
    f"Complex: "
    f"{type(type_complex_value)}"
)

print(
    f"String: "
    f"{type(type_string_value)}"
)

print(
    f"Boolean: "
    f"{type(type_boolean_value)}"
)


# =============================================================================
# 03. type() With None
# =============================================================================

type_none_value: None = None

type_none_result: type[None] = type(
    type_none_value
)

print(
    f"Value: "
    f"{type_none_value!r}"
)

print(
    f"Type: "
    f"{type_none_result}"
)


# Expected:
#
#     <class 'NoneType'>


# =============================================================================
# 04. type() Returns a Type Object
# =============================================================================

type_object_source: int = 500

type_object_result: type = type(
    type_object_source
)

print(
    f"Returned object: "
    f"{type_object_result!r}"
)

print(
    f"Returned object's type: "
    f"{type(type_object_result)!r}"
)


# Interesting:
#
#     type(500)
#         -> int
#
# and:
#
#     type(type(500))
#         -> type
#
# Classes themselves are objects.


# =============================================================================
# 05. __name__ of a Type
# =============================================================================

type_name_source: float = 15.75

type_name_result: type = type(
    type_name_source
)

print(
    f"Type object: "
    f"{type_name_result}"
)

print(
    f"Type name: "
    f"{type_name_result.__name__!r}"
)


# __name__ gives the class name as a string.


# =============================================================================
# 06. __module__ of a Type
# =============================================================================

type_module_source: str = "Python"

type_module_result: type = type(
    type_module_source
)

print(
    f"Type: "
    f"{type_module_result}"
)

print(
    f"Module: "
    f"{type_module_result.__module__!r}"
)


# Built-in types such as str, int and float belong to the `builtins` module.


# =============================================================================
# 07. Type Object Stored in a Variable
# =============================================================================

type_variable_source: int = 250

type_variable_result: type = type(
    type_variable_source
)

print(
    f"Detected type: "
    f"{type_variable_result}"
)

print(
    f"Type variable itself: "
    f"{type(type_variable_result)}"
)


# A type object can itself be stored in a variable.


# =============================================================================
# 08. Exact Type Comparison
# =============================================================================

type_exact_integer_value: int = 42

type_exact_integer_result: bool = (
    type(type_exact_integer_value) is int
)

print(
    f"Exact type is int: "
    f"{type_exact_integer_result}"
)


# type() can be used with `is` for exact type comparison.


# =============================================================================
# 09. Exact Type Comparison With Multiple Types
# =============================================================================

type_exact_float_value: float = 42.5

type_exact_float_result: bool = (
    type(type_exact_float_value) is float
)

print(
    f"Exact type is float: "
    f"{type_exact_float_result}"
)


# This checks whether the object's exact type is float.


# =============================================================================
# 10. Type Objects and Identity
# =============================================================================

type_identity_source_a: int = 10
type_identity_source_b: int = 20

type_identity_result: bool = (
    type(type_identity_source_a)
    is type(type_identity_source_b)
)

print(
    f"Both have same type object: "
    f"{type_identity_result}"
)


# Both objects have the same exact type:
#
#     int
#
# Therefore their returned type objects are identical.


# =============================================================================
# 11. Different Type Objects
# =============================================================================

type_difference_integer: int = 10
type_difference_text: str = "10"

type_difference_result: bool = (
    type(type_difference_integer)
    is type(type_difference_text)
)# pyright: ignore[reportUnnecessaryComparison]

print(
    f"Same type object: "
    f"{type_difference_result}"
)


# The values may look conceptually similar,
# but their types are different:
#
#     10
#         -> int
#
#     "10"
#         -> str


# =============================================================================
# 12. type() With an Expression
# =============================================================================

type_expression_left: int = 20
type_expression_right: float = 5.5

type_expression_result: type = type(
    type_expression_left
    + type_expression_right
)

print(
    f"Expression type: "
    f"{type_expression_result}"
)


# type() evaluates the expression first,
# then determines the type of its result.


# =============================================================================
# 13. type() With a Function Result
# =============================================================================

def type_function_result() -> float:
    return 12.5


type_function_detected: type = type(
    type_function_result()
)

print(
    f"Function result type: "
    f"{type_function_detected}"
)


# type() checks the type of the returned value,
# not the function definition itself.


# =============================================================================
# 14. type() of a Function Object
# =============================================================================

def type_function_object() -> str:
    return "Python"


type_function_object_result: type = type(
    type_function_object
)

print(
    f"Function object type: "
    f"{type_function_object_result}"
)


# Notice the difference:
#
#     type(function_name)
#         -> function type
#
#     type(function_name())
#         -> type of the returned value


# =============================================================================
# 15. type() With a List
# =============================================================================

type_list_value: list[int] = [
    10,
    20,
    30,
]

type_list_result: type = type(
    type_list_value
)

print(
    f"List type: "
    f"{type_list_result}"
)


# =============================================================================
# 16. type() With a Tuple
# =============================================================================

type_tuple_value: tuple[int, ...] = (
    10,
    20,
    30,
)

type_tuple_result: type = type(
    type_tuple_value
)

print(
    f"Tuple type: "
    f"{type_tuple_result}"
)


# =============================================================================
# 17. type() With a Set
# =============================================================================

type_set_value: set[int] = {
    10,
    20,
    30,
}

type_set_result: type = type(
    type_set_value
)

print(
    f"Set type: "
    f"{type_set_result}"
)


# =============================================================================
# 18. type() With a Dictionary
# =============================================================================

type_dictionary_value: dict[str, int] = {
    "Python": 100,
    "SQL": 90,
}

type_dictionary_result: type = type(
    type_dictionary_value
)

print(
    f"Dictionary type: "
    f"{type_dictionary_result}"
)


# =============================================================================
# 19. type() With Nested Objects
# =============================================================================

type_nested_value: list[dict[str, int]] = [
    {
        "Python": 100,
    }
]

type_nested_result: type = type(
    type_nested_value
)

print(
    f"Outer type: "
    f"{type_nested_result}"
)

print(
    f"Inner type: "
    f"{type(type_nested_value[0])}"
)


# type() checks the specific object supplied to it.


# =============================================================================
# 20. type() and Type Annotation
# =============================================================================

type_annotation_value: int = 500

type_annotation_detected: type = type(
    type_annotation_value
)

print(
    f"Runtime type: "
    f"{type_annotation_detected}"
)


# Type annotations do not perform runtime type checking.
#
# `type()` examines the actual runtime object.


# =============================================================================
# 21. Type Annotation vs Runtime Type
# =============================================================================

type_annotation_example: int = 100

type_runtime_result: type = type(
    type_annotation_example
)

print(
    f"Annotation: int"
)

print(
    f"Runtime type: "
    f"{type_runtime_result}"
)


# The annotation tells static type checkers what type is expected.
#
# type() tells us what type the runtime object actually has.


# =============================================================================
# 22. User-Defined Class
# =============================================================================

class TypeBasicExample:
    """Simple user-defined class."""


type_user_object: TypeBasicExample = (
    TypeBasicExample()
)

type_user_result: type = type(
    type_user_object
)

print(
    f"User-defined type: "
    f"{type_user_result}"
)

print(
    f"Type name: "
    f"{type_user_result.__name__!r}"
)


# type() works with user-defined objects as well.


# =============================================================================
# 23. User-Defined Type Module
# =============================================================================

type_user_module_result: str = (
    type_user_result.__module__
)

print(
    f"Module: "
    f"{type_user_module_result!r}"
)


# When the class is defined in this file,
# its module is normally `__main__` when executed directly.


# =============================================================================
# 24. type() of a Class
# =============================================================================

type_class_object_result: type = type(
    TypeBasicExample
)

print(
    f"Type of class object: "
    f"{type_class_object_result}"
)


# A class is itself an object.
#
# The type of a normal user-defined class is:
#
#     type


# =============================================================================
# 25. type() With Boolean Values
# =============================================================================

type_boolean_true: bool = True
type_boolean_false: bool = False

type_boolean_true_result: type[bool] = type(
    type_boolean_true
)

type_boolean_false_result: type[bool] = type(
    type_boolean_false
)

print(
    f"True type: "
    f"{type_boolean_true_result}"
)

print(
    f"False type: "
    f"{type_boolean_false_result}"
)


# =============================================================================
# 26. type() With Bytes
# =============================================================================

type_bytes_value: bytes = b"Python"

type_bytes_result: type = type(
    type_bytes_value
)

print(
    f"Bytes type: "
    f"{type_bytes_result}"
)


# =============================================================================
# 27. type() With Bytearray
# =============================================================================

type_bytearray_value: bytearray = bytearray(
    b"Python"
)

type_bytearray_result: type = type(
    type_bytearray_value
)

print(
    f"Bytearray type: "
    f"{type_bytearray_result}"
)


# =============================================================================
# 28. type() With Memoryview
# =============================================================================

type_memoryview_source: bytes = b"Python"

type_memoryview_value: memoryview = memoryview(
    type_memoryview_source
)

type_memoryview_result: type = type(
    type_memoryview_value
)

print(
    f"Memoryview type: "
    f"{type_memoryview_result}"
)


# =============================================================================
# 29. type() With Range
# =============================================================================

type_range_value: range = range(
    1,
    6,
)

type_range_result: type = type(
    type_range_value
)

print(
    f"Range type: "
    f"{type_range_result}"
)


# =============================================================================
# 30. type() With None
# =============================================================================

type_none_object: None = None

type_none_object_result: type[None] = type(
    type_none_object
)

print(
    f"None type: "
    f"{type_none_object_result}"
)

print(
    f"Type name: "
    f"{type_none_object_result.__name__!r}"
)


# =============================================================================
# 31. Comparing a Runtime Type With a Known Type
# =============================================================================

type_runtime_integer: int = 250

type_runtime_is_integer: bool = (
    type(type_runtime_integer) is int
)

print(
    f"Runtime object has exact int type: "
    f"{type_runtime_is_integer}"
)


# This is an exact type check.
#
# It does not check subclasses.


# =============================================================================
# 32. type() Does Not Inspect Variable Names
# =============================================================================

type_variable_name_example: int = 100

type_variable_name_result: type = type(
    type_variable_name_example
)

print(
    f"Variable name: "
    f"type_variable_name_example"
)

print(
    f"Detected type: "
    f"{type_variable_name_result}"
)


# type() examines the object stored in the variable,
# not the variable's name.


# =============================================================================
# 33. Type Object's Name
# =============================================================================

type_name_inspection_value: complex = 4 + 2j

type_name_inspection_result: type = type(
    type_name_inspection_value
)

print(
    f"Full type: "
    f"{type_name_inspection_result}"
)

print(
    f"Type name: "
    f"{type_name_inspection_result.__name__!r}"
)


# =============================================================================
# 34. Type Object's Module
# =============================================================================

type_module_inspection_value: int = 75

type_module_inspection_result: type = type(
    type_module_inspection_value
)

print(
    f"Type: "
    f"{type_module_inspection_result}"
)

print(
    f"Module: "
    f"{type_module_inspection_result.__module__!r}"
)


# =============================================================================
# 35. type() Is Itself a Type
# =============================================================================

type_function_result_object: type = type(
    100
)

type_type_result: type = type(
    type_function_result_object
)

print(
    f"Type of type(100): "
    f"{type_type_result}"
)


# This demonstrates the relationship:
#
#     100
#       ↓
#     int
#       ↓
#     type


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `type(object)` returns the runtime type of an object.

✓ Example:

      type(100)
          -> <class 'int'>

✓ The returned value is itself a type object.

✓ A type object can be stored in a variable.

✓ Type objects have useful attributes such as:

      __name__
      __module__

✓ Example:

      type(100).__name__
          -> 'int'

✓ `type()` works with:

      integers
      floats
      complex numbers
      strings
      booleans
      None
      lists
      tuples
      sets
      dictionaries
      bytes
      bytearray
      memoryview
      range
      user-defined objects
      functions

✓ `type()` can inspect:

      variables
      expressions
      function results
      function objects
      classes
      collection objects

✓ Important distinction:

      type(function_name)
          -> type of the function object

      type(function_name())
          -> type of the returned value

✓ `type()` checks the actual runtime object.

✓ Type annotations are mainly for static analysis and documentation.
  They do not themselves perform runtime type checking.

✓ Exact type comparison can be performed with:

      type(value) is int

✓ `type(value) is SomeType` checks the exact type.

✓ `isinstance()` should be learned separately when inheritance and
  subclass-aware checking are required.

Conceptual flow:

      object
        ↓
      type(object)
        ↓
      type object
        ↓
      __name__ / __module__

Example:

      value = 100

      type(value)
          ↓
      <class 'int'>
"""


# =============================================================================
# End of File
# =============================================================================