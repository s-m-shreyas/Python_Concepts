# type: ignore

"""
03_comparison_methods.py

Demonstrates comparison dunder methods such as <, <=, >, >=.

These methods allow custom objects to be ordered naturally.
"""


# ============================================================
# 1. ORDERING OBJECTS BY A VALUE
# ============================================================

class Student:
    """Student with a score attribute."""

    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.score < other.score

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.score <= other.score

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.score > other.score

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.score >= other.score


s1 = Student("Amit", 90)
s2 = Student("Neha", 85)

print(s1 > s2)
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)

"""
The comparison is based on score, which gives the objects a clear
ordering in a business sense.
"""


# ============================================================
# 2. SORTING CUSTOM OBJECTS
# ============================================================

students = [
    Student("Ravi", 82),
    Student("Kavya", 95),
    Student("Anu", 88),
]

sorted_students = sorted(students)
for student in sorted_students:
    print(student.name, student.score)

"""
sorted() uses comparison methods to order objects by score.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __lt__, __le__, __gt__, __ge__ define ordering.
# - They make custom objects comparable with Python operators.
# - This is useful in sorting, ranking, and business logic.
# - Custom comparison logic makes programs more readable.
