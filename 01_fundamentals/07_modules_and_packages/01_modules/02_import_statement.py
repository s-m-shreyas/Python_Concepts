# type: ignore
"""
02_import_statement.py

Topic:
    The import statement

Purpose:
    Understand how Python imports a module and how objects defined
    inside that module are accessed.

Concepts covered:
    1. Basic import syntax
    2. Importing a custom module
    3. Accessing module-level variables
    4. Accessing module-level functions
    5. Accessing module-level classes
    6. Module-qualified names
    7. Importing the same module only once
    8. Difference between importing a module and accessing its objects

Important:
    - This file uses a small custom module created dynamically at runtime
      so that the example remains completely self-contained.
    - The temporary module is removed after the demonstration.
    - Import aliases are intentionally not covered here.
      They are covered in 03_import_as.py.
    - "from ... import ..." is intentionally not covered here.
      It is covered in 04_from_import.py.
"""


# =============================================================================
# 1. WHAT DOES `import` DO?
# =============================================================================

# The basic import syntax is:
#
#     import module_name
#
# After the import, the module is available through its module name.
#
# Objects inside the module are accessed using:
#
#     module_name.object_name
#
# Conceptually:
#
#     import module
#            ↓
#     module
#            ↓
#     module.object
#
# Example:
#
#     import math
#
#     math.sqrt(25)
#
# Here:
#
#     math      → module
#     sqrt      → object/function inside the module
#
#     math.sqrt → module-qualified name


# =============================================================================
# 2. CREATE A SMALL CUSTOM MODULE FOR THE EXAMPLES
# =============================================================================

# Normally, a custom module would already exist as a separate `.py` file.
#
# For example:
#
#     project/
#     │
#     ├── 02_import_statement.py
#     └── calculator.py
#
# Then we could simply write:
#
#     import calculator
#
# To keep this teaching file copy-paste runnable by itself, we create
# a small temporary module file programmatically.

from pathlib import Path
import sys
import tempfile


temporary_directory = Path(tempfile.mkdtemp())
module_file = temporary_directory / "calculator_module.py"

module_file.write_text(
    """
MODULE_NAME = "Calculator Module"
DEFAULT_VALUE = 10


def add(first: int, second: int) -> int:
    return first + second


def multiply(first: int, second: int) -> int:
    return first * second


class Calculator:
    def subtract(self, first: int, second: int) -> int:
        return first - second
""".strip()
    + "\n",
    encoding="utf-8",
)


# Python needs to know where it can search for the module.
#
# The mechanics of module searching and `sys.path` are covered deeply in:
#
#     02_module_search_and_resolution/
#
# Here, we only make the temporary module discoverable so this file can run
# independently.

sys.path.insert(0, str(temporary_directory))


# =============================================================================
# 3. BASIC MODULE IMPORT
# =============================================================================

import calculator_module


# After this statement:
#
#     import calculator_module
#
# Python makes the module available through the name:
#
#     calculator_module
#
# The module itself is now the object referred to by that name.


# =============================================================================
# 4. ACCESS A MODULE-LEVEL VARIABLE
# =============================================================================

# The module contains:
#
#     MODULE_NAME = "Calculator Module"
#
# We access it through the module name.

print("Module name:")
print(calculator_module.MODULE_NAME)


# Notice the structure:
#
#     calculator_module.MODULE_NAME
#     └───────┬───────┘ └──────┬──────┘
#           module            object
#
# This is called qualified access.


# =============================================================================
# 5. ACCESS ANOTHER MODULE-LEVEL VARIABLE
# =============================================================================

print("\nDefault value:")
print(calculator_module.DEFAULT_VALUE)


# The variable belongs to the imported module's namespace.
#
# It is accessed using:
#
#     module_name.variable_name


# =============================================================================
# 6. ACCESS A MODULE-LEVEL FUNCTION
# =============================================================================

# The module contains:
#
#     def add(first, second):
#         ...
#
# We access and call it using:

addition_result = calculator_module.add(10, 20)

print("\nAddition:")
print(addition_result)


# The important point is that:
#
#     calculator_module.add
#
# refers to the function defined inside calculator_module.
#
# Calling it:
#
#     calculator_module.add(10, 20)
#
# executes that function.


# =============================================================================
# 7. ACCESS ANOTHER MODULE-LEVEL FUNCTION
# =============================================================================

multiplication_result = calculator_module.multiply(5, 4)

print("\nMultiplication:")
print(multiplication_result)


# Again:
#
#     calculator_module.multiply
#
# refers to the function stored in the module's namespace.


# =============================================================================
# 8. ACCESS A CLASS DEFINED INSIDE A MODULE
# =============================================================================

# Modules can contain classes as well.
#
# The custom module contains:
#
#     class Calculator:
#         ...
#
# We can access that class through the module.

calculator = calculator_module.Calculator()


# We can now use the object created from that class.

subtraction_result = calculator.subtract(20, 7)

print("\nSubtraction:")
print(subtraction_result)


# Notice:
#
#     calculator_module.Calculator
#            ↓
#         class
#
#     calculator_module.Calculator()
#            ↓
#        class instance
#
# The module acts as the namespace through which the class is accessed.


# =============================================================================
# 9. MODULE-QUALIFIED NAMES
# =============================================================================

# A name written as:
#
#     module_name.object_name
#
# is a qualified name.
#
# Examples from this file:
#
#     calculator_module.MODULE_NAME
#     calculator_module.DEFAULT_VALUE
#     calculator_module.add
#     calculator_module.multiply
#     calculator_module.Calculator
#
# The module name tells Python where the object is being accessed from.


# =============================================================================
# 10. WHY USE MODULE-QUALIFIED ACCESS?
# =============================================================================

# Imagine two different modules both contain a function called:
#
#     calculate()
#
# If we access them through their module namespaces:
#
#     module_a.calculate()
#     module_b.calculate()
#
# Python can distinguish between them.
#
# The module name therefore provides an important namespace boundary.


# =============================================================================
# 11. THE IMPORTED MODULE IS A MODULE OBJECT
# =============================================================================

# The name `calculator_module` refers to a module object.

print("\nImported object type:")
print(type(calculator_module))


# The result is:
#
#     <class 'module'>
#
# This reinforces an important idea:
#
#     import calculator_module
#
# does not simply copy the source code into this file.
#
# Python creates or retrieves a module object and binds the name
# `calculator_module` to that module object.


# =============================================================================
# 12. IMPORTING THE SAME MODULE AGAIN
# =============================================================================

# If the same module is imported again:

import calculator_module


# Python does not normally create an entirely new independent module object
# for every import statement.
#
# Imported modules are cached by Python.
#
# The module cache is associated with `sys.modules`.
#
# The detailed import and resolution mechanism will be studied later.
#
# For now, the important observation is that repeated imports of the same
# module generally refer to the same loaded module object.

print("\nRepeated import refers to the same module object:")
print(calculator_module is sys.modules["calculator_module"])


# The expected result is:
#
#     True


# =============================================================================
# 13. IMPORT DOES NOT MEAN "IMPORT EVERY NAME INTO THE CURRENT NAMESPACE"
# =============================================================================

# Consider:
#
#     import calculator_module
#
# This creates the name:
#
#     calculator_module
#
# in the current namespace.
#
# It does NOT create these names directly:
#
#     add
#     multiply
#     Calculator
#
# Therefore, this would NOT work simply because of the import above:
#
#     add(10, 20)
#
# Instead, we use:
#
#     calculator_module.add(10, 20)
#
# The `from module import object` syntax, which provides direct access to
# selected objects, is covered separately in:
#
#     04_from_import.py


# =============================================================================
# 14. IMPORTING A STANDARD-LIBRARY MODULE
# =============================================================================

# The same basic mechanism applies to Python's standard-library modules.
#
# For example:

import math

square_root = math.sqrt(81)

print("\nStandard-library module:")
print("Square root:", square_root)


# Here:
#
#     math
#       ↓
#     module
#
#     math.sqrt
#       ↓
#     function inside the module
#
# The difference between standard-library modules and custom modules will
# be discussed in more detail later.


# =============================================================================
# 15. IMPORTING DOES NOT REQUIRE A FUNCTION CALL
# =============================================================================

# Notice the syntax:
#
#     import math
#
# There are no parentheses.
#
# `import` is a Python statement/keyword construct used to perform
# module importing.
#
# It is not equivalent to:
#
#     import(math)
#
# The import statement has its own syntax and semantics.


# =============================================================================
# 16. BASIC IMPORT MENTAL MODEL
# =============================================================================

# A useful mental model is:
#
#     import module_name
#            │
#            ▼
#     Python locates the module
#            │
#            ▼
#     Python loads/initializes the module
#            │
#            ▼
#     module object becomes available
#            │
#            ▼
#     module_name refers to that object
#            │
#            ▼
#     module_name.object_name
#
# The detailed process behind "Python locates the module" is intentionally
# postponed until the module search and resolution section.


# =============================================================================
# 17. CLEAN UP THE TEMPORARY MODULE
# =============================================================================

# The examples above used a temporary directory so this file could be
# executed independently.
#
# Remove the temporary module from the import cache before cleaning up.

sys.modules.pop("calculator_module", None)

try:
    sys.path.remove(str(temporary_directory))
except ValueError:
    pass

module_file.unlink(missing_ok=True)
temporary_directory.rmdir()


# =============================================================================
# 18. KEY TAKEAWAYS
# =============================================================================

# 1. `import module_name` imports a module.
#
# 2. The imported module is accessed through its module name.
#
# 3. Objects inside the module are accessed using:
#
#       module_name.object_name
#
# 4. A module can contain:
#
#       - variables
#       - constants
#       - functions
#       - classes
#
# 5. Module-qualified access keeps names organized within the module's
#    namespace.
#
# 6. `import module_name` does not directly place every object from the
#    module into the current namespace.
#
# 7. Python caches loaded modules, so repeated imports generally reuse
#    the same module object.
#
# 8. The detailed mechanics of locating and resolving modules are covered
#    later in:
#
#       02_module_search_and_resolution/
#
# 9. Import aliases are covered in:
#
#       03_import_as.py
#
# 10. `from ... import ...` is covered in:
#
#       04_from_import.py