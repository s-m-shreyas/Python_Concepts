# =============================================================================
# 02_comparison_operators.py
# =============================================================================
# type: ignore

"""
Python Operators

File:
    02_comparison_operators.py

Topic:
    Comparison Operators

Overview:
    Comparison operators compare two values and produce a boolean result.

    Python comparison operators:

        ==    Equal to
        !=    Not equal to
        >     Greater than
        <     Less than
        >=    Greater than or equal to
        <=    Less than or equal to

    Comparison operators return:

        True
        False

    This file contains 50 distinct examples covering:

        - Equality
        - Inequality
        - Greater than
        - Less than
        - Greater than or equal to
        - Less than or equal to
        - Integer comparisons
        - Float comparisons
        - String comparisons
        - Boolean comparisons
        - Variable comparisons
        - Function-result comparisons
        - Comparison expressions
        - Chained comparisons
        - Range checks
        - Sorting-related comparisons
        - Membership-related comparisons
        - None comparisons
        - Identity versus equality
        - Custom comparison-friendly examples
        - Practical validation patterns
"""

# =============================================================================
# 01. Equal To With Integers
# =============================================================================

first_number: int = 10
second_number: int = 10

result_01: bool = first_number == second_number

print(result_01)


# =============================================================================
# 02. Equal To With Different Integers
# =============================================================================

first_number = 10
second_number = 20

result_02: bool = first_number == second_number

print(result_02)


# =============================================================================
# 03. Not Equal To
# =============================================================================

first_number = 10
second_number = 20

result_03: bool = first_number != second_number

print(result_03)


# =============================================================================
# 04. Greater Than
# =============================================================================

larger_number: int = 20
smaller_number: int = 10

result_04: bool = larger_number > smaller_number

print(result_04)


# =============================================================================
# 05. Less Than
# =============================================================================

smaller_number = 10
larger_number = 20

result_05: bool = smaller_number < larger_number

print(result_05)


# =============================================================================
# 06. Greater Than Or Equal To
# =============================================================================

first_number = 20
second_number = 20

result_06: bool = first_number >= second_number

print(result_06)


# =============================================================================
# 07. Less Than Or Equal To
# =============================================================================

first_number = 20
second_number = 20

result_07: bool = first_number <= second_number

print(result_07)


# =============================================================================
# 08. Greater Than With Different Values
# =============================================================================

first_number = 25
second_number = 10

result_08: bool = first_number > second_number

print(result_08)


# =============================================================================
# 09. Less Than With Different Values
# =============================================================================

first_number = 5
second_number = 15

result_09: bool = first_number < second_number

print(result_09)


# =============================================================================
# 10. Comparing Negative Numbers
# =============================================================================

first_number: int = -5
second_number: int = -10

result_10: bool = first_number > second_number

print(result_10)


# =============================================================================
# 11. Comparing Zero
# =============================================================================

number: int = 0

result_11: bool = number == 0

print(result_11)


# =============================================================================
# 12. Comparing Positive And Negative Numbers
# =============================================================================

positive_number: int = 10
negative_number: int = -10

result_12: bool = positive_number > negative_number

print(result_12)


# =============================================================================
# 13. Comparing Floating-Point Numbers
# =============================================================================

first_price: float = 10.5
second_price: float = 10.5

result_13: bool = first_price == second_price

print(result_13)


# =============================================================================
# 14. Comparing Different Floating-Point Values
# =============================================================================

first_price = 10.5
second_price = 12.75

result_14: bool = first_price < second_price

print(result_14)


# =============================================================================
# 15. Comparing Integer And Float
# =============================================================================

integer_value: int = 10
float_value: float = 10.0

result_15: bool = integer_value == float_value

print(result_15)


# =============================================================================
# 16. Comparing Strings For Equality
# =============================================================================

first_name: str = "Python"
second_name: str = "Python"

result_16: bool = first_name == second_name

print(result_16)


# =============================================================================
# 17. Comparing Different Strings
# =============================================================================

first_name = "Python"
second_name = "Java"

result_17: bool = first_name != second_name

print(result_17)


# =============================================================================
# 18. String Greater Than Comparison
# =============================================================================

first_word: str = "Python"
second_word: str = "Java"

result_18: bool = first_word > second_word

print(result_18)


# =============================================================================
# 19. String Less Than Comparison
# =============================================================================

first_word = "Apple"
second_word = "Banana"

result_19: bool = first_word < second_word

print(result_19)


# =============================================================================
# 20. Case-Sensitive String Comparison
# =============================================================================

lowercase_name: str = "python"
uppercase_name: str = "Python"

result_20: bool = lowercase_name != uppercase_name

print(result_20)


# =============================================================================
# 21. Boolean Equality
# =============================================================================

first_flag: bool = True
second_flag: bool = True

result_21: bool = first_flag == second_flag

print(result_21)


# =============================================================================
# 22. Boolean Inequality
# =============================================================================

first_flag = True
second_flag = False

result_22: bool = first_flag != second_flag

print(result_22)


# =============================================================================
# 23. Boolean And Integer Comparison
# =============================================================================

boolean_value: bool = True
integer_value: int = 1

result_23: bool = boolean_value == integer_value

print(result_23)


# =============================================================================
# 24. Comparing Variables
# =============================================================================

minimum_age: int = 18
user_age: int = 21

result_24: bool = user_age >= minimum_age

print(result_24)


# =============================================================================
# 25. Password Length Validation
# =============================================================================

password: str = "secure123"
minimum_length: int = 8

result_25: bool = len(password) >= minimum_length

print(result_25)


# =============================================================================
# 26. Comparing List Lengths
# =============================================================================

first_items: list[int] = [1, 2, 3]
second_items: list[int] = [4, 5]

result_26: bool = len(first_items) > len(second_items)

print(result_26)


# =============================================================================
# 27. Comparing List Contents
# =============================================================================

first_list: list[int] = [1, 2, 3]
second_list: list[int] = [1, 2, 3]

result_27: bool = first_list == second_list

print(result_27)


# =============================================================================
# 28. Comparing Different Lists
# =============================================================================

first_list = [1, 2, 3]
second_list = [1, 2, 4]

result_28: bool = first_list != second_list

print(result_28)


# =============================================================================
# 29. Comparing Tuples
# =============================================================================

first_tuple: tuple[int, int] = (10, 20)
second_tuple: tuple[int, int] = (10, 20)

result_29: bool = first_tuple == second_tuple

print(result_29)


# =============================================================================
# 30. Comparing Dictionaries
# =============================================================================

first_user: dict[str, str] = {
    "name": "Alex",
    "role": "Developer",
}

second_user: dict[str, str] = {
    "name": "Alex",
    "role": "Developer",
}

result_30: bool = first_user == second_user

print(result_30)


# =============================================================================
# 31. Comparing Function Results
# =============================================================================

def calculate_square(number: int) -> int:
    """Return the square of a number."""
    return number * number


result_31: bool = calculate_square(5) == 25

print(result_31)


# =============================================================================
# 32. Comparing Function Results With Greater Than
# =============================================================================

def calculate_total(price: float, quantity: int) -> float:
    """Return the total price."""
    return price * quantity


result_32: bool = calculate_total(100.0, 3) > 250.0

print(result_32)


# =============================================================================
# 33. Comparing Expressions
# =============================================================================

first_value: int = 10
second_value: int = 5

result_33: bool = (first_value + second_value) == 15

print(result_33)


# =============================================================================
# 34. Comparing Arithmetic Results
# =============================================================================

first_value = 10
second_value = 5

result_34: bool = (first_value * 2) > (second_value * 3)

print(result_34)


# =============================================================================
# 35. Chained Greater-Than Comparison
# =============================================================================

minimum_value: int = 10
current_value: int = 20
maximum_value: int = 30

result_35: bool = minimum_value < current_value < maximum_value

print(result_35)


# =============================================================================
# 36. Chained Greater-Than-Or-Equal Comparison
# =============================================================================

minimum_age: int = 18
maximum_age: int = 60
user_age: int = 30

result_36: bool = minimum_age <= user_age <= maximum_age

print(result_36)


# =============================================================================
# 37. Range Validation
# =============================================================================

score: int = 85

result_37: bool = 0 <= score <= 100

print(result_37)


# =============================================================================
# 38. Temperature Range Validation
# =============================================================================

temperature: float = 24.5

result_38: bool = 15.0 <= temperature <= 30.0

print(result_38)


# =============================================================================
# 39. Comparing Dates As Strings
# =============================================================================

start_date: str = "2026-01-01"
end_date: str = "2026-12-31"

result_39: bool = start_date < end_date

print(result_39)


# =============================================================================
# 40. Checking Whether Values Are Equal Before Processing
# =============================================================================

expected_value: int = 100
actual_value: int = 100

if actual_value == expected_value:
    print("Values match.")
else:
    print("Values do not match.")


# =============================================================================
# 41. Greater-Than Conditional
# =============================================================================

account_balance: float = 1500.0

if account_balance > 0:
    print("Account has a positive balance.")
else:
    print("Account has no positive balance.")


# =============================================================================
# 42. Less-Than Conditional
# =============================================================================

stock_quantity: int = 5

if stock_quantity < 10:
    print("Stock is running low.")
else:
    print("Stock level is sufficient.")


# =============================================================================
# 43. Greater-Than-Or-Equal Conditional
# =============================================================================

exam_score: int = 75
passing_score: int = 50

if exam_score >= passing_score:
    print("Exam passed.")
else:
    print("Exam failed.")


# =============================================================================
# 44. Less-Than-Or-Equal Conditional
# =============================================================================

age: int = 17
adult_age: int = 18

if age <= adult_age:
    print("Age is within the specified limit.")
else:
    print("Age exceeds the specified limit.")


# =============================================================================
# 45. Comparing None With Equality
# =============================================================================

optional_value: str | None = None

result_45: bool = optional_value == None

print(result_45)

# In normal Python code, prefer:

if optional_value is None:
    print("Value is None.")


# =============================================================================
# 46. Equality Versus Identity
# =============================================================================

first_text: str = "Python"
second_text: str = "Python"

equality_result: bool = first_text == second_text

print(equality_result)

# == compares values.
#
# is compares object identity.
#
# For value comparison, use ==.
# For checking None, use is None.


# =============================================================================
# 47. Comparing Sorted Values
# =============================================================================

numbers: list[int] = [30, 10, 20]

smallest_number: int = min(numbers)
largest_number: int = max(numbers)

result_47: bool = smallest_number < largest_number

print(result_47)


# =============================================================================
# 48. Comparing User Input After Conversion
# =============================================================================

user_input: str = "25"
required_age: int = 18

user_age: int = int(user_input)

result_48: bool = user_age >= required_age

print(result_48)


# =============================================================================
# 49. Practical Validation Function
# =============================================================================

def is_valid_score(score: int) -> bool:
    """Return True when a score is within the valid range."""
    return 0 <= score <= 100


valid_score: bool = is_valid_score(85)
invalid_score: bool = is_valid_score(120)

print(valid_score)
print(invalid_score)


# =============================================================================
# 50. Practical Comparison Function
# =============================================================================

def is_greater(first: float, second: float) -> bool:
    """Return True when the first value is greater than the second."""
    return first > second


comparison_result: bool = is_greater(100.0, 50.0)

print(comparison_result)


# =============================================================================
# Comparison Operators Summary
# =============================================================================

"""
Comparison operators:

    ==    Equal to

    !=    Not equal to

    >     Greater than

    <     Less than

    >=    Greater than or equal to

    <=    Less than or equal to


All comparison operators produce a boolean result:

    True
    False


Examples:

    10 == 10
    10 != 20
    20 > 10
    10 < 20
    20 >= 20
    20 <= 20


Chained comparisons are also supported:

    10 < value < 20

    18 <= age <= 60

    0 <= score <= 100


Important distinction:

    ==

compares values.

    is

compares object identity.


For None checks, prefer:

    value is None

or:

    value is not None


Comparison operators are commonly used for:

    - Validation
    - Conditional statements
    - Filtering
    - Searching
    - Sorting logic
    - Range checks
    - Business rules
    - Data processing
    - Function return conditions
"""


# =============================================================================
# End of 02_comparison_operators.py
# =============================================================================