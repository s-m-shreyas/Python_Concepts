"""
==============================================================================
Python Functions
==============================================================================

File
----
03_positional_arguments.py

Topic
-----
Positional Arguments

Overview
--------
Positional arguments are arguments supplied to a function without explicitly
assigning parameter names during the function call.

Python associates positional arguments with parameters according to their
position in the function call.

Therefore, when positional arguments are used, the order of the arguments
must be maintained.

In normal mode, a function can generally be called using positional
arguments, keyword arguments, or a combination of both.

Python also provides strict parameter syntax using `/` to make certain
parameters positional-only.

This file focuses on positional argument behaviour in both normal mode and
strict mode.

Topics covered:

    - What is a positional argument?
    - Normal positional argument passing
    - Positional argument order
    - Positional arguments with multiple parameters
    - Positional arguments and data types
    - Type annotations do not determine positional association
    - Positional arguments versus keyword arguments
    - Normal argument-passing flexibility
    - Positional and keyword arguments together
    - Positional-only parameters
    - The `/` syntax
    - Strict positional argument passing
    - Errors caused by violating positional-only rules
"""


# =============================================================================
# 01. Basic Positional Argument
# =============================================================================

def display_student_name(
    student_name: str,
) -> None:
    """
    Display a supplied student name.
    """
    print(
        student_name
    )


display_student_name(
    "Alex"
)


# "Alex" is supplied without explicitly assigning a parameter name.
#
# Python associates the value with the first parameter:
#
#     student_name
#
# This is a positional argument.


# =============================================================================
# 02. Positional Argument Means Position Determines Association
# =============================================================================

def display_person_information(
    person_name: str,
    person_age: int,
) -> None:
    """
    Display a person's information.
    """
    print(
        f"Name: {person_name}"
    )

    print(
        f"Age: {person_age}"
    )


display_person_information(
    "Shreyas",
    30,
)


# Python associates the arguments according to their position:
#
#     "Shreyas" -> person_name
#     30        -> person_age
#
# No parameter names were explicitly supplied.


# =============================================================================
# 03. Positional Arguments Are Matched From Left to Right
# =============================================================================

def display_values(
    first_value: str,
    second_value: str,
    third_value: str,
) -> None:
    """
    Display three supplied values.
    """
    print(
        first_value
    )

    print(
        second_value
    )

    print(
        third_value
    )


display_values(
    "First",
    "Second",
    "Third",
)


# The mapping is:
#
#     first argument  -> first parameter
#     second argument -> second parameter
#     third argument  -> third parameter


# =============================================================================
# 04. Positional Argument Order Must Be Maintained
# =============================================================================

def create_coordinate(
    horizontal_position: int,
    vertical_position: int,
) -> tuple[int, int]:
    """
    Create a two-dimensional coordinate.
    """
    return (
        horizontal_position,
        vertical_position,
    )


first_coordinate: tuple[int, int] = create_coordinate(
    10,
    20,
)

second_coordinate: tuple[int, int] = create_coordinate(
    20,
    10,
)

print(
    first_coordinate
)

print(
    second_coordinate
)


# The first call means:
#
#     10 -> horizontal_position
#     20 -> vertical_position
#
# The second call means:
#
#     20 -> horizontal_position
#     10 -> vertical_position
#
# The values are the same, but their positions are different.
#
# Therefore, the result is different.


# =============================================================================
# 05. Positional Arguments With Different Data Types
# =============================================================================

def display_product(
    product_name: str,
    product_price: float,
    product_available: bool,
) -> None:
    """
    Display product information.
    """
    print(
        f"Product: {product_name}"
    )

    print(
        f"Price: {product_price!r}"
    )

    print(
        f"Available: {product_available!r}"
    )


display_product(
    "Keyboard",
    1499.50,
    True,
)


# The mapping is based on position:
#
#     "Keyboard" -> product_name
#     1499.50    -> product_price
#     True       -> product_available
#
# Python does not search for a parameter based on the data type
# of the supplied argument.


# =============================================================================
# 06. Type Annotations Do Not Determine Positional Association
# =============================================================================

def check_values(
    first_value: str,
    second_value: int,
    third_value: float,
) -> str:
    """
    Return the supplied values.
    """
    return (
        f"first_value->{first_value}; "
        f"second_value->{second_value}; "
        f"third_value->{third_value}"
    )


print(
    check_values(
        "shreyas",
        30,
        1996.0,
    )
)


# The parameters are annotated as:
#
#     first_value  -> str
#     second_value -> int
#     third_value  -> float
#
# The positional mapping is:
#
#     "shreyas" -> first_value
#     30        -> second_value
#     1996.0    -> third_value
#
# The association is determined by position.
#
# The annotations do not cause Python to search for a parameter
# whose annotation matches the supplied value.


# =============================================================================
# 07. Same or Similar Data Types Do Not Change Positional Rules
# =============================================================================

# mypy: disable-error-code="arg-type"

def check(
    psn_arg: str,
    key_wrd_arg: int,
    key_wrd_arg_2: float,
) -> str:
    """
    Return values supplied to the function.
    """
    return (
        f"psn_arg->{psn_arg}; "
        f"key_wrd_arg->{key_wrd_arg}; "
        f"key_wrd_arg_2->{key_wrd_arg_2}"
    )


print(
    check(
        "shreyas",
        30,
        1996.0,
    )
)


print(
    check(
        "shreyas",
        1996.0, # pyright: ignore[reportArgumentType]
        30,
    )
)


# The second call is intentionally important:
#
#     check(
#         "shreyas",
#         1996.0,
#         30,
#     )
#
# Python does NOT think:
#
#     1996.0 -> key_wrd_arg_2
#     30      -> key_wrd_arg
#
# Instead, it follows position:
#
#     "shreyas" -> psn_arg
#     1996.0    -> key_wrd_arg
#     30        -> key_wrd_arg_2
#
# A static type checker may report type mismatches here, but the
# positional association itself remains unchanged.


# =============================================================================
# 08. Positional Arguments Can Be Supplied Using Variables
# =============================================================================

def calculate_total(
    item_price: float,
    quantity: int,
) -> float:
    """
    Calculate the total price.
    """
    return (
        item_price
        * quantity
    )


item_price_value: float = 1500.0
quantity_value: int = 2

total_result: float = calculate_total(
    item_price_value,
    quantity_value,
)

print(
    total_result
)


# Variables can be supplied as positional arguments.
#
# Their positions determine which parameters receive their values.


# =============================================================================
# 09. Positional Arguments Can Be Expressions
# =============================================================================

expression_result: float = calculate_total(
    1000.0 + 500.0,
    1 + 1,
)

print(
    expression_result
)


# The expressions are evaluated first.
#
# Their resulting values are then supplied according to position.


# =============================================================================
# 10. Positional Arguments Can Be Function Results
# =============================================================================

def get_price() -> float:
    """
    Return a product price.
    """
    return 1500.0


def get_quantity() -> int:
    """
    Return a product quantity.
    """
    return 2


function_result: float = calculate_total(
    get_price(),
    get_quantity(),
)

print(
    function_result
)


# Function results can also be supplied positionally.


# =============================================================================
# 11. Normal Mode Allows Positional Arguments
# =============================================================================

def create_profile(
    name: str,
    age: int,
    birth_year: float,
) -> str:
    """
    Create a simple profile string.
    """
    return (
        f"name->{name}; "
        f"age->{age}; "
        f"birth_year->{birth_year}"
    )


print(
    create_profile(
        "shreyas",
        30,
        1996.0,
    )
)


# In normal mode, positional argument passing is allowed.
#
# The caller does not need to explicitly name the parameters.


# =============================================================================
# 12. Normal Mode Also Allows Keyword Arguments
# =============================================================================

print(
    create_profile(
        name="shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# The same function can also be called using keyword arguments.
#
# Here the caller explicitly identifies each parameter.


# =============================================================================
# 13. Keyword Argument Order Is Not Important
# =============================================================================

print(
    create_profile(
        birth_year=1996.0,
        name="shreyas",
        age=30,
    )
)


# The keyword arguments can be rearranged.
#
# Python identifies the target parameter from the keyword name.


# =============================================================================
# 14. Normal Mode Allows Mixing Positional and Keyword Arguments
# =============================================================================

print(
    create_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# In normal mode, positional and keyword arguments can be used together.
#
# The rule is:
#
#     positional arguments
#             ↓
#     must come before
#             ↓
#     keyword arguments


# =============================================================================
# 15. Invalid Mixing Order
# =============================================================================

# The following call is intentionally not executed:
#
# create_profile(
#     name="shreyas",
#     30,
#     birth_year=1996.0,
# )
#
# A positional argument cannot appear after a keyword argument.


# =============================================================================
# 16. Normal Mode Gives the Caller Flexibility
# =============================================================================

"""
In normal mode, the function designer has not restricted the way
arguments must be supplied.

For example:

    create_profile(
        "shreyas",
        30,
        1996.0,
    )


or:

    create_profile(
        name="shreyas",
        age=30,
        birth_year=1996.0,
    )


or:

    create_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )


All three forms are allowed.

The important rules are:

    Positional arguments
        -> order matters

    Keyword arguments
        -> order does not matter

    Mixed arguments
        -> positional arguments must come first
"""


# =============================================================================
# 17. Strict Mode: Positional-Only Parameters
# =============================================================================

def create_strict_profile(
    name: str,
    /,
    age: int,
    birth_year: float,
) -> str:
    """
    Create a profile where name must be positional.
    """
    return (
        f"name->{name}; "
        f"age->{age}; "
        f"birth_year->{birth_year}"
    )


print(
    create_strict_profile(
        "shreyas",
        30,
        1996.0,
    )
)


# The `/` marks the end of positional-only parameters.
#
# Therefore:
#
#     name
#
# must be supplied positionally.


# =============================================================================
# 18. The Meaning of /
# =============================================================================

"""
Consider:

    def create_strict_profile(
        name: str,
        /,
        age: int,
        birth_year: float,
    ) -> str:
        ...


The `/` means:

    Parameters before /
        ↓
    positional-only


Therefore:

    name
        ↓
    must be supplied positionally.


The following is valid:

    create_strict_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )


The following is invalid:

    create_strict_profile(
        name="shreyas",
        age=30,
        birth_year=1996.0,
    )


The second call violates the positional-only rule.
"""


# =============================================================================
# 19. Strict Mode Prevents Keyword Passing for Positional-Only Parameters
# =============================================================================

print(
    create_strict_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# This is valid because:
#
#     "shreyas" -> name
#
# is supplied positionally.


# The following call is intentionally not executed:
#
# create_strict_profile(
#     name="shreyas",
#     age=30,
#     birth_year=1996.0,
# )
#
# Python raises a TypeError because `name` is positional-only.


# =============================================================================
# 20. Strict Mode Is Used to Enforce Intended Usage
# =============================================================================

def calculate_power(
    base_value: int,
    /,
    exponent_value: int,
) -> int:
    """
    Calculate a power where base_value is positional-only.
    """
    return (
        base_value
        ** exponent_value
    )


valid_power_result: int = calculate_power(
    2,
    exponent_value=5,
)

print(
    valid_power_result
)


# The function designer has intentionally made base_value positional-only.
#
# This communicates that callers should supply the base value by position.


# =============================================================================
# 21. Strict Positional-Only Violation
# =============================================================================

# The following call is intentionally not executed:
#
# calculate_power(
#     base_value=2,
#     exponent_value=5,
# )
#
# This raises a TypeError because base_value is positional-only.


# =============================================================================
# 22. Normal Mode Versus Strict Mode
# =============================================================================

def normal_function(
    value: int,
) -> int:
    """
    Accept a value normally.
    """
    return value


def strict_function(
    value: int,
    /,
) -> int:
    """
    Accept a positional-only value.
    """
    return value


normal_result: int = normal_function(
    value=10,
)

strict_result: int = strict_function(
    10,
)

print(
    normal_result
)

print(
    strict_result
)


# Normal function:
#
#     normal_function(
#         value=10,
#     )
#
# is valid.
#
#
# Strict function:
#
#     strict_function(
#         10,
#     )
#
# is valid.
#
# But:
#
#     strict_function(
#         value=10,
#     )
#
# is invalid because value is positional-only.


# =============================================================================
# 23. Positional-Only Parameters Can Be Combined With Normal Parameters
# =============================================================================

def calculate_discount(
    product_price: float,
    /,
    discount_percentage: float,
) -> float:
    """
    Calculate a discounted price.
    """
    discount_amount: float = (
        product_price
        * discount_percentage
        / 100
    )

    return (
        product_price
        - discount_amount
    )


discounted_price: float = calculate_discount(
    1000.0,
    discount_percentage=10.0,
)

print(
    discounted_price
)


# Here:
#
#     product_price
#         ↓
#     positional-only
#
#     discount_percentage
#         ↓
#     normal parameter
#
# Therefore the first argument must be positional, while the second
# can be supplied positionally or by keyword.


# =============================================================================
# 24. Strict Mode Does Not Change the Meaning of Positional Arguments
# =============================================================================

"""
Strict mode does not create a new type of positional argument.

A positional argument still means:

    value supplied according to position.

The difference is that the function designer has now enforced the rule:

    "This parameter cannot be supplied using a keyword."


Normal mode:

    caller has flexibility


Strict mode:

    function designer restricts how the caller can use the parameter


Therefore `/` is a parameter-definition rule, not a different
argument-passing mechanism.
"""


# =============================================================================
# 25. Positional Argument Core Model
# =============================================================================

"""
Positional argument:

    A value supplied without explicitly assigning a parameter name.

Example:

    check(
        "shreyas",
        30,
        1996.0,
    )


Mapping:

    "shreyas" -> first parameter
    30        -> second parameter
    1996.0    -> third parameter


Core rule:

    POSITION
       ↓
    PARAMETER


Not:

    DATA TYPE
       ↓
    PARAMETER


Normal mode:

    Caller can generally choose between positional and keyword
    argument passing.


Strict mode:

    The function designer can use `/` to make parameters
    positional-only.


Example:

    def check_strict(
        psn_arg: str,
        /,
        key_wrd_arg: int,
        key_wrd_arg_2: float,
    ) -> str:
        ...


Here:

    psn_arg
        ↓
    must be positional
"""


# =============================================================================
# 26. Positional Arguments Summary
# =============================================================================

"""
Positional arguments:

    - Are supplied without explicitly naming parameters.
    - Are matched according to position.
    - Are matched from left to right.
    - Require the caller to maintain the correct order.
    - Are not matched according to data type.
    - Can be literals, variables, expressions, or function results.

Normal mode:

    - Allows positional arguments.
    - Allows keyword arguments.
    - Allows positional and keyword arguments together.
    - Positional arguments must come before keyword arguments.
    - Keyword argument order is not important.

Strict mode:

    - Uses `/` in the function definition.
    - Makes parameters before `/` positional-only.
    - Prevents those parameters from being supplied using keywords.
    - Raises a TypeError when the positional-only rule is violated.

Example:

    def check(
        psn_arg: str,
        /,
        key_wrd_arg: int,
        key_wrd_arg_2: float,
    ) -> str:
        ...


    check(
        "shreyas",
        key_wrd_arg=30,
        key_wrd_arg_2=1996.0,
    )


Here:

    psn_arg
        -> positional-only

    key_wrd_arg
        -> normal parameter

    key_wrd_arg_2
        -> normal parameter
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A positional argument is supplied without explicitly assigning a
  parameter name.

✓ Positional arguments are associated with parameters by position.

✓ Positional arguments are matched from left to right.

✓ Therefore, positional argument order matters.

✓ Python does not select a parameter based on the data type of an
  argument.

✓ Type annotations describe intended types but do not determine
  positional argument association.

✓ In normal mode, callers generally have flexibility to use positional
  arguments, keyword arguments, or both.

✓ When positional and keyword arguments are mixed, positional arguments
  must come first.

✓ Keyword arguments are associated by parameter name, so their order
  is not important.

✓ The `/` syntax creates positional-only parameters.

✓ Parameters before `/` must be supplied positionally.

✓ Supplying a positional-only parameter using a keyword raises a
  TypeError.

✓ Strict positional-only behaviour allows the function designer to
  enforce the intended way a parameter should be used.

Core idea:

    Normal mode
          ↓
    caller has flexibility
          ↓
    positional OR keyword
          ↓
    positional → order matters
    keyword    → order does not matter


    Strict mode
          ↓
    function designer restricts usage
          ↓
          /
          ↓
    parameters before /
          ↓
    positional-only
"""