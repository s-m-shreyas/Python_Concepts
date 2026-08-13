# type: ignore

"""
05_container_methods.py

Demonstrates how container-like dunder methods make a class behave
like a collection.
"""


# ============================================================
# 1. CUSTOM LIST-LIKE CLASS
# ============================================================

class CustomList:
    """A simplified custom collection."""

    def __init__(self, items: list[int]) -> None:
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.items[index] = value

    def __contains__(self, item: int) -> bool:
        return item in self.items


values = CustomList([10, 20, 30])

print(len(values))
print(values[1])
values[0] = 99
print(values[0])
print(20 in values)

"""
This class behaves like a container even though it is user-defined.
"""


# ============================================================
# 2. USING COLLECTION FEATURES
# ============================================================

class Bag:
    """A simple bag-like class."""

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __iter__(self):
        return iter(self.items)


bag = Bag(["apple", "banana", "mango"])
for item in bag:
    print(item)

"""
__iter__ is another dunder method that makes the object iterable.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __len__ gives length semantics.
# - __getitem__ allows index access.
# - __setitem__ allows item assignment.
# - __contains__ allows membership testing.
# - These methods make custom containers work like native Python collections.
