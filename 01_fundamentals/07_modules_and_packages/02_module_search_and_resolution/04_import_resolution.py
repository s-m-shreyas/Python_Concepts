# type: ignore
"""
04_import_resolution.py

Topic:
    Import resolution

Purpose:
    Understand how Python resolves an import statement and how the import
    system decides what module or package should be loaded.

Concepts covered:
    1. What import resolution means
    2. Import statement vs import resolution
    3. Module search path
    4. Module specifications
    5. Finders
    6. Loaders
    7. sys.modules
    8. Module caching
    9. Importing the same module multiple times
    10. Module identity
    11. ModuleNotFoundError
    12. Module shadowing
    13. Import resolution debugging
    14. A simplified import-resolution model
    15. Practical import-system inspection

Previous topics:
    01_sys_path.py
    02_module_search_path.py
    03_standard_library_vs_custom_modules.py

Next section:
    03_packages
"""


# =============================================================================
# 1. WHAT IS IMPORT RESOLUTION?
# =============================================================================

# When Python encounters:
#
#     import module_name
#
# Python needs to answer several questions:
#
#     1. Has this module already been loaded?
#     2. Where can the module be found?
#     3. Which import mechanism can handle it?
#     4. How should it be loaded?
#     5. What module object should be returned?
#
# The process of answering these questions is broadly called:
#
#     IMPORT RESOLUTION
#
#
# A simplified mental model is:
#
#     import module
#           ↓
#     check module cache
#           ↓
#     locate module
#           ↓
#     determine how it should be loaded
#           ↓
#     load module
#           ↓
#     create/reuse module object
#           ↓
#     make it available to the importing code


# =============================================================================
# 2. IMPORT IS MORE THAN "FIND A FILE"
# =============================================================================

# A common beginner model is:
#
#     import module
#         ↓
#     find module.py
#         ↓
#     execute module.py
#
# This is useful as an initial approximation, but it is incomplete.
#
# Python's import system supports:
#
#     - Python source modules
#     - packages
#     - built-in modules
#     - extension modules
#     - modules supplied by custom import mechanisms
#
# Therefore, import resolution is more general than simply searching for
# a `.py` file.


# =============================================================================
# 3. THE IMPORT SYSTEM
# =============================================================================

# Python provides an import system responsible for handling imports.
#
# Important components include:
#
#     sys.modules
#         ↓
#     module cache
#
#     sys.meta_path
#         ↓
#     meta path finders
#
#     module specification
#         ↓
#     describes how the module can be loaded
#
#     loader
#         ↓
#     responsible for loading module contents
#
#
# We will inspect these components directly.


import sys


# =============================================================================
# 4. sys.modules
# =============================================================================

# `sys.modules` is a dictionary containing modules that have already been
# loaded by the current Python interpreter.
#
# The keys are module names.
#
# The values are module objects.

print("Type of sys.modules:")
print(type(sys.modules))


# Expected:
#
#     <class 'dict'>


# =============================================================================
# 5. INSPECT A LOADED MODULE
# =============================================================================

# This file itself is being executed as a module.
#
# Therefore, depending on how it is executed, its module name can be
# available in sys.modules.

print("\nCurrent module name:")
print(__name__)

print("\nCurrent module is cached:")
print(__name__ in sys.modules)


# The important concept is:
#
#     imported modules
#           ↓
#     are represented in
#           ↓
#     sys.modules


# =============================================================================
# 6. IMPORT A STANDARD-LIBRARY MODULE
# =============================================================================

import json


print("\njson in sys.modules:")
print("json" in sys.modules)


# Once `json` has been imported, its module name is normally present in:
#
#     sys.modules
#
# This allows Python to reuse the already-loaded module.


# =============================================================================
# 7. MODULE CACHING
# =============================================================================

# Suppose we write:
#
#     import json
#
# and later:
#
#     import json
#
# Python does not normally load and execute the module from scratch every
# time.
#
# Instead, Python can reuse the module object already stored in:
#
#     sys.modules
#
#
# Conceptually:
#
#     first import
#         ↓
#     locate module
#         ↓
#     load module
#         ↓
#     store module in sys.modules
#
#
#     second import
#         ↓
#     check sys.modules
#         ↓
#     reuse existing module


# =============================================================================
# 8. DEMONSTRATE MODULE REUSE
# =============================================================================

import json as json_again


print("\njson object identity:")
print(json is json_again)


# Expected:
#
#     True
#
# Both references point to the same module object.


# =============================================================================
# 9. MODULE IDENTITY
# =============================================================================

print("\njson module id:")
print(id(json))

print("\njson_again module id:")
print(id(json_again))


# The values should be the same because both names refer to the same
# module object.


# =============================================================================
# 10. WHY MODULE CACHING EXISTS
# =============================================================================

# Module caching provides several benefits.
#
# First:
#
#     performance
#
# Python does not need to repeatedly locate and execute the same module.
#
#
# Second:
#
#     consistency
#
# Multiple parts of a program normally work with the same module object.
#
#
# Third:
#
#     state preservation
#
# If a module contains module-level state, importing it again normally
# reuses the existing module object rather than creating a fresh one.


# =============================================================================
# 11. MODULE SPECIFICATION
# =============================================================================

# Python can describe a discovered module through a module specification.
#
# A module specification is represented by:
#
#     ModuleSpec
#
# and is accessible through:
#
#     module.__spec__
#
# Let's inspect it.

print("\njson module specification:")
print(json.__spec__)


# A module specification contains information that helps Python understand
# how the module can be loaded.


# =============================================================================
# 12. IMPORTANT MODULE SPEC ATTRIBUTES
# =============================================================================

print("\njson module spec name:")
print(json.__spec__.name)

print("\njson module spec loader:")
print(json.__spec__.loader)

print("\njson module spec origin:")
print(json.__spec__.origin)


# The exact values depend on the Python installation.


# =============================================================================
# 13. WHAT IS A FINDER?
# =============================================================================

# A finder is responsible for determining whether it can locate a module.
#
# Python's import machinery consults registered finders when it needs to
# locate a module.
#
# A finder does not necessarily load the module itself.
#
# Conceptually:
#
#     finder
#         ↓
#     "I found information about this module."
#         ↓
#     module specification
#         ↓
#     loader
#         ↓
#     module loading


# =============================================================================
# 14. sys.meta_path
# =============================================================================

# Python exposes a collection of meta path finders through:
#
#     sys.meta_path

print("\nMeta path finders:")

for index, finder in enumerate(sys.meta_path):
    print(f"{index}: {finder!r}")


# These objects participate in the process of locating modules.


# =============================================================================
# 15. WHY sys.meta_path MATTERS
# =============================================================================

# When Python needs to resolve an import, it can consult the finders
# registered in sys.meta_path.
#
# Conceptually:
#
#     import module_name
#           ↓
#     import machinery
#           ↓
#     sys.meta_path
#           ↓
#     finder 1
#           ↓
#     finder 2
#           ↓
#     finder 3
#           ↓
#     module found
#
#
# The actual import system contains additional details, but this model
# is sufficient for understanding the architecture at this stage.


# =============================================================================
# 16. FIND A MODULE SPECIFICATION MANUALLY
# =============================================================================

# Python exposes a useful function through importlib:
#
#     importlib.util.find_spec()
#
# It allows us to ask:
#
#     "What specification would Python use for this module?"

import importlib.util


json_spec = importlib.util.find_spec("json")


print("\nSpecification found for json:")
print(json_spec)


# This is useful for learning and debugging the import system.


# =============================================================================
# 17. INSPECT THE SPECIFICATION
# =============================================================================

if json_spec is not None:
    print("\njson spec name:")
    print(json_spec.name)

    print("\njson spec origin:")
    print(json_spec.origin)

    print("\njson spec loader:")
    print(json_spec.loader)


# The conditional check keeps the example safe for static type checkers
# and makes it clear that `find_spec()` can return None.


# =============================================================================
# 18. FINDER VS LOADER
# =============================================================================

# These concepts are easy to mix up.
#
#
# FINDER
# ------
#
# Responsible for locating or identifying a module.
#
#
# LOADER
# ------
#
# Responsible for loading the module once the import system has determined
# how it should be loaded.
#
#
# Simplified:
#
#     Finder
#        ↓
#     "I know where/how this module can be loaded."
#        ↓
#     ModuleSpec
#        ↓
#     Loader
#        ↓
#     module object


# =============================================================================
# 19. A MODULE SPEC IS NOT THE MODULE
# =============================================================================

# Another important distinction:
#
#     ModuleSpec
#
# describes how a module can be loaded.
#
# It is not the actual module object.
#
# Compare:
#
#     json.__spec__
#
# with:
#
#     json
#
# The first describes the module's loading information.
#
# The second is the actual module object.


# =============================================================================
# 20. MODULE LOADER
# =============================================================================

if json_spec is not None:
    print("\nLoader type:")
    print(type(json_spec.loader))


# The exact loader depends on the module and environment.


# =============================================================================
# 21. CUSTOM MODULE RESOLUTION
# =============================================================================

# Let's create a custom module dynamically so that we can observe the
# resolution process without requiring an extra file.

import pathlib
import tempfile


temporary_directory = pathlib.Path(tempfile.mkdtemp())

custom_module_path = temporary_directory / "resolution_demo.py"

custom_module_path.write_text(
    """
VALUE = 42


def get_message() -> str:
    return "Custom module successfully resolved."
""".strip(),
    encoding="utf-8",
)


# Add its parent directory to the runtime search path.

temporary_directory_string = str(temporary_directory)

sys.path.insert(0, temporary_directory_string)


# =============================================================================
# 22. FIND THE CUSTOM MODULE SPEC
# =============================================================================

custom_spec = importlib.util.find_spec("resolution_demo")


print("\nCustom module specification:")
print(custom_spec)


# If the module is discoverable, the specification should contain
# information about its location and loader.


# =============================================================================
# 23. INSPECT CUSTOM MODULE SPEC
# =============================================================================

if custom_spec is not None:
    print("\nCustom module spec name:")
    print(custom_spec.name)

    print("\nCustom module spec origin:")
    print(custom_spec.origin)

    print("\nCustom module spec loader:")
    print(custom_spec.loader)


# Notice how the specification identifies the custom module's source.


# =============================================================================
# 24. IMPORT THE CUSTOM MODULE
# =============================================================================

import resolution_demo


print("\nCustom module value:")
print(resolution_demo.VALUE)

print("\nCustom module message:")
print(resolution_demo.get_message())


# =============================================================================
# 25. VERIFY THE MODULE CACHE
# =============================================================================

print("\nCustom module in sys.modules:")
print("resolution_demo" in sys.modules)


# After importing:
#
#     resolution_demo
#
# should normally be present in:
#
#     sys.modules


# =============================================================================
# 26. COMPARE THE MODULE OBJECT WITH sys.modules
# =============================================================================

print("\nModule object identity:")
print(resolution_demo is sys.modules["resolution_demo"])


# Expected:
#
#     True
#
# This demonstrates that the object exposed through the import is the
# same object stored in the module cache.


# =============================================================================
# 27. IMPORT THE SAME CUSTOM MODULE AGAIN
# =============================================================================

import resolution_demo as resolution_demo_again


print("\nRepeated import reuses module:")
print(resolution_demo is resolution_demo_again)


# Expected:
#
#     True


# =============================================================================
# 28. WHAT HAPPENS DURING A SECOND IMPORT?
# =============================================================================

# Conceptually:
#
#     import resolution_demo
#             ↓
#     Is "resolution_demo" in sys.modules?
#             ↓
#           YES
#             ↓
#     Reuse existing module object
#
#
# Therefore, Python does not normally repeat the complete discovery and
# execution process.


# =============================================================================
# 29. MODULE EXECUTION VS MODULE IMPORT
# =============================================================================

# A common misunderstanding is:
#
#     "Every import executes the module."
#
# More accurately:
#
#     The module's top-level code normally executes when the module is
#     initially loaded.
#
# Subsequent imports normally reuse the cached module object.
#
# This distinction becomes extremely important when a module contains
# side effects at module level.


# =============================================================================
# 30. DEMONSTRATE MODULE INITIALIZATION
# =============================================================================

initialization_module_path = temporary_directory / "initialization_demo.py"

initialization_module_path.write_text(
    """
print("initialization_demo module executed")

VALUE = 100
""".strip(),
    encoding="utf-8",
)


# First import:

import initialization_demo


print("\nInitialization module value:")
print(initialization_demo.VALUE)


# Import again:

import initialization_demo as initialization_demo_again


print("\nSecond reference value:")
print(initialization_demo_again.VALUE)


# You should observe that the module-level print happens during the
# initial loading rather than once for every import statement.


# =============================================================================
# 31. `importlib.reload()`
# =============================================================================

# Python also provides:
#
#     importlib.reload()
#
# which explicitly asks Python to execute the module's code again.
#
# This is different from simply writing another:
#
#     import module
#
#
# We will demonstrate it carefully.

import importlib


importlib.reload(initialization_demo)


# You should see the module's initialization message again.


# IMPORTANT:
#
#     repeated import
#
# and:
#
#     importlib.reload()
#
# are not equivalent.


# =============================================================================
# 32. MODULE NOT FOUND
# =============================================================================

# If Python cannot resolve an import, it can raise:
#
#     ModuleNotFoundError
#
# Example:
#
#     import module_that_does_not_exist
#
# would fail because Python cannot find a matching module or package.


# We will demonstrate this safely.

try:
    import module_that_does_not_exist
except ModuleNotFoundError as error:
    print("\nModuleNotFoundError caught:")
    print(error)


# This is useful because it lets us observe the exception without
# terminating the entire teaching program.


# =============================================================================
# 33. WHAT DOES MODULE NOT FOUND ACTUALLY MEAN?
# =============================================================================

# It does NOT necessarily mean:
#
#     "The file does not exist anywhere on the computer."
#
# It means that Python could not resolve the requested module through
# its import system in the current execution environment.
#
# A file can exist somewhere on disk but still be unavailable to the
# current import system.


# =============================================================================
# 34. MODULE SHADOWING
# =============================================================================

# Module shadowing occurs when one module has the same name as another
# module that Python might otherwise import.
#
# Example:
#
#     project/
#     ├── json.py
#     └── main.py
#
#
# `main.py`:
#
#     import json
#
#
# Depending on the import environment and resolution rules, the local
# module can interfere with the expected standard-library module.
#
# This is one reason developers should avoid naming files after common
# standard-library or third-party modules.


# =============================================================================
# 35. INSPECT WHERE A MODULE CAME FROM
# =============================================================================

print("\njson module location:")
print(json.__file__)

print("\nresolution_demo location:")
print(resolution_demo.__file__)


# If an import behaves strangely, checking `__file__` is often one of
# the quickest debugging techniques.


# =============================================================================
# 36. IMPORT RESOLUTION VS IMPORT EXECUTION
# =============================================================================

# These are related but distinct ideas.
#
#
# IMPORT RESOLUTION
# -----------------
#
# Determines which module/package should satisfy an import request.
#
#
# MODULE LOADING
# --------------
#
# Loads the selected module.
#
#
# MODULE EXECUTION
# ----------------
#
# Executes the module's code when it is initially loaded.
#
#
# MODULE CACHING
# --------------
#
# Stores the loaded module in sys.modules for reuse.


# =============================================================================
# 37. COMPLETE SIMPLIFIED IMPORT FLOW
# =============================================================================

# When Python encounters:
#
#     import example
#
# use this mental model:
#
#
#     import example
#             ↓
#     check sys.modules
#             ↓
#     already loaded?
#          /       \
#        YES        NO
#        ↓           ↓
#     reuse      find module
#                   ↓
#              create spec
#                   ↓
#                loader
#                   ↓
#             create/load module
#                   ↓
#             execute module
#                   ↓
#          store in sys.modules
#                   ↓
#              return module
#
#
# This is a simplified conceptual model, not the complete CPython
# implementation.


# =============================================================================
# 38. WHY sys.modules COMES FIRST
# =============================================================================

# Module caching is important enough to remember:
#
#     sys.modules
#
# is the first major place to think about when studying repeated imports.
#
# If a module is already loaded, Python can reuse the existing module
# object rather than performing the entire loading process again.


# =============================================================================
# 39. IMPORTLIB
# =============================================================================

# Python exposes parts of its import machinery through:
#
#     importlib
#
# We already used:
#
#     importlib.util.find_spec()
#
# and:
#
#     importlib.reload()
#
# `importlib` is extremely useful when learning how Python's import
# machinery works.


# =============================================================================
# 40. PRACTICAL DEBUGGING CHECKLIST
# =============================================================================

# If:
#
#     import my_module
#
# fails unexpectedly, check:
#
#     1. Does the module actually exist?
#
#     2. Is the module's parent directory available to Python?
#
#     3. What does sys.path contain?
#
#     4. Which Python interpreter is running?
#
#     5. Is a virtual environment active?
#
#     6. Is another module shadowing the expected module?
#
#     7. Does importlib.util.find_spec() find the module?
#
#     8. Is the module already present in sys.modules?
#
# These checks solve a surprisingly large number of import problems.


# =============================================================================
# 41. INSPECT THE CURRENT ENVIRONMENT
# =============================================================================

print("\n--- Import Debugging Information ---")

print("\nPython executable:")
print(sys.executable)

print("\nCurrent working directory:")
print(pathlib.Path.cwd())

print("\nNumber of entries in sys.path:")
print(len(sys.path))

print("\nNumber of loaded modules:")
print(len(sys.modules))


# These values give a quick snapshot of the import environment.


# =============================================================================
# 42. FIND SPEC WITHOUT IMPORTING THE MODULE
# =============================================================================

# One useful distinction:
#
#     importlib.util.find_spec()
#
# can provide information about how a module could be found.
#
# It is therefore useful when investigating import behavior.
#
# For example:

pathlib_spec = importlib.util.find_spec("pathlib")

print("\nPathlib specification:")
print(pathlib_spec)


# This gives us information about the module without writing:
#
#     import pathlib
#
# in this particular statement.


# =============================================================================
# 43. IMPORTANT CAVEAT ABOUT find_spec()
# =============================================================================

# `find_spec()` is a diagnostic/inspection tool.
#
# It should not be treated as a replacement for ordinary imports.
#
# Normal application code should generally use:
#
#     import module
#
# rather than manually implementing module discovery.
#
# We are using these tools here because the purpose of this file is to
# understand Python's import architecture.


# =============================================================================
# 44. WHY THIS MATTERS FOR DATA ENGINEERING
# =============================================================================

# In data engineering projects, you will frequently have structures such
# as:
#
#     project/
#     │
#     ├── main.py
#     ├── config.py
#     ├── ingestion/
#     │   ├── csv_loader.py
#     │   └── s3_loader.py
#     ├── transformation/
#     │   └── clean_data.py
#     └── database/
#         └── oracle.py
#
#
# Imports create relationships between these components.
#
# For example:
#
#     main.py
#         ↓
#     s3_loader.py
#         ↓
#     boto3
#
#     main.py
#         ↓
#     clean_data.py
#         ↓
#     pandas
#
#     main.py
#         ↓
#     oracle.py
#         ↓
#     sqlalchemy
#
#
# Understanding import resolution helps you understand why these
# relationships work — and why they sometimes break.


# =============================================================================
# 45. KEY TAKEAWAYS
# =============================================================================

# 1. Import resolution is the process Python uses to satisfy an import.
#
# 2. Import resolution is more than simply searching for `.py` files.
#
# 3. Python supports several types of importable modules.
#
# 4. `sys.modules` stores modules already loaded by the interpreter.
#
# 5. Repeated imports normally reuse the cached module object.
#
# 6. `module.__spec__` contains information about how the module can be
#    loaded.
#
# 7. Finders participate in locating modules.
#
# 8. Loaders participate in loading modules.
#
# 9. `sys.meta_path` contains important finder objects.
#
# 10. `importlib.util.find_spec()` can be used to inspect module
#     resolution information.
#
# 11. `module.__file__` can reveal where an imported module came from.
#
# 12. `ModuleNotFoundError` means Python could not resolve the requested
#     module in the current import environment.
#
# 13. A file existing somewhere on disk does not automatically make it
#     importable.
#
# 14. Module shadowing can cause unexpected imports.
#
# 15. `import` and `importlib.reload()` have different behavior.
#
# 16. A simplified import architecture is:
#
#         import request
#              ↓
#         sys.modules
#              ↓
#         finders
#              ↓
#         ModuleSpec
#              ↓
#         loader
#              ↓
#         module
#              ↓
#         sys.modules
#
#
# NEXT:
#
#     03_packages/
#
#     The next stage is to move from individual modules to packages and
#     understand how Python organizes multiple modules into a larger
#     application structure.