# type: ignore
"""
02_module_search_path.py

Topic:
    Module search path

Purpose:
    Understand the different locations Python considers when searching
    for modules and packages, how those locations relate to `sys.path`,
    and why the search path can differ between execution environments.

Concepts covered:
    1. What the module search path means
    2. Relationship between sys.path and module search
    3. Script directory
    4. Current working directory
    5. Standard library directories
    6. site-packages
    7. Virtual-environment paths
    8. PYTHONPATH
    9. Environment-dependent search paths
    10. Search path ordering
    11. Project source directories
    12. Why Python may find one module instead of another
    13. Inspecting module locations
    14. Practical debugging techniques
    15. Common misconceptions

Important:
    This file builds on:
        01_sys_path.py

    The next file:
        03_standard_library_vs_custom_modules.py

    will distinguish Python's standard-library modules from modules created
    by the developer.

    A deeper treatment of the complete import-resolution mechanism comes
    later in:
        04_import_resolution.py

Note:
    Exact paths printed by this program depend on the Python installation,
    operating system, execution method, virtual environment, and shell
    configuration.
"""


# =============================================================================
# 1. WHAT IS THE MODULE SEARCH PATH?
# =============================================================================

# When Python encounters:
#
#     import module_name
#
# it needs to determine where that module can be found.
#
# The collection of locations available to the import system is commonly
# referred to as the module search path.
#
# The most visible representation of this path is:
#
#     sys.path
#
# Therefore, a useful beginner mental model is:
#
#     module search path
#             ↓
#         represented by
#             ↓
#          sys.path
#
# However, the complete import mechanism is more sophisticated than
# simply iterating over a list of folders.


import sys
from pathlib import Path


# =============================================================================
# 2. DISPLAY THE CURRENT SEARCH PATH
# =============================================================================

print("Current module search path:")
print()

for index, path_entry in enumerate(sys.path):
    print(f"{index}: {path_entry!r}")


# The output gives us the search locations available to this Python
# process.
#
# The exact entries are environment-dependent.


# =============================================================================
# 3. WHY ARE THERE MULTIPLE SEARCH LOCATIONS?
# =============================================================================

# Python needs to support many types of importable code.
#
# For example:
#
#     import math
#
#     import json
#
#     import pandas
#
#     import my_project_module
#
# These modules can come from very different locations:
#
#     - Python's standard library
#     - third-party packages
#     - the current project
#     - explicitly configured locations
#     - custom development directories
#
# Therefore, Python needs more than one possible search location.


# =============================================================================
# 4. THE FIRST IMPORTANT CONCEPT: SEARCH ORDER
# =============================================================================

# `sys.path` is ordered.
#
# This means that the position of a directory matters.
#
# Consider:
#
#     sys.path = [
#         "directory_A",
#         "directory_B",
#         "directory_C",
#     ]
#
# If all three directories contain:
#
#     helper.py
#
# then the first matching location can influence which `helper` module
# gets imported.
#
# Therefore:
#
#     SEARCH PATH
#
# is not merely a collection of folders.
#
# It is an ORDERED collection of locations.


# =============================================================================
# 5. INSPECT THE FIRST SEARCH ENTRY
# =============================================================================

print("\nFirst search-path entry:")
print(repr(sys.path[0]) if sys.path else "sys.path is empty")


# Depending on how Python was started, the first entry can represent
# the directory associated with the execution context.
#
# Do not assume that the value is always the same across:
#
#     - command-line execution
#     - IDE execution
#     - notebooks
#     - interactive Python
#     - package execution


# =============================================================================
# 6. SCRIPT DIRECTORY
# =============================================================================

# When Python executes a script from a file, the directory associated
# with that script can be important to module discovery.
#
# We can inspect the directory containing this file:

script_directory = Path(__file__).resolve().parent

print("\nDirectory containing this script:")
print(script_directory)


# This is the directory where this `.py` file physically exists.


# =============================================================================
# 7. CURRENT WORKING DIRECTORY
# =============================================================================

# The current working directory belongs to the running process.

current_working_directory = Path.cwd()

print("\nCurrent working directory:")
print(current_working_directory)


# These two values can be different:
#
#     script_directory
#
# and:
#
#     current_working_directory
#
#
# Example:
#
#     script:
#         C:\\projects\\python-concepts\\example.py
#
#     current working directory:
#         C:\\projects
#
# They represent different concepts.


# =============================================================================
# 8. WHY THE DISTINCTION MATTERS
# =============================================================================

# Beginners often use this assumption:
#
#     "Python always searches the directory I'm currently looking at."
#
# That is not a reliable model.
#
# Module discovery depends on the interpreter's execution context and
# import configuration.
#
# `sys.path` lets us inspect the actual search locations available to
# the running interpreter.


# =============================================================================
# 9. STANDARD LIBRARY LOCATIONS
# =============================================================================

# Python ships with a standard library containing modules such as:
#
#     math
#     pathlib
#     json
#     datetime
#     re
#     os
#     sys
#
# These modules are installed alongside the Python interpreter.
#
# Their source or compiled implementation is located within Python's
# installation structure.
#
# We can inspect where selected standard-library modules come from.


import math
import json


print("\nMath module:")
print(math.__file__)

print("\nJSON module:")
print(json.__file__)


# `__file__` provides useful information about the module's associated
# file when that attribute is available.
#
# This is particularly useful for debugging unexpected imports.


# =============================================================================
# 10. STANDARD LIBRARY DOES NOT MEAN "CURRENT PROJECT"
# =============================================================================

# Consider:
#
#     import json
#
# You do not need to provide a filesystem path such as:
#
#     C:\\Python\\Lib\\json
#
# Python's import system knows how to locate standard-library modules
# through the interpreter's configured import environment.


# =============================================================================
# 11. SITE-PACKAGES
# =============================================================================

# Third-party Python packages are commonly installed into a directory
# called:
#
#     site-packages
#
# Examples:
#
#     pandas
#     numpy
#     requests
#
# can commonly live under a site-packages directory.
#
# Let's inspect search-path entries containing "site-packages".

print("\nsite-packages entries:")

site_package_entries = [
    path_entry
    for path_entry in sys.path
    if "site-packages" in path_entry.lower()
]

if site_package_entries:
    for path_entry in site_package_entries:
        print(path_entry)
else:
    print("No site-packages entry was detected in sys.path.")


# The exact location depends on the Python environment.


# =============================================================================
# 12. VIRTUAL ENVIRONMENTS
# =============================================================================

# A virtual environment provides an isolated Python environment for a
# project.
#
# A virtual environment commonly has its own:
#
#     - Python interpreter
#     - installed third-party packages
#     - site-packages directory
#
# Therefore, when Python runs inside a virtual environment, the module
# search path can point toward that environment's package locations.


print("\nPython executable:")
print(sys.executable)


# `sys.executable` tells us which Python interpreter is currently
# executing the program.
#
# This is an excellent debugging tool when multiple Python installations
# exist on the same machine.


# =============================================================================
# 13. PYTHON PREFIX
# =============================================================================

# Python exposes information about the installation through attributes
# such as:
#
#     sys.prefix
#     sys.base_prefix
#
# Let's inspect them.

print("\nPython prefix:")
print(sys.prefix)

print("\nPython base prefix:")
print(sys.base_prefix)


# In a normal Python installation, these values can represent the same
# installation.
#
# In a virtual environment, they can differ.
#
# This distinction can help identify whether the current interpreter is
# operating inside a virtual environment.


# =============================================================================
# 14. DETECTING A COMMON VIRTUAL-ENVIRONMENT CONDITION
# =============================================================================

is_virtual_environment = sys.prefix != sys.base_prefix

print("\nVirtual environment detected:")
print(is_virtual_environment)


# This is a useful practical diagnostic.
#
# It is not necessary to memorize the implementation details right now.
#
# The important idea is:
#
#     current environment
#             ↓
#     can affect module search locations


# =============================================================================
# 15. PYTHONPATH
# =============================================================================

# Python also supports an environment variable called:
#
#     PYTHONPATH
#
# It can be used to provide additional module search locations.
#
# For example, conceptually:
#
#     PYTHONPATH=C:\\my_python_modules
#
# can make that location available to Python's import environment.
#
# The exact way the variable is configured depends on the operating
# system and shell.


import os


python_path = os.environ.get("PYTHONPATH")

print("\nPYTHONPATH environment variable:")
print(repr(python_path))


# `None` means that the variable is not explicitly available through
# the current environment.
#
# If it exists, its value may contain one or more path entries.


# =============================================================================
# 16. PYTHONPATH VS sys.path
# =============================================================================

# These are related but not identical concepts.
#
# `PYTHONPATH`:
#
#     an environment variable that can provide additional import locations.
#
#
# `sys.path`:
#
#     the runtime list used by the current Python process.
#
#
# Python's startup process can incorporate environment configuration into
# the runtime import search path.
#
# Therefore:
#
#     PYTHONPATH
#         ↓
#     can influence
#         ↓
#     sys.path
#
# But `sys.path` can contain many entries that did not originate directly
# from PYTHONPATH.


# =============================================================================
# 17. PYTHONPATH ENTRIES
# =============================================================================

# If PYTHONPATH is defined, operating systems use a path separator to
# separate multiple locations.
#
# Python provides the correct separator through:
#
#     os.pathsep
#
# On Windows this is normally:
#
#     ;
#
# On Unix-like systems this is normally:
#
#     :
#
# We can inspect it:

print("\nPlatform path separator:")
print(repr(os.pathsep))


# This is useful when working with environment variables containing
# multiple directories.


# =============================================================================
# 18. STANDARD PATH SOURCES
# =============================================================================

# A simplified conceptual picture of Python's startup path is:
#
#     Python starts
#         ↓
#     execution context is established
#         ↓
#     relevant project/script location is considered
#         ↓
#     configured environment paths can be considered
#         ↓
#     standard Python locations are included
#         ↓
#     installed package locations are included
#         ↓
#     sys.path is available to the running process
#
# The actual initialization algorithm contains additional details and
# platform-specific behavior.


# =============================================================================
# 19. SEARCH PATH IS ENVIRONMENT-DEPENDENT
# =============================================================================

# The following can affect the resulting search path:
#
#     - operating system
#     - Python version
#     - Python installation
#     - virtual environment
#     - IDE
#     - command used to launch Python
#     - PYTHONPATH
#     - package installation
#     - execution mode
#
# Therefore, copying someone else's `sys.path` and expecting identical
# results is not reliable.


# =============================================================================
# 20. COMMAND-LINE EXECUTION
# =============================================================================

# If you execute:
#
#     python my_script.py
#
# Python establishes an execution environment associated with that
# command.
#
# The resulting module search path can therefore differ from what you
# see in:
#
#     python
#
# interactive mode,
#
# or:
#
#     python -m package.module
#
# or:
#
#     Jupyter Notebook
#
# or:
#
#     an IDE's run configuration.


# =============================================================================
# 21. `python -m` EXECUTION
# =============================================================================

# Python also supports:
#
#     python -m package.module
#
# This executes a module through Python's module system rather than
# treating the file purely as a standalone script path.
#
# This distinction becomes very important in package-based projects.
#
# We will explore the consequences more deeply when studying packages
# and import resolution.


# =============================================================================
# 22. PROJECT SOURCE DIRECTORIES
# =============================================================================

# Consider a project:
#
#     project/
#     │
#     ├── src/
#     │   └── data_pipeline/
#     │       ├── __init__.py
#     │       ├── ingestion.py
#     │       └── transformation.py
#     │
#     └── tests/
#
# The directory that Python needs to recognize as the beginning of the
# importable package structure matters.
#
# For example, conceptually:
#
#     src/
#         ↓
#     data_pipeline/
#
# Python needs the appropriate parent location available to the import
# system for:
#
#     import data_pipeline
#
# to work.


# =============================================================================
# 23. COMMON PROJECT IMPORT PROBLEM
# =============================================================================

# Suppose the project contains:
#
#     project/
#     │
#     ├── src/
#     │   └── myapp/
#     │       └── utility.py
#     │
#     └── tests/
#         └── test_utility.py
#
# A developer may run:
#
#     python tests/test_utility.py
#
# and then encounter:
#
#     ModuleNotFoundError
#
# even though:
#
#     utility.py
#
# clearly exists.
#
# Why?
#
# Because:
#
#     "The file exists"
#
# and:
#
#     "The module is discoverable by the import system"
#
# are two different things.


# =============================================================================
# 24. FILE EXISTENCE VS IMPORTABILITY
# =============================================================================

# This distinction is fundamental.
#
# A file can exist at:
#
#     C:\\somewhere\\helper.py
#
# but:
#
#     import helper
#
# may fail.
#
# The reason is that the relevant directory may not be available to
# Python's import system.
#
# Therefore:
#
#     EXISTS ON DISK
#
# does not automatically mean:
#
#     IMPORTABLE


# =============================================================================
# 25. DEMONSTRATING FILE EXISTENCE VS IMPORTABILITY
# =============================================================================

# We can demonstrate this with a temporary module.

import tempfile


temporary_directory = Path(tempfile.mkdtemp())

temporary_module_path = temporary_directory / "search_demo_module.py"

temporary_module_path.write_text(
    """
value = "Found through the module search path."
""".strip(),
    encoding="utf-8",
)


print("\nTemporary module exists:")
print(temporary_module_path.exists())


# The file exists.
#
# But its directory is not currently guaranteed to be in sys.path.


# =============================================================================
# 26. CHECK WHETHER PYTHON CAN CURRENTLY SEE THE DIRECTORY
# =============================================================================

temporary_directory_string = str(temporary_directory)

print("\nTemporary directory in sys.path:")
print(temporary_directory_string in sys.path)


# Expected:
#
#     False
#
# assuming the temporary directory was not already included.


# =============================================================================
# 27. MAKE THE MODULE SEARCHABLE
# =============================================================================

sys.path.insert(0, temporary_directory_string)


print("\nTemporary directory added to sys.path:")
print(temporary_directory_string in sys.path)


# Now the directory is available as a search location.


# =============================================================================
# 28. IMPORT THE TEMPORARY MODULE
# =============================================================================

import search_demo_module


print("\nImported temporary module value:")
print(search_demo_module.value)


# The important chain is:
#
#     search_demo_module.py
#             ↓
#     parent directory
#             ↓
#     parent directory added to sys.path
#             ↓
#     import search_demo_module
#             ↓
#     Python finds module
#             ↓
#     module is loaded


# =============================================================================
# 29. VERIFY THE ACTUAL MODULE LOCATION
# =============================================================================

print("\nActual imported module location:")
print(search_demo_module.__file__)


# This should point to the temporary file we created.


# =============================================================================
# 30. CLEAN UP THE SEARCH PATH
# =============================================================================

sys.path.remove(temporary_directory_string)


print("\nTemporary directory removed:")
print(temporary_directory_string in sys.path)


# This returns the runtime search path to approximately its previous
# state.


# =============================================================================
# 31. SEARCH PATH AND MODULE SHADOWING
# =============================================================================

# Consider:
#
#     project/
#     │
#     ├── json.py
#     └── main.py
#
# and:
#
#     main.py
#
# contains:
#
#     import json
#
# The developer may expect Python's standard-library `json`.
#
# However, if the project location is searched before the standard-library
# location, the local `json.py` can interfere with that expectation.
#
# This is called module shadowing.


# =============================================================================
# 32. AVOID SHADOWING IMPORTANT MODULE NAMES
# =============================================================================

# Avoid naming project files:
#
#     json.py
#     random.py
#     pathlib.py
#     typing.py
#     logging.py
#     csv.py
#     os.py
#     sys.py
#
# when you intend to import those standard-library modules.
#
# A safer naming convention is to use names that describe your actual
# application functionality.
#
# Examples:
#
#     csv_reader.py
#     data_validator.py
#     file_loader.py
#     pipeline_config.py


# =============================================================================
# 33. IMPORT DEBUGGING TECHNIQUE
# =============================================================================

# If you suspect that Python imported the wrong module, inspect:
#
#     module.__file__
#
# Example:

print("\nLocation of imported json module:")
print(json.__file__)


# This can immediately reveal whether Python loaded the expected module.


# =============================================================================
# 34. ANOTHER USEFUL DEBUGGING TECHNIQUE
# =============================================================================

# Inspect the complete runtime search path:

print("\nRuntime search path during this program:")

for index, path_entry in enumerate(sys.path):
    print(f"{index}: {path_entry!r}")


# If an import unexpectedly fails, this is one of the first things worth
# checking.


# =============================================================================
# 35. SEARCH PATH AND VIRTUAL ENVIRONMENTS
# =============================================================================

# In data engineering, you will frequently work with environments
# containing packages such as:
#
#     pandas
#     numpy
#     sqlalchemy
#     boto3
#     apache-airflow
#     pyspark
#
# Different projects may require different package versions.
#
# Virtual environments help isolate these dependencies.
#
# Therefore:
#
#     project A
#         ↓
#     virtual environment A
#         ↓
#     package locations A
#
#
#     project B
#         ↓
#     virtual environment B
#         ↓
#     package locations B
#
# The module search path of the active Python interpreter reflects the
# environment in which that interpreter is running.


# =============================================================================
# 36. WHY `sys.executable` MATTERS
# =============================================================================

# If:
#
#     import pandas
#
# works in one terminal but fails in another, inspect:
#
#     sys.executable
#
# in both environments.
#
# You may discover that they are using different Python interpreters.


print("\nCurrent interpreter:")
print(sys.executable)


# This is one of the most practical Python environment debugging checks.


# =============================================================================
# 37. PYTHON VERSION ALSO MATTERS
# =============================================================================

print("\nPython version:")
print(sys.version)


# Different Python installations can have different:
#
#     - standard-library locations
#     - package installations
#     - virtual environments
#     - search paths
#
# Therefore, when debugging import problems, identify the interpreter
# first.


# =============================================================================
# 38. SEARCH PATH IS CREATED BEFORE MOST USER CODE RUNS
# =============================================================================

# By the time your normal Python module code starts executing,
# Python has already established the runtime environment necessary for
# imports.
#
# This is why you can write:
#
#     import sys
#
# and immediately inspect:
#
#     sys.path
#
# The import machinery and interpreter startup process establish the
# relevant environment before your module's ordinary top-level code
# executes.


# =============================================================================
# 39. IMPORTANT DISTINCTION:
#    `sys.path` VS FILESYSTEM PATH
# =============================================================================

# `sys.path` is NOT:
#
#     "all directories on my computer."
#
# It is specifically a collection of locations relevant to Python's
# module import system.
#
# Your computer may contain:
#
#     C:\\Users\\...
#     C:\\Program Files\\...
#     D:\\Projects\\...
#     ...
#
# but Python does not automatically search every directory on every
# drive when you write:
#
#     import something
#
# That would be wildly inefficient and unpredictable.


# =============================================================================
# 40. SIMPLIFIED SEARCH MODEL
# =============================================================================

# For now, use this model:
#
#     import module_name
#             ↓
#     Python consults import machinery
#             ↓
#     relevant search locations are considered
#             ↓
#     sys.path provides important locations
#             ↓
#     Python searches according to its resolution rules
#             ↓
#     matching module/package is found
#             ↓
#     module is loaded
#
#
# Later, `04_import_resolution.py` will refine this model by introducing
# finders, loaders, module specifications, and other import-system
# components.


# =============================================================================
# 41. COMMON MISCONCEPTIONS
# =============================================================================

# MISCONCEPTION 1:
#
#     "Python searches my entire computer for a module."
#
# Correction:
#
#     Python searches locations available through its import system.
#
#
# MISCONCEPTION 2:
#
#     "If a .py file exists, import must work."
#
# Correction:
#
#     The file must be discoverable according to the import system.
#
#
# MISCONCEPTION 3:
#
#     "The current working directory is always the module search path."
#
# Correction:
#
#     The search path contains multiple locations and depends on the
#     execution environment.
#
#
# MISCONCEPTION 4:
#
#     "PYTHONPATH and sys.path are exactly the same thing."
#
# Correction:
#
#     PYTHONPATH is an environment variable that can influence the
#     runtime search path. `sys.path` is the actual runtime list.
#
#
# MISCONCEPTION 5:
#
#     "Virtual environments only change installed packages."
#
# Correction:
#
#     The interpreter and package environment influence where Python
#     searches for modules.
#
#
# MISCONCEPTION 6:
#
#     "Changing sys.path changes Python permanently."
#
# Correction:
#
#     Normal runtime changes affect the current Python process.
#
#
# MISCONCEPTION 7:
#
#     "The first path in sys.path is always the same."
#
# Correction:
#
#     It can depend on how Python was launched.


# =============================================================================
# 42. KEY TAKEAWAYS
# =============================================================================

# 1. The module search path is the collection of locations Python can use
#    when resolving imports.
#
# 2. `sys.path` is the primary runtime representation we inspect when
#    studying that search path.
#
# 3. `sys.path` is ordered.
#
# 4. Search order can influence which module is imported.
#
# 5. The script directory and current working directory are different
#    concepts.
#
# 6. Python's standard library has its own installation locations.
#
# 7. Third-party packages are commonly installed under site-packages.
#
# 8. Virtual environments provide isolated package environments and can
#    therefore affect the module search path.
#
# 9. `PYTHONPATH` can provide additional import locations.
#
# 10. `sys.executable` tells you which Python interpreter is running.
#
# 11. A file existing on disk does not automatically make it importable.
#
# 12. The parent directory containing a module generally needs to be
#     discoverable by the import system.
#
# 13. `module.__file__` is extremely useful for finding out which actual
#     file Python imported.
#
# 14. Duplicate module names can cause shadowing problems.
#
# 15. Manually modifying `sys.path` is useful for understanding the
#     mechanism, but proper project/package structure is preferable in
#     real applications.
#
# 16. `sys.path` is only one part of Python's complete import machinery.
#
# 17. The next topic is:
#
#         03_standard_library_vs_custom_modules.py
#
#     where we will distinguish Python's built-in/standard-library
#     modules from modules created by developers.