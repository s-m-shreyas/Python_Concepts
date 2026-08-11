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

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Directory Structure](#directory-structure)
- [Recommended Learning Order](#recommended-learning-order)
- [Operator Categories](#operator-categories)
- [1. Arithmetic Operators](#1-arithmetic-operators)
- [2. Comparison Operators](#2-comparison-operators)
- [3. Assignment Operators](#3-assignment-operators)
- [4. Augmented Assignment Operators](#4-augmented-assignment-operators)
- [5. Logical Operators](#5-logical-operators)
- [6. Bitwise Operators](#6-bitwise-operators)
- [7. Membership Operators](#7-membership-operators)
- [8. Identity Operators](#8-identity-operators)
- [9. Unary Operators](#9-unary-operators)
- [10. Ternary Operator](#10-ternary-operator)
- [11. Chained Comparisons](#11-chained-comparisons)
- [12. Short-Circuit Evaluation](#12-short-circuit-evaluation)
- [13. Operator Precedence](#13-operator-precedence)
- [14. Operator Associativity](#14-operator-associativity)
- [15. Operator Overloading](#15-operator-overloading)
## Continued in 07_operators_oops folder
- [16. Dunder Operator Methods](#16-dunder-operator-methods)
- [17. Arithmetic Dunder Methods](#17-arithmetic-dunder-methods)
- [18. Comparison Dunder Methods](#18-comparison-dunder-methods)
- [19. In-Place Operators](#19-in-place-operators)
- [20. Custom Operator Overloading](#20-custom-operator-overloading)
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