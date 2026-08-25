# type: ignore

"""
===============================================================================
Topic    : Handling Multiple Exceptions
File     : 03_multiple_exceptions.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains how Python handles multiple exceptions using multiple
'except' blocks and by catching multiple exception types in a single block.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. Why multiple exception handling is useful.
2. Using multiple except blocks.
3. Catching multiple exception types together.
4. Exception hierarchy.
5. Why the order of except blocks matters.
6. Real-world examples.
7. Best practices.

Run this file
-------------
python 03_multiple_exceptions.py
===============================================================================
"""

print("=" * 80)
print("HANDLING MULTIPLE EXCEPTIONS")
print("=" * 80)

# =============================================================================
# Why Handle Multiple Exceptions?
# =============================================================================

print("\n1. WHY HANDLE MULTIPLE EXCEPTIONS?")
print("-" * 40)

"""
A single block of code can fail in different ways.

Example:
- User enters invalid text → ValueError
- User divides by zero → ZeroDivisionError

Instead of writing separate programs, Python allows us to handle each
exception appropriately.
"""

print("One try block can have multiple possible exceptions.")


# =============================================================================
# Multiple except Blocks
# =============================================================================

print("\n2. MULTIPLE EXCEPT BLOCKS")
print("-" * 40)

print("Example A: ValueError")

try:
    number = int("Python")
    print(number)
except ValueError:
    print("ValueError handled.")
except ZeroDivisionError:
    print("ZeroDivisionError handled.")

print("\nExample B: ZeroDivisionError")

try:
    result = 100 / 0
    print(result)
except ValueError:
    print("ValueError handled.")
except ZeroDivisionError:
    print("ZeroDivisionError handled.")

print("""
Python checks each except block from top to bottom.
The first matching handler executes.
""")


# =============================================================================
# Catching Multiple Exceptions Together
# =============================================================================

print("\n3. CATCHING MULTIPLE EXCEPTIONS TOGETHER")
print("-" * 40)

"""
If different exceptions require the same handling,
they can be grouped together.
"""

examples = ["Python", 0]

for item in examples:
    try:
        if item == 0:
            print(10 / item)
        else:
            print(int(item))
    except (ValueError, ZeroDivisionError):
        print(f"Handled error for input: {item}")

print("""
Syntax:

except (ValueError, ZeroDivisionError):
    ...
""")


# =============================================================================
# Exception Hierarchy
# =============================================================================

print("\n4. EXCEPTION HIERARCHY")
print("-" * 40)

"""
All exceptions inherit from BaseException.

BaseException
│
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── IndexError
│   ├── KeyError
│   ├── FileNotFoundError
│   └── ZeroDivisionError
│
├── KeyboardInterrupt
└── SystemExit

Because of inheritance, catching Exception also catches
most built-in runtime exceptions.
"""

print("Exceptions follow an inheritance hierarchy.")


# =============================================================================
# Order Matters
# =============================================================================

print("\n5. ORDER OF EXCEPT BLOCKS")
print("-" * 40)

print("Correct Order")

try:
    int("Python")
except ValueError:
    print("Specific handler executed.")
except Exception:
    print("Generic handler executed.")

print("""
The specific exception executes first.
""")

print("\nIncorrect Order (Example Only)")

"""
The following is incorrect:

try:
    int("Python")
except Exception:
    ...
except ValueError:
    ...

The ValueError block becomes unreachable because Exception
already catches it.

Python raises:

SyntaxError:
except clauses are in the wrong order
"""

print("Always place specific exceptions before generic ones.")


# =============================================================================
# Real-World Example
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE")
print("-" * 40)

"""
Imagine a calculator.

Possible failures:
- Invalid number
- Division by zero
"""

test_cases = [
    ("25", "5"),
    ("hello", "5"),
    ("10", "0")
]

for first, second in test_cases:

    print(f"\nInput: {first}, {second}")

    try:
        num1 = float(first)
        num2 = float(second)
        print("Result:", num1 / num2)

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

print("\nCalculator continues running safely.")


# =============================================================================
# Generic Exception Handling
# =============================================================================

print("\n7. GENERIC EXCEPTION HANDLING")
print("-" * 40)

"""
Sometimes unexpected exceptions should be logged.

Avoid using this unless necessary.
"""

try:
    value = [1, 2, 3]
    print(value[10])

except Exception as error:
    print("Unexpected error occurred:", error)

print("""
Generic handling is useful for logging,
but specific exceptions should be preferred.
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n8. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Handle specific exceptions first.",
    "Group exceptions only when handling is identical.",
    "Use Exception as a last resort.",
    "Write meaningful error messages.",
    "Keep try blocks small."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n9. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Wrong order of except blocks.

except Exception
except ValueError

This makes ValueError unreachable.

❌ Catching unrelated exceptions together.

Only combine exceptions when both require
the same response.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n10. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
Why should specific exceptions come before Exception?

Answer:
Exception is the parent class for most runtime exceptions.
If it appears first, it catches child exceptions immediately,
making later handlers unreachable.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n11. QUICK REVISION")
print("-" * 40)

revision = [
    ("Multiple except blocks", "Different handling"),
    ("except (A, B)", "Same handling"),
    ("Exception", "Generic parent class"),
    ("Order", "Specific → Generic")
]

for concept, meaning in revision:
    print(f"{concept:<25} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n12. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "One try block can handle multiple exception types.",
    "Use separate except blocks for different responses.",
    "Group exceptions when handling is identical.",
    "Exception hierarchy affects handler behavior.",
    "Specific handlers must come before generic ones."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 03_multiple_exceptions.py")
print("=" * 80)