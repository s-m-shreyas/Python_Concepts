
# Python Concepts — Style Guide

This document defines the coding, naming, documentation, and example-design conventions used throughout the Python Concepts repository.

The goal is to keep the repository:

- Consistent
- Readable
- Beginner-friendly
- Technically accurate
- Copy-paste ready
- Static-type-checker friendly
- Easy to maintain
- Suitable for long-term revision


# 1. Core Principles

Every example should prioritize:

1. Conceptual clarity
2. Correct Python behaviour
3. Readability
4. Simplicity
5. Consistency
6. Appropriate type annotations
7. Easy execution
8. Focused learning

The code should teach the concept rather than demonstrate unnecessary complexity.

Prefer:

    clear code
        ↓
    understandable logic
        ↓
    correct behaviour

over:

    clever code
        ↓
    unnecessary abstraction
        ↓
    harder learning


# 2. One Primary Concept Per File

Each Python file should have one clear primary learning objective.

For example:

    03_positional_arguments.py

should primarily teach positional arguments.

Related concepts may be used when necessary to explain the target concept, but unrelated concepts should not be introduced simply to make the example more sophisticated.

A reader should be able to answer:

    "What is this file teaching me?"

without ambiguity.


# 3. File Naming

Python files should use:

- Lowercase names
- `snake_case`
- Descriptive names
- Numeric prefixes where the folder uses ordered concepts

Preferred:

    01_function_basics.py
    02_positional_arguments.py
    03_keyword_arguments.py

Avoid:

    FunctionBasics.py
    functionBasics.py
    example1.py
    test.py


# 4. Folder Naming

Folders should use:

- Numeric prefixes for learning order
- Lowercase names
- `snake_case`
- Descriptive names

Preferred:

    01_fundamentals/
    02_oops/
    03_advanced/
    04_algorithms/
    05_libraries_and_modules/

And:

    02_module_search_and_resolution/


# 5. Ordering

Numeric prefixes should represent conceptual progression.

For example:

    01_function_basics.py
    02_function_parameters.py
    03_positional_arguments.py
    04_keyword_arguments.py

The numbering should generally follow the recommended learning sequence.

Numbers should not be changed casually after content has been established.


# 6. Variables

Use descriptive `snake_case` variable names.

Preferred:

    student_name = "Shreyas"
    total_marks = 450
    employee_count = 10

Avoid:

    x = "Shreyas"
    tm = 450
    ec = 10

Short names are acceptable when the meaning is obvious from the context.

For example:

    i
    j
    n

may be appropriate for simple loop or algorithm examples.


# 7. Constants

Constants should use uppercase `UPPER_SNAKE_CASE`.

Example:

    MAX_RETRIES = 3
    DEFAULT_TIMEOUT = 30
    PI = 3.14159

Python does not enforce constants at runtime.

The naming convention communicates the intended usage.


# 8. Functions

Functions should use `snake_case`.

Example:

    def calculate_total(price: float, quantity: int) -> float:
        return price * quantity

Function names should describe actions or behaviour.

Preferred:

    calculate_total()
    validate_age()
    convert_temperature()

Avoid vague names such as:

    do_it()
    process()
    thing()


# 9. Classes

Classes should use `PascalCase`.

Example:

    class Employee:
        pass

    class BankAccount:
        pass

    class DataProcessor:
        pass

Avoid:

    class employee:
        pass

    class bank_account:
        pass


# 10. Methods

Methods should use `snake_case`.

Example:

    class Employee:

        def calculate_salary(self) -> float:
            return 50000.0

Methods should generally describe an action or behaviour.


# 11. `self` and `cls`

Use the conventional names:

    self

for instance methods.

Use:

    cls

for class methods.

Example:

    class Employee:

        company_name = "Example"

        def __init__(self, name: str) -> None:
            self.name = name

        @classmethod
        def from_company(cls, name: str) -> "Employee":
            return cls(name)


# 12. Type Annotations

Type annotations should be used where they improve clarity and are appropriate for the concept being demonstrated.

Example:

    name: str = "Shreyas"
    age: int = 30

Function annotations should normally include both parameter and return types.

Example:

    def add(first: int, second: int) -> int:
        return first + second


# 13. Type Hinting Philosophy

Type annotations should support learning rather than distract from it.

Avoid unnecessarily complicated typing in beginner examples.

Prefer:

    def greet(name: str) -> str:
        return f"Hello, {name}"

over introducing advanced typing constructs when they are not relevant to the concept.

Advanced typing concepts should be introduced in their appropriate learning area.


# 14. Static Type Checker Compatibility

Examples should be written with common static type checkers in mind.

The repository should avoid unnecessary warnings from:

- Pyright
- Pylance
- Mypy

Avoid:

- Incompatible annotations
- Unnecessary casts
- Unreachable conditions
- Literal narrowing problems
- Variable redefinition warnings
- Incorrect return types
- Unused or invalid type annotations

When a static type checker cannot infer something that is obvious from the intended teaching example, use the simplest appropriate solution.

If `typing.cast()` is genuinely necessary, include a beginner-friendly comment explaining why it is being used.


# 15. Non-Interactive Examples

Examples should normally be non-interactive.

Avoid `input()` unless interactive input is specifically the concept being demonstrated.

Preferred:

    age = 30

rather than:

    age = int(input("Enter your age: "))

This allows examples to be:

- Copy-pasted
- Executed immediately
- Tested automatically
- Used in documentation
- Used in demonstrations


# 16. Deterministic Examples

Examples should generally produce predictable output.

Avoid unnecessary:

- Random values
- Current timestamps
- External API calls
- Network dependencies
- User interaction
- Environment-specific behaviour

unless those behaviours are the actual subject being demonstrated.


# 17. Imports

Imports should normally appear at the top of the file.

Example:

    from typing import Final

    MAX_USERS: Final = 100

Avoid unnecessary imports.

Do not import a library merely to demonstrate a concept that can be explained using the standard language.


# 18. Import Ordering

When multiple imports exist, generally organize them as:

    1. Standard library imports
    2. Third-party imports
    3. Local imports

Example:

    import os
    import sys

    import pandas as pd

    from project.utils import helper


# 19. Comments

Comments should explain intent, behaviour, or an important Python rule.

Good:

    # Positional arguments are matched to parameters by order.

Avoid comments that merely repeat the code.

Weak:

    # Add two numbers
    total = first + second

Better:

    # The arguments are matched to parameters according to their position.
    total = add(10, 20)


# 20. Teaching Comments

Teaching examples may contain more comments than production code.

Comments may explain:

- Why something works
- Why something fails
- Important Python rules
- Expected output
- Edge cases
- Common mistakes

However, comments should not explain every obvious line.


# 21. Docstrings

Use docstrings when they provide meaningful documentation.

Example:

    def calculate_area(radius: float) -> float:
        """Return the area of a circle."""
        return 3.14159 * radius ** 2

Docstrings should be concise and relevant to the concept.


# 22. Output Demonstrations

When output is important to understanding the concept, use explicit `print()` statements.

Example:

    result = add(10, 20)

    print(result)

Expected output:

    30

Do not rely on a user manually inspecting internal variables.


# 23. Expected Output

Expected output may be included in comments when it helps explain the example.

Example:

    print(employee.name)

    # Output:
    # Shreyas

Keep expected output accurate.


# 24. Example Data

Use simple, meaningful example data.

Preferred:

    employee_name = "Shreyas"
    employee_age = 30

    products = ["Laptop", "Mouse", "Keyboard"]

Avoid unnecessarily large datasets when demonstrating a basic concept.


# 25. Edge Cases

Important edge cases should be demonstrated where they improve conceptual understanding.

Examples include:

- Empty collections
- Zero values
- Negative values
- Duplicate values
- Missing keys
- Boundary conditions
- Invalid input

Do not add artificial edge cases merely to increase file length.


# 26. Errors and Exceptions

When demonstrating an error, make the error intentional and clearly explain it.

For example, when teaching `TypeError`, the example should make it obvious:

    # This operation is invalid because Python does not add
    # a string and an integer directly.
    result = "10" + 5

If an intentionally failing example is included, it should be clearly identified so the reader does not mistake it for broken repository code.


# 27. Demonstrating Alternative Syntax

When Python provides multiple valid ways to perform an operation, explain the distinction rather than presenting alternatives randomly.

For example:

    # Positional arguments
    greet("Shreyas", 30)

    # Keyword arguments
    greet(name="Shreyas", age=30)

The purpose should be to demonstrate the difference between the two approaches.


# 28. Avoid Unnecessary Abstraction

Beginner examples should not introduce abstractions that are unrelated to the concept.

Avoid creating:

- Unnecessary helper classes
- Excessive functions
- Complex inheritance
- Frameworks
- External dependencies

unless they are directly relevant to the concept being taught.


# 29. Preserve the Conceptual Scenario

Do not change an example's intended scenario merely to make the implementation shorter.

If the example is intended to demonstrate a particular Python behaviour, preserve that behaviour.

The goal is:

    Conceptual accuracy
        >
    Artificial simplification


# 30. Production Quality vs Teaching Clarity

The repository aims for production-quality correctness while remaining educational.

This means:

    Correct Python
        +
    Clear structure
        +
    Beginner-friendly explanation

The code does not need to imitate a large production application when doing so would obscure the concept.


# 31. Comprehensions

Comprehensions are treated as an Advanced Python topic.

Examples should clearly distinguish them from ordinary loops.

For example:

    squares = [number ** 2 for number in numbers]

should be explained in relation to the equivalent loop when useful.

Do not introduce unnecessarily complex comprehensions simply because they are possible.

Readability should remain the priority.


# 32. OOP Examples

OOP examples should clearly distinguish:

- Class attributes
- Instance attributes
- Instance methods
- Class methods
- Static methods
- Inheritance
- Composition
- Polymorphism
- Encapsulation
- Abstraction

Examples should avoid mixing several unrelated OOP concepts unless the combination is itself the teaching objective.


# 33. Algorithm Examples

Algorithm implementations should prioritize understanding of the algorithm.

Each implementation should make clear:

- Input
- Output
- Core logic
- Important steps
- Complexity where relevant

Avoid hiding the algorithm behind built-in functionality when the purpose is to learn the algorithm itself.

For example, a sorting algorithm implementation should not simply call:

    sorted()

when the objective is to understand the sorting algorithm.


# 34. Library Examples

Library examples may use external dependencies when the library itself is the subject.

Examples should:

- Identify the required library
- Use clear imports
- Keep the example focused
- Avoid unnecessary complexity
- Explain important library-specific behaviour


# 35. README Files

Each major topic folder should contain a `README.md`.

A topic README should generally explain:

- What the topic is
- Why it matters
- Important concepts
- Learning order
- Relationship between the example files
- Important rules
- Common mistakes where relevant

The README should complement the Python examples rather than duplicate every line of code.


# 36. Project-Level Documentation

The repository uses the following documentation files:

    README.md
    ARCHITECTURE.md
    ROADMAP.md
    STYLE_GUIDE.md
    folder_tree.txt

Each document should have a distinct responsibility.

`README.md`

    What the repository is.

`ARCHITECTURE.md`

    How the repository is organized and why.

`ROADMAP.md`

    What has been completed and what comes next.

`STYLE_GUIDE.md`

    How code and documentation should be written.

`folder_tree.txt`

    Quick structural reference.


# 37. Markdown Formatting

Markdown files should use:

- Clear headings
- Consistent heading levels
- Bullet lists
- Numbered lists when order matters
- Code blocks for code
- Tables only when they improve readability

Avoid excessive formatting.


# 38. Code Formatting

Use standard Python formatting conventions.

Preferred:

    def calculate_total(price: float, quantity: int) -> float:
        return price * quantity

Avoid overly compressed code:

    def calculate_total(p,q):return p*q


# 39. Line Length

Keep lines reasonably short and readable.

When a line becomes difficult to read, restructure it rather than allowing excessive horizontal length.

Clarity is more important than enforcing an arbitrary line length in teaching examples.


# 40. Whitespace

Use blank lines to separate logical sections.

Example:

    employee_name = "Shreyas"
    employee_age = 30


    def display_employee() -> None:
        print(employee_name)
        print(employee_age)

Avoid excessive blank lines or tightly packed unrelated code.


# 41. Naming Consistency

Once a naming convention has been established for a concept, keep it consistent across related files.

For example, if an example uses:

    employee_name

do not switch between:

    employee_name
    emp_name
    name_of_employee

without a conceptual reason.


# 42. No Unnecessary Cleverness

The repository is intended for learning.

Avoid code that is technically impressive but conceptually distracting.

Prefer:

    explicit
    readable
    understandable

over:

    clever
    compressed
    obscure


# 43. Repository Cleanliness

Generated files should not be committed.

Examples include:

    __pycache__/
    *.pyc
    *.pyo
    .venv/
    venv/
    .mypy_cache/
    .pyright/
    .ruff_cache/

These are handled through `.gitignore`.

IDE-specific files and operating-system-generated files should also remain outside the repository unless there is a specific reason to include them.


# 44. Dependencies

Avoid adding dependencies unless they are required for the concept being demonstrated.

Fundamental Python examples should generally use Python's built-in functionality.

Third-party dependencies belong primarily in:

    05_libraries_and_modules/


# 45. Version Target

The repository targets:

    Python 3.12+

Examples should therefore use Python features supported by the target version.

If a newer Python feature is used, the example should clearly identify the relevant version requirement when necessary.


# 46. Testing Examples

Every example should be executed at least once before being considered complete.

Where appropriate, examples should also be checked for:

- Syntax errors
- Runtime errors
- Incorrect output
- Type-checking issues
- Import issues


# 47. Git Practices

Commits should describe the change clearly.

Preferred:

    feat: add list comprehension examples
    fix: correct merge sort recursion
    docs: update advanced roadmap
    chore: clean repository

Avoid vague commit messages such as:

    update
    changes
    stuff
    final


# 48. Documentation and Code Must Agree

The README, roadmap, architecture documentation, and actual repository structure should remain consistent.

If the structure changes:

    Code structure
        ↓
    folder_tree.txt
        ↓
    ARCHITECTURE.md
        ↓
    ROADMAP.md

should be reviewed for consistency.


# 49. Definition of a Good Example

A good example should answer three questions:

    What is this?

    How does it work?

    Why does it behave this way?

The reader should be able to run the file and connect the output to the concept being explained.


# 50. Final Principle

The repository is a learning system.

Therefore:

    Correctness > cleverness

    Clarity > brevity

    Understanding > abstraction

    Consistency > convenience

    Conceptual accuracy > unnecessary simplification

Every file should contribute to building a stronger mental model of Python.

