# Import Patterns

This section focuses on **common ways of writing imports in Python** and the conventions used to keep imports clear, readable, and maintainable.

It builds on the previous sections covering module search, resolution, and packages.

## Topics Covered

### 01. Absolute Imports

Understanding imports that specify the complete path from the top-level package.

Example:

```python
from application.users.profile import get_profile
```

Key concepts:

* Absolute import paths
* Top-level packages
* Importing modules
* Importing objects
* Absolute imports in nested packages
* Absolute vs relative imports

### 02. Relative Imports

Understanding imports relative to the current package.

Examples:

```python
from .validation import validate_user
from ..database import connect
```

Key concepts:

* Current package
* Parent package
* `.` notation
* `..` notation
* Multi-level relative imports
* Package context
* Absolute vs relative imports

### 03. Import Aliases

Understanding the `as` keyword for assigning local names to imported modules or objects.

Examples:

```python
import pandas as pd
import application.utilities as utils

from application.models import User as UserAccount
```

Key concepts:

* Module aliases
* Function aliases
* Class aliases
* Naming conflicts
* Standard alias conventions
* Meaningful aliases

### 04. Import Conventions

Understanding how imports should generally be organized in clean Python code.

Key concepts:

* Standard-library imports
* Third-party imports
* Local application imports
* Import grouping
* Blank-line separation
* Explicit imports
* Avoiding wildcard imports
* Meaningful aliases
* Circular imports
* Readable import formatting

## Import Pattern Overview

The four concepts can be visualized as:

```text
Import Patterns
│
├── Absolute Imports
│       ↓
│   Complete package path
│
├── Relative Imports
│       ↓
│   Current package context
│
├── Import Aliases
│       ↓
│   Alternative local names
│
└── Import Conventions
        ↓
    Clean and consistent organization
```

## Learning Objective

By the end of this section, you should be able to:

* Write absolute imports.
* Write relative imports.
* Understand the difference between absolute and relative imports.
* Use import aliases appropriately.
* Resolve common naming conflicts.
* Organize imports into logical groups.
* Avoid unnecessary or problematic import patterns.
* Write imports that are easy to read and maintain.

The goal is not simply to memorize import syntax, but to understand **why a particular import style is appropriate in a given package structure**.
