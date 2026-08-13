# 08 — Properties

Properties are a Python feature that lets us control access to instance attributes through methods that look like normal attribute access.

This folder explains how properties can be used to implement validation, encapsulation, and cleaner APIs without exposing raw internal state unnecessarily.

---

## Learning Objectives

By completing this folder, you should understand:

- What a property is
- How `@property` works
- Getter and setter methods
- Read-only properties
- Property validation
- Why properties are useful in object-oriented design

---

# 1. Property Function

**File:** `01_property_function.py`

A property allows a method to be accessed like an attribute.

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Now `student.name` works like a normal attribute, but the logic is still controlled internally.

---

# 2. Getter and Setter

**File:** `02_getter_and_setter.py`

The getter reads the value and the setter updates the value, often with validation.

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

This allows you to validate data before assigning it.

---

# 3. Read-Only Properties

**File:** `03_read_only_properties.py`

A property can be made read-only by defining only the getter and no setter.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

This prevents outside code from modifying the value directly.

---

# 4. Property Validation

**File:** `04_property_validation.py`

Properties are especially useful when you need to validate input before storing it.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

This is a classic use of property-based encapsulation.

---

# Why Properties Matter

Properties matter because they:

- improve encapsulation
- allow validation
- make code cleaner and more Pythonic
- provide controlled access to internal attributes
- hide implementation details behind a simple interface

Rather than directly mutating private data, we can centralize logic inside a property.

---

# Key Takeaways

- `@property` allows method-like access using attribute syntax.
- Getter methods read values.
- Setter methods validate and assign values.
- Read-only properties prevent updates.
- Properties are a very useful way to enforce object invariants.
- Properties help balance encapsulation and usability.

---

# Final Thought

Properties are one of Python’s most elegant tools for controlling attribute access. They let you protect internal state while keeping the class interface simple and readable.
