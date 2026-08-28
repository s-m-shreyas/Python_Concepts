# type: ignore

"""
=================================================
09. The with Statement
=================================================

What is the with Statement?
---------------------------
The 'with' statement is Python's recommended way to work
with files.

It automatically closes the file when the block finishes,
even if an exception occurs.

Without with:
--------------
file = open("data.txt", "r")
content = file.read()
file.close()

With with:
-----------
with open("data.txt", "r") as file:
    content = file.read()

The second approach is safer and cleaner.
"""

print("=" * 50)
print("THE with STATEMENT")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

with open("with_demo.txt", "w") as file:
    file.write("Python\n")
    file.write("File Handling\n")
    file.write("Using with Statement")

print("\nCreated with_demo.txt")

# -------------------------------------------------
# Example 1: Reading with 'with'
# -------------------------------------------------

print("\n1. Reading with with")

with open("with_demo.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 2: Writing with 'with'
# -------------------------------------------------

print("\n2. Writing with with")

with open("write_with.txt", "w") as file:
    file.write("Writing safely.\n")
    file.write("Automatic closing.")

print("write_with.txt created.")

with open("write_with.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 3: Appending with 'with'
# -------------------------------------------------

print("\n3. Appending with with")

with open("write_with.txt", "a") as file:
    file.write("\nAppended successfully.")

with open("write_with.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 4: Automatic Closing
# -------------------------------------------------

print("\n4. Automatic Closing")

with open("with_demo.txt", "r") as file:
    print("Inside block:", file.closed)

print("Outside block:", file.closed)

# -------------------------------------------------
# Example 5: Exception Safety
# -------------------------------------------------

print("\n5. Exception Safety")

try:
    with open("with_demo.txt", "r") as file:
        print(file.readline())

        # Force an error
        10 / 0

except ZeroDivisionError:
    print("An exception occurred.")

print("File is still closed:", file.closed)

# -------------------------------------------------
# Example 6: Multiple Files
# -------------------------------------------------

print("\n6. Opening Multiple Files")

with open("source.txt", "w") as file:
    file.write("Copy this text.")

with open("source.txt", "r") as source, \
     open("destination.txt", "w") as destination:

    destination.write(source.read())

with open("destination.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Trying to use a file after leaving the with block
try:
    with open("with_demo.txt", "r") as file:
        text = file.read()

    file.read()

except ValueError as e:
    print("Error:", e)

# -------------------------------------------------
# Why 'with' is Better
# -------------------------------------------------

print("\nWhy 'with' is Better")

advantages = [
    "Automatically closes files.",
    "Works even if an exception occurs.",
    "Reduces code.",
    "Prevents resource leaks.",
    "Recommended by Python."
]

for item in advantages:
    print("-", item)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("with", "Automatic resource management"),
    ("as file", "Stores the file object"),
    ("Auto close", "Yes"),
    ("Exception Safe", "Yes"),
    ("Recommended", "Always")
]

for item, value in summary:
    print(f"{item:<18}: {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create notes.txt using with.")
print("2. Write three lines.")
print("3. Read and print the file.")
print("4. Append another line.")
print("5. Open two files and copy content.")

print("\nEnd of Lesson 09.")