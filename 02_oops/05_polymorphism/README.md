# 05 — Polymorphism

Polymorphism is one of the core concepts of Object-Oriented Programming (OOP).

The word **polymorphism** means:

> **Many forms.**

In Python, polymorphism allows different objects to respond to the **same operation or interface** in different ways.

---

## Folder Structure

```text
05_polymorphism/
│
├── 01_method_overriding.py
├── 02_duck_typing.py
├── 03_polymorphic_functions.py
# Polymorphism — improved guide

This folder contains focused examples that demonstrate runtime polymorphism in Python. The goal is to make the concept tangible with short, runnable examples, clear outputs, and exercises that reinforce both inheritance-based polymorphism and duck typing.

## What you'll learn

- The difference between polymorphism via inheritance and polymorphism via duck typing.
- How method overriding enables subclass-specific behavior through base-class references.
- How to write polymorphic functions that accept many object types.
- When to prefer abstract base classes (`abc`) versus lightweight duck typing.

## Files (quick map)

- `01_method_overriding.py` — Simple inheritance example showing `Animal` → `Dog`/`Cat` and overridden `speak()` behaviour.
- `02_duck_typing.py` — Demonstrates interchangeable objects that implement the same method name without shared inheritance.
- `03_polymorphic_functions.py` — Utility functions that accept different object types and operate polymorphically.
- `04_polymorphism_with_inheritance.py` — A richer example using `abc.ABC` (optional) to define a protocol plus several concrete subclasses.

## Quick start — run examples

From the repository root run the scripts with your Python interpreter:

```bash
python 02_oops/05_polymorphism/01_method_overriding.py
python 02_oops/05_polymorphism/02_duck_typing.py
python 02_oops/05_polymorphism/03_polymorphic_functions.py
python 02_oops/05_polymorphism/04_polymorphism_with_inheritance.py
```

Run one at a time and read the printed output. Each script prints class names and the method results so you can observe which implementation ran.

## Walkthrough & expected behavior

- Method overriding: `Animal.speak()` is defined in the base class; `Dog` and `Cat` override it. When code holds an `Animal`-typed reference that actually points to a `Dog`, calling `.speak()` runs `Dog.speak()`.

- Duck typing: Two unrelated classes implement the same method (for example, `render()` or `quack()`). A function that calls that method on its argument will succeed for either object as long as the method exists. This avoids rigid class hierarchies and makes code flexible.

- Polymorphic functions: Functions should document the expected protocol (method name and semantics). Prefer clear names like `speak()` or `serialize()` and document return types/side effects in a docstring.

- Using `abc.ABC`: When you want explicit contracts and static checks (and to fail fast for missing implementations), use `abc.ABC` and `@abstractmethod`. For lightweight code, duck typing is often sufficient.

## Short examples (conceptual)

- Overriding example (concept):

```py
class Animal:
	def speak(self):
		return "..."

class Dog(Animal):
	def speak(self):
		return "woof"

obj: Animal = Dog()
print(obj.speak())  # prints 'woof' — Dog's implementation
```

- Duck typing example (concept):

```py
class FileLike:
	def read(self):
		return "data"

class StringLike:
	def read(self):
		return "str-data"

def process(r):
	print(r.read())

process(FileLike())
process(StringLike())
```

## Exercises

1. Add `Bird` to `01_method_overriding.py` with `speak()` returning `chirp`. Show polymorphism by storing different animals in a list and calling `speak()` in a loop.
2. In `02_duck_typing.py` add a `Broken` class without the required method; update the consumer to handle missing methods gracefully (use `hasattr` or `try/except`).
3. Expand `03_polymorphic_functions.py` with a `serialize(obj)` function that accepts objects implementing either `to_json()` or `to_dict()` and prefers `to_json()` when available.
4. In `04_polymorphism_with_inheritance.py` add unit tests using `pytest` that assert each concrete subclass behaves as expected.

## Teaching notes

- Show both inheritance and duck-typing examples side-by-side to compare trade-offs: explicit contract vs flexibility.
- Use small printed examples to surface method dispatch; include the concrete class name in logs to avoid confusion.
- Encourage students to prefer simple interfaces and to document expected object protocols (method names and return types).

## Suggested unit tests (quick)

Create `tests/test_polymorphism.py` and assert that `speak()` returns expected strings for each concrete class. Running:

```bash
pip install pytest
pytest -q
```

## References

- Python classes tutorial: https://docs.python.org/3/tutorial/classes.html
- abc — Abstract Base Classes: https://docs.python.org/3/library/abc.html
- Articles: search "duck typing python" and "polymorphism in python" for community posts and examples.

---

I've updated this README to be more instructional and actionable. I'll mark the task done — would you like me to also add unit tests or update any of the example scripts with comments and output examples next?