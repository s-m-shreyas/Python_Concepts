"""
01_absolute_imports.py

Demonstrates absolute imports in Python.

An absolute import specifies the complete path to a module
or object starting from the top-level package.

Example structure:

project/
│
├── main.py
│
└── application/
    ├── __init__.py
    ├── calculations.py
    │
    └── users/
        ├── __init__.py
        └── profile.py


Absolute import examples:

    import application.calculations

    from application.calculations import add

    from application.users.profile import get_profile
"""


# ============================================================
# 1. WHAT IS AN ABSOLUTE IMPORT?
# ============================================================

"""
An absolute import identifies an imported object using its
complete package path.

Example:

    from application.calculations import add


The path is:

    application
        ↓
    calculations
        ↓
    add


Python starts from the top-level package and follows the
specified path.
"""


# ============================================================
# 2. BASIC ABSOLUTE IMPORT
# ============================================================

"""
Structure:

application/
├── __init__.py
└── calculations.py


Import:

    import application.calculations


The complete module name is:

    application.calculations
"""


# ============================================================
# 3. IMPORTING AN OBJECT
# ============================================================

"""
Suppose calculations.py contains:

    def add(first: int, second: int) -> int:
        return first + second


We can import it using:

    from application.calculations import add


Then:

    add(10, 20)


The complete path is explicitly specified.
"""


# ============================================================
# 4. ABSOLUTE IMPORT FROM A SUBPACKAGE
# ============================================================

"""
Structure:

application/
├── __init__.py
└── users/
    ├── __init__.py
    └── profile.py


Suppose profile.py contains:

    def get_profile() -> str:
        return "User profile"


Absolute import:

    from application.users.profile import get_profile


The complete path is:

    application
        ↓
    users
        ↓
    profile
        ↓
    get_profile
"""


# ============================================================
# 5. IMPORTING THE MODULE
# ============================================================

"""
Instead of importing an object directly:

    from application.users.profile import get_profile


we can import the module:

    import application.users.profile


Then access the function through the module:

    application.users.profile.get_profile()


This keeps the module namespace explicit.
"""


# ============================================================
# 6. MULTIPLE ABSOLUTE IMPORTS
# ============================================================

"""
Suppose:

application/
├── calculations.py
└── formatting.py


We can write:

    from application.calculations import add
    from application.formatting import format_number


Each import specifies the complete path from the
top-level package.
"""


# ============================================================
# 7. ABSOLUTE IMPORTS VS LOCAL MODULES
# ============================================================

"""
Consider:

project/
├── main.py
│
└── application/
    ├── calculations.py
    └── users/
        └── profile.py


Inside main.py:

    from application.calculations import add


This is an absolute import because the path begins with:

    application


rather than navigating relative to main.py.
"""


# ============================================================
# 8. ABSOLUTE IMPORTS VS RELATIVE IMPORTS
# ============================================================

"""
Suppose:

application/
├── calculations.py
└── users/
    └── profile.py


Inside profile.py:

Absolute import:

    from application.calculations import add


Relative import:

    from ..calculations import add


Both can refer to the same module.

The difference is how the path is expressed.

Absolute:

    application.calculations

Relative:

    ..calculations
"""


# ============================================================
# 9. ABSOLUTE IMPORTS ARE CONTEXT-INDEPENDENT
# ============================================================

"""
An absolute import describes the destination from the
top-level package.

Example:

    from application.database.connection import connect


The import does not depend on the location of the file
containing the import.

The package hierarchy itself defines the path.
"""


# ============================================================
# 10. DEEP PACKAGE STRUCTURE
# ============================================================

"""
Example:

project/
└── application/
    └── services/
        └── users/
            └── authentication/
                └── login.py


Suppose login.py needs a function from:

application/database/connection.py


An absolute import could be:

    from application.database.connection import connect


Even though login.py is deeply nested, the import starts
from the top-level package:

    application
"""


# ============================================================
# 11. ABSOLUTE IMPORT WITH A MODULE
# ============================================================

"""
This form:

    import application.calculations


imports the module.

Usage:

    application.calculations.add(10, 20)


The package and module names remain visible.
"""


# ============================================================
# 12. ABSOLUTE IMPORT WITH FROM
# ============================================================

"""
This form:

    from application.calculations import add


imports the specific object.

Usage:

    add(10, 20)


The import path identifies exactly where the object comes from.
"""


# ============================================================
# 13. ADVANTAGE: CLEAR ORIGIN
# ============================================================

"""
Absolute imports make the origin of an imported object easy
to identify.

Example:

    from application.database.connection import connect


A reader can immediately see:

    application
        → database
            → connection
                → connect


This becomes especially useful in larger projects.
"""


# ============================================================
# 14. ADVANTAGE: LESS AMBIGUITY
# ============================================================

"""
Consider:

    from utilities import format_data


In a large project, it may not immediately be obvious which
utilities package is being referenced.

A complete absolute path provides more context:

    from application.utilities.formatting import format_data


The source is explicit.
"""


# ============================================================
# 15. IMPORTANT EXECUTION CONTEXT
# ============================================================

"""
Absolute imports depend on Python being able to locate the
top-level package.

For example:

    from application.calculations import add


requires "application" to be importable from the current
Python environment.

Therefore, the way a project is executed can affect whether
an absolute import succeeds.

This connects directly to the previous topic:

    Module Search and Resolution
"""


# ============================================================
# 16. COMMON PROJECT STRUCTURE
# ============================================================

"""
A common application structure:

project/
│
├── main.py
│
└── application/
    ├── __init__.py
    │
    ├── services/
    │   ├── __init__.py
    │   └── user_service.py
    │
    ├── database/
    │   ├── __init__.py
    │   └── connection.py
    │
    └── utilities/
        ├── __init__.py
        └── formatting.py


Absolute imports from within the project may look like:

    from application.database.connection import connect
    from application.services.user_service import create_user
    from application.utilities.formatting import format_name
"""


# ============================================================
# 17. ABSOLUTE IMPORT MENTAL MODEL
# ============================================================

"""
Think of an absolute import as giving Python a complete
address.

Example:

    from application.users.profile import get_profile


Address:

    application
        ↓
    users
        ↓
    profile
        ↓
    get_profile


There is no "go up one directory" instruction.

The path starts from the top-level package.
"""


# ============================================================
# 18. KEY TAKEAWAY
# ============================================================

"""
Absolute import:

    Uses the complete package path.

Example:

    from application.users.profile import get_profile


Mental model:

    top-level package
          ↓
      subpackage
          ↓
        module
          ↓
        object


Advantages:

    - explicit
    - readable
    - less ambiguous
    - easier to understand in large projects

Next concept:

    Relative imports
"""