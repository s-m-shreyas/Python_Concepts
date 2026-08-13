# 06 — Encapsulation

Encapsulation is an object-oriented concept that binds data and the methods that work on that data together while controlling access to the internal state of an object.

This folder covers the different visibility levels in Python and how they help us design safer and cleaner classes.

---

## Learning Objectives

By completing this folder, you should understand:

- What encapsulation means
- Public members
- Protected members by convention
- Private members
- Name mangling
- Why direct access is often discouraged
- How methods provide controlled access

---

# 1. Public Members

**File:** `01_public_members.py`

Public members are default attributes and methods in Python. They can be accessed directly from outside the class.

Example:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student = Student("Alice", 90)
print(student.name)
print(student.marks)
```

Public members are convenient, but they do not protect the object from invalid state changes.

---

# 2. Protected Convention

**File:** `02_protected_convention.py`

In Python, a single underscore prefix indicates a protected member.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
```

This signals:

- the member is intended for internal use
- subclasses may access it
- external code should avoid direct access

It is a convention, not a strict access restriction.

---

# 3. Private Members

**File:** `03_private_members.py`

A double underscore prefix is used for private members.

```python
class Account:
    def __init__(self, password):
        self.__password = password
```

Python stores this internally with name mangling, so the attribute is renamed to something like:

```python
_Account__password
```

This reduces accidental collisions and communicates that the attribute is meant to stay internal.

---

# 4. Name Mangling

**File:** `04_name_mangling.py`

Name mangling is the process by which Python changes the internal name of a private attribute or method.

```python
class Parent:
    def __private_method(self):
        print("Parent secret")
```

The actual internal name becomes:

```python
_Parent__private_method
```

This helps avoid collisions between parent and child classes that both define private members with the same name.

---

# Why Encapsulation Matters

Encapsulation matters because it:

- protects object state
- prevents accidental misuse
- encourages validation through methods
- organizes code into safer interfaces
- makes large systems easier to maintain

A class should often expose meaningful public methods instead of allowing arbitrary direct mutation of internal state.

---

# Key Takeaways

- Public members are accessible everywhere.
- A single underscore means “protected by convention”.
- A double underscore means “private-like” and triggers name mangling.
- Python does not enforce encapsulation as strictly as some other languages.
- Good encapsulation is mostly about design discipline and controlled access.
- Methods such as getters/setters help enforce validation and logic.

---

# Final Thought

Encapsulation is not only about hiding data. It is about exposing the correct interface and protecting the object from invalid or unintended use.

That is why Python encourages a clean design: data should usually be modified through methods, not by arbitrary direct access from outside the class.
