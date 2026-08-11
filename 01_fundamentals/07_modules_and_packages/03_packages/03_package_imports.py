"""
03_package_imports.py

Demonstrates different ways to import modules and objects
from packages and subpackages.

Example package structure used in this file:

project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── calculations.py
    │
    └── text/
        ├── __init__.py
        └── formatting.py


The examples below demonstrate the import syntax conceptually.
The actual package structure is shown in comments so the file
can be read independently.
"""


# ============================================================
# 1. IMPORT THE PACKAGE
# ============================================================

"""
Structure:

utilities/
└── __init__.py


Import:

    import utilities


This imports the package itself.

The package can then be accessed through its package name:

    utilities
"""


# ============================================================
# 2. IMPORT A MODULE FROM A PACKAGE
# ============================================================

"""
Structure:

utilities/
├── __init__.py
└── calculations.py


Import:

    import utilities.calculations


The complete dotted name identifies the module:

    utilities.calculations
"""


# ============================================================
# 3. ACCESS THE MODULE THROUGH THE PACKAGE
# ============================================================

"""
After:

    import utilities.calculations


The module can be accessed as:

    utilities.calculations


For example, if calculations.py contains:

    def add(first: int, second: int) -> int:
        return first + second


We can call:

    utilities.calculations.add(10, 20)
"""


# ============================================================
# 4. IMPORT THE MODULE DIRECTLY
# ============================================================

"""
Another form is:

    from utilities import calculations


Now the module name can be used directly:

    calculations.add(10, 20)


Compare:

    import utilities.calculations

    utilities.calculations.add(10, 20)


with:

    from utilities import calculations

    calculations.add(10, 20)


Both refer to the same module.
"""


# ============================================================
# 5. IMPORT A FUNCTION FROM A MODULE
# ============================================================

"""
Structure:

utilities/
├── __init__.py
└── calculations.py


Suppose calculations.py contains:

    def add(first: int, second: int) -> int:
        return first + second


We can import the function directly:

    from utilities.calculations import add


Then:

    add(10, 20)


The import path identifies the exact location:

    utilities
        ↓
    calculations
        ↓
    add
"""


# ============================================================
# 6. IMPORT MULTIPLE OBJECTS
# ============================================================

"""
Suppose calculations.py contains:

    def add(first: int, second: int) -> int:
        return first + second

    def subtract(first: int, second: int) -> int:
        return first - second


Both can be imported:

    from utilities.calculations import add, subtract


Then:

    add(10, 20)
    subtract(20, 10)
"""


# ============================================================
# 7. IMPORT A CLASS FROM A PACKAGE MODULE
# ============================================================

"""
Suppose:

utilities/
└── calculations.py


contains:

    class Calculator:
        ...


The class can be imported with:

    from utilities.calculations import Calculator


Then:

    calculator = Calculator()
"""


# ============================================================
# 8. IMPORT FROM A SUBPACKAGE
# ============================================================

"""
Structure:

utilities/
├── __init__.py
└── text/
    ├── __init__.py
    └── formatting.py


The module can be imported with:

    import utilities.text.formatting


The complete path is:

    utilities
        ↓
    text
        ↓
    formatting
"""


# ============================================================
# 9. IMPORT A MODULE FROM A SUBPACKAGE
# ============================================================

"""
Another form:

    from utilities.text import formatting


Then:

    formatting.some_function()


Here:

utilities.text
    -> subpackage

formatting
    -> module
"""


# ============================================================
# 10. IMPORT AN OBJECT FROM A SUBPACKAGE MODULE
# ============================================================

"""
Suppose formatting.py contains:

    def uppercase(text: str) -> str:
        return text.upper()


We can write:

    from utilities.text.formatting import uppercase


Then:

    uppercase("python")


The complete import path is:

    utilities
        ↓
    text
        ↓
    formatting
        ↓
    uppercase
"""


# ============================================================
# 11. IMPORT USING AN ALIAS
# ============================================================

"""
Any imported module can be given a local alias.

Example:

    import utilities.calculations as calc


Now:

    calc.add(10, 20)


Aliases are useful when:

    - a module has a long name
    - a shorter name improves readability
    - a naming conflict needs to be avoided
"""


# ============================================================
# 12. ALIASING AN IMPORTED OBJECT
# ============================================================

"""
Individual objects can also have aliases.

Example:

    from utilities.calculations import add as addition


Now:

    addition(10, 20)


The original function is still named:

    add

but the importing module refers to it locally as:

    addition
"""


# ============================================================
# 13. WILDCARD IMPORT
# ============================================================

"""
Python also allows:

    from utilities.calculations import *


This attempts to import the names exposed by the module.

However, wildcard imports are generally discouraged because
they make it difficult to determine where names came from.

Prefer:

    from utilities.calculations import add, subtract


over:

    from utilities.calculations import *
"""


# ============================================================
# 14. ABSOLUTE IMPORT
# ============================================================

"""
An absolute import specifies the complete path from the
top-level package.

Example:

    from utilities.text.formatting import uppercase


The complete package hierarchy is explicitly written.

This is called an absolute import.
"""


# ============================================================
# 15. RELATIVE IMPORT
# ============================================================

"""
Relative imports are normally used inside package modules.

Structure:

utilities/
├── __init__.py
├── calculations.py
└── text/
    ├── __init__.py
    └── formatting.py


Inside formatting.py:

    from ..calculations import add


Meaning:

    ..              -> parent package: utilities
    calculations    -> calculations.py


Relative imports describe the location relative to the
current package.
"""


# ============================================================
# 16. SINGLE DOT VS DOUBLE DOT
# ============================================================

"""
Inside a package:

    .module

means:

    module in the current package


While:

    ..module

means:

    module in the parent package


Example:

utilities/
├── calculations.py
└── text/
    └── formatting.py


Inside formatting.py:

    from .another_module import something

means:

    utilities.text.another_module


While:

    from ..calculations import add

means:

    utilities.calculations.add
"""


# ============================================================
# 17. PACKAGE IMPORT VS MODULE IMPORT
# ============================================================

"""
Consider:

utilities/
├── __init__.py
└── calculations.py


These are different:

    import utilities

    import utilities.calculations


The first imports the package.

The second imports the calculations module inside
the package.
"""


# ============================================================
# 18. IMPORTING THROUGH __init__.py
# ============================================================

"""
Suppose:

utilities/
├── __init__.py
└── calculations.py


calculations.py:

    def add(first: int, second: int) -> int:
        return first + second


__init__.py:

    from .calculations import add


Now the package can expose add directly.

Instead of:

    from utilities.calculations import add


users can write:

    from utilities import add


This allows __init__.py to act as part of the package's
public interface.
"""


# ============================================================
# 19. CHOOSING AN IMPORT STYLE
# ============================================================

"""
Prefer explicit imports.

Good:

    from utilities.calculations import add


Also good when the module namespace is useful:

    import utilities.calculations


Usually avoid:

    from utilities.calculations import *


because wildcard imports make the source of names unclear.
"""


# ============================================================
# 20. IMPORT PATH MENTAL MODEL
# ============================================================

"""
Think of a package import as walking through directories.

Example:

    from company.employees.developers import write_code


Read it as:

    company
        ↓
    employees
        ↓
    developers
        ↓
    write_code


The path identifies the object from the top-level package
down to the required module or object.
"""


# ============================================================
# 21. SUMMARY
# ============================================================

"""
Common package import forms:

1. Import a package:

       import utilities


2. Import a module:

       import utilities.calculations


3. Import a module from a package:

       from utilities import calculations


4. Import an object:

       from utilities.calculations import add


5. Import with an alias:

       import utilities.calculations as calc


6. Import an object with an alias:

       from utilities.calculations import add as addition


7. Import from a subpackage:

       from utilities.text.formatting import uppercase


8. Relative import:

       from ..calculations import add


Main idea:

    package → subpackage → module → object

is represented through dotted import paths.
"""