# type: ignore
"""
06_module_namespace.py

Topic:
    Module namespaces

Purpose:
    Understand what a module namespace is, what names it contains,
    how imported names become part of the namespace, and how Python
    resolves names inside a module.

Concepts covered:
    1. What a namespace is
    2. A module's namespace
    3. The `globals()` function
    4. Names defined directly in a module
    5. Imported names in a module namespace
    6. Module namespace as a mapping
    7. Accessing namespace entries
    8. Difference between module namespace and module object
    9. Functions and classes stored in the namespace
    10. Name rebinding
    11. Namespace isolation between modules
    12. Why module namespaces matter

Important:
    - Basic importing is covered in the previous files.
    - Module attributes are covered separately in:
          07_module_attributes.py
    - Module execution is covered separately in:
          08_module_execution.py
    - Module search and resolution are covered later.
"""


# =============================================================================
# 1. WHAT IS A NAMESPACE?
# =============================================================================

# A namespace is a mapping between names and the objects those names refer to.
#
# Conceptually:
#
#     name  ─────────→  object
#
# For example:
#
#     age  ──────────→  30
#     name ──────────→  "Python"
#
# A namespace prevents unrelated names from having to exist in one
# giant global pool.
#
# Python uses several namespaces, including:
#
#     - local namespaces
#     - global/module namespaces
#     - built-in namespace
#
# This file focuses specifically on the module namespace.


# =============================================================================
# 2. THE MODULE NAMESPACE
# =============================================================================

# Every Python module has its own namespace.
#
# This file itself is a module.
#
# Therefore, names defined at the top level of this file belong to this
# module's namespace.
#
# For example:

language = "Python"
version = 3


# These names now belong to this module's global namespace:
#
#     language
#     version


# =============================================================================
# 3. VIEWING THE CURRENT MODULE NAMESPACE
# =============================================================================

# Python provides the `globals()` function to access the current global
# namespace.
#
# At module level, `globals()` returns a dictionary representing the
# current module's global namespace.

namespace = globals()

print("Type of module namespace:")
print(type(namespace))


# The expected result is:
#
#     <class 'dict'>
#
# Therefore, the module's global namespace is represented as a dictionary.


# =============================================================================
# 4. NAMES WE DEFINED ARE STORED IN THE NAMESPACE
# =============================================================================

# We defined:
#
#     language = "Python"
#     version = 3
#
# These names can be found in the global namespace.

print("\nValues from globals():")
print(namespace["language"])
print(namespace["version"])


# Notice the relationship:
#
#     language = "Python"
#
# creates a namespace entry conceptually equivalent to:
#
#     "language" → "Python"


# =============================================================================
# 5. THE NAMESPACE CONTAINS MORE THAN OUR VARIABLES
# =============================================================================

# The module namespace also contains names created by Python itself,
# imported names, functions, classes, and other module-level objects.
#
# For example, this file has a special name:
#
#     __name__
#
# We can inspect it:

print("\nCurrent module name:")
print(namespace["__name__"])


# Other special names also exist in a module namespace.
#
# We will study these special module attributes in more detail later.


# =============================================================================
# 6. IMPORTED NAMES BECOME NAMESPACE ENTRIES
# =============================================================================

import math


# After:
#
#     import math
#
# the name `math` becomes available in this module's namespace.
#
# Therefore:

print("\nImported module from namespace:")
print(namespace["math"])


# The namespace now contains:
#
#     "math" → math module object


# This is an important connection between importing and namespaces:
#
#     import math
#          ↓
#     bind the name `math`
#          ↓
#     current module namespace


# =============================================================================
# 7. DIRECTLY IMPORTED OBJECTS ALSO BECOME NAMESPACE ENTRIES
# =============================================================================

from math import sqrt


# Now the name `sqrt` is also part of this module's namespace.

print("\nDirectly imported function:")
print(namespace["sqrt"])


# Compare:
#
#     import math
#
# creates:
#
#     "math" → math module
#
#
#     from math import sqrt
#
# creates:
#
#     "sqrt" → sqrt function
#
# This is one reason the distinction between the two import forms matters.


# =============================================================================
# 8. FUNCTIONS ARE ALSO NAMESPACE ENTRIES
# =============================================================================

def add(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


# Defining a function at module level creates a name in the module namespace.
#
# The name:
#
#     add
#
# now refers to the function object.

print("\nFunction from namespace:")
print(namespace["add"])


# We can call the function normally:

print("\nFunction result:")
print(add(10, 20))


# Conceptually:
#
#     "add" ─────────→ function object


# =============================================================================
# 9. CLASSES ARE ALSO NAMESPACE ENTRIES
# =============================================================================

class Calculator:
    """Perform a basic arithmetic operation."""

    def multiply(self, first: int, second: int) -> int:
        return first * second


# The class name also becomes an entry in the module namespace.

print("\nClass from namespace:")
print(namespace["Calculator"])


# Conceptually:
#
#     "Calculator" ──→ class object


# =============================================================================
# 10. CREATING AN OBJECT DOES NOT CREATE A NEW MODULE NAMESPACE
# =============================================================================

calculator = Calculator()


# The name `calculator` is another entry in this module's namespace.

print("\nInstance from namespace:")
print(namespace["calculator"])


# Notice:
#
#     Calculator
#         → class object
#
#     calculator
#         → instance of Calculator
#
# Both names exist in the same module namespace because they were
# created at module level.


# =============================================================================
# 11. NAMESPACE ENTRIES ARE NAME-TO-OBJECT REFERENCES
# =============================================================================

# Consider:

score = 100


# The namespace contains a relationship like:
#
#     "score" → integer object 100
#
# If we assign another value:

score = 200


# the name `score` is rebound to the new object.

print("\nRebound name:")
print(namespace["score"])


# The expected result is:
#
#     200
#
# The namespace entry for `score` now refers to the new object.


# =============================================================================
# 12. REASSIGNMENT CHANGES THE BINDING
# =============================================================================

status = "pending"

print("\nOriginal status:")
print(namespace["status"])


status = "completed"

print("Updated status:")
print(namespace["status"])


# The important idea is:
#
#     status = "pending"
#             ↓
#     "status" → "pending"
#
# Then:
#
#     status = "completed"
#             ↓
#     "status" → "completed"
#
# The name is rebound.


# =============================================================================
# 13. DIFFERENT NAMES CAN REFER TO THE SAME OBJECT
# =============================================================================

numbers: list[int] = [10, 20, 30]

other_numbers = numbers


# Both names refer to the same list object.

print("\nSame object:")
print(numbers is other_numbers)


# The namespace therefore contains:
#
#     "numbers"       ──┐
#                      ├──→ same list object
#     "other_numbers" ──┘
#
# A namespace stores names and their object references.
#
# It does not require every name to refer to a unique object.


# =============================================================================
# 14. THE MODULE NAMESPACE IS A DICTIONARY
# =============================================================================

# Because `globals()` returns a dictionary, we can inspect namespace
# entries using normal dictionary operations.

print("\nNamespace contains 'language':")
print("language" in namespace)

print("\nNamespace contains 'add':")
print("add" in namespace)

print("\nNamespace contains 'Calculator':")
print("Calculator" in namespace)


# This demonstrates that the global namespace behaves like a mapping
# from names to objects.


# =============================================================================
# 15. READING A NAME THROUGH `globals()`
# =============================================================================

# We can retrieve an object from the namespace using its string name.

retrieved_language = globals()["language"]

print("\nRetrieved through globals():")
print(retrieved_language)


# Compare:
#
#     language
#
# with:
#
#     globals()["language"]
#
# Both refer to the same object in this context.


# =============================================================================
# 16. WRITING TO THE GLOBAL NAMESPACE
# =============================================================================

# `globals()` returns the module's global namespace dictionary.
#
# A new entry can therefore be added to it.

globals()["country"] = "India"


# The newly created name is now accessible at module level.

print("\nDynamically added global name:")
print(country)


# The relationship is:
#
#     globals()["country"] = "India"
#             ↓
#     "country" → "India"
#
# This is possible, but directly assigning variables is generally
# clearer and preferred for ordinary code.


# =============================================================================
# 17. MODULE NAMESPACE IS DIFFERENT FROM LOCAL FUNCTION NAMESPACE
# =============================================================================

def demonstrate_local_namespace() -> None:
    """Demonstrate that functions have their own local namespace."""

    local_value = 50

    print("\nInside function:")
    print("Local value:", local_value)
    print("Function global language:", language)

    # `locals()` represents the current local namespace.

    local_namespace = locals()

    print("Local namespace contains 'local_value':")
    print("local_value" in local_namespace)


demonstrate_local_namespace()


# Inside the function:
#
#     local_value
#
# belongs to the function's local namespace.
#
# Meanwhile:
#
#     language
#
# belongs to this module's global namespace.
#
# This distinction becomes important when studying scope and name
# resolution.


# =============================================================================
# 18. MODULE NAMESPACE VS LOCAL NAMESPACE
# =============================================================================

# Consider:
#
#     language = "Python"
#
# at module level.
#
# This belongs to the module namespace.
#
# Then inside a function:
#
#     def example():
#         language = "SQL"
#
# that `language` belongs to the function's local namespace.
#
# The two names can have the same spelling while belonging to
# different namespaces.
#
# Scope determines which name Python uses in a particular context.


# =============================================================================
# 19. MODULE NAMESPACE ISOLATION
# =============================================================================

# Each module has its own namespace.
#
# Suppose two modules both define:
#
#     value = ...
#
# They do not automatically overwrite each other's variables.
#
# They can be accessed through their respective module names:
#
#     module_a.value
#     module_b.value
#
# This namespace isolation is one of the major reasons modules are
# useful for organizing larger programs.


# =============================================================================
# 20. WHY MODULE NAMESPACES MATTER
# =============================================================================

# Imagine a large application with hundreds of functions.
#
# Without namespace organization, names could easily collide:
#
#     process()
#     process()
#     process()
#
# Modules allow those names to be grouped:
#
#     ingestion.process()
#     transformation.process()
#     validation.process()
#
# Each module provides its own namespace.
#
# This is especially useful in larger applications and data pipelines.


# =============================================================================
# 21. SIMPLE DATA-ENGINEERING-STYLE EXAMPLE
# =============================================================================

# Imagine a project structured like:
#
#     pipeline/
#     │
#     ├── ingestion.py
#     ├── transformation.py
#     └── validation.py
#
# Each module could define:
#
#     ingestion.load_data()
#     transformation.clean_data()
#     validation.validate_data()
#
# Their module namespaces keep those names organized.
#
# This is one of the practical reasons understanding module namespaces
# is important before working with larger Python projects.


# =============================================================================
# 22. INSPECTING SELECTED NAMESPACE ENTRIES
# =============================================================================

# We can inspect the namespace without printing the entire dictionary.

selected_names = [
    "language",
    "version",
    "math",
    "sqrt",
    "add",
    "Calculator",
    "calculator",
    "score",
    "status",
    "country",
]

print("\nSelected namespace entries:")

for name in selected_names:
    print(f"{name!r} -> {globals()[name]!r}")


# This is simply using normal dictionary-style access on the global
# namespace returned by `globals()`.


# =============================================================================
# 23. IMPORTANT DISTINCTION: MODULE OBJECT VS MODULE NAMESPACE
# =============================================================================

# These two concepts are related but not identical.
#
# MODULE OBJECT:
#
#     The actual object representing the loaded module.
#
# MODULE NAMESPACE:
#
#     The collection of names associated with that module.
#
# When we write:
#
#     import math
#
# the name `math` refers to the module object.
#
# That module object has its own namespace containing names such as:
#
#     sqrt
#     pi
#     sin
#     cos
#     ...
#
# Therefore:
#
#     math
#         → module object
#
#     math.__dict__
#         → dictionary representing the module's namespace
#
# Module attributes will be explored separately.


# =============================================================================
# 24. ACCESSING THE MATH MODULE NAMESPACE
# =============================================================================

# Modules expose their namespace through `__dict__`.
#
# For example:

math_namespace = math.__dict__

print("\nMath module namespace type:")
print(type(math_namespace))


# The result is a dictionary.
#
# We can inspect selected entries:

print("\nSelected names from math namespace:")
print("pi:", math_namespace["pi"])
print("sqrt:", math_namespace["sqrt"])


# This demonstrates the relationship:
#
#     math module object
#            │
#            ▼
#       math.__dict__
#            │
#            ▼
#       module namespace
#
# The detailed topic of module attributes will be covered next.


# =============================================================================
# 25. KEY TAKEAWAYS
# =============================================================================

# 1. Every Python module has its own namespace.
#
# 2. A namespace maps names to objects.
#
# 3. A module-level variable becomes an entry in the module namespace.
#
# 4. A module-level function becomes an entry in the module namespace.
#
# 5. A module-level class becomes an entry in the module namespace.
#
# 6. Imported names also become entries in the current module namespace.
#
# 7. `globals()` provides access to the current module's global namespace.
#
# 8. The global namespace returned by `globals()` is dictionary-like and
#    represented by a `dict`.
#
# 9. Reassignment changes what an existing name refers to.
#
# 10. Multiple names can refer to the same object.
#
# 11. Each module has its own namespace, providing namespace isolation.
#
# 12. A module object and its namespace are related but are not the
#     same concept.
#
# 13. A module's namespace can be represented through:
#
#         module.__dict__
#
# 14. Understanding namespaces makes imports, scope, and name resolution
#     much easier to understand.
#
# 15. The next topic is:
#
#         07_module_attributes.py
#
#     where we will examine the special attributes exposed by modules.