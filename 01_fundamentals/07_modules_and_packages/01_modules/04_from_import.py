"""
04_from_import.py

Topic:
    The `from ... import ...` statement

Purpose:
    Understand how Python imports specific objects from a module
    directly into the current namespace.

Concepts covered:
    1. Basic `from ... import ...` syntax
    2. Importing a function
    3. Importing a variable
    4. Importing a class
    5. Calling imported functions directly
    6. Importing multiple objects
    7. Difference between `import module` and `from module import object`
    8. Aliasing an imported object
    9. Name binding created by `from ... import ...`
    10. Namespace implications

Important:
    - Basic module importing is covered in 02_import_statement.py.
    - Module aliases are covered in 03_import_as.py.
    - Importing multiple objects is covered separately in
      05_import_multiple_objects.py.
    - Relative and absolute import patterns are covered later.
"""


# =============================================================================
# 1. BASIC `from ... import ...` SYNTAX
# =============================================================================

# The basic syntax is:
#
#     from module_name import object_name
#
# This means:
#
#     1. Import the specified module.
#     2. Find the specified object inside that module.
#     3. Bind that object to the given name in the current namespace.
#
# Example:
#
#     from math import sqrt
#
# After this statement, `sqrt` can be used directly:
#
#     sqrt(25)
#
# We do not need:
#
#     math.sqrt(25)


from math import sqrt


# The imported function can now be called directly.

square_root = sqrt(81)

print("Square root:")
print(square_root)


# Compare the two forms:
#
#     import math
#     math.sqrt(81)
#
# versus:
#
#     from math import sqrt
#     sqrt(81)
#
# Both provide access to the same function, but the name available
# in the current namespace is different.


# =============================================================================
# 2. IMPORTING A VARIABLE
# =============================================================================

# A module can contain variables as well as functions.
#
# The `math` module provides the constant `pi`.
#
# We can import it directly.

from math import pi


circle_area = pi * 5**2

print("\nCircle area:")
print(circle_area)


# After:
#
#     from math import pi
#
# the name `pi` directly refers to the imported object.
#
# We therefore write:
#
#     pi
#
# rather than:
#
#     math.pi


# =============================================================================
# 3. IMPORTING A CLASS
# =============================================================================

# `from ... import ...` can also import classes.
#
# `pathlib` contains the `Path` class.

from pathlib import Path


current_directory = Path.cwd()

print("\nCurrent directory:")
print(current_directory)


# Here:
#
#     Path
#
# directly refers to the imported class.
#
# We can therefore write:
#
#     Path.cwd()
#
# instead of:
#
#     pathlib.Path.cwd()


# =============================================================================
# 4. IMPORTED OBJECTS ARE AVAILABLE BY THEIR LOCAL NAMES
# =============================================================================

# After:
#
#     from math import sqrt
#
# `sqrt` becomes a name in the current namespace.
#
# We can demonstrate this using `callable()`.

print("\nIs sqrt callable?")
print(callable(sqrt))


# The expected result is:
#
#     True
#
# This confirms that the local name `sqrt` refers to a callable function.


# =============================================================================
# 5. THE IMPORTED OBJECT IS NOT AUTOMATICALLY ACCESSED THROUGH THE MODULE
# =============================================================================

# With:
#
#     from math import sqrt
#
# the common usage is:
#
#     sqrt(100)
#
# rather than:
#
#     math.sqrt(100)
#
# because this file did not bind the name `math` through this import statement.


square_root = sqrt(100)

print("\nDirect function access:")
print(square_root)


# This is one of the main differences between:
#
#     import math
#
# and:
#
#     from math import sqrt


# =============================================================================
# 6. DIFFERENCE BETWEEN `import` AND `from ... import`
# =============================================================================

# Form 1:
#
#     import math
#
# Access:
#
#     math.sqrt()
#
# The name `math` refers to the module.
#
#
# Form 2:
#
#     from math import sqrt
#
# Access:
#
#     sqrt()
#
# The name `sqrt` refers directly to the imported function.
#
#
# Mental model:
#
#     import math
#         ↓
#     current namespace
#         ↓
#     math ──────────→ module
#                         ↓
#                       sqrt
#
#
#     from math import sqrt
#         ↓
#     current namespace
#         ↓
#     sqrt ───────────→ function


# =============================================================================
# 7. IMPORTING AN OBJECT DOES NOT COPY IT
# =============================================================================

# `from math import sqrt` does not create a new copy of the function.
#
# The local name `sqrt` refers to the function object provided by the
# math module.
#
# This is a name-binding operation rather than a source-code copy operation.


# =============================================================================
# 8. ALIASING AN IMPORTED OBJECT
# =============================================================================

# An imported object can also be given a local alias:
#
#     from module import object as alias
#
# Example:

from math import sqrt as square_root_function


print("\nAliased imported function:")
print(square_root_function(144))


# Here:
#
#     square_root_function
#
# is the local name bound to the imported `sqrt` function.
#
# This is different from:
#
#     import math as mathematics
#
# because that aliases the MODULE.
#
# Here we are aliasing an OBJECT from the module.


# =============================================================================
# 9. MODULE ALIAS VS OBJECT ALIAS
# =============================================================================

# Module alias:
#
#     import math as mathematics
#
# Access:
#
#     mathematics.sqrt()
#
#
# Object alias:
#
#     from math import sqrt as square_root_function
#
# Access:
#
#     square_root_function()
#
#
# The difference is:
#
#     import ... as ...
#         → aliases the module
#
#     from ... import ... as ...
#         → aliases the selected object


# =============================================================================
# 10. IMPORTING AN OBJECT FROM A NESTED MODULE
# =============================================================================

# Python modules can be organized into packages.
#
# For example, `pathlib` is a module containing the `Path` class.
#
# We already used:
#
#     from pathlib import Path
#
# The resulting local name is:
#
#     Path
#
# This demonstrates that the object imported using `from ... import ...`
# does not have to be a function.


# =============================================================================
# 11. NAME BINDING
# =============================================================================

# The most useful mental model for:
#
#     from math import sqrt
#
# is:
#
#     Find `sqrt` inside `math`
#             ↓
#     bind that object to the name `sqrt`
#     in the current namespace.
#
# The current namespace now contains a name:
#
#     sqrt
#
# which refers to the imported function.


# =============================================================================
# 12. LOCAL NAME CAN BE DIFFERENT FROM ORIGINAL NAME
# =============================================================================

# Using `as`, the local name can differ from the object's original name.

from math import factorial as calculate_factorial


factorial_result = calculate_factorial(5)

print("\nAliased factorial function:")
print(factorial_result)


# The function is originally named:
#
#     factorial
#
# but this file uses:
#
#     calculate_factorial
#
# as the local name.


# =============================================================================
# 13. IMPORTING SPECIFIC OBJECTS CAN MAKE CODE SHORTER
# =============================================================================

# Compare:
#
#     import math
#
#     result = math.sqrt(25)
#     result = math.factorial(5)
#
# with:
#
#     from math import sqrt, factorial
#
#     result = sqrt(25)
#     result = factorial(5)
#
# The second form can make code shorter.
#
# However, importing many names directly can also make it harder to see
# where a name came from.
#
# Import conventions and style considerations are covered separately.


# =============================================================================
# 14. IMPORTING A NON-EXISTENT OBJECT
# =============================================================================

# Python raises ImportError if the requested object cannot be imported.
#
# For example, this would fail:
#
#     from math import does_not_exist
#
# because the `math` module does not provide an object with that name.
#
# The example is intentionally kept commented out so this file remains
# completely runnable.
#
# Uncommenting it would raise:
#
#     ImportError


# from math import does_not_exist


# =============================================================================
# 15. IMPORTING A MODULE OBJECT USING `from`
# =============================================================================

# The object after `import` does not necessarily have to be a function.
#
# Python packages can contain submodules.
#
# For example, `xml` contains submodules.
#
# This form:
#
#     from xml import etree
#
# imports the `etree` submodule and binds it to the local name `etree`.

from xml import etree


print("\nImported submodule:")
print(etree)


# This demonstrates that:
#
#     from package import name
#
# can be used to access names that are modules themselves.


# =============================================================================
# 16. `from ... import ...` DOES NOT MEAN "COPY EVERYTHING"
# =============================================================================

# Consider:
#
#     from math import sqrt
#
# Only the requested name `sqrt` is bound directly in the current namespace.
#
# Other math objects are not automatically bound:
#
#     pi
#     factorial
#     sin
#     cos
#
# They would need to be imported separately if direct access is desired.


# =============================================================================
# 17. COMMON MENTAL MODEL
# =============================================================================

# Think of:
#
#     from math import sqrt
#
# as:
#
#     math module
#         │
#         ├── sqrt
#         ├── pi
#         ├── factorial
#         ├── sin
#         └── ...
#              │
#              │ select
#              ▼
#            sqrt
#              │
#              ▼
#       current namespace
#
# Only the selected object gets the local name `sqrt`.


# =============================================================================
# 18. IMPORTANT DISTINCTION
# =============================================================================

# These two statements are NOT interchangeable in terms of the names
# they create:
#
#     import math
#
# creates:
#
#     math
#
#
# while:
#
#     from math import sqrt
#
# creates:
#
#     sqrt
#
#
# Therefore:
#
#     import math
#     math.sqrt(25)
#
# and:
#
#     from math import sqrt
#     sqrt(25)
#
# provide different namespace structures even though both access the
# same underlying function.


# =============================================================================
# 19. KEY TAKEAWAYS
# =============================================================================

# 1. `from ... import ...` imports a selected object from a module.
#
# 2. Basic syntax:
#
#       from module_name import object_name
#
# 3. The imported object becomes available directly by its name.
#
#       from math import sqrt
#
#       sqrt(25)
#
# 4. The imported object can be a:
#
#       - variable
#       - function
#       - class
#       - submodule
#       - other module-level object
#
# 5. An imported object can be given an alias:
#
#       from math import sqrt as square_root
#
# 6. `import module` binds the module name.
#
# 7. `from module import object` binds the selected object name.
#
# 8. `from ... import ...` does not copy the object's source code.
#
# 9. Importing a non-existent object raises `ImportError`.
#
# 10. Importing multiple objects will be covered separately in:
#
#       05_import_multiple_objects.py