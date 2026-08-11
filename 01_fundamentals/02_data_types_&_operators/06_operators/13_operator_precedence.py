# type: ignore
# =============================================================================
# 13. Operator Precedence
# =============================================================================
"""
Python Operators

File:
13_operator_precedence.py

Topic:
Operator Precedence

Overview:
Operator precedence determines the order in which Python evaluates
different operators in an expression.

When an expression contains multiple operators, Python follows a
defined precedence hierarchy.

Example:

    result = 2 + 3 * 4

Multiplication has higher precedence than addition, so Python evaluates:

    3 * 4
    ↓
    12

Then:

    2 + 12
    ↓
    14

Parentheses can be used to explicitly control evaluation order.

This file demonstrates the most important operator-precedence rules
using distinct practical examples.

Common precedence order from higher to lower:

    1. Parentheses
    2. Exponentiation
    3. Unary +, -, ~
    4. Multiplication, division, floor division, modulo
    5. Addition and subtraction
    6. Shifts
    7. Bitwise &
    8. Bitwise ^
    9. Bitwise |
    10. Comparisons, membership, identity
    11. not
    12. and
    13. or
    14. Conditional expression
    15. lambda

Important:
    When in doubt, use parentheses.

Parentheses make the intended evaluation order explicit and improve
readability.
"""


# =============================================================================
# 01. Basic Arithmetic Precedence
# =============================================================================

result_01: int = 10 + 5 * 2

print(result_01)

# Multiplication is evaluated before addition.

# Equivalent to:
#
# 10 + (5 * 2)
#
# Result:
#
# 20


# =============================================================================
# 02. Parentheses Override Precedence
# =============================================================================

result_02: int = (10 + 5) * 2

print(result_02)

# Parentheses force addition to happen first.
#
# Equivalent to:
#
# (10 + 5) * 2
#
# Result:
#
# 30


# =============================================================================
# 03. Multiplication Before Subtraction
# =============================================================================

result_03: int = 20 - 4 * 3

print(result_03)

# Equivalent to:
#
# 20 - (4 * 3)
#
# Result:
#
# 8


# =============================================================================
# 04. Division Before Addition
# =============================================================================

result_04: float = 20 + 10 / 2

print(result_04)

# Equivalent to:
#
# 20 + (10 / 2)
#
# Result:
#
# 25.0


# =============================================================================
# 05. Floor Division Before Addition
# =============================================================================

result_05: int = 20 + 11 // 3

print(result_05)

# Equivalent to:
#
# 20 + (11 // 3)
#
# Result:
#
# 23


# =============================================================================
# 06. Modulo Before Addition
# =============================================================================

result_06: int = 20 + 11 % 3

print(result_06)

# Equivalent to:
#
# 20 + (11 % 3)
#
# Result:
#
# 22


# =============================================================================
# 07. Multiplication and Division Have Equal Precedence
# =============================================================================

result_07: float = 100 / 5 * 2

print(result_07)

# Operators with equal precedence are evaluated from left to right.
#
# Equivalent to:
#
# (100 / 5) * 2
#
# Result:
#
# 40.0


# =============================================================================
# 08. Addition and Subtraction Have Equal Precedence
# =============================================================================

result_08: int = 100 - 20 + 5

print(result_08)

# Evaluation proceeds from left to right.
#
# Equivalent to:
#
# (100 - 20) + 5
#
# Result:
#
# 85


# =============================================================================
# 09. Exponentiation Before Multiplication
# =============================================================================

result_09: int = 2 * 3**2

print(result_09)

# Equivalent to:
#
# 2 * (3**2)
#
# Result:
#
# 18


# =============================================================================
# 10. Exponentiation Before Addition
# =============================================================================

result_10: int = 5 + 2**3

print(result_10)

# Equivalent to:
#
# 5 + (2**3)
#
# Result:
#
# 13


# =============================================================================
# 11. Parentheses Around Exponentiation Base
# =============================================================================

result_11: int = (2 + 3) ** 2

print(result_11)

# Parentheses cause the addition to happen first.
#
# Equivalent to:
#
# (2 + 3) ** 2
#
# Result:
#
# 25


# =============================================================================
# 12. Parentheses Around Exponentiation Result
# =============================================================================

result_12: int = (2**3) + 4

print(result_12)

# Equivalent to:
#
# 8 + 4
#
# Result:
#
# 12


# =============================================================================
# 13. Unary Minus and Exponentiation
# =============================================================================

result_13: int = -2**2

print(result_13)

# Exponentiation has higher precedence than unary minus on its left.
#
# Therefore this is interpreted as:
#
# -(2**2)
#
# Result:
#
# -4


# =============================================================================
# 14. Parentheses Change Unary Minus Behavior
# =============================================================================

result_14: int = (-2) ** 2

print(result_14)

# The parentheses make -2 the base.
#
# Equivalent to:
#
# (-2) ** 2
#
# Result:
#
# 4


# =============================================================================
# 15. Unary Plus
# =============================================================================

result_15: int = +5 * 2

print(result_15)

# Unary plus applies to 5 before multiplication.
#
# Equivalent to:
#
# (+5) * 2
#
# Result:
#
# 10


# =============================================================================
# 16. Unary Minus With Multiplication
# =============================================================================

result_16: int = -5 * 2

print(result_16)

# Equivalent to:
#
# (-5) * 2
#
# Result:
#
# -10


# =============================================================================
# 17. Unary Bitwise NOT
# =============================================================================

result_17: int = ~5 + 2

print(result_17)

# Unary ~ has higher precedence than addition.
#
# Equivalent to:
#
# (~5) + 2
#
# Result:
#
# -4


# =============================================================================
# 18. Multiplication Before Addition With Variables
# =============================================================================

price: float = 100.0
quantity: int = 3
shipping: float = 20.0

total_18: float = price * quantity + shipping

print(total_18)

# Equivalent to:
#
# (price * quantity) + shipping
#
# Result:
#
# 320.0


# =============================================================================
# 19. Parentheses For Business Logic
# =============================================================================

discount: float = 10.0

final_price_19: float = price * quantity - discount

print(final_price_19)

# Equivalent to:
#
# (price * quantity) - discount
#
# Result:
#
# 290.0


# =============================================================================
# 20. Parentheses Change Business Logic
# =============================================================================

final_price_20: float = price * (quantity - discount)

print(final_price_20)

# Parentheses change the meaning completely.
#
# This example is mathematically valid but usually not meaningful
# for real pricing logic.
#
# Always use parentheses when business logic could be ambiguous.


# =============================================================================
# 21. Comparison After Arithmetic
# =============================================================================

comparison_21: bool = 10 + 5 > 12

print(comparison_21)

# Arithmetic has higher precedence than comparison.
#
# Equivalent to:
#
# (10 + 5) > 12
#
# Result:
#
# True


# =============================================================================
# 22. Multiplication Before Comparison
# =============================================================================

comparison_22: bool = 5 * 3 == 15

print(comparison_22)

# Equivalent to:
#
# (5 * 3) == 15
#
# Result:
#
# True


# =============================================================================
# 23. Arithmetic Before Boolean and
# =============================================================================

result_23: bool = 10 + 5 > 10 and 20 > 5

print(result_23)

# Equivalent to:
#
# ((10 + 5) > 10) and (20 > 5)
#
# Result:
#
# True


# =============================================================================
# 24. Comparison Before Boolean and
# =============================================================================

result_24: bool = 5 * 2 == 10 and 3 < 5

print(result_24)

# Arithmetic:
#
# 5 * 2
#
# Comparison:
#
# 10 == 10
#
# and:
#
# True and True


# =============================================================================
# 25. not Has Lower Precedence Than Comparisons
# =============================================================================

result_25: bool = not 5 > 3

print(result_25)

# Equivalent to:
#
# not (5 > 3)
#
# Result:
#
# False


# =============================================================================
# 26. Parentheses With not
# =============================================================================

result_26: bool = (not 5 > 3)

print(result_26)

# Explicitly expresses:
#
# not (5 > 3)


# =============================================================================
# 27. not Before and
# =============================================================================

result_27: bool = not False and True

print(result_27)

# not has higher precedence than and.
#
# Equivalent to:
#
# (not False) and True
#
# Result:
#
# True


# =============================================================================
# 28. and Before or
# =============================================================================

result_28: bool = False or True and False

print(result_28)

# and has higher precedence than or.
#
# Equivalent to:
#
# False or (True and False)
#
# Result:
#
# False


# =============================================================================
# 29. Parentheses Change and/or Evaluation
# =============================================================================

result_29: bool = (False or True) and False

print(result_29)

# Parentheses force or to happen first.
#
# Equivalent to:
#
# (False or True) and False
#
# Result:
#
# False


# =============================================================================
# 30. or With Comparisons
# =============================================================================

age: int = 25

result_30: bool = age < 18 or age > 60

print(result_30)

# Comparisons are evaluated before or.
#
# Equivalent to:
#
# (age < 18) or (age > 60)


# =============================================================================
# 31. and With Comparisons
# =============================================================================

score: int = 85

result_31: bool = score >= 50 and score <= 100

print(result_31)

# Equivalent to:
#
# (score >= 50) and (score <= 100)


# =============================================================================
# 32. Comparison and Membership Operator
# =============================================================================

languages: list[str] = [
    "Python",
    "Java",
    "Go",
]

result_32: bool = "Python" in languages and len(languages) == 3

print(result_32)

# Membership and comparison expressions are evaluated before and.
#
# Equivalent to:
#
# ("Python" in languages) and (len(languages) == 3)


# =============================================================================
# 33. Identity and Comparison Operators
# =============================================================================

first_value: None = None

result_33: bool = first_value is None

print(result_33)

# Identity operators are part of the comparison level of precedence.
#
# Equivalent to:
#
# first_value is None


# =============================================================================
# 34. Membership With not
# =============================================================================

languages_34: list[str] = [
    "Python",
    "Java",
]

result_34: bool = "Go" not in languages_34

print(result_34)

# Membership testing is evaluated as part of comparison-level operations.


# =============================================================================
# 35. Bitwise AND Before Bitwise OR
# =============================================================================

result_35: int = 6 | 4 & 3

print(result_35)

# Bitwise AND has higher precedence than bitwise OR.
#
# Equivalent to:
#
# 6 | (4 & 3)


# =============================================================================
# 36. Bitwise XOR Between AND and OR
# =============================================================================

result_36: int = 6 | 4 ^ 3

print(result_36)

# Bitwise XOR has higher precedence than bitwise OR.
#
# Equivalent to:
#
# 6 | (4 ^ 3)


# =============================================================================
# 37. Parentheses With Bitwise Operators
# =============================================================================

result_37: int = (6 | 4) & 3

print(result_37)

# Parentheses force bitwise OR to happen first.


# =============================================================================
# 38. Shift Operators Have Lower Precedence Than Addition
# =============================================================================

result_38: int = 1 + 2 << 2

print(result_38)

# Addition has higher precedence than shifting.
#
# Equivalent to:
#
# (1 + 2) << 2
#
# Result:
#
# 12


# =============================================================================
# 39. Parentheses Change Shift Evaluation
# =============================================================================

result_39: int = 1 + (2 << 2)

print(result_39)

# Equivalent to:
#
# 1 + 8
#
# Result:
#
# 9


# =============================================================================
# 40. Conditional Expression
# =============================================================================

temperature: int = 25

description_40: str = "hot" if temperature > 30 else "comfortable"

print(description_40)

# Conditional expressions have lower precedence than most operators.
#
# The condition:
#
# temperature > 30
#
# is evaluated before selecting the result.


# =============================================================================
# 41. Conditional Expression With Arithmetic
# =============================================================================

value_41: int = 10

result_41: int = value_41 * 2 if value_41 > 5 else value_41 + 2

print(result_41)

# Equivalent to:
#
# (value_41 * 2) if (value_41 > 5) else (value_41 + 2)


# =============================================================================
# 42. Parentheses Make Conditional Expressions Clear
# =============================================================================

result_42: int = (
    (value_41 * 2)
    if (value_41 > 5)
    else (value_41 + 2)
)

print(result_42)


# =============================================================================
# 43. Comparison Chaining
# =============================================================================

number_43: int = 50

result_43: bool = 10 < number_43 < 100

print(result_43)

# Chained comparisons have comparison-level precedence.
#
# This is conceptually similar to:
#
# 10 < number_43 and number_43 < 100
#
# Python handles chained comparisons directly.


# =============================================================================
# 44. Parentheses Around Comparison
# =============================================================================

result_44: bool = (10 + 5) > (3 * 4)

print(result_44)

# Arithmetic occurs inside the parentheses before the comparison.


# =============================================================================
# 45. Assignment Expression Precedence
# =============================================================================

numbers_45: list[int] = [
    10,
    20,
    30,
]

if (count_45 := len(numbers_45)) > 2:
    print(count_45)

# The assignment expression:
#
# count_45 := len(numbers_45)
#
# produces the value assigned to count_45.
#
# Parentheses make the intended expression boundary explicit.


# =============================================================================
# 46. Operator Precedence With Function Calls
# =============================================================================

def get_value_46() -> int:
    """
    Return a value for a precedence example.
    """
    return 10


result_46: int = get_value_46() + 5 * 2

print(result_46)

# Function calls and primary expressions are evaluated before arithmetic
# operators.
#
# Equivalent to:
#
# get_value_46() + (5 * 2)


# =============================================================================
# 47. Attribute Access Before Arithmetic
# =============================================================================

text_47: str = "Python"

result_47: int = len(text_47) + 5

print(result_47)

# The function call:
#
# len(text_47)
#
# is evaluated before addition.


# =============================================================================
# 48. Parentheses Improve Complex Expressions
# =============================================================================

price_48: float = 100.0
quantity_48: int = 4
discount_48: float = 0.10
tax_48: float = 0.18

total_48: float = (
    (price_48 * quantity_48)
    * (1 - discount_48)
    * (1 + tax_48)
)

print(total_48)

# Parentheses make each logical stage explicit:
#
# price * quantity
#       ↓
# subtotal
#       ↓
# discount
#       ↓
# tax
#       ↓
# final total


# =============================================================================
# 49. Avoid Relying On Complex Precedence
# =============================================================================

result_49: bool = (
    (price_48 > 50)
    and (quantity_48 >= 2)
    or (discount_48 > 0)
)

print(result_49)

# Python evaluates and before or.
#
# However, explicit parentheses make the intended logic easier to read.
#
# Equivalent to:
#
# ((price_48 > 50) and (quantity_48 >= 2))
# or (discount_48 > 0)


# =============================================================================
# 50. Best Practice: Use Parentheses For Readability
# =============================================================================

income: float = 5000.0
expenses: float = 3000.0
tax_rate: float = 0.20

taxable_income: float = max(
    0.0,
    income - expenses,
)

tax: float = taxable_income * tax_rate

remaining_income: float = (
    income
    - expenses
    - tax
)

print(remaining_income)

# Even when Python's precedence rules would produce the same result,
# parentheses can make business logic easier to understand.
#
# Prefer:
#
# remaining_income = (
#     income
#     - expenses
#     - tax
# )
#
# over unnecessarily dense expressions.


# =============================================================================
# Operator Precedence Reference
# =============================================================================

"""
A simplified precedence hierarchy from higher to lower:

1. Parentheses / grouping
2. Function calls, indexing, attribute access
3. Exponentiation **
4. Unary +, -, ~
5. *, /, //, %
6. +, -
7. <<, >>
8. &
9. ^
10. |
11. Comparisons:
        < <= > >=
        == !=
        is
        is not
        in
        not in
12. not
13. and
14. or
15. Conditional expression:
        x if condition else y
16. lambda

Important details:

Exponentiation:

    **

has special associativity behaviour.

For example:

    2 ** 3 ** 2

is evaluated as:

    2 ** (3 ** 2)

not:

    (2 ** 3) ** 2

Most operators at the same precedence level are evaluated from left
to right.

Examples:

    100 / 5 * 2

becomes:

    (100 / 5) * 2

and:

    100 - 20 + 5

becomes:

    (100 - 20) + 5

However, operator associativity has exceptions, so always consult
Python's precedence rules when dealing with unusual expressions.
"""


# =============================================================================
# Operator Precedence Cheat Sheet
# =============================================================================

"""
HIGHER PRECEDENCE
        ↓

    ()
    function calls
    indexing
    attribute access

        ↓

    **

        ↓

    +x
    -x
    ~x

        ↓

    *
    /
    //
    %

        ↓

    +
    -

        ↓

    <<
    >>

        ↓

    &

        ↓

    ^

        ↓

    |

        ↓

    comparisons
    in
    not in
    is
    is not
    ==
    !=
    <
    <=
    >
    >=

        ↓

    not

        ↓

    and

        ↓

    or

        ↓

    x if condition else y

        ↓

    lambda

LOWER PRECEDENCE
"""


# =============================================================================
# Important Rule 1: Parentheses Win
# =============================================================================

expression_1: int = 10 + 2 * 3

expression_2: int = (10 + 2) * 3

print(expression_1)

print(expression_2)

# Without parentheses:
#
# 10 + (2 * 3)
#
# Result:
#
# 16
#
# With parentheses:
#
# (10 + 2) * 3
#
# Result:
#
# 36


# =============================================================================
# Important Rule 2: Multiplication Before Addition
# =============================================================================

expression_3: int = 2 + 3 * 4

print(expression_3)

# Result:
#
# 14
#
# Not:
#
# 20


# =============================================================================
# Important Rule 3: Comparisons After Arithmetic
# =============================================================================

expression_4: bool = 2 + 3 * 4 > 10

print(expression_4)

# Equivalent to:
#
# (2 + (3 * 4)) > 10


# =============================================================================
# Important Rule 4: not Before and
# =============================================================================

expression_5: bool = not False and True

print(expression_5)

# Equivalent to:
#
# (not False) and True


# =============================================================================
# Important Rule 5: and Before or
# =============================================================================

expression_6: bool = True or False and False

print(expression_6)

# Equivalent to:
#
# True or (False and False)


# =============================================================================
# Important Rule 6: Parentheses Override Boolean Precedence
# =============================================================================

expression_7: bool = (True or False) and False

print(expression_7)

# Parentheses force or to execute first.


# =============================================================================
# Important Rule 7: Exponentiation Is Higher Than Multiplication
# =============================================================================

expression_8: int = 2 * 3**2

print(expression_8)

# Equivalent to:
#
# 2 * (3**2)


# =============================================================================
# Important Rule 8: Unary Minus and Exponentiation
# =============================================================================

expression_9: int = -2**2
expression_10: int = (-2) ** 2

print(expression_9)

print(expression_10)

# Results:
#
# -4
#  4
#
# Parentheses change the base of exponentiation.


# =============================================================================
# Important Rule 9: Same-Level Operators Usually Associate Left To Right
# =============================================================================

expression_11: float = 100 / 10 * 2

print(expression_11)

# Equivalent to:
#
# (100 / 10) * 2


# =============================================================================
# Important Rule 10: Exponentiation Associates Right To Left
# =============================================================================

expression_12: int = 2**3**2

print(expression_12)

# Equivalent to:
#
# 2 ** (3 ** 2)
#
# Therefore:
#
# 2 ** 9
#
# Result:
#
# 512


# =============================================================================
# Practical Example 1: Order Calculation
# =============================================================================

unit_price: float = 25.0
quantity: int = 4
shipping_cost: float = 10.0

order_total: float = (
    (unit_price * quantity)
    + shipping_cost
)

print(order_total)


# =============================================================================
# Practical Example 2: Discount Calculation
# =============================================================================

product_price: float = 1000.0
discount_rate: float = 0.15

discounted_price: float = (
    product_price
    * (1 - discount_rate)
)

print(discounted_price)


# =============================================================================
# Practical Example 3: Tax Calculation
# =============================================================================

tax_rate: float = 0.18

final_price: float = (
    discounted_price
    * (1 + tax_rate)
)

print(final_price)


# =============================================================================
# Practical Example 4: Eligibility Check
# =============================================================================

age_eligible: int = 25
has_license: bool = True

is_eligible: bool = (
    (age_eligible >= 18)
    and has_license
)

print(is_eligible)


# =============================================================================
# Practical Example 5: Range Check
# =============================================================================

score_5: int = 85

is_valid_score: bool = (
    0 <= score_5 <= 100
)

print(is_valid_score)


# =============================================================================
# Practical Example 6: Multiple Conditions
# =============================================================================

user_is_active: bool = True
user_is_admin: bool = False
user_is_owner: bool = True

can_manage: bool = (
    user_is_active
    and (user_is_admin or user_is_owner)
)

print(can_manage)

# Parentheses clearly communicate the intended logic:
#
# active AND (admin OR owner)


# =============================================================================
# Practical Example 7: Bitwise Permission Check
# =============================================================================

READ_PERMISSION: int = 1
WRITE_PERMISSION: int = 2
EXECUTE_PERMISSION: int = 4

permissions: int = (
    READ_PERMISSION
    | WRITE_PERMISSION
)

has_write_permission: bool = (
    permissions & WRITE_PERMISSION
) != 0

print(has_write_permission)

# Parentheses make the bitwise operation and comparison boundary explicit.


# =============================================================================
# Practical Example 8: Average Calculation
# =============================================================================

total_score: float = 450.0
number_of_students: int = 5

average_score: float = (
    total_score
    / number_of_students
)

print(average_score)


# =============================================================================
# Practical Example 9: Percentage Calculation
# =============================================================================

completed_tasks: int = 45
total_tasks: int = 50

completion_percentage: float = (
    completed_tasks
    / total_tasks
    * 100
)

print(completion_percentage)


# =============================================================================
# Practical Example 10: Safe Complex Expression
# =============================================================================

base_price: float = 500.0
quantity_10: int = 3
discount_percentage: float = 10.0
tax_percentage: float = 18.0

subtotal_10: float = (
    base_price
    * quantity_10
)

discount_amount_10: float = (
    subtotal_10
    * discount_percentage
    / 100
)

price_after_discount_10: float = (
    subtotal_10
    - discount_amount_10
)

tax_amount_10: float = (
    price_after_discount_10
    * tax_percentage
    / 100
)

final_amount_10: float = (
    price_after_discount_10
    + tax_amount_10
)

print(final_amount_10)


# =============================================================================
# Best Practices
# =============================================================================

"""
Best practices for operator precedence:

1. Know the common precedence hierarchy.

2. Use parentheses when the expression is not immediately obvious.

3. Do not rely on readers remembering obscure precedence rules.

4. Use parentheses around complex boolean conditions.

5. Use parentheses around complex arithmetic calculations.

6. Break very complicated expressions into meaningful intermediate
   variables.

7. Remember that *, /, //, and % have higher precedence than + and -.

8. Remember that comparisons occur before not, and, and or.

9. Remember that and has higher precedence than or.

10. Be especially careful with unary minus and exponentiation.

11. Remember that exponentiation associates from right to left.

12. Avoid unnecessarily dense expressions.

13. Prefer readability over saving a pair of parentheses.

14. Use intermediate variables when an expression represents multiple
    business concepts.

15. Parentheses are not only for changing behaviour; they can also
    communicate intent.


Example:

    final_price = (
        (price * quantity)
        * (1 - discount_rate)
        * (1 + tax_rate)
    )

This is often easier to understand than:

    final_price = price * quantity * (1 - discount_rate) * (1 + tax_rate)


For complicated logic, prefer:

    is_valid_user = (
        user_is_active
        and (user_is_admin or user_is_owner)
    )

instead of depending entirely on:

    user_is_active and user_is_admin or user_is_owner
"""


# =============================================================================
# Summary
# =============================================================================

"""
Operator precedence determines which operators are evaluated first.

Core hierarchy:

    Parentheses
        ↓
    Function calls / indexing / attributes
        ↓
    Exponentiation
        ↓
    Unary operators
        ↓
    Multiplication / division / floor division / modulo
        ↓
    Addition / subtraction
        ↓
    Shifts
        ↓
    Bitwise AND
        ↓
    Bitwise XOR
        ↓
    Bitwise OR
        ↓
    Comparisons / membership / identity
        ↓
    not
        ↓
    and
        ↓
    or
        ↓
    Conditional expression
        ↓
    lambda

Important examples:

    2 + 3 * 4
    -> 14

    (2 + 3) * 4
    -> 20

    2 * 3**2
    -> 18

    -2**2
    -> -4

    (-2)**2
    -> 4

    True or False and False
    -> True

    (True or False) and False
    -> False

    2**3**2
    -> 512

The most important practical rule is:

    When an expression is difficult to read,
    use parentheses or split it into smaller expressions.

Operator precedence is part of Python's syntax rules, but readable code
should make important evaluation order obvious.
"""


# =============================================================================
# End of 13_operator_precedence.py
# =============================================================================