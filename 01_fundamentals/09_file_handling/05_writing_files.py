# type: ignore

"""
=================================================
05. Writing Files
=================================================

What is Writing to a File?
---------------------------
Writing means storing data inside a file.

Python provides two main methods:

- write()       -> Write a string
- writelines()  -> Write multiple strings

Most writing is done using 'w' (write) mode.
"""

print("=" * 50)
print("WRITING FILES")
print("=" * 50)

# -------------------------------------------------
# Example 1: write()
# -------------------------------------------------

print("\n1. Writing using write()")

with open("write_demo.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning File Handling.\n")

print("write_demo.txt created.")

with open("write_demo.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 2: write() returns number of characters
# -------------------------------------------------

print("\n2. write() return value")

with open("count_demo.txt", "w") as file:
    count = file.write("Python")

print("Characters written:", count)

# -------------------------------------------------
# Example 3: Overwriting Existing Content
# -------------------------------------------------

print("\n3. Overwriting a file")

with open("overwrite_demo.txt", "w") as file:
    file.write("Old Content")

# Opening again in 'w' removes previous content
with open("overwrite_demo.txt", "w") as file:
    file.write("New Content")

with open("overwrite_demo.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 4: writelines()
# -------------------------------------------------

print("\n4. Using writelines()")

lines = [
    "Apple\n",
    "Banana\n",
    "Orange\n"
]

with open("fruits.txt", "w") as file:
    file.writelines(lines)

with open("fruits.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 5: Newline Behavior
# -------------------------------------------------

print("\n5. Newline behavior")

with open("newline_demo.txt", "w") as file:
    file.write("Line One")
    file.write("Line Two")

print("Without '\\n':")

with open("newline_demo.txt", "r") as file:
    print(file.read())

with open("newline_demo.txt", "w") as file:
    file.write("Line One\n")
    file.write("Line Two\n")

print("\nWith '\\n':")

with open("newline_demo.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 6: Writing User Data
# -------------------------------------------------

print("\n6. Writing formatted text")

name = "Alice"
age = 25

with open("user_info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age : {age}\n")

with open("user_info.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Writing after closing
try:
    file = open("temp.txt", "w")
    file.close()
    file.write("Hello")
except ValueError as e:
    print("Error:", e)

# Writing non-string data
try:
    with open("numbers.txt", "w") as file:
        file.write(100)
except TypeError as e:
    print("TypeError:", e)

# Correct approach
with open("numbers.txt", "w") as file:
    file.write(str(100))

print("Number written successfully.")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use with open() for automatic closing.",
    "Remember that 'w' overwrites existing content.",
    "Add '\\n' when writing multiple lines.",
    "Convert numbers to strings before writing.",
    "Use writelines() for multiple strings."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("write()", "Write one string"),
    ("writelines()", "Write multiple strings"),
    ("w mode", "Overwrite existing content"),
    ("\\n", "Start a new line"),
    ("str()", "Convert non-strings before writing")
]

for method, purpose in summary:
    print(f"{method:<15} : {purpose}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create notes.txt.")
print("2. Write three lines using write().")
print("3. Create another file using writelines().")
print("4. Store your name and city in a file.")
print("5. Try writing a number using str().")

print("\nEnd of Lesson 05.")