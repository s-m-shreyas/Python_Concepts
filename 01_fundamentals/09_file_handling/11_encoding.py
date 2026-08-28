"""
=================================================
11. Character Encoding
=================================================

What is Encoding?
-----------------
Encoding is the process of converting Python strings (str)
into bytes so they can be stored in a file or transmitted.

Decoding is the reverse process:
bytes -> str

Everything on disk is stored as bytes.
Encoding tells Python how characters should be represented.
"""

print("=" * 50)
print("CHARACTER ENCODING")
print("=" * 50)

# -------------------------------------------------
# Example 1: Encoding a String
# -------------------------------------------------

print("\n1. Encoding")

text = "Hello 🌍"

encoded = text.encode("utf-8")

print("String :", text)
print("Bytes  :", encoded)
print("Type   :", type(encoded))

# -------------------------------------------------
# Example 2: Decoding Bytes
# -------------------------------------------------

print("\n2. Decoding")

decoded = encoded.decode("utf-8")

print("Decoded:", decoded)
print("Type   :", type(decoded))

# -------------------------------------------------
# Example 3: Writing with UTF-8
# -------------------------------------------------

print("\n3. Writing UTF-8")

with open("utf8_demo.txt", "w", encoding="utf-8") as file:
    file.write("Python ❤️ UTF-8")

with open("utf8_demo.txt", "r", encoding="utf-8") as file:
    print(file.read())

# -------------------------------------------------
# Example 4: ASCII vs UTF-8
# -------------------------------------------------

print("\n4. ASCII vs UTF-8")

print("ASCII can store:")
print("Hello".encode("ascii"))

print("UTF-8 can store:")
print("Hello 🌍".encode("utf-8"))

try:
    print("🌍".encode("ascii"))
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)

# -------------------------------------------------
# Example 5: Viewing Raw Bytes
# -------------------------------------------------

print("\n5. Raw Bytes")

word = "Café"

utf8_bytes = word.encode("utf-8")

print(word)
print(utf8_bytes)

# -------------------------------------------------
# Example 6: UnicodeDecodeError
# -------------------------------------------------

print("\n6. UnicodeDecodeError")

# Create UTF-8 data
with open("unicode.txt", "w", encoding="utf-8") as file:
    file.write("Café")

# Read correctly
with open("unicode.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Read incorrectly
try:
    with open("unicode.txt", "r", encoding="ascii") as file:
        print(file.read())
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)

# -------------------------------------------------
# Example 7: Different Encodings
# -------------------------------------------------

print("\n7. Different Encodings")

text = "Python"

encodings = ["utf-8", "utf-16", "utf-32"]

for enc in encodings:
    print(enc, ":", text.encode(enc))

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

print("\nCommon Mistakes")

try:
    "😊".encode("ascii")
except UnicodeEncodeError as e:
    print("Cannot encode emoji in ASCII.")

try:
    b"\xff".decode("utf-8")
except UnicodeDecodeError:
    print("Invalid UTF-8 bytes.")

# -------------------------------------------------
# Best Practices
# -------------------------------------------------

print("\nBest Practices")

tips = [
    "Use UTF-8 by default.",
    "Specify encoding='utf-8' when opening text files.",
    "Use encode() before writing bytes manually.",
    "Use decode() when converting bytes to strings."
]

for tip in tips:
    print("-", tip)

# -------------------------------------------------
# Quick Summary
# -------------------------------------------------

print("\nQuick Summary")

summary = [
    ("encode()", "str -> bytes"),
    ("decode()", "bytes -> str"),
    ("UTF-8", "Most common encoding"),
    ("ASCII", "English characters only"),
    ("Unicode", "Universal character set")
]

for item, value in summary:
    print(f"{item:<12}: {value}")

# -------------------------------------------------
# Mini Practice
# -------------------------------------------------

print("\nMini Practice")

print("1. Encode your name in UTF-8.")
print("2. Decode it back.")
print("3. Write a file containing an emoji.")
print("4. Try reading it using ASCII.")
print("5. Compare UTF-8 and UTF-16 byte lengths.")

print("\nEnd of Lesson 11.")