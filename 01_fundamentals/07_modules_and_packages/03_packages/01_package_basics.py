# type: ignore
"""
01_package_basics.py

Demonstrates the basic structure and purpose of a Python package.

A package is a directory used to organize related Python modules.

Example structure:

03_packages/
│
├── __init__.py
├── calculations.py
└── main.py

The directory itself represents the package, while each .py file
inside it represents a module.
"""


# ============================================================
# 1. PACKAGE CONCEPT
# ============================================================

"""
A module:
    A single .py file containing Python code.

A package:
    A directory containing related modules and/or subpackages.

Example:

my_package/
├── __init__.py
├── calculations.py
├── strings.py
└── utilities.py

Here:

my_package       -> package
calculations.py  -> module
strings.py       -> module
utilities.py     -> module
"""


# ============================================================
# 2. WHY PACKAGES ARE USED
# ============================================================

"""
Packages help us:

1. Organize related modules.
2. Separate large programs into logical sections.
3. Avoid having one extremely large Python file.
4. Create reusable code structures.
5. Prevent naming conflicts between unrelated modules.

Example:

project/
├── users/
│   ├── __init__.py
│   ├── authentication.py
│   └── profile.py
│
├── payments/
│   ├── __init__.py
│   ├── invoices.py
│   └── transactions.py
│
└── main.py

The project is divided into logical packages:

users
payments
"""


# ============================================================
# 3. PACKAGE VS MODULE
# ============================================================

"""
MODULE
------

A module is a single Python file.

Example:

calculations.py

PACKAGE
-------

A package is a directory containing related Python modules.

Example:

calculations/
├── __init__.py
├── arithmetic.py
└── statistics.py

So the relationship is:

Package
    ├── Module
    ├── Module
    └── Module
"""


# ============================================================
# 4. SIMPLE PACKAGE EXAMPLE
# ============================================================

"""
Consider this project structure:

project/
│
├── mathematics/
│   ├── __init__.py
│   ├── addition.py
│   └── multiplication.py
│
└── main.py

Here:

mathematics
    -> package

addition.py
    -> module inside mathematics

multiplication.py
    -> module inside mathematics

main.py
    -> separate module using the package
"""


# ============================================================
# 5. PACKAGE NAME
# ============================================================

"""
A package is imported using its package name.

For example:

    import mathematics

The package can also be used as part of a module import:

    import mathematics.addition

Or:

    from mathematics import addition

Or:

    from mathematics.addition import add


The exact import behavior depends on how the package
and its modules are structured.
"""


# ============================================================
# 6. IMPORTANT DISTINCTION
# ============================================================

"""
Do not confuse:

    package
    module
    function
    class

Example:

mathematics/
├── __init__.py
└── addition.py

Inside addition.py:

    def add(first: int, second: int) -> int:
        return first + second


Here:

mathematics
    -> package

addition
    -> module

add
    -> function
"""


# ============================================================
# 7. CONCEPTUAL HIERARCHY
# ============================================================

"""
A useful way to visualize Python's organization:

PROJECT
   │
   ├── PACKAGE
   │      │
   │      ├── MODULE
   │      │      ├── FUNCTION
   │      │      └── CLASS
   │      │
   │      └── MODULE
   │
   └── MODULE

Packages therefore provide a higher-level organizational
structure around modules.
"""


# ============================================================
# 8. KEY TAKEAWAY
# ============================================================

"""
Module  -> one Python file

Package -> directory used to organize Python modules

The main purpose of packages is organization, separation,
reusability, and maintainability.

The next file covers:

    __init__.py
"""

