"""
=================================================
06. Appending Files
=================================================

What is Appending?
------------------
Appending means adding new data to the END of an existing file
without removing its previous content.

Python uses 'a' (append) mode for this purpose.

Difference:
- 'w' -> Overwrites existing content.
- 'a' -> Preserves existing content and adds new data.
"""

print("=" * 50)
print("APPENDING FILES")
print("=" * 50)

# -------------------------------------------------
# Example 1: Basic Append
# -------------------------------------------------

print("\n1. Basic Append")

with open("journal.txt", "w") as file:
    file.write("Day 1: Started learning Python.\n")

with open("journal.txt", "a") as file:
    file.write("Day 2: Learned file handling.\n")
    file.write("Day 3: Practiced append mode.\n")

with open("journal.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 2: Append Creates a File
# -------------------------------------------------

print("\n2. Append creates a file if it doesn't exist")

with open("new_notes.txt", "a") as file:
    file.write("First note.\n")

print("new_notes.txt created successfully.")

# -------------------------------------------------
# Example 3: Cursor Position in Append Mode
# -------------------------------------------------

print("\n3. Cursor position")

with open("journal.txt", "a") as file:
    print("Cursor Position:", file.tell())

    file.write("Day 4: Cursor starts at the end.\n")

with open("journal.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 4: Append Multiple Lines
# -------------------------------------------------

print("\n4. Append multiple lines")

new_tasks = [
    "Task 1\n",
    "Task 2\n",
    "Task 3\n"
]

with open("tasks.txt", "w") as file:
    file.write("Today's Tasks:\n")

with open("tasks.txt", "a") as file:
    file.writelines(new_tasks)

with open("tasks.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 5: Logging Example
# -------------------------------------------------

print("\n5. Simple Log File")

events = [
    "Program Started",
    "User Logged In",
    "File Saved"
]

with open("app.log", "a") as file:
    for event in events:
        file.write(f"{event}\n")

with open("app.log", "r") as file:
    print(file.read())

# -------------------------------------------------
# Example 6: Append vs Write
# -------------------------------------------------

print("\n6. Append vs Write")

with open("compare.txt", "w") as file:
    file.write("Original Content\n")

with open("compare.txt", "a") as file:
    file.write("Added using append\n")

print("After append:")

with open("compare.txt", "r") as file:
    print(file.read())

with open("compare.txt", "w") as file:
    file.write("Replaced using write")

print("After write:")

with open("compare.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Forgetting a newline
with open("mistake.txt", "w") as file:
    file.write("Line One")

with open("mistake.txt", "a") as file:
    file.write("Line Two")

print("Without newline:")

with open("mistake.txt", "r") as file:
    print(file.read())

# Correct version
with open("mistake.txt", "w") as file:
    file.write("Line One\n")

with open("mistake.txt", "a") as file:
    file.write("Line Two\n")

print("With newline:")

with open("mistake.txt", "r") as file:
    print(file.read())

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use append mode for logs and journals.",
    "Append never deletes existing content.",
    "Use '\\n' when writing new lines.",
    "Use with open() for automatic closing."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("a", "Append to end of file"),
    ("Creates file?", "Yes"),
    ("Overwrites?", "No"),
    ("Cursor", "Starts at the end"),
    ("writelines()", "Append multiple strings")
]

for item, value in summary:
    print(f"{item:<15} : {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create diary.txt.")
print("2. Write one entry using 'w'.")
print("3. Add two more entries using 'a'.")
print("4. Create a log file that stores three events.")
print("5. Try appending without '\\n' and observe the result.")

print("\nEnd of Lesson 06.")