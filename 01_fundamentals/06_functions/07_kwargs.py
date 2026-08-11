# =============================================================================
#
# Python Functions
#
# File
#
# 07_kwargs.py
#
# Topic
#
# Variable-Length Keyword Arguments (**kwargs)
#
# =============================================================================

# """

# Overview

# A variable-length keyword argument allows a function to accept any number
# of keyword arguments.

# Python provides the special parameter syntax:

# **kwargs

# The name "kwargs" is only a conventional name.

# The important part is the "**".

# When a function contains **kwargs, all additional keyword arguments that
# are not assigned to earlier parameters are collected into a dictionary.

# Variable-length keyword arguments therefore allow a function to work with
# an arbitrary number of named values without knowing in advance how many
# keyword arguments the caller will provide.

# Topics covered:

# - What are variable-length keyword arguments?
# - Understanding **kwargs
# - Why **kwargs is used
# - Calling a function without keyword arguments
# - Calling a function with one keyword argument
# - Calling a function with multiple keyword arguments
# - The collected arguments are stored in a dictionary
# - Accessing keyword arguments by key
# - Iterating over **kwargs
# - Finding the number of keyword arguments
# - Checking whether a key exists
# - Using get() with **kwargs
# - Updating values inside **kwargs
# - Combining required parameters with **kwargs
# - Combining normal parameters with **kwargs
# - Keyword arguments are collected after normal parameters
# - **kwargs can collect zero or more arguments
# - **kwargs and dictionary behaviour
# - Unpacking a dictionary into **kwargs
# - Passing a dictionary using **
# - Combining normal keyword arguments with unpacking
# - Using **kwargs with strings
# - Using **kwargs with mixed values
# - Using **kwargs with loops
# - Using **kwargs with built-in functions
# - **kwargs does not collect positional arguments
# - Difference between *args and **kwargs
# - Positional-only parameters with **kwargs
# - Keyword-only parameters with **kwargs
# - Parameter ordering rules
# - **kwargs and strict calling conventions
# - Forwarding keyword arguments to another function
# - Building flexible configuration functions
# - **kwargs and dictionary unpacking
# - Common mistakes with **kwargs

# """


# =============================================================================
#
# 01. Basic **kwargs
#
# =============================================================================

def display_keyword_arguments(
    **kwargs: str,
) -> dict[str, str]:
    """
    Return all supplied keyword arguments.
    """
    return (
        kwargs
    )


arguments: dict[str, str] = display_keyword_arguments(
    language="Python",
    database="SQL",
    version="3.14",
)

print(
    arguments
)

# The parameter:

# **kwargs

# collects all keyword arguments supplied to the function.

#

# The collected values are stored in a dictionary.

#

# Therefore:

#

# display_keyword_arguments(
#     language="Python",
#     database="SQL",
#     version="3.14",
# )

#

# produces a dictionary similar to:

#

# {
#     "language": "Python",
#     "database": "SQL",
#     "version": "3.14",
# }


# =============================================================================
#
# 02. **kwargs Can Receive No Arguments
#
# =============================================================================

def collect_settings(
    **kwargs: object,
) -> dict[str, object]:
    """
    Collect zero or more keyword arguments.
    """
    return (
        kwargs
    )


no_settings: dict[str, object] = collect_settings()

print(
    no_settings
)

# **kwargs can receive zero keyword arguments.

#

# Therefore:

#

# collect_settings()

#

# produces:

#

# {}

#

# The empty dictionary represents that no keyword arguments were supplied.


# =============================================================================
#
# 03. **kwargs Can Receive One Argument
#
# =============================================================================

one_setting: dict[str, object] = collect_settings(
    debug=True,
)

print(
    one_setting
)

# When one keyword argument is supplied:

#

# collect_settings(
#     debug=True,
# )

#

# kwargs becomes:

#

# {
#     "debug": True,
# }


# =============================================================================
#
# 04. **kwargs Can Receive Multiple Arguments
#
# =============================================================================

multiple_settings: dict[str, object] = collect_settings(
    debug=True,
    timeout=30,
    environment="development",
)

print(
    multiple_settings
)

# All keyword arguments are collected into the dictionary.

#

# Therefore:

#

# collect_settings(
#     debug=True,
#     timeout=30,
#     environment="development",
# )

#

# produces:

#

# {
#     "debug": True,
#     "timeout": 30,
#     "environment": "development",
# }


# =============================================================================
#
# 05. **kwargs Is Stored as a Dictionary
#
# =============================================================================

def inspect_keyword_arguments(
    **kwargs: object,
) -> str:
    """
    Return information about the collected keyword arguments.
    """
    return (
        f"type->{type(kwargs).__name__}; "
        f"values->{kwargs}"
    )


argument_information: str = inspect_keyword_arguments(
    language="Python",
    database="SQL",
)

print(
    argument_information
)

# The type of kwargs is:

#

# dict

#

# Therefore:

#

# **kwargs

#

# does NOT create a tuple.

#

# It creates a dictionary containing the collected keyword arguments.


# =============================================================================
#
# 06. Accessing a Keyword Argument
#
# =============================================================================

def get_language(
    **kwargs: str,
) -> str:
    """
    Return the language keyword argument.
    """
    return (
        kwargs["language"]
    )


language: str = get_language(
    language="Python",
    database="SQL",
)

print(
    language
)

# Keyword arguments are stored using their names as dictionary keys.

#

# Therefore:

#

# language="Python"

#

# becomes:

#

# "language": "Python"

#

# inside kwargs.


# =============================================================================
#
# 07. Accessing Multiple Keyword Arguments
#
# =============================================================================

def get_configuration(
    **kwargs: object,
) -> str:
    """
    Return selected configuration values.
    """
    return (
        f"debug->{kwargs['debug']!r}; "
        f"timeout->{kwargs['timeout']}"
    )


configuration: str = get_configuration(
    debug=True,
    timeout=60,
)

print(
    configuration
)

# kwargs behaves like a normal dictionary.

#

# Therefore dictionary indexing can be used:

#

# kwargs["debug"]

#

# kwargs["timeout"]


# =============================================================================
#
# 08. Iterating Over **kwargs
#
# =============================================================================

def print_settings(
    **kwargs: object,
) -> None:
    """
    Print every keyword argument.
    """
    for key, value in kwargs.items():
        print(
            f"{key}->{value!r}"
        )


print_settings(
    environment="development",
    debug=True,
    timeout=30,
)

# kwargs.items()

#

# provides key-value pairs.

#

# The loop receives:

#

# key

# ↓

# keyword name

#

# value

# ↓

# keyword value


# =============================================================================
#
# 09. Iterating Over Keyword Names
#
# =============================================================================

def print_setting_names(
    **kwargs: object,
) -> None:
    """
    Print all keyword argument names.
    """
    for key in kwargs:
        print(
            key
        )


print_setting_names(
    name="Alex",
    age=30,
    city="Bengaluru",
)

# Iterating directly over a dictionary produces its keys.

#

# Therefore:

#

# for key in kwargs:

#

# iterates over the keyword names.


# =============================================================================
#
# 10. Finding the Number of Keyword Arguments
#
# =============================================================================

def count_settings(
    **kwargs: object,
) -> int:
    """
    Return the number of keyword arguments.
    """
    return (
        len(kwargs)
    )


setting_count: int = count_settings(
    name="Alex",
    age=30,
    city="Bengaluru",
)

print(
    setting_count
)

# len(kwargs)

#

# returns the number of collected keyword arguments.


# =============================================================================
#
# 11. Checking Whether a Key Exists
#
# =============================================================================

def has_debug_setting(
    **kwargs: object,
) -> bool:
    """
    Check whether a debug setting exists.
    """
    return (
        "debug" in kwargs
    )


debug_present: bool = has_debug_setting(
    debug=True,
    timeout=30,
)

print(
    debug_present
)

# Since kwargs is a dictionary:

#

# "debug" in kwargs

#

# checks whether the key exists.


# =============================================================================
#
# 12. Using get() With **kwargs
#
# =============================================================================

def get_timeout(
    **kwargs: object,
) -> object:
    """
    Return the timeout value if supplied.
    """
    return (
        kwargs.get(
            "timeout"
        )
    )


timeout_value: object = get_timeout(
    debug=True,
    timeout=60,
)

print(
    timeout_value
)

# Dictionary get() can safely retrieve a value.

#

# Unlike:

#

# kwargs["timeout"]

#

# get():

#

# kwargs.get("timeout")

#

# returns None if the key does not exist.


# =============================================================================
#
# 13. get() With a Fallback Value
#
# =============================================================================

def get_timeout_with_default(
    **kwargs: object,
) -> object:
    """
    Return timeout or a fallback value.
    """
    return (
        kwargs.get(
            "timeout",
            30,
        )
    )


default_timeout: object = get_timeout_with_default(
    debug=True,
)

custom_timeout: object = get_timeout_with_default(
    debug=True,
    timeout=60,
)

print(
    default_timeout
)

print(
    custom_timeout
)

# get() can receive a fallback value.

#

# Therefore:

#

# kwargs.get(
#     "timeout",
#     30,
# )

#

# means:

#

# return timeout if it exists.

#

# Otherwise:

#

# return 30.


# =============================================================================
#
# 14. Updating Values Inside **kwargs
#
# =============================================================================

def enable_debug(
    **kwargs: object,
) -> dict[str, object]:
    """
    Enable debug mode in the collected settings.
    """
    kwargs["debug"] = True

    return (
        kwargs
    )


updated_settings: dict[str, object] = enable_debug(
    timeout=30,
)

print(
    updated_settings
)

# kwargs is a normal dictionary inside the function.

#

# Therefore dictionary operations can be performed.

#

# For example:

#

# kwargs["debug"] = True


# =============================================================================
#
# 15. Required Parameter With **kwargs
#
# =============================================================================

def configure_application(
    application_name: str,
    **settings: object,
) -> str:
    """
    Configure an application using arbitrary keyword settings.
    """
    return (
        f"application->{application_name}; "
        f"settings->{settings}"
    )


application_configuration: str = configure_application(
    "DataPipeline",
    debug=True,
    timeout=60,
    environment="production",
)

print(
    application_configuration
)

# application_name is a normal required parameter.

#

# settings is a variable-length keyword parameter.

#

# Therefore:

#

# "DataPipeline"

# ↓

# application_name

#

# debug=True

# timeout=60

# environment="production"

# ↓

# settings


# =============================================================================
#
# 16. **kwargs Collects Remaining Keyword Arguments
#
# =============================================================================

def create_profile(
    name: str,
    **details: object,
) -> str:
    """
    Create a profile using arbitrary additional details.
    """
    return (
        f"name->{name}; "
        f"details->{details}"
    )


profile: str = create_profile(
    "Alex",
    age=30,
    city="Bengaluru",
    occupation="Developer",
)

print(
    profile
)

# name receives the normal argument.

#

# details receives all remaining keyword arguments.

#

# Therefore:

#

# name = "Alex"

#

# details = {
#     "age": 30,
#     "city": "Bengaluru",
#     "occupation": "Developer",
# }


# =============================================================================
#
# 17. **kwargs Can Represent Zero Additional Keyword Arguments
#
# =============================================================================

def create_profile_without_details(
    name: str,
    **details: object,
) -> str:
    """
    Create a profile with optional additional details.
    """
    return (
        f"name->{name}; "
        f"details->{details}"
    )


profile_without_details: str = create_profile_without_details(
    "Alex",
)

print(
    profile_without_details
)

# The name parameter is required.

#

# details can contain zero values.

#

# Therefore:

#

# details = {}


# =============================================================================
#
# 18. **kwargs With Strings
#
# =============================================================================

def format_attributes(
    **attributes: str,
) -> str:
    """
    Format arbitrary string attributes.
    """
    return (
        "; ".join(
            f"{key}->{value}"
            for key, value in attributes.items()
        )
    )


formatted_attributes: str = format_attributes(
    name="Alex",
    city="Bengaluru",
    role="Developer",
)

print(
    formatted_attributes
)

# Each keyword name becomes a dictionary key.

#

# Each keyword value becomes the corresponding dictionary value.


# =============================================================================
#
# 19. **kwargs With Mixed Values
#
# =============================================================================

def inspect_settings(
    **settings: object,
) -> tuple[str, ...]:
    """
    Return the type name of every setting.
    """
    return tuple(
        type(value).__name__
        for value in settings.values()
    )


setting_types: tuple[str, ...] = inspect_settings(
    name="Alex",
    age=30,
    active=True,
    score=95.5,
)

print(
    setting_types
)

# **kwargs does not require every value to have the same type.

#

# The annotation:

#

# object

#

# allows arbitrary Python objects to be represented.


# =============================================================================
#
# 20. **kwargs With a Loop
#
# =============================================================================

def calculate_numeric_total(
    **values: float,
) -> float:
    """
    Calculate the total of numeric keyword values.
    """
    total: float = 0.0

    for value in values.values():
        total += value

    return (
        total
    )


numeric_total: float = calculate_numeric_total(
    first=100.0,
    second=250.0,
    third=50.0,
)

print(
    numeric_total
)

# values.values()

#

# provides all collected keyword values.

#

# The keys are not required for the calculation.


# =============================================================================
#
# 21. **kwargs With Dictionary Operations
#
# =============================================================================

def analyze_settings(
    **settings: object,
) -> str:
    """
    Analyze collected settings.
    """
    return (
        f"count->{len(settings)}; "
        f"keys->{tuple(settings.keys())}"
    )


settings_analysis: str = analyze_settings(
    debug=True,
    timeout=30,
    environment="development",
)

print(
    settings_analysis
)

# Since settings is a dictionary, normal dictionary methods are available.

#

# Examples:

#

# settings.keys()

# settings.values()

# settings.items()

# settings.get()

# len(settings)


# =============================================================================
#
# 22. Passing a Dictionary Using **
#
# =============================================================================

configuration_values: dict[str, object] = {
    "debug": True,
    "timeout": 60,
    "environment": "production",
}


def display_configuration(
    **configuration: object,
) -> dict[str, object]:
    """
    Return configuration values.
    """
    return (
        configuration
    )


configuration_result: dict[str, object] = display_configuration(
    **configuration_values,
)

print(
    configuration_result
)

# The ** operator can unpack a dictionary when calling a function.

#

# Therefore:

#

# display_configuration(
#     **configuration_values,
# )

#

# behaves like supplying:

#

# debug=True,

# timeout=60,

# environment="production"


# =============================================================================
#
# 23. Dictionary Unpacking With **
#
# =============================================================================

user_details: dict[str, object] = {
    "name": "Alex",
    "age": 30,
}


def describe_user(
    **details: object,
) -> str:
    """
    Describe a user from keyword arguments.
    """
    return (
        f"name->{details['name']}; "
        f"age->{details['age']}"
    )


user_description: str = describe_user(
    **user_details,
)

print(
    user_description
)

# The dictionary:

#

# {
#     "name": "Alex",
#     "age": 30,
# }

#

# is unpacked into keyword arguments.

#

# Therefore:

#

# **user_details

#

# becomes conceptually:

#

# name="Alex"

# age=30


# =============================================================================
#
# 24. Combining Direct Keyword Arguments With **
#
# =============================================================================

base_configuration: dict[str, object] = {
    "debug": True,
    "timeout": 30,
}


def show_configuration(
    **configuration: object,
) -> dict[str, object]:
    """
    Return configuration values.
    """
    return (
        configuration
    )


combined_configuration: dict[str, object] = show_configuration(
    **base_configuration,
    environment="development",
)

print(
    combined_configuration
)

# A dictionary can be unpacked and additional keyword arguments can be
# supplied in the same function call.

#

# Therefore:

#

# **base_configuration

# ↓

# debug=True

# timeout=30

#

# environment="development"

# ↓

# additional keyword argument


# =============================================================================
#
# 25. Multiple Dictionary Unpacking
#
# =============================================================================

first_configuration: dict[str, object] = {
    "debug": True,
}

second_configuration: dict[str, object] = {
    "timeout": 60,
}

all_configuration: dict[str, object] = show_configuration(
    **first_configuration,
    **second_configuration,
)

print(
    all_configuration
)

# Multiple dictionaries can be unpacked into keyword arguments.

#

# The resulting keyword arguments are collected by **configuration.


# =============================================================================
#
# 26. **kwargs Does Not Collect Positional Arguments
#
# =============================================================================

def collect_keyword_values(
    **kwargs: object,
) -> dict[str, object]:
    """
    Collect keyword arguments only.
    """
    return (
        kwargs
    )


keyword_values: dict[str, object] = collect_keyword_values(
    language="Python",
    database="SQL",
)

print(
    keyword_values
)

# **kwargs collects keyword arguments only.

#

# It does NOT collect positional arguments.

#

# Therefore:

#

# **kwargs

# ↓

# keyword arguments

#

# while:

#

# *args

# ↓

# positional arguments


# =============================================================================
#
# 27. Difference Between *args and **kwargs
#
# =============================================================================

"""
The two special parameter forms serve different purposes.

*args

collects:

positional arguments

Example:

def example(
    *args,
):
    ...

Call:

example(
    10,
    20,
    30,
)

Produces:

args = (
    10,
    20,
    30,
)

---

**kwargs

collects:

keyword arguments

Example:

def example(
    **kwargs,
):
    ...

Call:

example(
    name="Alex",
    age=30,
)

Produces:

kwargs = {
    "name": "Alex",
    "age": 30,
}

Therefore:

*args
    ↓
positional arguments
    ↓
tuple

**kwargs
    ↓
keyword arguments
    ↓
dictionary
"""


# =============================================================================
#
# 28. Combining *args and **kwargs
#
# =============================================================================

def describe_call(
    *args: object,
    **kwargs: object,
) -> str:
    """
    Return both positional and keyword arguments.
    """
    return (
        f"args->{args}; "
        f"kwargs->{kwargs}"
    )


call_description: str = describe_call(
    10,
    20,
    name="Alex",
    active=True,
)

print(
    call_description
)

# A function can contain both:

#

# *args

# and:

# **kwargs

#

# They collect different types of arguments.

#

# args:

#

# (
#     10,
#     20,
# )

#

# kwargs:

#

# {
#     "name": "Alex",
#     "active": True,
# }


# =============================================================================
#
# 29. Required Parameter With *args and **kwargs
#
# =============================================================================

def process_request(
    request_name: str,
    *values: object,
    **options: object,
) -> str:
    """
    Process a request with flexible positional values and options.
    """
    return (
        f"request->{request_name}; "
        f"values->{values}; "
        f"options->{options}"
    )


request_result: str = process_request(
    "import",
    "sales.csv",
    "customers.csv",
    validate=True,
    batch_size=100,
)

print(
    request_result
)

# The parameter categories are:

#

# request_name

# ↓

# normal required parameter

#

# values

# ↓

# variable-length positional arguments

#

# options

# ↓

# variable-length keyword arguments


# =============================================================================
#
# 30. Positional Arguments Go To *args
#
# =============================================================================

def inspect_call(
    *args: object,
    **kwargs: object,
) -> str:
    """
    Inspect positional and keyword arguments separately.
    """
    return (
        f"positional->{args}; "
        f"keyword->{kwargs}"
    )


inspection: str = inspect_call(
    10,
    20,
    30,
    name="Alex",
    city="Bengaluru",
)

print(
    inspection
)

# The positional values:

#

# 10

# 20

# 30

#

# go into args.

#

# The keyword values:

#

# name="Alex"

# city="Bengaluru"

#

# go into kwargs.


# =============================================================================
#
# 31. Keyword Names Become Dictionary Keys
#
# =============================================================================

def inspect_keys(
    **kwargs: object,
) -> tuple[str, ...]:
    """
    Return all keyword names.
    """
    return (
        tuple(
            kwargs.keys()
        )
    )


keys: tuple[str, ...] = inspect_keys(
    language="Python",
    database="SQL",
    framework="Django",
)

print(
    keys
)

# The keyword names:

#

# language

# database

# framework

#

# become dictionary keys.


# =============================================================================
#
# 32. Keyword Values Become Dictionary Values
#
# =============================================================================

def inspect_values(
    **kwargs: object,
) -> tuple[object, ...]:
    """
    Return all keyword values.
    """
    return (
        tuple(
            kwargs.values()
        )
    )


values: tuple[object, ...] = inspect_values(
    language="Python",
    version=3.14,
    active=True,
)

print(
    values
)

# The supplied values become dictionary values.

#

# Conceptually:

#

# language="Python"

# ↓

# "language": "Python"

#

# version=3.14

# ↓

# "version": 3.14

#

# active=True

# ↓

# "active": True


# =============================================================================
#
# 33. Keyword Name Must Be Unique
#
# =============================================================================

def display_profile(
    **profile: object,
) -> dict[str, object]:
    """
    Return profile information.
    """
    return (
        profile
    )


profile_information: dict[str, object] = display_profile(
    name="Alex",
    age=30,
)

print(
    profile_information
)

# A keyword argument is identified by its name.

#

# The same keyword cannot be supplied multiple times in one function call.

#

# For example, conceptually:

#

# display_profile(
#     name="Alex",
#     name="Bob",
# )

#

# is invalid.

#

# Python raises an error because the keyword:

#

# name

#

# was supplied more than once.


# =============================================================================
#
# 34. Dictionary Unpacking Can Cause Duplicate Keywords
#
# =============================================================================

profile_data: dict[str, object] = {
    "name": "Alex",
}


def display_name(
    **details: object,
) -> object:
    """
    Return a name from keyword arguments.
    """
    return (
        details["name"]
    )


profile_name: object = display_name(
    **profile_data,
)

print(
    profile_name
)

# Dictionary unpacking is another way of creating keyword arguments.

#

# If the same keyword is also supplied directly, Python can encounter a
# duplicate keyword argument.

#

# Therefore callers should avoid creating duplicate keyword names when
# combining **dictionary unpacking with explicit keyword arguments.


# =============================================================================
#
# 35. **kwargs With Positional-Only Parameters
#
# =============================================================================

def process_data(
    source_name: str,
    /,
    **options: object,
) -> str:
    """
    Process data using a positional-only source name and arbitrary options.
    """
    return (
        f"source->{source_name}; "
        f"options->{options}"
    )


processed_data: str = process_data(
    "sales.csv",
    validate=True,
    batch_size=100,
)

print(
    processed_data
)

# source_name is positional-only.

#

# options collects arbitrary keyword arguments.

#

# Therefore:

#

# source_name

# ↓

# positional-only

#

# options

# ↓

# variable-length keyword arguments


# =============================================================================
#
# 36. **kwargs With Keyword-Only Parameters
#
# =============================================================================

def configure_service(
    service_name: str,
    *,
    debug: bool = False,
    **options: object,
) -> str:
    """
    Configure a service with known and arbitrary keyword options.
    """
    return (
        f"service->{service_name}; "
        f"debug->{debug!r}; "
        f"options->{options}"
    )


default_service: str = configure_service(
    "API",
)

custom_service: str = configure_service(
    "API",
    debug=True,
    timeout=60,
    region="asia-south1",
)

print(
    default_service
)

print(
    custom_service
)

# debug is a known keyword-only parameter.

#

# options collects additional keyword arguments that are not assigned to
# earlier parameters.


# =============================================================================
#
# 37. Known Keyword Parameters Before **kwargs
#
# =============================================================================

def configure_database(
    database_name: str,
    *,
    readonly: bool = False,
    **options: object,
) -> str:
    """
    Configure a database.
    """
    return (
        f"database->{database_name}; "
        f"readonly->{readonly!r}; "
        f"options->{options}"
    )


database_configuration: str = configure_database(
    "production",
    readonly=True,
    timeout=30,
    pool_size=10,
)

print(
    database_configuration
)

# readonly is matched to its named parameter.

#

# timeout and pool_size are collected into options.


# =============================================================================
#
# 38. **kwargs Can Forward Keyword Arguments
#
# =============================================================================

from typing import Any
def configure_application_core(
    application_name: str,
    *,
    debug: bool = False,
    timeout: int = 30,
) -> str:
    """
    Configure the core application settings.
    """
    return (
        f"application->{application_name}; "
        f"debug->{debug!r}; "
        f"timeout->{timeout}"
    )


def configure_application_wrapper(
    application_name: str,
    **options: Any,
) -> str:
    """
    Forward keyword arguments to the core configuration function.
    """
    return (
        configure_application_core(
            application_name,
            **options,
        )
    )


forwarded_configuration: str = configure_application_wrapper(
    "DataPipeline",
    debug=True,
    timeout=60,
)

print(
    forwarded_configuration
)

# kwargs can be unpacked into another function call.

#

# Therefore:

#

# **options

#

# forwards the collected keyword arguments.


# =============================================================================
#
# 39. **kwargs Can Build Flexible Configuration
#
# =============================================================================

def create_configuration(
    application_name: str,
    **settings: object,
) -> dict[str, object]:
    """
    Create a configuration dictionary.
    """
    configuration: dict[str, object] = {
        "application_name": application_name,
    }

    configuration.update(
        settings
    )

    return (
        configuration
    )


application_configuration_data: dict[str, object] = (
    create_configuration(
        "DataPipeline",
        debug=True,
        timeout=60,
        environment="production",
    )
)

print(
    application_configuration_data
)

# **kwargs is useful for configuration-style functions.

#

# The function can accept known information:

#

# application_name

#

# and arbitrary additional settings:

#

# debug

# timeout

# environment

# region

# etc.


# =============================================================================
#
# 40. **kwargs and Dictionary Comprehension
#
# =============================================================================

def uppercase_keys(
    **kwargs: object,
) -> dict[str, object]:
    """
    Return a dictionary with uppercase keys.
    """
    return {
        key.upper(): value
        for key, value in kwargs.items()
    }


uppercase_configuration: dict[str, object] = uppercase_keys(
    environment="production",
    debug=True,
)

print(
    uppercase_configuration
)

# kwargs is a normal dictionary.

#

# Therefore dictionary comprehensions can be used with it.


# =============================================================================
#
# 41. Filtering **kwargs
#
# =============================================================================

def filter_debug_settings(
    **kwargs: object,
) -> dict[str, object]:
    """
    Return only debug-related settings.
    """
    return {
        key: value
        for key, value in kwargs.items()
        if key.startswith(
            "debug"
        )
    }


debug_settings: dict[str, object] = filter_debug_settings(
    debug=True,
    debug_level="verbose",
    timeout=30,
    environment="production",
)

print(
    debug_settings
)

# Because kwargs is a dictionary, it can be filtered using normal
# dictionary techniques.


# =============================================================================
#
# 42. **kwargs and Dictionary Merging
#
# =============================================================================

default_settings: dict[str, object] = {
    "debug": False,
    "timeout": 30,
}


def build_settings(
    **settings: object,
) -> dict[str, object]:
    """
    Return supplied settings.
    """
    return (
        settings
    )


merged_settings: dict[str, object] = {
    **default_settings,
    **build_settings(
        debug=True,
        timeout=60,
    ),
}

print(
    merged_settings
)

# Dictionary unpacking using ** can also be used while constructing
# dictionaries.

#

# This is separate from **kwargs in a function definition.

#

# Here:

#

# **default_settings

# and:

# **build_settings(...)

#

# unpack dictionaries into a new dictionary.


# =============================================================================
#
# 43. **kwargs With Arbitrary Metadata
#
# =============================================================================

def create_metadata(
    **metadata: object,
) -> dict[str, object]:
    """
    Create metadata from arbitrary keyword arguments.
    """
    return (
        metadata
    )


metadata: dict[str, object] = create_metadata(
    author="Shreyas",
    version=1,
    published=True,
    category="Python",
)

print(
    metadata
)

# **kwargs is useful when the names of additional values are not fixed
# in advance.


# =============================================================================
#
# 44. **kwargs With Validation
#
# =============================================================================

def configure_logging(
    **settings: object,
) -> str:
    """
    Configure logging with validation for supported settings.
    """
    allowed_keys: set[str] = {
        "enabled",
        "level",
    }

    unknown_keys: set[str] = (
        set(settings)
        -
        allowed_keys
    )

    if unknown_keys:
        raise ValueError(
            f"Unknown settings: {unknown_keys}"
        )

    return (
        f"settings->{settings}"
    )


valid_logging_configuration: str = configure_logging(
    enabled=True,
    level="INFO",
)

print(
    valid_logging_configuration
)

# **kwargs allows flexible input.

#

# The function can still validate which keyword names are allowed.

#

# Therefore flexible input does not mean that every possible keyword
# must automatically be accepted as valid business logic.


# =============================================================================
#
# 45. **kwargs and Strict Calling Conventions
#
# =============================================================================

"""
A parameter using:

**kwargs

answers:

"What named arguments may this function receive?"

It allows zero or more keyword arguments.

For example:

def example(
    **kwargs: object,
) -> dict[str, object]:
    return kwargs

The following are valid:

example()

example(
    name="Alex",
)

example(
    name="Alex",
    age=30,
)

example(
    name="Alex",
    age=30,
    city="Bengaluru",
)

The values are collected into a dictionary.
"""


# =============================================================================
#
# 46. **kwargs and Argument Unpacking
#
# =============================================================================

"""
A dictionary can be unpacked into keyword arguments using **.

Example:

settings = {
    "debug": True,
    "timeout": 60,
}

def configure(
    **kwargs,
):
    return kwargs

Call:

configure(
    **settings,
)

The dictionary is unpacked into:

debug=True

timeout=60

and then **kwargs collects them again:

kwargs = {
    "debug": True,
    "timeout": 60,
}

Therefore:

** in a function definition
    ↓
collect keyword arguments


** in a function call
    ↓
unpack a dictionary into keyword arguments
"""


# =============================================================================
#
# 47. Difference Between * and **
#
# =============================================================================

"""
The symbols * and ** have different meanings depending on where they appear.

FUNCTION DEFINITION

*args
    ↓
collect positional arguments


**kwargs
    ↓
collect keyword arguments


FUNCTION CALL

*values
    ↓
unpack an iterable into positional arguments


**values
    ↓
unpack a dictionary into keyword arguments


Therefore:

*args
    = collect positional


**kwargs
    = collect keyword


*values
    = unpack positional


**values
    = unpack keyword
"""


# =============================================================================
#
# 48. Combining Everything
#
# =============================================================================

def process_request_fully(
    request_name: str,
    /,
    *values: object,
    debug: bool = False,
    **options: object,
) -> str:
    """
    Demonstrate positional-only, variable positional, keyword-only,
    and variable keyword parameters together.
    """
    return (
        f"request->{request_name}; "
        f"values->{values}; "
        f"debug->{debug!r}; "
        f"options->{options}"
    )


full_request: str = process_request_fully(
    "import",
    "sales.csv",
    "customers.csv",
    debug=True,
    timeout=60,
    batch_size=100,
)

print(
    full_request
)

# Parameter categories:

#

# request_name

# ↓

# positional-only

#

# values

# ↓

# variable-length positional

#

# debug

# ↓

# keyword-only

#

# options

# ↓

# variable-length keyword

#

# This demonstrates the major parameter categories working together.


# =============================================================================
#
# 49. **kwargs Can Receive Dictionary Values of Different Types
#
# =============================================================================

def display_user_data(
    **user_data: object,
) -> str:
    """
    Display arbitrary user data.
    """
    return (
        f"user_data->{user_data}"
    )


user_data: str = display_user_data(
    name="Alex",
    age=30,
    active=True,
    score=95.5,
)

print(
    user_data
)

# **kwargs itself stores key-value pairs.

#

# The values may be different Python types.

#

# The annotation:

#

# object

#

# is useful when the function intentionally accepts arbitrary value types.


# =============================================================================
#
# 50. **kwargs Summary
#
# =============================================================================

"""
Variable-length keyword arguments:
"""