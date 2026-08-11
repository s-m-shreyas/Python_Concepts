# 01 - Modules

## Overview

A **module** is one of Python's fundamental mechanisms for organizing and reusing code.

This section starts with the simplest question:

> What exactly is a Python module?

From there, it progressively explains how modules are imported, how imported objects are accessed, how a module provides its own namespace, what attributes a module contains, and what happens when a module is executed.

The objective is to build a clear mental model of modules before moving into packages and the deeper import-resolution mechanism.

---

# Learning Objectives

After completing this section, you should be able to:

* Define a Python module.
* Understand the relationship between a `.py` file and a module.
* Explain why modules are used.
* Create a custom module.
* Import a module.
* Access objects defined inside a module.
* Understand the `import` statement.
* Use module aliases.
* Import specific objects using `from ... import ...`.
* Import multiple objects from a module.
* Understand the difference between importing a module and importing objects from a module.
* Explain what a module namespace is.
* Understand how module-level names are stored.
* Access module attributes.
* Understand common built-in module attributes.
* Understand what happens when a module is executed.
* Distinguish module definition from module execution.

---

# File Structure

```text
01_modules/
│
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

# Learning Sequence

## 01 - Module Basics

Introduces the fundamental concept of a module.

Topics include:

* What is a module?
* Python source files and modules
* Why modules are useful
* Creating a custom module
* Defining variables, functions, and other objects inside a module
* Reusing code through modules

---

## 02 - Import Statement

Introduces the basic `import` statement.

Topics include:

```python
import module_name
```

and:

```python
module_name.object_name
```

The focus is understanding what importing a module means and how objects inside the imported module are accessed.

---

## 03 - Import as

Introduces import aliases.

Topics include:

```python
import module_name as alias
```

The focus is understanding why aliases are used and how they affect the name used to access an imported module.

---

## 04 - From Import

Introduces importing specific objects from a module.

Topics include:

```python
from module_name import object_name
```

The focus is understanding the difference between:

```python
import module_name
```

and:

```python
from module_name import object_name
```

---

## 05 - Import Multiple Objects

Expands `from ... import ...` to multiple objects.

Topics include:

```python
from module_name import object_one, object_two
```

The focus is understanding how multiple names can be imported from the same module.

---

## 06 - Module Namespace

Introduces the concept of a module's namespace.

Topics include:

* Module-level names
* Names defined inside a module
* How imported objects are accessed
* Namespace separation between modules
* Why module-qualified access exists

This topic is important because it moves the learner beyond memorizing import syntax and toward understanding **how Python organizes names**.

---

## 07 - Module Attributes

Explores attributes associated with module objects.

Topics include:

* Module attributes
* Accessing attributes with dot notation
* Common module-level attributes
* Understanding modules as Python objects

This prepares the learner for later topics involving:

```python
__name__
__file__
```

and other special module attributes.

---

## 08 - Module Execution

Explains what happens when Python executes a module.

Topics include:

* Module-level code
* Execution of top-level statements
* Import-time execution
* Difference between defining code and executing code
* Module execution during import
* Relationship between importing and executing a module

This topic provides the foundation required for understanding the later:

```text
05_special_module_attributes/
```

section.

---

# Conceptual Progression

The modules section follows this sequence:

```text
What is a module?
        ↓
How do I import it?
        ↓
How do I access its objects?
        ↓
How do I rename the imported module?
        ↓
How do I import specific objects?
        ↓
How do I import multiple objects?
        ↓
Where do module names live?
        ↓
What attributes does a module have?
        ↓
What happens when a module executes?
```

---

# Key Mental Model

A useful mental model for this section is:

```text
Python Source File
       ↓
    Module
       ↓
 Module Namespace
       ↓
Variables / Functions / Classes / Objects
       ↓
      import
       ↓
Access through module namespace
```

For example:

```python
import calculator

calculator.add(...)
calculator.subtract(...)
```

The important idea is not merely knowing the syntax.

The important idea is understanding that:

> A module provides a namespace containing the objects defined within it.

---

# Prerequisites

Before starting this section, you should be comfortable with:

* Variables
* Data types
* Functions
* Function parameters
* Return values
* Names and scope
* Basic file structure

These concepts have already been covered in the preceding Fundamentals sections.

---

# What Comes Next?

After completing this section, the next stage is:

```text
02_module_search_and_resolution/
```

There we move from:

> **"How do I import a module?"**

to:

> **"How does Python find and resolve the module I asked it to import?"**

That transition takes the learner from basic module usage into the internal mechanics of Python's import system.
