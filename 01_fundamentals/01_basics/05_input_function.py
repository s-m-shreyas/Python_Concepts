"""
==============================================================================
Python Basics
==============================================================================

File
----
04_input_function.py

Topic
-----
input() Function

Overview
--------
The input() function reads text entered by the user through standard input.

The important rule is:

    input()
        -> returns a str

Even when the user enters something that looks like a number,
input() initially produces a string.

This file covers:

    - Basic input()
    - Input prompts
    - Return value of input()
    - Input stored in variables
    - Multiple inputs
    - Whitespace
    - Empty input
    - String conversion
    - Numeric conversion
    - Input with annotations
    - Input and expressions
    - Input validation basics
"""


# =============================================================================
# 01. Basic input()
# =============================================================================

input_basic_name: str = input()

print(
    f"Name entered: {input_basic_name!r}"
)


# input() waits for the user to enter text
# and press Enter.


# =============================================================================
# 02. input() With a Prompt
# =============================================================================

input_prompt_name: str = input(
    "Enter your name: "
)

print(
    f"Hello, {input_prompt_name}!"
)


# The string passed to input() is displayed before waiting for input.


# =============================================================================
# 03. input() Returns a String
# =============================================================================

input_return_value: str = input(
    "Enter anything: "
)

print(
    f"Value: {input_return_value!r}"
)

print(
    f"Runtime type: "
    f"{type(input_return_value).__name__!r}"
)


# Regardless of what the user enters,
# input() initially returns a string.


# =============================================================================
# 04. Number-Looking Input
# =============================================================================

input_number_text: str = input(
    "Enter a number: "
)

print(
    f"Entered value: {input_number_text!r}"
)

print(
    f"Runtime type: "
    f"{type(input_number_text).__name__!r}"
)


# If the user enters:
#
#     100
#
# the returned value is:
#
#     "100"
#
# not:
#
#     100


# =============================================================================
# 05. Input With Type Annotation
# =============================================================================

input_annotated_name: str = input(
    "Enter your name: "
)

print(
    f"Name: {input_annotated_name!r}"
)


# The annotation documents that input() returns a string.


# =============================================================================
# 06. Empty Input
# =============================================================================

input_empty_text: str = input(
    "Press Enter without typing anything: "
)

print(
    f"Input: {input_empty_text!r}"
)

print(
    f"Is empty: "
    f"{input_empty_text == ''}"
)


# Pressing Enter without entering text produces an empty string.


# =============================================================================
# 07. Whitespace Input
# =============================================================================

input_whitespace_text: str = input(
    "Enter text with spaces: "
)

print(
    f"Original input: {input_whitespace_text!r}"
)


# Input preserves the entered characters.


# =============================================================================
# 08. strip() After Input
# =============================================================================

input_raw_text: str = input(
    "Enter text: "
)

input_clean_text: str = input_raw_text.strip()

print(
    f"Original: {input_raw_text!r}"
)

print(
    f"Stripped: {input_clean_text!r}"
)


# strip() removes leading and trailing whitespace.
#
# It does not modify the original string because strings are immutable.


# =============================================================================
# 09. Lowercase Input
# =============================================================================

input_case_text: str = input(
    "Enter a word: "
)

input_lower_text: str = input_case_text.lower()

print(
    f"Lowercase: {input_lower_text!r}"
)


# =============================================================================
# 10. Multiple Inputs
# =============================================================================

input_first_name: str = input(
    "Enter first name: "
)

input_last_name: str = input(
    "Enter last name: "
)

print(
    f"Name: {input_first_name} {input_last_name}"
)


# Each input() call waits for its own input.


# =============================================================================
# 11. Input and Concatenation
# =============================================================================

input_city_name: str = input(
    "Enter city: "
)

input_country_name: str = input(
    "Enter country: "
)

input_location_text: str = (
    input_city_name
    + ", "
    + input_country_name
)

print(
    input_location_text
)


# Since both values are strings, they can be concatenated.


# =============================================================================
# 12. String Conversion
# =============================================================================

input_text_value: str = input(
    "Enter text: "
)

input_string_value: str = str(
    input_text_value
)

print(
    f"Value: {input_string_value!r}"
)


# input() already returns str,
# so str() is usually unnecessary here.


# =============================================================================
# 13. Integer Conversion
# =============================================================================

input_integer_text: str = input(
    "Enter an integer: "
)

input_integer_value: int = int(
    input_integer_text
)

print(
    f"Value: {input_integer_value!r}"
)

print(
    f"Runtime type: "
    f"{type(input_integer_value).__name__!r}"
)


# int() converts suitable text into an integer.


# =============================================================================
# 14. Float Conversion
# =============================================================================

input_float_text: str = input(
    "Enter a decimal number: "
)

input_float_value: float = float(
    input_float_text
)

print(
    f"Value: {input_float_value!r}"
)

print(
    f"Runtime type: "
    f"{type(input_float_value).__name__!r}"
)


# float() converts suitable text into a floating-point number.


# =============================================================================
# 15. Boolean Input Consideration
# =============================================================================

input_boolean_text: str = input(
    "Enter yes or no: "
)

input_boolean_normalized: str = (
    input_boolean_text.strip().lower()
)

print(
    f"Normalized input: "
    f"{input_boolean_normalized!r}"
)


# Important:
#
# bool("False")
#
# does NOT mean that the user entered the boolean False.
#
# Any non-empty string is truthy.
#
# Boolean input normally requires explicit interpretation.


# =============================================================================
# 16. Interpreting Yes / No
# =============================================================================

input_confirmation_text: str = input(
    "Continue? (yes/no): "
)

input_confirmation_normalized: str = (
    input_confirmation_text.strip().lower()
)

if input_confirmation_normalized == "yes":
    print("Continue selected.")
else:
    print("Continue not selected.")


# The input is still a string.
#
# The program interprets that string according to its own logic.


# =============================================================================
# 17. Input and Arithmetic
# =============================================================================

input_first_number_text: str = input(
    "Enter first number: "
)

input_second_number_text: str = input(
    "Enter second number: "
)

input_first_number: int = int(
    input_first_number_text
)

input_second_number: int = int(
    input_second_number_text
)

input_sum_result: int = (
    input_first_number
    + input_second_number
)

print(
    f"Sum: {input_sum_result}"
)


# Conversion is required before numeric arithmetic.


# =============================================================================
# 18. Direct Conversion Around input()
# =============================================================================

input_direct_integer: int = int(
    input(
        "Enter an integer: "
    )
)

print(
    f"Integer: {input_direct_integer!r}"
)


# Conversion can be performed directly around input().


# =============================================================================
# 19. Direct Float Conversion
# =============================================================================

input_direct_float: float = float(
    input(
        "Enter a decimal value: "
    )
)

print(
    f"Float: {input_direct_float!r}"
)


# =============================================================================
# 20. Input Can Be Assigned to a Variable
# =============================================================================

input_assignment_name: str

input_assignment_name = input(
    "Enter your name: "
)

print(
    input_assignment_name
)


# Annotation and assignment can be written separately.


# =============================================================================
# 21. Input With a Default-Like Fallback
# =============================================================================

input_optional_name: str = input(
    "Enter your name (press Enter for Guest): "
)

if input_optional_name.strip() == "":
    input_display_name: str = "Guest"
else:
    input_display_name = input_optional_name.strip()

print(
    f"Name: {input_display_name!r}"
)


# input() itself does not provide a default-value parameter.
#
# A program can implement a fallback using its own logic.


# =============================================================================
# 22. Input Validation With try / except
# =============================================================================

input_safe_integer_text: str = input(
    "Enter an integer: "
)

try:
    input_safe_integer_value: int = int(
        input_safe_integer_text
    )
except ValueError:
    input_safe_integer_value = 0

print(
    f"Result: {input_safe_integer_value!r}"
)


# Invalid numeric text can cause ValueError during conversion.
#
# Exception handling is covered in detail later.


# =============================================================================
# 23. Checking Empty Input Before Conversion
# =============================================================================

input_optional_number_text: str = input(
    "Enter an integer or press Enter: "
)

if input_optional_number_text.strip() == "":
    print("No number entered.")
else:
    input_optional_number_value: int = int(
        input_optional_number_text
    )

    print(
        f"Number: {input_optional_number_value!r}"
    )


# This prevents an empty string from being passed directly to int().


# =============================================================================
# 24. Input Is Read as Text
# =============================================================================

input_text_a: str = input(
    "Enter first value: "
)

input_text_b: str = input(
    "Enter second value: "
)

print(
    f"Concatenated: "
    f"{input_text_a + input_text_b!r}"
)


# If the user enters:
#
#     10
#     20
#
# the result is:
#
#     "1020"
#
# because both inputs are strings.


# =============================================================================
# 25. Convert Before Arithmetic
# =============================================================================

input_math_a_text: str = input(
    "Enter first integer: "
)

input_math_b_text: str = input(
    "Enter second integer: "
)

input_math_a: int = int(
    input_math_a_text
)

input_math_b: int = int(
    input_math_b_text
)

print(
    f"Arithmetic result: "
    f"{input_math_a + input_math_b}"
)


# =============================================================================
# 26. Multiple Values From One Input
# =============================================================================

input_values_text: str = input(
    "Enter three values separated by spaces: "
)

input_values_parts: list[str] = (
    input_values_text.split()
)

print(
    f"Parts: {input_values_parts!r}"
)


# split() turns one input string into multiple string values.


# =============================================================================
# 27. Converting Multiple Input Values
# =============================================================================

input_numbers_text: str = input(
    "Enter integers separated by spaces: "
)

input_number_parts: list[str] = (
    input_numbers_text.split()
)

input_number_values: list[int] = [
    int(input_part)
    for input_part in input_number_parts
]

print(
    f"Numbers: {input_number_values!r}"
)


# Each individual string is converted into an integer.


# =============================================================================
# 28. Input and repr()
# =============================================================================

input_visible_text: str = input(
    "Enter text containing spaces: "
)

print(
    f"repr: {input_visible_text!r}"
)


# !r makes spaces, escape characters, and other representation details
# easier to see.


# =============================================================================
# 29. input() Return Model
# =============================================================================

"""
Conceptually:

    user enters:

        100

    input() produces:

        "100"


Then:

    int(input(...))

produces:

        100


Therefore:

    input()
        ↓
    str
        ↓
    explicit conversion when required
        ↓
    int / float / another required type
"""


# =============================================================================
# 30. Basic Input Flow
# =============================================================================

"""
A typical input workflow is:

    1. Display prompt
            ↓
    2. Wait for user
            ↓
    3. Read entered text
            ↓
    4. Store returned string
            ↓
    5. Clean / validate if required
            ↓
    6. Convert if required
            ↓
    7. Use the resulting value
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ input() reads user input from standard input.

✓ input() returns a string.

✓ Even numeric-looking input initially arrives as str.

      input()

      user enters:
          100

      returned value:
          "100"


✓ A prompt can be supplied:

      input("Enter your name: ")


✓ Pressing Enter without text produces:

      ""


✓ Input preserves the entered text.

✓ strip() can remove leading and trailing whitespace.

✓ Numeric conversion must be explicit:

      int(input(...))

      float(input(...))


✓ input() itself does not provide a default value.

✓ A fallback can be implemented using program logic.

✓ Boolean input requires interpretation.

✓ Multiple values can be separated using split().

✓ Conversion may fail when the entered text is invalid.

✓ input() can be combined directly with conversion:

      int(input(...))

Core model:

    input()
        ↓
    str
        ↓
    optional cleaning / validation
        ↓
    optional conversion
        ↓
    program logic
"""