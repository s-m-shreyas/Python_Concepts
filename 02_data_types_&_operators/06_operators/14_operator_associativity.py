# type: ignore
# =============================================================================
# 14. Operator Associativity
# =============================================================================
"""
Python Operators

File:
14_operator_associativity.py

Topic:
Operator Associativity

Overview:

Operator associativity determines how operators with the same precedence
are grouped when an expression contains multiple operators.

For example:

    100 - 20 - 10

Subtraction has left-to-right associativity.

Therefore Python evaluates it as:

    (100 - 20) - 10

which gives:

    70

Associativity is different from precedence.

Precedence answers:

    "Which operator is evaluated first?"

Associativity answers:

    "When operators have the same precedence, how are they grouped?"

Most Python binary operators associate from left to right.

Important exceptions include:

    **

Exponentiation associates from right to left.

Conditional expressions also associate from right to left.

Comparisons are special because chained comparisons are interpreted as
a sequence of comparisons rather than ordinary left-to-right or
right-to-left grouping.

This file demonstrates the most important associativity rules.
"""


# =============================================================================
# 01. Basic Left-to-Right Subtraction
# =============================================================================

result_01: int = 100 - 20 - 10

print(result_01)

# Subtraction associates from left to right.
#
# Equivalent to:
#
# (100 - 20) - 10
#
# Result:
#
# 70


# =============================================================================
# 02. Right-to-Left Subtraction Would Produce a Different Result
# =============================================================================

result_02: int = 100 - (20 - 10)

print(result_02)

# Parentheses explicitly force right-side grouping.
#
# Result:
#
# 90
#
# This is different from:
#
# 100 - 20 - 10
#
# which produces:
#
# 70


# =============================================================================
# 03. Left-to-Right Addition
# =============================================================================

result_03: int = 10 + 20 + 30

print(result_03)

# Addition is left associative.
#
# Equivalent to:
#
# (10 + 20) + 30


# =============================================================================
# 04. Parentheses Can Explicitly Group Addition
# =============================================================================

result_04: int = 10 + (20 + 30)

print(result_04)

# The numerical result is the same:
#
# 60
#
# But the grouping is explicitly right-sided.


# =============================================================================
# 05. Left-to-Right Division
# =============================================================================

result_05: float = 100 / 10 / 2

print(result_05)

# Division associates from left to right.
#
# Equivalent to:
#
# (100 / 10) / 2
#
# Result:
#
# 5.0


# =============================================================================
# 06. Parentheses Change Division Grouping
# =============================================================================

result_06: float = 100 / (10 / 2)

print(result_06)

# Equivalent to:
#
# 100 / 5
#
# Result:
#
# 20.0


# =============================================================================
# 07. Left-to-Right Floor Division
# =============================================================================

result_07: int = 100 // 10 // 2

print(result_07)

# Equivalent to:
#
# (100 // 10) // 2


# =============================================================================
# 08. Parentheses Change Floor-Division Grouping
# =============================================================================

result_08: int = 100 // (10 // 2)

print(result_08)

# Equivalent to:
#
# 100 // 5
#
# Result:
#
# 20


# =============================================================================
# 09. Left-to-Right Modulo
# =============================================================================

result_09: int = 100 % 30 % 7

print(result_09)

# Equivalent to:
#
# (100 % 30) % 7
#
# Result:
#
# 10


# =============================================================================
# 10. Parentheses Change Modulo Grouping
# =============================================================================

result_10: int = 100 % (30 % 7)

print(result_10)

# Equivalent to:
#
# 100 % 2
#
# Result:
#
# 0


# =============================================================================
# 11. Multiplication Is Left Associative
# =============================================================================

result_11: int = 2 * 3 * 4

print(result_11)

# Equivalent to:
#
# (2 * 3) * 4


# =============================================================================
# 12. Parentheses With Multiplication
# =============================================================================

result_12: int = 2 * (3 * 4)

print(result_12)

# Both expressions produce:
#
# 24
#
# Multiplication is associative mathematically, but Python still
# follows its defined left-to-right grouping for the expression.


# =============================================================================
# 13. Mixed Multiplication and Division
# =============================================================================

result_13: float = 100 / 5 * 2

print(result_13)

# / and * have the same precedence.
#
# They therefore follow left-to-right associativity.
#
# Equivalent to:
#
# (100 / 5) * 2
#
# Result:
#
# 40.0


# =============================================================================
# 14. Reversing the Grouping
# =============================================================================

result_14: float = 100 / (5 * 2)

print(result_14)

# Parentheses change the grouping.
#
# Result:
#
# 10.0
#
# This demonstrates why associativity matters.


# =============================================================================
# 15. Mixed Addition and Subtraction
# =============================================================================

result_15: int = 100 - 20 + 5

print(result_15)

# + and - have the same precedence.
#
# They associate from left to right.
#
# Equivalent to:
#
# (100 - 20) + 5
#
# Result:
#
# 85


# =============================================================================
# 16. Explicit Right Grouping
# =============================================================================

result_16: int = 100 - (20 + 5)

print(result_16)

# Result:
#
# 75
#
# This differs from:
#
# (100 - 20) + 5
#
# which produces:
#
# 85


# =============================================================================
# 17. Mixed Addition and Subtraction
# =============================================================================

result_17: int = 50 + 20 - 10 + 5

print(result_17)

# Equivalent to:
#
# (((50 + 20) - 10) + 5)


# =============================================================================
# 18. Explicit Grouping of Mixed Addition
# =============================================================================

result_18: int = 50 + (20 - 10) + 5

print(result_18)

# Parentheses make the intended grouping explicit.


# =============================================================================
# 19. Mixed Multiplication and Modulo
# =============================================================================

result_19: int = 20 * 7 % 6

print(result_19)

# * and % have the same precedence.
#
# Left-to-right:
#
# (20 * 7) % 6


# =============================================================================
# 20. Explicit Right Grouping With Modulo
# =============================================================================

result_20: int = 20 * (7 % 6)

print(result_20)

# Parentheses force:
#
# 7 % 6
#
# to happen first.


# =============================================================================
# 21. Exponentiation Is Right Associative
# =============================================================================

result_21: int = 2**3**2

print(result_21)

# Exponentiation associates from right to left.
#
# Equivalent to:
#
# 2 ** (3 ** 2)
#
# which becomes:
#
# 2 ** 9
#
# Result:
#
# 512


# =============================================================================
# 22. Left Grouping of Exponentiation
# =============================================================================

result_22: int = (2**3) ** 2

print(result_22)

# Parentheses force:
#
# (2 ** 3) ** 2
#
# Result:
#
# 64
#
# This differs from:
#
# 2 ** 3 ** 2
#
# which is:
#
# 512


# =============================================================================
# 23. Three Exponents
# =============================================================================

result_23: int = 2**2**3

print(result_23)

# Equivalent to:
#
# 2 ** (2 ** 3)
#
# = 2 ** 8
#
# = 256


# =============================================================================
# 24. Four Exponents
# =============================================================================

result_24: int = 2**2**2**2

print(result_24)

# Equivalent grouping:
#
# 2 ** (2 ** (2 ** 2))
#
# The right side is evaluated first.


# =============================================================================
# 25. Explicit Left Grouping of Three Exponents
# =============================================================================

result_25: int = ((2**2) ** 2) ** 2

print(result_25)

# Parentheses override the default right associativity of **.


# =============================================================================
# 26. Exponentiation and Unary Minus
# =============================================================================

result_26: int = -2**2

print(result_26)

# Exponentiation binds more strongly than unary minus on its left.
#
# Equivalent to:
#
# -(2**2)
#
# Result:
#
# -4


# =============================================================================
# 27. Parentheses Around Negative Base
# =============================================================================

result_27: int = (-2) ** 2

print(result_27)

# Parentheses make -2 the base.
#
# Result:
#
# 4


# =============================================================================
# 28. Unary Operators Can Be Nested
# =============================================================================

result_28: int = --10

print(result_28)

# Unary operators are applied through the expression.
#
# Equivalent to:
#
# -(-10)
#
# Result:
#
# 10


# =============================================================================
# 29. Multiple Unary Operators
# =============================================================================

result_29: int = ~~~10

print(result_29)

# Unary bitwise NOT operators can be nested.
#
# Each ~ operates on the result of the next expression.


# =============================================================================
# 30. Comparison Operators Are Special
# =============================================================================

result_30: bool = 1 < 2 < 3

print(result_30)

# Python does not interpret this as:
#
# (1 < 2) < 3
#
# Instead, it is a chained comparison equivalent in behaviour to:
#
# (1 < 2) and (2 < 3)
#
# Both comparisons must be true.


# =============================================================================
# 31. Chained Comparison With Failure
# =============================================================================

result_31: bool = 1 < 2 > 5

print(result_31)

# This is interpreted as:
#
# (1 < 2) and (2 > 5)
#
# The second comparison is false.


# =============================================================================
# 32. Multiple Chained Comparisons
# =============================================================================

value_32: int = 50

result_32: bool = 10 < value_32 < 100

print(result_32)

# Equivalent conceptually to:
#
# (10 < value_32) and (value_32 < 100)


# =============================================================================
# 33. Comparison Operators Do Not Chain Like Arithmetic Operators
# =============================================================================

result_33: bool = 10 == 10 == 10

print(result_33)

# This is a chained comparison:
#
# (10 == 10) and (10 == 10)
#
# Result:
#
# True


# =============================================================================
# 34. Identity Comparison Chaining
# =============================================================================

value_34: None = None

result_34: bool = value_34 is None is not False

print(result_34)

# This is a chained comparison.
#
# It is conceptually equivalent to:
#
# (value_34 is None) and (None is not False)


# =============================================================================
# 35. Membership Comparison Chaining
# =============================================================================

numbers_35: list[int] = [
    1,
    2,
    3,
]

result_35: bool = 1 in numbers_35 and 3 in numbers_35

print(result_35)

# and is lower precedence than membership operators.
#
# Parentheses are useful when communicating complex conditions.


# =============================================================================
# 36. Boolean and Is Left Associative
# =============================================================================

result_36: bool = True and True and False

print(result_36)

# and expressions group from left to right.
#
# Equivalent grouping:
#
# (True and True) and False


# =============================================================================
# 37. Boolean or Is Left Associative
# =============================================================================

result_37: bool = False or False or True

print(result_37)

# Equivalent grouping:
#
# (False or False) or True


# =============================================================================
# 38. and Has Higher Precedence Than or
# =============================================================================

result_38: bool = True or False and False

print(result_38)

# This example primarily demonstrates precedence.
#
# Since and has higher precedence than or:
#
# True or (False and False)


# =============================================================================
# 39. Parentheses Override Boolean Grouping
# =============================================================================

result_39: bool = (True or False) and False

print(result_39)

# Parentheses force:
#
# (True or False)
#
# before:
#
# and False


# =============================================================================
# 40. Conditional Expressions Associate Right to Left
# =============================================================================

condition_40: bool = True
second_condition_40: bool = False

result_40: str = (
    "A"
    if condition_40
    else "B"
    if second_condition_40
    else "C"
)

print(result_40)

# Conditional expressions associate from right to left.
#
# Conceptually:
#
# "A" if condition_40 else (
#     "B" if second_condition_40 else "C"
# )


# =============================================================================
# 41. Explicit Conditional Grouping
# =============================================================================

result_41: str = (
    "A"
    if condition_40
    else (
        "B"
        if second_condition_40
        else "C"
    )
)

print(result_41)

# The parentheses make the right-to-left grouping obvious.


# =============================================================================
# 42. Assignment Statements Are Not Ordinary Expressions
# =============================================================================

first_value_42: int = 10
second_value_42: int = 20

print(first_value_42)

print(second_value_42)

# Python assignment statements such as:
#
# first_value_42 = 10
#
# should not be treated as ordinary left-to-right arithmetic operators.
#
# Assignment expressions using := are expressions and have their own
# precedence rules.


# =============================================================================
# 43. Assignment Expression With Arithmetic
# =============================================================================

if (number_43 := 10) + 5 > 12:
    print(number_43)

# The parentheses make the assignment expression boundary explicit.
#
# The resulting value of:
#
# number_43 := 10
#
# participates in the larger expression.


# =============================================================================
# 44. Left Associativity With String Concatenation
# =============================================================================

result_44: str = "Python" + " " + "Programming"

print(result_44)

# + associates from left to right.
#
# Equivalent grouping:
#
# ("Python" + " ") + "Programming"


# =============================================================================
# 45. String Concatenation With Parentheses
# =============================================================================

result_45: str = "Python" + (" " + "Programming")

print(result_45)

# The result is the same for strings, but the grouping is explicitly
# controlled.


# =============================================================================
# 46. Bitwise AND and OR
# =============================================================================

result_46: int = 6 | 4 & 3

print(result_46)

# This example involves both precedence and grouping.
#
# Bitwise AND has higher precedence than bitwise OR.
#
# Therefore:
#
# 6 | (4 & 3)
#
# Associativity applies after precedence has determined which operators
# belong to the same level.


# =============================================================================
# 47. Same-Level Bitwise OR Operators
# =============================================================================

result_47: int = 1 | 2 | 4

print(result_47)

# Bitwise OR is left associative.
#
# Equivalent grouping:
#
# (1 | 2) | 4


# =============================================================================
# 48. Same-Level Bitwise XOR Operators
# =============================================================================

result_48: int = 7 ^ 3 ^ 1

print(result_48)

# Bitwise XOR is left associative.
#
# Equivalent grouping:
#
# (7 ^ 3) ^ 1


# =============================================================================
# 49. Same-Level Bitwise AND Operators
# =============================================================================

result_49: int = 15 & 7 & 3

print(result_49)

# Bitwise AND is left associative.
#
# Equivalent grouping:
#
# (15 & 7) & 3


# =============================================================================
# 50. Practical Example Combining Associativity and Precedence
# =============================================================================

price: float = 100.0
quantity: int = 3
discount: float = 10.0
tax_rate: float = 0.18

subtotal: float = price * quantity

discounted_price: float = subtotal - discount

final_price: float = discounted_price * (1 + tax_rate)

print(final_price)

# This example is intentionally separated into meaningful steps.
#
# Instead of relying on a complicated expression such as:
#
# price * quantity - discount * (1 + tax_rate)
#
# the calculation is divided into stages.
#
# This makes precedence and associativity much easier to understand.


# =============================================================================
# Precedence Versus Associativity
# =============================================================================

"""
Precedence and associativity solve different problems.

Precedence:

    Determines which operator has priority.

Example:

    10 + 5 * 2

Multiplication has higher precedence than addition.

Therefore:

    10 + (5 * 2)


Associativity:

    Determines grouping when operators have the same precedence.

Example:

    100 - 20 - 10

Both - operators have the same precedence.

Subtraction is left associative.

Therefore:

    (100 - 20) - 10


Another example:

    100 / 10 * 2

/ and * have the same precedence.

Both are left associative.

Therefore:

    (100 / 10) * 2


Exception:

    2 ** 3 ** 2

Exponentiation is right associative.

Therefore:

    2 ** (3 ** 2)


A useful mental model is:

    STEP 1
        ↓
    Check precedence

    STEP 2
        ↓
    Group operators with equal precedence
    according to associativity

    STEP 3
        ↓
    Evaluate the resulting expression
"""


# =============================================================================
# Left Associative Operators
# =============================================================================

"""
Many Python operators are left associative.

Common examples include:

    +
    -
    *
    /
    //
    %
    <<
    >>
    &
    ^
    |

For example:

    a - b - c

means:

    (a - b) - c


And:

    a / b / c

means:

    (a / b) / c


And:

    a << b << c

is grouped from left to right.

The important point is that associativity applies between operators
that have the same precedence.
"""


# =============================================================================
# Right Associative Operators
# =============================================================================

"""
Important right-associative Python operators include:

    **

and the conditional expression:

    x if condition else y

For exponentiation:

    a ** b ** c

means:

    a ** (b ** c)

not:

    (a ** b) ** c


For nested conditional expressions:

    a if condition_1 else b if condition_2 else c

the grouping is effectively:

    a if condition_1 else (
        b if condition_2 else c
    )
"""


# =============================================================================
# Associativity Does Not Mean Evaluation Order
# =============================================================================

"""
Associativity describes how an expression is grouped.

It should not be confused with the complete runtime evaluation order
of every subexpression.

For example:

    a - b - c

is grouped as:

    (a - b) - c

This tells us the structure of the expression.

It does not mean that every aspect of Python's runtime evaluation should
be described simply as "left side executes first."

Associativity is primarily a parsing and grouping rule.
"""


# =============================================================================
# Parentheses Override Default Associativity
# =============================================================================

"""
Parentheses explicitly define grouping.

Without parentheses:

    100 - 20 - 10

Python uses left associativity:

    (100 - 20) - 10


With parentheses:

    100 - (20 - 10)

Python must use the explicitly requested grouping.

Therefore:

    70

and:

    90

are different results.

When an expression is difficult to understand, parentheses are often
the best way to communicate the intended grouping.
"""


# =============================================================================
# Associativity And Floating-Point Arithmetic
# =============================================================================

"""
Associativity can matter even when the mathematical operation appears
associative.

For example, floating-point addition can produce different results
depending on grouping because floating-point arithmetic has limited
precision.

Example:

    (a + b) + c

may not always produce exactly the same floating-point result as:

    a + (b + c)

Therefore, do not assume that mathematical associativity always means
computer arithmetic will produce bit-for-bit identical results.
"""


# =============================================================================
# Floating-Point Grouping Example
# =============================================================================

first_float: float = 1e16
second_float: float = -1e16
third_float: float = 1.0

left_grouped: float = (
    (first_float + second_float)
    + third_float
)

right_grouped: float = (
    first_float
    + (second_float + third_float)
)

print(left_grouped)

print(right_grouped)

# Floating-point rounding can make the grouping observable.
#
# This is an important practical reason to understand associativity
# rather than treating it as only a theoretical syntax rule.


# =============================================================================
# Common Mistake 1: Assuming Subtraction Is Right Associative
# =============================================================================

wrong_assumption_01: int = 100 - 20 - 10

print(wrong_assumption_01)

# A common mistaken interpretation is:
#
# 100 - (20 - 10)
#
# But Python uses:
#
# (100 - 20) - 10


# =============================================================================
# Common Mistake 2: Assuming Division Is Right Associative
# =============================================================================

wrong_assumption_02: float = 100 / 10 / 2

print(wrong_assumption_02)

# Python uses:
#
# (100 / 10) / 2
#
# not:
#
# 100 / (10 / 2)


# =============================================================================
# Common Mistake 3: Assuming Exponentiation Is Left Associative
# =============================================================================

correct_exponentiation: int = 2**3**2

print(correct_exponentiation)

# Python uses:
#
# 2 ** (3 ** 2)
#
# not:
#
# (2 ** 3) ** 2


# =============================================================================
# Common Mistake 4: Confusing Precedence With Associativity
# =============================================================================

result_50: int = 10 + 20 * 3 - 5

print(result_50)

# First precedence determines that * is evaluated at a higher level:
#
# 10 + (20 * 3) - 5
#
# Then + and - have equal precedence and associate left to right:
#
# (10 + (20 * 3)) - 5
#
# Result:
#
# 65


# =============================================================================
# Practical Guidelines
# =============================================================================

"""
Guidelines for using operator associativity:

1. Most binary operators are left associative.

2. Exponentiation is right associative.

3. Conditional expressions associate from right to left.

4. Comparisons are special because Python supports chained comparisons.

5. Precedence determines the operator hierarchy first.

6. Associativity determines grouping among operators at the same
   precedence level.

7. Parentheses override normal associativity.

8. Do not assume subtraction is right associative.

9. Do not assume division is right associative.

10. Do not assume exponentiation is left associative.

11. Use parentheses when grouping matters to the meaning of the code.

12. For complicated expressions, prefer intermediate variables.

13. Readability is more important than relying on a reader to remember
    obscure precedence and associativity rules.

14. Floating-point calculations can make grouping mathematically
    significant because of rounding.

15. Chained comparisons should be understood as Python's special
    comparison syntax rather than ordinary binary-operator chaining.
"""


# =============================================================================
# Quick Reference
# =============================================================================

"""
LEFT ASSOCIATIVE

Common operators:

    +
    -
    *
    /
    //
    %
    <<
    >>
    &
    ^
    |

Examples:

    a - b - c
    -> (a - b) - c

    a / b / c
    -> (a / b) / c

    a + b + c
    -> (a + b) + c


RIGHT ASSOCIATIVE

Important operators:

    **

Example:

    a ** b ** c
    -> a ** (b ** c)


CONDITIONAL EXPRESSION

Example:

    a if condition_1 else b if condition_2 else c

Grouping:

    a if condition_1 else (
        b if condition_2 else c
    )


SPECIAL CASE

Comparisons:

    a < b < c

are chained comparisons.

They are conceptually similar to:

    (a < b) and (b < c)

but Python handles chained comparisons directly.
"""


# =============================================================================
# Final Summary
# =============================================================================

"""
Operator associativity determines how operators with equal precedence
are grouped.

Core concept:

    PRECEDENCE
        ↓
    Which operator has priority?

    ASSOCIATIVITY
        ↓
    How are equal-precedence operators grouped?


Most common pattern:

    LEFT ASSOCIATIVE

    a - b - c

    ↓

    (a - b) - c


Important exception:

    RIGHT ASSOCIATIVE

    a ** b ** c

    ↓

    a ** (b ** c)


Parentheses override the default grouping:

    a - (b - c)

    (a - b) - c


The most important examples to remember are:

    100 - 20 - 10
    -> (100 - 20) - 10

    100 / 10 / 2
    -> (100 / 10) / 2

    2 ** 3 ** 2
    -> 2 ** (3 ** 2)

    1 < 2 < 3
    -> chained comparison

    True or False and False
    -> True or (False and False)

Remember:

    Precedence tells Python which operator level comes first.

    Associativity tells Python how operators at the same precedence
    level are grouped.

    Parentheses explicitly control grouping.

For maintainable code:

    If the grouping matters,
    make it obvious.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Associativity determines how equal-precedence operators are grouped.

✓ Most Python binary operators are left associative.

✓ Addition is left associative.

✓ Subtraction is left associative.

✓ Multiplication is left associative.

✓ Division is left associative.

✓ Floor division is left associative.

✓ Modulo is left associative.

✓ Bitwise AND, XOR, and OR are left associative.

✓ Exponentiation is right associative.

✓ Conditional expressions associate from right to left.

✓ Comparisons support special chained-comparison syntax.

✓ Precedence and associativity are different concepts.

✓ Precedence determines which operator level has priority.

✓ Associativity determines grouping within the same precedence level.

✓ Parentheses override default associativity.

✓ Subtraction should not be interpreted as right associative.

✓ Division should not be interpreted as right associative.

✓ Exponentiation should not be interpreted as left associative.

✓ Floating-point arithmetic can make grouping differences observable.

✓ Complex expressions should use parentheses or intermediate variables.

Core model:

    EXPRESSION
        ↓
    CHECK PRECEDENCE
        ↓
    GROUP SAME-PRECEDENCE OPERATORS
        ↓
    APPLY ASSOCIATIVITY
        ↓
    EVALUATE EXPRESSION


Most important examples:

    100 - 20 - 10
        ↓
    (100 - 20) - 10


    100 / 10 / 2
        ↓
    (100 / 10) / 2


    2 ** 3 ** 2
        ↓
    2 ** (3 ** 2)


    1 < 2 < 3
        ↓
    chained comparison


When in doubt:

    USE PARENTHESES.

Clear grouping is better than making the reader remember every
operator rule.
"""


# =============================================================================
# End of 14_operator_associativity.py
# =============================================================================