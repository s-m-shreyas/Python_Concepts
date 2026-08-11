# type: ignore
# =============================================================================
# 11. Chained Comparisons
# =============================================================================
"""
Python Operators

File:
    11_chained_comparisons.py

Topic:
    Chained Comparisons

Overview:
    Python allows multiple comparison operators to be combined into a single
    expression.

    Instead of writing:

        minimum <= value and value <= maximum

    Python allows:

        minimum <= value <= maximum

    Chained comparisons are evaluated from left to right.

    Common comparison operators:

        <
        <=
        >
        >=
        ==
        !=

    A chained comparison such as:

        a < b < c

    is conceptually equivalent to:

        a < b and b < c

    The middle expression is evaluated only once.

Topics covered:

    - Basic chained comparisons
    - Less-than chains
    - Less-than-or-equal chains
    - Greater-than chains
    - Greater-than-or-equal chains
    - Equality in chains
    - Inequality in chains
    - Range validation
    - Inclusive ranges
    - Exclusive ranges
    - Mixed comparison operators
    - Numeric ranges
    - Negative ranges
    - Decimal values
    - Variables in chains
    - Boolean results
    - Chaining with expressions
    - Chaining with arithmetic expressions
    - Chaining with function calls
    - Chaining with strings
    - Chaining with characters
    - Chaining with dates
    - Ascending order checks
    - Descending order checks
    - Multiple values
    - Three-way comparisons
    - Four-value chains
    - Avoiding unnecessary and expressions
    - Comparison precedence
    - Comparison evaluation order
    - Short-circuit behaviour
    - Practical validation patterns
"""

# =============================================================================
# 01. Basic Chained Comparison
# =============================================================================

first_value: int = 10
second_value: int = 20
third_value: int = 30

basic_chain: bool = first_value < second_value < third_value

print(basic_chain)

# Equivalent:

equivalent_basic: bool = (
    first_value < second_value
    and second_value < third_value
)

print(equivalent_basic)


# =============================================================================
# 02. Simple Increasing Chain
# =============================================================================

a: int = 1
b: int = 2
c: int = 3

increasing_values: bool = a < b < c

print(increasing_values)


# =============================================================================
# 03. Simple Decreasing Chain
# =============================================================================

x: int = 30
y: int = 20
z: int = 10

decreasing_values: bool = x > y > z

print(decreasing_values)


# =============================================================================
# 04. Less-Than Chain
# =============================================================================

value_04_a: int = 5
value_04_b: int = 10
value_04_c: int = 15

less_than_result: bool = value_04_a < value_04_b < value_04_c

print(less_than_result)


# =============================================================================
# 05. Less-Than-Or-Equal Chain
# =============================================================================

value_05_a: int = 10
value_05_b: int = 10
value_05_c: int = 20

less_equal_result: bool = value_05_a <= value_05_b <= value_05_c

print(less_equal_result)


# =============================================================================
# 06. Greater-Than Chain
# =============================================================================

value_06_a: int = 100
value_06_b: int = 50
value_06_c: int = 25

greater_than_result: bool = value_06_a > value_06_b > value_06_c

print(greater_than_result)


# =============================================================================
# 07. Greater-Than-Or-Equal Chain
# =============================================================================

value_07_a: int = 100
value_07_b: int = 100
value_07_c: int = 50

greater_equal_result: bool = value_07_a >= value_07_b >= value_07_c

print(greater_equal_result)


# =============================================================================
# 08. Equality in a Chain
# =============================================================================

value_08_a: int = 10
value_08_b: int = 10
value_08_c: int = 10

all_equal: bool = value_08_a == value_08_b == value_08_c

print(all_equal)


# =============================================================================
# 09. Equality Chain With Different Values
# =============================================================================

value_09_a: int = 10
value_09_b: int = 10
value_09_c: int = 20

not_all_equal: bool = value_09_a == value_09_b == value_09_c

print(not_all_equal)


# =============================================================================
# 10. Not-Equal Chain
# =============================================================================

value_10_a: int = 10
value_10_b: int = 20
value_10_c: int = 30

different_values: bool = (
    value_10_a != value_10_b != value_10_c
)

print(different_values)


# =============================================================================
# 11. Inclusive Range
# =============================================================================

age: int = 25

valid_age: bool = 18 <= age <= 65

print(valid_age)


# =============================================================================
# 12. Exclusive Range
# =============================================================================

temperature: float = 25.5

comfortable_temperature: bool = 20.0 < temperature < 30.0

print(comfortable_temperature)


# =============================================================================
# 13. Inclusive Lower Bound
# =============================================================================

score: int = 50

valid_score: bool = 50 <= score < 100

print(valid_score)


# =============================================================================
# 14. Inclusive Upper Bound
# =============================================================================

percentage: float = 85.0

valid_percentage: bool = 0.0 < percentage <= 100.0

print(valid_percentage)


# =============================================================================
# 15. Both Bounds Inclusive
# =============================================================================

number: int = 50

inside_range: bool = 1 <= number <= 100

print(inside_range)


# =============================================================================
# 16. Both Bounds Exclusive
# =============================================================================

number_16: int = 50

strictly_inside_range: bool = 1 < number_16 < 100

print(strictly_inside_range)


# =============================================================================
# 17. Mixed Comparison Operators
# =============================================================================

value_17_a: int = 10
value_17_b: int = 20
value_17_c: int = 20

mixed_comparison: bool = (
    value_17_a < value_17_b <= value_17_c
)

print(mixed_comparison)


# =============================================================================
# 18. Greater-Than Followed by Equality
# =============================================================================

value_18_a: int = 30
value_18_b: int = 20
value_18_c: int = 20

mixed_greater_comparison: bool = (
    value_18_a > value_18_b == value_18_c
)

print(mixed_greater_comparison)


# =============================================================================
# 19. Numeric Validation
# =============================================================================

user_age: int = 32

age_is_valid: bool = 18 <= user_age <= 120

print(age_is_valid)


# =============================================================================
# 20. Percentage Validation
# =============================================================================

completion_percentage: float = 75.5

percentage_is_valid: bool = (
    0.0 <= completion_percentage <= 100.0
)

print(percentage_is_valid)


# =============================================================================
# 21. Temperature Validation
# =============================================================================

current_temperature: float = 22.5

temperature_is_valid: bool = (
    -10.0 <= current_temperature <= 50.0
)

print(temperature_is_valid)


# =============================================================================
# 22. Negative Range
# =============================================================================

negative_value: int = -5

negative_range_check: bool = -10 <= negative_value <= -1

print(negative_range_check)


# =============================================================================
# 23. Crossing Zero
# =============================================================================

zero_range_value: int = 5

crossing_zero: bool = -10 < zero_range_value < 10

print(crossing_zero)


# =============================================================================
# 24. Decimal Range
# =============================================================================

price: float = 149.99

valid_price: bool = 100.0 <= price <= 500.0

print(valid_price)


# =============================================================================
# 25. Variable-Based Bounds
# =============================================================================

minimum_value: int = 10
current_value: int = 25
maximum_value: int = 50

within_bounds: bool = (
    minimum_value <= current_value <= maximum_value
)

print(within_bounds)


# =============================================================================
# 26. Chained Comparison Produces Boolean
# =============================================================================

lower_limit: int = 1
middle_value: int = 5
upper_limit: int = 10

comparison_result: bool = (
    lower_limit < middle_value < upper_limit
)

print(type(comparison_result))
print(comparison_result)


# =============================================================================
# 27. Chained Comparison in an if Statement
# =============================================================================

user_score: int = 85

if 0 <= user_score <= 100:
    print("Valid score.")
else:
    print("Invalid score.")


# =============================================================================
# 28. Chained Comparison With Arithmetic
# =============================================================================

number_28: int = 10

arithmetic_chain: bool = (
    5 < number_28 * 2 < 25
)

print(arithmetic_chain)


# =============================================================================
# 29. Chained Comparison With Addition
# =============================================================================

base_value: int = 10

addition_chain: bool = (
    15 < base_value + 10 < 30
)

print(addition_chain)


# =============================================================================
# 30. Chained Comparison With Multiplication
# =============================================================================

quantity: int = 5

multiplication_chain: bool = (
    10 <= quantity * 2 <= 20
)

print(multiplication_chain)


# =============================================================================
# 31. Chained Comparison With Function Result
# =============================================================================

def get_score() -> int:
    """
    Return a sample score.
    """
    return 75


function_score: int = get_score()

score_range_check: bool = 0 <= function_score <= 100

print(score_range_check)


# =============================================================================
# 32. Chained Comparison With String Values
# =============================================================================

first_word: str = "apple"
second_word: str = "banana"
third_word: str = "cherry"

alphabetical_order: bool = (
    first_word < second_word < third_word
)

print(alphabetical_order)


# =============================================================================
# 33. String Equality Chain
# =============================================================================

first_name: str = "Python"
second_name: str = "Python"
third_name: str = "Python"

same_strings: bool = (
    first_name == second_name == third_name
)

print(same_strings)


# =============================================================================
# 34. Character Range
# =============================================================================

character: str = "m"

character_range: bool = "a" <= character <= "z"

print(character_range)


# =============================================================================
# 35. Uppercase Character Range
# =============================================================================

uppercase_character: str = "G"

uppercase_range: bool = "A" <= uppercase_character <= "Z"

print(uppercase_range)


# =============================================================================
# 36. Ascending Order Check
# =============================================================================

first_number: int = 10
second_number: int = 20
third_number: int = 30
fourth_number: int = 40

ascending_order: bool = (
    first_number
    < second_number
    < third_number
    < fourth_number
)

print(ascending_order)


# =============================================================================
# 37. Descending Order Check
# =============================================================================

first_number_37: int = 40
second_number_37: int = 30
third_number_37: int = 20
fourth_number_37: int = 10

descending_order: bool = (
    first_number_37
    > second_number_37
    > third_number_37
    > fourth_number_37
)

print(descending_order)


# =============================================================================
# 38. Four-Value Increasing Chain
# =============================================================================

a_38: int = 1
b_38: int = 5
c_38: int = 10
d_38: int = 15

four_value_chain: bool = a_38 < b_38 < c_38 < d_38

print(four_value_chain)


# =============================================================================
# 39. Four-Value Decreasing Chain
# =============================================================================

a_39: int = 100
b_39: int = 75
c_39: int = 50
d_39: int = 25

four_value_decreasing: bool = a_39 > b_39 > c_39 > d_39

print(four_value_decreasing)


# =============================================================================
# 40. Multiple Equal Values
# =============================================================================

a_40: int = 5
b_40: int = 5
c_40: int = 5
d_40: int = 5

all_values_equal: bool = a_40 == b_40 == c_40 == d_40

print(all_values_equal)


# =============================================================================
# 41. Mixed Equality and Ordering
# =============================================================================

a_41: int = 10
b_41: int = 10
c_41: int = 20
d_41: int = 20

mixed_chain: bool = (
    a_41 == b_41 < c_41 == d_41
)

print(mixed_chain)


# =============================================================================
# 42. Avoiding Unnecessary and
# =============================================================================

value_42: int = 50

direct_chain: bool = 0 <= value_42 <= 100

print(direct_chain)

# Instead of:

separate_comparisons: bool = (
    0 <= value_42
    and value_42 <= 100
)

print(separate_comparisons)


# =============================================================================
# 43. Chained Comparison With Boolean Logic
# =============================================================================

age_43: int = 30
has_permission: bool = True

access_allowed: bool = (
    18 <= age_43 <= 65
    and has_permission
)

print(access_allowed)


# =============================================================================
# 44. Multiple Chained Conditions
# =============================================================================

score_44: int = 85
attendance_44: float = 95.0

eligible: bool = (
    50 <= score_44 <= 100
    and 75.0 <= attendance_44 <= 100.0
)

print(eligible)


# =============================================================================
# 45. Short-Circuit Behaviour
# =============================================================================

value_45: int = 5

short_circuit_result: bool = (
    10 < value_45 < 20
)

print(short_circuit_result)

# The first comparison:

#     10 < 5

# is False.

# Python does not need to evaluate the remaining comparison.


# =============================================================================
# 46. Comparison Evaluation Order
# =============================================================================

left_value: int = 10
middle_value: int = 20
right_value: int = 30

evaluation_order_result: bool = (
    left_value < middle_value < right_value
)

print(evaluation_order_result)

# The comparisons are evaluated from left to right.


# =============================================================================
# 47. Chained Comparisons Are Not the Same as Independent Comparisons
# =============================================================================

value_47_a: int = 1
value_47_b: int = 2
value_47_c: int = 3

chained_result: bool = (
    value_47_a < value_47_b < value_47_c
)

independent_result: bool = (
    value_47_a < value_47_b
    and value_47_b < value_47_c
)

print(chained_result)
print(independent_result)


# =============================================================================
# 48. Range Validation Function
# =============================================================================

def is_valid_age(age: int) -> bool:
    """
    Return True when age is within the valid range.
    """
    return 0 <= age <= 120


valid_age_result: bool = is_valid_age(30)

print(valid_age_result)


# =============================================================================
# 49. Percentage Validation Function
# =============================================================================

def is_valid_percentage(value: float) -> bool:
    """
    Return True when value is a valid percentage.
    """
    return 0.0 <= value <= 100.0


valid_percentage_result: bool = is_valid_percentage(85.5)

print(valid_percentage_result)


# =============================================================================
# 50. Practical Range Validation
# =============================================================================

def is_valid_temperature(
    temperature: float,
) -> bool:
    """
    Return True when temperature is inside the supported range.
    """
    return -50.0 <= temperature <= 60.0


temperature_result: bool = is_valid_temperature(25.0)

print(temperature_result)


# =============================================================================
# 51. Practical Score Validation
# =============================================================================

def is_valid_score(score: int) -> bool:
    """
    Return True when score is between 0 and 100 inclusive.
    """
    return 0 <= score <= 100


score_result: bool = is_valid_score(90)

print(score_result)


# =============================================================================
# 52. Practical Price Validation
# =============================================================================

def is_valid_price(
    price: float,
) -> bool:
    """
    Return True when price is within the accepted range.
    """
    return 0.0 < price <= 1_000_000.0


price_result: bool = is_valid_price(999.99)

print(price_result)


# =============================================================================
# 53. Strictly Increasing Three Values
# =============================================================================

def is_strictly_increasing(
    first: int,
    second: int,
    third: int,
) -> bool:
    """
    Return True when three values are strictly increasing.
    """
    return first < second < third


increasing_result: bool = is_strictly_increasing(
    10,
    20,
    30,
)

print(increasing_result)


# =============================================================================
# 54. Non-Decreasing Three Values
# =============================================================================

def is_non_decreasing(
    first: int,
    second: int,
    third: int,
) -> bool:
    """
    Return True when values never decrease.
    """
    return first <= second <= third


non_decreasing_result: bool = is_non_decreasing(
    10,
    10,
    20,
)

print(non_decreasing_result)


# =============================================================================
# 55. Strictly Decreasing Three Values
# =============================================================================

def is_strictly_decreasing(
    first: int,
    second: int,
    third: int,
) -> bool:
    """
    Return True when three values are strictly decreasing.
    """
    return first > second > third


decreasing_result: bool = is_strictly_decreasing(
    30,
    20,
    10,
)

print(decreasing_result)


# =============================================================================
# 56. Non-Increasing Three Values
# =============================================================================

def is_non_increasing(
    first: int,
    second: int,
    third: int,
) -> bool:
    """
    Return True when values never increase.
    """
    return first >= second >= third


non_increasing_result: bool = is_non_increasing(
    30,
    30,
    20,
)

print(non_increasing_result)


# =============================================================================
# 57. Range With Negative and Positive Bounds
# =============================================================================

coordinate_x: float = 15.5

valid_coordinate: bool = (
    -100.0 <= coordinate_x <= 100.0
)

print(valid_coordinate)


# =============================================================================
# 58. Multiple Comparison Operators
# =============================================================================

value_58_a: int = 5
value_58_b: int = 10
value_58_c: int = 10
value_58_d: int = 20

complex_chain: bool = (
    value_58_a < value_58_b
    <= value_58_c
    < value_58_d
)

print(complex_chain)


# =============================================================================
# 59. Chained Comparison With Variables From a Collection
# =============================================================================

numbers_59: list[int] = [10, 20, 30]

first_59: int = numbers_59[0]
second_59: int = numbers_59[1]
third_59: int = numbers_59[2]

collection_order: bool = first_59 < second_59 < third_59

print(collection_order)


# =============================================================================
# 60. Final Practical Example
# =============================================================================

def validate_exam_result(
    score: int,
    attendance: float,
) -> bool:
    """
    Validate an exam result using chained comparisons.

    Conditions:

        score must be between 0 and 100 inclusive.
        attendance must be between 75 and 100 inclusive.
    """
    valid_score: bool = 0 <= score <= 100
    valid_attendance: bool = 75.0 <= attendance <= 100.0

    return valid_score and valid_attendance


exam_is_valid: bool = validate_exam_result(
    score=85,
    attendance=92.5,
)

print(exam_is_valid)


# =============================================================================
# Chained Comparison Summary
# =============================================================================
"""
Chained comparisons allow multiple comparisons to be written naturally.

Basic form:

    a < b < c

Equivalent logical form:

    a < b and b < c

Range validation:

    minimum <= value <= maximum

Strict range:

    minimum < value < maximum

Increasing values:

    a < b < c

Non-decreasing values:

    a <= b <= c

Decreasing values:

    a > b > c

Non-increasing values:

    a >= b >= c

Equality:

    a == b == c

Inequality:

    a != b != c

Mixed comparisons:

    a < b <= c < d

Important:

    Chained comparisons are evaluated from left to right.

    Python stops evaluating the chain when a comparison is false.

    The middle expressions in a chained comparison are evaluated only once.

Prefer:

    0 <= score <= 100

over:

    0 <= score and score <= 100

when a range check is what the code means.

Core idea:

    LOWER_BOUND
         <
       VALUE
         <
    UPPER_BOUND

becomes:

    LOWER_BOUND < VALUE < UPPER_BOUND

Chained comparisons make range checks, ordering checks, and validation
conditions concise and readable.
"""

# =============================================================================
# End of 11_chained_comparisons.py
# =============================================================================