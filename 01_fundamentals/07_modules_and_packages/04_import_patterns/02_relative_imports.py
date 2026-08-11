"""
02_relative_imports.py

Demonstrates relative imports in Python.

A relative import specifies the location of a module or object
relative to the current package.

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


Relative imports are normally used from modules inside
a package.
"""


# ============================================================
# 1. WHAT IS A RELATIVE IMPORT?
# ============================================================

"""
A relative import identifies a module using its position
relative to the current package.

Example:

    from ..calculations import add


If this statement appears inside:

    application.users.profile


then:

    ..calculations

means:

    go to the parent package (application)
    and find calculations.py
"""


# ============================================================
# 2. SINGLE DOT
# ============================================================

"""
A single dot means:

    the current package


Example structure:

application/
└── users/
    ├── __init__.py
    ├── profile.py
    └── formatting.py


Inside profile.py:

    from .formatting import format_name


The single dot means:

    application.users

Therefore:

    .formatting

refers to:

    application.users.formatting
"""


# ============================================================
# 3. DOUBLE DOT
# ============================================================

"""
Two dots mean:

    the parent package


Example:

application/
├── calculations.py
└── users/
    ├── __init__.py
    └── profile.py


Inside profile.py:

    from ..calculations import add


The path is:

    profile.py
        ↓
    users
        ↓
    application
        ↓
    calculations.py


Therefore:

    ..calculations

means:

    application.calculations
"""


# ============================================================
# 4. TRIPLE DOT
# ============================================================

"""
Three dots move up two package levels.

Example:

application/
├── utilities.py
│
└── services/
    └── users/
        └── profile.py


Inside profile.py:

    from ...utilities import format_value


Movement:

    ...  -> go up two package levels


Starting from:

    application.services.users


go up:

    users
      ↓
    services
      ↓
    application


Then find:

    utilities.py
"""


# ============================================================
# 5. RELATIVE IMPORT PATH
# ============================================================

"""
The number of dots controls how far upward Python moves.

    .module
        -> current package

    ..module
        -> parent package

    ...module
        -> parent's parent package


The general pattern is:

    from <dots><module> import <object>
"""


# ============================================================
# 6. IMPORTING A MODULE RELATIVELY
# ============================================================

"""
Example:

application/
└── users/
    ├── __init__.py
    ├── profile.py
    └── validation.py


Inside profile.py:

    from . import validation


This imports the validation module from the current package.
"""


# ============================================================
# 7. IMPORTING AN OBJECT RELATIVELY
# ============================================================

"""
Suppose validation.py contains:

    def validate_name(name: str) -> bool:
        return bool(name.strip())


Inside profile.py:

    from .validation import validate_name


Then:

    validate_name("Alice")


The import is relative because it starts with:

    .
"""


# ============================================================
# 8. IMPORTING FROM A PARENT PACKAGE
# ============================================================

"""
Example:

application/
├── calculations.py
│
└── users/
    ├── __init__.py
    └── profile.py


Inside profile.py:

    from ..calculations import add


The two dots mean:

    current package
        ↓
    parent package


So:

    ..calculations

means:

    application.calculations
"""


# ============================================================
# 9. ABSOLUTE VS RELATIVE
# ============================================================

"""
Same project:

application/
├── calculations.py
└── users/
    └── profile.py


Absolute import:

    from application.calculations import add


Relative import:

    from ..calculations import add


Both can point to:

    application.calculations.add


The difference is how the destination is expressed.
"""


# ============================================================
# 10. RELATIVE IMPORTS ARE PACKAGE-BASED
# ============================================================

"""
Relative imports depend on the current module's package.

Example:

    from ..calculations import add


Python needs to know the package context of the module
containing this statement.

This is why relative imports are normally used inside
properly structured packages.
"""


# ============================================================
# 11. RELATIVE IMPORTS AND __package__
# ============================================================

"""
Python determines relative-import context using package
information associated with the current module.

Conceptually:

    current module
          ↓
    current package
          ↓
    relative import


The module's __package__ attribute helps Python determine
where a relative import should begin.
"""


# ============================================================
# 12. RELATIVE IMPORTS CANNOT START FROM NOWHERE
# ============================================================

"""
A relative import such as:

    from .utilities import helper


requires a package context.

A standalone script executed directly may not have the
package context required for relative imports.

For example, directly running a deeply nested file can lead
to errors such as:

    ImportError:
    attempted relative import with no known parent package


This is an important reason to understand how Python modules
are executed.
"""


# ============================================================
# 13. CURRENT PACKAGE VS CURRENT DIRECTORY
# ============================================================

"""
Do not think of:

    .

as simply:

    "current filesystem directory"


For imports, the dot represents the current PACKAGE context.

Example:

    from .validation import validate_name


means:

    validation relative to the current package.


It is not simply a filesystem navigation operator.
"""


# ============================================================
# 14. RELATIVE IMPORTS IN SUBPACKAGES
# ============================================================

"""
Example:

application/
│
├── calculations.py
│
└── services/
    ├── __init__.py
    │
    └── users/
        ├── __init__.py
        └── profile.py


Inside profile.py:

    from ...calculations import add


Movement:

    profile
      ↓
    users
      ↓
    services
      ↓
    application
      ↓
    calculations


The number of dots corresponds to the package levels
being traversed.
"""


# ============================================================
# 15. RELATIVE IMPORT WITH A SUBPACKAGE
# ============================================================

"""
Example:

application/
└── users/
    ├── __init__.py
    ├── profile.py
    │
    └── formatting/
        ├── __init__.py
        └── names.py


Inside profile.py:

    from .formatting.names import format_name


The single dot means:

    application.users

Then:

    formatting
        ↓
    names
        ↓
    format_name
"""


# ============================================================
# 16. ADVANTAGE: PACKAGE RELOCATION
# ============================================================

"""
Relative imports can make internal package relationships
less dependent on the package's top-level name.

Example:

    from ..calculations import add


The import describes:

    "calculations is in my parent package"

rather than:

    "calculations is inside a package named application"


This can be useful when the internal package structure is
more important than the top-level package name.
"""


# ============================================================
# 17. ADVANTAGE: CLEAR INTERNAL RELATIONSHIPS
# ============================================================

"""
Relative imports can clearly communicate that an import comes
from the same package hierarchy.

Example:

    from .validation import validate_name


The leading dot immediately tells the reader:

    validation belongs to the current package.
"""


# ============================================================
# 18. LIMITATION: HARDER TO READ IN DEEP STRUCTURES
# ============================================================

"""
Deep relative imports can become difficult to understand.

Example:

    from ....utilities.formatting import format_value


A reader must count the dots to determine where the import
starts.

For this reason, excessive relative nesting can reduce
readability.
"""


# ============================================================
# 19. COMMON ERROR
# ============================================================

"""
Incorrect assumption:

    from .module import function


can be used from any Python file.

Not necessarily.

Relative imports require package context.

They are designed primarily for modules that are part of
a package hierarchy.
"""


# ============================================================
# 20. RELATIVE IMPORT MENTAL MODEL
# ============================================================

"""
Think of relative imports as navigating the package tree.

Example:

application/
├── calculations.py
└── users/
    └── profile.py


Inside profile.py:

    from .validation import validate


means:

    stay here


While:

    from ..calculations import add


means:

    move to parent package
        ↓
    find calculations


Mental model:

    .      -> current package
    ..     -> parent package
    ...    -> parent's parent package
"""


# ============================================================
# 21. KEY TAKEAWAY
# ============================================================

"""
Relative imports:

    -> describe imports relative to the current package
    -> use dots to move through the package hierarchy
    -> require package context

Examples:

    from .module import object

        current package


    from ..module import object

        parent package


    from ...module import object

        two levels above


Absolute:

    from application.users.profile import get_profile


Relative:

    from .profile import get_profile

or:

    from ..calculations import add


Main distinction:

    Absolute import
        -> starts from the top-level package

    Relative import
        -> starts from the current package context
"""