"""
=================================================
03. File Modes
=================================================

What are File Modes?
--------------------
File modes tell Python how a file should be opened.

Examples:
- Read an existing file.
- Create a new file.
- Write new data.
- Append data.
- Work with binary files.

Syntax
------
open(file_name, mode)

Common Modes
------------
r   -> Read
w   -> Write
a   -> Append
x   -> Create
r+  -> Read and Write
w+  -> Write and Read
a+  -> Append and Read
b   -> Binary Mode
t   -> Text Mode (default)
"""

print("=" * 50)
print("PYTHON FILE MODES")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

# Create a sample file for demonstrations.
with open("sample_modes.txt", "w") as file:
    file.write("Line 1\nLine 2\n")

# -------------------------------------------------
# Read Mode (r)
# -------------------------------------------------

print("\n1. Read Mode (r)")

with open("sample_modes.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Write Mode (w)
# -------------------------------------------------

print("\n2. Write Mode (w)")

with open("write_mode.txt", "w") as file:
    file.write("Old content is replaced.\n")

print("write_mode.txt created.")

# Demonstrate overwriting.
with open("write_mode.txt", "w") as file:
    file.write("New content after overwrite.")

with open("write_mode.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Append Mode (a)
# -------------------------------------------------

print("\n3. Append Mode (a)")

with open("append_mode.txt", "w") as file:
    file.write("First Line\n")

with open("append_mode.txt", "a") as file:
    file.write("Second Line\n")
    file.write("Third Line\n")

with open("append_mode.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Exclusive Create Mode (x)
# -------------------------------------------------

print("\n4. Create Mode (x)")

try:
    with open("new_file.txt", "x") as file:
        file.write("Created successfully.")
    print("new_file.txt created.")
except FileExistsError:
    print("new_file.txt already exists.")

# -------------------------------------------------
# Read and Write (r+)
# -------------------------------------------------

print("\n5. Read and Write Mode (r+)")

with open("sample_modes.txt", "r+") as file:
    print("Before writing:")
    print(file.read())

    file.seek(0)
    file.write("Updated")

with open("sample_modes.txt", "r") as file:
    print("\nAfter update:")
    print(file.read())

# Restore original content for later examples.
with open("sample_modes.txt", "w") as file:
    file.write("Line 1\nLine 2\n")

# -------------------------------------------------
# Write and Read (w+)
# -------------------------------------------------

print("\n6. Write and Read Mode (w+)")

with open("wplus.txt", "w+") as file:
    file.write("Hello World")
    file.seek(0)
    print(file.read())

# -------------------------------------------------
# Append and Read (a+)
# -------------------------------------------------

print("\n7. Append and Read Mode (a+)")

with open("aplus.txt", "a+") as file:
    file.write("Python\n")
    file.write("File Handling\n")

    file.seek(0)
    print(file.read())

# -------------------------------------------------
# Binary Mode (b)
# -------------------------------------------------

print("\n8. Binary Mode (rb / wb)")

with open("binary_demo.bin", "wb") as file:
    file.write(b"ABC123")

with open("binary_demo.bin", "rb") as file:
    print(file.read())

# -------------------------------------------------
# Text Mode (t)
# -------------------------------------------------

print("\n9. Text Mode (default)")

with open("text_demo.txt", "wt") as file:
    file.write("Text Mode Example")

with open("text_demo.txt", "rt") as file:
    print(file.read())

# -------------------------------------------------
# Mode Comparison Table
# -------------------------------------------------

print("\nMode Comparison")

comparison = [
    ("r", "Read existing file"),
    ("w", "Write (overwrite)"),
    ("a", "Append"),
    ("x", "Create new file"),
    ("r+", "Read and Write"),
    ("w+", "Write and Read"),
    ("a+", "Append and Read"),
    ("rb", "Read binary"),
    ("wb", "Write binary"),
    ("rt", "Read text"),
    ("wt", "Write text")
]

for mode, purpose in comparison:
    print(f"{mode:<4} : {purpose}")

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

try:
    open("missing.txt", "r")
except FileNotFoundError:
    print("Read mode cannot open missing files.")

try:
    open("sample_modes.txt", "invalid")
except ValueError:
    print("Invalid file mode raises ValueError.")


# -------------------------------------------------
# Quick Notes: seek() and tell()
# -------------------------------------------------

print("\nQuick Notes: seek() and tell()")

print("seek(position) -> Moves the file cursor to a specific position.")
print("tell() -> Returns the current position of the file cursor.")

with open("sample_modes.txt", "r") as file:
    print("Initial Position:", file.tell())   # 0

    file.read(5)

    print("After reading 5 characters:", file.tell())   # 5

    file.seek(0)

    print("After seek(0):", file.tell())   # 0
    
# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create diary.txt using 'w'.")
print("2. Add another entry using 'a'.")
print("3. Read it using 'r'.")
print("4. Create a binary file and read it back.")

print("\nEnd of Lesson 03.")