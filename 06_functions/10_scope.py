# =============================================================================
# 10. Scope
# =============================================================================

"""
# Python Functions

## File

10_scope.py

## Topic

Scope

## Overview

Scope determines where a variable can be accessed in a Python program.

A variable is not automatically available everywhere.

Python resolves variable names according to a well-defined scope system.

The main scopes commonly encountered when working with functions are:

    - Local scope
    - Enclosing scope
    - Global scope
    - Built-in scope

These scopes are commonly remembered using the LEGB rule:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

When Python encounters a variable name, it searches these scopes in that
order.

Functions are especially important for understanding scope because every
function call creates a local scope.

Topics covered:

    - What is scope?
    - Local scope
    - Local variables
    - Function parameters and local scope
    - Local variables are created during function execution
    - Local variables are unavailable outside the function
    - Different function calls have separate local scopes
    - Global scope
    - Global variables
    - Reading global variables inside functions
    - Local variables shadowing global variables
    - Modifying global variables
    - The global statement
    - Why global variables should be used carefully
    - Enclosing scope
    - Nested functions
    - Reading variables from an enclosing scope
    - The nonlocal statement
    - Modifying enclosing variables
    - Built-in scope
    - LEGB name resolution
    - Scope and function parameters
    - Scope and assignment
    - NameError caused by unavailable variables
    - UnboundLocalError
    - Local scope created by function calls
    - Scope does not depend on indentation alone
    - Scope and mutable objects
    - Scope versus lifetime
    - Functions create local scope
    - Nested scope and closures
    - Practical scope rules
"""

# =============================================================================
# 01. What Is Scope?
# =============================================================================

"""
Scope means:

    The region of a Python program where a variable name can be accessed.

For example:

    def greet() -> None:
        message: str = "Hello"

The variable:

    message

exists in the local scope of greet().

It can be accessed inside that function.

It cannot normally be accessed from outside the function.

Therefore:

    scope
        ↓
    determines where a name is available

Scope is about name visibility and name resolution.

"""

# =============================================================================
# 02. Local Scope
# =============================================================================

def greet_user() -> str:
    """
    Demonstrate a local variable.
    """
    message: str = "Hello, Guest"

    return message


local_greeting: str = greet_user()

print(
    local_greeting
)

# The variable:
#
# message
#
# is local to:
#
# greet_user()
#
# Therefore it can be accessed inside the function.
#
# It cannot normally be accessed outside the function.

# =============================================================================
# 03. Local Variables Are Created Inside Functions
# =============================================================================

def calculate_square(
    number: int,
) -> int:
    """
    Calculate the square of a number.
    """
    result: int = number ** 2

    return result


square_result: int = calculate_square(
    5,
)

print(
    square_result
)

# The variable:
#
# result
#
# is created inside calculate_square().
#
# Therefore result belongs to the local scope of that function call.

# =============================================================================
# 04. Local Variables Are Not Available Outside the Function
# =============================================================================

def create_message() -> str:
    """
    Create a local message.
    """
    message: str = "Hello"

    return message


created_message: str = create_message()

print(
    created_message
)

# This is valid because the function returns the value.
#
# The following would be invalid:
#
# print(message)
#
# because message is a local variable inside create_message().
#
# Python would raise:
#
# NameError
#
# because message does not exist in the current outer scope.

# =============================================================================
# 05. Function Parameters Are Local Variables
# =============================================================================

def greet(
    name: str,
) -> str:
    """
    Demonstrate that function parameters belong to local scope.
    """
    greeting: str = f"Hello, {name}!"

    return greeting


greeting_result: str = greet(
    "Shreyas",
)

print(
    greeting_result
)

# The parameter:
#
# name
#
# is local to the function.
#
# The variable:
#
# greeting
#
# is also local to the function.
#
# Both belong to the local scope created for the function call.

# =============================================================================
# 06. Each Function Call Has Its Own Local Scope
# =============================================================================

def calculate_value(
    number: int,
) -> int:
    """
    Return a local calculation.
    """
    result: int = number * 10

    return result


first_result: int = calculate_value(
    5,
)

second_result: int = calculate_value(
    10,
)

print(
    first_result
)

print(
    second_result
)

# Each function call creates its own local execution context.
#
# First call:
#
# calculate_value(5)
#
# has:
#
# number = 5
# result = 50
#
# Second call:
#
# calculate_value(10)
#
# has:
#
# number = 10
# result = 100
#
# The local variables from one function call are not shared with another
# function call.

# =============================================================================
# 07. Local Variables With the Same Name
# =============================================================================

def get_first_value() -> int:
    """
    Return a local value.
    """
    value: int = 10

    return value


def get_second_value() -> int:
    """
    Return another local value with the same variable name.
    """
    value: int = 20

    return value


first_value: int = get_first_value()

second_value: int = get_second_value()

print(
    first_value
)

print(
    second_value
)

# Both functions contain a variable named:
#
# value
#
# but these are separate local variables.
#
# get_first_value():
#
# value = 10
#
# get_second_value():
#
# value = 20
#
# The names are the same, but their scopes are different.

# =============================================================================
# 08. Global Scope
# =============================================================================

application_name: str = "DataPipeline"


def show_application() -> str:
    """
    Read a variable from global scope.
    """
    return application_name


global_application_name: str = show_application()

print(
    global_application_name
)

# application_name is defined outside the function.
#
# Therefore it belongs to the global scope of this module.
#
# The function can read the global variable because Python does not find
# a local variable named application_name and continues searching outward.

# =============================================================================
# 09. Reading a Global Variable Inside a Function
# =============================================================================

default_timeout: int = 30


def get_timeout() -> int:
    """
    Read a global configuration value.
    """
    return default_timeout


timeout_value: int = get_timeout()

print(
    timeout_value
)

# The function does not define:
#
# default_timeout
#
# locally.
#
# Python therefore searches the enclosing scopes and then the global scope.
#
# It finds:
#
# default_timeout = 30
#
# and returns that value.

# =============================================================================
# 10. Local Variable Shadows a Global Variable
# =============================================================================

message: str = "Global message"


def show_message() -> str:
    """
    Demonstrate local variable shadowing.
    """
    message: str = "Local message"

    return message


local_message: str = show_message()

print(
    message
)

print(
    local_message
)

# Global scope contains:
#
# message = "Global message"
#
# Local scope inside show_message() contains:
#
# message = "Local message"
#
# When Python looks for message inside show_message(), it finds the local
# variable first.
#
# Therefore the local variable shadows the global variable.

# =============================================================================
# 11. Shadowing Does Not Modify the Global Variable
# =============================================================================

status: str = "global"


def get_status() -> str:
    """
    Return a local variable with the same name.
    """
    status: str = "local"

    return status


local_status: str = get_status()

print(
    local_status
)

print(
    status
)

# The local assignment:
#
# status = "local"
#
# does not change:
#
# status = "global"
#
# because they belong to different scopes.

# =============================================================================
# 12. Assignment Creates a Local Variable
# =============================================================================

counter_12: int = 100


def change_counter() -> int:
    """
    Demonstrate local assignment.
    """
    counter_12: int = 10

    return counter_12


changed_counter: int = change_counter()

print(
    changed_counter
)

print(
    counter_12
)

# Because counter is assigned inside change_counter(),
# Python treats that name as local to the function.
#
# Therefore:
#
# local counter = 10
#
# global counter = 100
#
# remain separate.

# =============================================================================
# 13. Reading Before Local Assignment
# =============================================================================

value_13: int = 100


def demonstrate_assignment() -> int:
    """
    Demonstrate local-variable assignment behaviour.
    """
    value_13: int = 200

    return value_13


assignment_value: int = demonstrate_assignment()

print(
    assignment_value
)

# Once Python sees an assignment to value inside the function,
# value is treated as a local variable throughout that function.
#
# Therefore local assignment and global lookup are separate concepts.

# =============================================================================
# 14. UnboundLocalError
# =============================================================================

counter_value: int = 10


def invalid_counter_update() -> None:
    """
    Demonstrate why reading a local variable before assignment is invalid.
    """
    # The following code is intentionally not executed:
    #
    # print(counter_value)
    #
    # counter_value = counter_value + 1
    #
    # Python sees:
    #
    # counter_value = ...
    #
    # and therefore treats counter_value as local to this function.
    #
    # The attempted read happens before the local variable has received
    # a value.
    #
    # Python raises:
    #
    # UnboundLocalError

    return None


invalid_counter_update()

# Important distinction:
#
# NameError:
#
# the name cannot be found.
#
#
# UnboundLocalError:
#
# Python knows the name is local, but the local variable has not yet
# received a value at the point where it is being accessed.

# =============================================================================
# 15. The global Statement
# =============================================================================

global_counter: int = 0


def increment_global_counter() -> int:
    """
    Modify a global variable using the global statement.
    """
    global global_counter

    global_counter += 1

    return global_counter


first_global_count: int = increment_global_counter()

second_global_count: int = increment_global_counter()

print(
    first_global_count
)

print(
    second_global_count
)

print(
    global_counter
)

# Without:
#
# global global_counter
#
# the assignment:
#
# global_counter += 1
#
# would make global_counter local to the function.
#
# The global statement tells Python:
#
# "Use the variable from global scope."

# =============================================================================
# 16. global Allows Modification of a Global Name
# =============================================================================

configuration_mode: str = "development"


def set_production_mode() -> None:
    """
    Change a global variable.
    """
    global configuration_mode

    configuration_mode = "production"


set_production_mode()

print(
    configuration_mode
)

# The global statement allows the function to rebind the global name:
#
# configuration_mode
#
# from:
#
# "development"
#
# to:
#
# "production"

# =============================================================================
# 17. global Is Not Required Just To Read
# =============================================================================

maximum_limit: int = 100


def get_maximum_limit() -> int:
    """
    Read a global variable without using global.
    """
    return maximum_limit


current_limit: int = get_maximum_limit()

print(
    current_limit
)

# The global statement is not required when only reading a global variable.
#
# It is required when the function needs to assign to the global name.

# =============================================================================
# 18. global Changes the Binding, Not the Object Itself
# =============================================================================

global_items: list[str] = []


def add_global_item(
    item: str,
) -> None:
    """
    Mutate a global list.
    """
    global_items.append(
        item
    )


add_global_item(
    "Python"
)

add_global_item(
    "SQL"
)

print(
    global_items
)

# No global statement is required here.
#
# The function is not assigning a new object to global_items.
#
# It is mutating the existing list object.
#
# The distinction is:
#
# rebinding the name
#     versus
# mutating the object

# =============================================================================
# 19. Rebinding a Global Mutable Object Requires global
# =============================================================================

global_numbers: list[int] = [
    1,
    2,
]


def replace_global_numbers() -> None:
    """
    Replace the global list object.
    """
    global global_numbers

    global_numbers = [
        10,
        20,
    ]


replace_global_numbers()

print(
    global_numbers
)

# Here the function assigns a completely new list to the name:
#
# global_numbers
#
# Therefore global is required.
#
# Compare:
#
# global_numbers.append(3)
#
# with:
#
# global_numbers = [10, 20]
#
# The first mutates the existing object.
#
# The second rebinds the name to a new object.

# =============================================================================
# 20. Why Global Variables Should Be Used Carefully
# =============================================================================

"""
Global variables can be useful for:

    - constants
    - configuration
    - application-wide read-only values

However, excessive use of mutable global state can make programs harder
to understand and test.

For example:

    global_counter = 0

    def increment() -> None:
        global global_counter
        global_counter += 1

The function depends on state outside its local scope.

This can make behaviour less predictable.

A function that receives data through parameters and returns data through
return values is often easier to reason about.

For example:

    def increment(
        counter: int,
    ) -> int:
        return counter + 1

Here the input and output are explicit.

"""

# =============================================================================
# 21. Enclosing Scope
# =============================================================================

def outer_function() -> str:
    """
    Demonstrate an enclosing scope.
    """
    message: str = "Hello from outer"

    def inner_function() -> str:
        """
        Access a variable from the enclosing function.
        """
        return message

    return inner_function()


enclosing_message: str = outer_function()

print(
    enclosing_message
)

# inner_function() has its own local scope.
#
# message is not local to inner_function().
#
# It is defined in outer_function().
#
# Therefore message belongs to the enclosing scope of inner_function().

# =============================================================================
# 22. Nested Functions Create Enclosing Scope
# =============================================================================

def create_greeting() -> str:
    """
    Demonstrate a nested function.
    """
    greeting: str = "Welcome"

    def build_message(
        name: str,
    ) -> str:
        """
        Build a message using the enclosing greeting.
        """
        return f"{greeting}, {name}!"

    return build_message(
        "Shreyas"
    )


nested_greeting: str = create_greeting()

print(
    nested_greeting
)

# Scope structure:
#
# create_greeting()
#
#     greeting
#         ↓
#     enclosing scope
#
# build_message()
#
#     name
#         ↓
#     local scope
#
# build_message() can access greeting because Python searches the
# enclosing scope after the local scope.

# =============================================================================
# 23. Enclosing Scope Is Different From Global Scope
# =============================================================================

application_title: str = "Global Application"


def outer() -> str:
    """
    Demonstrate the difference between enclosing and global scope.
    """
    section_title: str = "Outer Section"

    def inner() -> str:
        """
        Access enclosing and global variables.
        """
        return (
            f"{application_title}; "
            f"{section_title}"
        )

    return inner()


scope_result: str = outer()

print(
    scope_result
)

# For inner(), the scopes include:
#
# Local:
#
#     variables defined inside inner()
#
# Enclosing:
#
#     variables defined inside outer()
#
# Global:
#
#     variables defined at module level
#
# Built-in:
#
#     Python built-in names

# =============================================================================
# 24. The nonlocal Statement
# =============================================================================

from collections.abc import Callable


def create_counter() -> Callable[[], int]:
    """
    Create a counter using an enclosing variable.
    """
    count: int = 0

    def increment() -> int:
        """
        Modify the enclosing count variable.
        """
        nonlocal count

        count += 1

        return count

    return increment


counter: Callable[[], int] = create_counter()

first_count: int = counter()

second_count: int = counter()

third_count: int = counter()

print(
    first_count
)

print(
    second_count
)

print(
    third_count
)

# count belongs to create_counter().
#
# increment() needs to modify that variable.
#
# Therefore:
#
# nonlocal count
#
# tells Python to use the variable from the nearest enclosing function
# scope instead of creating a new local variable.

# =============================================================================
# 25. nonlocal Is Used With Enclosing Function Variables
# =============================================================================

def create_score():
    """
    Create a score updater.
    """
    score: int = 0

    def add_score(
        points: int,
    ) -> int:
        """
        Modify the enclosing score.
        """
        nonlocal score

        score += points

        return score

    return add_score


score = create_score()

first_score: int = score(
    10
)

second_score: int = score(
    20
)

print(
    first_score
)

print(
    second_score
)

# score belongs to the enclosing function create_score().
#
# add_score() modifies that variable using nonlocal.

# =============================================================================
# 26. nonlocal Does Not Refer To Global Scope
# =============================================================================

"""
The nonlocal statement searches enclosing function scopes.

It does NOT search global scope.

For example:

    value = 100

    def outer():
        def inner():
            nonlocal value

The above is invalid because there is no enclosing function scope
containing value.

The variable value exists in global scope, not an enclosing function scope.

Use:

    global

for global scope.

Use:

    nonlocal

for an enclosing function scope.

"""

# =============================================================================
# 27. Built-in Scope
# =============================================================================

def use_builtin_scope(
    values: list[int],
) -> int:
    """
    Demonstrate access to a built-in function.
    """
    return len(
        values
    )


value_count: int = use_builtin_scope(
    [10, 20, 30]
)

print(
    value_count
)

# len is not defined locally.
#
# It is not defined in an enclosing function.
#
# It is not defined as a global variable in this module.
#
# Python therefore searches the built-in scope.
#
# It finds:
#
# len
#
# which is a built-in function.

# =============================================================================
# 28. LEGB Rule
# =============================================================================

"""
Python commonly resolves names using the LEGB rule.

L
↓
Local

E
↓
Enclosing

G
↓
Global

B
↓
Built-in

The search order is:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

Python checks the nearest applicable scope first.

Example:

    value = "global"

    def outer():
        value = "enclosing"

        def inner():
            value = "local"
            return value

        return inner()

The result is:

    "local"

because the local scope contains value.

If the local variable did not exist, Python would search the enclosing
scope.

If it did not exist there, Python would search global scope.

Finally, Python would search built-in scope.

"""

# =============================================================================
# 29. LEGB Example
# =============================================================================

value: str = "global"


def demonstrate_legb() -> str:
    """
    Demonstrate Local, Enclosing, Global, and Built-in lookup.
    """
    value: str = "local"

    return value


legb_value: str = demonstrate_legb()

print(
    legb_value
)

# The local value is found first.
#
# Therefore Python does not continue searching for value in global scope.

# =============================================================================
# 30. LEGB With an Enclosing Variable
# =============================================================================

value: str = "global"


def outer_value() -> str:
    """
    Demonstrate enclosing scope lookup.
    """
    value: str = "enclosing"

    def inner_value() -> str:
        """
        Read the enclosing value.
        """
        return value

    return inner_value()


enclosing_result: str = outer_value()

print(
    enclosing_result
)

# inner_value() does not define value locally.
#
# Python searches:
#
# Local
#     ↓
# not found
#
# Enclosing
#     ↓
# found:
#
# value = "enclosing"
#
# Therefore the enclosing value is returned.

# =============================================================================
# 31. LEGB With Global Lookup
# =============================================================================

global_name: str = "Global"


def read_global_name() -> str:
    """
    Demonstrate global lookup.
    """
    return global_name


global_name_result: str = read_global_name()

print(
    global_name_result
)

# Local scope:
#
# global_name not found
#
# Enclosing scope:
#
# no enclosing function
#
# Global scope:
#
# global_name found
#
# Therefore the global value is returned.

# =============================================================================
# 32. LEGB With Built-in Lookup
# =============================================================================

def calculate_length(
    values: list[int],
) -> int:
    """
    Demonstrate built-in name lookup.
    """
    return len(
        values
    )


length_result: int = calculate_length(
    [1, 2, 3, 4]
)

print(
    length_result
)

# len is found in built-in scope.

# =============================================================================
# 33. Scope of a Function Parameter
# =============================================================================

def multiply(
    number: int,
    multiplier: int,
) -> int:
    """
    Demonstrate parameter scope.
    """
    result: int = number * multiplier

    return result


multiplication_result: int = multiply(
    5,
    3,
)

print(
    multiplication_result
)

# Both:
#
# number
#
# and:
#
# multiplier
#
# are local to the function call.
#
# result is also local to the function call.

# =============================================================================
# 34. Scope of Variables Created During Function Execution
# =============================================================================

def process_number(
    number: int,
) -> int:
    """
    Create multiple local variables.
    """
    doubled: int = number * 2
    squared: int = number ** 2

    return doubled + squared


processed_number: int = process_number(
    5
)

print(
    processed_number
)

# doubled and squared exist in the local scope of process_number().
#
# They are not global variables.

# =============================================================================
# 35. Local Scope Exists During Function Execution
# =============================================================================

def temporary_calculation() -> int:
    """
    Demonstrate temporary local state.
    """
    temporary_value: int = 100

    return temporary_value


temporary_result: int = temporary_calculation()

print(
    temporary_result
)

# temporary_value belongs to the function's local scope.
#
# Once the function finishes executing, that local execution context is
# no longer active.
#
# The returned value can continue to exist because it was returned and
# stored in temporary_result.

# =============================================================================
# 36. Scope and Return Values
# =============================================================================

def create_value() -> int:
    """
    Return a local value to the caller.
    """
    local_value: int = 500

    return local_value


returned_value: int = create_value()

print(
    returned_value
)

# The caller cannot directly access local_value by name.
#
# Instead, the function explicitly transfers its value through return.
#
# Therefore:
#
# local variable
#       ↓
# return
#       ↓
# caller receives value

# =============================================================================
# 37. Scope and Mutable Objects
# =============================================================================

def add_value(
    values: list[int],
) -> None:
    """
    Mutate a list received as an argument.
    """
    values.append(
        10
    )


numbers: list[int] = []

add_value(
    numbers
)

print(
    numbers
)

# The parameter:
#
# values
#
# is local to add_value().
#
# However, values refers to the same list object supplied by the caller.
#
# Therefore:
#
# local parameter
#       ↓
# references
#       ↓
# caller's list object
#
# Mutating the object changes what the caller observes.

# =============================================================================
# 38. Scope Does Not Mean Object Ownership
# =============================================================================

def append_item(
    items: list[str],
) -> None:
    """
    Demonstrate local reference to an external object.
    """
    items.append(
        "Python"
    )


languages: list[str] = []

append_item(
    languages
)

print(
    languages
)

# items is a local name.
#
# languages is a global name in this example.
#
# Both names can refer to the same list object.
#
# Scope determines where the names are accessible.
#
# It does not automatically determine who owns the object.

# =============================================================================
# 39. Rebinding a Local Name Does Not Rebind the Caller Name
# =============================================================================

def replace_list(
    items: list[str],
) -> None:
    """
    Rebind the local parameter to a new list.
    """
    items = [# pyright: ignore[reportUnusedVariable]
        "SQL"
    ]


languages: list[str] = [
    "Python"
]

replace_list(
    languages
)

print(
    languages
)

# The assignment:
#
# items = ["SQL"]
#
# creates a new local binding for items.
#
# It does not replace the caller's languages variable.
#
# Therefore languages remains:
#
# ["Python"]

# =============================================================================
# 40. Mutating Versus Rebinding
# =============================================================================

def mutate_list(
    items: list[str],
) -> None:
    """
    Mutate the received list.
    """
    items.append(
        "SQL"
    )


def rebind_list(
    items: list[str],
) -> None:
    """
    Rebind the local parameter.
    """
    items = [# pyright: ignore[reportUnusedVariable]
        "Java"
    ]


languages: list[str] = [
    "Python"
]

mutate_list(
    languages
)

print(
    languages
)

rebind_list(
    languages
)

print(
    languages
)

# After mutate_list():
#
# languages becomes:
#
# ["Python", "SQL"]
#
# because the original list object was mutated.
#
# After rebind_list():
#
# languages remains:
#
# ["Python", "SQL"]
#
# because the local name items was merely rebound to another list.

# =============================================================================
# 41. Nested Scope Can Access Outer Variables
# =============================================================================

def create_message_builder(
    prefix: str,
):
    """
    Create a nested message-building function.
    """

    def build_message(
        message: str,
    ) -> str:
        """
        Use the enclosing prefix.
        """
        return f"{prefix}: {message}"

    return build_message


message_builder = create_message_builder(
    "INFO"
)

built_message: str = message_builder(
    "Process completed"
)

print(
    built_message
)

# build_message() does not receive prefix as its parameter.
#
# It obtains prefix from the enclosing scope.
#
# This behaviour is an important part of closures.

# =============================================================================
# 42. Closure Scope
# =============================================================================

def create_multiplier(
    multiplier: float,
):
    """
    Create a function that remembers multiplier.
    """

    def multiply(
        number: float,
    ) -> float:
        """
        Multiply a number using the enclosing multiplier.
        """
        return number * multiplier

    return multiply


double = create_multiplier(
    2
)

triple = create_multiplier(
    3
)

double_result: float = double(
    10
)

triple_result: float = triple(
    10
)

print(
    double_result
)

print(
    triple_result
)

# create_multiplier() creates an enclosing scope containing:
#
# multiplier
#
# The returned multiply() function remembers that enclosing value.
#
# Therefore:
#
# double
#
# remembers:
#
# multiplier = 2
#
# while:
#
# triple
#
# remembers:
#
# multiplier = 3
#
# This is an example of a closure.

# =============================================================================
# 43. Scope and Closures
# =============================================================================

"""
A closure occurs when a nested function remembers variables from its
enclosing scope even after the outer function has finished executing.

Example:

    def create_multiplier(
        multiplier: float,
    ):
        def multiply(
            number: float,
        ) -> float:
            return number * multiplier

        return multiply

The returned function remembers:

    multiplier

Therefore:

    double = create_multiplier(2)

creates a function that remembers:

    multiplier = 2

and:

    triple = create_multiplier(3)

creates another function that remembers:

    multiplier = 3

The local parameter:

    number

is supplied when the returned function is called.

The enclosing variable:

    multiplier

comes from the scope captured by the closure.

"""

# =============================================================================
# 44. Scope and Default Arguments Are Different
# =============================================================================

default_value: int = 10


def demonstrate_default(
    value: int = default_value,
) -> int:
    """
    Demonstrate default-value evaluation.
    """
    return value


default_value = 20

default_scope_result: int = demonstrate_default()

print(
    default_scope_result
)

# The default expression:
#
# default_value
#
# was evaluated when the function was defined.
#
# Therefore changing the global variable afterward does not change the
# already established default value.
#
# This demonstrates that default-argument evaluation and runtime name
# lookup are separate concepts.

# =============================================================================
# 45. NameError From Missing Scope
# =============================================================================

def valid_function() -> str:
    """
    Return a valid local value.
    """
    local_message: str = "Hello"

    return local_message


valid_message: str = valid_function()

print(
    valid_message
)

# The following would be invalid:
#
# print(local_message)
#
# because local_message exists only inside valid_function().
#
# Python would raise:
#
# NameError

# =============================================================================
# 46. Same Name in Different Scopes
# =============================================================================

name_46: str = "Global Name"


def outer_name() -> str:
    """
    Demonstrate multiple names with the same spelling.
    """
    name_46: str = "Enclosing Name" # pyright: ignore[reportUnusedVariable]

    def inner_name() -> str:
        """
        Define a local name that shadows the enclosing name.
        """
        name_46: str = "Local Name"

        return name_46

    return inner_name()


same_name_result: str = outer_name()

print(
    name_46
)

print(
    same_name_result
)

# Three different scopes can contain:
#
# name
#
# Global:
#
# "Global Name"
#
# Enclosing:
#
# "Enclosing Name"
#
# Local:
#
# "Local Name"
#
# The closest scope wins.

# =============================================================================
# 47. LEGB Search Order in Practice
# =============================================================================

scope_name: str = "global"


def outer_scope() -> str:
    """
    Demonstrate LEGB lookup.
    """
    scope_name: str = "enclosing"

    def inner_scope() -> str:
        """
        Search for scope_name.
        """
        return scope_name

    return inner_scope()


scope_result: str = outer_scope()

print(
    scope_result
)

# inner_scope() searches:
#
# Local
#     ↓
# scope_name not found
#
# Enclosing
#     ↓
# scope_name = "enclosing"
#
# found.
#
# Python stops searching once it finds the name.

# =============================================================================
# 48. Scope and Assignment Inside Nested Functions
# =============================================================================

def create_state():
    """
    Demonstrate local and enclosing assignment.
    """
    state: int = 0

    def read_state() -> int:
        """
        Read the enclosing state.
        """
        return state

    return read_state


state_reader = create_state()

state_value: int = state_reader()

print(
    state_value
)

# Reading the enclosing variable does not require nonlocal.
#
# nonlocal is required only when the nested function needs to rebind
# the enclosing variable.

# =============================================================================
# 49. nonlocal Changes the Enclosing Binding
# =============================================================================

def create_sequence():
    """
    Create a sequence generator using nonlocal state.
    """
    current_value: int = 0

    def next_value() -> int:
        """
        Increment and return the enclosing value.
        """
        nonlocal current_value

        current_value += 1

        return current_value

    return next_value


sequence = create_sequence()

sequence_value_1: int = sequence()

sequence_value_2: int = sequence()

sequence_value_3: int = sequence()

print(
    sequence_value_1
)

print(
    sequence_value_2
)

print(
    sequence_value_3
)

# The nested function changes the variable:
#
# current_value
#
# that belongs to the enclosing function.

# =============================================================================
# 50. Local, Enclosing, and Global Together
# =============================================================================

environment: str = "production"


def outer_configuration() -> str:
    """
    Demonstrate local, enclosing, and global scope together.
    """
    configuration: str = "application"

    def inner_configuration() -> str:
        """
        Access local, enclosing, and global values.
        """
        operation: str = "processing"

        return (
            f"environment->{environment}; "
            f"configuration->{configuration}; "
            f"operation->{operation}"
        )

    return inner_configuration()


configuration_result: str = outer_configuration()

print(
    configuration_result
)

# inner_configuration() has access to:
#
# Local:
#
# operation
#
# Enclosing:
#
# configuration
#
# Global:
#
# environment
#
# Built-in:
#
# any required built-in names such as str, print, etc.

# =============================================================================
# 51. Scope Is Determined Lexically
# =============================================================================

"""
Python functions use lexical scope.

This means that scope is determined by where functions and variables are
defined in the source code.

Consider:

    value = "global"

    def outer():
        value = "outer"

        def inner():
            return value

        return inner()

inner() uses the value from outer() because inner() is defined inside
outer().

The lookup is based on the source-code nesting structure.

This is why the enclosing scope is sometimes called a lexical scope.

"""

# =============================================================================
# 52. Scope Does Not Mean "Where the Function Was Called"
# =============================================================================

value: str = "global"


def read_value() -> str:
    """
    Read value using lexical scope.
    """
    return value


def caller() -> str:
    """
    Call another function.
    """
    value: str = "caller" # pyright: ignore[reportUnusedVariable]

    return read_value()


caller_result: str = caller()

print(
    caller_result
)

# read_value() does not use caller()'s local value.
#
# caller() contains:
#
# value = "caller"
#
# but read_value() was defined at global scope.
#
# Therefore read_value() searches its own lexical scope and finds:
#
# global value = "global"
#
# The caller's local variables do not automatically become enclosing
# variables of the called function.

# =============================================================================
# 53. Called Function Does Not Inherit Caller Scope
# =============================================================================

def first_function() -> str:
    """
    Define a local variable and call another function.
    """
    message: str = "first" # pyright: ignore[reportUnusedVariable]

    return second_function()


def second_function() -> str:
    """
    Attempt to access a name from another function.
    """
    # The following would be invalid:
    #
    # return message
    #
    # message belongs to first_function(), not second_function().
    #
    # Function calls do not transfer local variables between functions.

    return "second"


function_scope_result: str = first_function()

print(
    function_scope_result
)

# The local scope of first_function() is not the enclosing scope of
# second_function().
#
# Only lexical nesting creates an enclosing scope.

# =============================================================================
# 54. Function Definitions Create Names in Their Defining Scope
# =============================================================================

def calculate_total(
    price: float,
) -> float:
    """
    Calculate a simple total.
    """
    return price


total_function_result: float = calculate_total(
    100.0
)

print(
    total_function_result
)

# The name:
#
# calculate_total
#
# is created in the surrounding module scope.
#
# The variables inside the function are local to the function.

# =============================================================================
# 55. Nested Function Name Is Local to the Outer Function
# =============================================================================

def outer_builder() -> str:
    """
    Define a nested function.
    """

    def inner_builder() -> str:
        """
        Return a nested value.
        """
        return "Nested function"

    return inner_builder()


nested_function_result: str = outer_builder()

print(
    nested_function_result
)

# inner_builder is defined inside outer_builder().
#
# Therefore the name inner_builder belongs to the local scope of
# outer_builder().
#
# It is not automatically available globally.

# =============================================================================
# 56. Scope and Function Objects
# =============================================================================

def create_function() -> str:
    """
    Return a function result.
    """

    def inner() -> str:
        """
        Return a nested message.
        """
        return "Hello"

    return inner()


function_object_result: str = create_function()

print(
    function_object_result
)

# A function defined inside another function is itself an object.
#
# Its name:
#
# inner
#
# is local to the outer function unless it is returned or otherwise exposed.

# =============================================================================
# 57. Scope and Constants
# =============================================================================

DEFAULT_BATCH_SIZE: int = 100


def process_batch(
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> int:
    """
    Use a module-level constant.
    """
    return batch_size


default_batch: int = process_batch()

custom_batch: int = process_batch(
    250
)

print(
    default_batch
)

print(
    custom_batch
)

# Module-level constants are commonly written in uppercase.
#
# They are still names in global scope.
#
# A function can read them without using global.

# =============================================================================
# 58. Scope and Imports
# =============================================================================

"""
Imported names also become names in the scope where they are imported.

For example:

    import math

The name:

    math

becomes available in the module's global scope.

A function defined in that module can then read math through normal
LEGB lookup.

Example:

    import math

    def calculate_square_root(
        number: float,
    ) -> float:
        return math.sqrt(number)

The function finds math in global scope.

"""

# =============================================================================
# 59. Local Import Scope
# =============================================================================

def calculate_square_root(
    number: float,
) -> float:
    """
    Demonstrate a locally imported name.
    """
    import math

    return math.sqrt(
        number
    )


square_root: float = calculate_square_root(
    25.0
)

print(
    square_root
)

# math is imported inside the function.
#
# Therefore the name math is local to the function's scope.
#
# It is not automatically available as a global name.

# =============================================================================
# 60. Scope and Comprehensions
# =============================================================================

numbers: list[int] = [
    1,
    2,
    3,
]


def create_squared_values(
    values: list[int],
) -> list[int]:
    """
    Create squared values using a comprehension.
    """
    squared_values: list[int] = [
        value ** 2
        for value in values
    ]

    return squared_values


squared_values: list[int] = create_squared_values(
    numbers
)

print(
    squared_values
)

# Comprehensions have their own iteration-variable scope in modern Python.
#
# The variable:
#
# value
#
# does not leak into the surrounding scope as a normal for-loop variable
# would in older Python versions.

# =============================================================================
# 61. Scope and for Loops
# =============================================================================

def calculate_sum(
    values: list[int],
) -> int:
    """
    Demonstrate loop variables inside function scope.
    """
    total: int = 0

    for value in values:
        total += value

    return total


sum_result: int = calculate_sum(
    [10, 20, 30]
)

print(
    sum_result
)

# The function creates one local scope.
#
# total and value belong to that function scope.
#
# A for loop does not create a separate function-like scope.

# =============================================================================
# 62. Scope and if Statements
# =============================================================================

# mypy: ignore-errors

def get_status_62(
    enabled: bool,
) -> str:
    """
    Demonstrate that if blocks do not create function scope.
    """
    if enabled:
        status: str = "enabled"
    else:
        status = "disabled"

    return status


enabled_status_62: str = get_status(True)# pyright: ignore[reportUnknownVariableType, reportCallIssue]

disabled_status_62: str = get_status(False)# pyright: ignore[reportUnknownVariableType, reportCallIssue]

print(
    enabled_status_62)# pyright: ignore[reportUnknownArgumentType]

print(
    disabled_status_62) # pyright: ignore[reportUnknownArgumentType]

# if and else blocks do not create a separate local scope.
#
# status belongs to the function scope.

# =============================================================================
# 63. Scope and try Statements
# =============================================================================

def parse_number(
    value: str,
) -> int:
    """
    Demonstrate variable scope inside try/except.
    """
    try:
        number: int = int(
            value
        )
    except ValueError:
        number = 0

    return number


parsed_number: int = parse_number(
    "100"
)

print(
    parsed_number
)

# try and except blocks do not create function-like scopes.
#
# number belongs to the function scope.

# =============================================================================
# 64. Scope Versus Lifetime
# =============================================================================

"""
Scope and lifetime are related but different concepts.

Scope asks:

    "Where can this name be accessed?"

Lifetime asks:

    "How long does the object exist?"

For example:

    def create_message() -> str:
        message: str = "Hello"
        return message

The name:

    message

has local scope.

After the function returns, that local name is no longer accessible
from outside the function.

However, the string object can continue to exist because the returned
value is stored by the caller.

Therefore:

    scope
        ↓
    visibility of a name

while:

    lifetime
        ↓
    existence of an object

"""

# =============================================================================
# 65. Local Scope and Object Lifetime
# =============================================================================

def create_list() -> list[int]:
    """
    Create and return a local list.
    """
    values: list[int] = [
        1,
        2,
        3,
    ]

    return values


returned_values: list[int] = create_list()

print(
    returned_values
)

# The local name:
#
# values
#
# is no longer accessible after the function returns.
#
# But the list object continues to exist because returned_values refers
# to that object.

# =============================================================================
# 66. Scope and Parameters With Mutable Objects
# =============================================================================

def append_number(
    numbers: list[int],
) -> None:
    """
    Mutate a list through a local parameter.
    """
    numbers.append(
        100
    )


values: list[int] = [
    1,
    2,
]

append_number(
    values
)

print(
    values
)

# numbers is local.
#
# values is outside the function.
#
# Both names reference the same list object during the function call.
#
# The local scope does not create a copy automatically.

# =============================================================================
# 67. Scope and Immutable Objects
# =============================================================================

def increment_number(
    number: int,
) -> None:
    """
    Rebind a local integer parameter.
    """
    number += 10


value_67: int = 100

increment_number(
    value_67
)

print(
    value_67
)

# Integers are immutable.
#
# The expression:
#
# number += 10
#
# creates a new integer object and rebinds the local name number.
#
# The caller's value variable remains unchanged.

# =============================================================================
# 68. Scope Does Not Automatically Copy Arguments
# =============================================================================

def demonstrate_reference(
    values: list[int],
) -> None:
    """
    Demonstrate that function parameters receive references to objects.
    """
    values.append(
        3
    )


numbers_68: list[int] = [
    1,
    2,
]

demonstrate_reference(
    numbers_68
)

print(
    numbers_68
)

# The parameter values is local.
#
# The list object itself is not copied automatically.
#
# Therefore mutation is visible through the caller's reference.

# =============================================================================
# 69. global Versus nonlocal
# =============================================================================

"""
global:

    Refers to a name in module/global scope.

Example:

    counter = 0

    def increment():
        global counter
        counter += 1


nonlocal:

    Refers to a name in an enclosing function scope.

Example:

    def create_counter():
        counter = 0

        def increment():
            nonlocal counter
            counter += 1

        return increment

The distinction is:

    global
        ↓
    module scope

    nonlocal
        ↓
    nearest enclosing function scope

Neither keyword is required merely to read a variable.

"""

# =============================================================================
# 70. Local Versus Global Assignment
# =============================================================================

global_value: int = 10


def local_assignment() -> int:
    """
    Create a local variable with the same name.
    """
    global_value: int = 20

    return global_value


local_assignment_result: int = local_assignment()

print(
    local_assignment_result
)

print(
    global_value
)

# Without global, assignment inside the function creates a local name.
#
# Therefore:
#
# local global_value = 20
#
# does not modify:
#
# global global_value = 10

# =============================================================================
# 71. Explicit global Assignment
# =============================================================================

global_value_explicit: int = 10


def global_assignment() -> None:
    """
    Explicitly modify the global variable.
    """
    global global_value_explicit

    global_value_explicit = 20


global_assignment()

print(
    global_value_explicit
)

# global explicitly changes the binding target from local scope to
# global scope.

# =============================================================================
# 72. Explicit nonlocal Assignment
# =============================================================================

def create_value_updater():
    """
    Create an updater for an enclosing variable.
    """
    value: int = 10

    def update() -> int:
        """
        Modify the enclosing variable.
        """
        nonlocal value

        value = 20

        return value

    return update


update_value = create_value_updater()

updated_value: int = update_value()

print(
    updated_value
)

# nonlocal changes the binding target from:
#
# inner local scope
#
# to:
#
# nearest enclosing function scope.

# =============================================================================
# 73. LEGB Core Example
# =============================================================================

name_73: str = "Global"


def outer_function_scope() -> str:
    """
    Demonstrate LEGB using nested functions.
    """
    name_73: str = "Enclosing" # pyright: ignore[reportUnusedVariable]

    def inner_function_scope() -> str:
        """
        Demonstrate local lookup.
        """
        name_73: str = "Local"

        return name_73

    return inner_function_scope()


legb_core_result: str = outer_function_scope()

print(
    legb_core_result
)

# Search order:
#
# Local
#     ↓
# "Local"
#
# Search stops immediately.
#
# Enclosing and global values are not considered once the local name
# has been found.

# =============================================================================
# 74. LEGB When Local Name Is Missing
# =============================================================================

name_74: str = "Global"


def outer_function_scope_2() -> str:
    """
    Demonstrate enclosing lookup.
    """
    name_74: str = "Enclosing" # pyright: ignore[reportUnusedVariable]

    def inner_function_scope_2() -> str:
        """
        Read the enclosing name.
        """
        return name_74

    return inner_function_scope_2()


legb_enclosing_result: str = outer_function_scope_2()

print(
    legb_enclosing_result
)

# Local:
#
# name not found.
#
# Enclosing:
#
# name = "Enclosing"
#
# found.
#
# Search stops.

# =============================================================================
# 75. LEGB When Local and Enclosing Names Are Missing
# =============================================================================

name_75: str = "Global"


def read_global_from_nested_function() -> str:
    """
    Read a global value from a nested function.
    """

    def inner() -> str:
        """
        Read the global name.
        """
        return name_75

    return inner()


legb_global_result: str = read_global_from_nested_function()

print(
    legb_global_result
)

# Local:
#
# name not found.
#
# Enclosing:
#
# name not found.
#
# Global:
#
# name found.
#
# Therefore the global value is returned.

# =============================================================================
# 76. LEGB Built-in Fallback
# =============================================================================

def use_builtin(
    values: list[int],
) -> int:
    """
    Use a name supplied by built-in scope.
    """
    return sum(
        values
    )


builtin_result: int = use_builtin(
    [10, 20, 30]
)

print(
    builtin_result
)

# sum is not defined locally.
#
# It is not defined in an enclosing function.
#
# It is not required to be defined globally.
#
# Python finds sum in built-in scope.

# =============================================================================
# 77. Avoiding Name Shadowing
# =============================================================================

"""
It is generally a good practice to avoid unnecessary shadowing of:

    - global variables
    - imported names
    - built-in names

For example, avoid:

    list = [1, 2, 3]

because list is also a built-in type.

Similarly, avoid:

    sum = 100

if the code later needs the built-in sum() function.

Shadowing is allowed by Python, but it can make code confusing or cause
unexpected errors.

"""

# =============================================================================
# 78. Built-in Name Shadowing Example
# =============================================================================

def calculate_total_from_values(
    values: list[int],
) -> int:
    """
    Calculate a total without shadowing built-ins.
    """
    total: int = sum(
        values
    )

    return total


total_from_values: int = calculate_total_from_values(
    [10, 20, 30]
)

print(
    total_from_values
)

# Prefer descriptive names such as:
#
# total
#
# instead of:
#
# sum
#
# when the built-in sum() function may also be needed.

# =============================================================================
# 79. Scope and Constants
# =============================================================================

DEFAULT_TIMEOUT_SECONDS: int = 30


def configure_timeout(
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> int:
    """
    Use a global constant as a default.
    """
    return timeout_seconds


configured_timeout: int = configure_timeout()

print(
    configured_timeout
)

# DEFAULT_TIMEOUT_SECONDS is available through global scope.
#
# The default expression is evaluated when the function is defined.

# =============================================================================
# 80. Scope With Multiple Nested Levels
# =============================================================================

def level_one() -> str:
    """
    Demonstrate multiple enclosing scopes.
    """
    value: str = "level-one" # pyright: ignore[reportUnusedVariable]

    def level_two() -> str:
        """
        Define a second nested scope.
        """
        value: str = "level-two"

        def level_three() -> str:
            """
            Access the nearest enclosing value.
            """
            return value

        return level_three()

    return level_two()


nested_scope_result: str = level_one()

print(
    nested_scope_result
)

# level_three() searches:
#
# Local:
#
# value not found.
#
# Enclosing:
#
# level_two() contains:
#
# value = "level-two"
#
# Therefore that value is selected.
#
# The search does not continue to level_one() because the name was already
# found in the nearest enclosing scope.

# =============================================================================
# 81. nonlocal Selects the Nearest Enclosing Binding
# =============================================================================

def multiple_enclosing_scopes():
    """
    Demonstrate nonlocal with multiple enclosing scopes.
    """
    value: str = "outer" # pyright: ignore[reportUnusedVariable]

    def middle() -> str:
        """
        Create another enclosing scope.
        """
        value: str = "middle"

        def inner() -> str:
            """
            Modify the nearest enclosing value.
            """
            nonlocal value

            value = "changed"

            return value

        return inner()

    return middle()


multiple_scope_result: str = multiple_enclosing_scopes()

print(
    multiple_scope_result
)

# nonlocal value refers to the nearest enclosing function scope containing
# value.
#
# In this example that is middle(), not multiple_enclosing_scopes().

# =============================================================================
# 82. Scope and Function Factories
# =============================================================================

def create_power_function(
    exponent: int,
):
    """
    Create a function that remembers an exponent.
    """

    def power(
        number: int,
    ) -> int:
        """
        Calculate a power using the enclosing exponent.
        """
        return number ** exponent

    return power


square = create_power_function(
    2
)

cube = create_power_function(
    3
)

square_value: int = square(
    5
)

cube_value: int = cube(
    5
)

print(
    square_value
)

print(
    cube_value
)

# square remembers:
#
# exponent = 2
#
# cube remembers:
#
# exponent = 3
#
# The nested function uses an enclosing variable.

# =============================================================================
# 83. Scope and Decorator-Like Structure
# =============================================================================

def create_multiplier_function(
    multiplier: float,
):
    """
    Create a multiplier function using an enclosing variable.
    """

    def multiply(
        number: float,
    ) -> float:
        """
        Multiply using the captured multiplier.
        """
        return number * multiplier

    return multiply


double_function = create_multiplier_function(
    2
)

triple_function = create_multiplier_function(
    3
)

double_output: float = double_function(
    10
)

triple_output: float = triple_function(
    10
)

print(
    double_output
)

print(
    triple_output
)

# The outer function receives:
#
# multiplier
#
# The nested function receives:
#
# number
#
# Therefore the two values come from different scopes:
#
# multiplier
#     ↓
# enclosing scope
#
# number
#     ↓
# local scope
#
# This is one of the fundamental mechanisms behind closures and is also
# heavily used by decorators.

# =============================================================================
# 84. Scope and Callable Objects
# =============================================================================

def create_multiplier_84(
    multiplier: float,
):
    """
    Return a callable that remembers multiplier.
    """

    def multiply(
        number: float,
    ) -> float:
        """
        Multiply number by the enclosing multiplier.
        """
        return number * multiplier

    return multiply


double = create_multiplier_84(
    2
)

triple = create_multiplier_84(
    3
)

print(
    double(
        10
    )
)

print(
    triple(
        10
    )
)

# create_multiplier_84() takes one argument:
#
# multiplier
#
# It returns another function.
#
# That returned function takes one argument:
#
# number
#
# Therefore:
#
# create_multiplier(2)
#
# creates a function that remembers:
#
# multiplier = 2
#
# Then:
#
# double(10)
#
# supplies:
#
# number = 10
#
# The calculation becomes:
#
# 10 * 2
#
# The two values are not supplied to the same function call.
#
# One value belongs to the enclosing scope.
#
# The other belongs to the local scope of the returned function call.

# =============================================================================
# 85. Scope and Type Annotations
# =============================================================================

def calculate_area(
    width: float,
    height: float,
) -> float:
    """
    Demonstrate local variables with annotations.
    """
    area: float = width * height

    return area


rectangle_area: float = calculate_area(
    10.0,
    5.0,
)

print(
    rectangle_area
)

# Type annotations do not change scope.
#
# width, height, and area are still local names.

# =============================================================================
# 86. Scope Does Not Depend On Type Annotations
# =============================================================================

def create_user_name() -> str:
    """
    Demonstrate local scope with an annotated variable.
    """
    user_name: str = "Alex"

    return user_name


user_name_result: str = create_user_name()

print(
    user_name_result
)

# The annotation:
#
# : str
#
# provides type information.
#
# It does not determine the scope.
#
# Scope is determined by where the name is defined.

# =============================================================================
# 87. Practical Scope Pattern
# =============================================================================

def calculate_invoice(
    price: float,
    quantity: int,
) -> float:
    """
    Calculate an invoice total using local variables.
    """
    subtotal: float = price * quantity
    tax: float = subtotal * 0.18
    total: float = subtotal + tax

    return total


invoice_total: float = calculate_invoice(
    1000.0,
    2,
)

print(
    invoice_total
)

# price:
#
# local parameter
#
# quantity:
#
# local parameter
#
# subtotal:
#
# local variable
#
# tax:
#
# local variable
#
# total:
#
# local variable
#
# None of these names need to be global.

# =============================================================================
# 88. Prefer Explicit Data Flow
# =============================================================================

def calculate_discounted_price(
    price: float,
    discount_percentage: float,
) -> float:
    """
    Calculate a discounted price using explicit inputs.
    """
    discount_amount: float = (
        price
        * discount_percentage
        / 100
    )

    final_price: float = (
        price
        - discount_amount
    )

    return final_price


discounted_price: float = calculate_discounted_price(
    1000.0,
    10.0,
)

print(
    discounted_price
)

# The function receives all required information through parameters.
#
# It returns the result through return.
#
# This makes data flow explicit and reduces unnecessary global state.

# =============================================================================
# 89. Scope and Pure Functions
# =============================================================================

def add_numbers(
    first: int,
    second: int,
) -> int:
    """
    Add two numbers using only local inputs.
    """
    result: int = first + second

    return result


addition_result: int = add_numbers(
    10,
    20,
)

print(
    addition_result
)

# The function does not depend on mutable global state.
#
# Its result is determined by its inputs.
#
# This style is generally easier to test and reason about.

# =============================================================================
# 90. Scope Core Model
# =============================================================================

"""
Scope determines where a name can be accessed.

The most important scopes are:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

This is the LEGB rule.

Example:

    value = "global"

    def outer():
        value = "enclosing"

        def inner():
            value = "local"
            return value

        return inner()

Python searches:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

and stops when the name is found.

"""

# =============================================================================
# 91. Scope Rules
# =============================================================================

"""
Important scope rules:

1. Every function call creates a local scope.

2. Function parameters belong to the local scope.

3. Variables assigned inside a function are local by default.

4. A local variable can shadow a global variable with the same name.

5. A function can read global variables without using global.

6. The global statement is required when a function needs to rebind a
   global name.

7. Nested functions can access variables from enclosing function scopes.

8. The nonlocal statement is required when a nested function needs to
   rebind a variable from an enclosing function scope.

9. The nonlocal statement does not refer to global scope.

10. Built-in names are searched after global scope.

11. A called function does not inherit the caller's local scope.

12. Only lexical nesting creates an enclosing scope.

13. Mutating an object is different from rebinding a name.

14. Scope controls name visibility, not object ownership.

15. Scope and object lifetime are related but are not the same concept.

"""

# =============================================================================
# 92. Scope Keywords
# =============================================================================

"""
Python provides two statements for explicitly changing where assignment
targets a name.

global:

    global variable_name

means:

    use the variable from global/module scope.

nonlocal:

    nonlocal variable_name

means:

    use the variable from the nearest enclosing function scope.

Example:

    counter = 0

    def increment_global():
        global counter
        counter += 1

Example:

    def create_counter():
        counter = 0

        def increment():
            nonlocal counter
            counter += 1

        return increment

The two statements solve different scope problems.

"""

# =============================================================================
# 93. Scope and Name Resolution
# =============================================================================

"""
When Python encounters:

    print(value)

it must determine which value the name refers to.

For a nested function, Python conceptually searches:

    1. Local scope
    2. Enclosing function scopes
    3. Global scope
    4. Built-in scope

If no matching name is found, Python raises:

    NameError

If Python determines that a name is local because of an assignment but
the name is read before it has been assigned, Python can raise:

    UnboundLocalError

Understanding name resolution is therefore essential for understanding
functions.

"""

# =============================================================================
# 94. Common Scope Mistakes
# =============================================================================

"""
Common mistakes include:

    - Assuming a local variable is available outside its function.
    - Assuming called functions can access the caller's local variables.
    - Forgetting that assignment inside a function creates a local name.
    - Using global variables unnecessarily.
    - Using global when only reading a global variable.
    - Confusing global with nonlocal.
    - Forgetting nonlocal when modifying an enclosing variable.
    - Assuming mutable arguments are automatically copied.
    - Confusing mutation with rebinding.
    - Shadowing built-in names.
    - Assuming if/for/try blocks create function-like scopes.
    - Forgetting the LEGB lookup order.

"""

# =============================================================================
# 95. Safe Scope Design
# =============================================================================

"""
A practical function design generally prefers:

    inputs
        ↓
    parameters
        ↓
    local calculations
        ↓
    return value

Example:

    def calculate_total(
        price: float,
        quantity: int,
    ) -> float:
        total: float = price * quantity
        return total

Instead of relying on:

    global_price
    global_quantity
    global_total

explicit parameters and return values make data flow easier to understand.

Global constants can still be appropriate when the value is genuinely
shared and conceptually constant.

"""

# =============================================================================
# 96. Scope Summary
# =============================================================================

"""
Scope:

    - Determines where a variable name can be accessed.
    - Is created locally when a function executes.
    - Includes local, enclosing, global, and built-in scopes.
    - Follows the LEGB name-resolution rule.
    - Allows nested functions to access enclosing variables.
    - Allows global variables to be read from functions.
    - Uses global for rebinding global names.
    - Uses nonlocal for rebinding enclosing function names.
    - Does not automatically copy mutable objects.
    - Does not transfer caller-local variables into called functions.
    - Is different from object lifetime.
    - Is different from object ownership.

Core model:

    LOCAL
      ↓
    ENCLOSING
      ↓
    GLOBAL
      ↓
    BUILT-IN

Important distinction:

    assignment inside function
        ↓
    local name by default

    global statement
        ↓
    rebind global name

    nonlocal statement
        ↓
    rebind enclosing function name

"""

# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ Scope determines where a variable name can be accessed.

✓ Every function call creates a local scope.

✓ Function parameters are local variables.

✓ Variables assigned inside a function are local by default.

✓ Local variables are not directly accessible outside their function.

✓ Different function calls have separate local scopes.

✓ A function can read a global variable without using global.

✓ A local variable can shadow a global variable with the same name.

✓ The global statement allows a function to rebind a global variable.

✓ The global statement is not required merely to read a global variable.

✓ Nested functions create enclosing scopes.

✓ A nested function can read variables from an enclosing function.

✓ The nonlocal statement allows a nested function to rebind an enclosing
  function variable.

✓ nonlocal does not refer to global scope.

✓ Built-in names are searched after global scope.

✓ Python commonly resolves names using the LEGB rule:

    Local
      ↓
    Enclosing
      ↓
    Global
      ↓
    Built-in

✓ A called function does not inherit the caller's local scope.

✓ Only lexical nesting creates an enclosing scope.

✓ if, for, and try blocks do not create function-like local scopes.

✓ Mutating an object is different from rebinding a name.

✓ Passing a mutable object to a function does not automatically create a copy.

✓ Scope determines name visibility, not object ownership.

✓ Scope and object lifetime are different concepts.

✓ Closures allow nested functions to remember enclosing variables.

✓ Decorators and function factories heavily rely on enclosing scopes and
  closures.

Core idea:

    VARIABLE NAME
          ↓
    WHERE IS IT DEFINED?
          ↓
    DETERMINE ITS SCOPE
          ↓
    PYTHON SEARCHES USING LEGB
          ↓
    Local
      ↓
    Enclosing
      ↓
    Global
      ↓
    Built-in

Important distinction:

    DEFAULT VALUE
        controls
    what value is used when omitted


    /
        controls
    positional-only parameters


    *
        controls
    keyword-only parameters


    global
        controls
    rebinding a global name


    nonlocal
        controls
    rebinding an enclosing function name
"""

# =============================================================================
# End of 10_scope.py
# =============================================================================