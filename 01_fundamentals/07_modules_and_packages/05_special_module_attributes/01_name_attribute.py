"""
01_name_attribute.py

Demonstrates the special __name__ attribute of a Python module.

Every Python module has a built-in __name__ attribute that
identifies how the module is being used.

The value of __name__ depends on how the module is executed
or imported.
"""


# ============================================================
# 1. WHAT IS __name__?
# ============================================================

"""
__name__ is a special attribute automatically provided by
Python for every module.

Example:

    print(__name__)


The value tells us the name under which the current module
is being used.
"""


# ============================================================
# 2. MODULE EXECUTED DIRECTLY
# ============================================================

"""
Suppose we have:

example.py


and execute:

    python example.py


Then:

    __name__

has the value:

    "__main__"


So:

    print(__name__)

produces:

    __main__
"""


# ============================================================
# 3. MODULE IMPORTED
# ============================================================

"""
Suppose:

example.py:

    print(__name__)


main.py:

    import example


When main.py is executed, example.py is imported.

Inside example.py:

    __name__

will contain:

    "example"


rather than:

    "__main__"


The module is being used as an imported module rather than
as the directly executed program.
"""


# ============================================================
# 4. DIRECT EXECUTION VS IMPORT
# ============================================================

"""
The same file can therefore have different __name__ values.

Direct execution:

    python example.py

Result:

    __name__ == "__main__"


Imported:

    import example

Result inside example.py:

    __name__ == "example"


This distinction is fundamental to understanding the
main guard.
"""


# ============================================================
# 5. SIMPLE EXAMPLE
# ============================================================

"""
Example module:

calculator.py:

    print(__name__)


If executed directly:

    python calculator.py

Output:

    __main__


If imported:

    import calculator

Output:

    calculator
"""


# ============================================================
# 6. __name__ IS A MODULE ATTRIBUTE
# ============================================================

"""
__name__ belongs to the module namespace.

Example:

    print(__name__)


Python has already created this attribute for the module.

Other special module attributes include:

    __file__
    __package__
    __spec__

These attributes provide information about the module.
"""


# ============================================================
# 7. __name__ WITH PACKAGES
# ============================================================

"""
Consider:

application/
├── __init__.py
└── calculations.py


If calculations.py is imported as:

    import application.calculations


then inside calculations.py:

    __name__

will be:

    "application.calculations"


The package hierarchy becomes part of the module name.
"""


# ============================================================
# 8. __name__ WITH SUBPACKAGES
# ============================================================

"""
Consider:

application/
└── users/
    ├── __init__.py
    └── profile.py


If profile.py is imported as:

    import application.users.profile


then:

    __name__

inside profile.py becomes:

    "application.users.profile"
"""


# ============================================================
# 9. __name__ IDENTIFIES THE CURRENT MODULE
# ============================================================

"""
Think of __name__ as the module's current import identity.

Example:

    application.users.profile


The module's:

    __name__

is:

    "application.users.profile"


When that same module is executed directly, Python assigns:

    "__main__"

to __name__.
"""


# ============================================================
# 10. WHY "__main__"?
# ============================================================

"""
Python uses the special name:

    "__main__"

for the module that is being used as the program's
top-level entry point.

Therefore:

    __name__ == "__main__"


means:

    "This module is currently being executed as the
     main program."


It does NOT mean that the file is literally named:

    main.py
"""


# ============================================================
# 11. __name__ DOES NOT MEAN FILE NAME
# ============================================================

"""
A common misconception is:

    __name__ == filename


Not always.

If:

    calculator.py


is executed directly:

    __name__ == "__main__"


If imported:

    __name__ == "calculator"


Therefore __name__ represents the module's execution/import
identity, not simply its filename.
"""


# ============================================================
# 12. __name__ AND MODULE IMPORTS
# ============================================================

"""
Suppose:

project/
├── main.py
└── calculator.py


calculator.py:

    print(__name__)


main.py:

    import calculator


Execution:

    python main.py


Output from calculator.py:

    calculator


Because calculator.py was imported.
"""


# ============================================================
# 13. DIRECT EXECUTION OF THE SAME MODULE
# ============================================================

"""
Now execute:

    python calculator.py


The same statement:

    print(__name__)


produces:

    __main__


So:

    imported module
        -> __name__ = module name

    directly executed module
        -> __name__ = "__main__"
"""


# ============================================================
# 14. PRACTICAL INSPECTION
# ============================================================

"""
The simplest way to inspect __name__ is:

    print(__name__)


A module can therefore reveal whether it is currently being
executed directly or imported.
"""


# ============================================================
# 15. RELATIONSHIP WITH THE MAIN GUARD
# ============================================================

"""
The most common use of __name__ is:

    if __name__ == "__main__":
        ...


This is called the main guard.

It allows a module to behave differently when:

    executed directly

versus:

    imported by another module


The next file explores this pattern in detail.
"""


# ============================================================
# 16. IMPORTANT MENTAL MODEL
# ============================================================

"""
Think of Python choosing a special identity for the module
that starts the program.

Starting module:

    __name__ = "__main__"


Imported module:

    __name__ = its importable module name


Example:

    python main.py

main.py:

    __name__ = "__main__"


If main.py imports:

    calculator


then calculator.py:

    __name__ = "calculator"
"""


# ============================================================
# 17. KEY TAKEAWAY
# ============================================================

"""
__name__ is a special module attribute.

When executed directly:

    __name__ == "__main__"


When imported:

    __name__ == module's import name


Examples:

    calculator.py
        ↓
    direct execution
        ↓
    "__main__"


    import calculator
        ↓
    calculator.py
        ↓
    "calculator"


Core purpose:

    __name__ allows a module to know whether it is being
    executed directly or imported.

Next concept:

    if __name__ == "__main__":
"""