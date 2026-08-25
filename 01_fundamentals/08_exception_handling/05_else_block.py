# type: ignore

"""
===============================================================================
Topic    : The else Block in Exception Handling
File     : 05_else_block.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Python's 'else' block in exception handling.
The else block executes only when the try block completes successfully,
making it useful for separating successful execution from error handling.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What the else block is.
2. When else executes.
3. The execution flow of try-except-else.
4. Why else makes code cleaner.
5. Real-world examples.
6. Best practices and common mistakes.

Run this file
-------------
python 05_else_block.py
===============================================================================
"""

print("=" * 80)
print("THE ELSE BLOCK IN EXCEPTION HANDLING")
print("=" * 80)

# =============================================================================
# What is the else Block?
# =============================================================================

print("\n1. WHAT IS THE ELSE BLOCK?")
print("-" * 40)

"""
The else block executes only when the try block finishes successfully.

Execution Flow

try
 ├── No Exception → else executes
 └── Exception → matching except executes

The else block never runs if an exception occurs.
"""

print("The else block separates successful execution from error handling.")


# =============================================================================
# Basic Syntax
# =============================================================================

print("\n2. BASIC SYNTAX")
print("-" * 40)

"""
Structure:

try:
    risky_code()
except ExceptionType:
    handle_error()
else:
    success_code()

The else block is optional.
"""

print("Basic syntax understood.")


# =============================================================================
# Example: Successful Execution
# =============================================================================

print("\n3. EXAMPLE: SUCCESSFUL EXECUTION")
print("-" * 40)

try:
    number = int("100")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful.")
    print(f"Converted number: {number}")

print("The else block executed because no exception occurred.")


# =============================================================================
# Example: Exception Occurs
# =============================================================================

print("\n4. EXAMPLE: EXCEPTION OCCURS")
print("-" * 40)

try:
    number = int("Python")
except ValueError:
    print("Invalid input.")
else:
    print("This never executes.")

print("The else block was skipped.")


# =============================================================================
# Why Not Put Everything Inside try?
# =============================================================================

print("\n5. WHY USE ELSE?")
print("-" * 40)

"""
Consider this approach.

Bad Example:

try:
    number = int("50")
    print(number)
    print("Processing data...")
except ValueError:
    ...

The second print() is unrelated to the risky operation.

A better approach is to move successful work into else.
"""

try:
    number = int("50")
except ValueError:
    print("Conversion failed.")
else:
    print("Processing data...")
    print("Saving results...")

print("The try block now contains only risky code.")


# =============================================================================
# Real-World Example: User Login
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE")
print("-" * 40)

"""
Imagine a login system.

The risky operation is converting a PIN entered by the user.
Only after successful conversion should we verify access.
"""

user_inputs = ["1234", "abcd"]

for pin in user_inputs:

    print(f"\nInput: {pin}")

    try:
        pin_number = int(pin)

    except ValueError:
        print("PIN must contain only digits.")

    else:
        print(f"PIN accepted: {pin_number}")
        print("Access verification started.")

print("\nThe else block keeps validation and processing separate.")


# =============================================================================
# Execution Flow Demonstration
# =============================================================================

print("\n7. EXECUTION FLOW")
print("-" * 40)

print("Scenario A: Success")

try:
    print("Try executed.")
except Exception:
    print("Except executed.")
else:
    print("Else executed.")

print("\nScenario B: Failure")

try:
    raise ValueError("Example error")
except ValueError:
    print("Except executed.")
else:
    print("Else executed.")

print("""
Execution Summary

Success:
    try → else

Failure:
    try → except
""")


# =============================================================================
# else vs finally
# =============================================================================

print("\n8. ELSE VS FINALLY")
print("-" * 40)

print("""
else
----
Runs only when try succeeds.

finally
-------
Runs whether try succeeds or fails.

Think of them this way:

else:
    "Everything worked."

finally:
    "Clean up no matter what."
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n9. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Keep only risky code inside try.",
    "Move success-only logic into else.",
    "Keep exception handling focused.",
    "Use else to improve readability."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n10. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Putting unrelated code inside try.

Bad:

try:
    open_file()
    process_data()
    save_results()

Better:

try:
    open_file()
except FileNotFoundError:
    ...
else:
    process_data()
    save_results()
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n11. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
When does the else block execute?

Answer:
The else block executes only if the try block completes without raising
an exception.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n12. QUICK REVISION")
print("-" * 40)

revision = [
    ("try", "Risky code"),
    ("except", "Handles errors"),
    ("else", "Runs on success"),
    ("finally", "Always runs")
]

for concept, meaning in revision:
    print(f"{concept:<12} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n13. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "The else block executes only when no exception occurs.",
    "It keeps successful logic separate from error handling.",
    "The try block should contain only risky operations.",
    "Using else improves readability and maintainability.",
    "else and finally serve different purposes."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 05_else_block.py")
print("=" * 80)