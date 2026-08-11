"""
03_file_attribute.py

Demonstrates the special __file__ attribute of a Python module.

__file__ contains the path associated with the module's source
file when the module has a file-based representation.

This attribute is useful when a module needs to determine the
location of its own file or files relative to it.
"""


# ============================================================
# 1. WHAT IS __file__?
# ============================================================

"""
__file__ is a special module attribute.

It represents the path of the current module's file.

Example:

    print(__file__)


If the module is located at:

    project/application/calculations.py


__file__ will contain a path referring to:

    calculations.py
"""


# ============================================================
# 2. SIMPLE INSPECTION
# ============================================================

"""
The simplest way to inspect __file__ is:

    print(__file__)


The exact value depends on:

    - where the module is located
    - how Python was started
    - the execution environment


Therefore, do not assume that __file__ will always have
one specific absolute path format.
"""


# ============================================================
# 3. __file__ IS A STRING
# ============================================================

"""
The __file__ attribute normally contains a string-like path
representation.

Example:

    print(type(__file__))


In a normal file-based Python module, the result is generally:

    <class 'str'>
"""


# ============================================================
# 4. __file__ AND THE MODULE LOCATION
# ============================================================

"""
Consider:

project/
│
├── main.py
│
└── application/
    └── calculations.py


Inside calculations.py:

    print(__file__)


The value identifies the file associated with:

    application/calculations.py
"""


# ============================================================
# 5. __file__ VS __name__
# ============================================================

"""
These two special attributes provide different information.

__name__

    identifies the module's execution/import name.


__file__

    identifies the path associated with the module's file.


Example:

    __name__
        -> "application.calculations"


    __file__
        -> path to calculations.py


Mental model:

    __name__
        = "Who am I?"


    __file__
        = "Where is my file?"
"""


# ============================================================
# 6. CONVERTING __file__ TO A Path OBJECT
# ============================================================

"""
The pathlib module can be used to work with __file__.

Example:

    from pathlib import Path

    file_path = Path(__file__)


Now:

    file_path

represents the module's file path as a Path object.

This is usually more convenient than manually manipulating
path strings.
"""


# ============================================================
# 7. GETTING THE FILE NAME
# ============================================================

"""
Example:

    from pathlib import Path

    file_path = Path(__file__)

    print(file_path.name)


If the file is:

    calculations.py


then:

    file_path.name

produces:

    calculations.py
"""


# ============================================================
# 8. GETTING THE FILE SUFFIX
# ============================================================

"""
Example:

    from pathlib import Path

    file_path = Path(__file__)

    print(file_path.suffix)


For:

    calculations.py


the result is:

    .py
"""


# ============================================================
# 9. GETTING THE PARENT DIRECTORY
# ============================================================

"""
Example:

    from pathlib import Path

    file_path = Path(__file__)

    print(file_path.parent)


If:

    __file__

refers to:

    project/application/calculations.py


then:

    file_path.parent

refers to:

    project/application
"""


# ============================================================
# 10. GETTING THE ABSOLUTE PATH
# ============================================================

"""
A Path object can be resolved:

    from pathlib import Path

    file_path = Path(__file__).resolve()


resolve() produces an absolute, normalized path representation
in typical filesystem environments.

This can be useful when the original __file__ value is relative.
"""


# ============================================================
# 11. __file__ AND CURRENT WORKING DIRECTORY
# ============================================================

"""
Important distinction:

    __file__

and:

    current working directory


are not necessarily the same location.

Example:

    project/
    ├── main.py
    └── application/
        └── data.txt


If main.py is executed while the current working directory
is project/, then:

    Path.cwd()

refers to:

    project/


But:

    Path(__file__).resolve().parent

refers to:

    the directory containing main.py


These concepts should not be confused.
"""


# ============================================================
# 12. USING __file__ FOR RELATIVE RESOURCES
# ============================================================

"""
Suppose:

application/
├── loader.py
└── data/
    └── records.txt


loader.py can locate records.txt relative to itself:

    from pathlib import Path

    module_directory = Path(__file__).resolve().parent
    data_file = module_directory / "data" / "records.txt"


This means the resource path is based on the module's location
rather than the process's current working directory.
"""


# ============================================================
# 13. WHY THIS IS USEFUL
# ============================================================

"""
Using __file__ can help when code needs to locate resources
that belong to the module.

Examples:

    configuration files
    templates
    static resources
    bundled data files
    package-specific files


The important idea is:

    locate the resource relative to the module
"""


# ============================================================
# 14. __file__ WITH PACKAGES
# ============================================================

"""
Consider:

application/
├── __init__.py
├── config.py
└── data/
    └── settings.json


Inside config.py:

    from pathlib import Path

    module_directory = Path(__file__).resolve().parent
    settings_file = module_directory / "data" / "settings.json"


The path is constructed relative to config.py.

This avoids depending on where the program was launched from.
"""


# ============================================================
# 15. __file__ IS NOT ALWAYS AVAILABLE
# ============================================================

"""
Do not assume that __file__ exists in every Python execution
environment.

For example, interactive environments such as some REPLs or
notebook environments may not provide a normal __file__
attribute.

Therefore code that depends on __file__ should only use it
when running in an environment where the module has a
file-based location.
"""


# ============================================================
# 16. __file__ CAN BE RELATIVE
# ============================================================

"""
The exact form of __file__ can depend on how the module was
loaded.

It may represent:

    a relative path

or:

    an absolute path


Therefore, when an absolute filesystem location is required,
a common pattern is:

    from pathlib import Path

    file_path = Path(__file__).resolve()


This normalizes the path for filesystem operations.
"""


# ============================================================
# 17. __file__ VS Path.cwd()
# ============================================================

"""
Compare:

    Path(__file__).resolve().parent


with:

    Path.cwd()


They answer different questions.

Path(__file__).resolve().parent:

    "Where is this module located?"


Path.cwd():

    "What directory is the process currently running from?"


Example:

project/
├── main.py
└── application/
    └── loader.py


If main.py imports loader.py:

    Path(__file__).resolve().parent

inside loader.py points to:

    project/application


while:

    Path.cwd()

depends on where the process was started.
"""


# ============================================================
# 18. COMMON PATH PATTERN
# ============================================================

"""
A common pattern is:

    from pathlib import Path


    BASE_DIR = Path(__file__).resolve().parent


Then:

    config_file = BASE_DIR / "config.json"


The / operator combines Path objects into a new path.

This is preferable to manually concatenating strings.
"""


# ============================================================
# 19. __file__ AND RESOURCE PATHS
# ============================================================

"""
For a module:

    application/config/loader.py


we can determine its directory:

    from pathlib import Path

    module_directory = Path(__file__).resolve().parent


Then construct paths relative to it:

    schema_file = module_directory / "schema.json"


This creates a location independent of the process's
current working directory.
"""


# ============================================================
# 20. COMMON MISUNDERSTANDING
# ============================================================

"""
Do not assume:

    __file__

means:

    current working directory


It does not.

It identifies the module file.

The current working directory is represented separately,
for example by:

    Path.cwd()
"""


# ============================================================
# 21. COMMON MISUNDERSTANDING
# ============================================================

"""
Do not assume:

    __file__

is always an absolute path.

Its exact representation can depend on the execution and
loading environment.

Use:

    Path(__file__).resolve()

when your code needs a resolved filesystem path.
"""


# ============================================================
# 22. RELATIONSHIP WITH OTHER SPECIAL ATTRIBUTES
# ============================================================

"""
Python modules can contain several special attributes.

Examples:

    __name__
    __file__
    __package__
    __spec__


Their purposes differ:

    __name__
        -> module identity


    __file__
        -> module file location


    __package__
        -> package context


    __spec__
        -> import specification


Together, these attributes provide information about how
Python is treating the current module.
"""


# ============================================================
# 23. PRACTICAL EXAMPLE
# ============================================================

"""
Example:

project/
└── application/
    ├── loader.py
    └── data/
        └── records.txt


loader.py:

    from pathlib import Path


    BASE_DIR = Path(__file__).resolve().parent
    DATA_FILE = BASE_DIR / "data" / "records.txt"


Now DATA_FILE points to the records file relative to
loader.py.

The code does not depend on the process being started
from the application directory.
"""


# ============================================================
# 24. MAIN GUARD + __file__
# ============================================================

"""
These two concepts can appear together:

    from pathlib import Path


    def main() -> None:
        file_path = Path(__file__).resolve()
        print(file_path)


    if __name__ == "__main__":
        main()


Here:

    __name__

controls direct execution.

    __file__

provides the module's file location.
"""


# ============================================================
# 25. __file__ MENTAL MODEL
# ============================================================

"""
Think of:

    __file__


as the module asking:

    "Where is my source file?"


Then:

    Path(__file__).resolve()


can be thought of as:

    "Give me the resolved filesystem path of my source file."


And:

    Path(__file__).resolve().parent


means:

    "Give me the directory containing my source file."
"""

print(f'path->{__file__}')
# ============================================================
# 26. KEY TAKEAWAY
# ============================================================

"""
__file__:

    -> identifies the path associated with a module file
    -> can be converted to a pathlib.Path
    -> can help locate resources relative to a module
    -> should not be confused with the current working directory
    -> is not guaranteed to exist in every execution environment

Common pattern:

    from pathlib import Path

    module_directory = Path(__file__).resolve().parent


Important distinction:

    __name__
        -> module identity


    __file__
        -> module file location


    Path.cwd()
        -> current working directory
"""