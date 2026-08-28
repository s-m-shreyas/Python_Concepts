"""
=================================================
01. File Handling Basics
=================================================

What is File Handling?
----------------------
File handling is the process of creating, opening, reading,
writing, and closing files using Python.

Why use files?
--------------
- Store data permanently.
- Read existing data.
- Write reports.
- Save logs.
- Work with configuration files.

Python mainly works with two types of files:
1. Text files (.txt, .csv, .py)
2. Binary files (.jpg, .png, .pdf)

-------------------------------------------------
Basic Workflow
-------------------------------------------------

Open File
    ↓
Read or Write
    ↓
Close File

Python provides the open() function for this purpose.
"""

print("=" * 50)
print("FILE HANDLING BASICS")
print("=" * 50)

# -------------------------------------------------
# Example 1: Creating and Writing a File
# -------------------------------------------------

print("\n1. Creating a file and writing text")

file = open("sample.txt", "w")
file.write("Hello from Python!\n")
file.write("Learning File Handling.")
file.close()

print("sample.txt created successfully.")

# -------------------------------------------------
# Example 2: Reading the File
# -------------------------------------------------

print("\n2. Reading the file")

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)

# -------------------------------------------------
# Example 3: File Exists After Program Ends
# -------------------------------------------------

print("\n3. Files store data permanently.")

print("Even after this program finishes,")
print("'sample.txt' remains on your computer.")

# -------------------------------------------------
# Important Concepts
# -------------------------------------------------

print("\nImportant Concepts")

concepts = [
    "open() opens a file.",
    "read() reads data.",
    "write() writes data.",
    "close() closes the file.",
    "Always close files after using them."
]

for item in concepts:
    print("-", item)

# -------------------------------------------------
# Common Mistake
# -------------------------------------------------

print("\nCommon Mistake")

print("Trying to read a file that does not exist raises an error.")

try:
    file = open("missing_file.txt", "r")
    file.close()
except FileNotFoundError:
    print("FileNotFoundError: missing_file.txt was not found.")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("Try these yourself:")
print("1. Create a file named notes.txt.")
print("2. Write three lines into it.")
print("3. Read and print its contents.")
print("4. Create another file named welcome.txt.")

print("\nEnd of Lesson 01.")

# -------------------------------------------------
# Mini Practice - Solution
# -------------------------------------------------
target_file_path = r'C:\Users\User\Python_Concepts\01_fundamentals\09_file_handling\notes.txt'

some_notes = open(target_file_path, 'w')

some_notes.write('Line 1\n')
some_notes.write('Line 2\n')
some_notes.write('Line 3\n')

some_notes.close()