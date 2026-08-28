"""
=================================================
02. The open() Function
=================================================

What is open()?
---------------
The open() function is used to open a file so Python can
read from it, write to it, or modify it.

Syntax
------
file_object = open(file_name, mode, encoding)

Parameters
----------
1. file_name : Name or path of the file.
2. mode      : How the file should be opened.
3. encoding  : Character encoding (optional for text files).

The open() function returns a file object that allows
operations like read(), write(), and close().
"""

print("=" * 50)
print("THE open() FUNCTION")
print("=" * 50)

# -------------------------------------------------
# Example 1: Open a file for writing
# -------------------------------------------------

print("\n1. Opening a file in write mode")

file = open("demo.txt", "w")
file.write("Hello from open() function.\n")
file.close()

print("demo.txt created successfully.")

# -------------------------------------------------
# Example 2: Open a file for reading
# -------------------------------------------------

print("\n2. Opening a file in read mode")

file = open("demo.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)

# -------------------------------------------------
# Example 3: Using the default mode
# -------------------------------------------------

print("\n3. Default mode")

print("If mode is omitted, Python uses 'r' (read mode).")

file = open("demo.txt")
print(file.read())
file.close()

# -------------------------------------------------
# Example 4: Using encoding
# -------------------------------------------------

print("\n4. Using UTF-8 encoding")

file = open("utf8_demo.txt", "w", encoding="utf-8")
file.write("Hello 🌍")
file.close()

file = open("utf8_demo.txt", "r", encoding="utf-8")
print(file.read())
file.close()

# -------------------------------------------------
# Absolute vs Relative Paths
# -------------------------------------------------

print("\n5. File Paths")

print("Relative Path:")
print("   demo.txt")

print("\nAbsolute Path:")
print(r"   C:\Users\YourName\Documents\demo.txt")

# -------------------------------------------------
# Checking File Properties
# -------------------------------------------------

print("\n6. File Object Properties")

file = open("demo.txt", "r")

print("Name :", file.name)
print("Mode :", file.mode)
print("Closed:", file.closed)

file.close()

print("Closed after close():", file.closed)

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Missing file
try:
    open("unknown.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: unknown.txt does not exist.")

# Invalid mode
try:
    open("demo.txt", "invalid")
except ValueError as e:
    print("ValueError:", e)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    "open() returns a file object.",
    "Default mode is 'r'.",
    "Use encoding='utf-8' for text files.",
    "Always close files after use."
]

for item in summary:
    print("-", item)

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create practice.txt using open().")
print("2. Write your name into it.")
print("3. Read and print the contents.")
print("4. Print file.name and file.mode.")

print("\nEnd of Lesson 02.")

# -------------------------------------------------
# Mini Practice - Solution
# -------------------------------------------------

file = open(r'practice.txt', 'w')
file.write('S.M.Shreyas\n')

file = open(r'practice.txt', 'r')
print(file.read())
print(file.name)
print(file.mode)