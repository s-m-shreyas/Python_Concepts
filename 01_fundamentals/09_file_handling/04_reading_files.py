"""
=================================================
04. Reading Files
=================================================

What is Reading a File?
------------------------
Reading a file means retrieving the data stored inside it.

Python provides several ways to read files:

- read()        -> Read the entire file
- read(size)    -> Read a specific number of characters
- readline()    -> Read one line
- readlines()   -> Read all lines into a list
- for line in file -> Read line by line (recommended for large files)

This lesson demonstrates each method.
"""

print("=" * 50)
print("READING FILES")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

with open("reading_demo.txt", "w") as file:
    file.write("Python\n")
    file.write("File Handling\n")
    file.write("Reading Files\n")
    file.write("Line Four")

print("\nCreated reading_demo.txt for examples.")

# -------------------------------------------------
# Example 1: read()
# -------------------------------------------------

print("\n1. read()")

with open("reading_demo.txt", "r") as file:
    content = file.read()
    print(content)

# -------------------------------------------------
# Example 2: read(size)
# -------------------------------------------------

print("\n2. read(size)")

with open("reading_demo.txt", "r") as file:
    print(file.read(6))
    print(file.read(8))
    print(file.read())

# -------------------------------------------------
# Example 3: readline()
# -------------------------------------------------

print("\n3. readline()")

with open("reading_demo.txt", "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")

# -------------------------------------------------
# Example 4: readlines()
# -------------------------------------------------

print("\n\n4. readlines()")

with open("reading_demo.txt", "r") as file:
    lines = file.readlines()

print(lines)

print("\nAccessing individual lines:")

for index, line in enumerate(lines, start=1):
    print(f"Line {index}: {line.strip()}")

# -------------------------------------------------
# Example 5: Loop Through a File
# -------------------------------------------------

print("\n5. Reading line by line")

with open("reading_demo.txt", "r") as file:
    for line in file:
        print(line.strip())

# -------------------------------------------------
# Example 6: Empty File
# -------------------------------------------------

print("\n6. Reading an empty file")

open("empty.txt", "w").close()

with open("empty.txt", "r") as file:
    print("Content:", repr(file.read()))

# -------------------------------------------------
# Example 7: Cursor Behavior
# -------------------------------------------------

print("\n7. File cursor behavior")

with open("reading_demo.txt", "r") as file:
    print(file.read(6))
    print("Cursor:", file.tell())

    print(file.read(5))
    print("Cursor:", file.tell())

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Reading after closing
try:
    file = open("reading_demo.txt", "r")
    file.close()
    file.read()
except ValueError as e:
    print("Error:", e)

# Missing file
try:
    open("does_not_exist.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: File does not exist.")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use with open() so files close automatically.",
    "Use read() for small files.",
    "Use readline() when reading one line.",
    "Use readlines() when you need a list of lines.",
    "Use a for loop for large files."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("read()", "Entire file"),
    ("read(n)", "First n characters"),
    ("readline()", "One line"),
    ("readlines()", "List of lines"),
    ("for line in file", "Efficient line-by-line reading")
]

for method, purpose in summary:
    print(f"{method:<15} : {purpose}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create story.txt with four lines.")
print("2. Read the entire file.")
print("3. Read only the first 10 characters.")
print("4. Read each line using readline().")
print("5. Read the file using a for loop.")

print("\nEnd of Lesson 04.")