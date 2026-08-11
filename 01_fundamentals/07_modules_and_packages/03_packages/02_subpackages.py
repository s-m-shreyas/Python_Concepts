"""
02_subpackages.py

Demonstrates subpackages (nested packages) in Python.

A subpackage is a package located inside another package.

Example structure:

03_packages/
│
└── company/
    ├── __init__.py
    │
    ├── employees/
    │   ├── __init__.py
    │   ├── developers.py
    │   └── managers.py
    │
    └── finance/
        ├── __init__.py
        ├── payroll.py
        └── billing.py
"""


# ============================================================
# 1. WHAT IS A SUBPACKAGE?
# ============================================================

"""
A subpackage is simply a package inside another package.

Example:

company/
├── __init__.py
│
└── employees/
    ├── __init__.py
    └── developers.py


Here:

company
    -> parent package

employees
    -> subpackage

developers.py
    -> module inside the subpackage
"""


# ============================================================
# 2. PACKAGE HIERARCHY
# ============================================================

"""
A package can contain:

    modules
    subpackages
    modules inside subpackages
    further nested subpackages

Example:

company/
├── __init__.py
│
├── employees/
│   ├── __init__.py
│   ├── developers.py
│   └── managers.py
│
└── finance/
    ├── __init__.py
    ├── payroll.py
    └── billing.py


Hierarchy:

company
│
├── employees
│   ├── developers
│   └── managers
│
└── finance
    ├── payroll
    └── billing
"""


# ============================================================
# 3. WHY USE SUBPACKAGES?
# ============================================================

"""
Subpackages are useful when a package becomes large.

Instead of:

company/
├── employee_developers.py
├── employee_managers.py
├── finance_payroll.py
├── finance_billing.py
├── hr_recruitment.py
├── hr_training.py
└── ...

We can organize related modules:

company/
├── employees/
│   ├── developers.py
│   └── managers.py
│
├── finance/
│   ├── payroll.py
│   └── billing.py
│
└── hr/
    ├── recruitment.py
    └── training.py


This creates a logical hierarchy.
"""


# ============================================================
# 4. PACKAGE → SUBPACKAGE → MODULE
# ============================================================

"""
Consider:

company/
└── employees/
    └── developers.py


There are three levels:

company
    -> package

employees
    -> subpackage

developers.py
    -> module


The full module path is:

company.employees.developers
"""


# ============================================================
# 5. IMPORTING A MODULE FROM A SUBPACKAGE
# ============================================================

"""
Suppose:

company/
├── __init__.py
└── employees/
    ├── __init__.py
    └── developers.py


The module can be imported with:

    import company.employees.developers


The complete dotted path identifies:

    company
        ↓
    employees
        ↓
    developers


Dotted notation represents the package hierarchy.
"""


# ============================================================
# 6. IMPORTING AN OBJECT FROM A SUBPACKAGE MODULE
# ============================================================

"""
Suppose developers.py contains:

    def write_code() -> str:
        return "Writing Python code"


It can be imported using:

    from company.employees.developers import write_code


The path means:

    company
        -> employees
            -> developers
                -> write_code
"""


# ============================================================
# 7. IMPORTING THE SUBPACKAGE
# ============================================================

"""
A subpackage can also be imported directly.

Example:

    import company.employees


Here:

company
    -> parent package

employees
    -> subpackage


The subpackage can then be accessed through the parent:

    company.employees
"""


# ============================================================
# 8. MULTIPLE SUBPACKAGES
# ============================================================

"""
A package can contain multiple subpackages.

Example:

application/
│
├── users/
│   ├── __init__.py
│   ├── authentication.py
│   └── profile.py
│
├── orders/
│   ├── __init__.py
│   ├── creation.py
│   └── tracking.py
│
└── payments/
    ├── __init__.py
    ├── billing.py
    └── refunds.py


Here:

application
    -> parent package

users
    -> subpackage

orders
    -> subpackage

payments
    -> subpackage
"""


# ============================================================
# 9. MULTI-LEVEL NESTING
# ============================================================

"""
Subpackages can themselves contain subpackages.

Example:

company/
└── departments/
    └── engineering/
        └── backend/
            └── python/
                └── utilities.py


The complete module path is:

company.departments.engineering.backend.python.utilities


Python package structures can therefore form multiple
hierarchical levels.
"""


# ============================================================
# 10. RELATIVE IMPORTS IN SUBPACKAGES
# ============================================================

"""
Relative imports are especially useful in nested packages.

Example:

company/
├── __init__.py
└── employees/
    ├── __init__.py
    ├── developers.py
    └── managers.py


Inside developers.py:

    from .managers import Manager


The single dot means:

    current package


So:

    .managers

means:

    company.employees.managers
"""


# ============================================================
# 11. GOING TO THE PARENT PACKAGE
# ============================================================

"""
Two dots can be used to move to the parent package.

Example:

company/
├── __init__.py
├── common.py
└── employees/
    ├── __init__.py
    └── developers.py


Inside developers.py:

    from ..common import some_function


Meaning:

    ..      -> parent package (company)
    common  -> common.py


So:

    ..common

refers to:

    company.common
"""


# ============================================================
# 12. SUBPACKAGE VS MODULE
# ============================================================

"""
These are different:

company/
├── employees.py
└── finance/
    └── payroll.py


employees.py
    -> module

finance/
    -> package/subpackage

payroll.py
    -> module inside the finance subpackage


A directory and a .py file are not the same thing.
"""


# ============================================================
# 13. REAL-WORLD ORGANIZATION
# ============================================================

"""
A larger application might look like:

data_engineering/
│
├── ingestion/
│   ├── csv/
│   │   ├── reader.py
│   │   └── validator.py
│   │
│   └── database/
│       ├── reader.py
│       └── connector.py
│
├── transformation/
│   ├── cleaning/
│   │   ├── nulls.py
│   │   └── duplicates.py
│   │
│   └── aggregation/
│       └── metrics.py
│
└── output/
    ├── csv/
    │   └── writer.py
    │
    └── database/
        └── writer.py


This is a practical example of using subpackages to organize
a larger codebase.
"""


# ============================================================
# 14. IMPORTANT RULE
# ============================================================

"""
The dot-separated import path follows the directory hierarchy.

Example:

project/
└── company/
    └── employees/
        └── developers.py


Import path:

    company.employees.developers


Read it from left to right:

    company
        ↓
    employees
        ↓
    developers
"""


# ============================================================
# 15. KEY TAKEAWAY
# ============================================================

"""
Package:
    A directory used to organize Python modules.

Subpackage:
    A package inside another package.

Module:
    A Python .py file.

Example:

company/
└── employees/
    └── developers.py

    company
        -> package

    employees
        -> subpackage

    developers.py
        -> module

Full module path:

    company.employees.developers

Subpackages allow large Python projects to be organized
into multiple logical levels.
"""