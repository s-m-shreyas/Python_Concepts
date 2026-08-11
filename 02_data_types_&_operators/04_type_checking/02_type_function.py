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
type() - Function Behaviour

Overview
--------
The built-in `type()` function has two major forms:

    1. type(object)

    2. type(name, bases, namespace)

The first form is used to inspect an object's exact runtime type.

The second form dynamically creates a new class.

This file focuses on the functional behaviour of `type()`.

This file covers:

    - type() as a built-in
    - type() with one argument
    - type() return value
    - exact type checking
    - type() with variables
    - type() with expressions
    - type() with functions
    - type() with classes
    - inheritance
    - type() vs isinstance()
    - multiple inheritance
    - dynamic class creation
    - dynamic attributes
    - dynamic methods
    - dynamic inheritance
    - name, bases and namespace
"""


# =============================================================================
# Imports
# =============================================================================

from typing import Any, Mapping


# =============================================================================
# 01. type() Is a Built-in
# =============================================================================

type_builtin_reference: Any = type

print(
    f"type object: "
    f"{type_builtin_reference!r}"
)

print(
    f"type object's type: "
    f"{type(type_builtin_reference)!r}"
)


# `type` is itself an object.
#
# It is used for:
#
#     - runtime type inspection
#     - dynamic class creation


# =============================================================================
# 02. type() With One Argument
# =============================================================================

type_single_argument_value: int = 500

type_single_argument_result: type = type(
    type_single_argument_value
)

print(
    f"Value: "
    f"{type_single_argument_value!r}"
)

print(
    f"Detected type: "
    f"{type_single_argument_result}"
)


# Basic form:
#
#     type(object)


# =============================================================================
# 03. type() Returns the Exact Runtime Type
# =============================================================================

type_runtime_float_value: float = 25.5

type_runtime_float_result: type = type(
    type_runtime_float_value
)

print(
    f"Runtime type: "
    f"{type_runtime_float_result}"
)

print(
    f"Type name: "
    f"{type_runtime_float_result.__name__!r}"
)


# type() returns the object's exact runtime class.


# =============================================================================
# 04. Exact Type Checking
# =============================================================================

type_exact_integer_value: int = 100

type_exact_integer_result: bool = (
    type(type_exact_integer_value) is int
)

print(
    f"Exact int type: "
    f"{type_exact_integer_result}"
)


# `type(value) is SomeType`
#
# performs an exact type comparison.


# =============================================================================
# 05. Exact Type Checking With Another Type
# =============================================================================

type_exact_decimal_value: float = 12.75

type_exact_decimal_result: bool = (
    type(type_exact_decimal_value) is float
)

print(
    f"Exact float type: "
    f"{type_exact_decimal_result}"
)


# =============================================================================
# 06. type() and Expressions
# =============================================================================

type_expression_number_a: int = 20
type_expression_number_b: float = 5.5

type_expression_result: type = type(
    type_expression_number_a
    + type_expression_number_b
)

print(
    f"Expression type: "
    f"{type_expression_result}"
)


# The expression is evaluated first.
#
# Then type() examines the resulting object.


# =============================================================================
# 07. type() and Function Objects
# =============================================================================

def type_function_sample() -> str:
    return "Python"


type_function_object_result: type = type(
    type_function_sample
)

print(
    f"Function object type: "
    f"{type_function_object_result}"
)


# type(function_name)
#
# examines the function object itself.


# =============================================================================
# 08. type() and Function Return Values
# =============================================================================

def type_function_return_sample() -> int:
    return 250


type_function_return_result: type = type(
    type_function_return_sample()
)

print(
    f"Returned value type: "
    f"{type_function_return_result}"
)


# Compare:
#
#     type(function_name)
#
# with:
#
#     type(function_name())
#
# They inspect different objects.


# =============================================================================
# 09. User-Defined Parent Class
# =============================================================================

class TypeFunctionParent:
    """Parent class used for inheritance examples."""


type_parent_instance: TypeFunctionParent = (
    TypeFunctionParent()
)

type_parent_result: type = type(
    type_parent_instance
)

print(
    f"Parent instance type: "
    f"{type_parent_result}"
)


# =============================================================================
# 10. User-Defined Child Class
# =============================================================================

class TypeFunctionChild(TypeFunctionParent):
    """Child class used for inheritance examples."""


type_child_instance: TypeFunctionChild = (
    TypeFunctionChild()
)

type_child_result: type = type(
    type_child_instance
)

print(
    f"Child instance type: "
    f"{type_child_result}"
)


# type() reports the actual class used to create the object.


# =============================================================================
# 11. type() and Inheritance
# =============================================================================

type_inheritance_exact_result: bool = (
    type(type_child_instance) is TypeFunctionParent
)

print(
    f"Child exact type is parent: "
    f"{type_inheritance_exact_result}"
)


# Result:
#
#     False
#
# type() checks the exact runtime type.
#
# It does not consider a parent class to be the exact type.


# =============================================================================
# 12. isinstance() and Inheritance
# =============================================================================

type_inheritance_instance_result: bool = (
    isinstance(
        type_child_instance,
        TypeFunctionParent,
    )# pyright: ignore[reportUnnecessaryIsInstance]
)

print(
    f"Child is instance of parent: "
    f"{type_inheritance_instance_result}"
)


# isinstance() considers inheritance.
#
# This is one of the major differences between:
#
#     type()
#
# and:
#
#     isinstance()


# =============================================================================
# 13. type() vs isinstance()
# =============================================================================

class TypeComparisonParent:
    """Parent class used for comparison."""


class TypeComparisonChild(TypeComparisonParent):
    """Child class used for comparison."""


type_comparison_instance: TypeComparisonChild = (
    TypeComparisonChild()
)

type_comparison_exact_result: bool = (
    type(type_comparison_instance)
    is TypeComparisonParent
)

type_comparison_inheritance_result: bool = (
    isinstance(
        type_comparison_instance,
        TypeComparisonParent,
    )# pyright: ignore[reportUnnecessaryIsInstance]
)

print(
    f"type() exact check: "
    f"{type_comparison_exact_result}"
)

print(
    f"isinstance() inheritance check: "
    f"{type_comparison_inheritance_result}"
)


# Important:
#
# type():
#     exact runtime type
#
# isinstance():
#     compatible type including inheritance


# =============================================================================
# 14. Multiple Levels of Inheritance
# =============================================================================

class TypeHierarchyRoot:
    """Root class."""


class TypeHierarchyMiddle(TypeHierarchyRoot):
    """Middle class."""


class TypeHierarchyLeaf(TypeHierarchyMiddle):
    """Leaf class."""


type_hierarchy_instance: TypeHierarchyLeaf = (
    TypeHierarchyLeaf()
)

type_hierarchy_runtime_result: type = type(
    type_hierarchy_instance
)

print(
    f"Runtime type: "
    f"{type_hierarchy_runtime_result}"
)

print(
    f"Is root: "
    f"{isinstance(
        type_hierarchy_instance,
        TypeHierarchyRoot,
    )}"# pyright: ignore[reportUnnecessaryIsInstance]
)

print(
    f"Is middle: "
    f"{isinstance(
        type_hierarchy_instance,
        TypeHierarchyMiddle,
    )}"# pyright: ignore[reportUnnecessaryIsInstance]
)

print(
    f"Is leaf: "
    f"{isinstance(
        type_hierarchy_instance,
        TypeHierarchyLeaf,
    )}"# pyright: ignore[reportUnnecessaryIsInstance]
)


# type() reports only the exact runtime class.
#
# isinstance() can recognize the entire inheritance chain.


# =============================================================================
# 15. isinstance() With Multiple Types
# =============================================================================

type_multiple_check_value: str = "Python"

type_multiple_check_result: bool = isinstance(
    type_multiple_check_value,
    (int, str),
)# pyright: ignore[reportUnnecessaryIsInstance]

print(
    f"Matches int or str: "
    f"{type_multiple_check_result}"
)


# isinstance() can accept a tuple of possible types.
#
# type() does not provide this subclass-aware checking behaviour.


# =============================================================================
# 16. type() Does Not Perform Subclass Checking
# =============================================================================

class TypeSubclassBase:
    """Base class."""


class TypeSubclassDerived(TypeSubclassBase):
    """Derived class."""


type_subclass_instance: TypeSubclassDerived = (
    TypeSubclassDerived()
)

type_subclass_exact_result: bool = (
    type(type_subclass_instance)
    is TypeSubclassBase
)

print(
    f"Exact base type: "
    f"{type_subclass_exact_result}"
)


# The result is False.
#
# The actual runtime type is TypeSubclassDerived.


# =============================================================================
# 17. isinstance() Performs Subclass-Aware Checking
# =============================================================================

type_subclass_instance_result: bool = (
    isinstance(
        type_subclass_instance,
        TypeSubclassBase,
    )# pyright: ignore[reportUnnecessaryIsInstance]
)

print(
    f"Subclass-aware check: "
    f"{type_subclass_instance_result}"
)


# =============================================================================
# 18. type() Can Inspect Classes
# =============================================================================

class TypeClassInspectionExample:
    """Example user-defined class."""


type_class_inspection_result: type = type(
    TypeClassInspectionExample
)

print(
    f"Type of class object: "
    f"{type_class_inspection_result}"
)


# A class is itself an object.
#
# Therefore:
#
#     type(SomeClass)
#
# normally produces:
#
#     <class 'type'>


# =============================================================================
# 19. type() of a Type Object
# =============================================================================

type_inner_class_reference: type = int

type_outer_class_result: type = type(
    type_inner_class_reference
)

print(
    f"Type of int class object: "
    f"{type_outer_class_result}"
)


# `int` is itself a class object.
#
# The type of the class object `int` is `type`.


# =============================================================================
# 20. Dynamic Class Creation
# =============================================================================

type_dynamic_class_name: str = (
    "DynamicExample"
)

type_dynamic_class_bases: tuple[type, ...] = ()

type_dynamic_class_namespace: dict[str, Any] = {
    "__module__": __name__,
}

TypeDynamicExample: type = type(
    type_dynamic_class_name,
    type_dynamic_class_bases,
    type_dynamic_class_namespace,
)

type_dynamic_instance: Any = (
    TypeDynamicExample()
)

print(
    f"Dynamic class: "
    f"{TypeDynamicExample}"
)

print(
    f"Dynamic instance type: "
    f"{type(type_dynamic_instance)}"
)


# Three-argument form:
#
#     type(name, bases, namespace)
#
# creates a new class dynamically.


# =============================================================================
# 21. Dynamic Class With an Attribute
# =============================================================================

type_attribute_namespace: dict[str, Any] = {
    "__module__": __name__,
    "category": "Data Engineering",
}

TypeDynamicCategory: type = type(
    "TypeDynamicCategory",
    (),
    type_attribute_namespace,
)

type_dynamic_category_instance: Any = (
    TypeDynamicCategory()
)

type_dynamic_category_attributes: Mapping[str, Any] = (
    TypeDynamicCategory.__dict__
)

print(
    f"Category: "
    f"{type_dynamic_category_attributes['category']!r}"
)

print(
    f"Instance type: "
    f"{type(type_dynamic_category_instance)}"
)


# The namespace supplied to type() becomes the class namespace.
#
# A class's __dict__ is exposed as a read-only mapping proxy.
#
# Therefore Mapping is more accurate than dict for __dict__.


# =============================================================================
# 22. Dynamic Class With a Method
# =============================================================================

def type_dynamic_description(
    dynamic_method_self: Any,
) -> str:
    return "Dynamic method executed"


type_dynamic_method_namespace: dict[str, Any] = {
    "__module__": __name__,
    "describe": type_dynamic_description,
}

TypeDynamicMethodClass: type = type(
    "TypeDynamicMethodClass",
    (),
    type_dynamic_method_namespace,
)

type_dynamic_method_instance: Any = (
    TypeDynamicMethodClass()
)

print(
    type_dynamic_method_instance.describe()
)


# A function placed in the class namespace becomes a method.


# =============================================================================
# 23. Dynamic Class With a Parent
# =============================================================================

class TypeDynamicParent:
    """Parent class for dynamic inheritance."""


type_dynamic_child_namespace: dict[str, Any] = {
    "__module__": __name__,
}

TypeDynamicChild: type = type(
    "TypeDynamicChild",
    (TypeDynamicParent,),
    type_dynamic_child_namespace,
)

type_dynamic_child_instance: Any = (
    TypeDynamicChild()
)

print(
    f"Exact type: "
    f"{type(type_dynamic_child_instance)}"
)

print(
    f"Is parent instance: "
    f"{isinstance(
        type_dynamic_child_instance,
        TypeDynamicParent,
    )}"
)


# The bases tuple determines the inheritance of the dynamic class.


# =============================================================================
# 24. Dynamic Class Name
# =============================================================================

type_named_dynamic_class: type = type(
    "AnalyticsObject",
    (),
    {
        "__module__": __name__,
    },
)

print(
    f"Class name: "
    f"{type_named_dynamic_class.__name__!r}"
)


# The first argument becomes the class name.


# =============================================================================
# 25. Dynamic Class Bases
# =============================================================================

class TypeDynamicBase:
    """Base class for dynamic class."""


type_dynamic_derived_class: type = type(
    "DerivedAnalyticsObject",
    (TypeDynamicBase,),
    {
        "__module__": __name__,
    },
)

print(
    f"Base classes: "
    f"{type_dynamic_derived_class.__bases__!r}"
)


# The second argument specifies the base classes.


# =============================================================================
# 26. Dynamic Class Namespace
# =============================================================================

type_namespace_dynamic_class: type = type(
    "NamespaceExample",
    (),
    {
        "__module__": __name__,
        "language": "Python",
        "version": 3,
    },
)

type_namespace_attributes: Mapping[str, Any] = (
    type_namespace_dynamic_class.__dict__
)

print(
    f"Language: "
    f"{type_namespace_attributes['language']!r}"
)

print(
    f"Version: "
    f"{type_namespace_attributes['version']!r}"
)


# The third argument contains the class namespace.
#
# The class __dict__ is a read-only mapping proxy.
#
# Therefore:
#
#     Mapping[str, Any]
#
# is appropriate for the exposed namespace.


# =============================================================================
# 27. type() With Built-in Types
# =============================================================================

type_builtin_integer_value: int = 100
type_builtin_string_value: str = "Python"
type_builtin_list_value: list[int] = [
    1,
    2,
    3,
]

print(
    f"Integer type: "
    f"{type(type_builtin_integer_value).__name__!r}"
)

print(
    f"String type: "
    f"{type(type_builtin_string_value).__name__!r}"
)

print(
    f"List type: "
    f"{type(type_builtin_list_value).__name__!r}"
)


# =============================================================================
# 28. type() and Exact Type Matching
# =============================================================================

type_matching_text_value: str = "Data"

type_matching_text_result: bool = (
    type(type_matching_text_value) is str
)

print(
    f"Exact string type: "
    f"{type_matching_text_result}"
)


# =============================================================================
# 29. type() and None
# =============================================================================

type_none_function_value: None = None

type_none_function_result: type[None] = type(
    type_none_function_value
)

print(
    f"None type: "
    f"{type_none_function_result}"
)


# =============================================================================
# 30. type() and bool
# =============================================================================

type_boolean_function_value: bool = True

type_boolean_function_result: type[bool] = type(
    type_boolean_function_value
)

print(
    f"Boolean type: "
    f"{type_boolean_function_result}"
)


# =============================================================================
# 31. Dynamic Class __name__
# =============================================================================

type_dynamic_name_class: type = type(
    "ReportingObject",
    (),
    {
        "__module__": __name__,
    },
)

type_dynamic_name_result: str = (
    type_dynamic_name_class.__name__
)

print(
    f"Dynamic class name: "
    f"{type_dynamic_name_result!r}"
)


# =============================================================================
# 32. Dynamic Class __module__
# =============================================================================

type_dynamic_module_class: type = type(
    "PipelineObject",
    (),
    {
        "__module__": __name__,
    },
)

type_dynamic_module_result: str = (
    type_dynamic_module_class.__module__
)

print(
    f"Dynamic class module: "
    f"{type_dynamic_module_result!r}"
)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ type() has two major forms:

      type(object)

      type(name, bases, namespace)


──────────────────────────────────────────────────────────────────────────────
ONE-ARGUMENT FORM
──────────────────────────────────────────────────────────────────────────────

      type(object)

returns the object's exact runtime type.


──────────────────────────────────────────────────────────────────────────────
EXACT TYPE CHECKING
──────────────────────────────────────────────────────────────────────────────

      type(value) is int

checks whether the exact runtime type is int.


──────────────────────────────────────────────────────────────────────────────
INHERITANCE
──────────────────────────────────────────────────────────────────────────────

type():

    exact runtime type

isinstance():

    compatible type
    +
    inheritance


──────────────────────────────────────────────────────────────────────────────
THREE-ARGUMENT FORM
──────────────────────────────────────────────────────────────────────────────

      type(name, bases, namespace)

creates a class dynamically.

name:
    class name

bases:
    parent classes

namespace:
    class attributes and methods


──────────────────────────────────────────────────────────────────────────────
CLASS NAMESPACE
──────────────────────────────────────────────────────────────────────────────

The dynamically supplied namespace becomes the class namespace.

A class's `__dict__` is exposed through a read-only mapping proxy.

Therefore:

    Mapping[str, Any]

is more appropriate than:

    dict[str, Any]

when referring to a class's `__dict__`.


──────────────────────────────────────────────────────────────────────────────
CORE CONCEPT
──────────────────────────────────────────────────────────────────────────────

type()
    │
    ├── type(object)
    │       │
    │       └── runtime type inspection
    │
    └── type(name, bases, namespace)
            │
            └── dynamic class creation
"""


# =============================================================================
# End of File
# =============================================================================