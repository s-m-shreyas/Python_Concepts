"""
==============================================================================
Python Functions
==============================================================================

File
----
05_default_arguments.py

Topic
-----
Default Arguments

Overview
--------
A default argument is a parameter that has a predefined value in the
function definition.

If the caller does not provide a value for that parameter, Python uses
the predefined default value.

If the caller does provide a value, the supplied value replaces the
default value for that particular function call.

Default arguments therefore allow a function to provide optional behaviour
without requiring the caller to explicitly supply every argument.

Topics covered:

    - What is a default argument?
    - Defining default arguments
    - Calling a function without overriding defaults
    - Overriding default values
    - Multiple default arguments
    - Positional arguments with defaults
    - Keyword arguments with defaults
    - Mixing required and default parameters
    - Parameter ordering rules
    - Default values are evaluated when the function is defined
    - Mutable default argument problem
    - Why mutable defaults can produce unexpected behaviour
    - Safe alternatives for mutable defaults
    - Default arguments with positional-only parameters
    - Default arguments with keyword-only parameters
    - Default arguments and strict calling conventions
"""


# =============================================================================
# 01. Basic Default Argument
# =============================================================================

def greet_user(
    user_name: str = "Guest",
) -> str:
    """
    Return a greeting for a user.
    """
    return (
        f"Hello, {user_name}!"
    )


default_greeting: str = greet_user()

print(
    default_greeting
)


# No argument was supplied.
#
# Therefore Python uses the default value:
#
#     user_name = "Guest"
#
# The function behaves as though the caller had supplied:
#
#     greet_user(
#         "Guest"
#     )


# =============================================================================
# 02. Overriding a Default Argument
# =============================================================================

custom_greeting: str = greet_user(
    "Shreyas"
)

print(
    custom_greeting
)


# The function definition contains:
#
#     user_name="Guest"
#
# but the caller supplied:
#
#     "Shreyas"
#
# Therefore the supplied value overrides the default value.


# =============================================================================
# 03. Default Argument Can Be Supplied Positionally
# =============================================================================

def calculate_square(
    number: int = 10,
) -> int:
    """
    Return the square of a number.
    """
    return (
        number
        ** 2
    )


default_square: int = calculate_square()

custom_square: int = calculate_square(
    5
)

print(
    default_square
)

print(
    custom_square
)


# First call:
#
#     calculate_square()
#
# uses:
#
#     number = 10
#
#
# Second call:
#
#     calculate_square(5)
#
# overrides the default:
#
#     number = 5


# =============================================================================
# 04. Default Argument Can Be Supplied Using a Keyword
# =============================================================================

keyword_square: int = calculate_square(
    number=7,
)

print(
    keyword_square
)


# A default parameter can still be explicitly supplied using a keyword.
#
# The default value is used only when the caller does not provide
# a value for that parameter.


# =============================================================================
# 05. Default Argument With Another Required Parameter
# =============================================================================

def calculate_total(
    item_price: float,
    quantity: int = 1,
) -> float:
    """
    Calculate total price.
    """
    return (
        item_price
        * quantity
    )


single_item_total: float = calculate_total(
    1500.0,
)

multiple_item_total: float = calculate_total(
    1500.0,
    3,
)

print(
    single_item_total
)

print(
    multiple_item_total
)


# The function requires:
#
#     item_price
#
# but provides a default for:
#
#     quantity
#
#
# Therefore:
#
#     calculate_total(1500.0)
#
# uses:
#
#     quantity = 1
#
#
# while:
#
#     calculate_total(1500.0, 3)
#
# uses:
#
#     quantity = 3


# =============================================================================
# 06. Required Parameters Must Come Before Default Parameters
# =============================================================================

def create_order(
    product_name: str,
    quantity: int = 1,
) -> str:
    """
    Create a simple order description.
    """
    return (
        f"Product: {product_name}; "
        f"Quantity: {quantity}"
    )


default_order: str = create_order(
    "Keyboard"
)

custom_order: str = create_order(
    "Keyboard",
    3,
)

print(
    default_order
)

print(
    custom_order
)


# This parameter arrangement is valid:
#
#     product_name: str
#     quantity: int = 1
#
#
# The required parameter comes first.
#
# The parameter with a default value comes after it.


# =============================================================================
# 07. Invalid Parameter Ordering
# =============================================================================

# The following function definition is intentionally not executed:
#
# def invalid_function(
#     quantity: int = 1,
#     product_name: str,
# ) -> str:
#     return f"{product_name}: {quantity}"
#
#
# Python raises a SyntaxError:
#
#     non-default argument follows default argument
#
#
# The rule is:
#
#     required parameters
#             ↓
#     before
#             ↓
#     default parameters


# =============================================================================
# 08. Multiple Default Arguments
# =============================================================================

def create_profile(
    name: str,
    age: int = 18,
    city: str = "Bengaluru",
) -> str:
    """
    Create a simple profile.
    """
    return (
        f"name->{name}; "
        f"age->{age}; "
        f"city->{city}"
    )


profile_1: str = create_profile(
    "Alex"
)

profile_2: str = create_profile(
    "Alex",
    30,
)

profile_3: str = create_profile(
    "Alex",
    30,
    "Mysuru",
)

print(
    profile_1
)

print(
    profile_2
)

print(
    profile_3
)


# profile_1:
#
#     name = "Alex"
#     age = 18
#     city = "Bengaluru"
#
#
# profile_2:
#
#     name = "Alex"
#     age = 30
#     city = "Bengaluru"
#
#
# profile_3:
#
#     name = "Alex"
#     age = 30
#     city = "Mysuru"


# =============================================================================
# 09. Skipping a Default Parameter Using a Keyword
# =============================================================================

profile_with_skipped_default: str = create_profile(
    "Alex",
    city="Mysuru",
)

print(
    profile_with_skipped_default
)


# This is an important use of keyword arguments with default parameters.
#
# The caller wants:
#
#     name = "Alex"
#
# and:
#
#     city = "Mysuru"
#
# but wants to keep:
#
#     age = 18
#
# as the default.
#
# Therefore the caller can explicitly name city:
#
#     city="Mysuru"
#
# without supplying age.


# =============================================================================
# 10. Default Arguments and Positional Order
# =============================================================================

def format_date(
    day: int,
    month: int = 1,
    year: int = 2026,
) -> str:
    """
    Format a date.
    """
    return (
        f"{day:02d}-{month:02d}-{year}"
    )


date_1: str = format_date(
    10
)

date_2: str = format_date(
    10,
    8,
)

date_3: str = format_date(
    10,
    8,
    2026,
)

print(
    date_1
)

print(
    date_2
)

print(
    date_3
)


# Positional arguments still follow their normal positional rules.
#
# The existence of default values does not change positional matching.


# =============================================================================
# 11. Default Arguments and Keyword Arguments
# =============================================================================

date_4: str = format_date(
    day=10,
)

date_5: str = format_date(
    year=2026,
    day=10,
    month=8,
)

print(
    date_4
)

print(
    date_5
)


# Keyword arguments are matched by name.
#
# Therefore their order does not matter.


# =============================================================================
# 12. Default Arguments With Mixed Passing
# =============================================================================

date_6: str = format_date(
    10,
    year=2026,
)

print(
    date_6
)


# Here:
#
#     10
#         ↓
#     day
#
# is positional.
#
#     year=2026
#         ↓
#     year
#
# is keyword-based.
#
# month is not supplied, so its default value is used:
#
#     month = 1


# =============================================================================
# 13. Default Argument Is Used Only When Value Is Not Supplied
# =============================================================================

def set_timeout(
    timeout_seconds: int = 30,
) -> str:
    """
    Return a timeout configuration.
    """
    return (
        f"Timeout: {timeout_seconds} seconds"
    )


default_timeout: str = set_timeout()

custom_timeout: str = set_timeout(
    60
)

explicit_default_timeout: str = set_timeout(
    timeout_seconds=30,
)

print(
    default_timeout
)

print(
    custom_timeout
)

print(
    explicit_default_timeout
)


# These calls demonstrate three situations:
#
#     set_timeout()
#         -> default is used
#
#     set_timeout(60)
#         -> default is overridden
#
#     set_timeout(timeout_seconds=30)
#         -> default value is explicitly supplied


# =============================================================================
# 14. Default Values Are Part of the Function Definition
# =============================================================================

def calculate_discount(
    price: float,
    discount_percentage: float = 10.0,
) -> float:
    """
    Calculate a discounted price.
    """
    discount_amount: float = (
        price
        * discount_percentage
        / 100
    )

    return (
        price
        - discount_amount
    )


default_discount: float = calculate_discount(
    1000.0
)

custom_discount: float = calculate_discount(
    1000.0,
    20.0,
)

print(
    default_discount
)

print(
    custom_discount
)


# The function definition establishes:
#
#     discount_percentage = 10.0
#
# unless the caller supplies another value.


# =============================================================================
# 15. Default Arguments Do Not Make the Parameter Mandatory
# =============================================================================

def display_message(
    message: str,
    prefix: str = "INFO",
) -> str:
    """
    Create a formatted message.
    """
    return (
        f"[{prefix}] {message}"
    )


message_1: str = display_message(
    "Process completed"
)

message_2: str = display_message(
    "Process failed",
    "ERROR",
)

print(
    message_1
)

print(
    message_2
)


# message is mandatory.
#
# prefix is optional because it has a default value.


# =============================================================================
# 16. Default Arguments Provide Optional Behaviour
# =============================================================================

def generate_filename(
    file_name: str,
    extension: str = "txt",
) -> str:
    """
    Generate a filename.
    """
    return (
        f"{file_name}.{extension}"
    )


text_filename: str = generate_filename(
    "report"
)

csv_filename: str = generate_filename(
    "report",
    "csv",
)

print(
    text_filename
)

print(
    csv_filename
)


# The caller does not have to provide the extension.
#
# If omitted:
#
#     extension = "txt"
#
# If supplied:
#
#     extension = supplied value


# =============================================================================
# 17. Default Values Can Be Strings
# =============================================================================

def greet(
    name: str,
    greeting: str = "Hello",
) -> str:
    """
    Create a greeting.
    """
    return (
        f"{greeting}, {name}!"
    )


default_greeting_17: str = greet(
    "Shreyas"
)

custom_greeting_17: str = greet(
    "Shreyas",
    "Welcome",
)

print(
    default_greeting
)

print(
    custom_greeting
)


# Default values are not restricted to numeric values.


# =============================================================================
# 18. Default Values Can Be Numeric
# =============================================================================

def calculate_power(
    base: int,
    exponent: int = 2,
) -> int:
    """
    Calculate a power.
    """
    return (
        base
        ** exponent
    )


square_result: int = calculate_power(
    5
)

cube_result: int = calculate_power(
    5,
    3,
)

print(
    square_result
)

print(
    cube_result
)


# The default exponent is:
#
#     2
#
# Therefore the function calculates a square when exponent is omitted.


# =============================================================================
# 19. Default Values Can Be Boolean
# =============================================================================

def configure_logging(
    log_name: str,
    enabled: bool = True,
) -> str:
    """
    Return logging configuration.
    """
    return (
        f"log_name->{log_name}; "
        f"enabled->{enabled!r}"
    )


default_logging: str = configure_logging(
    "application"
)

disabled_logging: str = configure_logging(
    "application",
    False,
)

print(
    default_logging
)

print(
    disabled_logging
)


# Default values can also be boolean values.


# =============================================================================
# 20. Default Values and Function Calls
# =============================================================================

def get_default_limit() -> int:
    """
    Return a default limit.
    """
    return 100


# The following function definition is intentionally not used:
#
# def invalid_default(
#     limit: int = get_default_limit(),
# ) -> int:
#     return limit
#
#
# Function calls can technically be used in default expressions, but the
# important behaviour is that the expression is evaluated when the function
# definition executes, not each time the function is called.


# =============================================================================
# 21. Default Values Are Evaluated Once
# =============================================================================

default_limit: int = 100


def show_limit(
    limit: int = default_limit,
) -> int:
    """
    Return the configured limit.
    """
    return limit


default_limit = 200

first_limit: int = show_limit()

print(
    first_limit
)


# The default expression:
#
#     default_limit
#
# was evaluated when show_limit() was defined.
#
# Changing the global variable afterward does not change the already
# established default value.


# =============================================================================
# 22. Mutable Default Argument Problem
# =============================================================================

def add_item(
    item: str,
    items: list[str] = [],
) -> list[str]:
    """
    Add an item to a list.

    This function intentionally demonstrates the mutable default
    argument problem.
    """
    items.append(
        item
    )

    return items


first_items: list[str] = add_item(
    "Python"
)

second_items: list[str] = add_item(
    "SQL"
)

print(
    first_items
)

print(
    second_items
)


# This produces surprising behaviour.
#
# The default list:
#
#     []
#
# is created only once when the function is defined.
#
# It is NOT recreated every time add_item() is called.
#
# Therefore the same list is reused across calls where items is omitted.


# =============================================================================
# 23. Why Mutable Defaults Are Dangerous
# =============================================================================

"""
Consider:

    def add_item(
        item: str,
        items: list[str] = [],
    ) -> list[str]:
        ...


The default list is created once.

First call:

    add_item("Python")


The default list becomes:

    ["Python"]


Second call:

    add_item("SQL")


The SAME default list is used.

It becomes:

    ["Python", "SQL"]


Therefore mutable default arguments such as:

    []
    {}
    set()

can retain state between function calls.

This is usually not the intended behaviour.
"""


# =============================================================================
# 24. Safe Alternative For Mutable Defaults
# =============================================================================

def add_item_safely(
    item: str,
    items: list[str] | None = None,
) -> list[str]:
    """
    Add an item safely using None as the default.
    """
    if items is None:
        items = []

    items.append(
        item
    )

    return items


safe_first_items: list[str] = add_item_safely(
    "Python"
)

safe_second_items: list[str] = add_item_safely(
    "SQL"
)

print(
    safe_first_items
)

print(
    safe_second_items
)


# Now:
#
#     items=None
#
# is the default.
#
# A new list is created inside the function whenever the caller does
# not provide a list.
#
# Therefore the calls do not share the same list.


# =============================================================================
# 25. Supplying an Existing Mutable Object
# =============================================================================

existing_items: list[str] = [
    "Python"
]

updated_items: list[str] = add_item_safely(
    "SQL",
    existing_items,
)

print(
    updated_items
)


# If the caller explicitly supplies a list, that list is used.
#
# The safe pattern therefore supports both:
#
#     no list supplied
#
# and:
#
#     existing list supplied


# =============================================================================
# 26. Mutable Dictionary Default Problem
# =============================================================================

def add_setting(
    key: str,
    value: str,
    settings: dict[str, str] = {},
) -> dict[str, str]:
    """
    Demonstrate the mutable dictionary default problem.
    """
    settings[key] = value

    return settings


first_settings: dict[str, str] = add_setting(
    "environment",
    "development",
)

second_settings: dict[str, str] = add_setting(
    "debug",
    "enabled",
)

print(
    first_settings
)

print(
    second_settings
)


# The same problem occurs with dictionaries.
#
# The default dictionary is created once and reused between calls.


# =============================================================================
# 27. Safe Dictionary Default
# =============================================================================

def add_setting_safely(
    key: str,
    value: str,
    settings: dict[str, str] | None = None,
) -> dict[str, str]:
    """
    Add a setting safely.
    """
    if settings is None:
        settings = {}

    settings[key] = value

    return settings


safe_first_settings: dict[str, str] = add_setting_safely(
    "environment",
    "development",
)

safe_second_settings: dict[str, str] = add_setting_safely(
    "debug",
    "enabled",
)

print(
    safe_first_settings
)

print(
    safe_second_settings
)


# Each call receives a fresh dictionary when no dictionary is supplied.


# =============================================================================
# 28. Default Arguments With Positional-Only Parameters
# =============================================================================

def calculate_power_strict(
    base: int = 2,
    /,
    exponent: int = 2,
) -> int:
    """
    Calculate a power with a positional-only default parameter.
    """
    return (
        base
        ** exponent
    )


default_power: int = calculate_power_strict()

custom_base_power: int = calculate_power_strict(
    3,
)

custom_power: int = calculate_power_strict(
    3,
    4,
)

print(
    default_power
)

print(
    custom_base_power
)

print(
    custom_power
)


# The parameter:
#
#     base
#
# is both:
#
#     - positional-only
#     - optional
#
# because it has a default value.
#
# Therefore it may be omitted, but if supplied, it must be positional.


# =============================================================================
# 29. Default Arguments With Keyword-Only Parameters
# =============================================================================

def configure_application(
    application_name: str,
    *,
    debug: bool = False,
    timeout: int = 30,
) -> str:
    """
    Configure an application using keyword-only optional parameters.
    """
    return (
        f"application->{application_name}; "
        f"debug->{debug!r}; "
        f"timeout->{timeout}"
    )


default_configuration: str = configure_application(
    "DataPipeline"
)

custom_configuration: str = configure_application(
    "DataPipeline",
    debug=True,
    timeout=60,
)

print(
    default_configuration
)

print(
    custom_configuration
)


# debug and timeout are:
#
#     keyword-only
#
# and:
#
#     optional
#
# because both have default values.


# =============================================================================
# 30. Keyword-Only Does Not Mean Mandatory
# =============================================================================

"""
A parameter can be:

    keyword-only + optional


For example:

    def configure_application(
        application_name: str,
        *,
        debug: bool = False,
    ) -> str:
        ...


debug must be supplied using a keyword IF the caller wants to override it.

But the caller does not have to supply it at all.

Therefore:

    configure_application(
        "DataPipeline"
    )

is valid.

And:

    configure_application(
        "DataPipeline",
        debug=True,
    )

is also valid.
"""


# =============================================================================
# 31. Keyword-Only Default Parameters Can Be Reordered
# =============================================================================

reordered_configuration: str = configure_application(
    timeout=60,
    application_name="DataPipeline",
    debug=True,
)

print(
    reordered_configuration
)


# Keyword argument order remains irrelevant.
#
# The parameter names determine the association.


# =============================================================================
# 32. Combining Positional-Only, Required, and Default Parameters
# =============================================================================

def process_data(
    source_name: str,
    /,
    record_count: int,
    *,
    validate: bool = True,
    batch_size: int = 100,
) -> str:
    """
    Demonstrate different parameter categories together.
    """
    return (
        f"source->{source_name}; "
        f"records->{record_count}; "
        f"validate->{validate!r}; "
        f"batch_size->{batch_size}"
    )


default_process: str = process_data(
    "sales.csv",
    1000,
)

custom_process: str = process_data(
    "sales.csv",
    1000,
    validate=False,
    batch_size=250,
)

print(
    default_process
)

print(
    custom_process
)


# Parameter categories:
#
#     source_name
#         ↓
#     positional-only
#     required
#
#
#     record_count
#         ↓
#     normal parameter
#     required
#
#
#     validate
#         ↓
#     keyword-only
#     optional
#
#
#     batch_size
#         ↓
#     keyword-only
#     optional
#
#
# This demonstrates that positional-only, normal, keyword-only,
# required, and default parameters can all participate in one
# function definition.


# =============================================================================
# 33. Default Arguments Do Not Change Argument Passing Rules
# =============================================================================

"""
A default value answers:

    "What value should this parameter receive if the caller
     does not provide one?"


It does NOT answer:

    "How must the caller provide this parameter?"


Argument-passing rules are controlled separately.

For example:

    def example(
        value: int = 10,
    ) -> int:
        ...


value:

    - has a default
    - can be omitted
    - can be supplied positionally
    - can be supplied using a keyword


With positional-only:

    def example(
        value: int = 10,
        /,
    ) -> int:
        ...


value:

    - has a default
    - can be omitted
    - must be positional if supplied


With keyword-only:

    def example(
        *,
        value: int = 10,
    ) -> int:
        ...


value:

    - has a default
    - can be omitted
    - must be supplied using a keyword if supplied
"""


# =============================================================================
# 34. Default Argument Core Model
# =============================================================================

"""
Default argument:

    A parameter with a predefined value in the function definition.


Example:

    def greet(
        name: str = "Guest",
    ) -> str:
        ...


If omitted:

    greet()


Python uses:

    name = "Guest"


If supplied:

    greet("Shreyas")


Python uses:

    name = "Shreyas"


Therefore:

    DEFAULT VALUE
          ↓
    used when argument
    is not supplied


    SUPPLIED VALUE
          ↓
    overrides the default
"""


# =============================================================================
# 35. Default Arguments Summary
# =============================================================================

"""
Default arguments:

    - Provide a predefined value for a parameter.
    - Make that parameter optional for the caller.
    - Are used when the caller does not supply a value.
    - Can be overridden by supplying another value.
    - Can be supplied positionally.
    - Can be supplied using keywords.
    - Can be combined with required parameters.
    - Must follow required parameters in a normal function definition.

Important rule:

    required parameter
            ↓
    before
            ↓
    default parameter


Default values are evaluated when the function definition executes.

Therefore, mutable defaults such as:

    []
    {}
    set()

can retain state between function calls.

Prefer:

    None

and create the mutable object inside the function when needed.

Example:

    def add_item(
        item: str,
        items: list[str] | None = None,
    ) -> list[str]:
        if items is None:
            items = []

        items.append(item)

        return items


Default arguments can also be combined with strict parameter rules:

    `/`
        -> positional-only

    `*`
        -> keyword-only


A parameter can therefore be:

    positional-only + default

or:

    keyword-only + default.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A default argument is a parameter with a predefined value.

✓ If the caller omits that parameter, Python uses its default value.

✓ If the caller supplies a value, the supplied value overrides the default.

✓ Default arguments make parameters optional from the caller's perspective.

✓ Required parameters must come before parameters with default values.

✓ Default arguments can be supplied positionally.

✓ Default arguments can be supplied using keywords.

✓ Keyword arguments can be used to skip over an earlier default parameter.

✓ Default values do not change the normal rules for positional or keyword
  argument passing.

✓ Default expressions are evaluated when the function definition executes.

✓ Mutable default values such as lists and dictionaries can retain state
  between function calls.

✓ Using None as the default and creating the mutable object inside the
  function is the standard safe pattern.

✓ A parameter can be both positional-only and optional.

✓ A parameter can be both keyword-only and optional.

✓ `/` controls positional-only behaviour.

✓ `*` controls keyword-only behaviour.

✓ Default values control whether supplying a value is optional.

Core idea:

    Default argument
          ↓
    predefined value
          ↓
    caller may omit argument
          ↓
    default is used


    caller supplies value
          ↓
    supplied value overrides default


Important distinction:

    DEFAULT VALUE
        controls
    whether a value is optional


    / and *
        control
    how the value may be supplied
"""