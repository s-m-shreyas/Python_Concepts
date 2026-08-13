# Polymorphism

This folder contains examples and explanations demonstrating polymorphism in Python. The code samples are small, focused, and intended for learners who are comfortable with basic classes, inheritance, and functions.

## Learning objectives

- Understand what polymorphism means and why it matters.
- See practical examples of method overriding and duck typing.
- Write polymorphic functions that operate on multiple types.
- Observe how inheritance-based polymorphism differs from duck typing.

## Prerequisites

- Basic familiarity with Python syntax and functions.
- Comfort with classes and inheritance (see earlier OOP sections in this repository).

## Files in this folder

- `01_method_overriding.py` — Demonstrates overriding a parent class method in a subclass and calling the overridden method via a base-class reference.
- `02_duck_typing.py` — Illustrates duck typing: objects that share the same method names can be used interchangeably without sharing a common base class.
- `03_polymorphic_functions.py` — Shows functions that accept different object types and call the same method name, relying on polymorphism to work correctly.
- `04_polymorphism_with_inheritance.py` — A longer example combining abstract/base classes, multiple subclasses, and polymorphic dispatch.
- `README.md` — (this file) explains the examples, provides usage instructions, and suggests exercises.

## Key concepts

- Polymorphism: The ability for different object types to be used through the same interface (method names or protocols).
- Method overriding: A subclass provides a new implementation for a method defined in a superclass.
- Duck typing: "If it quacks like a duck, it's a duck" — code depends on the presence of methods/attributes rather than object types.
- Polymorphic functions: Functions that operate on objects of different types by relying on a shared method or protocol.

## How to run the examples

From the repository root (or this folder), run each file using Python. Examples:

```bash
python 05_polymorphism/01_method_overriding.py
python 05_polymorphism/02_duck_typing.py
python 05_polymorphism/03_polymorphic_functions.py
python 05_polymorphism/04_polymorphism_with_inheritance.py
```

Each script prints short output demonstrating method dispatch and interchangeable usage.

## Example summaries

- Method overriding: A base class `Animal` defines `speak()`; subclasses `Dog` and `Cat` override `speak()` to provide type-specific behavior. Calling `speak()` on an `Animal` reference that actually holds a `Dog` instance calls the `Dog` implementation.

- Duck typing: Two unrelated classes both implement a `render()` or `quack()` method. A function that calls `render()` on its argument works with both classes without inheritance.

- Polymorphic functions: A function `announce(entity)` calls `entity.speak()`; it works for `Dog`, `Cat`, or any object implementing `speak()`.

- Inheritance example: Uses a common interface (or abstract base class) to define required methods and demonstrates runtime selection of subclass behavior.

## Exercises (recommended)

1. Add a new subclass (e.g., `Bird`) to `01_method_overriding.py` and implement `speak()` differently. Verify polymorphic dispatch.
2. Modify `02_duck_typing.py` to add a class that deliberately lacks the expected method; add a safe check and fall-back behavior.
3. In `03_polymorphic_functions.py` write a function that accepts either a single object or a list of objects and calls the common method on each element.
4. Extend `04_polymorphism_with_inheritance.py` to include an abstract base class (using `abc.ABC`) and add type checks or `isinstance` guards where appropriate.

## Teaching tips

- When explaining polymorphism, show both inheritance-based and duck-typed examples side-by-side to highlight differences.
- Use printouts that include the class name and method result to make dispatch behavior explicit.
- Encourage students to write small, focused tests that assert behavior for each concrete type.

## Further reading

- Python docs on classes and inheritance: https://docs.python.org/3/tutorial/classes.html
- Abstract Base Classes (abc module): https://docs.python.org/3/library/abc.html
- Articles on duck typing and dynamic polymorphism in Python.

## Glossary

- Polymorphism: Ability of different object types to be used via the same interface.
- Duck typing: Relying on method/attribute presence rather than explicit types.
- Method overriding: Redefining a method in a subclass to change behavior.

---

If you want, I can add short unit tests for each example or expand any file with more comments and additional examples. Would you like tests or expanded explanations added next?
