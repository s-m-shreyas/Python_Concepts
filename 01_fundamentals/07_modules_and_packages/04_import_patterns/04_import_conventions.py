"""
04_import_conventions.py

Demonstrates common Python conventions for writing imports.

This file focuses on writing imports in a clean, readable,
consistent, and maintainable way.

The examples are based on commonly followed Python style
conventions.
"""


# ============================================================
# 1. IMPORTS SHOULD GENERALLY BE AT THE TOP
# ============================================================

"""
Imports are normally placed near the beginning of a module.

Example:

    import os
    import sys

    from application.database import connect
    from application.users import User


Then the rest of the module follows.

Keeping imports near the top makes dependencies easy to see.
"""


# ============================================================
# 2. STANDARD LIBRARY FIRST
# ============================================================

"""
A common convention is to group imports into three sections:

    1. Standard library
    2. Third-party packages
    3. Local application imports


Example:

    import os
    import sys
    from pathlib import Path

    import pandas as pd
    import requests

    from application.database import connect
    from application.users import User


Each group is separated by a blank line.
"""


# ============================================================
# 3. STANDARD LIBRARY IMPORTS
# ============================================================

"""
Standard-library modules come first.

Example:

    import os
    import sys
    from pathlib import Path
    from datetime import datetime


These modules are provided by Python itself.
"""


# ============================================================
# 4. THIRD-PARTY IMPORTS
# ============================================================

"""
Third-party libraries are normally placed after standard
library imports.

Example:

    import pandas as pd
    import requests


These packages are installed separately from Python itself.
"""


# ============================================================
# 5. LOCAL APPLICATION IMPORTS
# ============================================================

"""
Imports belonging to the current project are normally placed
after third-party imports.

Example:

    from application.database import connect
    from application.models import User
    from application.services import UserService
"""


# ============================================================
# 6. GROUP RELATED IMPORTS
# ============================================================

"""
Related imports can be grouped together.

Example:

    from application.models import User
    from application.models import Address
    from application.models import Order


This makes the relationship between imported objects clear.
"""


# ============================================================
# 7. SEPARATE IMPORT GROUPS WITH BLANK LINES
# ============================================================

"""
Recommended structure:

    import os
    import sys

    import pandas as pd
    import numpy as np

    from application.database import connect
    from application.models import User


The blank lines visually separate dependency categories.
"""


# ============================================================
# 8. PREFER EXPLICIT IMPORTS
# ============================================================

"""
Prefer:

    from application.calculations import add, subtract


over:

    from application.calculations import *


Explicit imports make it clear which names are being used.
"""


# ============================================================
# 9. AVOID WILDCARD IMPORTS
# ============================================================

"""
Avoid:

    from application.calculations import *


Wildcard imports make it difficult to determine:

    - where a name came from
    - which names are available
    - whether names conflict with each other


Prefer:

    from application.calculations import add, subtract
"""


# ============================================================
# 10. USE ALIASES WHEN THEY ARE STANDARD
# ============================================================

"""
Some libraries have widely accepted aliases.

Examples:

    import pandas as pd
    import numpy as np


These conventions are immediately recognizable to most
Python developers.
"""


# ============================================================
# 11. USE MEANINGFUL CUSTOM ALIASES
# ============================================================

"""
When a custom alias is necessary, make it understandable.

Good:

    import application.utilities.formatting as fmt


Less useful:

    import application.utilities.formatting as x


An alias should improve readability rather than reduce it.
"""


# ============================================================
# 12. AVOID UNNECESSARY ALIASES
# ============================================================

"""
Avoid:

    import application.calculations as calculations


if the alias is identical to the original name.

Also avoid:

    from application.calculations import add as add


There is no benefit from either alias.
"""


# ============================================================
# 13. IMPORT MODULES WHEN NAMESPACE CLARITY HELPS
# ============================================================

"""
Consider:

    import application.calculations as calc


Then:

    calc.add(10, 20)
    calc.subtract(20, 10)


This makes it obvious that add() and subtract() belong
to the calculations module.
"""


# ============================================================
# 14. IMPORT SPECIFIC OBJECTS WHEN APPROPRIATE
# ============================================================

"""
Instead of:

    import application.calculations as calc


you can use:

    from application.calculations import add


Then:

    add(10, 20)


This can be convenient when only one or two objects are needed.
"""


# ============================================================
# 15. AVOID VERY LONG IMPORT LINES
# ============================================================

"""
If an import becomes too long, it can be formatted across
multiple lines.

Example:

    from application.data_processing.transformations import (
        clean_data,
        normalize_data,
        remove_duplicates,
    )


This is easier to read than one extremely long line.
"""


# ============================================================
# 16. TRAILING COMMA IN MULTI-LINE IMPORTS
# ============================================================

"""
For multi-line imports, a trailing comma is commonly used.

Example:

    from application.models import (
        User,
        Address,
        Order,
    )


Benefits include:

    - easier future additions
    - cleaner diffs
    - consistent formatting
"""


# ============================================================
# 17. SORT IMPORTS CONSISTENTLY
# ============================================================

"""
Within an import group, imports are commonly kept in a
consistent order.

Example:

    import json
    import os
    import sys

    from datetime import datetime
    from pathlib import Path


Consistency is more important than manually optimizing
the order for every file.
"""


# ============================================================
# 18. ABSOLUTE IMPORTS FOR APPLICATION CODE
# ============================================================

"""
Absolute imports are often preferred for clarity.

Example:

    from application.database import connect
    from application.models import User


The complete application package is visible.

This is especially useful in larger projects.
"""


# ============================================================
# 19. RELATIVE IMPORTS INSIDE PACKAGES
# ============================================================

"""
Relative imports are commonly useful for closely related
modules inside the same package.

Example:

    from .validation import validate_user
    from ..database import connect


The choice depends on the project's structure and conventions.

The important rule is to use imports consistently.
"""


# ============================================================
# 20. AVOID IMPORTS IN THE MIDDLE OF THE FILE
# ============================================================

"""
Generally avoid:

    def process_data() -> None:
        import pandas as pd

        ...


when the import is not intentionally local.

Usually prefer:

    import pandas as pd


at the top of the file.

Local imports can sometimes be appropriate for:

    - breaking circular dependencies
    - optional dependencies
    - expensive imports that should be delayed

These should be intentional decisions.
"""


# ============================================================
# 21. AVOID CIRCULAR IMPORTS
# ============================================================

"""
A circular dependency can occur when:

    module_a
        ↓
    imports module_b
        ↓
    imports module_a


Example:

a.py:

    from b import function_b


b.py:

    from a import function_a


This can produce import errors or partially initialized
modules.

A better design is often to move shared functionality into
a separate module.
"""


# ============================================================
# 22. KEEP IMPORTS SIMPLE
# ============================================================

"""
Prefer straightforward imports such as:

    from application.models import User


over complicated import structures that are difficult to
understand.

Imports are dependencies.

A reader should be able to quickly understand:

    What does this module depend on?
    Where does each dependency come from?
"""


# ============================================================
# 23. IMPORT CONVENTION EXAMPLE
# ============================================================

"""
A well-organized module might begin like this:

    import json
    import os
    from pathlib import Path

    import pandas as pd
    import requests

    from application.database import connect
    from application.models import User
    from application.services import UserService


Notice:

    standard library
        ↓
    third-party
        ↓
    local application


Each group is separated by a blank line.
"""


# ============================================================
# 24. POOR VS CLEAN IMPORTS
# ============================================================

"""
Poor:

    import pandas as pd
    from application.models import *
    import os
    from application.database import connect
    import sys
    import numpy as np


Problems:

    - groups are mixed
    - wildcard import
    - standard library imports are scattered


Cleaner:

    import os
    import sys

    import numpy as np
    import pandas as pd

    from application.database import connect
    from application.models import User


The second version is easier to scan and maintain.
"""


# ============================================================
# 25. IMPORTS ARE PART OF CODE ORGANIZATION
# ============================================================

"""
Import conventions are not just about appearance.

Well-organized imports help communicate:

    - module dependencies
    - project structure
    - external libraries
    - internal modules
    - naming conventions


A clean import section gives the reader a quick overview
of what the module depends on.
"""


# ============================================================
# 26. AUTOMATED TOOLS
# ============================================================

"""
Import formatting can be automated using tools such as:

    Ruff
    isort

These tools can:

    - sort imports
    - group imports
    - remove unused imports
    - enforce project conventions


Manual understanding is still important because tools enforce
rules; they do not replace understanding of import behavior.
"""


# ============================================================
# 27. CORE CONVENTION
# ============================================================

"""
A practical import structure is:

    # Standard library
    import ...

    from ... import ...

    # Third-party
    import ...

    from ... import ...

    # Local application
    import ...

    from ... import ...


Keep imports:

    - organized
    - explicit
    - consistent
    - readable
    - minimal
"""


# ============================================================
# 28. KEY TAKEAWAY
# ============================================================

"""
Good import conventions generally mean:

    1. Keep imports near the top.
    2. Group standard-library imports first.
    3. Put third-party imports second.
    4. Put local application imports last.
    5. Separate groups with blank lines.
    6. Prefer explicit imports.
    7. Avoid wildcard imports.
    8. Use recognized aliases where appropriate.
    9. Use meaningful custom aliases.
   10. Avoid unnecessary local imports.
   11. Avoid circular dependencies.
   12. Keep import statements readable.

Mental model:

    Imports
       ↓
    Dependencies
       ↓
    Organized clearly
       ↓
    Easier maintenance
"""