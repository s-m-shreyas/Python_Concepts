# type: ignore

"""
07_len_and_bool.py

Demonstrates __len__ and __bool__.

These methods define the length and truthiness of custom objects.
"""


# ============================================================
# 1. __len__
# ============================================================

class Box:
    """A box with items stored inside it."""

    def __init__(self, items: list[int]) -> None:
        self.items = items

    def __len__(self) -> int:
        return len(self.items)


box = Box([1, 2, 3, 4])
print(len(box))

"""
len(box) uses __len__.
"""


# ============================================================
# 2. __bool__
# ============================================================

class Queue:
    """A queue-like class with truthiness based on items."""

    def __init__(self, items: list[int]) -> None:
        self.items = items

    def __bool__(self) -> bool:
        return len(self.items) > 0


empty_queue = Queue([])
nonempty_queue = Queue([10])

print(bool(empty_queue))
print(bool(nonempty_queue))

if empty_queue:
    print("This will not print.")
else:
    print("The queue is empty.")

"""
__bool__ controls how the object behaves in if conditions.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __len__ defines the length of an object.
# - __bool__ defines truthiness.
# - These methods make custom objects fit naturally into Python logic.
# - This is especially helpful for collection-like classes.
