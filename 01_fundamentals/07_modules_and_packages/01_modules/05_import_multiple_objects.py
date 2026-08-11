# type: ignore
"""
05_import_multiple_objects.py

Topic:
    Importing multiple objects with `from ... import ...`

Purpose:
    Understand how multiple objects can be imported from the same module
    and how Python binds each imported object into the current namespace.

Concepts covered:
    1. Importing multiple objects from one module
    2. Comma-separated imports
    3. Functions, constants, and classes in one import statement
    4. Using imported objects directly
    5. Combining multiple imports from the same module
    6. Aliasing individual imported objects
    7. Parenthesized imports
    8. Difference between multiple-object import and module import
    9. Namespace implications
    10. Readability considerations

Important:
    - Basic `import` is covered in 02_import_statement.py.
    - Module aliases are covered in 03_import_as.py.
    - Basic `from ... import ...` is covered in 04_from_import.py.
    - Import conventions are covered later.
"""


# =============================================================================
# 1. BASIC MULTIPLE-OBJECT IMPORT
# =============================================================================

# Python allows multiple objects to be imported from the same module
# in a single statement.
#
# Syntax:
#
#     from module_name import object_one, object_two, object_three
#
# For example:

from math import pi, sqrt, factorial


# All three names are now directly available in the current namespace:
#
#     pi
#     sqrt
#     factorial


# =============================================================================
# 2. USING THE IMPORTED OBJECTS
# =============================================================================

circle_area = pi * 5**2
square_root = sqrt(144)
factorial_result = factorial(5)

print("Circle area:")
print(circle_area)

print("\nSquare root:")
print(square_root)

print("\nFactorial:")
print(factorial_result)


# Notice that we do not need:
#
#     math.pi
#     math.sqrt()
#     math.factorial()
#
# because the selected objects were imported directly.


# =============================================================================
# 3. IMPORTING DIFFERENT TYPES OF OBJECTS
# =============================================================================

# A single `from ... import ...` statement can import different kinds
# of objects from a module.
#
# The objects could be:
#
#     - constants
#     - functions
#     - classes
#     - submodules
#     - other module-level objects
#
# Example with pathlib:

from pathlib import Path, PurePath


current_directory = Path.cwd()
path_object = PurePath("data", "input.csv")

print("\nCurrent directory:")
print(current_directory)

print("\nPure path:")
print(path_object)


# Here:
#
#     Path
#         → class
#
#     PurePath
#         → class
#
# Both were imported in the same statement.


# =============================================================================
# 4. IMPORTING MULTIPLE FUNCTIONS
# =============================================================================

# Multiple functions can be imported together.

from statistics import mean, median, mode


numbers: list[int] = [10, 20, 20, 30, 40]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print("\nStatistics:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)


# The names:
#
#     mean
#     median
#     mode
#
# are now directly available in this module.


# =============================================================================
# 5. IMPORTING MULTIPLE OBJECTS DOES NOT IMPORT EVERYTHING
# =============================================================================

# Consider:
#
#     from math import pi, sqrt, factorial
#
# Only these three selected names are imported directly:
#
#     pi
#     sqrt
#     factorial
#
# Other names from `math` are not automatically placed into the
# current namespace.
#
# For example:
#
#     sin
#     cos
#     ceil
#     floor
#
# are not directly available simply because we imported the three
# objects above.


# =============================================================================
# 6. MULTIPLE IMPORTS CAN BE WRITTEN AS SEPARATE STATEMENTS
# =============================================================================

# These are both valid approaches:
#
# Option A:
#
#     from math import pi, sqrt, factorial
#
#
# Option B:
#
#     from math import pi
#     from math import sqrt
#     from math import factorial
#
#
# When objects come from the same module, combining them into one import
# statement is usually more concise.


# =============================================================================
# 7. ALIASING INDIVIDUAL OBJECTS
# =============================================================================

# Individual imported objects can have aliases.
#
# Syntax:
#
#     from module import object as alias
#
# Multiple objects can also be aliased in the same statement.

from math import sqrt as square_root_function, factorial as calculate_factorial


print("\nAliased imported objects:")
print("Square root:", square_root_function(225))
print("Factorial:", calculate_factorial(6))


# The original names:
#
#     sqrt
#     factorial
#
# are not the names introduced by this particular import statement.
#
# The local names introduced here are:
#
#     square_root_function
#     calculate_factorial


# =============================================================================
# 8. MIXING ALIASED AND NON-ALIASED IMPORTS
# =============================================================================

# Some imported objects can use their original names while others
# receive aliases.

from math import pi as circle_constant, cos, sin


angle = 0.0

print("\nMixed aliases:")
print("Pi:", circle_constant)
print("Cosine:", cos(angle))
print("Sine:", sin(angle))


# Here:
#
#     circle_constant
#         → alias for pi
#
#     cos
#         → original name
#
#     sin
#         → original name


# =============================================================================
# 9. PARENTHESIZED MULTIPLE IMPORTS
# =============================================================================

# When a long import statement contains many objects, Python allows
# the imported names to be split across multiple lines using parentheses.
#
# Example:

from math import (
    ceil,
    floor,
    gcd,
    lcm,
)


print("\nParenthesized imports:")
print("Ceiling:", ceil(4.2))
print("Floor:", floor(4.8))
print("GCD:", gcd(24, 36))
print("LCM:", lcm(12, 18))


# Parentheses allow the import to remain readable without using
# explicit line-continuation characters.


# =============================================================================
# 10. WHY PARENTHESIZED IMPORTS ARE USEFUL
# =============================================================================

# Compare a potentially long one-line import:
#
#     from some_module import object_one, object_two, object_three, ...
#
# with:
#
#     from some_module import (
#         object_one,
#         object_two,
#         object_three,
#     )
#
# The second form is easier to scan when many objects must be imported.


# =============================================================================
# 11. MULTIPLE OBJECTS VS MODULE IMPORT
# =============================================================================

# Compare:
#
#     import math
#
# with:
#
#     from math import pi, sqrt, factorial
#
#
# With module import:
#
#     math.pi
#     math.sqrt()
#     math.factorial()
#
#
# With multiple-object import:
#
#     pi
#     sqrt()
#     factorial()
#
#
# The first approach keeps the module name visible.
#
# The second approach places the selected objects directly into the
# current namespace.


# =============================================================================
# 12. SAME OBJECT, DIFFERENT ACCESS STYLE
# =============================================================================

# We can demonstrate that the same mathematical operation can be
# accessed through different names.

import math

module_result = math.sqrt(256)
direct_result = sqrt(256)


print("\nDifferent access styles:")
print("Through module:", module_result)
print("Through imported function:", direct_result)


# Both results are the same.
#
# The difference is how the function is referenced:
#
#     math.sqrt()
#
# versus:
#
#     sqrt()


# =============================================================================
# 13. MULTIPLE IMPORTS DO NOT CREATE MULTIPLE COPIES
# =============================================================================

# Importing several objects from the same module does not mean Python
# creates a separate module for each object.
#
# For example:
#
#     from math import pi, sqrt, factorial
#
# conceptually means:
#
#     math module
#       │
#       ├── pi
#       ├── sqrt
#       └── factorial
#              │
#              ▼
#       selected objects become directly accessible
#
# The objects remain associated with the original module.


# =============================================================================
# 14. NAME COLLISIONS
# =============================================================================

# Direct imports can introduce names into the current namespace.
#
# Therefore, importing an object whose name already exists locally can
# replace the previous binding.
#
# Example:

sqrt_value = 100

from math import sqrt


# The name `sqrt` is now available as the imported function.
#
# The unrelated variable `sqrt_value` remains untouched.

print("\nName collision example:")
print("Existing variable:", sqrt_value)
print("Imported function:", sqrt(49))


# If we had already created a variable literally named `sqrt`, importing
# the function with the same name would rebind that name.
#
# For example:
#
#     sqrt = "some value"
#     from math import sqrt
#
# After the import, `sqrt` would refer to the imported function.
#
# This is one reason namespace management matters.


# =============================================================================
# 15. USING ALIASES TO AVOID NAME COLLISIONS
# =============================================================================

# Instead of introducing an imported object using a potentially
# conflicting name, we can provide an alias.

sqrt = "local value"

from math import sqrt as calculate_square_root


print("\nAvoiding a name collision:")
print("Local sqrt value:", sqrt)
print("Imported function:", calculate_square_root(64))


# Now:
#
#     sqrt
#         → existing local value
#
#     calculate_square_root
#         → imported math.sqrt function


# =============================================================================
# 16. IMPORTING MANY OBJECTS CAN REDUCE NAMESPACE CLARITY
# =============================================================================

# Direct imports are convenient, but there is a trade-off.
#
# Consider:
#
#     from module_a import process
#     from module_b import process
#
# The second import can replace the local name `process` introduced
# by the first import.
#
# This can make code harder to understand.
#
# Using module-qualified access can make the source of an object clearer:
#
#     module_a.process()
#     module_b.process()
#
# This is a namespace/readability consideration rather than a syntax rule.


# =============================================================================
# 17. IMPORTING THE SAME MODULE OBJECT IN DIFFERENT WAYS
# =============================================================================

# We can use both:
#
#     import module
#
# and:
#
#     from module import object
#
# in the same program when appropriate.

import random
from random import randint


random_number_one = random.randint(1, 10)
random_number_two = randint(1, 10)

print("\nDifferent access styles:")
print("Using module:", random_number_one)
print("Using direct import:", random_number_two)


# Both names ultimately provide access to functionality from the same
# `random` module.


# =============================================================================
# 18. COMMON MENTAL MODEL
# =============================================================================

# Think of:
#
#     from module import a, b, c
#
# as:
#
#     module
#       │
#       ├── a ───────→ current namespace: a
#       ├── b ───────→ current namespace: b
#       └── c ───────→ current namespace: c
#
#
# Compare:
#
#     import module
#
# which gives:
#
#     current namespace: module
#                         │
#                         ├── a
#                         ├── b
#                         └── c
#
#
# This distinction becomes especially important when working with
# larger Python projects.


# =============================================================================
# 19. KEY TAKEAWAYS
# =============================================================================

# 1. Multiple objects can be imported from one module:
#
#       from math import pi, sqrt, factorial
#
# 2. Each selected object becomes directly accessible by its imported name.
#
# 3. Different object types can be imported together:
#
#       functions
#       classes
#       variables
#       submodules
#
# 4. Individual objects can be aliased:
#
#       from math import sqrt as square_root
#
# 5. Multiple aliased imports can appear in one statement.
#
# 6. Parentheses can be used to format long import statements:
#
#       from math import (
#           object_one,
#           object_two,
#       )
#
# 7. Direct imports introduce names into the current namespace.
#
# 8. Name collisions are therefore possible.
#
# 9. Aliases can help avoid naming conflicts.
#
# 10. Module-qualified access:
#
#       module.object
#
#     keeps the module source visible.
#
# 11. Direct object access:
#
#       object
#
#     is shorter but can make the object's origin less obvious.
#
# 12. The next topic is:
#
#       06_module_namespace.py
#
#     where we will examine what a module's namespace actually contains.