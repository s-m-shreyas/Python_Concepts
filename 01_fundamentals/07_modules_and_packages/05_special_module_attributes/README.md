# Special Module Attributes

This section introduces important **special attributes automatically associated with Python modules**.

These attributes provide information about a module's identity, execution context, and file location.

## Topics Covered

### 01. `__name__` Attribute

Understanding the special `__name__` attribute.

Key concepts:

* Module identity
* `__name__`
* `"__main__"`
* Direct execution
* Imported modules
* Module names inside packages
* `__name__` vs filename

Basic idea:

```python
print(__name__)
```

When a module is executed directly:

```text
__name__ == "__main__"
```

When it is imported:

```text
__name__ == module's import name
```

### 02. Main Guard

Understanding:

```python
if __name__ == "__main__":
    ...
```

Key concepts:

* Main guard
* Direct execution
* Module imports
* Reusable code
* Entry-point logic
* `main()` function pattern
* Preventing execution during imports

Common pattern:

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

The main guard allows a module to function both as:

```text
Reusable module
      +
Directly executable script
```

### 03. `__file__` Attribute

Understanding the special `__file__` attribute and how a module can identify its associated file.

Key concepts:

* Module file location
* `__file__`
* `pathlib.Path`
* `Path(__file__)`
* `.resolve()`
* `.parent`
* Resource paths
* `Path.cwd()` vs `__file__`

Common pattern:

```python
from pathlib import Path

module_directory = Path(__file__).resolve().parent
```

This is useful when locating resources relative to the module itself.

## Special Attribute Overview

The concepts can be visualized as:

```text
Python Module
│
├── __name__
│      ↓
│   Module identity
│
├── Main Guard
│      ↓
│   Execution control
│
└── __file__
       ↓
    Module file location
```

## Important Distinctions

### `__name__`

Answers:

> **"What is this module's current execution/import identity?"**

```text
Direct execution
    ↓
"__main__"

Imported module
    ↓
"package.module"
```

### Main Guard

Answers:

> **"Should this code run only when this module is executed directly?"**

```python
if __name__ == "__main__":
    main()
```

### `__file__`

Answers:

> **"Where is this module's file located?"**

```python
from pathlib import Path

Path(__file__).resolve()
```

## Learning Objective

By the end of this section, you should understand how Python modules can:

* Identify themselves using `__name__`.
* Detect whether they are being executed directly.
* Separate reusable code from executable code.
* Use the main guard correctly.
* Identify their own source-file location using `__file__`.
* Distinguish a module's file location from the current working directory.

These concepts form an important foundation for understanding **Python module execution, imports, packages, and application entry points**.
