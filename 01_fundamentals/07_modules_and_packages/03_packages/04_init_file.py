"""
04_init_file.py

Demonstrates the role of __init__.py in a Python package.

Package structure used in the examples:

project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── calculations.py
    └── text/
        ├── __init__.py
        └── formatting.py
"""


# ============================================================
# 1. WHAT IS __init__.py?
# ============================================================

"""
__init__.py is a special file associated with a Python package.

Example:

utilities/
├── __init__.py
└── calculations.py


Here:

utilities
    -> package

__init__.py
    -> package initialization file

calculations.py
    -> module
"""


# ============================================================
# 2. __init__.py CAN BE EMPTY
# ============================================================

"""
An __init__.py file does not have to contain code.

Example:

utilities/
├── __init__.py
└── calculations.py


An empty __init__.py is still a valid package file.

The package can still contain and expose modules such as:

    utilities.calculations
"""


# ============================================================
# 3. __init__.py IS EXECUTED DURING PACKAGE IMPORT
# ============================================================

"""
Suppose utilities/__init__.py contains:

    print("utilities package initialized")


Then:

    import utilities


causes the initialization code in __init__.py to execute.

This is why __init__.py can be used for package-level
initialization.
"""


# ============================================================
# 4. PACKAGE-LEVEL VARIABLES
# ============================================================

"""
__init__.py can define variables belonging to the package.

Example:

# utilities/__init__.py

PACKAGE_NAME = "utilities"
PACKAGE_VERSION = "1.0"


Then:

    import utilities

    print(utilities.PACKAGE_NAME)
    print(utilities.PACKAGE_VERSION)
"""


# ============================================================
# 5. PACKAGE-LEVEL FUNCTIONS
# ============================================================

"""
Functions can also be defined in __init__.py.

Example:

# utilities/__init__.py

def package_info() -> str:
    return "Utility package"


Then:

    import utilities

    print(utilities.package_info())


However, large functionality should normally remain inside
dedicated modules.
"""


# ============================================================
# 6. RE-EXPORTING OBJECTS
# ============================================================

"""
One of the most useful purposes of __init__.py is re-exporting
selected objects.

Suppose:

utilities/
├── __init__.py
└── calculations.py


calculations.py:

    def add(first: int, second: int) -> int:
        return first + second


__init__.py:

    from .calculations import add


Now users can write:

    from utilities import add


instead of:

    from utilities.calculations import add


The package provides a cleaner public interface.
"""


# ============================================================
# 7. __init__.py AND THE PACKAGE NAMESPACE
# ============================================================

"""
Consider:

utilities/
├── __init__.py
└── calculations.py


If __init__.py contains:

    from .calculations import add


Then:

    import utilities

makes the following available:

    utilities.add


The function has been brought into the package namespace.
"""


# ============================================================
# 8. __init__.py IN A SUBPACKAGE
# ============================================================

"""
__init__.py can also exist inside a subpackage.

Example:

utilities/
├── __init__.py
└── text/
    ├── __init__.py
    └── formatting.py


Here:

utilities
    -> package

utilities.text
    -> subpackage

utilities.text.__init__.py
    -> initialization file of the text subpackage
"""


# ============================================================
# 9. RE-EXPORTING FROM A SUBPACKAGE
# ============================================================

"""
Suppose:

utilities/text/formatting.py:

    def uppercase(text: str) -> str:
        return text.upper()


utilities/text/__init__.py:

    from .formatting import uppercase


Now:

    from utilities.text import uppercase


is possible.

The subpackage's __init__.py acts as the interface for
the text subpackage.
"""


# ============================================================
# 10. HIERARCHICAL PUBLIC INTERFACE
# ============================================================

"""
A package can create a public interface at multiple levels.

Example:

utilities/
├── __init__.py
│
└── text/
    ├── __init__.py
    └── formatting.py


formatting.py:

    def uppercase(text: str) -> str:
        return text.upper()


text/__init__.py:

    from .formatting import uppercase


utilities/__init__.py:

    from .text import uppercase


Now the user can write:

    from utilities import uppercase


The internal structure is hidden behind the package interface.
"""


# ============================================================
# 11. RELATIVE IMPORTS IN __init__.py
# ============================================================

"""
Inside __init__.py, relative imports are commonly used.

Example:

    from .calculations import add


The single dot means:

    current package


So:

    .calculations

refers to:

    utilities.calculations
"""


# ============================================================
# 12. __all__
# ============================================================

"""
__init__.py can define __all__ to describe names intended
for wildcard imports.

Example:

# utilities/__init__.py

from .calculations import add
from .calculations import subtract

__all__ = ["add", "subtract"]


Then:

    from utilities import *


imports the names listed in __all__.


Important:

Wildcard imports are generally discouraged in application
code. __all__ is more useful as an explicit declaration of
the intended public API.
"""


# ============================================================
# 13. __init__.py IS NOT THE SAME AS main.py
# ============================================================

"""
Do not confuse:

    __init__.py
    main.py


__init__.py:

    -> initializes a package
    -> can define package-level names
    -> can expose package functionality


main.py:

    -> usually contains application entry-point logic
    -> normally runs the application


They serve different purposes.
"""


# ============================================================
# 14. KEEP __init__.py LIGHTWEIGHT
# ============================================================

"""
A good __init__.py is generally small.

Good:

    from .calculations import add
    from .calculations import subtract


Less desirable:

    complex business logic
    database connections
    large workflows
    heavy processing
    application execution


Keep actual functionality inside appropriate modules.
Use __init__.py mainly for package organization and interface.
"""


# ============================================================
# 15. MODERN PYTHON NOTE
# ============================================================

"""
__init__.py is not technically required for every possible
Python package.

Python supports namespace packages that can exist without
__init__.py.

However, regular packages commonly use __init__.py because
it provides an explicit package boundary and a place for
package initialization and public exports.
"""


# ============================================================
# 16. COMPLETE EXAMPLE
# ============================================================

"""
Package structure:

utilities/
├── __init__.py
├── calculations.py
└── text/
    ├── __init__.py
    └── formatting.py


calculations.py:

    def add(first: int, second: int) -> int:
        return first + second


text/formatting.py:

    def uppercase(text: str) -> str:
        return text.upper()


utilities/__init__.py:

    from .calculations import add


text/__init__.py:

    from .formatting import uppercase


Usage:

    from utilities import add
    from utilities.text import uppercase


Then:

    print(add(10, 20))
    print(uppercase("python"))


The package structure determines how the public interface
is exposed.
"""


# ============================================================
# 17. KEY TAKEAWAY
# ============================================================

"""
__init__.py can:

    -> mark/use a regular package structure
    -> initialize a package
    -> define package-level names
    -> re-export selected objects
    -> define __all__
    -> provide a clean public interface

Think of it as:

    package
        ↓
    __init__.py
        ↓
    package interface


while:

    module.py
        ↓
    actual functionality
"""