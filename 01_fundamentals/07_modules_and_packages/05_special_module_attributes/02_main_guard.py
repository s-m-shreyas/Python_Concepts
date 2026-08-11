"""
02_main_guard.py

Demonstrates the main guard:

    if __name__ == "__main__":

The main guard allows a module to distinguish between:

    1. Being executed directly.
    2. Being imported by another module.

This is one of the most common patterns in Python modules.
"""


# ============================================================
# 1. BASIC MAIN GUARD
# ============================================================

"""
Basic syntax:

    if __name__ == "__main__":
        ...


When this module is executed directly:

    __name__ == "__main__"

so the code inside the guard runs.

When this module is imported:

    __name__ != "__main__"

so the code inside the guard does not run.
"""


# ============================================================
# 2. SIMPLE EXAMPLE
# ============================================================

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Python"))


"""
If this file is executed directly:

    python 02_main_guard.py

the output is:

    Hello, Python!


If this module is imported by another module:

    import 02_main_guard


the guarded code does not execute.

Note:

Python module names normally cannot begin with a number
when imported using normal import syntax, so in a real
project this file would typically have a name such as:

    main_guard.py
"""


# ============================================================
# 3. WHY USE THE MAIN GUARD?
# ============================================================

"""
Without a main guard:

    print("Program started")


the statement executes whenever the module is imported.

With a main guard:

    if __name__ == "__main__":
        print("Program started")


the statement executes only when the module is run directly.
"""


# ============================================================
# 4. MODULE WITH REUSABLE CODE
# ============================================================

"""
A module can contain reusable definitions:

    functions
    classes
    constants

and also contain code intended to run only when the module
is executed directly.

Example:

    def add(first: int, second: int) -> int:
        return first + second


    def subtract(first: int, second: int) -> int:
        return first - second


    if __name__ == "__main__":
        print(add(10, 20))
        print(subtract(20, 10))


The functions are available to importers.

The demonstration code runs only during direct execution.
"""


# ============================================================
# 5. DIRECT EXECUTION
# ============================================================

"""
Suppose:

calculator.py

contains:

    def add(first: int, second: int) -> int:
        return first + second


    if __name__ == "__main__":
        print(add(10, 20))


Running:

    python calculator.py


causes:

    __name__ == "__main__"


Therefore the print statement executes.
"""


# ============================================================
# 6. IMPORTING THE MODULE
# ============================================================

"""
Suppose:

calculator.py

contains:

    def add(first: int, second: int) -> int:
        return first + second


    if __name__ == "__main__":
        print(add(10, 20))


Another module:

main.py

contains:

    import calculator


During this import:

    calculator.__name__ == "calculator"


Therefore:

    calculator.__name__ == "__main__"

is False.

The guarded print statement does not execute.
"""


# ============================================================
# 7. MAIN GUARD PROTECTS EXECUTION CODE
# ============================================================

"""
The main guard is primarily used to separate:

    reusable definitions

from:

    direct-execution behavior


Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        return price * quantity


    if __name__ == "__main__":
        total = calculate_total(100.0, 3)
        print(total)


The function can be imported without running the example
calculation automatically.
"""


# ============================================================
# 8. MAIN GUARD WITH MULTIPLE STATEMENTS
# ============================================================

"""
The guard can contain multiple statements.

Example:

    if __name__ == "__main__":
        result = greet("Alice")
        print(result)

        result = greet("Bob")
        print(result)


All statements execute only when the module is the
directly executed module.
"""


# ============================================================
# 9. MAIN GUARD WITH A MAIN FUNCTION
# ============================================================

"""
A common pattern is to define a main() function.

Example:

    def main() -> None:
        print("Application started")


    if __name__ == "__main__":
        main()


This separates the program's entry-point logic from the
module's reusable definitions.
"""


# ============================================================
# 10. WHY DEFINE main()?
# ============================================================

"""
Using a main() function can make the structure clearer.

Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        return price * quantity


    def main() -> None:
        total = calculate_total(100.0, 3)
        print(total)


    if __name__ == "__main__":
        main()


Now the module has a clear structure:

    reusable functions
            ↓
        main()
            ↓
      main guard
"""


# ============================================================
# 11. MAIN GUARD IS NOT A FUNCTION
# ============================================================

"""
This:

    if __name__ == "__main__":
        ...


is a conditional statement.

It is not:

    a special function
    a special keyword
    a function call


Python simply evaluates whether:

    __name__

equals:

    "__main__"
"""


# ============================================================
# 12. MAIN GUARD AND IMPORTS
# ============================================================

"""
The main guard does not prevent the entire module from being
loaded.

When a module is imported, Python still executes the module's
top-level code.

The difference is that the condition:

    __name__ == "__main__"

is false for an imported module.

Therefore code inside the guard is skipped.
"""


# ============================================================
# 13. CODE OUTSIDE VS INSIDE THE GUARD
# ============================================================

"""
Example:

    print("Module loaded")


    if __name__ == "__main__":
        print("Program executed directly")


If directly executed:

    Module loaded
    Program executed directly


If imported:

    Module loaded


The first print is outside the guard.

The second print is protected by the guard.
"""


# ============================================================
# 14. COMMON USE CASE: DEMONSTRATION CODE
# ============================================================

"""
A module can contain reusable functionality and a small
demonstration section.

Example:

    def square(number: int) -> int:
        return number * number


    if __name__ == "__main__":
        print(square(5))


This allows the module to be:

    imported as reusable code

or:

    executed as a small demonstration.
"""


# ============================================================
# 15. COMMON USE CASE: SCRIPT ENTRY POINT
# ============================================================

"""
The main guard is also commonly used for scripts.

Example:

    def main() -> None:
        print("Starting data processing...")
        ...


    if __name__ == "__main__":
        main()


This gives the file a clear executable entry point.
"""


# ============================================================
# 16. MAIN GUARD IN A PACKAGE
# ============================================================

"""
Consider:

project/
│
├── main.py
│
└── application/
    ├── __init__.py
    └── calculations.py


calculations.py can contain:

    def add(first: int, second: int) -> int:
        return first + second


    if __name__ == "__main__":
        print(add(10, 20))


The same module can therefore be imported by:

    main.py

without automatically running its demonstration code.
"""


# ============================================================
# 17. MAIN GUARD AND TESTING
# ============================================================

"""
The main guard can also be useful for small manual tests.

Example:

    def multiply(first: int, second: int) -> int:
        return first * second


    if __name__ == "__main__":
        assert multiply(5, 4) == 20


The test runs when the file is executed directly.

When imported, the assertion is not executed.
"""


# ============================================================
# 18. COMMON MISTAKE
# ============================================================

"""
Incorrect:

    if __name__ = "__main__":
        ...


Correct:

    if __name__ == "__main__":
        ...


Use:

    ==

because we are comparing values.

We are not assigning a value.
"""


# ============================================================
# 19. COMMON MISTAKE: WRONG STRING
# ============================================================

"""
Correct:

    if __name__ == "__main__":
        ...


Not:

    if __name__ == "__main":
        ...


The value is exactly:

    "__main__"

including both pairs of underscores.
"""


# ============================================================
# 20. COMMON MISTAKE: GUARDING DEFINITIONS
# ============================================================

"""
Usually, reusable definitions should NOT be placed inside
the main guard.

Avoid:

    if __name__ == "__main__":
        def add(first: int, second: int) -> int:
            return first + second


This prevents the function from being created when the module
is imported.

Prefer:

    def add(first: int, second: int) -> int:
        return first + second


    if __name__ == "__main__":
        print(add(10, 20))


Definitions remain available to importers.
"""


# ============================================================
# 21. MAIN GUARD MENTAL MODEL
# ============================================================

"""
Think of the main guard as a gate:

                __name__
                    ↓
          Is it "__main__"?
             ↙           ↘
           YES            NO
            ↓              ↓
        run code       skip code


Direct execution:

    YES


Import:

    NO
"""


# ============================================================
# 22. STANDARD PATTERN
# ============================================================

"""
A clean executable module often follows this structure:

    constants


    reusable functions


    reusable classes


    def main() -> None:
        ...


    if __name__ == "__main__":
        main()


This pattern separates reusable code from direct execution.
"""


# ============================================================
# 23. KEY TAKEAWAY
# ============================================================

"""
Main guard:

    if __name__ == "__main__":
        ...


Purpose:

    Run specific code only when the module is executed
    directly.

Direct execution:

    __name__ == "__main__"
        ↓
    guarded code runs


Import:

    __name__ == module name
        ↓
    guarded code does not run


Common pattern:

    def main() -> None:
        ...


    if __name__ == "__main__":
        main()


Core idea:

    __name__
        ↓
    execution context
        ↓
    main guard
        ↓
    controlled execution
"""