# Copy Operations

## Overview

Copy operations determine how objects are duplicated in Python.

Understanding Python's object referencing and copying behavior is essential for writing correct and bug-free programs, especially when working with mutable data types such as lists, dictionaries, and sets.

This module explains the differences between object references, shallow copies, and deep copies through practical examples.

---

# Topics Covered

## General Copy

- Object References
- Assignment Behavior
- Shared Objects
- Identity vs Equality

## Shallow Copy

- copy.copy()
- One-Level Copy
- Shared Nested Objects

## Deep Copy

- copy.deepcopy()
- Recursive Copy
- Independent Objects

---

# Learning Objectives

After completing this module, you should be able to:

- Understand how Python stores objects in memory.
- Differentiate between assignment and copying.
- Identify shared object references.
- Explain shallow copy behavior.
- Explain deep copy behavior.
- Choose the appropriate copying technique for different scenarios.

---

# Module Organization

```
05_copy_operations/

README.md

01_general_copy.py
02_shallow_copy.py
03_deep_copy.py
```

---

# Copy Operation Comparison

| Operation | New Object | Nested Objects | Common Usage |
|-----------|-----------:|---------------:|-------------|
| General Copy | ❌ No | Shared | Variable Assignment |
| Shallow Copy | ✅ Yes | Shared | Flat Collections |
| Deep Copy | ✅ Yes | Independent | Nested Collections |

---

# Why Learn Copy Operations?

Understanding copy operations helps prevent common programming mistakes such as:

- Unintended data modification.
- Shared mutable objects.
- Side effects between variables.
- Bugs caused by nested collections.
- Incorrect object duplication.

---

# Best Practices

- Understand object references before learning copy operations.
- Use assignment only when shared references are intended.
- Use shallow copy for simple collections.
- Use deep copy when nested mutable objects must be completely independent.
- Always verify whether an object is mutable before deciding how to copy it.

---

# References

- Python Official Documentation

  https://docs.python.org/3/library/copy.html

---

# Next Module

Continue to:

**06_control_statements/**