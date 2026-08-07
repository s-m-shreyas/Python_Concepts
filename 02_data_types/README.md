# Data Types

## Overview

Data types define the kind of value a variable can store and determine the operations that can be performed on that value.

Python is a **dynamically typed** language, meaning variables do not require explicit type declarations. The Python interpreter automatically determines the data type based on the assigned value.

Understanding data types is fundamental to writing correct, efficient, and maintainable Python programs.

---

# Topics Covered

## Numeric Types

- Integer (`int`)
- Floating Point (`float`)
- Complex (`complex`)

## Boolean Type

- Boolean (`bool`)

## Text Type

- String (`str`)

## Sequence Types

- List (`list`)
- Tuple (`tuple`)
- Range (`range`)

## Set Types

- Set (`set`)
- Frozen Set (`frozenset`)

## Mapping Type

- Dictionary (`dict`)

## Binary Types

- Bytes (`bytes`)
- Bytearray (`bytearray`)
- Memoryview (`memoryview`)

## Special Type

- NoneType (`None`)

---

# Learning Objectives

After completing this section, you should be able to:

- Understand Python's built-in data types.
- Identify mutable and immutable objects.
- Choose appropriate data types for different scenarios.
- Perform common operations on each data type.
- Understand memory behavior and object mutability.
- Write cleaner and more efficient Python code.

---

# Module Organization

```
02_data_types/

README.md

01_integer.py
02_float.py
03_complex.py
04_boolean.py
05_string.py
06_list.py
07_tuple.py
08_range.py
09_set.py
10_frozenset.py
11_dictionary.py
12_bytes.py
13_bytearray.py
14_memoryview.py
15_none.py
```

---

# Mutable vs Immutable

| Mutable | Immutable |
|----------|-----------|
| list | int |
| dict | float |
| set | complex |
| bytearray | bool |
| | str |
| | tuple |
| | range |
| | frozenset |
| | bytes |
| | memoryview* |
| | None |

> **Note:** A `memoryview` provides a view into binary data. Whether the underlying data can be modified depends on the original object.

---

# Best Practices

- Choose the most appropriate data type for the problem.
- Prefer immutable data types whenever modification is unnecessary.
- Use descriptive variable names.
- Understand mutability before passing objects between functions.
- Avoid unnecessary type conversions.

---

# References

- Python Official Documentation

  https://docs.python.org/3/library/stdtypes.html

---

# Next Module

After completing this section, continue to:

**03_operators/**