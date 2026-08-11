# =============================================================================
# 11. Global Keyword
# =============================================================================
"""
Python Functions

File:
    11_global_keyword.py

Topic:
    global Keyword

Overview:
    The global keyword tells Python that a name inside a function refers to
    a variable defined in the module/global scope.

The global keyword is mainly used when a function needs to rebind a global
name.

Topics covered:

    - What is the global keyword?
    - Reading global variables
    - Reading does not require global
    - Assignment creates a local variable by default
    - Why += can cause UnboundLocalError
    - Using global for assignment
    - Using global for +=
    - Using global for -=
    - Using global with strings
    - Using global with booleans
    - Using global with lists
    - Mutating a global list without global
    - Rebinding a global list with global
    - global with dictionaries
    - Rebinding dictionary names
    - Multiple global variables
    - Global state
    - Global constants
    - Why excessive global state is risky
    - global versus nonlocal
    - Practical alternatives to global state
    - Explicit data flow
    - Function parameters and return values
    - Encapsulating state
    - Scope rules
    - Common mistakes
"""

# =============================================================================
# 01. What Is the global Keyword?
# =============================================================================

"""
The global keyword tells Python:

    "This name refers to the variable in the module/global scope."

Example:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

Without:

    global counter

Python would treat:

    counter

as a local variable because the function assigns to it.

The global keyword changes the assignment target from local scope to
global/module scope.
"""


# =============================================================================
# 02. A Global Variable
# =============================================================================

application_name: str = "DataPipeline"


def get_application_name() -> str:
    """
    Read a global variable.
    """
    return application_name


application_name_result: str = get_application_name()

print(application_name_result)


# =============================================================================
# 03. Reading a Global Variable Does Not Require global
# =============================================================================

default_timeout: int = 30


def get_default_timeout() -> int:
    """
    Read a global variable.

    The global keyword is not required because the function does not
    reassign the name.
    """
    return default_timeout


default_timeout_result: int = get_default_timeout()

print(default_timeout_result)


# =============================================================================
# 04. Assignment Inside a Function Creates a Local Variable
# =============================================================================

status: str = "global"


def get_local_status() -> str:
    """
    Create a local variable with the same name as the global variable.
    """
    status: str = "local"

    return status


local_status_result: str = get_local_status()

print(local_status_result)
print(status)


# =============================================================================
# 05. Local Assignment Does Not Change the Global Variable
# =============================================================================

message: str = "Global message"


def change_local_message() -> str:
    """
    Change a local variable instead of the global variable.
    """
    message: str = "Local message"

    return message


local_message_result: str = change_local_message()

print(local_message_result)
print(message)


# =============================================================================
# 06. Why global Is Needed for Reassignment
# =============================================================================

counter: int = 0


def increment_counter() -> None:
    """
    Reassign the global counter.

    The global keyword is required because counter is being reassigned.
    """
    global counter

    counter += 1


increment_counter()
increment_counter()
increment_counter()

print(counter)


# =============================================================================
# 07. global With +=
# =============================================================================

score: int = 0


def add_score(points: int) -> None:
    """
    Add points to the global score.
    """
    global score

    score += points


add_score(10)
add_score(20)
add_score(30)

print(score)


# =============================================================================
# 08. global With -=
# =============================================================================

remaining_items: int = 100


def consume_items(amount: int) -> None:
    """
    Decrease the global remaining_items value.
    """
    global remaining_items

    remaining_items -= amount


consume_items(10)
consume_items(20)

print(remaining_items)


# =============================================================================
# 09. global With String Reassignment
# =============================================================================

environment: str = "development"


def set_production_environment() -> None:
    """
    Reassign the global environment variable.
    """
    global environment

    environment = "production"


set_production_environment()

print(environment)


# =============================================================================
# 10. global With Boolean Values
# =============================================================================

application_running: bool = False


def start_application() -> None:
    """
    Set the global application_running flag to True.
    """
    global application_running

    application_running = True


def stop_application() -> None:
    """
    Set the global application_running flag to False.
    """
    global application_running

    application_running = False


start_application()

print(application_running)

stop_application()

print(application_running)


# =============================================================================
# 11. global With Floating-Point Values
# =============================================================================

exchange_rate: float = 1.10


def update_exchange_rate(new_rate: float) -> None:
    """
    Reassign the global exchange rate.
    """
    global exchange_rate

    exchange_rate = new_rate


update_exchange_rate(1.25)

print(exchange_rate)


# =============================================================================
# 12. global With Multiple Variables
# =============================================================================

total_requests: int = 0
successful_requests: int = 0


def record_successful_request() -> None:
    """
    Modify multiple global variables.
    """
    global total_requests
    global successful_requests

    total_requests += 1
    successful_requests += 1


record_successful_request()
record_successful_request()
record_successful_request()

print(total_requests)
print(successful_requests)


# =============================================================================
# 13. Multiple global Names on One Statement
# =============================================================================

processed_files: int = 0
failed_files: int = 0


def record_file_result(success: bool) -> None:
    """
    Modify multiple global variables using one global statement.
    """
    global processed_files, failed_files

    processed_files += 1

    if not success:
        failed_files += 1


record_file_result(True)
record_file_result(True)
record_file_result(False)

print(processed_files)
print(failed_files)


# =============================================================================
# 14. global Can Be Used With Assignment
# =============================================================================

configuration_mode: str = "development"


def enable_production_mode() -> None:
    """
    Change the global configuration mode.
    """
    global configuration_mode

    configuration_mode = "production"


enable_production_mode()

print(configuration_mode)


# =============================================================================
# 15. global Can Be Used With +=
# =============================================================================

download_count: int = 0


def record_download() -> None:
    """
    Increment the global download count.
    """
    global download_count

    download_count += 1


record_download()
record_download()
record_download()

print(download_count)


# =============================================================================
# 16. global Can Be Used With -=
# =============================================================================

available_slots: int = 50


def reserve_slot() -> None:
    """
    Decrease the global number of available slots.
    """
    global available_slots

    available_slots -= 1


reserve_slot()
reserve_slot()

print(available_slots)


# =============================================================================
# 17. global Can Be Used With *=
# =============================================================================

batch_size: int = 10


def double_batch_size() -> None:
    """
    Double the global batch size.
    """
    global batch_size

    batch_size *= 2


double_batch_size()
double_batch_size()

print(batch_size)


# =============================================================================
# 18. global Can Be Used With /= for Compatible Types
# =============================================================================

processing_rate: float = 100.0


def reduce_processing_rate() -> None:
    """
    Reduce the global processing rate.
    """
    global processing_rate

    processing_rate /= 2.0


reduce_processing_rate()

print(processing_rate)


# =============================================================================
# 19. global and Lists
# =============================================================================

global_items: list[str] = []


def replace_global_items() -> None:
    """
    Rebind the global list to a new list.
    """
    global global_items

    global_items = [
        "Python",
        "SQL",
    ]


replace_global_items()

print(global_items)


# =============================================================================
# 20. Mutating a Global List Does Not Require global
# =============================================================================

languages: list[str] = []


def add_language(language: str) -> None:
    """
    Mutate the global list.

    The global keyword is not required because the name languages is not
    being rebound. The existing list object is being mutated.
    """
    languages.append(language)


add_language("Python")
add_language("Go")
add_language("SQL")

print(languages)


# =============================================================================
# 21. Mutation Versus Rebinding
# =============================================================================

"""
There is an important difference between:

    languages.append("Python")

and:

    languages = ["Python"]

The first operation mutates the existing list object.

The second operation rebinds the name languages to a new list.

Therefore:

    languages.append(...)

does not require global.

But:

    languages = [...]

requires global if languages is intended to refer to the module-level name.
"""


# =============================================================================
# 22. Rebinding a Global List Requires global
# =============================================================================

numbers: list[int] = [
    1,
    2,
    3,
]


def replace_numbers() -> None:
    """
    Replace the global list object.
    """
    global numbers

    numbers = [
        10,
        20,
        30,
    ]


replace_numbers()

print(numbers)


# =============================================================================
# 23. Mutating a Global Dictionary Does Not Require global
# =============================================================================

configuration: dict[str, str] = {}


def set_configuration(key: str, value: str) -> None:
    """
    Mutate the global dictionary.
    """
    configuration[key] = value


set_configuration("environment", "production")
set_configuration("debug", "false")

print(configuration)


# =============================================================================
# 24. Rebinding a Global Dictionary Requires global
# =============================================================================

settings: dict[str, str] = {
    "environment": "development",
}


def replace_settings() -> None:
    """
    Replace the global dictionary object.
    """
    global settings

    settings = {
        "environment": "production",
        "debug": "false",
    }


replace_settings()

print(settings)


# =============================================================================
# 25. Reading and Reassigning a Global Variable
# =============================================================================

current_version: int = 1


def upgrade_version() -> int:
    """
    Read and then reassign the global version.
    """
    global current_version

    current_version += 1

    return current_version


version_one: int = upgrade_version()
version_two: int = upgrade_version()

print(version_one)
print(version_two)


# =============================================================================
# 26. global Is Not Needed When Only Reading
# =============================================================================

maximum_connections: int = 100


def show_maximum_connections() -> str:
    """
    Read a global value and return a formatted string.
    """
    return f"Maximum connections: {maximum_connections}"


maximum_connections_message: str = show_maximum_connections()

print(maximum_connections_message)


# =============================================================================
# 27. UnboundLocalError Without global
# =============================================================================

"""
The following pattern would cause UnboundLocalError:

    counter = 0

    def invalid_increment() -> None:
        counter += 1

Python sees:

    counter += 1

and treats counter as a local variable because the function assigns to it.

The operation is conceptually similar to:

    counter = counter + 1

Python therefore attempts to read the local counter before it has received
a value.

The correct version is:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

This example is intentionally described rather than executed so that this
file itself remains error-free.
"""


# =============================================================================
# 28. Correcting the Counter Example With global
# =============================================================================

safe_counter: int = 0


def increment_safe_counter() -> None:
    """
    Correctly increment the global counter.
    """
    global safe_counter

    safe_counter += 1


increment_safe_counter()
increment_safe_counter()

print(safe_counter)


# =============================================================================
# 29. global Does Not Create a New Variable
# =============================================================================

global_value: int = 100


def update_global_value() -> None:
    """
    Rebind the existing global name.
    """
    global global_value

    global_value = 200


update_global_value()

print(global_value)


# =============================================================================
# 30. global Must Refer to a Global Name
# =============================================================================

"""
The global statement does not create a separate local copy.

For example:

    value = 10

    def update() -> None:
        global value
        value = 20

After update() executes:

    value

in the module scope refers to:

    20

The function and the module are referring to the same global name.
"""


# =============================================================================
# 31. global and Function Calls
# =============================================================================

request_count: int = 0


def register_request() -> None:
    """
    Increment a global request counter.
    """
    global request_count

    request_count += 1


def process_requests() -> None:
    """
    Register several requests.
    """
    register_request()
    register_request()
    register_request()


process_requests()

print(request_count)


# =============================================================================
# 32. Global State Persists Between Function Calls
# =============================================================================

login_attempts: int = 0


def record_login_attempt() -> int:
    """
    Increment and return the persistent global login-attempt count.
    """
    global login_attempts

    login_attempts += 1

    return login_attempts


first_attempt: int = record_login_attempt()
second_attempt: int = record_login_attempt()
third_attempt: int = record_login_attempt()

print(first_attempt)
print(second_attempt)
print(third_attempt)


# =============================================================================
# 33. Global State Is Shared
# =============================================================================

shared_counter: int = 0


def first_function() -> None:
    """
    Modify shared global state.
    """
    global shared_counter

    shared_counter += 1


def second_function() -> None:
    """
    Modify the same shared global state.
    """
    global shared_counter

    shared_counter += 10


first_function()
second_function()

print(shared_counter)


# =============================================================================
# 34. Multiple Functions Can Modify the Same Global Variable
# =============================================================================

balance: float = 1000.0


def deposit(amount: float) -> None:
    """
    Add money to the global balance.
    """
    global balance

    balance += amount


def withdraw(amount: float) -> None:
    """
    Remove money from the global balance.
    """
    global balance

    balance -= amount


deposit(500.0)
withdraw(200.0)

print(balance)


# =============================================================================
# 35. global With Conditional Assignment
# =============================================================================

feature_enabled: bool = False


def enable_feature(enabled: bool) -> None:
    """
    Update a global feature flag.
    """
    global feature_enabled

    if enabled:
        feature_enabled = True
    else:
        feature_enabled = False


enable_feature(True)

print(feature_enabled)

enable_feature(False)

print(feature_enabled)


# =============================================================================
# 36. global With a Loop
# =============================================================================

processed_count: int = 0


def process_items(items: list[str]) -> None:
    """
    Increment a global counter while processing items.
    """
    global processed_count

    for _item in items:
        processed_count += 1


process_items(
    [
        "Python",
        "Go",
        "SQL",
    ]
)

print(processed_count)


# =============================================================================
# 37. global and Nested Functions
# =============================================================================

nested_global_counter: int = 0


def outer_function() -> None:
    """
    Define a nested function that modifies a global variable.
    """

    def inner_function() -> None:
        """
        Modify the module-level global variable.
        """
        global nested_global_counter

        nested_global_counter += 1

    inner_function()


outer_function()

print(nested_global_counter)


# =============================================================================
# 38. global Versus Local
# =============================================================================

comparison_value: str = "global"


def demonstrate_local_scope() -> str:
    """
    Create a local variable with the same name.
    """
    comparison_value: str = "local"

    return comparison_value


def demonstrate_global_scope() -> str:
    """
    Return the global variable.
    """
    return comparison_value


local_comparison: str = demonstrate_local_scope()
global_comparison: str = demonstrate_global_scope()

print(local_comparison)
print(global_comparison)
print(comparison_value)


# =============================================================================
# 39. global Changes the Binding Target
# =============================================================================

binding_value: int = 10


def local_binding() -> int:
    """
    Create a local binding.
    """
    binding_value: int = 20

    return binding_value


def global_binding() -> int:
    """
    Modify the module-level binding.
    """
    global binding_value

    binding_value = 30

    return binding_value


local_binding_result: int = local_binding()

print(local_binding_result)
print(binding_value)

global_binding_result: int = global_binding()

print(global_binding_result)
print(binding_value)


# =============================================================================
# 40. global With a Module-Level Constant
# =============================================================================

"""
Global constants are normally not modified.

For example:

    DEFAULT_TIMEOUT_SECONDS = 30

A function can read the constant directly:

    def get_timeout() -> int:
        return DEFAULT_TIMEOUT_SECONDS

No global statement is required.

The global keyword is only relevant if the name needs to be rebound.
"""


DEFAULT_TIMEOUT_SECONDS: int = 30


def get_timeout_seconds() -> int:
    """
    Read the global constant.
    """
    return DEFAULT_TIMEOUT_SECONDS


timeout_seconds: int = get_timeout_seconds()

print(timeout_seconds)


# =============================================================================
# 41. Avoid Rebinding Global Constants
# =============================================================================

"""
Although Python technically allows a module-level constant to be rebound,
constants are conventionally treated as read-only.

Prefer:

    DEFAULT_BATCH_SIZE = 100

and read it from functions:

    def get_batch_size() -> int:
        return DEFAULT_BATCH_SIZE

rather than modifying it with:

    global DEFAULT_BATCH_SIZE

Constants communicate intent to other developers.
"""


DEFAULT_BATCH_SIZE: int = 100


def get_default_batch_size() -> int:
    """
    Return the module-level default batch size.
    """
    return DEFAULT_BATCH_SIZE


batch_size_result: int = get_default_batch_size()

print(batch_size_result)


# =============================================================================
# 42. Global State Can Make Functions Less Predictable
# =============================================================================

"""
Consider:

    total = 0

    def add(value: int) -> None:
        global total
        total += value

The result of add() depends on external mutable state.

A function with explicit inputs and outputs is often easier to understand:

    def add(total: int, value: int) -> int:
        return total + value

The second version makes the data flow explicit.
"""


# =============================================================================
# 43. Prefer Parameters and Return Values
# =============================================================================

def calculate_total(
    current_total: int,
    amount: int,
) -> int:
    """
    Calculate a new total using explicit inputs.
    """
    return current_total + amount


total_result: int = calculate_total(
    100,
    25,
)

print(total_result)


# =============================================================================
# 44. Global State Versus Explicit Data Flow
# =============================================================================

"""
Global-state approach:

    total = 0

    def add_amount(amount: int) -> None:
        global total
        total += amount

Explicit-data-flow approach:

    def add_amount(
        total: int,
        amount: int,
    ) -> int:
        return total + amount

The explicit-data-flow approach is usually easier to:

    - test
    - understand
    - reuse
    - debug
    - reason about
"""


# =============================================================================
# 45. Example Without global
# =============================================================================

def increment_value(
    value: int,
) -> int:
    """
    Return an incremented value without using global state.
    """
    return value + 1


initial_value: int = 10

next_value: int = increment_value(
    initial_value
)

print(initial_value)
print(next_value)


# =============================================================================
# 46. Encapsulating State With a Class
# =============================================================================

class Counter:
    """
    Encapsulate mutable counter state inside an object.
    """

    def __init__(self) -> None:
        """
        Initialize the counter.
        """
        self.value: int = 0

    def increment(self) -> int:
        """
        Increment and return the counter.
        """
        self.value += 1

        return self.value


counter_object: Counter = Counter()

counter_object_first: int = counter_object.increment()
counter_object_second: int = counter_object.increment()

print(counter_object_first)
print(counter_object_second)


# =============================================================================
# 47. Encapsulating State With a Closure
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


counter_function: Callable[[], int] = create_counter()

counter_function_first: int = counter_function()
counter_function_second: int = counter_function()

print(counter_function_first)
print(counter_function_second)


# =============================================================================
# 48. global Versus nonlocal
# =============================================================================

"""
global:

    Refers to a name in module/global scope.

Example:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

nonlocal:

    Refers to a name in the nearest enclosing function scope.

Example:

    def create_counter() -> Callable[[], int]:
        counter = 0

        def increment() -> int:
            nonlocal counter
            counter += 1
            return counter

        return increment

The distinction is:

    global
        ↓
    module/global scope

    nonlocal
        ↓
    nearest enclosing function scope
"""


# =============================================================================
# 49. global Does Not Mean nonlocal
# =============================================================================

global_example_value: int = 100


def demonstrate_global() -> int:
    """
    Modify a module-level value.
    """
    global global_example_value

    global_example_value += 10

    return global_example_value


global_example_result: int = demonstrate_global()

print(global_example_result)


def create_nonlocal_example() -> Callable[[], int]:
    """
    Create a closure with an enclosing value.
    """
    enclosing_value: int = 100

    def update() -> int:
        """
        Modify the enclosing value.
        """
        nonlocal enclosing_value

        enclosing_value += 10

        return enclosing_value

    return update


nonlocal_example: Callable[[], int] = create_nonlocal_example()

print(nonlocal_example())
print(nonlocal_example())


# =============================================================================
# 50. global Only Targets Module Scope
# =============================================================================

"""
The global keyword does not mean:

    "find any variable outside this function."

It specifically refers to the module/global namespace.

For nested functions:

    def outer() -> None:
        value = 10

        def inner() -> None:
            global value

the global declaration refers to the module-level value, not outer()'s
local value.

To modify outer()'s value, use:

    nonlocal value
"""


# =============================================================================
# 51. Correct Nested Function Example With nonlocal
# =============================================================================

def create_score() -> Callable[[int], int]:
    """
    Create a score updater using an enclosing variable.
    """
    score: int = 0

    def add_points(points: int) -> int:
        """
        Modify the enclosing score.
        """
        nonlocal score

        score += points

        return score

    return add_points


score_function: Callable[[int], int] = create_score()

score_first: int = score_function(10)
score_second: int = score_function(20)

print(score_first)
print(score_second)


# =============================================================================
# 52. Global Variables Are Shared Across Calls
# =============================================================================

visits: int = 0


def record_visit() -> int:
    """
    Record a visit using global state.
    """
    global visits

    visits += 1

    return visits


visit_one: int = record_visit()
visit_two: int = record_visit()
visit_three: int = record_visit()

print(visit_one)
print(visit_two)
print(visit_three)


# =============================================================================
# 53. Global Variables Can Be Reset
# =============================================================================

session_count: int = 0


def start_session() -> None:
    """
    Increment the global session count.
    """
    global session_count

    session_count += 1


def reset_sessions() -> None:
    """
    Reset the global session count.
    """
    global session_count

    session_count = 0


start_session()
start_session()

print(session_count)

reset_sessions()

print(session_count)


# =============================================================================
# 54. Global Configuration Example
# =============================================================================

log_level: str = "INFO"


def set_log_level(level: str) -> None:
    """
    Update the global log level.
    """
    global log_level

    log_level = level


def get_log_level() -> str:
    """
    Read the global log level.
    """
    return log_level


set_log_level("DEBUG")

current_log_level: str = get_log_level()

print(current_log_level)


# =============================================================================
# 55. Global Cache Example
# =============================================================================

cache: dict[str, str] = {}


def cache_value(key: str, value: str) -> None:
    """
    Add a value to the global cache.

    Mutation does not require global.
    """
    cache[key] = value


def get_cached_value(key: str) -> str | None:
    """
    Read a value from the global cache.
    """
    return cache.get(key)


cache_value("language", "Python")
cache_value("database", "PostgreSQL")

cached_language: str | None = get_cached_value("language")
cached_database: str | None = get_cached_value("database")

print(cached_language)
print(cached_database)


# =============================================================================
# 56. Replacing a Global Cache
# =============================================================================

def clear_cache() -> None:
    """
    Rebind the global cache to a new dictionary.
    """
    global cache

    cache = {}


clear_cache()

print(cache)


# =============================================================================
# 57. Clearing Versus Rebinding a Dictionary
# =============================================================================

cache_data: dict[str, str] = {
    "language": "Python",
    "database": "PostgreSQL",
}


def clear_cache_by_mutation() -> None:
    """
    Clear the existing dictionary object.

    No global keyword is required because the name is not rebound.
    """
    cache_data.clear()


clear_cache_by_mutation()

print(cache_data)


# =============================================================================
# 58. Rebinding the Dictionary
# =============================================================================

cache_data = {
    "language": "Python",
}


def reset_cache_by_rebinding() -> None:
    """
    Rebind the global dictionary name.
    """
    global cache_data

    cache_data = {}


reset_cache_by_rebinding()

print(cache_data)


# =============================================================================
# 59. global and Lists: append
# =============================================================================

event_log: list[str] = []


def log_event(event: str) -> None:
    """
    Append to a global list.

    No global statement is necessary because the list object is mutated.
    """
    event_log.append(event)


log_event("Application started")
log_event("Application finished")

print(event_log)


# =============================================================================
# 60. global and Lists: reassignment
# =============================================================================

event_log = [
    "Initial event",
]


def reset_event_log() -> None:
    """
    Replace the global event log.
    """
    global event_log

    event_log = []


reset_event_log()

print(event_log)


# =============================================================================
# 61. Global Names and Shadowing
# =============================================================================

user_name: str = "Global User"


def show_user_name() -> str:
    """
    Create a local name that shadows the global name.
    """
    user_name: str = "Local User"

    return user_name


shadowed_name: str = show_user_name()

print(shadowed_name)
print(user_name)


# =============================================================================
# 62. Using global Avoids Shadowing During Reassignment
# =============================================================================

current_user: str = "Guest"


def login_user(name: str) -> None:
    """
    Update the global current_user variable.
    """
    global current_user

    current_user = name


login_user("Alex")

print(current_user)


# =============================================================================
# 63. A Global Variable Can Be Read Before global Is Needed
# =============================================================================

system_name: str = "Production"


def show_system_name() -> str:
    """
    Read a global variable.
    """
    return system_name


system_name_result: str = show_system_name()

print(system_name_result)


# =============================================================================
# 64. A Function Can Return a Global Variable
# =============================================================================

application_version: str = "1.0.0"


def get_application_version() -> str:
    """
    Return the global application version.
    """
    return application_version


version_result: str = get_application_version()

print(version_result)


# =============================================================================
# 65. A Function Can Modify a Global Variable and Return It
# =============================================================================

release_number: int = 1


def create_next_release() -> int:
    """
    Increment and return the global release number.
    """
    global release_number

    release_number += 1

    return release_number


release_one: int = create_next_release()
release_two: int = create_next_release()

print(release_one)
print(release_two)


# =============================================================================
# 66. Global State With Several Functions
# =============================================================================

active_users: int = 0


def user_logged_in() -> None:
    """
    Increase the global active-user count.
    """
    global active_users

    active_users += 1


def user_logged_out() -> None:
    """
    Decrease the global active-user count.
    """
    global active_users

    active_users -= 1


user_logged_in()
user_logged_in()
user_logged_in()

print(active_users)

user_logged_out()

print(active_users)


# =============================================================================
# 67. Global State Can Introduce Hidden Dependencies
# =============================================================================

"""
Consider:

    tax_rate = 0.18

    def calculate_tax(amount: float) -> float:
        return amount * tax_rate

The function depends on global tax_rate.

A more explicit design is:

    def calculate_tax(
        amount: float,
        tax_rate: float,
    ) -> float:
        return amount * tax_rate

Now the function's required data is visible in its parameters.
"""


# =============================================================================
# 68. Explicit Tax Calculation
# =============================================================================

def calculate_tax(
    amount: float,
    tax_rate: float,
) -> float:
    """
    Calculate tax using explicit inputs.
    """
    return amount * tax_rate


tax_result: float = calculate_tax(
    1000.0,
    0.18,
)

print(tax_result)


# =============================================================================
# 69. Global Constants Can Still Be Useful
# =============================================================================

STANDARD_TAX_RATE: float = 0.18


def calculate_standard_tax(
    amount: float,
) -> float:
    """
    Calculate tax using a shared module-level constant.
    """
    return amount * STANDARD_TAX_RATE


standard_tax_result: float = calculate_standard_tax(
    1000.0
)

print(standard_tax_result)


# =============================================================================
# 70. Global Mutable State Should Be Used Carefully
# =============================================================================

"""
Global mutable state can make a program harder to reason about.

For example:

    total_requests = 0

    def record_request() -> None:
        global total_requests
        total_requests += 1

Now the function depends on state outside its parameters.

This can make:

    - testing harder
    - debugging harder
    - concurrency more complicated
    - dependencies less obvious
    - function behaviour less predictable

This does not mean global is always bad.

It means global mutable state should have a clear purpose.
"""


# =============================================================================
# 71. Good Use Case: Shared Constant
# =============================================================================

MAX_RETRY_ATTEMPTS: int = 3


def get_max_retry_attempts() -> int:
    """
    Read a shared constant.
    """
    return MAX_RETRY_ATTEMPTS


max_retry_result: int = get_max_retry_attempts()

print(max_retry_result)


# =============================================================================
# 72. Another Good Use Case: Application Configuration
# =============================================================================

APP_NAME: str = "DataPipeline"
APP_VERSION: str = "1.0.0"


def get_application_info() -> str:
    """
    Read application-wide constants.
    """
    return f"{APP_NAME} {APP_VERSION}"


application_info: str = get_application_info()

print(application_info)


# =============================================================================
# 73. Avoid Unnecessary global
# =============================================================================

"""
Avoid writing:

    global value

when the function only needs to read:

    value

For example:

    value = 100

    def get_value() -> int:
        return value

This is correct.

Adding:

    global value

would be unnecessary because no reassignment occurs.
"""


# =============================================================================
# 74. global Is About Names, Not Objects
# =============================================================================

"""
The global keyword controls name binding.

For example:

    values = []

    def add_value() -> None:
        values.append(10)

The function accesses the global name:

    values

and mutates the object referenced by that name.

But:

    def replace_value() -> None:
        global values
        values = []

rebinds the global name to a new object.

Therefore remember:

    mutation
        changes an existing object

    rebinding
        changes what a name refers to

The global keyword matters primarily for rebinding.
"""


# =============================================================================
# 75. Mutation Example
# =============================================================================

global_list: list[int] = []


def mutate_global_list() -> None:
    """
    Mutate the global list.
    """
    global_list.append(10)


mutate_global_list()

print(global_list)


# =============================================================================
# 76. Rebinding Example
# =============================================================================

def rebind_global_list() -> None:
    """
    Rebind the global list.
    """
    global global_list

    global_list = [
        20,
        30,
    ]


rebind_global_list()

print(global_list)


# =============================================================================
# 77. global and Dictionaries
# =============================================================================

user_settings: dict[str, str] = {
    "theme": "light",
}


def update_theme(theme: str) -> None:
    """
    Mutate the global dictionary.
    """
    user_settings["theme"] = theme


update_theme("dark")

print(user_settings)


# =============================================================================
# 78. Rebinding a Dictionary
# =============================================================================

def replace_user_settings() -> None:
    """
    Rebind the global dictionary.
    """
    global user_settings

    user_settings = {
        "theme": "light",
        "language": "English",
    }


replace_user_settings()

print(user_settings)


# =============================================================================
# 79. Global Variable With a Counter Function
# =============================================================================

api_calls: int = 0


def make_api_call() -> int:
    """
    Increment the global API call count.
    """
    global api_calls

    api_calls += 1

    return api_calls


api_call_one: int = make_api_call()
api_call_two: int = make_api_call()
api_call_three: int = make_api_call()

print(api_call_one)
print(api_call_two)
print(api_call_three)


# =============================================================================
# 80. Global Variable With a Reset Function
# =============================================================================

def reset_api_calls() -> None:
    """
    Reset the global API call count.
    """
    global api_calls

    api_calls = 0


reset_api_calls()

print(api_calls)


# =============================================================================
# 81. global and Return Values
# =============================================================================

operation_count: int = 0


def perform_operation() -> int:
    """
    Modify global state and return the new value.
    """
    global operation_count

    operation_count += 1

    return operation_count


operation_one: int = perform_operation()
operation_two: int = perform_operation()

print(operation_one)
print(operation_two)


# =============================================================================
# 82. global and Type Annotations
# =============================================================================

annotated_counter: int = 0


def increment_annotated_counter() -> None:
    """
    Modify an annotated global variable.

    The type annotation belongs to the module-level declaration.
    The global statement tells Python which binding to modify.
    """
    global annotated_counter

    annotated_counter += 1


increment_annotated_counter()

print(annotated_counter)


# =============================================================================
# 83. global and Function Parameters
# =============================================================================

global_multiplier: int = 2


def multiply_using_global(
    value: int,
) -> int:
    """
    Use a global variable together with a local parameter.
    """
    return value * global_multiplier


multiplied_result: int = multiply_using_global(
    10
)

print(multiplied_result)


# =============================================================================
# 84. Reassigning a Global Used With a Parameter
# =============================================================================

global_multiplier = 3


def update_multiplier(
    multiplier: int,
) -> None:
    """
    Update the global multiplier.
    """
    global global_multiplier

    global_multiplier = multiplier


def multiply_with_current_multiplier(
    value: int,
) -> int:
    """
    Multiply using the current global multiplier.
    """
    return value * global_multiplier


update_multiplier(5)

multiplier_result: int = multiply_with_current_multiplier(
    10
)

print(multiplier_result)


# =============================================================================
# 85. Global State and Explicit State
# =============================================================================

"""
Global-state design:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

Explicit-state design:

    def increment(counter: int) -> int:
        return counter + 1

The explicit-state version is generally easier to test because the input
and output are visible.
"""


# =============================================================================
# 86. Explicit Counter Alternative
# =============================================================================

def increment_counter_explicit(
    counter_value: int,
) -> int:
    """
    Increment a counter without global state.
    """
    return counter_value + 1


explicit_counter: int = 0

explicit_counter = increment_counter_explicit(
    explicit_counter
)

explicit_counter = increment_counter_explicit(
    explicit_counter
)

print(explicit_counter)


# =============================================================================
# 87. global and Testing Considerations
# =============================================================================

"""
Global mutable state can affect tests because one test can modify a global
variable and another test can observe the changed value.

For example:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

A test must carefully reset counter between test cases.

Using explicit state:

    def increment(counter: int) -> int:
        return counter + 1

makes each call independent of previous global state.
"""


# =============================================================================
# 88. Practical Example: Global Application Status
# =============================================================================

application_status: str = "stopped"


def start_application_status() -> None:
    """
    Start the application.
    """
    global application_status

    application_status = "running"


def stop_application_status() -> None:
    """
    Stop the application.
    """
    global application_status

    application_status = "stopped"


def get_application_status() -> str:
    """
    Return the current global application status.
    """
    return application_status


start_application_status()

print(get_application_status())

stop_application_status()

print(get_application_status())


# =============================================================================
# 89. Practical Example: Global Request Statistics
# =============================================================================

request_statistics: dict[str, int] = {
    "total": 0,
    "successful": 0,
    "failed": 0,
}


def record_request(success: bool) -> None:
    """
    Update request statistics.

    The dictionary is mutated, so global is not required.
    """
    request_statistics["total"] += 1

    if success:
        request_statistics["successful"] += 1
    else:
        request_statistics["failed"] += 1


record_request(True)
record_request(True)
record_request(False)

print(request_statistics)


# =============================================================================
# 90. Replacing Global Statistics
# =============================================================================

def reset_request_statistics() -> None:
    """
    Replace the global statistics dictionary.
    """
    global request_statistics

    request_statistics = {
        "total": 0,
        "successful": 0,
        "failed": 0,
    }


reset_request_statistics()

print(request_statistics)


# =============================================================================
# 91. Common Mistake: Forgetting global
# =============================================================================

"""
Incorrect pattern:

    counter = 0

    def increment() -> None:
        counter += 1

This results in UnboundLocalError when the function executes.

Correct pattern:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1

This file does not execute the incorrect version so that the complete file
remains free of intentional runtime errors.
"""


# =============================================================================
# 92. Common Mistake: Using global When Reading Only
# =============================================================================

"""
This works:

    value = 100

    def get_value() -> int:
        global value
        return value

But global is unnecessary.

Prefer:

    value = 100

    def get_value() -> int:
        return value

Use global when rebinding is required.
"""


# =============================================================================
# 93. Common Mistake: Confusing Mutation and Rebinding
# =============================================================================

"""
Mutation:

    items.append("Python")

Rebinding:

    items = ["Python"]

For a global list:

    items.append("Python")

does not require global.

But:

    items = ["Python"]

requires global if the function intends to replace the module-level list.
"""


# =============================================================================
# 94. Common Mistake: Confusing global and nonlocal
# =============================================================================

"""
Use global for:

    module-level variables

Use nonlocal for:

    variables belonging to an enclosing function.

Example:

    counter = 0

    def increment_global() -> None:
        global counter
        counter += 1

Example:

    def create_counter() -> Callable[[], int]:
        counter = 0

        def increment() -> int:
            nonlocal counter
            counter += 1
            return counter

        return increment
"""


# =============================================================================
# 95. Common Mistake: Thinking global Copies a Variable
# =============================================================================

"""
global does not copy a variable.

Example:

    value = 10

    def update() -> None:
        global value
        value = 20

There is one module-level binding:

    value

The function is instructed to modify that binding.
"""


# =============================================================================
# 96. Common Mistake: Thinking Called Functions Share Local Variables
# =============================================================================

"""
The following idea is incorrect:

    def first() -> None:
        value = 10
        second()

    def second() -> None:
        print(value)

second() does not automatically receive first()'s local value.

Function calls do not transfer local variables between functions.

If shared state is required, pass it as an argument, return it, use an
object, use a closure, or intentionally use global state.
"""


# =============================================================================
# 97. Better Alternative: Pass the Value
# =============================================================================

def display_value(
    value: int,
) -> None:
    """
    Display a value passed explicitly as an argument.
    """
    print(value)


def create_value_for_display() -> int:
    """
    Create a local value.
    """
    value: int = 100

    return value


value_for_display: int = create_value_for_display()

display_value(
    value_for_display
)


# =============================================================================
# 98. Better Alternative: Return the Updated Value
# =============================================================================

def increment_explicit_value(
    value: int,
) -> int:
    """
    Return an updated value instead of modifying global state.
    """
    return value + 1


value_before: int = 10

value_after: int = increment_explicit_value(
    value_before
)

print(value_before)
print(value_after)


# =============================================================================
# 99. Better Alternative: Use a Class for Shared State
# =============================================================================

class RequestTracker:
    """
    Track request counts without module-level mutable state.
    """

    def __init__(self) -> None:
        """
        Initialize request counts.
        """
        self.total: int = 0
        self.successful: int = 0
        self.failed: int = 0

    def record(self, success: bool) -> None:
        """
        Record one request.
        """
        self.total += 1

        if success:
            self.successful += 1
        else:
            self.failed += 1


tracker: RequestTracker = RequestTracker()

tracker.record(True)
tracker.record(True)
tracker.record(False)

print(tracker.total)
print(tracker.successful)
print(tracker.failed)


# =============================================================================
# 100. Better Alternative: Use a Closure
# =============================================================================

def create_request_counter() -> Callable[[], int]:
    """
    Create a counter using an enclosing variable.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the enclosing counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


request_counter: Callable[[], int] = create_request_counter()

print(request_counter())
print(request_counter())
print(request_counter())


# =============================================================================
# 101. global and Lexical Scope
# =============================================================================

"""
The global keyword does not change the normal LEGB lookup rules for every
name in the function.

It specifically changes the binding target for the declared name.

For example:

    value = 10

    def update() -> None:
        global value
        value = 20

The assignment:

    value = 20

targets the global binding.

Other local variables in the function remain local.
"""


# =============================================================================
# 102. global With Local Variables in the Same Function
# =============================================================================

global_total: int = 100


def calculate_with_global() -> int:
    """
    Use one global variable and one local variable.
    """
    global global_total

    local_amount: int = 25

    global_total += local_amount

    return global_total


global_calculation_result: int = calculate_with_global()

print(global_calculation_result)


# =============================================================================
# 103. global and Local Parameters
# =============================================================================

global_rate: float = 0.18


def calculate_with_rate(
    amount: float,
) -> float:
    """
    Use a local parameter with a global rate.
    """
    tax: float = amount * global_rate

    return tax


rate_result: float = calculate_with_rate(
    1000.0
)

print(rate_result)


# =============================================================================
# 104. Updating the Global Rate
# =============================================================================

def set_global_rate(
    rate: float,
) -> None:
    """
    Update the global rate.
    """
    global global_rate

    global_rate = rate


set_global_rate(0.20)

updated_rate_result: float = calculate_with_rate(
    1000.0
)

print(updated_rate_result)


# =============================================================================
# 105. Practical Global Configuration
# =============================================================================

database_host: str = "localhost"
database_port: int = 5432


def set_database_configuration(
    host: str,
    port: int,
) -> None:
    """
    Update global database configuration.
    """
    global database_host, database_port

    database_host = host
    database_port = port


def get_database_configuration() -> str:
    """
    Return the current database configuration.
    """
    return f"{database_host}:{database_port}"


set_database_configuration(
    "database.example.com",
    5432,
)

database_configuration: str = get_database_configuration()

print(database_configuration)


# =============================================================================
# 106. Global State Is Module-Level State
# =============================================================================

"""
A global variable in a Python module is generally a module-level name.

For example:

    application_name = "DataPipeline"

The name application_name belongs to the module namespace.

A function can read it through normal name resolution.

If a function needs to rebind it, global is used:

    def rename_application() -> None:
        global application_name
        application_name = "NewName"
"""


# =============================================================================
# 107. global and Module-Level Names
# =============================================================================

module_name: str = "scope_demo"


def rename_module_name() -> None:
    """
    Rebind a module-level name.
    """
    global module_name

    module_name = "global_keyword_demo"


rename_module_name()

print(module_name)


# =============================================================================
# 108. global Does Not Make a Variable Constant
# =============================================================================

"""
Python does not have a special constant keyword.

Uppercase names are a convention:

    MAX_RETRIES = 3

The global keyword is unrelated to constants.

For example:

    global value

means:

    use the module-level binding named value.

It does not mean:

    make value permanent

or:

    make value immutable.
"""


# =============================================================================
# 109. global With an Immutable Object
# =============================================================================

global_integer: int = 10


def replace_global_integer() -> None:
    """
    Rebind a global integer.
    """
    global global_integer

    global_integer = 20


replace_global_integer()

print(global_integer)


# =============================================================================
# 110. global With a Mutable Object
# =============================================================================

global_dictionary: dict[str, int] = {
    "count": 0,
}


def increment_dictionary_count() -> None:
    """
    Mutate a value inside the global dictionary.
    """
    global_dictionary["count"] += 1


increment_dictionary_count()
increment_dictionary_count()

print(global_dictionary)


# =============================================================================
# 111. Rebinding the Mutable Object
# =============================================================================

def replace_global_dictionary() -> None:
    """
    Replace the global dictionary object.
    """
    global global_dictionary

    global_dictionary = {
        "count": 100,
    }


replace_global_dictionary()

print(global_dictionary)


# =============================================================================
# 112. Scope Rule: Assignment Is Local by Default
# =============================================================================

"""
The most important rule to remember is:

    Assignment inside a function creates a local name by default.

Example:

    value = 10

    def example() -> None:
        value = 20

The function creates a local value.

The global value remains:

    10

To change the global value:

    def example() -> None:
        global value
        value = 20
"""


# =============================================================================
# 113. Scope Rule: Reading Is Different From Assignment
# =============================================================================

read_only_value: int = 500


def read_value_without_global() -> int:
    """
    Read a global value.
    """
    return read_only_value


read_only_result: int = read_value_without_global()

print(read_only_result)


# =============================================================================
# 114. Scope Rule: Rebinding Requires global
# =============================================================================

rebind_value: int = 500


def rebind_value_globally() -> None:
    """
    Rebind a global name.
    """
    global rebind_value

    rebind_value = 1000


rebind_value_globally()

print(rebind_value)


# =============================================================================
# 115. Scope Rule: Mutation Usually Does Not Require global
# =============================================================================

mutable_state: list[int] = []


def mutate_state() -> None:
    """
    Mutate the existing global list.
    """
    mutable_state.append(1)


mutate_state()

print(mutable_state)


# =============================================================================
# 116. Scope Rule: Rebinding Requires global
# =============================================================================

def rebind_state() -> None:
    """
    Rebind the global list.
    """
    global mutable_state

    mutable_state = [
        10,
        20,
    ]


rebind_state()

print(mutable_state)


# =============================================================================
# 117. Global Keyword Checklist
# =============================================================================

"""
Before using global, ask:

    1. Am I only reading the variable?
       -> global is not required.

    2. Am I mutating an existing object?
       -> global is usually not required.

    3. Am I assigning a new value to the global name?
       -> global is required.

    4. Am I using +=, -=, *=, or similar reassignment?
       -> global is required for a global name.

    5. Is the variable actually in an enclosing function?
       -> use nonlocal instead.

    6. Could I pass the value as a parameter?
       -> consider doing that.

    7. Could I return the updated value?
       -> consider doing that.

    8. Would a class or closure better represent the state?
       -> consider using one.
"""


# =============================================================================
# 118. Complete global Example
# =============================================================================

inventory_count: int = 0


def add_inventory(amount: int) -> None:
    """
    Add inventory using global state.
    """
    global inventory_count

    inventory_count += amount


def remove_inventory(amount: int) -> None:
    """
    Remove inventory using global state.
    """
    global inventory_count

    inventory_count -= amount


def get_inventory() -> int:
    """
    Read the global inventory count.
    """
    return inventory_count


add_inventory(100)
remove_inventory(25)

current_inventory: int = get_inventory()

print(current_inventory)


# =============================================================================
# 119. Complete Configuration Example
# =============================================================================

service_name: str = "DataService"
service_enabled: bool = False
service_port: int = 8080


def configure_service(
    name: str,
    port: int,
) -> None:
    """
    Update global service configuration.
    """
    global service_name, service_port

    service_name = name
    service_port = port


def enable_service() -> None:
    """
    Enable the service.
    """
    global service_enabled

    service_enabled = True


def disable_service() -> None:
    """
    Disable the service.
    """
    global service_enabled

    service_enabled = False


def get_service_configuration() -> str:
    """
    Return the current service configuration.
    """
    status: str = "enabled" if service_enabled else "disabled"

    return (
        f"name={service_name}, "
        f"port={service_port}, "
        f"status={status}"
    )


configure_service(
    "ProductionDataService",
    9000,
)

enable_service()

print(get_service_configuration())

disable_service()

print(get_service_configuration())


# =============================================================================
# 120. Final Scope Model
# =============================================================================

"""
The global keyword is about assignment targets.

Without global:

    value = 10

    def update() -> None:
        value = 20

the assignment creates a local variable.

With global:

    value = 10

    def update() -> None:
        global value
        value = 20

the assignment modifies the module-level variable.

The core distinction is:

    READ
        ↓
    global usually not required

    MUTATE EXISTING OBJECT
        ↓
    global usually not required

    REBIND GLOBAL NAME
        ↓
    global required


Example:

    items = []

    def mutate() -> None:
        items.append("Python")

No global required.

Example:

    items = []

    def replace() -> None:
        global items
        items = ["Python"]

global required.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
✓ The global keyword refers to a module-level/global name.

✓ Reading a global variable does not require global.

✓ Assignment inside a function creates a local variable by default.

✓ The global keyword changes the assignment target to global scope.

✓ +=, -=, *=, and similar operations count as rebinding operations.

✓ Forgetting global when rebinding a global variable can cause
  UnboundLocalError.

✓ global is not required merely to read a global variable.

✓ global is usually not required when mutating a global mutable object.

✓ Rebinding a global list requires global.

✓ Rebinding a global dictionary requires global.

✓ global does not copy a variable.

✓ global does not make a variable constant.

✓ global does not make an object immutable.

✓ global and nonlocal solve different problems.

✓ global refers to module/global scope.

✓ nonlocal refers to the nearest enclosing function scope.

✓ Excessive global mutable state can make programs harder to test and
  maintain.

✓ Parameters and return values usually provide clearer data flow.

✓ Classes can encapsulate mutable state.

✓ Closures can encapsulate state using nonlocal.

Core model:

    GLOBAL VARIABLE
          ↓
    function reads it
          ↓
    global NOT required


    GLOBAL VARIABLE
          ↓
    function mutates existing object
          ↓
    global usually NOT required


    GLOBAL VARIABLE
          ↓
    function reassigns the name
          ↓
    global REQUIRED


Example:

    counter = 0

    def increment() -> None:
        global counter
        counter += 1


Remember:

    global
        ↓
    rebind a module-level name


    nonlocal
        ↓
    rebind an enclosing function name


    parameter
        ↓
    receive explicit input


    return
        ↓
    send explicit output
"""


# =============================================================================
# End of 11_global_keyword.py
# =============================================================================