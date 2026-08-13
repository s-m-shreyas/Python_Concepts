# 11 — Composition

Composition is an object-oriented design principle in which a class is built using other classes as parts of its functionality.

Instead of inheriting behavior, a class creates or holds objects of other classes and delegates responsibilities to them.

---

## Learning Objectives

By completing this folder, you should understand:

- The has-a relationship
- Composition in practice
- Aggregation as a looser form of composition
- Composition vs inheritance
- Why composition is often preferred for flexibility

---

# 1. Has-A Relationship

**File:** `01_has_a_relationship.py`

A class has-a relationship means one object contains another object as a component.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

Here, `Car` has an `Engine`.

---

# 2. Composition

**File:** `02_composition.py`

Composition is a stronger form of ownership where the contained object is created and managed by the outer object.

```python
class Keyboard:
    def type(self):
        print("Typing")

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
```

The `Computer` owns the `Keyboard` and controls its lifecycle.

---

# 3. Aggregation

**File:** `03_aggregation.py`

Aggregation is a looser relationship where the inner object is not necessarily owned by the outer object.

```python
class Department:
    def __init__(self, manager):
        self.manager = manager
```

The department uses a manager object, but the manager can also exist independently.

---

# 4. Composition vs Inheritance

**File:** `04_composition_vs_inheritance.py`

Composition and inheritance both help reuse behavior, but they are different.

- Inheritance models an `is-a` relationship.
- Composition models a `has-a` relationship.

Inheritance is useful when classes are closely related.
Composition is often more flexible when behavior is assembled from smaller reusable pieces.

---

# Why Composition Matters

Composition matters because it:

- improves flexibility
- reduces tight coupling
- makes systems easier to change
- allows behavior to be assembled from reusable components
- often leads to cleaner and more maintainable designs

---

# Key Takeaways

- Composition is about building objects from other objects.
- A has-a relationship is typical of composition.
- Aggregation is a looser version where dependencies are shared rather than owned.
- Composition often scales better than deep inheritance trees.
- Prefer composition when behavior should be reusable and loosely coupled.

---

# Final Thought

Composition allows a class to use other classes as building blocks, creating modular and flexible designs. It is often a better choice than inheritance when the goal is reuse without tightly coupling class hierarchies.
