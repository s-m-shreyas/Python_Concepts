"""
=================================================
08. seek() and tell()
=================================================

What are seek() and tell()?
---------------------------
- seek() moves the file cursor to a specific position.
- tell() returns the current cursor position.

These methods allow you to navigate inside a file instead of
reading or writing only from the current position.
"""

print("=" * 50)
print("SEEK() AND TELL()")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

with open("seek_demo.txt", "w") as file:
    file.write("Python File Handling")

print("\nCreated seek_demo.txt")

# -------------------------------------------------
# Example 1: tell()
# -------------------------------------------------

print("\n1. tell()")

with open("seek_demo.txt", "r") as file:
    print("Initial Position:", file.tell())

    file.read(6)

    print("After reading 6 characters:", file.tell())

# -------------------------------------------------
# Example 2: seek(0)
# -------------------------------------------------

print("\n2. seek(0)")

with open("seek_demo.txt", "r") as file:
    print(file.read(6))

    file.seek(0)

    print("Position:", file.tell())
    print(file.read(6))

# -------------------------------------------------
# Example 3: Jump to a Specific Position
# -------------------------------------------------

print("\n3. seek(7)")

with open("seek_demo.txt", "r") as file:
    file.seek(7)

    print("Position:", file.tell())
    print(file.read())

# -------------------------------------------------
# Example 4: Reading Different Sections
# -------------------------------------------------

print("\n4. Reading Different Parts")

with open("seek_demo.txt", "r") as file:
    file.seek(0)
    print("First:", file.read(6))

    file.seek(7)
    print("Second:", file.read(4))

    file.seek(12)
    print("Third:", file.read())

# -------------------------------------------------
# Example 5: seek() in Write Mode
# -------------------------------------------------

print("\n5. seek() while writing")

with open("modify_demo.txt", "w+") as file:
    file.write("Hello World")

    file.seek(6)
    file.write("Python")

    file.seek(0)
    print(file.read())

# -------------------------------------------------
# Example 6: Binary File Position
# -------------------------------------------------

print("\n6. Binary Files")

with open("binary_seek.bin", "wb") as file:
    file.write(b"ABCDEFGH")

with open("binary_seek.bin", "rb") as file:
    file.seek(3)
    print(file.read(2))

# -------------------------------------------------
# Example 7: seek() with whence
# -------------------------------------------------

print("\n7. seek() with whence")

with open("binary_seek.bin", "rb") as file:

    file.seek(2, 0)
    print("From beginning:", file.read(1))

    file.seek(-2, 2)
    print("From end:", file.read())

# -------------------------------------------------
# Understanding whence
# -------------------------------------------------

print("\nwhence Values")

whence = [
    (0, "Beginning of file"),
    (1, "Current position"),
    (2, "End of file")
]

for value, meaning in whence:
    print(f"{value} : {meaning}")

# -------------------------------------------------
# Practical Example: Re-read a File
# -------------------------------------------------

print("\n8. Re-reading a file")

with open("seek_demo.txt", "r") as file:
    print(file.read())

    file.seek(0)

    print("\nReading again:")
    print(file.read())

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

with open("seek_demo.txt", "r") as file:
    file.read()

    print("Second read:", repr(file.read()))

    file.seek(0)

    print("After seek(0):", file.read(6))

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use tell() to inspect the current position.",
    "Use seek(0) to restart reading.",
    "Use seek(position) for random access.",
    "Negative offsets are commonly used with binary files."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("tell()", "Current cursor position"),
    ("seek(0)", "Go to beginning"),
    ("seek(n)", "Jump to position n"),
    ("seek(-2, 2)", "Move relative to end"),
    ("Random Access", "Read specific locations")
]

for method, purpose in summary:
    print(f"{method:<15}: {purpose}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Read the first five characters.")
print("2. Print the cursor position.")
print("3. Jump back to the beginning.")
print("4. Jump to character position 10.")
print("5. Create a binary file and read its last two bytes.")

print("\nEnd of Lesson 08.")