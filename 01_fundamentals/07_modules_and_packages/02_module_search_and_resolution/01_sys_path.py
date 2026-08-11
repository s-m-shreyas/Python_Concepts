# type: ignore
"""
01_sys_path.py

Topic:
    sys.path

Purpose:
    Understand how Python's module search path works and how `sys.path`
    controls the locations Python searches when resolving imports.

Concepts covered:
    1. What sys.path is
    2. Why Python needs a module search path
    3. Inspecting sys.path
    4. The type of sys.path
    5. Current working directory vs script directory
    6. Standard library locations
    7. Site-packages
    8. Search order
    9. How Python uses sys.path during import
    10. Adding a custom directory to sys.path
    11. Removing a directory from sys.path
    12. Temporary modification of sys.path
    13. Why modifying sys.path globally is usually discouraged
    14. sys.path and import resolution
    15. Practical project example
    16. Common misconceptions

Important:
    - Basic import syntax is covered in:
          ../01_modules/02_import_statement.py
    - Module attributes are covered in:
          ../01_modules/07_module_attributes.py
    - Module execution is covered in:
          ../01_modules/08_module_execution.py
    - The detailed process Python uses to search for a module will be
      covered further in:
          02_module_search_path.py
          04_import_resolution.py

Note:
    `sys.path` is a runtime list. Its exact contents depend on how and
    where Python is being executed, so the output of this file will vary
    between systems and environments.
"""


# =============================================================================
# 1. WHAT IS `sys.path`?
# =============================================================================

# `sys.path` is a list of strings representing locations that Python
# searches when it needs to find an importable module or package.
#
# For example, when Python encounters:
#
#     import math
#
# or:
#
#     import my_module
#
# Python needs to determine where the requested module can be found.
#
# `sys.path` provides the locations that participate in that search.


import sys


# =============================================================================
# 2. INSPECTING `sys.path`
# =============================================================================

print("Python module search path:")
print(sys.path)


# The result is a list.
#
# Each element represents a location that Python can search for modules.
#
# The exact list will differ depending on:
#
#     - operating system
#     - Python installation
#     - virtual environment
#     - how Python was started
#     - environment configuration
#     - installed packages


# =============================================================================
# 3. THE TYPE OF `sys.path`
# =============================================================================

print("\nType of sys.path:")
print(type(sys.path))


# Expected result:
#
#     <class 'list'>
#
# Therefore:
#
#     sys.path
#
# is a normal Python list.


# =============================================================================
# 4. ELEMENTS OF `sys.path` ARE STRINGS
# =============================================================================

print("\nTypes of sys.path entries:")

for path_entry in sys.path:
    print(type(path_entry), "->", repr(path_entry))


# Each search location is represented as a string.
#
# Conceptually:
#
#     sys.path
#         ↓
#     [
#         "location_1",
#         "location_2",
#         "location_3",
#         ...
#     ]


# =============================================================================
# 5. HOW PYTHON USES `sys.path`
# =============================================================================

# Suppose Python sees:
#
#     import example
#
# Python needs to find something corresponding to:
#
#     example
#
# Python searches locations associated with its import system.
#
# `sys.path` contains important locations used during that search.
#
# Conceptually:
#
#     import example
#          ↓
#     search location 1
#          ↓
#     not found
#          ↓
#     search location 2
#          ↓
#     not found
#          ↓
#     search location 3
#          ↓
#     found
#          ↓
#     load module
#
# The detailed resolution process is more complicated than this simplified
# model, but this is the core idea behind `sys.path`.


# =============================================================================
# 6. SEARCH ORDER MATTERS
# =============================================================================

# `sys.path` is ordered.
#
# This means the position of a path matters.
#
# For example:
#
#     [
#         "location_A",
#         "location_B",
#         "location_C",
#     ]
#
# Python considers these locations in search order when resolving
# importable modules.
#
# Therefore, two different directories containing modules with the same
# import name can potentially lead to different results depending on
# which directory is encountered first.


# =============================================================================
# 7. DISPLAYING THE SEARCH ORDER
# =============================================================================

print("\nIndexed sys.path entries:")

for index, path_entry in enumerate(sys.path):
    print(f"{index}: {path_entry!r}")


# `enumerate()` makes the ordering easier to understand.
#
# Example conceptually:
#
#     0: '...'
#     1: '...'
#     2: '...'
#
# The lower index represents an earlier position in the list.


# =============================================================================
# 8. THE EMPTY STRING IN `sys.path`
# =============================================================================

# You may sometimes see:
#
#     ''
#
# as one of the entries in `sys.path`.
#
# The empty string has a special practical meaning in Python's import
# machinery: it represents the current working directory in contexts
# where Python initializes the path this way.
#
# Therefore:
#
#     ''
#
# is not simply a useless empty value.


print("\nEmpty-string path entries:")

for index, path_entry in enumerate(sys.path):
    if path_entry == "":
        print(f"Empty-string entry found at index {index}.")


# Depending on how this file is executed, you may or may not see one.


# =============================================================================
# 9. CURRENT WORKING DIRECTORY IS NOT THE SAME AS SCRIPT DIRECTORY
# =============================================================================

# This distinction is extremely important.
#
# Two concepts are often confused:
#
#     current working directory
#
# and:
#
#     directory containing the Python script.
#
# They are not necessarily the same directory.


from pathlib import Path


print("\nCurrent working directory:")
print(Path.cwd())


# `Path.cwd()` tells us the current working directory of the running
# Python process.


# =============================================================================
# 10. THE DIRECTORY OF THIS SCRIPT
# =============================================================================

print("\nDirectory containing this script:")
print(Path(__file__).resolve().parent)


# These two values can be different.
#
# For example:
#
#     current working directory
#         ↓
#     C:\\projects
#
# while:
#
#     script directory
#         ↓
#     C:\\projects\\python-concepts\\01_fundamentals\\...
#
# Therefore, do not automatically assume:
#
#     current working directory == script directory


# =============================================================================
# 11. WHY THIS DISTINCTION MATTERS FOR IMPORTS
# =============================================================================

# When learning imports, it is tempting to think:
#
#     "Python always searches the folder where my script is."
#
# That is an oversimplification.
#
# Python's import behavior depends on how the interpreter was started,
# the module being executed, package context, environment configuration,
# and the import machinery.
#
# `sys.path` gives us a concrete way to inspect the paths available to
# the current process.


# =============================================================================
# 12. STANDARD LIBRARY LOCATIONS
# =============================================================================

# Python's standard library contains modules such as:
#
#     math
#     pathlib
#     datetime
#     json
#     re
#     os
#     sys
#
# Python needs locations from which these modules can be loaded.
#
# Relevant standard-library paths are normally represented somewhere
# in the interpreter's import configuration.


print("\nPaths that look related to the standard library:")

for path_entry in sys.path:
    if "site-packages" not in path_entry.lower():
        print(path_entry)


# This is only an inspection example.
#
# We should not assume every non-site-packages entry is a standard-library
# directory because `sys.path` can contain many other locations.


# =============================================================================
# 13. SITE-PACKAGES
# =============================================================================

# Python installations commonly have a directory called:
#
#     site-packages
#
# This is where third-party Python packages are commonly installed.
#
# Examples include packages such as:
#
#     pandas
#     numpy
#     requests
#
# When Python searches for these packages, their installation locations
# need to be available to the import system.


print("\nPaths containing site-packages:")

for path_entry in sys.path:
    if "site-packages" in path_entry.lower():
        print(path_entry)


# If your environment has third-party packages installed, you will often
# see one or more site-packages paths.


# =============================================================================
# 14. WHY `pandas` CAN BE IMPORTED WITHOUT ITS FULL PATH
# =============================================================================

# Suppose pandas is installed in:
#
#     C:\\Python\\Lib\\site-packages
#
# You normally write:
#
#     import pandas
#
# rather than:
#
#     import "C:\\Python\\Lib\\site-packages\\pandas"
#
# Python's import system knows about the relevant package location through
# its module search configuration, including `sys.path`.


# =============================================================================
# 15. CREATING A CUSTOM MODULE DIRECTORY
# =============================================================================

# We can demonstrate how adding a directory to `sys.path` makes modules
# in that directory available to the import system.
#
# To keep this example self-contained, we create a temporary directory
# and a temporary module.

import tempfile


temporary_directory = Path(tempfile.mkdtemp())

temporary_module = temporary_directory / "custom_module.py"

temporary_module.write_text(
    """
message = "Hello from the custom module."


def get_message() -> str:
    return message
""".strip(),
    encoding="utf-8",
)


print("\nTemporary custom module:")
print(temporary_module)


# At this point, the directory containing the module is NOT explicitly
# added to `sys.path`.


# =============================================================================
# 16. CHECK WHETHER THE DIRECTORY IS IN `sys.path`
# =============================================================================

temporary_directory_string = str(temporary_directory)

print("\nTemporary directory initially in sys.path:")
print(temporary_directory_string in sys.path)


# Expected result:
#
#     False
#
# This means the temporary directory has not been explicitly added to
# the current module search path.


# =============================================================================
# 17. ADDING A DIRECTORY TO `sys.path`
# =============================================================================

# Because `sys.path` is a list, we can add a directory to it.

sys.path.insert(0, temporary_directory_string)


print("\nTemporary directory after insertion:")
print(temporary_directory_string in sys.path)


# Expected result:
#
#     True
#
# We have now modified the current process's module search path.


# =============================================================================
# 18. WHY USE `insert(0, ...)`?
# =============================================================================

# We used:
#
#     sys.path.insert(0, temporary_directory_string)
#
# instead of:
#
#     sys.path.append(temporary_directory_string)
#
# because `insert(0, ...)` places the directory at the beginning.
#
# This gives it an earlier position in the search order.
#
# Conceptually:
#
#     Before:
#
#         [A, B, C]
#
#     After insert(0, X):
#
#         [X, A, B, C]
#
#
# Whereas:
#
#     append(X)
#
# produces:
#
#     [A, B, C, X]


# =============================================================================
# 19. IMPORTING FROM THE CUSTOM DIRECTORY
# =============================================================================

# Now that the directory is part of sys.path, Python can resolve the
# custom module.

import custom_module


print("\nCustom module imported successfully:")
print(custom_module.get_message())


# Notice the important relationship:
#
#     custom_module.py
#             ↓
#     directory containing custom_module.py
#             ↓
#     directory added to sys.path
#             ↓
#     import custom_module
#             ↓
#     Python finds the module
#             ↓
#     module is loaded
#
# Without the directory being available to the import machinery, this
# import would not work in this isolated example.


# =============================================================================
# 20. THE MODULE'S `__file__`
# =============================================================================

# We can verify which file Python actually loaded.

print("\nImported custom module file:")
print(custom_module.__file__)


# This is a useful debugging technique.
#
# If you are ever unsure which copy of a module Python imported:
#
#     print(module.__file__)
#
# can reveal the actual module file being used.


# =============================================================================
# 21. VERIFYING THE MODULE SEARCH PATH
# =============================================================================

print("\nFirst sys.path entry:")
print(sys.path[0])


# Because we inserted our temporary directory at index 0, it should
# currently appear as the first entry.


# =============================================================================
# 22. APPEND VS INSERT
# =============================================================================

# Two common ways to modify sys.path are:
#
#     sys.path.append(path)
#
# and:
#
#     sys.path.insert(0, path)
#
#
# APPEND:
#
#     Adds the path at the end.
#
#
# INSERT(0, ...):
#
#     Adds the path at the beginning.
#
#
# The difference matters because path order can influence which module
# is found first when multiple locations contain modules with the same
# import name.


# =============================================================================
# 23. REMOVING A DIRECTORY FROM `sys.path`
# =============================================================================

# Since sys.path is a list, a path can also be removed.

sys.path.remove(temporary_directory_string)


print("\nTemporary directory after removal:")
print(temporary_directory_string in sys.path)


# Expected result:
#
#     False


# =============================================================================
# 24. IMPORTANT: `sys.path` IS PROCESS-LOCAL STATE
# =============================================================================

# When we modify:
#
#     sys.path
#
# we are modifying the search path of the current Python process.
#
# This does not permanently modify Python's installation.
#
# For example:
#
#     sys.path.append("some_directory")
#
# does NOT mean:
#
#     "Python will permanently remember this directory forever."
#
# It only changes the current running interpreter's list.


# =============================================================================
# 25. TEMPORARY PATH MODIFICATION
# =============================================================================

# A common pattern is:
#
#     sys.path.insert(0, custom_path)
#
#     # perform import
#
#     sys.path.remove(custom_path)
#
# This can temporarily make a directory available.
#
# We already demonstrated this pattern above.


# =============================================================================
# 26. WHY MANUALLY MODIFYING `sys.path` IS USUALLY DISCOURAGED
# =============================================================================

# Although modifying sys.path is possible, it is generally not the first
# solution you should reach for in a well-structured application.
#
# Excessive manual modification can make imports:
#
#     - harder to understand
#     - environment-dependent
#     - difficult to reproduce
#     - sensitive to path ordering
#     - harder to debug
#
# Larger projects normally use proper package structures and environments
# instead of repeatedly manipulating sys.path.


# =============================================================================
# 27. PROJECT STRUCTURE IS PREFERRED
# =============================================================================

# For example, instead of:
#
#     sys.path.insert(0, "C:\\some\\random\\folder")
#
# a project should normally have a clear package structure such as:
#
#     project/
#     │
#     ├── src/
#     │   └── application/
#     │       ├── __init__.py
#     │       ├── ingestion.py
#     │       └── transformation.py
#     │
#     └── ...
#
# and use an appropriate project/environment setup.
#
# This makes module resolution predictable and maintainable.


# =============================================================================
# 28. PRACTICAL DATA-ENGINEERING EXAMPLE
# =============================================================================

# Imagine a data-engineering project:
#
#     etl_project/
#     │
#     ├── ingestion/
#     │   ├── csv_reader.py
#     │   └── s3_reader.py
#     │
#     ├── transformation/
#     │   └── cleaner.py
#     │
#     └── validation/
#         └── validator.py
#
# If Python is correctly configured to recognize the project/package
# structure, code can use imports such as:
#
#     from ingestion.csv_reader import read_csv
#
# or:
#
#     from transformation.cleaner import clean_data
#
# Python's import system needs to know where the relevant package
# hierarchy begins.
#
# That is where the module search path becomes important.


# =============================================================================
# 29. `sys.path` IS NOT THE ENTIRE IMPORT SYSTEM
# =============================================================================

# A very important distinction:
#
#     sys.path
#
# is a major part of understanding module lookup, but it is not the
# entire import mechanism.
#
# Python's import system also involves:
#
#     - importers
#     - finders
#     - loaders
#     - module specifications
#     - package metadata
#     - sys.modules
#
# We will gradually build these concepts in the next files.
#
# Therefore, do not reduce Python imports to:
#
#     "Python loops over sys.path and opens a file."
#
# That is useful as a beginner mental model, but the real mechanism is
# richer.


# =============================================================================
# 30. `sys.path` AND `sys.modules` ARE DIFFERENT
# =============================================================================

# These two are often confused.
#
# `sys.path`:
#
#     tells the import system where it can search.
#
#
# `sys.modules`:
#
#     stores modules that have already been loaded.
#
#
# Conceptually:
#
#     sys.path
#         ↓
#     "Where can Python look?"
#
#
#     sys.modules
#         ↓
#     "What modules has Python already loaded?"
#
#
# They solve different parts of the import process.


# =============================================================================
# 31. SEARCH PATH VS LOADED MODULE
# =============================================================================

# Imagine:
#
#     import pandas
#
# First Python may need to locate pandas.
#
# The search configuration, including relevant path entries, participates
# in locating it.
#
# After pandas is loaded:
#
#     sys.modules["pandas"]
#
# can reference the loaded module object.
#
# Therefore:
#
#     path
#         → helps locate
#
#     modules cache
#         → helps reuse loaded modules


# =============================================================================
# 32. INSPECTING WHERE A MODULE WAS LOADED FROM
# =============================================================================

# The combination of:
#
#     module.__file__
#
# and:
#
#     sys.path
#
# can be very useful when debugging imports.
#
# For example:

print("\nCurrent pathlib module location:")
print(Path.__module__)


# Note:
#
# `Path.__module__` tells us the module in which the `Path` class is
# defined.
#
# This is different from:
#
#     pathlib.__file__
#
# which tells us the file associated with the pathlib module.
#
# Let's inspect the actual module:

import pathlib

print("\nPathlib module file:")
print(pathlib.__file__)


# This distinction will become useful as we study module resolution.


# =============================================================================
# 33. DUPLICATE MODULE NAMES
# =============================================================================

# Imagine two directories:
#
#     directory_A/
#         helper.py
#
#     directory_B/
#         helper.py
#
# and:
#
#     sys.path = [
#         directory_A,
#         directory_B,
#     ]
#
# If Python searches directory_A first and finds:
#
#     helper.py
#
# then that copy may be the one loaded.
#
# If the order changes:
#
#     sys.path = [
#         directory_B,
#         directory_A,
#     ]
#
# a different `helper.py` may be selected.
#
# This is one reason path ordering matters.


# =============================================================================
# 34. WHY SHADOWING CAN BE DANGEROUS
# =============================================================================

# Suppose your project contains:
#
#     random.py
#
# while your code expects Python's standard-library:
#
#     random
#
# Depending on the import context and path ordering, your local module
# can interfere with the expected import.
#
# Similar issues can happen with names such as:
#
#     json.py
#     logging.py
#     pathlib.py
#     typing.py
#
# Therefore, avoid naming your own modules after important standard-library
# modules.


# =============================================================================
# 35. INSPECTING PATHS CLEANLY
# =============================================================================

# A useful debugging pattern is:

print("\nFormatted sys.path:")

for index, path_entry in enumerate(sys.path, start=1):
    print(f"{index:>2}. {path_entry}")


# This does not modify sys.path.
#
# It simply makes the current search configuration easier to read.


# =============================================================================
# 36. A SIMPLE MENTAL MODEL
# =============================================================================

# For now, use this mental model:
#
#     import module_name
#             ↓
#     Python needs to locate module_name
#             ↓
#     import system uses its search configuration
#             ↓
#     sys.path provides important search locations
#             ↓
#     Python searches according to its import rules
#             ↓
#     module is found
#             ↓
#     module is loaded/executed
#             ↓
#     module becomes available
#
#
# This is intentionally simplified.
#
# The next topics will refine this model.


# =============================================================================
# 37. COMMON MISCONCEPTIONS
# =============================================================================

# MISCONCEPTION 1:
#
#     "`sys.path` is a single folder."
#
# Correction:
#
#     `sys.path` is a list containing multiple search locations.
#
#
# MISCONCEPTION 2:
#
#     "`sys.path` is fixed forever."
#
# Correction:
#
#     It is a mutable runtime list.
#
#
# MISCONCEPTION 3:
#
#     "Changing sys.path permanently changes Python."
#
# Correction:
#
#     Normal modifications affect the current Python process.
#
#
# MISCONCEPTION 4:
#
#     "The current working directory is always the script directory."
#
# Correction:
#
#     They can be different.
#
#
# MISCONCEPTION 5:
#
#     "sys.path contains only third-party packages."
#
# Correction:
#
#     It can contain locations for many kinds of importable modules,
#     including project code and standard-library-related locations.
#
#
# MISCONCEPTION 6:
#
#     "`sys.path` is the complete import system."
#
# Correction:
#
#     It is an important component, not the entire import mechanism.
#
#
# MISCONCEPTION 7:
#
#     "If a module exists somewhere on my computer, Python can import it."
#
# Correction:
#
#     The module must be discoverable through the import system's rules.
#     Simply existing on disk is not enough.


# =============================================================================
# 38. KEY TAKEAWAYS
# =============================================================================

# 1. `sys.path` is a list.
#
# 2. It contains locations used by Python's import machinery.
#
# 3. The order of entries matters.
#
# 4. `sys.path` can be inspected at runtime.
#
# 5. `sys.path` can be modified because it is mutable.
#
# 6. `sys.path.insert(0, path)` places a path at the beginning.
#
# 7. `sys.path.append(path)` places a path at the end.
#
# 8. `sys.path.remove(path)` removes a path.
#
# 9. Manual modification is useful for learning, experimentation, and
#    certain specialized situations, but should not replace proper
#    project/package structure.
#
# 10. The current working directory and script directory are different
#     concepts.
#
# 11. `sys.path` and `sys.modules` have different purposes:
#
#         sys.path
#             → search locations
#
#         sys.modules
#             → loaded module cache
#
# 12. Module resolution depends on more than just sys.path.
#
# 13. Understanding sys.path is the foundation for understanding:
#
#         module search
#         import resolution
#         packages
#         virtual environments
#         import errors
#
# 14. The next file is:
#
#         02_module_search_path.py
#
#     where we will go deeper into the actual locations Python searches
#     and how those locations are established.