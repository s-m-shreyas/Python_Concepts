"""
03_import_aliases.py

Demonstrates import aliases in Python.

An import alias gives an imported module, function, class,
or other object a different local name.

The alias is created using the `as` keyword.

Examples:

    import package.module as module_alias

    from package.module import function as function_alias
"""


# ============================================================
# 1. WHAT IS AN IMPORT ALIAS?
# ============================================================

"""
An import alias is an alternative name assigned to an imported
object in the current module.

Example:

    import calculations as calc


The actual module is still:

    calculations

but its local name becomes:

    calc
"""


# ============================================================
# 2. BASIC MODULE ALIAS
# ============================================================

"""
Without an alias:

    import application.calculations

Usage:

    application.calculations.add(10, 20)


With an alias:

    import application.calculations as calc

Usage:

    calc.add(10, 20)


The alias only changes the local name used to access the
imported module.
"""


# ============================================================
# 3. WHY USE MODULE ALIASES?
# ============================================================

"""
Aliases can be useful when:

    - a module name is long
    - a shorter name improves readability
    - two modules have similar names
    - a conventional alias is widely recognized

Example:

    import application.utilities.formatting as formatting


can become:

    import application.utilities.formatting as fmt


Then:

    fmt.format_name(...)
"""


# ============================================================
# 4. ALIASING A FUNCTION
# ============================================================

"""
Functions can also be given aliases.

Example:

    from application.calculations import add as addition


Now the local name is:

    addition


Usage:

    addition(10, 20)


The original function remains named:

    add

Only the local reference is called:

    addition
"""


# ============================================================
# 5. ALIASING A CLASS
# ============================================================

"""
Classes can also be aliased.

Example:

    from application.users import User as ApplicationUser


Now:

    ApplicationUser


refers to the imported User class.

This can be useful when two imported classes have the
same name.
"""


# ============================================================
# 6. SOLVING NAMING CONFLICTS
# ============================================================

"""
Suppose two modules contain a class called User:

application/users.py:

    class User:
        ...


admin/users.py:

    class User:
        ...


Both can be imported with aliases:

    from application.users import User as ApplicationUser
    from application.admin.users import User as AdminUser


Now the names are unambiguous:

    ApplicationUser
    AdminUser
"""


# ============================================================
# 7. ALIASING TWO MODULES WITH THE SAME LOCAL NAME
# ============================================================

"""
Suppose:

application/
├── users/
│   └── formatter.py
│
└── orders/
    └── formatter.py


Both modules have the same name:

    formatter


Aliases can distinguish them:

    from application.users import formatter as user_formatter
    from application.orders import formatter as order_formatter


Now:

    user_formatter
    order_formatter


refer to different modules.
"""


# ============================================================
# 8. STANDARD LIBRARY CONVENTIONS
# ============================================================

"""
Some modules have widely recognized conventional aliases.

Example:

    import datetime as dt


Then:

    dt.datetime
    dt.date


Another common example:

    import collections.abc as cabc


The important idea is that an alias can make repeated
module references shorter.
"""


# ============================================================
# 9. THIRD-PARTY LIBRARY CONVENTIONS
# ============================================================

"""
Many Python libraries have commonly recognized aliases.

For example:

    import pandas as pd
    import numpy as np


These aliases are conventions rather than requirements.

The library is still imported under its actual package name,
but the current module uses the conventional local alias.
"""


# ============================================================
# 10. ALIAS DOES NOT RENAME THE MODULE
# ============================================================

"""
Important:

    import application.calculations as calc


does NOT rename:

    application.calculations


Python still knows the module by its actual import identity.

The alias:

    calc


is simply the local name used in the importing module.
"""


# ============================================================
# 11. ALIASING A FUNCTION DOES NOT MODIFY THE FUNCTION
# ============================================================

"""
Example:

    from application.calculations import add as addition


The function itself has not been renamed.

The local module simply has another reference to it:

    addition


The original function can still have:

    __name__ == "add"


The alias is a local binding.
"""


# ============================================================
# 12. MODULE ALIAS VS OBJECT ALIAS
# ============================================================

"""
Module alias:

    import application.calculations as calc


Object alias:

    from application.calculations import add as addition


Difference:

    calc
        -> refers to the imported module

    addition
        -> refers to the imported function
"""


# ============================================================
# 13. ALIASING WITH from ... import
# ============================================================

"""
General syntax:

    from module import object as alias


Example:

    from application.calculations import multiply as product


Then:

    product(5, 4)


The general pattern is:

    original_name
          ↓
    local_alias
"""


# ============================================================
# 14. ALIASING WITH import
# ============================================================

"""
General syntax:

    import module as alias


Example:

    import application.calculations as calc


The general pattern is:

    module
      ↓
    alias
"""


# ============================================================
# 15. ALIASING PACKAGES
# ============================================================

"""
Packages can also be imported using aliases.

Example:

    import application.utilities as utils


Then:

    utils.formatting
    utils.validation


The package is accessed through:

    utils
"""


# ============================================================
# 16. ALIASING SUBMODULES
# ============================================================

"""
Example:

    import application.users.authentication as auth


Then:

    auth.login(...)
    auth.logout(...)


The alias represents the imported module:

    application.users.authentication
"""


# ============================================================
# 17. WHEN ALIASES IMPROVE READABILITY
# ============================================================

"""
Without an alias:

    application.data_processing.transformations.clean_data(
        records
    )


With an alias:

    import application.data_processing.transformations as transforms

    transforms.clean_data(records)


A good alias can make repeated references easier to read.
"""


# ============================================================
# 18. WHEN ALIASES HURT READABILITY
# ============================================================

"""
Aliases should not be unnecessarily cryptic.

For example:

    import application.utilities.formatting as x


is technically valid but unclear.

Prefer:

    import application.utilities.formatting as fmt


The purpose of an alias is to improve readability, not
make the code harder to understand.
"""


# ============================================================
# 19. AVOID UNNECESSARY ALIASES
# ============================================================

"""
Do not create aliases just because Python allows them.

For example:

    import calculations as calculations


adds no value.

Likewise:

    from calculations import add as add


does not improve the code.

Use aliases when they solve an actual readability,
naming, or convention problem.
"""


# ============================================================
# 20. ALIASES AND NAME COLLISIONS
# ============================================================

"""
Suppose:

    from application.users import User
    from application.admin import User


The second import would replace the local name User.

Aliases avoid this:

    from application.users import User as UserAccount
    from application.admin import User as AdminUser


Now both objects have distinct local names.
"""


# ============================================================
# 21. ALIAS MENTAL MODEL
# ============================================================

"""
Think of:

    import application.calculations as calc


as:

    imported object
          ↓
    local reference
          ↓
        calc


The alias belongs to the importing module.

It does not change the original module or object.
"""


# ============================================================
# 22. COMMON ALIAS PATTERNS
# ============================================================

"""
Common patterns include:

    import pandas as pd
    import numpy as np
    import datetime as dt

and:

    import application.utilities as utils
    import application.formatting as fmt


For functions/classes:

    from application.users import User as UserAccount
    from application.calculations import add as addition
"""


# ============================================================
# 23. KEY TAKEAWAY
# ============================================================

"""
Import aliases use:

    as


Two main forms:

    import module as alias

    from module import object as alias


Examples:

    import application.calculations as calc

    from application.calculations import add as addition


Aliases are useful for:

    - shortening long names
    - resolving naming conflicts
    - following established conventions
    - improving readability

Important:

    Alias
        -> local name

    Original module/object
        -> remains unchanged
"""