"""
==============================================================================
Python Functions
==============================================================================

File
----
04_keyword_arguments.py

Topic
-----
Keyword Arguments

Overview
--------
Keyword arguments are arguments supplied to a function by explicitly
specifying the parameter name while passing the value.

Unlike positional arguments, keyword arguments are associated with parameters
by name rather than by position.

Therefore, the order of keyword arguments does not matter.

In normal mode, a function can generally be called using positional
arguments, keyword arguments, or a combination of both.

Python also provides strict parameter syntax using `*` to make certain
parameters keyword-only.

This file focuses on keyword argument behaviour in both normal mode and
strict mode.

Topics covered:

    - What is a keyword argument?
    - Explicit parameter assignment
    - Keyword argument association
    - Keyword argument order
    - Keyword arguments with multiple parameters
    - Normal argument-passing flexibility
    - Mixing positional and keyword arguments
    - Keyword arguments and parameter names
    - The `*` syntax
    - Keyword-only parameters
    - Strict keyword argument passing
    - Errors caused by violating keyword-only rules
    - Combining positional-only and keyword-only parameters
"""


# =============================================================================
# 01. Basic Keyword Argument
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
    student_name="Alex"
)


# The value "Alex" is explicitly assigned to the parameter:
#
#     student_name
#
# Therefore:
#
#     student_name="Alex"
#
# is a keyword argument.


# =============================================================================
# 02. Keyword Argument Explicitly Identifies the Parameter
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
    person_name="Shreyas",
    person_age=30,
)


# The caller explicitly identifies the target parameters:
#
#     person_name="Shreyas"
#     person_age=30
#
# Python does not need to infer these associations from position.


# =============================================================================
# 03. Keyword Arguments Are Matched By Name
# =============================================================================

def display_values(
    first_value: str,
    second_value: int,
    third_value: float,
) -> None:
    """
    Display three supplied values.
    """
    print(
        f"first_value->{first_value}"
    )

    print(
        f"second_value->{second_value}"
    )

    print(
        f"third_value->{third_value}"
    )


display_values(
    first_value="Python",
    second_value=30,
    third_value=1996.0,
)


# The association is explicitly defined:
#
#     first_value="Python"
#         ↓
#     first_value
#
#     second_value=30
#         ↓
#     second_value
#
#     third_value=1996.0
#         ↓
#     third_value


# =============================================================================
# 04. Keyword Argument Order Does Not Matter
# =============================================================================

display_values(
    third_value=1996.0,
    first_value="Python",
    second_value=30,
)


# The order has changed.
#
# However, the result is logically the same because each argument
# explicitly identifies its parameter.


# =============================================================================
# 05. Keyword Arguments Can Be Rearranged Freely
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


first_profile: str = create_profile(
    name="shreyas",
    age=30,
    birth_year=1996.0,
)

second_profile: str = create_profile(
    birth_year=1996.0,
    name="shreyas",
    age=30,
)

third_profile: str = create_profile(
    age=30,
    birth_year=1996.0,
    name="shreyas",
)

print(
    first_profile
)

print(
    second_profile
)

print(
    third_profile
)


# All three calls provide the same values.
#
# The order does not matter because the parameter names explicitly
# identify where each value belongs.


# =============================================================================
# 06. Keyword Arguments Versus Positional Arguments
# =============================================================================

print(
    create_profile(
        "shreyas",
        30,
        1996.0,
    )
)


print(
    create_profile(
        name="shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# First call:
#
#     positional arguments
#
# The mapping depends on position.
#
#
# Second call:
#
#     keyword arguments
#
# The mapping depends on parameter names.


# =============================================================================
# 07. Normal Mode Allows Both Styles
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


positional_total: float = calculate_total(
    1500.0,
    2,
)

keyword_total: float = calculate_total(
    item_price=1500.0,
    quantity=2,
)

print(
    positional_total
)

print(
    keyword_total
)


# In normal mode, the caller can choose:
#
#     positional passing
#
# or:
#
#     keyword passing


# =============================================================================
# 08. Normal Mode Allows Mixed Argument Passing
# =============================================================================

mixed_total: float = calculate_total(
    1500.0,
    quantity=2,
)

print(
    mixed_total
)


# The first argument is positional:
#
#     1500.0 -> item_price
#
# The second argument is keyword-based:
#
#     quantity=2
#
# This is valid in normal mode.


# =============================================================================
# 09. Positional Arguments Must Come Before Keyword Arguments
# =============================================================================

def calculate_shipping_cost(
    item_cost: float,
    shipping_cost: float,
    tax_cost: float,
) -> float:
    """
    Calculate total cost.
    """
    return (
        item_cost
        + shipping_cost
        + tax_cost
    )


shipping_total: float = calculate_shipping_cost(
    1000.0,
    shipping_cost=100.0,
    tax_cost=180.0,
)

print(
    shipping_total
)


# This follows the normal mixed-argument rule:
#
#     positional
#          ↓
#     keyword
#          ↓
#     keyword


# =============================================================================
# 10. Invalid Positional Argument After Keyword Argument
# =============================================================================

# The following call is intentionally not executed:
#
# calculate_shipping_cost(
#     item_cost=1000.0,
#     100.0,
#     tax_cost=180.0,
# )
#
# A positional argument cannot appear after a keyword argument.


# =============================================================================
# 11. Keyword Arguments With Variables
# =============================================================================

item_price_value: float = 1500.0
quantity_value: int = 2

variable_total: float = calculate_total(
    item_price=item_price_value,
    quantity=quantity_value,
)

print(
    variable_total
)


# The values come from variables.
#
# The parameter names are still explicitly supplied.


# =============================================================================
# 12. Keyword Arguments With Expressions
# =============================================================================

expression_total: float = calculate_total(
    item_price=1000.0 + 500.0,
    quantity=1 + 1,
)

print(
    expression_total
)


# The expressions are evaluated and their results are associated
# with the explicitly named parameters.


# =============================================================================
# 13. Keyword Arguments With Function Results
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


function_result_total: float = calculate_total(
    quantity=get_quantity(),
    item_price=get_price(),
)

print(
    function_result_total
)


# Function results can be supplied as keyword argument values.
#
# The parameter names determine where those results are assigned.


# =============================================================================
# 14. Keyword Arguments With Different Data Types
# =============================================================================

def configure_feature(
    feature_name: str,
    feature_enabled: bool,
    retry_count: int,
) -> None:
    """
    Display feature configuration.
    """
    print(
        f"Feature: {feature_name}"
    )

    print(
        f"Enabled: {feature_enabled!r}"
    )

    print(
        f"Retry count: {retry_count}"
    )


configure_feature(
    retry_count=3,
    feature_name="Logging",
    feature_enabled=True,
)


# The order is irrelevant.
#
# The parameter names determine the association.


# =============================================================================
# 15. Keyword Argument Names Must Match Parameters
# =============================================================================

def display_name(
    first_name: str,
    last_name: str,
) -> None:
    """
    Display a person's full name.
    """
    print(
        f"{first_name} {last_name}"
    )


display_name(
    first_name="Shreyas",
    last_name="Global",
)


# Valid keyword names:
#
#     first_name
#     last_name
#
# These names correspond directly to the function parameters.


# =============================================================================
# 16. Unexpected Keyword Argument
# =============================================================================

# The following call is intentionally not executed:
#
# display_name(
#     first_name="Shreyas",
#     surname="Global",
# )
#
# `surname` is not a parameter of display_name().
#
# Therefore Python raises a TypeError.


# =============================================================================
# 17. Keyword Argument Names Are Not Determined By Data Type
# =============================================================================

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
        key_wrd_arg_2=1996.0,
        key_wrd_arg=30,
    )
)


# Here:
#
#     key_wrd_arg_2=1996.0
#
# explicitly identifies key_wrd_arg_2.
#
# The fact that 1996.0 is a float is not what makes the association.
#
# The keyword name:
#
#     key_wrd_arg_2
#
# determines the association.


# =============================================================================
# 18. Keyword Arguments Remove Positional Order Dependency
# =============================================================================

print(
    check(
        "shreyas",
        key_wrd_arg=30,
        key_wrd_arg_2=1996.0,
    )
)


print(
    check(
        "shreyas",
        key_wrd_arg_2=1996.0,
        key_wrd_arg=30,
    )
)


# Both calls produce the same logical parameter association.
#
# The keyword arguments can be reordered without changing their meaning.


# =============================================================================
# 19. Strict Mode: Keyword-Only Parameters
# =============================================================================

def create_strict_profile(
    name: str,
    *,
    age: int,
    birth_year: float,
) -> str:
    """
    Create a profile where age and birth_year are keyword-only.
    """
    return (
        f"name->{name}; "
        f"age->{age}; "
        f"birth_year->{birth_year}"
    )


print(
    create_strict_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# The `*` creates a boundary.
#
# Parameters after `*` become keyword-only.
#
# Therefore:
#
#     name
#         ↓
#     normal parameter
#
#     age
#         ↓
#     keyword-only
#
#     birth_year
#         ↓
#     keyword-only


# =============================================================================
# 20. The Meaning of *
# =============================================================================

"""
Consider:

    def create_strict_profile(
        name: str,
        *,
        age: int,
        birth_year: float,
    ) -> str:
        ...


The `*` means:

    Parameters after *
        ↓
    keyword-only


Therefore:

    age
        ↓
    must be supplied using a keyword

    birth_year
        ↓
    must be supplied using a keyword


The following is valid:

    create_strict_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )


The following is invalid:

    create_strict_profile(
        "shreyas",
        30,
        1996.0,
    )


because age and birth_year are keyword-only.
"""


# =============================================================================
# 21. Strict Keyword-Only Parameters Must Use Keywords
# =============================================================================

print(
    create_strict_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )
)


# This is valid because both keyword-only parameters are explicitly named.


# =============================================================================
# 22. Strict Keyword-Only Violation
# =============================================================================

# The following call is intentionally not executed:
#
# create_strict_profile(
#     "shreyas",
#     30,
#     1996.0,
# )
#
# This raises a TypeError.
#
# The reason is:
#
#     age
#         ↓
#     received positionally
#
# but:
#
#     age
#         ↓
#     is keyword-only
#
#
# Likewise:
#
#     birth_year
#
# is also keyword-only.


# =============================================================================
# 23. Keyword-Only Parameters Can Be Reordered
# =============================================================================

print(
    create_strict_profile(
        "shreyas",
        birth_year=1996.0,
        age=30,
    )
)


# Even though age and birth_year are keyword-only, their order does
# not matter.
#
# The keyword names explicitly identify the parameters.


# =============================================================================
# 24. Strict Mode Can Force Important Parameters To Be Explicit
# =============================================================================

def calculate_discount(
    product_price: float,
    *,
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


# The function designer has made discount_percentage keyword-only.
#
# This makes the call more explicit:
#
#     discount_percentage=10.0
#
# instead of simply:
#
#     10.0


# =============================================================================
# 25. Why Keyword-Only Parameters Can Be Useful
# =============================================================================

def configure_connection(
    host: str,
    *,
    timeout: int,
    secure: bool,
) -> None:
    """
    Display connection configuration.
    """
    print(
        f"Host: {host}"
    )

    print(
        f"Timeout: {timeout}"
    )

    print(
        f"Secure: {secure!r}"
    )


configure_connection(
    "database.example.com",
    timeout=30,
    secure=True,
)


# Without the keyword-only restriction, a caller might write:
#
#     configure_connection(
#         "database.example.com",
#         30,
#         True,
#     )
#
# The function designer may consider the keyword names clearer:
#
#     timeout=30
#     secure=True
#
# Strict mode allows the designer to enforce that style.


# =============================================================================
# 26. Keyword-Only Parameters Can Be Mixed With Positional Parameters
# =============================================================================

def create_user(
    user_name: str,
    user_id: int,
    *,
    active: bool,
    role: str,
) -> None:
    """
    Display user configuration.
    """
    print(
        f"Name: {user_name}"
    )

    print(
        f"ID: {user_id}"
    )

    print(
        f"Active: {active!r}"
    )

    print(
        f"Role: {role}"
    )


create_user(
    "Shreyas",
    101,
    active=True,
    role="Data Engineer",
)


# Here:
#
#     user_name
#     user_id
#
# can be positional.
#
# But:
#
#     active
#     role
#
# must be keyword arguments.


# =============================================================================
# 27. Keyword-Only Parameters Are Still Parameters
# =============================================================================

"""
The `*` does not create a different kind of parameter.

It creates a restriction on how the parameter can be supplied.

For example:

    def example(
        value: int,
        *,
        option: bool,
    ) -> None:
        ...


Both are normal function parameters:

    value
    option

But their calling rules differ:

    value
        -> can be supplied positionally

    option
        -> must be supplied using a keyword
"""


# =============================================================================
# 28. Combining Positional-Only and Keyword-Only Parameters
# =============================================================================

def strict_function(
    positional_value: str,
    /,
    *,
    keyword_value: int,
    keyword_value_2: float,
) -> str:
    """
    Demonstrate both positional-only and keyword-only parameters.
    """
    return (
        f"positional_value->{positional_value}; "
        f"keyword_value->{keyword_value}; "
        f"keyword_value_2->{keyword_value_2}"
    )


print(
    strict_function(
        "shreyas",
        keyword_value=30,
        keyword_value_2=1996.0,
    )
)


# This function establishes a strict calling convention:
#
#     positional_value
#         ↓
#     MUST be positional
#
#     keyword_value
#         ↓
#     MUST be keyword
#
#     keyword_value_2
#         ↓
#     MUST be keyword


# =============================================================================
# 29. Strict Function Rejects All-Positional Passing
# =============================================================================

# The following call is intentionally not executed:
#
# strict_function(
#     "shreyas",
#     30,
#     1996.0,
# )
#
# This raises a TypeError.
#
# Why?
#
#     positional_value
#         -> positional
#         -> valid
#
#     keyword_value
#         -> positional
#         -> INVALID
#
#     keyword_value_2
#         -> positional
#         -> INVALID
#
# The `*` prevents positional passing for parameters after it.


# =============================================================================
# 30. Strict Function Rejects Keyword Passing for Positional-Only Parameter
# =============================================================================

# The following call is intentionally not executed:
#
# strict_function(
#     positional_value="shreyas",
#     keyword_value=30,
#     keyword_value_2=1996.0,
# )
#
# This raises a TypeError.
#
# Why?
#
#     positional_value
#         ↓
#     appears before /
#         ↓
#     positional-only
#
# Therefore it cannot be supplied using a keyword.


# =============================================================================
# 31. Strict Calling Convention
# =============================================================================

"""
The following function:

    def strict_function(
        positional_value: str,
        /,
        *,
        keyword_value: int,
        keyword_value_2: float,
    ) -> str:
        ...


creates the following calling convention:


             positional-only
                    ↓
        positional_value
                    |
                    |
                    /
--------------------|--------------------
                    *
--------------------|--------------------
                    |
                    |
             keyword-only
                    ↓
             keyword_value
             keyword_value_2


Valid:

    strict_function(
        "shreyas",
        keyword_value=30,
        keyword_value_2=1996.0,
    )


Invalid:

    strict_function(
        "shreyas",
        30,
        1996.0,
    )


Invalid:

    strict_function(
        positional_value="shreyas",
        keyword_value=30,
        keyword_value_2=1996.0,
    )
"""


# =============================================================================
# 32. Normal Mode Versus Strict Mode
# =============================================================================

"""
NORMAL MODE
-----------

The function designer has not imposed positional-only or keyword-only
restrictions.

Example:

    def normal_function(
        value: int,
        option: bool,
    ) -> None:
        ...


The caller can use:

    normal_function(
        10,
        True,
    )


or:

    normal_function(
        value=10,
        option=True,
    )


or:

    normal_function(
        10,
        option=True,
    )


The caller has flexibility.


STRICT MODE
-----------

The function designer can impose restrictions using `/` and `*`.

Example:

    def strict_function(
        value: int,
        /,
        *,
        option: bool,
    ) -> None:
        ...


Now:

    value
        -> must be positional

    option
        -> must be keyword


The function designer has control over the intended calling style.
"""


# =============================================================================
# 33. Keyword Argument Core Model
# =============================================================================

"""
Keyword argument:

    A value supplied by explicitly specifying the parameter name.

Example:

    check(
        psn_arg="shreyas",
        key_wrd_arg=30,
        key_wrd_arg_2=1996.0,
    )


The mapping is explicit:

    psn_arg="shreyas"
        ↓
    psn_arg

    key_wrd_arg=30
        ↓
    key_wrd_arg

    key_wrd_arg_2=1996.0
        ↓
    key_wrd_arg_2


Core rule:

    PARAMETER NAME
          ↓
       PARAMETER


Therefore:

    keyword argument order does not matter.
"""


# =============================================================================
# 34. Keyword Arguments Summary
# =============================================================================

"""
Keyword arguments:

    - Explicitly specify the parameter name.
    - Are associated with parameters by name.
    - Do not depend on argument order.
    - Can be supplied in any order.
    - Can be mixed with positional arguments.
    - Must come after positional arguments when mixed normally.
    - Must use valid parameter names.
    - Can receive literals, variables, expressions, and function results.

Normal mode:

    caller has flexibility.


Strict mode:

    `*` makes parameters after it keyword-only.


Example:

    def create_profile(
        name: str,
        *,
        age: int,
        birth_year: float,
    ) -> str:
        ...


Valid:

    create_profile(
        "shreyas",
        age=30,
        birth_year=1996.0,
    )


Also valid:

    create_profile(
        "shreyas",
        birth_year=1996.0,
        age=30,
    )


Invalid:

    create_profile(
        "shreyas",
        30,
        1996.0,
    )


because age and birth_year are keyword-only.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A keyword argument explicitly specifies the parameter name.

✓ Keyword arguments are associated with parameters by name rather than
  by position.

✓ Keyword argument order does not matter.

✓ The parameter name determines where the value goes.

✓ Data type does not determine keyword argument association either.

✓ In normal mode, the caller can generally choose positional arguments,
  keyword arguments, or a combination of both.

✓ When positional and keyword arguments are mixed, positional arguments
  must come first.

✓ The `*` syntax creates keyword-only parameters.

✓ Parameters after `*` must be supplied using keywords.

✓ Passing a keyword-only parameter positionally raises a TypeError.

✓ Keyword-only parameters can be reordered because their names identify
  their target parameters.

✓ Keyword-only parameters are useful when the function designer wants
  important or potentially ambiguous arguments to be explicitly named.

✓ `/` can create positional-only parameters.

✓ `*` can create keyword-only parameters.

✓ `/` and `*` can be used together to create a strict calling convention.

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
    function designer controls usage
          ↓
          /
          ↓
    positional-only
          ↓
          *
          ↓
    keyword-only
"""