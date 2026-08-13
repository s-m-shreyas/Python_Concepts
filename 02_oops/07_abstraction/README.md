# 07 — Abstraction

Abstraction is the process of hiding unnecessary implementation details and exposing only the essential interface of a class.

This folder focuses on how Python implements abstraction using abstract base classes and abstract methods so that related classes can share a common contract.

---

## Learning Objectives

By completing this folder, you should understand:

- What abstraction means
- Abstract base classes (ABCs)
- Abstract methods
- Abstract properties
- Concrete classes
- Why abstraction helps in large software systems
- How abstraction supports polymorphism

---

# 1. Abstract Base Classes

**File:** `01_abstract_base_classes.py`

An abstract base class defines a common interface but cannot be instantiated directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

A class with abstract methods is incomplete until subclasses implement them.

---

# 2. Abstract Methods

**File:** `02_abstract_methods.py`

Abstract methods are methods declared in a base class but left without implementation.

```python
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

Every subclass must provide an implementation, or it also remains abstract.

---

# 3. Abstract Properties

**File:** `03_abstract_properties.py`

A property can also be abstract. This means every subclass must define how the property behaves.

```python
class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass
```

This helps define a required attribute contract across multiple classes.

---

# 4. Concrete Implementations

**File:** `04_concrete_implementations.py`

A concrete class implements all abstract methods and can then be instantiated.

Example:

```python
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"
```

The base class gives the design rule, and the subclass provides the real behavior.

---

# Why Abstraction Matters

Abstraction matters because it:

- reduces unnecessary complexity
- keeps code organized
- defines a standard interface for related classes
- helps teams design systems around contracts rather than implementation details
- supports polymorphism and scalability

Instead of worrying about how a task is done inside each class, we focus on what the class should provide.

---

# Key Takeaways

- Abstraction hides internal complexity.
- ABCs define a template for related classes.
- Abstract methods require subclasses to implement behavior.
- Abstract properties define required attribute contracts.
- Concrete classes are fully usable and can be instantiated.
- Abstraction improves design, consistency, and maintainability.

---

# Final Thought

In real applications, abstraction helps us write code to interfaces rather than concrete implementations. This makes programs easier to extend, easier to test, and easier to maintain as the system grows.
