# 12 — Class Design

Class design is about creating clean, understandable, and maintainable object-oriented code.

Good class design helps us model real-world responsibilities clearly, reduce coupling, and build systems that are easier to extend and test.

---

## Learning Objectives

By completing this folder, you should understand:

- Single Responsibility Principle (SRP)
- Instance responsibilities vs class responsibilities
- When to choose inheritance or composition
- Interface design principles
- How clean design improves maintainability

---

# 1. Single Responsibility Principle

**File:** `01_single_responsibility.py`

A class should have one reason to change.

```python
class ReportGenerator:
    def generate(self, data):
        return "report"
```

This class is responsible for generating reports, not for storing data or handling database logic.

---

# 2. Instance vs Class Responsibility

**File:** `02_instance_vs_class_responsibility.py`

Instance methods operate on a specific object, while class methods operate on the class as a whole.

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

    @classmethod
    def from_string(cls, value):
        return cls(value)
```

This distinction helps organize responsibilities clearly.

---

# 3. Inheritance vs Composition

**File:** `03_inheritance_vs_composition.py`

A class should use inheritance only when it is a true specialization.
If behavior can be reused through composition, composition is often cleaner.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

This shows a reusable component used by a larger object.

---

# 4. Interface Design

**File:** `04_interface_design.py`

A good interface is simple, clear, and focused on the essential behavior.

```python
class PaymentService:
    def pay(self, amount):
        pass
```

A well-designed interface tells clients what they can do without exposing unnecessary internal details.

---

# Why Class Design Matters

Class design matters because it:

- reduces confusion
- promotes maintainability
- lowers coupling between components
- makes code easier to test
- supports long-term code evolution

Poorly designed classes often become difficult to extend, debug, and reuse.

---

# Key Takeaways

- A class should have a single clear responsibility.
- Instance methods operate on an object; class methods operate on the class.
- Prefer composition when behavior can be assembled from reusable pieces.
- Use inheritance only for genuine specialization.
- Good interfaces are simple, consistent, and focused.

---

# Final Thought

Good class design helps us create software that is understandable and resilient. It is not just about writing code that works — it is about writing code that remains easy to change and extend over time.
