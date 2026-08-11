"""
03_import_as.py

Topic:
    Import aliases using `as`

Purpose:
    Understand how Python assigns an alternative local name to an
    imported module and why import aliases are useful.

Concepts covered:
    1. Basic import aliases
    2. Accessing an aliased module
    3. Module name vs local alias
    4. Multiple modules with aliases
    5. Avoiding long module names
    6. Preventing local naming conflicts
    7. Alias scope
    8. Standard-library alias conventions
    9. Difference between module aliasing and object aliasing

Important:
    - Basic `import` is covered in 02_import_statement.py.
    - `from ... import ...` is covered in 04_from_import.py.
    - Import conventions are discussed separately in
      04_import_patterns/04_import_conventions.py.
"""


# =============================================================================
# 1. BASIC IMPORT ALIAS SYNTAX
# =============================================================================

# The syntax is:
#
#     import module_name as alias
#
# Example:
#
#     import math as mathematics
#
# After this statement, the local name `mathematics` refers to the
# imported math module.
#
# We use the alias instead of the original module name when accessing
# objects from the module.

import math as mathematics


# Accessing the module through the alias:

square_root = mathematics.sqrt(81)

print("Square root:")
print(square_root)


# The important idea is:
#
#     import math as mathematics
#              │
#              └── original module name
#
#                         ↓
#
#              mathematics
#              └── local alias
#
# We use:
#
#     mathematics.sqrt()
#
# rather than:
#
#     math.sqrt()


# =============================================================================
# 2. THE ALIAS IS THE NAME AVAILABLE IN THE CURRENT NAMESPACE
# =============================================================================

# After:
#
#     import math as mathematics
#
# the name `mathematics` is available in the current namespace.
#
# The original name `math` is not created by this particular import statement.

print("\nAlias:")
print(mathematics)


# This works:
#
#     mathematics.sqrt(16)
#
# This would not be valid merely because of the aliased import:
#
#     math.sqrt(16)
#
# because this import created the local name `mathematics`, not `math`.


# =============================================================================
# 3. THE ALIAS STILL REFERS TO THE SAME MODULE
# =============================================================================

# An alias does not create another module.
#
# It creates another name referring to the imported module object.

import math as mathematics

print("\nModule identity:")
print(mathematics is __import__("math"))


# The expected result is:
#
#     True
#
# The alias is simply another reference to the same module object.


# =============================================================================
# 4. ALIASING DOES NOT CHANGE THE MODULE
# =============================================================================

# The following:
#
#     import math as mathematics
#
# does not rename the actual Python module.
#
# The module is still the `math` module.
#
# Only the name used to access it in the current namespace has changed.
#
# Conceptually:
#
#     Python's math module
#             ↑
#             │
#       mathematics
#       (local alias)


# =============================================================================
# 5. ALIASES CAN MAKE LONG MODULE NAMES EASIER TO USE
# =============================================================================

# Suppose a module has a long name:
#
#     data_processing_utilities
#
# Repeatedly writing:
#
#     data_processing_utilities.clean_data()
#     data_processing_utilities.validate_data()
#     data_processing_utilities.transform_data()
#
# can become cumbersome.
#
# An alias can provide a shorter local name:
#
#     import data_processing_utilities as dpu
#
# Then:
#
#     dpu.clean_data()
#     dpu.validate_data()
#     dpu.transform_data()
#
# This example is intentionally shown as a concept rather than importing
# a real custom module that does not exist in this repository.


# =============================================================================
# 6. MULTIPLE MODULES CAN HAVE ALIASES
# =============================================================================

import datetime as dt
import pathlib as path


current_date = dt.date.today()
current_directory = path.Path.cwd()


print("\nMultiple aliases:")
print("Current date:", current_date)
print("Current directory:", current_directory)


# Each import creates its own local alias:
#
#     dt   → datetime module
#     path → pathlib module
#
# Therefore:
#
#     dt.date
#     path.Path
#
# are qualified names using the aliases.


# =============================================================================
# 7. ALIASES ARE LOCAL NAMES
# =============================================================================

# The alias exists in the namespace where the import statement is executed.
#
# For example:

import math as mathematics


def calculate_circle_area(radius: float) -> float:
    """Return the area of a circle using the imported module alias."""
    return mathematics.pi * radius**2


print("\nUsing an alias inside a function:")
print(calculate_circle_area(5.0))


# The function can use `mathematics` because the alias exists in the
# module-level namespace where the function looks for global names.


# =============================================================================
# 8. ALIASING CAN AVOID NAME CONFLICTS
# =============================================================================

# Consider a situation where the current module already has a variable
# named `date`.
#
# An alias can provide a different local name for the imported module.

date = "2026-08-11"

import datetime as datetime_module


print("\nAvoiding a naming conflict:")
print("Local variable:", date)
print("Module alias:", datetime_module)


# We can now distinguish:
#
#     date
#             → local variable
#
#     datetime_module.date
#             → date class inside the datetime module
#
# The alias gives the imported module a distinct local name.


# =============================================================================
# 9. MODULE ALIAS VS OBJECT ALIAS
# =============================================================================

# There is an important distinction between:
#
#     import module as alias
#
# and:
#
#     from module import object as alias
#
# The first aliases the module:
#
#     import math as mathematics
#
#     mathematics.sqrt()
#
# The second aliases an object from a module:
#
#     from math import sqrt as square_root
#
#     square_root()
#
# The second form belongs to `from ... import ...` and will be covered
# in the next file.


# =============================================================================
# 10. AN ALIAS CAN BE USED THROUGHOUT THE MODULE
# =============================================================================

import statistics as stats


values: list[float] = [10.0, 20.0, 30.0, 40.0, 50.0]

mean_value = stats.mean(values)
median_value = stats.median(values)

print("\nUsing a module alias:")
print("Mean:", mean_value)
print("Median:", median_value)


# Once the alias is defined, it can be used wherever the name is visible
# according to Python's normal name-resolution rules.


# =============================================================================
# 11. ALIAS DOES NOT COPY THE MODULE
# =============================================================================

# Consider:
#
#     import math as mathematics
#
# The alias does not:
#
#     - duplicate the module
#     - copy its functions
#     - create a second independent module
#     - modify the original module
#
# It simply creates another name referring to the same module object.


# =============================================================================
# 12. COMMON MENTAL MODEL
# =============================================================================

# Think of:
#
#     import math as mathematics
#
# as:
#
#     module object
#          ↑
#          │
#     mathematics
#
# The name `mathematics` is a local reference to the module object.
#
# Therefore:
#
#     mathematics.sqrt()
#
# means:
#
#     find the module object referenced by `mathematics`
#             ↓
#     find `sqrt` inside that module
#             ↓
#     call the function


# =============================================================================
# 13. PRACTICAL EXAMPLE
# =============================================================================

# Module aliases are particularly useful when a module is used frequently.

import json as json_module


data: dict[str, str] = {
    "name": "Python",
    "type": "programming language",
}

json_text = json_module.dumps(data)

print("\nJSON example:")
print(json_text)


# Notice that we repeatedly use:
#
#     json_module.dumps()
#
# rather than:
#
#     json.dumps()
#
# because `json_module` is the local alias chosen by this file.


# =============================================================================
# 14. IMPORTANT RULE
# =============================================================================

# The syntax:
#
#     import module as alias
#
# means:
#
#     "Import this module and bind the given alias to it in the
#      current namespace."
#
# It does NOT mean:
#
#     "Create a new module with this name."


# =============================================================================
# 15. KEY TAKEAWAYS
# =============================================================================

# 1. Python supports module aliases using:
#
#       import module_name as alias
#
# 2. The alias becomes the local name used to access the module.
#
# 3. Example:
#
#       import math as mathematics
#
#       mathematics.sqrt(25)
#
# 4. The alias does not create a copy of the module.
#
# 5. The alias refers to the same underlying module object.
#
# 6. Aliases can:
#
#       - shorten long module names
#       - improve readability
#       - avoid naming conflicts
#       - make frequently used modules easier to reference
#
# 7. Module aliasing is different from aliasing an individual object
#    imported with `from ... import ...`.
#
# 8. The next topic covers:
#
#       from module import object
#
#    which allows individual objects to be imported directly.