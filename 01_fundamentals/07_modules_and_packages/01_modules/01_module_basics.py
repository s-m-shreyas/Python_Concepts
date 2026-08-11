"""
01_module_basics.py

Demonstrates the fundamental concept of a Python module.

A module is a Python source file containing definitions and statements.
A module can contain variables, constants, functions, classes, and
executable statements.

This file intentionally focuses only on module fundamentals.
Import syntax, module search paths, packages, and special module
attributes are covered in later files.
"""


# =============================================================================
# 1. A PYTHON FILE CAN REPRESENT A MODULE
# =============================================================================

# This file itself is a Python source file.
#
# When Python treats this file as a module, its module name is based on
# the filename, without the ".py" extension.
#
# For example:
#
#     01_module_basics.py
#
# represents the module:
#
#     01_module_basics
#
# The ".py" extension identifies the source file.
# The module name identifies the Python module.


# =============================================================================
# 2. A MODULE CAN CONTAIN VARIABLES
# =============================================================================

application_name: str = "Data Processor"
application_version: str = "1.0.0"

record_count: int = 100


# These variables are defined at module level.
#
# Conceptually:
#
#     application_name     -> "Data Processor"
#     application_version  -> "1.0.0"
#     record_count         -> 100


# =============================================================================
# 3. A MODULE CAN CONTAIN FUNCTIONS
# =============================================================================

def add_numbers(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


def get_application_info() -> str:
    """Return basic application information."""
    return f"{application_name} v{application_version}"


# Functions defined at module level also become part of the module's
# namespace.


# =============================================================================
# 4. A MODULE CAN CONTAIN CONSTANTS
# =============================================================================

MAX_RECORDS: int = 1_000
DEFAULT_TIMEOUT: float = 30.0


# Constants are simply module-level names that follow the convention
# of using uppercase letters.
#
# Python does not technically enforce constant immutability.


# =============================================================================
# 5. A MODULE CAN CONTAIN CLASSES
# =============================================================================

class DataRecord:
    """Represent a simple data record."""

    def __init__(self, record_id: int, value: str) -> None:
        self.record_id = record_id
        self.value = value

    def describe(self) -> str:
        """Return a description of the record."""
        return f"Record {self.record_id}: {self.value}"


# Classes defined at module level also belong to the module's namespace.


# =============================================================================
# 6. A MODULE IS A NAMESPACE
# =============================================================================

# A namespace is a mapping between names and objects.
#
# This module has names such as:
#
#     application_name
#     application_version
#     record_count
#     add_numbers
#     get_application_info
#     MAX_RECORDS
#     DEFAULT_TIMEOUT
#     DataRecord
#
# Each name refers to an object.


# We can inspect the module's global namespace using globals().

module_namespace = globals()

print("Module-level names:")
print("application_name:", module_namespace["application_name"])
print("record_count:", module_namespace["record_count"])
print("add_numbers:", module_namespace["add_numbers"])


# =============================================================================
# 7. MODULE NAMES ARE ASSOCIATED WITH OBJECTS
# =============================================================================

# A name does not contain the object itself.
# It refers to an object.
#
# The same idea applies at module level.

first_name = "Python"
second_name = first_name

print("\nName references:")
print("first_name:", first_name)
print("second_name:", second_name)


# The important concept is:
#
#     name
#       ↓
#     object
#
# A module namespace maintains these name-to-object associations.


# =============================================================================
# 8. MODULE-LEVEL FUNCTIONS CAN USE MODULE-LEVEL NAMES
# =============================================================================

print("\nFunction using module-level data:")
print(get_application_info())


# The function can access application_name and application_version because
# those names exist in the module's global namespace.


# =============================================================================
# 9. CREATING AN OBJECT FROM A MODULE-LEVEL CLASS
# =============================================================================

record = DataRecord(101, "Completed")

print("\nModule-level class:")
print(record.describe())


# DataRecord is a class defined in this module.
# The class can therefore be referenced by its module-level name.


# =============================================================================
# 10. MODULE-LEVEL EXECUTABLE STATEMENTS
# =============================================================================

# A module can also contain executable statements.
#
# For example, the following statement executes when Python reaches it:

calculated_total = add_numbers(10, 20)

print("\nModule-level execution:")
print("Calculated total:", calculated_total)


# This is an important characteristic of Python modules:
#
# A module is not necessarily limited to definitions.
# It may also contain statements that execute when the module is executed.
#
# The exact behavior when a module is imported versus executed directly
# will be studied in:
#
#     08_module_execution.py


# =============================================================================
# 11. MODULE OBJECT
# =============================================================================

# Python represents a loaded module using a module object.
#
# The current module can be identified through the global namespace
# associated with this source file.
#
# At this stage, focus on the mental model:
#
#     Python source file
#            ↓
#        module object
#            ↓
#       module namespace
#            ↓
#     names → Python objects
#
# The special attributes that expose information about the current module
# will be studied separately.


# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

# 1. A module is a Python source file used as an organizational unit.
#
# 2. A module can contain:
#       - variables
#       - constants
#       - functions
#       - classes
#       - executable statements
#
# 3. A module has its own namespace.
#
# 4. Names in a module's namespace refer to Python objects.
#
# 5. Module-level functions and classes become part of that namespace.
#
# 6. A module can contain executable code in addition to definitions.
#
# 7. Importing modules and the details of module execution are separate
#    concepts and will be covered in later files.