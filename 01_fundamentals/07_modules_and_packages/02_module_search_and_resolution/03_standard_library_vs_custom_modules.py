# type: ignore
"""
03_standard_library_vs_custom_modules.py

Topic:
    Standard library modules vs custom modules

Purpose:
    Understand the difference between modules provided by Python itself
    and modules created by the developer.

Concepts covered:
    1. What a standard-library module is
    2. What a custom module is
    3. Standard-library module examples
    4. Creating and importing a custom module
    5. Module location
    6. `module.__file__`
    7. Standard library vs third-party vs custom modules
    8. Importing from different module sources
    9. Why the distinction matters
    10. Practical debugging

Important:
    This file focuses on the conceptual distinction between different
    sources of Python modules.

    It does NOT deeply cover:
        - third-party package management
        - pip
        - virtual environments
        - individual libraries such as pandas or NumPy

    Those topics belong elsewhere in the repository.

Previous topic:
    02_module_search_and_resolution/02_module_search_path.py

Next topic:
    02_module_search_and_resolution/04_import_resolution.py
"""


# =============================================================================
# 1. WHAT IS A MODULE?
# =============================================================================

# A module is a Python file that can be imported and used by another
# Python program.
#
# Example:
#
#     calculator.py
#
# could contain:
#
#     def add(a, b):
#         return a + b
#
# Another Python file could then use:
#
#     import calculator
#
#     calculator.add(10, 20)
#
# Python modules can come from different sources.


# =============================================================================
# 2. THREE IMPORTANT SOURCES OF PYTHON MODULES
# =============================================================================

# A practical classification is:
#
#     1. Standard-library modules
#     2. Third-party modules
#     3. Custom modules
#
#
# STANDARD LIBRARY
# ----------------
#
# Provided as part of Python's standard distribution.
#
# Examples:
#
#     math
#     json
#     pathlib
#     datetime
#     re
#     os
#     sys
#
#
# THIRD-PARTY
# -----------
#
# Developed outside Python's standard library and installed separately.
#
# Examples:
#
#     pandas
#     numpy
#     requests
#     boto3
#     SQLAlchemy
#
#
# CUSTOM MODULES
# --------------
#
# Modules created by you or your organization.
#
# Examples:
#
#     data_validator.py
#     file_loader.py
#     database_utils.py
#     transformation.py


# =============================================================================
# 3. STANDARD-LIBRARY MODULES
# =============================================================================

# Python ships with a large standard library.
#
# This means that many useful modules are available without installing
# an external package.

import math
import json
import pathlib


print("Standard-library modules:")
print(math)
print(json)
print(pathlib)


# These modules are not custom files created inside this project.
#
# They are supplied by Python's standard library.


# =============================================================================
# 4. STANDARD LIBRARY MODULE LOCATION
# =============================================================================

# We can inspect where a module comes from using:
#
#     module.__file__
#
# Example:

print("\nStandard-library module locations:")

print(f"math:     {math.__file__}")
print(f"json:     {json.__file__}")
print(f"pathlib:  {pathlib.__file__}")


# The exact paths depend on:
#
#     - operating system
#     - Python installation
#     - Python version
#     - environment


# =============================================================================
# 5. STANDARD LIBRARY DOES NOT MEAN "BUILT-IN"
# =============================================================================

# This distinction is important.
#
# Python developers often casually use the terms:
#
#     built-in
#
# and:
#
#     standard library
#
# as though they mean the same thing.
#
# They do not.
#
#
# BUILT-IN
# --------
#
# Some functionality is directly available from the Python interpreter.
#
# Examples include:
#
#     print()
#     len()
#     type()
#     int()
#     str()
#
#
# STANDARD LIBRARY
# ----------------
#
# Many features are provided through importable modules.
#
# Examples:
#
#     import math
#     import json
#     import pathlib
#
# Therefore:
#
#     built-in functionality
#
# and:
#
#     standard-library modules
#
# are related concepts but are not identical.


# =============================================================================
# 6. THIRD-PARTY MODULES
# =============================================================================

# Third-party modules are developed outside Python's standard library.
#
# They are normally installed separately.
#
# Examples particularly relevant to data engineering include:
#
#     pandas
#     numpy
#     boto3
#     sqlalchemy
#
# Example:
#
#     import pandas
#
# The exact availability depends on the current Python environment.
#
# We will NOT import those packages in this teaching file because this
# repository should remain runnable without requiring external packages.


# =============================================================================
# 7. CUSTOM MODULES
# =============================================================================

# A custom module is simply a Python module created by the developer.
#
# For example:
#
#     calculator.py
#
# containing:
#
#     def add(first, second):
#         return first + second
#
# can be imported by another Python file.
#
# The important idea is:
#
#     module
#         ↓
#     does not have to come from Python
#         ↓
#     it can be created by you


# =============================================================================
# 8. CREATE A CUSTOM MODULE DYNAMICALLY
# =============================================================================

# To keep this example completely copy-paste runnable, we will create
# a temporary custom module during execution.
#
# This avoids requiring a second manually-created file.

import tempfile


temporary_directory = pathlib.Path(tempfile.mkdtemp())

custom_module_path = temporary_directory / "custom_math.py"

custom_module_path.write_text(
    """
PI_APPROXIMATION = 3.14159


def add(first: int, second: int) -> int:
    return first + second


def multiply(first: int, second: int) -> int:
    return first * second
""".strip(),
    encoding="utf-8",
)


print("\nCustom module created at:")
print(custom_module_path)


# =============================================================================
# 9. MAKE THE CUSTOM MODULE IMPORTABLE
# =============================================================================

# The module is physically present on disk.
#
# But Python needs to be able to discover it through the module search
# path.
#
# The directory containing the module must therefore be available to
# the import system.

import sys


temporary_directory_string = str(temporary_directory)

sys.path.insert(0, temporary_directory_string)


# The module can now be imported.

import custom_math


# =============================================================================
# 10. USE THE CUSTOM MODULE
# =============================================================================

print("\nCustom module results:")

print(custom_math.add(10, 20))
print(custom_math.multiply(5, 6))
print(custom_math.PI_APPROXIMATION)


# Notice that the syntax is exactly the same style used for standard
# library modules:
#
#     import math
#
# versus:
#
#     import custom_math
#
# The source of the module is different, but the basic import syntax
# remains the same.


# =============================================================================
# 11. INSPECT THE CUSTOM MODULE LOCATION
# =============================================================================

print("\nCustom module location:")
print(custom_math.__file__)


# This demonstrates an important debugging technique:
#
#     module.__file__
#
# tells us where the imported module came from, when the module provides
# that attribute.


# =============================================================================
# 12. COMPARE THE MODULE SOURCES
# =============================================================================

print("\nModule source comparison:")

print(f"Standard library : {json.__file__}")
print(f"Custom module    : {custom_math.__file__}")


# The two modules are both importable Python modules.
#
# Their difference is their source/location and how they are provided.


# =============================================================================
# 13. STANDARD LIBRARY MODULE
# =============================================================================

# Example:
#
#     import json
#
# Python provides `json` as part of its standard library.
#
# You normally do not need to install it separately.


# =============================================================================
# 14. THIRD-PARTY MODULE
# =============================================================================

# Example:
#
#     import pandas
#
# pandas is NOT part of Python's standard library.
#
# It must normally be installed separately into the environment.
#
# Once installed, however, importing it follows the same general pattern:
#
#     import pandas


# =============================================================================
# 15. CUSTOM MODULE
# =============================================================================

# Example:
#
#     import custom_math
#
# This module was created by us.
#
# Python does not care whether a module was written by:
#
#     - Python developers
#     - an external open-source project
#     - your organization
#     - you personally
#
# The import system deals with locating and loading the module.


# =============================================================================
# 16. THE THREE-WAY COMPARISON
# =============================================================================

# STANDARD LIBRARY
#
#     import json
#
#     Provided with Python.
#
#
# THIRD PARTY
#
#     import pandas
#
#     Installed separately.
#
#
# CUSTOM
#
#     import custom_math
#
#     Created by the developer.
#
#
# The import syntax itself does not tell you which category a module
# belongs to.


# =============================================================================
# 17. WHY THIS DISTINCTION MATTERS
# =============================================================================

# Imagine a data-engineering project:
#
#     data_pipeline/
#     │
#     ├── main.py
#     ├── config.py
#     ├── file_loader.py
#     ├── validator.py
#     └── transformer.py
#
#
# You might have:
#
#     import json
#     import pathlib
#
# These are standard-library modules.
#
#
# You might also have:
#
#     import pandas
#
# This is a third-party package.
#
#
# And:
#
#     import validator
#     import transformer
#
# These are custom project modules.


# =============================================================================
# 18. A REALISTIC DATA-ENGINEERING EXAMPLE
# =============================================================================

# Imagine:
#
#     pipeline/
#     │
#     ├── main.py
#     ├── config.py
#     ├── file_loader.py
#     └── transformer.py
#
#
# `main.py` might conceptually contain:
#
#     import json
#     import pandas
#
#     import config
#     import file_loader
#     import transformer
#
#
# The categories are:
#
#     json
#         ↓
#     standard library
#
#     pandas
#         ↓
#     third party
#
#     config
#         ↓
#     custom module
#
#     file_loader
#         ↓
#     custom module
#
#     transformer
#         ↓
#     custom module


# =============================================================================
# 19. STANDARD LIBRARY IS PART OF THE PYTHON ECOSYSTEM
# =============================================================================

# A Python installation gives you access to a large collection of
# functionality without requiring external packages.
#
# Examples:
#
#     math
#     statistics
#     pathlib
#     json
#     csv
#     datetime
#     collections
#     itertools
#     functools
#     re
#
# This is one reason Python can be productive even before installing
# third-party packages.


# =============================================================================
# 20. THIRD-PARTY PACKAGES EXTEND PYTHON
# =============================================================================

# Third-party packages extend Python with additional functionality.
#
# Data engineering is a great example.
#
# Python's standard library provides:
#
#     csv
#     json
#     pathlib
#     sqlite3
#
# while third-party packages provide tools such as:
#
#     pandas
#     SQLAlchemy
#     boto3
#     PySpark
#
# This creates a layered ecosystem:
#
#     Python
#       ↓
#     standard library
#       ↓
#     third-party ecosystem
#       ↓
#     organization/project modules


# =============================================================================
# 21. CUSTOM MODULES CREATE PROJECT STRUCTURE
# =============================================================================

# As applications grow, putting everything inside one file becomes
# difficult to maintain.
#
# Custom modules allow us to separate responsibilities.
#
# Example:
#
#     database.py
#         ↓
#     database-related functionality
#
#     validation.py
#         ↓
#     validation-related functionality
#
#     transformation.py
#         ↓
#     transformation-related functionality
#
#     main.py
#         ↓
#     orchestration
#
# This is the beginning of modular software design.


# =============================================================================
# 22. MODULE OWNERSHIP DOES NOT CHANGE IMPORT SYNTAX
# =============================================================================

# Consider:
#
#     import json
#     import pandas
#     import transformation
#
# All three use:
#
#     import <module>
#
# But they have different origins.
#
# Therefore:
#
#     import syntax
#
# and:
#
#     module source
#
# are separate concepts.


# =============================================================================
# 23. MODULE LOCATION IS MORE USEFUL THAN MODULE NAME
# =============================================================================

# If you are unsure where Python imported something from, do not guess.
#
# Inspect it.

print("\nWhere did json come from?")
print(json.__file__)

print("\nWhere did custom_math come from?")
print(custom_math.__file__)


# This is often much faster than debugging by assumption.


# =============================================================================
# 24. MODULE NAME COLLISIONS
# =============================================================================

# Suppose you create:
#
#     json.py
#
# in your project.
#
# Then your code contains:
#
#     import json
#
# You may accidentally interfere with Python's expected `json` module.
#
# This is a module-name collision.
#
# The same problem can happen with third-party package names.
#
# For example, creating:
#
#     pandas.py
#
# can create confusing behavior if you later try:
#
#     import pandas


# =============================================================================
# 25. SAFE CUSTOM MODULE NAMING
# =============================================================================

# Prefer descriptive project-specific names.
#
# Better:
#
#     csv_loader.py
#     database_connection.py
#     data_validator.py
#     pipeline_config.py
#
# Avoid unnecessarily generic names that collide with popular modules:
#
#     json.py
#     random.py
#     logging.py
#     typing.py
#     pathlib.py
#     pandas.py
#
# Good naming becomes increasingly important as projects grow.


# =============================================================================
# 26. MODULES CAN IMPORT OTHER MODULES
# =============================================================================

# A custom module can itself import:
#
#     standard-library modules
#     third-party packages
#     other custom modules
#
#
# Example:
#
#     transformer.py
#         |
#         +---- import json
#         |
#         +---- import pandas
#         |
#         +---- import validator
#
#
# This is how larger Python applications are built from smaller
# components.


# =============================================================================
# 27. DEPENDENCY CHAIN
# =============================================================================

# Imagine:
#
#     main.py
#         ↓
#     transformer.py
#         ↓
#     validator.py
#
# and:
#
#     validator.py
#         ↓
#     json
#
#
# The resulting dependency relationship is:
#
#     main
#       ↓
#     transformer
#       ↓
#     validator
#       ↓
#     json
#
#
# This is why understanding imports is essential before studying
# larger software architecture.


# =============================================================================
# 28. MODULES VS PACKAGES
# =============================================================================

# A module is commonly represented by a Python file:
#
#     validator.py
#
#
# A package is a directory structure used to organize modules.
#
# For example:
#
#     validation/
#     ├── __init__.py
#     ├── email.py
#     └── schema.py
#
#
# We will study packages in the next major section:
#
#     03_packages
#
# For now, keep this simple distinction:
#
#     module
#         ≈ Python file
#
#     package
#         ≈ organized collection of modules


# =============================================================================
# 29. CLEAN UP
# =============================================================================

# Remove the temporary directory from sys.path after the demonstration.

if temporary_directory_string in sys.path:
    sys.path.remove(temporary_directory_string)


# =============================================================================
# 30. FINAL SUMMARY
# =============================================================================

# STANDARD LIBRARY
#
#     Provided with Python.
#
#     Examples:
#         math
#         json
#         pathlib
#         datetime
#
#
# THIRD PARTY
#
#     Installed separately.
#
#     Examples:
#         pandas
#         numpy
#         boto3
#         SQLAlchemy
#
#
# CUSTOM
#
#     Created by developers.
#
#     Examples:
#         config.py
#         validator.py
#         transformer.py
#
#
# IMPORTANT:
#
#     All three can participate in Python's import system.
#
#
# The key mental model:
#
#     Python module
#           |
#           +--------------------+
#           |                    |
#     standard library      external/custom
#                                |
#                       +--------+--------+
#                       |                 |
#                   third-party        custom
#
#
# And when debugging:
#
#     import module_name
#            ↓
#     module.__file__
#            ↓
#     inspect where it actually came from
#
#
# NEXT:
#
#     04_import_resolution.py
#
# That file will move from:
#
#     "Where can Python find modules?"
#
# to:
#
#     "How does Python actually resolve an import?"