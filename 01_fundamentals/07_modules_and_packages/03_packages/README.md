# Packages

This section explains how Python uses **packages to organize related modules into structured, reusable codebases**.

The progression starts with basic packages and gradually moves toward nested packages, package imports, and package interfaces.

## Topics Covered

### 01. Package Basics

Understanding what a Python package is and why packages are useful.

Key concepts:

* Package
* Module
* Package vs module
* Package hierarchy
* Organizing related modules
* Package naming

Basic structure:

```text
package/
├── __init__.py
├── module_a.py
└── module_b.py
```

### 02. Subpackages

Understanding packages nested inside other packages.

Key concepts:

* Parent packages
* Subpackages
* Nested package structures
* Package hierarchy
* Multi-level package organization

Example:

```text
company/
├── __init__.py
│
├── employees/
│   ├── __init__.py
│   └── developers.py
│
└── finance/
    ├── __init__.py
    └── payroll.py
```

### 03. Package Imports

Understanding how modules and objects are imported from packages and subpackages.

Key concepts:

* `import package`
* `import package.module`
* `from package import module`
* `from package.module import object`
* Import aliases
* Absolute imports
* Relative imports
* Wildcard imports

Example:

```python
from company.employees.developers import write_code
```

### 04. `__init__.py`

Understanding the role of `__init__.py` in package initialization and package interfaces.

Key concepts:

* Empty `__init__.py`
* Package initialization
* Package-level names
* Re-exporting objects
* Package namespaces
* `__all__`
* Public package interfaces
* `__init__.py` in subpackages

Example:

```text
utilities/
├── __init__.py
├── calculations.py
└── text/
    ├── __init__.py
    └── formatting.py
```

## Learning Objective

By the end of this section, you should be able to understand and construct a package hierarchy such as:

```text
project/
│
├── main.py
│
└── application/
    ├── __init__.py
    │
    ├── users/
    │   ├── __init__.py
    │   ├── authentication.py
    │   └── profile.py
    │
    ├── database/
    │   ├── __init__.py
    │   └── connection.py
    │
    └── utilities/
        ├── __init__.py
        └── formatting.py
```

You should also understand how Python represents this hierarchy through dotted import paths:

```text
application.users.authentication
application.database.connection
application.utilities.formatting
```

## Core Mental Model

The package system can be visualized as:

```text
Project
   │
   └── Package
         │
         ├── Module
         │
         ├── Module
         │
         └── Subpackage
                │
                ├── Module
                └── Module
```

And imports navigate through this hierarchy:

```text
Package
   ↓
Subpackage
   ↓
Module
   ↓
Object
```

## Relationship With Previous Topics

This section builds directly on the previous module concepts.

```text
Modules
   ↓
Module Search & Resolution
   ↓
Packages
   ↓
Subpackages
   ↓
Package Imports
   ↓
Package Interfaces
```

The goal is not just to memorize import syntax, but to understand **how Python code is organized into scalable module and package structures**.
