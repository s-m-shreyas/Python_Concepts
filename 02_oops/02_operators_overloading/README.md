# Python Operators

A structured reference and learning guide for Python operators.

This directory contains focused examples covering Python's built-in
operators, expression evaluation, comparison behaviour, operator
precedence, short-circuit evaluation, and custom operator overloading.

The examples are intentionally separated by topic so that each concept
can be studied independently and then connected to the larger Python
expression model.

---

## Table of Contents

- [01. Operator Overloading](#15-operator-overloading)
- [02. Dunder Operator Methods](#16-dunder-operator-methods)
- [03. Arithmetic Dunder Methods](#17-arithmetic-dunder-methods)
- [04. Comparison Dunder Methods](#18-comparison-dunder-methods)
- [05. In-Place Operators](#19-in-place-operators)
- [06. Custom Operator Overloading](#20-custom-operator-overloading)
- [Quick Reference](#quick-reference)
- [Operator Precedence Reference](#operator-precedence-reference)
- [Operator Overloading Reference](#operator-overloading-reference)
- [Common Mistakes](#common-mistakes)
- [Important Distinctions](#important-distinctions)
- [Best Practices](#best-practices)
- [Learning Checklist](#learning-checklist)
- [Final Mental Model](#final-mental-model)

---

# Overview

Operators are symbols and keywords that allow Python programs to perform
operations on values and objects.

Examples include:

```python
10 + 5
10 > 5
value == 100
name in names
isinstance(value, int)
True and False
number << 2