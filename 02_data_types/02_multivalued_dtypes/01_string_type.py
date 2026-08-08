"""
==============================================================================
Python Data Types
==============================================================================

Category
--------
Multi-Valued Data Types

Data Type
---------
String (`str`)

Overview
--------
A string is an ordered sequence of characters.

Strings can contain:

    - Letters
    - Numbers
    - Symbols
    - Whitespace
    - Unicode characters

Examples:

    "Python"
    "12345"
    "Hello, World!"
    ""
    "Python 🐍"

Strings are:

    - Ordered
    - Indexable
    - Sliceable
    - Iterable
    - Immutable

This module covers:

    - String literals
    - Default and non-default values
    - Single, double, and triple quotes
    - Type identification
    - Runtime type checking
    - String length
    - Indexing
    - Slicing
    - Iteration
    - Concatenation
    - Repetition
    - Membership testing
    - Escape sequences
    - Raw strings
    - String formatting
    - Common string methods
    - Case conversion
    - Searching
    - Replacing
    - Splitting
    - Joining
    - Stripping whitespace
    - Validation methods
    - Unicode
    - String conversion

General type behaviour such as:

    - Mutability
    - Hashability
    - Equality vs identity
    - General type conversion

is covered separately under:

    17_type_behaviour/
"""


# =============================================================================
# Example 1: String Literals
# =============================================================================

single_quote_text: str = 'Python'
double_quote_text: str = "Programming"
numeric_text: str = "12345"
symbol_text: str = "@#$%"
empty_text: str = ""

print(f"Single quotes: {single_quote_text}")
print(f"Double quotes: {double_quote_text}")
print(f"Numeric text:  {numeric_text}")
print(f"Symbols:       {symbol_text}")
print(f"Empty string:  {empty_text!r}")


# Strings can contain characters of different kinds.
#
#     "Python"
#     "12345"
#     "@#$%"
#
# Even though "12345" contains only digits, it is still a string because
# it is enclosed in quotes.


# =============================================================================
# Example 2: Default and Non-Default String Values
# =============================================================================

default_like_text: str = ""

non_default_text_primary: str = "Python"
non_default_text_secondary: str = "Data Engineering"

print(f"Default-like value: {default_like_text!r}")
print(f"First value:        {non_default_text_primary}")
print(f"Second value:       {non_default_text_secondary}")


# Python does NOT automatically assign an empty string to an annotated
# variable.
#
# This:
#
#     name: str
#
# is only a type annotation.
#
# It does NOT initialize `name`.
#
# Explicit initialization is required:
#
#     name: str = ""
#
# Therefore, `""` is a commonly used default-like string value, not Python's
# automatic default.


# =============================================================================
# Example 3: Single, Double, and Triple Quotes
# =============================================================================

single_quoted_message: str = 'Hello'
double_quoted_message: str = "Hello"

triple_single_message: str = """
This is a
multi-line string.
"""

triple_double_message: str = """
This is also
a multi-line string.
"""

print(single_quoted_message)
print(double_quoted_message)
print(triple_single_message)
print(triple_double_message)


# Python supports:
#
#     'text'
#     "text"
#     '''text'''
#     """text"""
#
# Triple-quoted strings can span multiple lines.


# =============================================================================
# Example 4: Quotes Inside Strings
# =============================================================================

apostrophe_text: str = "Python's syntax"
quotation_text: str = 'He said "Hello"'

print(apostrophe_text)
print(quotation_text)


# Different quote styles can be used to avoid unnecessary escaping.


# =============================================================================
# Example 5: Type Identification
# =============================================================================

string_type_sample: str = "Python"

print(f"Value: {string_type_sample}")
print(f"Type:  {type(string_type_sample)}")


# `type()` returns the concrete type/class of an object.
#
# Expected:
#
#     <class 'str'>


# =============================================================================
# Example 6: Runtime String Type Checking
# =============================================================================

string_runtime_candidate: object = "Python"
integer_runtime_candidate: object = 100

string_runtime_check: bool = isinstance(
    string_runtime_candidate,
    str,
) # pyright: ignore[reportUnnecessaryIsInstance]

integer_string_check: bool = isinstance(
    integer_runtime_candidate,
    str,
)

print(
    f'"Python" is a string: '
    f"{string_runtime_check}"
)

print(
    f"100 is a string:     "
    f"{integer_string_check}"
)


# The candidates are intentionally typed as `object`.
#
# This gives `isinstance()` meaningful runtime work to perform.
#
# If we wrote:
#
#     value: str = "Python"
#
# a static type checker already knows that `value` is a string and may report
# the isinstance() call as unnecessary.


# =============================================================================
# Example 7: String Length
# =============================================================================

length_sample_text: str = "Python"

length_result: int = len(
    length_sample_text
)

print(
    f"String: {length_sample_text}"
)

print(
    f"Length: {length_result}"
)


# `len()` returns the number of characters in a string.


# =============================================================================
# Example 8: Positive Indexing
# =============================================================================

positive_index_text: str = "Python"

first_character: str = positive_index_text[0]
third_character: str = positive_index_text[2]

print(f"First character: {first_character}")
print(f"Third character: {third_character}")


# Python uses zero-based indexing.
#
#     P y t h o n
#     0 1 2 3 4 5
#
# Therefore:
#
#     text[0] -> 'P'
#     text[2] -> 't'


# =============================================================================
# Example 9: Negative Indexing
# =============================================================================

negative_index_text: str = "Python"

last_character: str = negative_index_text[-1]
second_last_character: str = negative_index_text[-2]

print(f"Last character:        {last_character}")
print(f"Second-last character: {second_last_character}")


# Negative indexing starts from the end:
#
#     P  y  t  h  o  n
#    -6 -5 -4 -3 -2 -1
#
# Therefore:
#
#     text[-1] -> 'n'


# =============================================================================
# Example 10: String Slicing
# =============================================================================

slice_source_text: str = "Python"

first_three_characters: str = slice_source_text[0:3]
last_three_characters: str = slice_source_text[3:6]

print(
    f"First three: {first_three_characters}"
)

print(
    f"Last three:  {last_three_characters}"
)


# General slicing syntax:
#
#     sequence[start:stop]
#
# The `stop` index is excluded.


# =============================================================================
# Example 11: String Iteration
# =============================================================================

iteration_text_value: str = "Python"

for iteration_character in iteration_text_value:
    print(iteration_character)


# Strings are iterable.
#
# Iterating over a string produces one character at a time.


# =============================================================================
# Example 12: String Concatenation
# =============================================================================

first_name_text: str = "S.M."
last_name_text: str = "Shreyas"

full_name_text: str = (
    first_name_text
    + " "
    + last_name_text
)

print(full_name_text)


# `+` joins strings together.
#
# This operation is called concatenation.


# =============================================================================
# Example 13: String Repetition
# =============================================================================

repeated_symbol_text: str = "-" * 10

print(repeated_symbol_text)


# `*` can repeat a string.
#
#     "-" * 10
#
# produces:
#
#     ----------


# =============================================================================
# Example 14: Membership Testing
# =============================================================================

membership_source_text: str = "Python Programming"

contains_python: bool = (
    "Python" in membership_source_text
)

contains_java: bool = (
    "Java" in membership_source_text
)

print(f'"Python" present: {contains_python}')
print(f'"Java" present:   {contains_java}')


# `in` checks whether a substring or character exists in a string.
#
# `not in` checks whether it does not exist.


# =============================================================================
# Example 15: Escape Sequences
# =============================================================================

escaped_newline_text: str = "Python\nProgramming"
escaped_tab_text: str = "Python\tProgramming"
escaped_quote_text: str = "He said \"Hello\""

print(escaped_newline_text)
print(escaped_tab_text)
print(escaped_quote_text)


# Common escape sequences:
#
#     \n -> newline
#     \t -> tab
#     \" -> double quote
#     \' -> single quote
#     \\ -> backslash


# =============================================================================
# Example 16: Raw Strings
# =============================================================================

raw_path_text: str = r"C:\Users\Python\Projects"

print(raw_path_text)


# A raw string treats backslashes mostly as literal characters.
#
# Raw strings are particularly useful when working with:
#
#     - Windows paths
#     - Regular expressions


# =============================================================================
# Example 17: String Formatting With f-Strings
# =============================================================================

developer_name_text: str = "Shreyas"
project_count_value: int = 5

formatted_summary_text: str = (
    f"{developer_name_text} has worked on "
    f"{project_count_value} projects."
)

print(formatted_summary_text)


# f-strings allow expressions and variables to be embedded directly inside
# string literals.


# =============================================================================
# Example 18: String Formatting With format()
# =============================================================================

format_language_text: str = "Python"
format_level_text: str = "Advanced"

formatted_learning_text: str = (
    "{} is being studied at an {} level.".format(
        format_language_text,
        format_level_text,
    )
)

print(formatted_learning_text)


# `.format()` provides another string-formatting mechanism.
#
# f-strings are generally preferred in modern Python when applicable.


# =============================================================================
# Example 19: Changing Case
# =============================================================================

case_source_text: str = "Python Programming"

uppercase_text: str = case_source_text.upper()
lowercase_text: str = case_source_text.lower()
titlecase_text: str = case_source_text.title()
capitalized_text: str = case_source_text.capitalize()

print(f"Uppercase:   {uppercase_text}")
print(f"Lowercase:   {lowercase_text}")
print(f"Title case:  {titlecase_text}")
print(f"Capitalized: {capitalized_text}")


# Common case-conversion methods:
#
#     upper()
#     lower()
#     title()
#     capitalize()


# =============================================================================
# Example 20: Searching Within a String
# =============================================================================

search_source_text: str = "Python Data Engineering"

find_result_index: int = search_source_text.find(
    "Data"
)

index_result_position: int = search_source_text.index(
    "Engineering"
)

print(f"find() result:  {find_result_index}")
print(f"index() result: {index_result_position}")


# `find()` returns the first index where the substring occurs.
#
# If the substring is not found:
#
#     find() -> -1
#
# `index()` also returns the position, but raises an exception if the
# substring does not exist.


# =============================================================================
# Example 21: Counting Substrings
# =============================================================================

count_source_text: str = "banana"

banana_count: int = count_source_text.count(
    "an"
)

print(
    f'"an" occurs {banana_count} times.'
)


# `count()` returns the number of non-overlapping occurrences of a substring.


# =============================================================================
# Example 22: Replacing Text
# =============================================================================

replace_source_text: str = "Python is difficult"

replace_result_text: str = (
    replace_source_text.replace(
        "difficult",
        "powerful",
    )
)

print(replace_result_text)


# `replace()` returns a new string with matching text replaced.
#
# The original string remains unchanged because strings are immutable.


# =============================================================================
# Example 23: Splitting a String
# =============================================================================

split_source_text: str = "Python,SQL,Airflow"

split_result_list: list[str] = (
    split_source_text.split(",")
) # pyright: ignore[reportAssignmentType]

print(split_result_list)


# `split()` divides a string into a list using a separator.
#
#     "Python,SQL,Airflow"
#
# becomes:
#
#     ["Python", "SQL", "Airflow"]


# =============================================================================
# Example 24: Joining Strings
# =============================================================================

join_values_list: list[str] = [
    "Python",
    "SQL",
    "Airflow",
]

joined_tools_text: str = ", ".join(
    join_values_list
)

print(joined_tools_text)


# `join()` combines multiple strings using the calling string as a separator.
#
#     ", ".join(["Python", "SQL", "Airflow"])
#
# produces:
#
#     "Python, SQL, Airflow"


# =============================================================================
# Example 25: Removing Whitespace
# =============================================================================

whitespace_source_text: str = "   Python   "

stripped_text: str = whitespace_source_text.strip()
left_stripped_text: str = whitespace_source_text.lstrip()
right_stripped_text: str = whitespace_source_text.rstrip()

print(f"Original: {whitespace_source_text!r}")
print(f"strip():  {stripped_text!r}")
print(f"lstrip(): {left_stripped_text!r}")
print(f"rstrip(): {right_stripped_text!r}")


#     strip()  -> removes leading and trailing whitespace
#     lstrip() -> removes leading whitespace
#     rstrip() -> removes trailing whitespace


# =============================================================================
# Example 26: String Validation Methods
# =============================================================================

validation_numeric_text: str = "12345"
validation_alpha_text: str = "Python"
validation_alphanumeric_text: str = "Python123"
validation_space_text: str = "   "

numeric_check: bool = validation_numeric_text.isdigit()
alphabetic_check: bool = validation_alpha_text.isalpha()
alphanumeric_check: bool = (
    validation_alphanumeric_text.isalnum()
)
space_check: bool = validation_space_text.isspace()

print(f"Only digits:       {numeric_check}")
print(f"Only letters:      {alphabetic_check}")
print(f"Letters/numbers:   {alphanumeric_check}")
print(f"Only whitespace:   {space_check}")


# Common validation methods include:
#
#     isdigit()
#     isalpha()
#     isalnum()
#     isspace()
#
# These methods return Boolean values.


# =============================================================================
# Example 27: Prefix and Suffix Checking
# =============================================================================

prefix_suffix_source_text: str = (
    "data_engineering.py"
)

starts_with_data: bool = (
    prefix_suffix_source_text.startswith("data")
)

ends_with_python: bool = (
    prefix_suffix_source_text.endswith(".py")
)

print(f"Starts with 'data': {starts_with_data}")
print(f"Ends with '.py':    {ends_with_python}")


# `startswith()` checks the beginning of a string.
#
# `endswith()` checks the end of a string.


# =============================================================================
# Example 28: Unicode Characters
# =============================================================================

unicode_greeting_text: str = "Hello, नमस्ते, 你好, 🐍"

print(unicode_greeting_text)

print(
    f"Length: {len(unicode_greeting_text)}"
)


# Python strings support Unicode characters.
#
# Strings are not restricted to ASCII characters.


# =============================================================================
# Example 29: Converting Values to Strings
# =============================================================================

conversion_integer_value: int = 250
conversion_float_value: float = 12.5
conversion_boolean_value: bool = True

integer_as_text: str = str(
    conversion_integer_value
)

float_as_text: str = str(
    conversion_float_value
)

boolean_as_text: str = str(
    conversion_boolean_value
)

print(f"Integer: {integer_as_text!r}")
print(f"Float:   {float_as_text!r}")
print(f"Boolean: {boolean_as_text!r}")


# `str()` converts suitable Python objects into their string representation.


# =============================================================================
# Example 30: String Immutability Preview
# =============================================================================

immutability_source_text: str = "Python"

immutability_modified_text: str = (
    immutability_source_text.replace(
        "P",
        "J",
    )
)

print(
    f"Original: {immutability_source_text}"
)

print(
    f"New:      {immutability_modified_text}"
)

print(
    f"Different objects: "
    f"{immutability_source_text is not immutability_modified_text}"
)


# String methods do not modify the original string.
#
# Instead, they create and return another string.
#
# This happens because strings are immutable.
#
# Detailed mutability behaviour is covered separately under:
#
#     17_type_behaviour/01_mutability.py


# =============================================================================
# Example 31: String Equality
# =============================================================================

equality_text_left: str = str(
    "Python"
)

equality_text_right: str = str(
    "Python"
)

string_equality_result: bool = (
    equality_text_left
    == equality_text_right
)

print(
    f"Equal values: {string_equality_result}"
)


# `==` compares the values/content of strings.


# =============================================================================
# Example 32: String Identity
# =============================================================================

identity_text_left: str = "".join(
    ["Python"]
)

identity_text_right: str = "".join(
    ["Python"]
)

string_identity_result: bool = (
    identity_text_left
    is identity_text_right
)

print(
    f"Same object: {string_identity_result}"
)


# `is` checks whether two variables refer to the exact same object.
#
# `==` should be used when comparing string values.
#
# Identity behaviour is covered separately under:
#
#     17_type_behaviour/03_equality_vs_identity.py


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ `str` represents a sequence of characters.

✓ Strings can contain letters, numbers, symbols, whitespace, and Unicode
  characters.

✓ Strings can be created using:
      'single quotes'
      "double quotes"
      '''triple quotes'''
      

✓ `""` is a common default-like string value, but Python does not
  automatically initialize an annotated string with it.

✓ A type annotation alone does not initialize a variable.

✓ Strings are:
      - ordered
      - indexable
      - sliceable
      - iterable
      - immutable

✓ `type()` identifies the concrete type of a string.

✓ `isinstance()` performs runtime type checking.

✓ `len()` returns the number of characters.

✓ Positive indexing starts from zero.

✓ Negative indexing starts from the end.

✓ Slicing extracts a portion of a string.

✓ Strings can be iterated character by character.

✓ `+` concatenates strings.

✓ `*` repeats strings.

✓ `in` performs membership testing.

✓ Escape sequences represent special characters.

✓ Raw strings are useful when working with literal backslashes.

✓ f-strings provide convenient string formatting.

✓ `.format()` provides another formatting mechanism.

✓ Common case methods include:
      upper()
      lower()
      title()
      capitalize()

✓ Searching methods include:
      find()
      index()
      count()

✓ `replace()` returns a new string.

✓ `split()` converts a string into a list.

✓ `join()` combines multiple strings into one string.

✓ Whitespace can be removed with:
      strip()
      lstrip()
      rstrip()

✓ Validation methods include:
      isdigit()
      isalpha()
      isalnum()
      isspace()

✓ `startswith()` and `endswith()` check prefixes and suffixes.

✓ Python strings support Unicode.

✓ `str()` converts suitable objects into strings.

✓ Strings are immutable, so string operations return new strings rather than
  modifying the original string.

✓ `==` compares string values.

✓ `is` compares object identity.

✓ Detailed mutability and identity behaviour is covered separately.
"""


# =============================================================================
# End of File
# =============================================================================