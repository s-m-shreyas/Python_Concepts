"""
=================================================
07. File Position (File Cursor)
=================================================

What is File Position?
----------------------
Every open file has a file cursor (also called a file pointer).

The cursor represents the current position inside the file,
where the next read or write operation will occur.

Think of it as a bookmark that moves automatically as you
read or write data.

File Content
------------
Python File Handling

Cursor at Start
        ↓
Python File Handling
^
Position 0
"""

print("=" * 50)
print("FILE POSITION (FILE CURSOR)")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

with open("cursor_demo.txt", "w") as file:
    file.write("Python File Handling")

print("\nCreated cursor_demo.txt")

# -------------------------------------------------
# Example 1: Initial Cursor Position
# -------------------------------------------------

print("\n1. Initial Cursor Position")

with open("cursor_demo.txt", "r") as file:
    print("Cursor:", file.tell())  # 0

# -------------------------------------------------
# Example 2: Cursor Moves While Reading
# -------------------------------------------------

print("\n2. Cursor Moves Automatically")

with open("cursor_demo.txt", "r") as file:
    print("Read:", file.read(6))
    print("Cursor:", file.tell())

    print("Read:", file.read(5))
    print("Cursor:", file.tell())

# -------------------------------------------------
# Example 3: Cursor at End of File
# -------------------------------------------------

print("\n3. Cursor at End")

with open("cursor_demo.txt", "r") as file:
    print(file.read())
    print("Cursor:", file.tell())

    print("Reading again:", repr(file.read()))

# -------------------------------------------------
# Example 4: Cursor While Writing
# -------------------------------------------------

print("\n4. Cursor During Writing")

with open("write_cursor.txt", "w") as file:
    print("Start:", file.tell())

    file.write("Hello")
    print("After 'Hello':", file.tell())

    file.write(" World")
    print("After ' World':", file.tell())

# -------------------------------------------------
# Example 5: Cursor in Append Mode
# -------------------------------------------------

print("\n5. Cursor in Append Mode")

with open("append_cursor.txt", "w") as file:
    file.write("Line One\n")

with open("append_cursor.txt", "a") as file:
    print("Starting Position:", file.tell())

    file.write("Line Two\n")
    print("After Writing:", file.tell())

with open("append_cursor.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 6: Resetting the Cursor
# -------------------------------------------------

print("\n6. Resetting the Cursor")

with open("cursor_demo.txt", "r") as file:
    print(file.read(6))
    print("Cursor:", file.tell())

    file.seek(0)

    print("After seek(0):", file.tell())
    print(file.read(6))

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

with open("cursor_demo.txt", "r") as file:
    print(file.read())
    print("Second read:", repr(file.read()))

print("The cursor stayed at the end.")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Remember that every read moves the cursor.",
    "Use tell() to check the current position.",
    "Use seek() to move the cursor.",
    "Reset to the beginning with seek(0)."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("Cursor", "Current position in a file"),
    ("Initial Position", "0"),
    ("Reading", "Moves the cursor forward"),
    ("Writing", "Moves the cursor forward"),
    ("seek(0)", "Return to beginning"),
    ("tell()", "Current cursor position")
]

for item, value in summary:
    print(f"{item:<18}: {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create a file with the text 'Python Programming'.")
print("2. Read the first 6 characters.")
print("3. Print the cursor position.")
print("4. Read the next 5 characters.")
print("5. Reset the cursor with seek(0).")
print("6. Read the first 6 characters again.")

print("\nEnd of Lesson 07.")