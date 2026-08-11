"""
==============================================================================
Python Basics
==============================================================================

File
----
05_variables.py

Topic
-----
Variables

Overview
--------
A variable is a name that refers to an object.

Python variables are created when a value is assigned to a name.

This file covers:

    - Creating variables
    - Assignment
    - Variable names and objects
    - Reassignment
    - Multiple variables
    - Multiple assignment
    - Unpacking
    - Swapping variables
    - Aliasing
    - Object references
    - Variables referring to the same object
    - Variables referring to different objects
    - Deleting a variable binding
    - Basic variable scope awareness

Type checking is covered separately in the data_types section.
Type annotations are covered separately in 08_type_hints.py.
"""


# =============================================================================
# 01. Creating a Variable
# =============================================================================

variable_name: str = "Alex"

print(
    variable_name
)


# Assignment creates a name that refers to an object.


# =============================================================================
# 02. Numeric Variable
# =============================================================================

variable_age: int = 30

print(
    variable_age
)


# =============================================================================
# 03. Floating-Point Variable
# =============================================================================

variable_height: float = 5.10

print(
    variable_height
)


# =============================================================================
# 04. Boolean Variable
# =============================================================================

variable_is_active: bool = True

print(
    variable_is_active
)


# =============================================================================
# 05. Multiple Variables
# =============================================================================

variable_first_name: str = "Alex"
variable_last_name: str = "Smith"
variable_city_name: str = "Bengaluru"

print(
    variable_first_name
)

print(
    variable_last_name
)

print(
    variable_city_name
)


# =============================================================================
# 06. Assignment From an Expression
# =============================================================================

variable_first_number: int = 100
variable_second_number: int = 50

variable_total_value: int = (
    variable_first_number
    + variable_second_number
)

print(
    variable_total_value
)


# The expression is evaluated first.
#
# The resulting object is then bound to the variable name.


# =============================================================================
# 07. Reassignment
# =============================================================================

reassignment_value: int = 100

print(
    reassignment_value
)

reassignment_value = 200

print(
    reassignment_value
)


# The same variable name can be rebound to another object.


# =============================================================================
# 08. Reassignment to a Different Type
# =============================================================================

reassignment_dynamic_value_int: int = 100

print(
    reassignment_dynamic_value_int
)

reassignment_dynamic_value = "Python"

print(
    reassignment_dynamic_value
)


# Python allows a name to be rebound to an object of another type.
#
# Type annotations and static type checking can impose stricter
# development-time expectations, but Python itself is dynamically typed.


# =============================================================================
# 09. Multiple Assignment
# =============================================================================

multiple_assignment_first: int = 10
multiple_assignment_second: int = 20
multiple_assignment_third: int = 30

print(
    multiple_assignment_first,
    multiple_assignment_second,
    multiple_assignment_third,
)


# =============================================================================
# 10. Multiple Assignment in One Statement
# =============================================================================

multiple_value_a, multiple_value_b, multiple_value_c = (
    10,
    20,
    30,
)

print(
    multiple_value_a
)

print(
    multiple_value_b
)

print(
    multiple_value_c
)


# Multiple variables can receive multiple values in one statement.


# =============================================================================
# 11. Same Value for Multiple Variables
# =============================================================================

shared_value_first = shared_value_second = shared_value_third = 100

print(
    shared_value_first
)

print(
    shared_value_second
)

print(
    shared_value_third
)


# All three names are assigned from the same value expression.


# =============================================================================
# 12. Tuple Unpacking
# =============================================================================

unpacking_first_name, unpacking_last_name = (
    "Alex",
    "Smith",
)

print(
    unpacking_first_name
)

print(
    unpacking_last_name
)


# The values are unpacked into the corresponding variables.


# =============================================================================
# 13. List Unpacking
# =============================================================================

unpacking_first_number, unpacking_second_number, unpacking_third_number = [
    10,
    20,
    30,
]

print(
    unpacking_first_number
)

print(
    unpacking_second_number
)

print(
    unpacking_third_number
)


# Unpacking works with iterable objects.


# =============================================================================
# 14. Extended Unpacking
# =============================================================================

extended_first_value, *extended_middle_values, extended_last_value = [
    10,
    20,
    30,
    40,
    50,
]

print(
    extended_first_value
)

print(
    extended_middle_values
)

print(
    extended_last_value
)


# * collects the remaining values into a list.


# =============================================================================
# 15. Swapping Variables
# =============================================================================

swap_left_value: int = 10
swap_right_value: int = 20

print(
    f"Before: {swap_left_value=}, {swap_right_value=}"
)

swap_left_value, swap_right_value = (
    swap_right_value,
    swap_left_value,
)

print(
    f"After: {swap_left_value=}, {swap_right_value=}"
)


# Python allows swapping without a temporary variable.


# =============================================================================
# 16. Variable as a Name
# =============================================================================

reference_number_value: int = 100

reference_alias_value: int = reference_number_value

print(
    reference_number_value
)

print(
    reference_alias_value
)


# Both names refer to an object representing the value 100.


# =============================================================================
# 17. Variables and Objects
# =============================================================================

object_reference_text: str = "Python"

print(
    object_reference_text
)


"""
Conceptual model:

    object_reference_text
             │
             ▼
       ┌─────────────┐
       │   "Python"  │
       └─────────────┘

The variable is the name.

The string is the object.

The name refers to the object.
"""


# =============================================================================
# 18. Two Names Referring to the Same Mutable Object
# =============================================================================

shared_list_original: list[int] = [
    10,
    20,
]

shared_list_alias: list[int] = (
    shared_list_original
)

shared_list_alias.append(30)

print(
    f"Original: {shared_list_original!r}"
)

print(
    f"Alias: {shared_list_alias!r}"
)


# Both variables refer to the same list object.
#
# Therefore a mutation through one reference is visible through the other.


# =============================================================================
# 19. Identity of Aliased Objects
# =============================================================================

identity_reference_source: list[str] = [
    "Python",
    "SQL",
]

identity_reference_alias: list[str] = (
    identity_reference_source
)

print(
    f"Same object: "
    f"{identity_reference_source is identity_reference_alias}"
)


# `is` checks whether both names refer to the same object.


# =============================================================================
# 20. Different Objects With Equal Values
# =============================================================================

separate_list_first: list[int] = [
    10,
    20,
]

separate_list_second: list[int] = [
    10,
    20,
]

print(
    f"Equal values: "
    f"{separate_list_first == separate_list_second}"
)

print(
    f"Same object: "
    f"{separate_list_first is separate_list_second}"
)


# Two different objects can contain equal values.


# =============================================================================
# 21. Copying Creates a New Outer Object
# =============================================================================

copy_source_values: list[int] = [
    10,
    20,
]

copy_result_values: list[int] = (
    copy_source_values.copy()
)

print(
    f"Equal: "
    f"{copy_source_values == copy_result_values}"
)

print(
    f"Same object: "
    f"{copy_source_values is copy_result_values}"
)


# copy() creates another list object with equal contents.


# =============================================================================
# 22. Variable Rebinding
# =============================================================================

rebind_reference_value: list[int] = [
    10,
    20,
]

rebind_reference_value = [
    30,
    40,
]

print(
    rebind_reference_value
)


"""
The original name is rebound.

Conceptually:

    Before:

        variable
            │
            ▼
        [10, 20]


    After reassignment:

        variable
            │
            ▼
        [30, 40]
"""


# =============================================================================
# 23. Multiple Names and One Object
# =============================================================================

common_object_list: list[str] = [
    "Python",
    "SQL",
]

common_object_alias_a: list[str] = common_object_list
common_object_alias_b: list[str] = common_object_list

print(
    common_object_alias_a is common_object_alias_b
)

print(
    common_object_alias_a is common_object_list
)

print(
    common_object_alias_b is common_object_list
)


# Three names refer to one object.


# =============================================================================
# 24. Rebinding One Alias
# =============================================================================

rebind_alias_source: list[int] = [
    10,
    20,
]

rebind_alias_reference: list[int] = (
    rebind_alias_source
)

rebind_alias_reference = [
    30,
    40,
]

print(
    f"Original: {rebind_alias_source!r}"
)

print(
    f"Rebound name: {rebind_alias_reference!r}"
)


# Rebinding the second name does not change the original object.
#
# The second name simply starts referring to another object.


# =============================================================================
# 25. Mutation vs Rebinding
# =============================================================================

mutation_reference_list: list[int] = [
    10,
    20,
]

mutation_reference_alias: list[int] = (
    mutation_reference_list
)

mutation_reference_alias.append(30)

print(
    f"After mutation: {mutation_reference_list!r}"
)


mutation_reference_alias = [
    100,
    200,
]

print(
    f"After rebinding alias: "
    f"{mutation_reference_list!r}"
)

print(
    f"Alias now refers to: "
    f"{mutation_reference_alias!r}"
)


"""
Mutation:

    Changes the existing object.

Rebinding:

    Makes a variable name refer to another object.
"""


# =============================================================================
# 26. del Removes a Name Binding
# =============================================================================

deletion_example_value: str = "Python"

print(
    deletion_example_value
)

del deletion_example_value


# The name is no longer available after del.


# =============================================================================
# 27. Variables Inside a Function
# =============================================================================

def create_local_value() -> int:
    local_function_value: int = 100
    return local_function_value


function_result_value: int = (
    create_local_value()
)

print(
    function_result_value
)


# local_function_value exists within the function's local scope.


# =============================================================================
# 28. Passing a Variable to a Function
# =============================================================================

def double_input_value(
    input_number_value: int,
) -> int:
    return input_number_value * 2


original_number_value: int = 25

doubled_number_value: int = (
    double_input_value(
        original_number_value
    )
)

print(
    doubled_number_value
)


# The value/object referenced by a variable can be passed to a function.


# =============================================================================
# 29. Mutable Object Passed to a Function
# =============================================================================

def add_item_to_list(
    target_values: list[int],
) -> None:
    target_values.append(100)


function_list_values: list[int] = [
    10,
    20,
]

add_item_to_list(
    function_list_values
)

print(
    function_list_values
)


# The function receives a reference to the same list object.
#
# Mutating that list is therefore visible outside the function.


# =============================================================================
# 30. Variable Names Can Refer to Different Objects Over Time
# =============================================================================

changing_reference_value_str: str = "Python"

print(
    changing_reference_value_str
)

changing_reference_value: list[str] = [
    "Python",
    "SQL",
]

print(
    changing_reference_value
)

changing_reference_value_int = 100

print(
    changing_reference_value_int
)


# A variable name can be rebound to different objects during execution.


# =============================================================================
# 31. Variables Do Not Store Types Separately
# =============================================================================

conceptual_variable_value: int = 100

print(
    conceptual_variable_value
)


"""
A useful mental model is:

    variable name
         │
         ▼
       object
         │
         ├── value
         └── type


The object has the type.

The variable is a name referring to that object.
"""


# =============================================================================
# 32. Equality vs Identity
# =============================================================================

variable_equality_first: list[int] = [
    10,
    20,
]

variable_equality_second: list[int] = [
    10,
    20,
]

variable_identity_reference: list[int] = (
    variable_equality_first
)

print(
    f"First == second: "
    f"{variable_equality_first == variable_equality_second}"
)

print(
    f"First is second: "
    f"{variable_equality_first is variable_equality_second}"
)

print(
    f"First is reference: "
    f"{variable_equality_first is variable_identity_reference}"
)


# == compares values.
#
# is compares object identity.


# =============================================================================
# 33. Variables and Immutable Objects
# =============================================================================

immutable_variable_value: int = 100

immutable_variable_alias: int = (
    immutable_variable_value
)

immutable_variable_value = 200

print(
    f"Original name: "
    f"{immutable_variable_value!r}"
)

print(
    f"Other name: "
    f"{immutable_variable_alias!r}"
)


# Rebinding one name does not change the object referenced by another name.


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ A variable is a name referring to an object.

✓ Assignment creates or updates a name binding.

      name = object

✓ Python variables do not need a separate declaration statement.

✓ A variable can be rebound:

      value = 100
      value = 200

✓ Multiple variables can be assigned together.

✓ Python supports unpacking.

✓ Variables can be swapped without a temporary variable.

✓ Multiple names can refer to the same object.

      first = some_object
      second = first

✓ This is called aliasing.

✓ Mutating an aliased mutable object affects what both names observe.

✓ Rebinding one name does not rebind the other name.

✓ `==` checks equality.

✓ `is` checks identity.

✓ `.copy()` can create a new outer object.

✓ `del` removes a variable binding.

✓ Function-local variables belong to the function's local scope.

✓ Objects have types and values.

Core mental model:

        VARIABLE NAME
              │
              ▼
           OBJECT
          /      \
       value     type


Assignment:

    variable = object


Rebinding:

    variable ─────► new object


Aliasing:

    variable_a ────┐
                   ├──► same object
    variable_b ────┘
"""