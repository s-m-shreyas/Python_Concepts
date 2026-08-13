# 09 — Dunder Methods

Dunder methods, also known as magic methods, are special methods in Python that begin and end with double underscores.

They allow user-defined classes to interact naturally with Python built-in behaviors such as printing, comparison, arithmetic, container operations, and function calls.

---

## Learning Objectives

By completing this folder, you should understand:

- What dunder methods are
- `__str__` and `__repr__`
- Equality and inequality methods
- Comparison operators
- Arithmetic dunder methods
- Container methods
- Callable objects
- `__len__` and `__bool__`
- Why dunder methods make classes Pythonic

---

# 1. `__str__` and `__repr__`

**File:** `01_str_and_repr.py`

These methods control how an object is converted to a string.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"

    def __repr__(self):
        return f"Person(name={self.name!r})"
```

`__str__` is for user-friendly output, while `__repr__` is for developer-friendly representation.

---

# 2. Equality and Inequality

**File:** `02_eq_and_ne.py`

`__eq__` and `__ne__` define how objects compare for equality and inequality.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

This lets us compare custom objects naturally.

---

# 3. Comparison Methods

**File:** `03_comparison_methods.py`

Comparison operators can be customized with methods such as:

- `__lt__` for `<`
- `__le__` for `<=`
- `__gt__` for `>`
- `__ge__` for `>=`

These are useful when you want objects to compare by a meaningful attribute.

---

# 4. Arithmetic Methods

**File:** `04_arithmetic_methods.py`

Arithmetic dunder methods allow operators like `+`, `-`, `*`, and `/` to work with custom objects.

```python
class Vector:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

This makes custom objects behave like built-in numeric types.

---

# 5. Container Methods

**File:** `05_container_methods.py`

Container methods let custom classes behave like lists, dictionaries, or other collections.

Examples include:

- `__len__`
- `__getitem__`
- `__setitem__`
- `__contains__`

These methods make custom container-like classes much easier to use.

---

# 6. Callable Objects

**File:** `06_callable_objects.py`

A class can be made callable by defining `__call__`.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
```

Then the object can be invoked like a function.

---

# 7. `__len__` and `__bool__`

**File:** `07_len_and_bool.py`

`__len__` defines the length of the object, while `__bool__` defines how it is evaluated in truth-value contexts.

```python
class Bag:
    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self.items) > 0
```

These methods help objects integrate naturally with Python control flow and built-ins such as `len()` and `if` conditions.

---

# Why Dunder Methods Matter

Dunder methods matter because they:

- make custom classes integrate with Python syntax
- enable operator overloading and built-in behaviors
- support richer and more readable APIs
- make user-defined objects feel like native Python types

They are one of the features that make Python feel expressive and consistent.

---

# Key Takeaways

- Dunder methods are special methods with double underscores.
- They allow custom classes to work with Python operators and built-ins.
- `__str__` and `__repr__` control string conversion.
- `__eq__` and comparison methods define equality and ordering behavior.
- Arithmetic dunder methods support `+`, `-`, `*`, etc.
- Container methods make objects behave like collections.
- `__call__` makes objects callable.
- `__len__` and `__bool__` control size and truthiness.

---

# Final Thought

Dunder methods are what make Python classes feel natural in a Python environment. Instead of writing verbose custom APIs, we can let objects behave like built-in types and use Python’s operators and syntax directly.
