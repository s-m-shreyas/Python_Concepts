# 13 — Dataclasses

Dataclasses are a Python feature that helps reduce boilerplate in class definitions.

They are especially useful for storing data objects, where the class mainly represents a set of attributes and a few convenience behaviors.

---

## Learning Objectives

By completing this folder, you should understand:

- What dataclasses are
- Basic dataclass syntax
- Generated methods such as `__init__`, `__repr__`, and `__eq__`
- Default values and `field()`
- `__post_init__`
- Frozen dataclasses
- Dataclass inheritance
- Comparison and ordering support

---

# 1. Dataclass Basics

**File:** `01_dataclass_basics.py`

A dataclass automatically creates an initializer and useful methods for simple data classes.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

This creates a constructor like `Person("Alice", 25)` automatically.

---

# 2. Generated Methods

**File:** `02_generated_methods.py`

Dataclasses generate several helpful methods automatically, including:

- `__init__`
- `__repr__`
- `__eq__`

This reduces boilerplate and makes debugging easier.

---

# 3. Default Values

**File:** `03_default_values.py`

Fields can have default values, which allows you to avoid writing custom constructors for common patterns.

```python
@dataclass
class User:
    name: str
    active: bool = True
```

---

# 4. `field()`

**File:** `04_field_function.py`

The `field()` function gives more control over dataclass behavior, such as default factories and metadata.

```python
from dataclasses import field, dataclass

@dataclass
class Team:
    members: list[str] = field(default_factory=list)
```

---

# 5. `__post_init__`

**File:** `05_post_init.py`

`__post_init__` runs after the generated `__init__` method. It is useful for validation or setting derived values.

```python
@dataclass
class Book:
    title: str
    pages: int

    def __post_init__(self):
        if self.pages < 0:
            raise ValueError("Pages cannot be negative")
```

---

# 6. Frozen Dataclasses

**File:** `06_frozen_dataclasses.py`

A frozen dataclass prevents mutation after creation.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

This is useful when the object should represent an immutable value.

### Important Note: What “frozen” really means

A frozen dataclass prevents normal mutation through Python attribute assignment:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 5   # This raises FrozenInstanceError
```

This means the object is intended to behave like an immutable value object in normal code.

However, Python does not guarantee that every possible low-level hack is blocked. For example, direct dictionary mutation can still bypass the usual attribute guard:

```python
p.__dict__['x'] = 5
print(p.x)   # 5
```

So a frozen dataclass is “immutable by normal Python rules,” not “impossible to mutate using low-level tricks.”

This is the same idea as tuples: they are immutable in normal use, but the object’s internal data can still be changed indirectly if it contains mutable elements.

---

# 7. Dataclass Inheritance

**File:** `07_dataclass_inheritance.py`

Dataclasses can inherit from other dataclasses, letting you extend fields and behavior naturally.

```python
@dataclass
class Employee:
    name: str

@dataclass
class Manager(Employee):
    department: str
```

---

# 8. Comparison and Ordering

**File:** `08_comparison_and_ordering.py`

Dataclasses can support easy comparison and ordering with `order=True`.

```python
@dataclass(order=True)
class Person:
    age: int
    name: str
```

This allows sorting and comparison using Python’s comparison operators.

---

# Why Dataclasses Matter

Dataclasses matter because they:

- reduce boilerplate code
- make data-focused classes easier to write
- generate useful methods automatically
- improve readability and maintainability
- encourage consistent design for value objects

---

# Key Takeaways

- Dataclasses reduce repetitive class boilerplate.
- They generate `__init__`, `__repr__`, and `__eq__` automatically.
- `field()` adds flexibility to defaults and metadata.
- `__post_init__` is useful for validation.
- `frozen=True` creates immutable-style objects that are safe to use as hash keys under normal Python rules.
- A frozen dataclass is not “absolutely unchangeable” in the low-level sense; it is protected against normal mutation.
- Inheritance works naturally with dataclasses.
- `order=True` enables sorting and comparisons.

---

# Final Thought

Dataclasses are one of Python’s most practical features for modeling data. They let us define simple, readable, and maintainable objects without writing a large amount of repetitive boilerplate.
