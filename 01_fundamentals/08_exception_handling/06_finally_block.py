# type: ignore

"""
===============================================================================
Topic    : The finally Block in Exception Handling
File     : 06_finally_block.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Python's 'finally' block, which executes regardless of
whether an exception occurs. It is commonly used for resource cleanup, such as
closing files, releasing database connections, and freeing system resources.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What the finally block is.
2. When finally executes.
3. Execution flow of try-except-else-finally.
4. Resource cleanup using finally.
5. Real-world examples.
6. Best practices and common mistakes.

Run this file
-------------
python 06_finally_block.py
===============================================================================
"""

print("=" * 80)
print("THE FINALLY BLOCK IN EXCEPTION HANDLING")
print("=" * 80)

# =============================================================================
# What is the finally Block?
# =============================================================================

print("\n1. WHAT IS THE FINALLY BLOCK?")
print("-" * 40)

"""
The finally block executes regardless of whether an exception occurs.

It is primarily used for cleanup operations.

Execution Flow

try
 ├── Success → else (optional) → finally
 └── Exception → except → finally

The finally block is guaranteed to execute before the program leaves
the try-except structure.
"""

print("The finally block guarantees cleanup.")


# =============================================================================
# Basic Syntax
# =============================================================================

print("\n2. BASIC SYNTAX")
print("-" * 40)

"""
Structure

try:
    risky_code()

except ExceptionType:
    handle_error()

finally:
    cleanup()

The finally block is optional but highly recommended when resources
need to be released.
"""

print("Basic syntax understood.")


# =============================================================================
# Example: No Exception
# =============================================================================

print("\n3. EXAMPLE: NO EXCEPTION")
print("-" * 40)

try:
    print("Task completed successfully.")

finally:
    print("Cleanup completed.")

print("Notice that finally executed even though nothing failed.")


# =============================================================================
# Example: Exception Occurs
# =============================================================================

print("\n4. EXAMPLE: EXCEPTION OCCURS")
print("-" * 40)

try:
    print("Performing calculation...")
    result = 10 / 0

except ZeroDivisionError:
    print("Division by zero handled.")

finally:
    print("Cleanup always executes.")

print("Program continues safely.")


# =============================================================================
# try-except-else-finally Together
# =============================================================================

print("\n5. COMPLETE EXECUTION FLOW")
print("-" * 40)

try:
    number = int("50")

except ValueError:
    print("Conversion failed.")

else:
    print("Conversion succeeded.")

finally:
    print("Final cleanup executed.")

print("""
Execution order

Success:
    try → else → finally

Failure:
    try → except → finally
""")


# =============================================================================
# Real-World Example: File Handling
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE: FILE HANDLING")
print("-" * 40)

"""
Files should always be closed after use.

finally guarantees that the file closes even if an error occurs.
"""

file = None

try:
    file = open("demo_file.txt", "w")
    file.write("Python Concepts Repository")

finally:
    if file:
        file.close()
        print("File closed successfully.")


# =============================================================================
# Simulated Database Connection
# =============================================================================

print("\n7. SIMULATED DATABASE CONNECTION")
print("-" * 40)

"""
Imagine a database connection.

Even if a query fails,
the connection should always close.
"""

connection_open = False

try:
    print("Opening database connection...")
    connection_open = True

    print("Executing query...")
    raise RuntimeError("Database timeout")

except RuntimeError as error:
    print("Database error:", error)

finally:
    if connection_open:
        print("Closing database connection...")
        connection_open = False

print("Connection cleaned up safely.")


# =============================================================================
# Multiple Cleanup Tasks
# =============================================================================

print("\n8. MULTIPLE CLEANUP TASKS")
print("-" * 40)

resources = []

try:
    print("Allocating resources...")
    resources.extend(["File", "Socket", "Cache"])

    raise RuntimeError("Unexpected failure")

except RuntimeError:
    print("Operation failed.")

finally:
    while resources:
        resource = resources.pop()
        print(f"Released: {resource}")

print("All resources were released.")


# =============================================================================
# finally with return
# =============================================================================

print("\n9. FINALLY WITH RETURN")
print("-" * 40)

"""
Even when a function returns,
finally still executes first.
"""

def example_function():

    try:
        return "Returned from try"

    finally:
        print("finally executed before returning.")

print(example_function())


# =============================================================================
# Best Practices
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Use finally for cleanup operations.",
    "Close files and database connections.",
    "Release external resources.",
    "Keep cleanup code simple.",
    "Prefer the with statement for files when possible."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n11. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Forgetting cleanup.

Bad:

file = open("data.txt")
# program crashes
# file remains open

Better:

try:
    ...
finally:
    file.close()

❌ Putting important business logic inside finally.

finally should focus on cleanup.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n12. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
When does the finally block execute?

Answer:
The finally block executes whether the try block succeeds, fails,
returns, or raises an exception.

Its primary purpose is resource cleanup.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n13. QUICK REVISION")
print("-" * 40)

revision = [
    ("try", "Risky code"),
    ("except", "Handles exceptions"),
    ("else", "Runs on success"),
    ("finally", "Always runs"),
]

for concept, meaning in revision:
    print(f"{concept:<12} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n14. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "finally always executes.",
    "Use it for cleanup operations.",
    "It works whether exceptions occur or not.",
    "Files and database connections should be cleaned up safely.",
    "The with statement is often preferred for file handling."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 06_finally_block.py")
print("=" * 80)