# Indexing & Slicing

## Overview

Indexing and slicing are fundamental operations used to access and extract
elements from Python sequences.

**Indexing** retrieves an individual element using its position.

**Slicing** extracts a portion of a sequence using a start position, stop
position, and optional step.

These operations are commonly used with strings, lists, tuples, bytes,
bytearrays, and range objects.

---

# Topics Covered

## Indexing

- Positive Indexing
- Negative Indexing
- Nested Indexing

## Slicing

- Basic Slicing
- Start and Stop Positions
- Step Values
- Negative Slicing
- Reverse Slicing
- Nested Slicing

## Advanced Slicing

- Slice Objects
- Copying Using Slicing

---

# Learning Objectives

After completing this module, you should be able to:

- Understand zero-based indexing.
- Access individual elements using positive indexes.
- Access elements from the end using negative indexes.
- Extract portions of sequences using slicing.
- Understand start, stop, and step values.
- Use negative step values.
- Reverse sequences using slicing.
- Work with nested sequences.
- Create reusable `slice` objects.
- Understand how slicing can be used to create shallow copies.

---

# Module Organization

```text
03_indexing_slicing/

README.md

01_positive_indexing.py
02_negative_indexing.py

03_basic_slicing.py
04_start_stop_slicing.py
05_step_slicing.py
06_negative_slicing.py
07_reverse_slicing.py

08_nested_indexing.py
09_nested_slicing.py

10_slice_object.py
11_copy_using_slicing.py
```

---

# Indexing

Indexing uses the following syntax:

```python
sequence[index]
```

Python uses **zero-based indexing**, meaning the first element is located at
index `0`.

For example:

```text
Index:    0    1    2    3    4
Element:  P    y    t    h    o
```

Therefore:

```python
word[0]
```

returns:

```text
P
```

---

# Negative Indexing

Negative indexing starts from the end of a sequence.

```text
Index:    -5   -4   -3   -2   -1
Element:   P    y    t    h    o
```

Therefore:

```python
word[-1]
```

returns the last element.

---

# Slicing

Slicing uses the following syntax:

```python
sequence[start:stop:step]
```

Where:

- `start` specifies where slicing begins.
- `stop` specifies where slicing ends.
- `step` specifies the distance between selected elements.

The **stop position is excluded** from the resulting sequence.

For example:

```python
numbers[1:4]
```

selects the elements at indexes:

```text
1, 2, 3
```

but not index `4`.

---

# Slicing Variations

Python allows individual slicing components to be omitted.

```python
sequence[:stop]
sequence[start:]
sequence[:]
sequence[start:stop]
sequence[start:stop:step]
```

These variations provide concise ways to extract portions of sequences.

---

# Supported Sequence Types

Indexing and slicing are commonly supported by:

- `str`
- `list`
- `tuple`
- `bytes`
- `bytearray`
- `range`

Sets do not support indexing or slicing because they are not sequence types.

Dictionaries are mapping types and are accessed using keys rather than
sequence indexes.

---

# Indexing vs Slicing

| Operation | Syntax | Result |
|-----------|--------|--------|
| Indexing | `sequence[index]` | Single element |
| Slicing | `sequence[start:stop]` | Sequence portion |

Indexing accesses **one element**, while slicing extracts **multiple elements**
as a sequence.

---

# Important Concepts

## Zero-Based Indexing

The first element of a sequence has index `0`.

## Stop Position

The stop position in a slice is excluded.

## Negative Indexing

Negative indexes access elements from the end of a sequence.

## Step

The step controls how far Python moves between selected elements.

## Negative Step

A negative step moves through a sequence from right to left.

## Nested Sequences

An element inside a sequence may itself be another sequence.

Nested indexing and slicing can therefore be applied at multiple levels.

---

# Common Mistakes

- Assuming the first index is `1`.
- Forgetting that Python uses zero-based indexing.
- Assuming the stop position is included in slicing.
- Confusing an index with an element.
- Using an invalid index.
- Forgetting that negative indexes start from `-1`.
- Confusing negative indexing with negative slicing steps.
- Expecting sets to support indexing.
- Using too many nested indexing operations when a clearer approach exists.

---

# Best Practices

- Use clear variable names when storing extracted elements or slices.
- Remember that indexing returns a single element.
- Remember that slicing returns a sequence.
- Use negative indexing when accessing elements relative to the end.
- Keep slice expressions readable.
- Use slicing when extracting contiguous portions of a sequence.
- Understand the behavior of mutable sequences before modifying sliced data.

---

# References

- Python Official Documentation

  https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

- Python Documentation – Built-in `slice()` Type

  https://docs.python.org/3/library/functions.html#slice

---

# Next Module

Continue to:

**04_copy_operations/**