# Indexing & Slicing

## Overview

Indexing and slicing are fundamental techniques used to access and manipulate elements within Python sequences.

These operations work with various sequence types, including strings, lists, tuples, bytes, bytearrays, and range objects.

Mastering indexing and slicing is essential for efficient data processing and forms the foundation for many advanced Python concepts.

---

# Topics Covered

## Indexing

- Positive Indexing
- Negative Indexing
- Accessing Individual Elements
- IndexError

## Slicing

- Basic Slicing
- Start Index
- Stop Index
- Step Value
- Negative Slicing
- Reverse Slicing
- Copying Using Slicing

---

# Learning Objectives

After completing this module, you should be able to:

- Access individual elements using indexes.
- Differentiate between positive and negative indexing.
- Extract portions of sequences using slicing.
- Use custom step values.
- Reverse sequences efficiently.
- Understand slice boundaries and common edge cases.

---

# Module Organization

```
04_indexing_slicing/

README.md

01_positive_indexing.py
02_negative_indexing.py
03_basic_slicing.py
04_slicing_with_start_stop.py
05_slicing_with_step.py
06_negative_slicing.py
07_reverse_slicing.py
08_copy_using_slicing.py
```

---

# Indexing vs Slicing

| Feature | Indexing | Slicing |
|----------|----------|----------|
| Returns | Single Element | New Sequence |
| Syntax | sequence[index] | sequence[start:stop:step] |
| Supports Step | ❌ No | ✅ Yes |
| Can Reverse Data | ❌ No | ✅ Yes |
| Raises IndexError | ✅ Yes | ❌ No |

---

# Supported Sequence Types

Indexing and slicing are supported by:

- String (`str`)
- List (`list`)
- Tuple (`tuple`)
- Bytes (`bytes`)
- Bytearray (`bytearray`)
- Range (`range`)

---

# Best Practices

- Prefer negative indexing when accessing elements from the end.
- Remember that the stop index is excluded during slicing.
- Use descriptive variable names for extracted sequences.
- Avoid hardcoding indexes whenever possible.
- Use slicing instead of loops when extracting contiguous portions of a sequence.

---

# Common Mistakes

- Forgetting that indexing starts from zero.
- Assuming the stop index is included.
- Mixing positive and negative indexes incorrectly.
- Confusing indexing with slicing.
- Expecting slicing to raise an IndexError.

---

# References

- Python Official Documentation

  https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

---

# Next Module

Continue to:

**05_copy_operations/**