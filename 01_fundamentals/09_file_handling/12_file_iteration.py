"""
=================================================
12. File Iteration
=================================================

What is File Iteration?
-----------------------
File iteration means processing a file one line at a time.

Instead of loading the entire file into memory with read(),
Python lets us iterate over the file object directly.

Why is this useful?
-------------------
- Memory efficient.
- Faster for large files.
- Cleaner and more Pythonic.
"""

print("=" * 50)
print("FILE ITERATION")
print("=" * 50)

# -------------------------------------------------
# Setup
# -------------------------------------------------

with open("iteration_demo.txt", "w") as file:
    file.write("Python\n")
    file.write("File Handling\n")
    file.write("Iteration\n")
    file.write("Best Practices\n")

print("\nCreated iteration_demo.txt")

# -------------------------------------------------
# Example 1: Basic File Iteration
# -------------------------------------------------

print("\n1. Iterating through a file")

with open("iteration_demo.txt", "r") as file:
    for line in file:
        print(line.strip())

# -------------------------------------------------
# Example 2: Using enumerate()
# -------------------------------------------------

print("\n2. Line Numbers")

with open("iteration_demo.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")

# -------------------------------------------------
# Example 3: Skipping Empty Lines
# -------------------------------------------------

print("\n3. Skipping Empty Lines")

with open("empty_lines.txt", "w") as file:
    file.write("Apple\n")
    file.write("\n")
    file.write("Banana\n")
    file.write("\n")
    file.write("Orange\n")

with open("empty_lines.txt", "r") as file:
    for line in file:
        if line.strip():
            print(line.strip())

# -------------------------------------------------
# Example 4: Searching for a Word
# -------------------------------------------------

print("\n4. Searching")

with open("iteration_demo.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print("Found:", line.strip())

# -------------------------------------------------
# Example 5: Counting Lines
# -------------------------------------------------

print("\n5. Counting Lines")

count = 0

with open("iteration_demo.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines:", count)

# -------------------------------------------------
# Example 6: Counting Words
# -------------------------------------------------

print("\n6. Counting Words")

words = 0

with open("iteration_demo.txt", "r") as file:
    for line in file:
        words += len(line.split())

print("Total Words:", words)

# -------------------------------------------------
# Example 7: Processing Large Files
# -------------------------------------------------

print("\n7. Large File Pattern")

print("Instead of read(), use:")

print("""
with open("large.txt") as file:
    for line in file:
        process(line)
""")

# -------------------------------------------------
# Example 8: Combining with strip()
# -------------------------------------------------

print("\n8. Using strip()")

with open("iteration_demo.txt", "r") as file:
    for line in file:
        cleaned = line.strip()
        print(f"[{cleaned}]")

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

with open("iteration_demo.txt", "r") as file:
    print(file.read())

    print("Trying to iterate afterward:")

    for line in file:
        print(line)

print("Nothing printed because the cursor reached the end.")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use for line in file for large files.",
    "Use enumerate() for line numbers.",
    "Use strip() to remove newline characters.",
    "Avoid read() for huge files.",
    "Process one line at a time."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("for line in file", "Memory-efficient reading"),
    ("enumerate()", "Line numbers"),
    ("strip()", "Remove newline characters"),
    ("split()", "Split into words"),
    ("Large files", "Process one line at a time")
]

for item, value in summary:
    print(f"{item:<18}: {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Print every line with its number.")
print("2. Count the number of lines.")
print("3. Count the number of words.")
print("4. Search for a specific word.")
print("5. Ignore blank lines while reading.")

print("\nEnd of Lesson 12.")