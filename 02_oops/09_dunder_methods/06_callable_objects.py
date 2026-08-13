# type: ignore

"""
06_callable_objects.py

Demonstrates the __call__ method.

An object with __call__ can be used like a function.
"""


# ============================================================
# 1. CALLABLE CLASS
# ============================================================

class Multiplier:
    """A callable object that multiplies a value."""

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, value: int) -> int:
        return value * self.factor


multiply_by_3 = Multiplier(3)
print(multiply_by_3(5))
print(multiply_by_3(10))

"""
The instance behaves like a function because __call__ is defined.
"""


# ============================================================
# 2. MORE COMPLEX CALLABLE OBJECTS
# ============================================================

class Greeter:
    """Callable object with state."""

    def __init__(self, greeting: str) -> None:
        self.greeting = greeting

    def __call__(self, name: str) -> str:
        return f"{self.greeting}, {name}!"


greet = Greeter("Hello")
print(greet("Alice"))

"""
This is useful when you need an object to carry configuration and
still be invoked like a function.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __call__ makes an object callable.
# - It is useful for configurable function-like behavior.
# - Callable objects are common in frameworks and higher-order logic.
