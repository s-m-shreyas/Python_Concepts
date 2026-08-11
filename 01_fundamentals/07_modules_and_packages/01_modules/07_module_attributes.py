# type: ignore
"""
07_module_attributes.py

Topic:
    Module attributes

Purpose:
    Understand the special attributes available on Python modules and
    how those attributes describe or expose information about the module.

Concepts covered:
    1. What module attributes are
    2. `__name__`
    3. `__file__`
    4. `__doc__`
    5. `__package__`
    6. `__spec__`
    7. `__loader__`
    8. `__cached__`
    9. `__dict__`
    10. Module attributes vs module variables
    11. Accessing attributes with dot notation
    12. Accessing attributes through `getattr()`
    13. Inspecting selected module attributes
    14. Why module attributes matter

Important:
    - Module namespaces are covered in:
          06_module_namespace.py
    - `__name__ == "__main__"` and the main guard are covered in:
          05_special_module_attributes/02_main_guard.py
    - Module execution is covered separately in:
          08_module_execution.py

Note:
    Some module attributes depend on how Python loads and executes a
    module. Therefore, their exact values can differ depending on whether
    this file is run directly or imported by another module.
"""


# =============================================================================
# 1. WHAT ARE MODULE ATTRIBUTES?
# =============================================================================

# A module is an object.
#
# Like other Python objects, a module can have attributes.
#
# For example:
#
#     module.__name__
#     module.__file__
#     module.__doc__
#
# Python automatically provides several special attributes when a module
# is created and loaded.
#
# These attributes usually begin and end with double underscores:
#
#     __name__
#     __file__
#     __doc__
#     __package__
#     __spec__
#     __loader__
#     __cached__
#     __dict__
#
# These are commonly called "dunder" attributes.


# =============================================================================
# 2. THE `__name__` ATTRIBUTE
# =============================================================================

# Every module has a `__name__` attribute.
#
# It identifies the module by name.
#
# When this file is executed directly, its value is normally:
#
#     "__main__"
#
# When the file is imported as a module, its value normally becomes the
# module's import name.


print("Module name:")
print(__name__)


# The exact value therefore depends on how the module is being used.
#
# Direct execution:
#
#     python 07_module_attributes.py
#
# usually results in:
#
#     __main__
#
# Imported execution:
#
#     import module_name
#
# gives the module its importable name.


# =============================================================================
# 3. THE `__file__` ATTRIBUTE
# =============================================================================

# `__file__` normally contains the path associated with the module file.
#
# Example conceptually:
#
#     C:\project\07_module_attributes.py
#
# We can inspect it:

print("\nModule file:")
print(__file__)


# This is useful when you need to know which file a module came from.
#
# Important:
#
# `__file__` is not guaranteed to exist in every Python execution
# environment.
#
# For example, some interactive environments may not provide it.
#
# In a normal Python file executed from disk, it is generally available.


# =============================================================================
# 4. THE `__doc__` ATTRIBUTE
# =============================================================================

# The module-level docstring at the top of this file becomes the module's
# `__doc__` attribute.
#
# We can inspect it:

print("\nModule documentation:")
print(__doc__)


# Therefore:
#
#     module.__doc__
#
# provides the module's documentation string.
#
# This is one reason module docstrings are useful.


# =============================================================================
# 5. THE `__package__` ATTRIBUTE
# =============================================================================

# `__package__` identifies the package context in which the module
# is being executed.
#
# We can inspect it:

print("\nModule package:")
print(__package__)


# When a module is part of a package, this attribute can contain the
# package name.
#
# When the file is executed directly as a standalone script, its value
# can be empty or otherwise differ from the value seen when imported.
#
# This attribute becomes particularly important for relative imports.


# =============================================================================
# 6. THE `__spec__` ATTRIBUTE
# =============================================================================

# `__spec__` contains the module's import specification when Python
# loads the module through the import system.
#
# We can inspect it:

print("\nModule specification:")
print(__spec__)


# A module specification contains metadata used by Python's import system.
#
# The exact representation depends on how the module was loaded.
#
# When a file is executed directly, `__spec__` can be `None`.


# =============================================================================
# 7. THE `__loader__` ATTRIBUTE
# =============================================================================

# `__loader__` refers to the loader responsible for loading the module.

print("\nModule loader:")
print(__loader__)


# The loader is part of Python's import machinery.
#
# It is responsible for helping Python locate and load module code.
#
# You normally do not need to interact with the loader directly in
# everyday Python programming.
#
# However, understanding that it exists helps when learning how Python's
# import system works internally.


# =============================================================================
# 8. THE `__cached__` ATTRIBUTE
# =============================================================================

# `__cached__` can contain the location of the cached bytecode file
# associated with a module.
#
# We can inspect it:

print("\nModule cached bytecode path:")
print(__cached__)


# Depending on how the module is executed and Python's environment,
# this may contain a path or may be `None`.
#
# Python's import system can use cached bytecode to avoid recompiling
# source code unnecessarily.


# =============================================================================
# 9. THE `__dict__` ATTRIBUTE
# =============================================================================

# A module's `__dict__` contains its namespace.
#
# This connects directly with the previous topic:
#
#     06_module_namespace.py
#
# We can inspect the type:

print("\nModule dictionary type:")
print(type(__dict__))


# The result is normally:
#
#     <class 'dict'>
#
# The module namespace contains names such as:
#
#     __name__
#     __file__
#     __doc__
#     __package__
#     __spec__
#     __loader__
#     __cached__
#
# along with names defined or imported by the module.


# =============================================================================
# 10. `__dict__` AND `globals()`
# =============================================================================

# At module level, these provide access to the same global namespace.

module_namespace = globals()

print("\nSame namespace object:")
print(module_namespace is __dict__)


# The expected result is:
#
#     True
#
# This demonstrates the relationship:
#
#     globals()
#         ↓
#     current module's global namespace
#
# and:
#
#     __dict__
#         ↓
#     current module's namespace dictionary


# =============================================================================
# 11. ACCESSING ATTRIBUTES WITH DOT NOTATION
# =============================================================================

# When we have a module object, its attributes can be accessed with
# dot notation.
#
# For example:
#
#     math.__name__
#     math.__doc__
#     math.__dict__
#
# Let's import a module:

import math


print("\nMath module name:")
print(math.__name__)

print("\nMath module documentation exists:")
print(math.__doc__ is not None)


# The module object:
#
#     math
#
# provides access to its attributes.


# =============================================================================
# 12. ACCESSING ATTRIBUTES THROUGH `getattr()`
# =============================================================================

# Python also provides `getattr()` for dynamic attribute access.
#
# Syntax:
#
#     getattr(object, attribute_name)
#
# Example:

math_name = getattr(math, "__name__")

print("\nMath module name using getattr():")
print(math_name)


# This is equivalent to:
#
#     math.__name__
#
# but `getattr()` is useful when the attribute name is stored dynamically
# as a string.


# =============================================================================
# 13. ATTRIBUTE NAME STORED IN A VARIABLE
# =============================================================================

attribute_name = "__name__"

dynamic_name = getattr(math, attribute_name)

print("\nDynamically accessed attribute:")
print(dynamic_name)


# Here:
#
#     attribute_name
#         ↓
#     "__name__"
#
# then:
#
#     getattr(math, attribute_name)
#
# accesses:
#
#     math.__name__


# =============================================================================
# 14. SAFE ATTRIBUTE ACCESS WITH `getattr()`
# =============================================================================

# `getattr()` can receive a default value.
#
# Syntax:
#
#     getattr(object, attribute_name, default)
#
# If the requested attribute does not exist, the default value is returned.

missing_attribute = getattr(
    math,
    "__does_not_exist__",
    "Attribute not available",
)

print("\nMissing attribute:")
print(missing_attribute)


# Without the default:
#
#     getattr(math, "__does_not_exist__")
#
# would raise:
#
#     AttributeError
#
# The default allows us to handle the missing attribute without an error.


# =============================================================================
# 15. MODULE ATTRIBUTES ARE ENTRIES IN THE MODULE NAMESPACE
# =============================================================================

# Module attributes such as `__name__` are also represented in the
# module's namespace dictionary.
#
# For example:

print("\n__name__ from namespace:")
print(__dict__["__name__"])


# This connects the two concepts:
#
#     module attribute
#             ↕
#     module namespace entry
#
# For a module, attributes and namespace entries are closely related.


# =============================================================================
# 16. `__name__` IS A MODULE ATTRIBUTE AND A NAMESPACE ENTRY
# =============================================================================

# We can compare:
#
#     __name__
#
# with:
#
#     globals()["__name__"]

print("\n__name__ comparison:")
print(__name__ == globals()["__name__"])


# The expected result is:
#
#     True


# =============================================================================
# 17. `__file__` IS ALSO AVAILABLE THROUGH THE NAMESPACE
# =============================================================================

print("\n__file__ comparison:")
print(__file__ == globals()["__file__"])


# Again, the module attribute corresponds to an entry in the module's
# namespace.


# =============================================================================
# 18. CUSTOM MODULE ATTRIBUTES
# =============================================================================

# Module attributes are not limited to Python's automatically created
# special attributes.
#
# We can create our own module-level variables.

project_name = "Python Concepts"
project_version = "1.0"


# These become module attributes as well.

print("\nCustom module attributes:")
print(project_name)
print(project_version)


# If this file were imported as a module:
#
#     import module_name
#
# those values could be accessed through:
#
#     module_name.project_name
#     module_name.project_version
#
# This is the same attribute-access mechanism used for built-in module
# attributes.


# =============================================================================
# 19. CUSTOM ATTRIBUTES APPEAR IN `__dict__`
# =============================================================================

print("\nCustom attributes in module namespace:")
print(__dict__["project_name"])
print(__dict__["project_version"])


# This demonstrates that module-level variables become entries in the
# module namespace and can therefore be accessed as module attributes.


# =============================================================================
# 20. MODULE ATTRIBUTES CAN BE READ USING DOT NOTATION
# =============================================================================

# The current module object can be accessed through `sys.modules`.
#
# `sys.modules` is a dictionary containing modules currently loaded by
# Python.

import sys


current_module = sys.modules[__name__]


print("\nCurrent module object:")
print(current_module)


# Now we can access this module's attributes through the module object:

print("\nCurrent module name through module object:")
print(current_module.__name__)

print("\nCurrent module file through module object:")
print(current_module.__file__)


# This demonstrates the complete relationship:
#
#     sys.modules
#         ↓
#     current module object
#         ↓
#     module attributes
#
# For example:
#
#     current_module.__name__
#     current_module.__file__
#     current_module.__dict__


# =============================================================================
# 21. MODULE OBJECT AND MODULE ATTRIBUTES
# =============================================================================

# Think of a module as an object containing information and functionality.
#
# Conceptually:
#
#     module object
#          │
#          ├── __name__
#          ├── __file__
#          ├── __doc__
#          ├── __package__
#          ├── __spec__
#          ├── __loader__
#          ├── __cached__
#          ├── __dict__
#          ├── custom_variable
#          ├── function
#          └── class
#
# This is why we can write:
#
#     module.function()
#
# and:
#
#     module.__name__
#
# Both are attribute access operations.


# =============================================================================
# 22. IMPORTANT: NOT EVERY ATTRIBUTE HAS THE SAME VALUE EVERYWHERE
# =============================================================================

# Some module attributes depend on the execution context.
#
# For example:
#
#     __name__
#     __file__
#     __package__
#     __spec__
#     __cached__
#
# can differ depending on whether the module is:
#
#     - executed directly
#     - imported normally
#     - loaded through another mechanism
#     - executed in an interactive environment
#
# Therefore, when studying module attributes, focus on their purpose
# rather than memorizing one fixed value.


# =============================================================================
# 23. QUICK ATTRIBUTE INSPECTION
# =============================================================================

# We can collect commonly encountered module attributes and inspect
# them systematically.

attribute_names = [
    "__name__",
    "__file__",
    "__doc__",
    "__package__",
    "__spec__",
    "__loader__",
    "__cached__",
]


print("\nSelected module attributes:")

for attribute in attribute_names:
    value = getattr(sys.modules[__name__], attribute, None)
    print(f"{attribute}: {value!r}")


# This is a useful inspection pattern when exploring an unfamiliar module.


# =============================================================================
# 24. WHY `__dict__` IS DIFFERENT FROM OTHER ATTRIBUTES
# =============================================================================

# Most attributes give us a specific piece of information:
#
#     __name__
#         → module name
#
#     __file__
#         → associated file path
#
#     __doc__
#         → documentation string
#
#     __package__
#         → package context
#
#     __spec__
#         → import specification
#
#     __loader__
#         → module loader
#
#     __cached__
#         → cached bytecode path
#
#
# But:
#
#     __dict__
#
# exposes the module's namespace mapping itself.


# =============================================================================
# 25. MODULE ATTRIBUTES AND IMPORTS
# =============================================================================

# When we write:
#
#     import math
#
# Python creates or obtains a module object representing `math`.
#
# That module object has attributes:
#
#     math.__name__
#     math.__doc__
#     math.__dict__
#
# and many others.
#
# The import system therefore does more than simply "bring code into
# the program."
#
# It provides access to a module object with its own namespace and
# attributes.


# =============================================================================
# 26. PRACTICAL DATA-ENGINEERING CONNECTION
# =============================================================================

# In a larger project, you may encounter code such as:
#
#     import ingestion
#     import transformation
#     import validation
#
# You can then inspect module information:
#
#     ingestion.__file__
#     transformation.__name__
#     validation.__dict__
#
# This can be useful when debugging:
#
#     - Which module was actually loaded?
#     - From which file?
#     - What names does it contain?
#     - What package does it belong to?
#
# Understanding module attributes makes these questions much easier
# to investigate.


# =============================================================================
# 27. COMMON CONFUSION: `__name__` VS A CUSTOM VARIABLE
# =============================================================================

# `__name__` is automatically provided by Python.
#
# A variable such as:
#
#     project_name = "Python Concepts"
#
# is defined by us.
#
# Both are module attributes.
#
# The difference is that:
#
#     __name__
#
# has a special meaning to Python, while:
#
#     project_name
#
# is an application-defined attribute.


# =============================================================================
# 28. COMMON CONFUSION: `__dict__` VS `globals()`
# =============================================================================

# At module level:
#
#     globals()
#
# gives access to the current module's global namespace.
#
# The module's:
#
#     __dict__
#
# represents that namespace as well.
#
# Therefore, at module level:
#
#     globals() is __dict__
#
# evaluates to True.
#
# They are different ways of accessing the same module-level namespace
# in this context.


# =============================================================================
# 29. KEY TAKEAWAYS
# =============================================================================

# 1. A module is an object.
#
# 2. Modules have attributes.
#
# 3. Python automatically provides several special module attributes.
#
# 4. `__name__`
#       Identifies the module in its current execution context.
#
# 5. `__file__`
#       Usually identifies the file associated with the module.
#
# 6. `__doc__`
#       Contains the module's documentation string.
#
# 7. `__package__`
#       Describes the module's package context.
#
# 8. `__spec__`
#       Contains the module's import specification.
#
# 9. `__loader__`
#       Refers to the loader used by the import system.
#
# 10. `__cached__`
#       Can contain the location of cached bytecode.
#
# 11. `__dict__`
#       Represents the module's namespace dictionary.
#
# 12. Module attributes can be accessed using:
#
#         module.attribute
#
# 13. Dynamic attribute access can be performed using:
#
#         getattr(module, "attribute")
#
# 14. Module-level variables, functions, and classes also become
#     attributes of the module.
#
# 15. Module attributes can vary depending on how the module is loaded.
#
# 16. Understanding module attributes provides the foundation for
#     understanding module execution and Python's import machinery.
#
# 17. The next topic is:
#
#         08_module_execution.py
#
#     where we will study what actually happens when Python executes
#     a module.