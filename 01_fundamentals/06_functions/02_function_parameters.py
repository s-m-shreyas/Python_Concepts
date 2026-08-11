"""
==============================================================================
Python Functions
==============================================================================

File
----
02_function_parameters.py

Topic
-----
Function Parameters

Overview
--------
Parameters allow a function to receive information from its caller.

A parameter is a variable defined in a function declaration.

When the function is called, the caller can provide an argument that is
associated with that parameter.

This file focuses on the fundamentals of parameters without going deeply
into specific argument-passing mechanisms.

Topics covered:

    - What is a parameter?
    - Single parameters
    - Multiple parameters
    - Parameter annotations
    - Parameters as local names
    - Parameters used in expressions
    - Parameters used in return values
    - Parameters with different data types
    - Parameter order
    - Reusing parameters
    - Parameters and function scope
    - Parameters versus arguments
"""


# =============================================================================
# 01. Function Without Parameters
# =============================================================================

def display_repository_name() -> None:
    """
    Display the repository name.
    """
    print(
        "Python Learning Repository"
    )


display_repository_name()


# A function does not require parameters.
#
# Parameters are introduced when a function needs information
# from its caller.


# =============================================================================
# 02. Function With One Parameter
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


# `student_name` is the parameter.
#
# "Alex" is the argument supplied during the function call.


# =============================================================================
# 03. Parameter Receives a Value
# =============================================================================

def display_city_name(
    city_name: str,
) -> None:
    """
    Display a supplied city name.
    """
    print(
        f"City: {city_name}"
    )


display_city_name(
    "Bengaluru"
)


# Conceptually:
#
#     city_name
#          ↓
#     receives "Bengaluru"
#          ↓
#     function body uses city_name


# =============================================================================
# 04. Function With Multiple Parameters
# =============================================================================

def display_person_information(
    person_name: str,
    person_age: int,
) -> None:
    """
    Display a person's basic information.
    """
    print(
        f"Name: {person_name}"
    )

    print(
        f"Age: {person_age}"
    )


display_person_information(
    "Sam",
    28,
)


# A function can define multiple parameters.


# =============================================================================
# 05. Multiple Parameters Have Individual Types
# =============================================================================

def display_product_information(
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


display_product_information(
    "Keyboard",
    1499.50,
    True,
)


# Each parameter can have its own annotation.


# =============================================================================
# 06. Parameter Used in a Calculation
# =============================================================================

def calculate_double_value(
    source_number: int,
) -> int:
    """
    Return twice the supplied number.
    """
    return source_number * 2


double_value_result: int = calculate_double_value(
    25
)

print(
    double_value_result
)


# A parameter behaves like a local name inside the function body.


# =============================================================================
# 07. Parameter Used in a String
# =============================================================================

def create_greeting_message(
    visitor_name: str,
) -> str:
    """
    Create a greeting using the supplied name.
    """
    return f"Hello, {visitor_name}!"


greeting_result: str = create_greeting_message(
    "Jordan"
)

print(
    greeting_result
)


# Parameters allow the same function logic to work with different values.


# =============================================================================
# 08. Reusing the Same Parameterized Function
# =============================================================================

def calculate_triple_value(
    input_number: int,
) -> int:
    """
    Return three times the supplied number.
    """
    return input_number * 3


triple_first_result: int = calculate_triple_value(
    10
)

triple_second_result: int = calculate_triple_value(
    15
)

triple_third_result: int = calculate_triple_value(
    20
)

print(
    triple_first_result
)

print(
    triple_second_result
)

print(
    triple_third_result
)


# The parameter receives a different value during each function call.


# =============================================================================
# 09. Parameters Can Be Used Multiple Times
# =============================================================================

def calculate_rectangle_area(
    rectangle_length: float,
    rectangle_width: float,
) -> float:
    """
    Calculate the area of a rectangle.
    """
    return (
        rectangle_length
        * rectangle_width
    )


rectangle_area_result: float = calculate_rectangle_area(
    12.5,
    8.0,
)

print(
    rectangle_area_result
)


# A parameter can participate in multiple operations within the function.


# =============================================================================
# 10. Parameters Can Be Used in Conditions
# =============================================================================

def classify_temperature(
    temperature_value: float,
) -> str:
    """
    Classify a temperature value.
    """
    if temperature_value >= 30:
        return "Hot"

    return "Moderate"


temperature_classification: str = classify_temperature(
    32.5
)

print(
    temperature_classification
)


# Parameters can be used anywhere a normal local name can be used.


# =============================================================================
# 11. Parameters Can Be Used With Collections
# =============================================================================

def display_first_item(
    item_collection: list[str],
) -> None:
    """
    Display the first item from a string list.
    """
    print(
        item_collection[0]
    )


language_collection: list[str] = [
    "Python",
    "SQL",
    "Java",
]

display_first_item(
    language_collection
)


# Parameters can refer to collection objects as well.


# =============================================================================
# 12. Parameter With a Tuple
# =============================================================================

def calculate_coordinate_sum(
    coordinate_pair: tuple[int, int],
) -> int:
    """
    Return the sum of two coordinates.
    """
    return (
        coordinate_pair[0]
        + coordinate_pair[1]
    )


coordinate_sum_result: int = calculate_coordinate_sum(
    (10, 20)
)

print(
    coordinate_sum_result
)


# Type annotations can describe structured parameter values.


# =============================================================================
# 13. Parameter With a Dictionary
# =============================================================================

def display_employee_department(
    employee_record: dict[str, str],
) -> None:
    """
    Display the department from an employee record.
    """
    print(
        employee_record["department"]
    )


employee_information: dict[str, str] = {
    "name": "Taylor",
    "department": "Engineering",
}

display_employee_department(
    employee_information
)


# =============================================================================
# 14. Parameter With Multiple Collection Types
# =============================================================================

def display_score_summary(
    score_values: list[int],
) -> None:
    """
    Display the number of supplied scores.
    """
    print(
        f"Number of scores: {len(score_values)}"
    )


exam_scores: list[int] = [
    80,
    75,
    92,
    88,
]

display_score_summary(
    exam_scores
)


# =============================================================================
# 15. Parameter Names Are Local to the Function
# =============================================================================

def display_local_parameter(
    local_message: str,
) -> None:
    """
    Display a function-local parameter.
    """
    print(
        local_message
    )


display_local_parameter(
    "Inside the function"
)


# `local_message` exists as a name within the function's local scope.
#
# Scope is covered in greater detail in 10_scope.py.


# =============================================================================
# 16. Parameter Does Not Need to Match Argument Name
# =============================================================================

def display_parameter_name(
    function_name: str,
) -> None:
    """
    Display a supplied name.
    """
    print(
        function_name
    )


caller_name_value: str = "Morgan"

display_parameter_name(
    caller_name_value
)


# The caller's variable is:
#
#     caller_name_value
#
# The function's parameter is:
#
#     function_name
#
# They are different names referring to the value passed to the function.


# =============================================================================
# 17. Multiple Parameters Can Be Independent
# =============================================================================

def calculate_total_cost(
    item_cost: float,
    shipping_cost: float,
    tax_cost: float,
) -> float:
    """
    Calculate total cost from three components.
    """
    return (
        item_cost
        + shipping_cost
        + tax_cost
    )


total_cost_result: float = calculate_total_cost(
    1000.0,
    100.0,
    180.0,
)

print(
    total_cost_result
)


# Each parameter represents a separate input to the function.


# =============================================================================
# 18. Parameter Order Matters
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


coordinate_result: tuple[int, int] = create_coordinate(
    10,
    25,
)

print(
    coordinate_result
)


# Parameter order determines which supplied value is associated
# with each parameter when using positional argument passing.
#
# Detailed positional argument behaviour is covered separately.


# =============================================================================
# 19. Parameter Can Receive an Expression Result
# =============================================================================

def display_calculated_value(
    calculated_value: int,
) -> None:
    """
    Display an integer result.
    """
    print(
        calculated_value
    )


display_calculated_value(
    10 + 20
)


# An argument does not have to be a literal.
#
# It can be the result of an expression.


# =============================================================================
# 20. Parameter Can Receive a Function Result
# =============================================================================

def get_reference_score() -> int:
    """
    Return a reference score.
    """
    return 85


def display_score_value(
    score_value: int,
) -> None:
    """
    Display a score.
    """
    print(
        score_value
    )


display_score_value(
    get_reference_score()
)


# The result of one function can become the argument
# supplied to another function.


# =============================================================================
# 21. Parameter With a Boolean Value
# =============================================================================

def display_feature_status(
    feature_enabled: bool,
) -> None:
    """
    Display whether a feature is enabled.
    """
    print(
        f"Feature enabled: {feature_enabled!r}"
    )


display_feature_status(
    True
)

display_feature_status(
    False
)


# Parameters can represent boolean states.


# =============================================================================
# 22. Parameter With None
# =============================================================================

def display_optional_value(
    optional_value: str | None,
) -> None:
    """
    Display a string value or None.
    """
    print(
        repr(optional_value)
    )


display_optional_value(
    "Available"
)

display_optional_value(
    None
)


# A parameter annotation can explicitly describe that None is permitted.


# =============================================================================
# 23. Parameters Are Assigned During Function Calls
# =============================================================================

def display_assignment_example(
    assigned_value: int,
) -> None:
    """
    Display a parameter value.
    """
    print(
        assigned_value
    )


display_assignment_example(
    500
)


# The function call supplies a value that becomes associated
# with the parameter for that invocation.


# =============================================================================
# 24. Each Function Call Has Its Own Parameter Binding
# =============================================================================

def display_invocation_value(
    invocation_value: int,
) -> None:
    """
    Display a value for the current invocation.
    """
    print(
        invocation_value
    )


display_invocation_value(
    100
)

display_invocation_value(
    200
)

display_invocation_value(
    300
)


# Each invocation receives its own parameter value.


# =============================================================================
# 25. Parameter Annotation Is Type Information
# =============================================================================

def display_annotated_parameter(
    annotated_value: int,
) -> None:
    """
    Display an annotated parameter.
    """
    print(
        annotated_value
    )


display_annotated_parameter(
    42
)


# The annotation:
#
#     annotated_value: int
#
# communicates the intended type to developers and static
# type-checking tools.
#
# It does not perform automatic conversion.


# =============================================================================
# 26. Parameters and Return Type Are Separate
# =============================================================================

def calculate_difference(
    minuend_value: int,
    subtrahend_value: int,
) -> int:
    """
    Return the difference between two integers.
    """
    return (
        minuend_value
        - subtrahend_value
    )


difference_result: int = calculate_difference(
    50,
    15,
)

print(
    difference_result
)


# Parameters describe the inputs.
#
# The return annotation describes the intended output.


# =============================================================================
# 27. Parameter Names Should Describe Their Meaning
# =============================================================================

def calculate_monthly_payment(
    loan_amount: float,
    interest_rate: float,
) -> float:
    """
    Demonstrate descriptive parameter names.
    """
    return (
        loan_amount
        * interest_rate
    )


monthly_payment_example: float = calculate_monthly_payment(
    10000.0,
    0.05,
)

print(
    monthly_payment_example
)


# Compare:

# def calculate_monthly_payment(x, y):
#     ...


# with:

# def calculate_monthly_payment(
#     loan_amount: float,
#     interest_rate: float,
# ) -> float:
#     ...


# Descriptive parameter names make the function easier to understand.


# =============================================================================
# 28. Parameters and Reusability
# =============================================================================

def convert_minutes_to_seconds(
    minute_count: int,
) -> int:
    """
    Convert minutes to seconds.
    """
    return minute_count * 60


short_duration_seconds: int = convert_minutes_to_seconds(
    5
)

long_duration_seconds: int = convert_minutes_to_seconds(
    30
)

print(
    short_duration_seconds
)

print(
    long_duration_seconds
)


# Without a parameter, separate functions or duplicated logic
# would be required for different values.


# =============================================================================
# 29. Parameters Versus Arguments
# =============================================================================

"""
Parameter:

    A name defined in the function declaration.

Example:

    def greet_user(
        user_name: str,
    ) -> str:
        ...


`user_name` is a parameter.


Argument:

    A value supplied during the function call.

Example:

    greet_user("Alex")


"Alex" is an argument.


Conceptually:

    Function definition
            ↓
        parameter

    Function call
            ↓
        argument
"""


# =============================================================================
# 30. Parameter Fundamentals Summary
# =============================================================================

"""
Parameters:

    - Receive information from the caller.
    - Are defined inside the function declaration.
    - Behave as local names inside the function.
    - Can have type annotations.
    - Can represent different data types.
    - Can be used in calculations.
    - Can be used in conditions.
    - Can be used with collections.
    - Can be used to produce return values.
    - Make functions reusable.


Basic structure:

    def function_name(
        parameter_name: type,
    ) -> return_type:
        ...


Multiple parameters:

    def function_name(
        first_parameter: type,
        second_parameter: type,
    ) -> return_type:
        ...


Parameter:

    Name defined by the function.


Argument:

    Value supplied by the caller.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Parameters allow functions to receive information.

✓ A parameter is defined in the function declaration.

✓ A function can have zero, one, or multiple parameters.

✓ Each parameter can have its own type annotation.

✓ Parameters behave as local names within the function.

✓ Parameters can be used in expressions and conditions.

✓ Parameters can represent primitive values or collections.

✓ Parameters make functions reusable.

✓ The same function can receive different values across calls.

✓ Parameter names should describe the meaning of the input.

✓ A parameter and an argument are not the same thing.

      parameter
          ↓
      name in function definition

      argument
          ↓
      value supplied during function call

✓ Parameter order matters when arguments are associated positionally.

✓ Detailed positional and keyword argument behaviour is covered
  in separate files.

Core idea:

    Function
       ↓
    Parameters
       ↓
    Receive inputs
       ↓
    Process inputs
       ↓
    Produce output
"""