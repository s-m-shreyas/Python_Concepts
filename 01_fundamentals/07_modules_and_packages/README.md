# 07 - Modules and Packages

## Overview

This section explains how Python organizes code into reusable and maintainable units using **modules and packages**.

The goal is not only to learn how to write:

```python
import module
```

but to understand the complete module and package system — including namespaces, module attributes, module execution, module search paths, import resolution, packages, absolute and relative imports, and special module attributes.

By the end of this section, you should understand both:

* **How to use Python's module and package system**
* **How Python finds, loads, and executes imported modules**

---

## Learning Objectives

After completing this section, you should be able to:

* Explain what a Python module is.
* Understand the relationship between a `.py` file and a module.
* Import modules using different import syntaxes.
* Import specific objects from a module.
* Use import aliases.
* Understand module namespaces.
* Access module attributes.
* Understand what happens when a module is executed.
* Understand how Python searches for modules.
* Understand `sys.path`.
* Understand module search paths.
* Distinguish standard-library modules from custom modules.
* Understand the basic import-resolution process.
* Explain what a Python package is.
* Understand subpackages.
* Import objects from packages.
* Understand the purpose of `__init__.py`.
* Understand absolute imports.
* Understand relative imports.
* Understand import conventions.
* Understand the special attributes `__name__`, `__main__`, and `__file__`.

---

# Section Structure

## 01 - Modules

This section establishes the fundamental concept of a Python module.

Topics include:

* What a module is
* Python files as modules
* Importing modules
* Import syntax variations
* Importing multiple objects
* Module namespaces
* Module attributes
* Module execution

Files:

```text
01_modules/
├── 01_module_basics.py
├── 02_import_statement.py
├── 03_import_as.py
├── 04_from_import.py
├── 05_import_multiple_objects.py
├── 06_module_namespace.py
├── 07_module_attributes.py
└── 08_module_execution.py
```

---

## 02 - Module Search and Resolution

This section goes deeper into how Python locates and resolves modules during an import.

Topics include:

* `sys.path`
* Module search paths
* Standard-library modules vs custom modules
* Import resolution

Files:

```text
02_module_search_and_resolution/
├── 01_sys_path.py
├── 02_module_search_path.py
├── 03_standard_library_vs_custom_modules.py
└── 04_import_resolution.py
```

---

## 03 - Packages

This section extends the module concept into multi-module project organization.

Topics include:

* Package basics
* Subpackages
* Package imports
* `__init__.py`

Files:

```text
03_packages/
├── 01_package_basics.py
├── 02_subpackages.py
├── 03_package_imports.py
└── 04_init_file.py
```

---

## 04 - Import Patterns

This section focuses on the different ways imports can be structured.

Topics include:

* Absolute imports
* Relative imports
* Import aliases
* Import conventions

Files:

```text
04_import_patterns/
├── 01_absolute_imports.py
├── 02_relative_imports.py
├── 03_import_aliases.py
└── 04_import_conventions.py
```

---

## 05 - Special Module Attributes

This section covers special attributes that help explain module identity, execution context, and source-file location.

Topics include:

* `__name__`
* `__main__`
* `__file__`

Files:

```text
05_special_module_attributes/
├── 01_name_attribute.py
├── 02_main_guard.py
└── 03_file_attribute.py
```

---

# Conceptual Progression

The section follows this progression:

```text
Python File
     ↓
Module
     ↓
Import
     ↓
Import Syntax
     ↓
Module Namespace
     ↓
Module Attributes
     ↓
Module Execution
     ↓
Module Search Path
     ↓
Import Resolution
     ↓
Package
     ↓
Subpackage
     ↓
Package Imports
     ↓
Absolute / Relative Imports
     ↓
__name__
     ↓
__main__
     ↓
__file__
```

The intention is to build the concepts progressively rather than treating modules and packages as a collection of unrelated import statements.

---

# Important Distinction

This section focuses on **Python's module and package mechanism itself**.

It does not attempt to teach individual libraries such as:

```text
NumPy
Pandas
Requests
SQLAlchemy
Matplotlib
```

Those will belong to the separate:

```text
05_libraries_&_modules/
```

section of the repository.

The purpose here is to understand **how Python organizes and imports code**, regardless of which library or package is being used.

---

# Completion Criteria

This section is considered complete when you can explain:

> What happens in Python when an `import` statement is executed?

You should be able to reason about:

```text
Where does Python look?
        ↓
What does it find?
        ↓
How is the module identified?
        ↓
What namespace is created?
        ↓
How are objects accessed?
        ↓
What happens when the module executes?
        ↓
How does this differ when the module is imported
versus executed directly?
```

The objective is **understanding the system**, not memorizing import syntax.
