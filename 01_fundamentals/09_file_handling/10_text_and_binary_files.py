# type: ignore

"""
=================================================
10. Text and Binary Files
=================================================

Everything stored on disk is ultimately binary (bytes).

Python can work with files in two ways:

1. Text Mode
   - Returns Python strings (str).
   - Automatically encodes and decodes data.
   - Used for .txt, .csv, .json, .py, etc.

2. Binary Mode
   - Returns raw bytes (bytes).
   - No encoding or decoding happens.
   - Used for images, PDFs, videos, ZIP files, etc.
"""

print("=" * 50)
print("TEXT AND BINARY FILES")
print("=" * 50)

# -------------------------------------------------
# Example 1: Writing a Text File
# -------------------------------------------------

print("\n1. Text Mode")

with open("text_demo.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python 🌍")

with open("text_demo.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Content:", content)
print("Type:", type(content))

# -------------------------------------------------
# Example 2: Writing a Binary File
# -------------------------------------------------

print("\n2. Binary Mode")

binary_data = b"ABC123"

with open("binary_demo.bin", "wb") as file:
    file.write(binary_data)

with open("binary_demo.bin", "rb") as file:
    content = file.read()

print("Content:", content)
print("Type:", type(content))

# -------------------------------------------------
# Example 3: Understanding Encoding
# -------------------------------------------------

print("\n3. Encoding Example")

text = "Hello"

print("Python String:", text)
print("UTF-8 Bytes:", text.encode("utf-8"))

# -------------------------------------------------
# Example 4: Decoding Bytes
# -------------------------------------------------

print("\n4. Decoding Example")

data = b"Python"

print("Bytes:", data)
print("Decoded:", data.decode("utf-8"))

# -------------------------------------------------
# Example 5: Copying a Binary File
# -------------------------------------------------

print("\n5. Copying Binary Data")

# Create a small binary file
with open("original.bin", "wb") as file:
    file.write(bytes(range(10)))

# Copy it
with open("original.bin", "rb") as source:
    with open("copy.bin", "wb") as destination:
        destination.write(source.read())

print("Binary file copied successfully.")

# -------------------------------------------------
# Example 6: Why Images Need Binary Mode
# -------------------------------------------------

print("\n6. Why Images Use Binary Mode")

print("Images contain raw bytes, not characters.")
print("Always use 'rb' and 'wb' for images.")

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

# Writing bytes in text mode
try:
    with open("error.txt", "w") as file:
        file.write(b"Hello")
except TypeError as e:
    print("TypeError:", e)

# Writing text in binary mode
try:
    with open("error.bin", "wb") as file:
        file.write("Hello")
except TypeError as e:
    print("TypeError:", e)

# Correct approaches
with open("correct_text.txt", "w") as file:
    file.write("Hello")

with open("correct_binary.bin", "wb") as file:
    file.write(b"Hello")

# -------------------------------------------------
# Comparison Table
# -------------------------------------------------

print("\nText vs Binary")

comparison = [
    ("Text", "str"),
    ("Binary", "bytes"),
    ("Text", "Uses encoding"),
    ("Binary", "No encoding"),
    ("Text", ".txt/.csv/.json"),
    ("Binary", ".jpg/.png/.pdf")
]

for item, value in comparison:
    print(f"{item:<10}: {value}")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use UTF-8 for text files.",
    "Use binary mode for non-text files.",
    "Never mix str and bytes.",
    "Use encode() and decode() when needed."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("Text Mode", "Returns str"),
    ("Binary Mode", "Returns bytes"),
    ("encode()", "str → bytes"),
    ("decode()", "bytes → str"),
    ("UTF-8", "Most common encoding")
]

for item, value in summary:
    print(f"{item:<15}: {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Create a UTF-8 text file with an emoji.")
print("2. Read and print it.")
print("3. Create a binary file containing bytes.")
print("4. Copy the binary file.")
print("5. Try encode() and decode() yourself.")

print("\nEnd of Lesson 10.")