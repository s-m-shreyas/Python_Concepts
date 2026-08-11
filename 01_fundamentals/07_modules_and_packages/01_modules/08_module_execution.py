# type: ignore
"""
08_module_execution.py

Topic:
    Module execution

Purpose:
    Understand what happens when Python executes a module, what code runs
    during module execution, what happens when a module is imported, and
    how the `__name__` attribute can distinguish direct execution from import.

Concepts covered:
    1. What module execution means
    2. A Python file is executable module code
    3. Top-level statements execute
    4. Execution happens from top to bottom
    5. Function definitions during module execution
    6. Class definitions during module execution
    7. Importing a module executes its top-level code
    8. Module execution vs function execution
    9. Direct execution
    10. Imported execution
    11. The `__name__` attribute during execution
    12. The `if __name__ == "__main__":` pattern
    13. Why the main guard matters
    14. Module initialization
    15. Re-importing and module caching
    16. Side effects caused by module-level code
    17. Practical project structure
    18. Common misconceptions

Important:
    - Basic module concepts are covered in:
          01_module_basics.py
    - Import syntax is covered in:
          02_import_statement.py
          03_import_as.py
          04_from_import.py
          05_import_multiple_objects.py
    - Module namespaces are covered in:
          06_module_namespace.py
    - Module attributes are covered in:
          07_module_attributes.py
    - The main guard is demonstrated here as part of module execution.
      A dedicated deeper treatment can be added later under
      special module attributes if required.

Note:
    This file is intentionally self-contained and copy-paste runnable.
    Some examples use temporary modules created at runtime so that the
    execution behavior can be demonstrated without requiring external
    project files.
"""


# =============================================================================
# 1. WHAT DOES "MODULE EXECUTION" MEAN?
# =============================================================================

# A Python file contains executable Python code.
#
# When Python executes that file, it processes the code and performs the
# operations represented by the statements.
#
# For example:

print("Module execution has started.")


# This print statement executes immediately when Python reaches it.
#
# This is different from a function body:
#
#     def greet():
#         print("Hello")
#
# Defining the function creates the function object, but the statements
# inside the function do not execute until the function is called.


# =============================================================================
# 2. MODULE CODE EXECUTES FROM TOP TO BOTTOM
# =============================================================================

print("\nFirst statement executed.")

first_value = 10

print("Second statement executed.")

second_value = 20

print("Third statement executed.")


# Python normally executes module-level statements in source-code order:
#
#     statement 1
#          ↓
#     statement 2
#          ↓
#     statement 3
#          ↓
#     statement 4
#
# This top-to-bottom behavior is important when one statement depends
# on something defined earlier in the module.


# =============================================================================
# 3. VARIABLES ARE CREATED DURING MODULE EXECUTION
# =============================================================================

# Consider:

number = 100


# The assignment executes while the module is executing.
#
# Therefore, after Python reaches this statement:
#
#     number
#
# refers to the integer object `100`.

print("\nNumber:")
print(number)


# Before Python executes the assignment, the name `number` does not yet
# exist in this module's namespace.
#
# After execution, the name exists.


# =============================================================================
# 4. FUNCTION DEFINITIONS ARE EXECUTED AS MODULE-LEVEL STATEMENTS
# =============================================================================

def add(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


# Important distinction:
#
# When Python reaches:
#
#     def add(...):
#
# Python creates the function object and binds it to the name `add`.
#
# The body:
#
#     return first + second
#
# does NOT execute at this point.
#
# The body executes only when:
#
#     add(...)
#
# is called.


print("\nFunction has been defined.")

print("Calling function:")
print(add(10, 20))


# Therefore:
#
# MODULE EXECUTION:
#
#     def add(...)
#         ↓
#     function object created
#         ↓
#     name `add` bound
#
#
# FUNCTION EXECUTION:
#
#     add(10, 20)
#         ↓
#     function body executes


# =============================================================================
# 5. CLASS DEFINITIONS ALSO EXECUTE DURING MODULE EXECUTION
# =============================================================================

class Calculator:
    """Perform basic arithmetic operations."""

    def multiply(self, first: int, second: int) -> int:
        return first * second


# When Python reaches the class statement, it executes the class body
# and creates the class object.
#
# The name:
#
#     Calculator
#
# is then bound to that class object.
#
# The method body itself does not execute merely because the class was
# defined.


calculator = Calculator()

print("\nClass method result:")
print(calculator.multiply(5, 6))


# Again:
#
#     class definition
#         ↓
#     class object created
#
# while:
#
#     calculator.multiply(5, 6)
#         ↓
#     method body executes


# =============================================================================
# 6. CONDITIONAL STATEMENTS AT MODULE LEVEL EXECUTE
# =============================================================================

condition = True

if condition:
    print("\nModule-level if statement executed.")


# Unlike a function body, this conditional statement is evaluated while
# the module itself is executing.
#
# Therefore, top-level control flow is part of module execution.


# =============================================================================
# 7. LOOPS AT MODULE LEVEL ALSO EXECUTE
# =============================================================================

print("\nModule-level loop:")

for value in range(3):
    print(value)


# The loop executes immediately as part of module execution.
#
# This means that module-level code can perform actual work when the
# module is loaded.


# =============================================================================
# 8. IMPORTING A MODULE ALSO CAUSES MODULE EXECUTION
# =============================================================================

# This is one of the most important concepts in Python imports.
#
# When Python imports a module, Python generally:
#
#     1. Finds the module.
#     2. Creates/prepares the module object.
#     3. Executes the module's code.
#     4. Makes the resulting module available to the importer.
#
# Therefore, importing is not merely:
#
#     "read the file"
#
# It involves executing the module's code as part of loading it.


# =============================================================================
# 9. DEMONSTRATING IMPORT EXECUTION
# =============================================================================

# To demonstrate this safely in a single file, we can create a small
# temporary module during runtime.
#
# The temporary module will contain top-level print statements.
#
# When we import it, those statements will execute.

from pathlib import Path
import importlib
import tempfile


temporary_directory = Path(tempfile.mkdtemp())

temporary_module_path = temporary_directory / "execution_demo_module.py"

temporary_module_source = '''
print("Temporary module: top-level code is executing.")

module_value = 500

print("Temporary module: module_value was created.")


def demonstrate() -> int:
    """Return a value from the temporary module."""
    return module_value
'''

temporary_module_path.write_text(
    temporary_module_source,
    encoding="utf-8",
)


# Add the temporary directory to Python's module search path.

import sys

sys.path.insert(0, str(temporary_directory))


print("\nBefore importing temporary module:")
print("The temporary module has not been imported yet.")


# Now import it.

execution_demo_module = importlib.import_module("execution_demo_module")


print("\nAfter importing temporary module:")
print("Imported module value:", execution_demo_module.module_value)


# Observe the order:
#
#     Before import message
#             ↓
#     import module
#             ↓
#     temporary module's top-level code executes
#             ↓
#     import completes
#             ↓
#     After import message
#
# This demonstrates that importing a module executes its top-level code.


# =============================================================================
# 10. IMPORTED FUNCTION DEFINITIONS DO NOT AUTOMATICALLY CALL THE FUNCTIONS
# =============================================================================

# The temporary module contained:
#
#     def demonstrate():
#         ...
#
# The function was defined during module execution.
#
# But its body did not execute during import.
#
# We can call it now:

print("\nCalling imported function:")
print(execution_demo_module.demonstrate())


# Therefore:
#
# IMPORT:
#
#     def demonstrate(...)
#         ↓
#     function object created
#
# CALL:
#
#     demonstrate()
#         ↓
#     function body executes


# =============================================================================
# 11. TOP-LEVEL SIDE EFFECTS
# =============================================================================

# A "side effect" is an observable action caused by executing code.
#
# Examples include:
#
#     - printing
#     - creating files
#     - modifying external data
#     - opening connections
#     - changing configuration
#     - writing to databases
#
# If such code exists at module level, importing the module can trigger
# that side effect.
#
# For example:
#
#     print("This happens during import.")
#
# is a side effect of importing the module.


# =============================================================================
# 12. WHY UNCONTROLLED MODULE-LEVEL CODE CAN BE A PROBLEM
# =============================================================================

# Imagine:
#
#     database.py
#
# contains:
#
#     connect_to_database()
#
# directly at module level.
#
# Then another file does:
#
#     import database
#
# The import itself could immediately establish a database connection.
#
# Sometimes this is intentional.
#
# But often, it is better to place executable application logic inside
# functions and explicitly call those functions when required.


# =============================================================================
# 13. DEFINITIONS VS EXECUTABLE WORK
# =============================================================================

# A useful distinction is:
#
# DEFINITIONS:
#
#     def ...
#     class ...
#
# These create reusable objects.
#
#
# EXECUTABLE WORK:
#
#     function_call()
#     print(...)
#     file.write(...)
#     database_operation()
#
# These perform actions immediately when encountered at module level.
#
#
# Good module design often keeps reusable definitions at module level
# while controlling application execution through functions or a
# main guard.


# =============================================================================
# 14. THE `__name__` ATTRIBUTE DURING DIRECT EXECUTION
# =============================================================================

# When Python executes a file directly, Python normally sets:
#
#     __name__ == "__main__"
#
# We can inspect it:

print("\nCurrent __name__ value:")
print(__name__)


# When this file is executed directly:
#
#     python 08_module_execution.py
#
# the expected value is:
#
#     __main__


# =============================================================================
# 15. THE `__name__` ATTRIBUTE DURING IMPORT
# =============================================================================

# When another module imports this module, this module is not normally
# named `__main__`.
#
# Instead, `__name__` becomes the module's import name.
#
# Conceptually:
#
# DIRECT EXECUTION:
#
#     file.py
#         ↓
#     __name__ = "__main__"
#
#
# IMPORT:
#
#     import file
#         ↓
#     __name__ = "file"


# =============================================================================
# 16. THE MAIN GUARD
# =============================================================================

# Python commonly uses:
#
#     if __name__ == "__main__":
#
# to distinguish direct execution from importing.
#
# The idea is:
#
#     if this file is being run directly:
#         execute application-specific code
#
#     otherwise:
#         do not execute that section during import
#
# Example:

def run_application() -> None:
    """Run the module's application-level demonstration."""
    print("\nApplication function is running.")


if __name__ == "__main__":
    run_application()


# When this file is executed directly:
#
#     __name__ == "__main__"
#
# therefore:
#
#     run_application()
#
# executes.
#
# If this module is imported:
#
#     __name__ != "__main__"
#
# therefore the function call inside the guard does not execute.


# =============================================================================
# 17. WHY THE MAIN GUARD IS IMPORTANT
# =============================================================================

# Without a main guard:
#
#     run_application()
#
# would execute whenever the module is imported.
#
# With:
#
#     if __name__ == "__main__":
#         run_application()
#
# the application-specific execution is controlled.
#
# This allows the same file to function as:
#
#     1. an importable module
#     2. a directly executable script


# =============================================================================
# 18. MODULE INITIALIZATION
# =============================================================================

# When a module is imported for the first time, its top-level code runs
# as part of module initialization.
#
# During this process, Python establishes:
#
#     - module attributes
#     - module namespace
#     - imported names
#     - functions
#     - classes
#     - module-level variables
#
# After successful initialization, the resulting module object can be
# reused by the import system.


# =============================================================================
# 19. MODULES ARE CACHED
# =============================================================================

# Python maintains a cache of loaded modules in:
#
#     sys.modules
#
# We can inspect whether our temporary module is present:

print("\nTemporary module is cached:")
print("execution_demo_module" in sys.modules)


# After importing:
#
#     import execution_demo_module
#
# Python stores the loaded module in `sys.modules`.


# =============================================================================
# 20. REIMPORTING A LOADED MODULE
# =============================================================================

# If we import an already-loaded module again, Python normally reuses
# the existing module object rather than executing the module source
# from scratch again.

first_module_object = execution_demo_module

second_module_object = importlib.import_module("execution_demo_module")

print("\nSame module object after second import:")
print(first_module_object is second_module_object)


# The expected result is:
#
#     True
#
# This is a very important part of Python's import behavior.


# =============================================================================
# 21. IMPORT CACHING AND EXECUTION
# =============================================================================

# Conceptually:
#
# FIRST IMPORT:
#
#     import module
#         ↓
#     locate module
#         ↓
#     execute module
#         ↓
#     store module in sys.modules
#
#
# SECOND IMPORT:
#
#     import module
#         ↓
#     find module in sys.modules
#         ↓
#     reuse existing module object
#
# Therefore, the module's top-level source code does not normally execute
# again simply because the same module is imported again.


# =============================================================================
# 22. EXPLICIT RELOADING
# =============================================================================

# Python provides `importlib.reload()` when a module needs to be executed
# again explicitly.
#
# We can demonstrate this:

print("\nReloading temporary module:")

importlib.reload(execution_demo_module)


# The temporary module's top-level print statements execute again because
# we explicitly requested a reload.
#
# This is different from performing a normal second import.


# =============================================================================
# 23. FIRST IMPORT VS RELOAD
# =============================================================================

# FIRST IMPORT:
#
#     import module
#
# normally:
#
#     executes module code once
#
#     and caches the module.
#
#
# SECOND NORMAL IMPORT:
#
#     import module
#
# normally:
#
#     reuses the cached module.
#
#
# EXPLICIT RELOAD:
#
#     importlib.reload(module)
#
# causes the module code to be executed again.


# =============================================================================
# 24. MODULE EXECUTION ORDER
# =============================================================================

# Suppose a module contains:
#
#     print("A")
#
#     value = 10
#
#     print("B")
#
#     def function():
#         print("C")
#
#     print("D")
#
# During module execution:
#
#     A
#     B
#     D
#
# are printed.
#
# `C` is not printed because the function is only defined, not called.
#
# This distinction is extremely important when reading unfamiliar
# Python modules.


# =============================================================================
# 25. ANOTHER EXECUTION-ORDER EXAMPLE
# =============================================================================

print("\nExecution-order example: start")

order_value = 10

print("Execution-order example: value created")

def show_order() -> None:
    """Print a message when the function is actually called."""
    print("Execution-order example: function body executed")


print("Execution-order example: function defined")

show_order()

print("Execution-order example: end")


# Expected conceptual sequence:
#
#     start
#     value created
#     function defined
#     function body executed
#     end
#
# The function body appears later because it executes only when called.


# =============================================================================
# 26. IMPORTING A MODULE DOES NOT MEAN "CALL EVERY FUNCTION"
# =============================================================================

# This is a common beginner misconception.
#
# Suppose a module contains:
#
#     def clean_data():
#         print("Cleaning data")
#
# Importing the module:
#
#     import cleaning
#
# creates the function object.
#
# It does NOT automatically execute:
#
#     cleaning.clean_data()
#
# unless the module itself explicitly calls that function at module level.


# =============================================================================
# 27. DATA-ENGINEERING EXAMPLE
# =============================================================================

# Imagine:
#
#     pipeline/
#     │
#     ├── ingestion.py
#     ├── transformation.py
#     └── validation.py
#
#
# `ingestion.py` might contain:
#
#     def load_data():
#         ...
#
#
# `transformation.py` might contain:
#
#     def transform_data():
#         ...
#
#
# `validation.py` might contain:
#
#     def validate_data():
#         ...
#
#
# Another module could then do:
#
#     from ingestion import load_data
#     from transformation import transform_data
#     from validation import validate_data
#
# Importing these modules defines their functions.
#
# The actual pipeline operations happen when the functions are called.


# =============================================================================
# 28. GOOD MODULE DESIGN
# =============================================================================

# A reusable module commonly contains:
#
#     1. imports
#     2. constants
#     3. functions
#     4. classes
#     5. controlled executable entry point
#
# For example:
#
#     import ...
#
#     CONSTANT = ...
#
#
#     def process_data():
#         ...
#
#
#     class DataProcessor:
#         ...
#
#
#     def main():
#         ...
#
#
#     if __name__ == "__main__":
#         main()
#
# This structure allows the module to be both reusable and directly
# executable.


# =============================================================================
# 29. IMPORTABLE MODULE VS SCRIPT
# =============================================================================

# A Python file can serve two roles:
#
# ROLE 1 — IMPORTABLE MODULE
#
#     Another file imports it and uses its functions/classes.
#
#
# ROLE 2 — EXECUTABLE SCRIPT
#
#     Python runs the file directly.
#
#
# The main guard allows both roles to coexist cleanly:
#
#     if __name__ == "__main__":
#         main()
#
# This is one of the most useful patterns to understand before working
# with larger Python projects.


# =============================================================================
# 30. MODULE EXECUTION AND SIDE EFFECT CONTROL
# =============================================================================

# Consider this undesirable structure:
#
#     connect_to_database()
#     extract_data()
#     transform_data()
#     load_data()
#
# all directly at module level.
#
# Importing the module could immediately execute the entire pipeline.
#
# A more controlled structure would be:
#
#     def run_pipeline():
#         connect_to_database()
#         extract_data()
#         transform_data()
#         load_data()
#
#
#     if __name__ == "__main__":
#         run_pipeline()
#
# Now importing the module does not automatically run the pipeline.


# =============================================================================
# 31. CLEANUP OF TEMPORARY DEMONSTRATION MODULE
# =============================================================================

# The temporary directory used earlier is no longer needed.
#
# We remove it from sys.path.
#
# The temporary directory itself is intentionally left to the operating
# system's temporary-file management rather than adding manual cleanup
# complexity to this fundamentals example.

sys.path.remove(str(temporary_directory))


# =============================================================================
# 32. COMMON MISCONCEPTIONS
# =============================================================================

# MISCONCEPTION 1:
#
#     "Importing a module only gives me access to its code."
#
# Correction:
#
#     Importing a module also initializes and executes its top-level code
#     during its first load.
#
#
# MISCONCEPTION 2:
#
#     "Importing a module calls all functions inside it."
#
# Correction:
#
#     Function definitions are executed as definitions, but function
#     bodies run only when called.
#
#
# MISCONCEPTION 3:
#
#     "Every import executes the module again."
#
# Correction:
#
#     Normally, Python reuses the module from `sys.modules` after the
#     first successful import.
#
#
# MISCONCEPTION 4:
#
#     "`if __name__ == '__main__'` means Python starts there."
#
# Correction:
#
#     Python still executes the module from top to bottom. The main guard
#     is simply a conditional that controls whether the guarded code runs.
#
#
# MISCONCEPTION 5:
#
#     "A module can only be used as a script."
#
# Correction:
#
#     A Python file can be both an importable module and a directly
#     executable script.


# =============================================================================
# 33. COMPLETE EXECUTION MODEL
# =============================================================================

# A simplified model for:
#
#     python my_module.py
#
# is:
#
#     Python starts the file
#             ↓
#     creates/prepares module execution context
#             ↓
#     sets module attributes
#             ↓
#     executes top-level statements
#             ↓
#     creates variables
#             ↓
#     defines functions/classes
#             ↓
#     executes top-level control flow
#             ↓
#     evaluates the main guard
#             ↓
#     finishes module execution
#
#
# A simplified model for:
#
#     import my_module
#
# is:
#
#     Python receives import request
#             ↓
#     checks module cache
#             ↓
#     locates module if necessary
#             ↓
#     creates/prepares module
#             ↓
#     executes module code
#             ↓
#     stores module in sys.modules
#             ↓
#     returns/reuses module object


# =============================================================================
# 34. KEY TAKEAWAYS
# =============================================================================

# 1. A Python module is executable code.
#
# 2. Module-level statements execute from top to bottom.
#
# 3. Variable assignments execute immediately during module execution.
#
# 4. Function definitions create function objects, but function bodies
#    execute only when the functions are called.
#
# 5. Class definitions create class objects during module execution.
#
# 6. Module-level `if` statements and loops execute during module execution.
#
# 7. Importing a module normally executes its top-level code during its
#    first load.
#
# 8. Imported functions are not automatically called merely because they
#    were defined.
#
# 9. Module-level side effects can therefore occur during import.
#
# 10. `__name__` normally equals:
#
#         "__main__"
#
#     when a file is executed directly.
#
# 11. When imported, `__name__` normally becomes the module's import name.
#
# 12. The common main-guard pattern is:
#
#         if __name__ == "__main__":
#             main()
#
# 13. Python caches loaded modules in:
#
#         sys.modules
#
# 14. A normal repeated import generally reuses the cached module instead
#     of executing its source code again.
#
# 15. `importlib.reload()` explicitly executes a loaded module again.
#
# 16. A well-designed module can be both:
#
#         - reusable through imports
#         - executable as a script
#
# 17. Understanding module execution is the bridge between basic imports
#     and the deeper Python import system.
#
# 18. This completes the current:
#
#         01_modules
#
#     section.
#
# 19. The next section is:
#
#         02_module_search_and_resolution
#
#     beginning with:
#
#         01_sys_path.py
#
#     where we will study how Python decides where to look for modules.