# =============================================================================
# 12. nonlocal Keyword
# =============================================================================
# type: ignore
"""
Python Functions

File
----
12_nonlocal_keyword.py

Topic
-----
nonlocal Keyword

Overview
--------
The nonlocal keyword is used inside a nested function when the nested
function needs to rebind a variable that belongs to an enclosing function
scope.

The nonlocal keyword does not refer to global scope.

The core relationship is:

    Local
       ↓
    Enclosing
       ↓
    Global
       ↓
    Built-in

The nonlocal keyword allows a nested function to modify a name found in
an enclosing function scope.

Topics covered
--------------
- What is nonlocal?
- Why nonlocal exists
- Local scope versus enclosing scope
- Reading an enclosing variable
- Modifying an enclosing variable
- Assignment without nonlocal
- Assignment with nonlocal
- Basic nonlocal example
- Nested functions
- Closures
- Function factories
- Stateful functions
- Counters
- Accumulators
- Configuration closures
- Multiple enclosing scopes
- Nearest enclosing scope
- nonlocal versus global
- nonlocal versus local
- nonlocal and mutable objects
- Mutation versus rebinding
- nonlocal with strings
- nonlocal with integers
- nonlocal with floats
- nonlocal with booleans
- nonlocal with lists
- nonlocal with dictionaries
- nonlocal with sets
- nonlocal with tuples
- nonlocal with objects
- nonlocal with type annotations
- nonlocal with multiple variables
- nonlocal in closures
- nonlocal and function factories
- nonlocal and decorators
- nonlocal and callbacks
- nonlocal and state
- common mistakes
- NameError
- UnboundLocalError
- SyntaxError
- practical design patterns
- best practices
- complete summary
"""

# =============================================================================
# 01. What Is nonlocal?
# =============================================================================
"""
The nonlocal keyword tells Python that an assignment inside a nested
function should modify a variable from an enclosing function scope.

Example:

    def outer() -> None:
        value: int = 10

        def inner() -> None:
            nonlocal value
            value = 20

The inner function modifies value belonging to outer().

Without nonlocal, Python would normally treat an assignment to value
inside inner() as a local assignment.
"""

# =============================================================================
# 02. Basic nonlocal Example
# =============================================================================


def create_counter() -> callable:
    """
    Create a counter function.

    The counter function uses nonlocal to modify the enclosing
    count variable.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the enclosing count.
        """
        nonlocal count

        count += 1

        return count

    return increment


counter = create_counter()

counter_value_1: int = counter()
counter_value_2: int = counter()
counter_value_3: int = counter()

print(counter_value_1)
print(counter_value_2)
print(counter_value_3)


# =============================================================================
# 03. Why nonlocal Is Needed
# =============================================================================
"""
Consider:

    def outer() -> None:
        value: int = 10

        def inner() -> None:
            value = 20

The assignment:

    value = 20

creates a local variable named value inside inner().

It does not modify outer()'s value.

The nonlocal keyword changes this behavior:

    def outer() -> None:
        value: int = 10

        def inner() -> None:
            nonlocal value
            value = 20

Now value refers to the variable from the enclosing function scope.
"""

# =============================================================================
# 04. Reading an Enclosing Variable Does Not Require nonlocal
# =============================================================================


def read_enclosing_value() -> int:
    """
    Read a value from an enclosing function scope.
    """
    value: int = 100

    def read_value() -> int:
        """
        Read the enclosing value.
        """
        return value

    return read_value()


enclosing_value: int = read_enclosing_value()

print(enclosing_value)


# =============================================================================
# 05. nonlocal Is Required for Rebinding
# =============================================================================


def update_enclosing_value() -> int:
    """
    Modify an enclosing variable using nonlocal.
    """
    value: int = 100

    def update_value() -> int:
        """
        Rebind the enclosing value.
        """
        nonlocal value

        value = 200

        return value

    return update_value()


updated_value: int = update_enclosing_value()

print(updated_value)


# =============================================================================
# 06. Local Assignment Without nonlocal
# =============================================================================


def local_assignment_example() -> int:
    """
    Demonstrate local assignment inside a nested function.
    """
    value: int = 100

    def change_value() -> int:
        """
        Create a new local value instead of modifying the enclosing value.
        """
        value: int = 200

        return value

    changed_value: int = change_value()

    return value + changed_value


local_assignment_result: int = local_assignment_example()

print(local_assignment_result)


# =============================================================================
# 07. Assignment With nonlocal
# =============================================================================


def nonlocal_assignment_example() -> int:
    """
    Demonstrate assignment using nonlocal.
    """
    value: int = 100

    def change_value() -> int:
        """
        Modify the enclosing value.
        """
        nonlocal value

        value = 200

        return value

    return change_value()


nonlocal_assignment_result: int = nonlocal_assignment_example()

print(nonlocal_assignment_result)


# =============================================================================
# 08. Local Versus Enclosing Scope
# =============================================================================


def demonstrate_local_and_enclosing() -> tuple[int, int]:
    """
    Demonstrate separate local and enclosing variables.
    """
    value: int = 10

    def inner() -> int:
        """
        Create a separate local value.
        """
        value: int = 20

        return value

    inner_value: int = inner()

    return value, inner_value


outer_value, inner_value = demonstrate_local_and_enclosing()

print(outer_value)
print(inner_value)


# =============================================================================
# 09. nonlocal Changes the Enclosing Variable
# =============================================================================


def demonstrate_nonlocal_change() -> int:
    """
    Demonstrate modification of an enclosing variable.
    """
    value: int = 10

    def inner() -> None:
        """
        Modify the enclosing variable.
        """
        nonlocal value

        value = 50

    inner()

    return value


changed_enclosing_value: int = demonstrate_nonlocal_change()

print(changed_enclosing_value)


# =============================================================================
# 10. Multiple Calls Share Enclosing State
# =============================================================================


def create_shared_counter() -> callable:
    """
    Create a stateful counter.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the shared enclosing count.
        """
        nonlocal count

        count += 1

        return count

    return increment


shared_counter = create_shared_counter()

print(shared_counter())
print(shared_counter())
print(shared_counter())
print(shared_counter())


# =============================================================================
# 11. Separate Closures Have Separate State
# =============================================================================


def create_independent_counter() -> callable:
    """
    Create an independent counter.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment this counter's state.
        """
        nonlocal count

        count += 1

        return count

    return increment


first_counter = create_independent_counter()
second_counter = create_independent_counter()

print(first_counter())
print(first_counter())

print(second_counter())
print(second_counter())


# =============================================================================
# 12. Counter Factory
# =============================================================================


def make_counter(start: int = 0) -> callable:
    """
    Create a counter starting from a supplied value.
    """
    count: int = start

    def increment() -> int:
        """
        Increment the counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


counter_from_zero = make_counter()
counter_from_hundred = make_counter(100)

print(counter_from_zero())
print(counter_from_zero())

print(counter_from_hundred())
print(counter_from_hundred())


# =============================================================================
# 13. Accumulator
# =============================================================================


def create_accumulator() -> callable:
    """
    Create an accumulator function.
    """
    total: int = 0

    def add(value: int) -> int:
        """
        Add a value to the enclosing total.
        """
        nonlocal total

        total += value

        return total

    return add


accumulate = create_accumulator()

print(accumulate(10))
print(accumulate(20))
print(accumulate(30))


# =============================================================================
# 14. String State
# =============================================================================


def create_message_store() -> callable:
    """
    Create a function that stores a string.
    """
    message: str = ""

    def set_message(new_message: str) -> str:
        """
        Replace the enclosing message.
        """
        nonlocal message

        message = new_message

        return message

    return set_message


message_store = create_message_store()

print(message_store("Hello"))
print(message_store("Python"))
print(message_store("Functions"))


# =============================================================================
# 15. Integer State
# =============================================================================


def create_integer_updater() -> callable:
    """
    Create an integer state updater.
    """
    value: int = 0

    def update(amount: int) -> int:
        """
        Modify the enclosing integer.
        """
        nonlocal value

        value += amount

        return value

    return update


integer_updater = create_integer_updater()

print(integer_updater(5))
print(integer_updater(10))
print(integer_updater(-3))


# =============================================================================
# 16. Float State
# =============================================================================


def create_balance() -> callable:
    """
    Create a balance updater.
    """
    balance: float = 0.0

    def change(amount: float) -> float:
        """
        Modify the enclosing balance.
        """
        nonlocal balance

        balance += amount

        return balance

    return change


balance = create_balance()

print(balance(100.0))
print(balance(50.5))
print(balance(-25.0))


# =============================================================================
# 17. Boolean State
# =============================================================================


def create_toggle() -> callable:
    """
    Create a toggle function.
    """
    enabled: bool = False

    def toggle() -> bool:
        """
        Toggle the enclosing boolean.
        """
        nonlocal enabled

        enabled = not enabled

        return enabled

    return toggle


toggle = create_toggle()

print(toggle())
print(toggle())
print(toggle())
print(toggle())


# =============================================================================
# 18. List Mutation Does Not Require nonlocal
# =============================================================================


def create_list_store() -> callable:
    """
    Create a function that mutates an enclosing list.
    """
    values: list[int] = []

    def add(value: int) -> list[int]:
        """
        Mutate the existing list.
        """
        values.append(value)

        return values.copy()

    return add


list_store = create_list_store()

print(list_store(10))
print(list_store(20))
print(list_store(30))


# =============================================================================
# 19. Rebinding a List Requires nonlocal
# =============================================================================


def create_list_replacer() -> callable:
    """
    Create a function that replaces an enclosing list.
    """
    values: list[int] = []

    def replace(new_values: list[int]) -> list[int]:
        """
        Rebind the enclosing list.
        """
        nonlocal values

        values = new_values.copy()

        return values.copy()

    return replace


list_replacer = create_list_replacer()

print(list_replacer([1, 2, 3]))
print(list_replacer([10, 20]))


# =============================================================================
# 20. Mutation Versus Rebinding
# =============================================================================
"""
Mutation:

    values.append(10)

changes the existing list object.

Rebinding:

    values = [10]

changes what the name values refers to.

Mutation does not require nonlocal.

Rebinding requires nonlocal when the name belongs to an enclosing
function scope.
"""


def demonstrate_mutation() -> list[int]:
    """
    Demonstrate mutation without nonlocal.
    """
    values: list[int] = []

    def add_value() -> None:
        """
        Mutate the existing list.
        """
        values.append(10)

    add_value()

    return values


mutated_values: list[int] = demonstrate_mutation()

print(mutated_values)


# =============================================================================
# 21. Dictionary Mutation
# =============================================================================


def create_dictionary_store() -> callable:
    """
    Create a dictionary-backed state store.
    """
    data: dict[str, int] = {}

    def set_value(key: str, value: int) -> dict[str, int]:
        """
        Mutate the existing dictionary.
        """
        data[key] = value

        return data.copy()

    return set_value


dictionary_store = create_dictionary_store()

print(dictionary_store("python", 10))
print(dictionary_store("sql", 20))


# =============================================================================
# 22. Dictionary Rebinding
# =============================================================================


def create_dictionary_replacer() -> callable:
    """
    Create a dictionary replacement function.
    """
    data: dict[str, int] = {}

    def replace(new_data: dict[str, int]) -> dict[str, int]:
        """
        Replace the enclosing dictionary.
        """
        nonlocal data

        data = new_data.copy()

        return data.copy()

    return replace


dictionary_replacer = create_dictionary_replacer()

print(dictionary_replacer({"python": 1}))
print(dictionary_replacer({"sql": 2}))


# =============================================================================
# 23. Set Mutation
# =============================================================================


def create_set_store() -> callable:
    """
    Create a set-backed state store.
    """
    values: set[str] = set()

    def add(value: str) -> set[str]:
        """
        Mutate the existing set.
        """
        values.add(value)

        return values.copy()

    return add


set_store = create_set_store()

print(set_store("Python"))
print(set_store("SQL"))


# =============================================================================
# 24. Set Rebinding
# =============================================================================


def create_set_replacer() -> callable:
    """
    Create a function that replaces an enclosing set.
    """
    values: set[str] = set()

    def replace(new_values: set[str]) -> set[str]:
        """
        Rebind the enclosing set.
        """
        nonlocal values

        values = new_values.copy()

        return values.copy()

    return replace


set_replacer = create_set_replacer()

print(set_replacer({"Python", "SQL"}))
print(set_replacer({"Go", "Rust"}))


# =============================================================================
# 25. Tuple Rebinding
# =============================================================================


def create_tuple_updater() -> callable:
    """
    Create a function that replaces an enclosing tuple.
    """
    values: tuple[int, ...] = ()

    def update(new_values: tuple[int, ...]) -> tuple[int, ...]:
        """
        Rebind the enclosing tuple.
        """
        nonlocal values

        values = new_values

        return values

    return update


tuple_updater = create_tuple_updater()

print(tuple_updater((1, 2, 3)))
print(tuple_updater((10, 20)))


# =============================================================================
# 26. Multiple nonlocal Variables
# =============================================================================


def create_state_manager() -> callable:
    """
    Create a state manager with multiple enclosing variables.
    """
    count: int = 0
    total: float = 0.0

    def update(value: float) -> tuple[int, float]:
        """
        Update multiple enclosing variables.
        """
        nonlocal count, total

        count += 1
        total += value

        return count, total

    return update


state_manager = create_state_manager()

print(state_manager(10.0))
print(state_manager(20.0))
print(state_manager(30.0))


# =============================================================================
# 27. nonlocal With Type Annotations
# =============================================================================


def create_typed_counter() -> callable:
    """
    Create a typed counter.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the typed enclosing variable.
        """
        nonlocal count

        count += 1

        return count

    return increment


typed_counter = create_typed_counter()

print(typed_counter())
print(typed_counter())


# =============================================================================
# 28. nonlocal With Multiple Types
# =============================================================================


def create_application_state() -> callable:
    """
    Create application state with multiple types.
    """
    username: str = "Guest"
    logged_in: bool = False

    def login(name: str) -> tuple[str, bool]:
        """
        Update the username and login state.
        """
        nonlocal username, logged_in

        username = name
        logged_in = True

        return username, logged_in

    return login


application_login = create_application_state()

print(application_login("Alex"))
print(application_login("Jordan"))


# =============================================================================
# 29. Resettable Counter
# =============================================================================


def create_resettable_counter() -> callable:
    """
    Create a counter that can increment and reset.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the counter.
        """
        nonlocal count

        count += 1

        return count

    def reset() -> int:
        """
        Reset the counter.
        """
        nonlocal count

        count = 0

        return count

    def get_count() -> int:
        """
        Read the current counter value.
        """
        return count

    def operation() -> int:
        """
        Demonstrate the current state.
        """
        return get_count()

    increment()
    increment()

    reset()

    return operation()


resettable_result: int = create_resettable_counter()

print(resettable_result)


# =============================================================================
# 30. Better Resettable Counter Factory
# =============================================================================


def create_counter_with_reset() -> tuple[callable, callable]:
    """
    Create increment and reset functions sharing one state.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the counter.
        """
        nonlocal count

        count += 1

        return count

    def reset() -> int:
        """
        Reset the counter.
        """
        nonlocal count

        count = 0

        return count

    return increment, reset


increment_counter, reset_counter = create_counter_with_reset()

print(increment_counter())
print(increment_counter())
print(reset_counter())
print(increment_counter())


# =============================================================================
# 31. Getter and Setter Closure
# =============================================================================


def create_value_container() -> tuple[callable, callable]:
    """
    Create getter and setter functions sharing one value.
    """
    value: int = 0

    def get_value() -> int:
        """
        Return the current value.
        """
        return value

    def set_value(new_value: int) -> None:
        """
        Replace the current value.
        """
        nonlocal value

        value = new_value

    return get_value, set_value


get_value, set_value = create_value_container()

print(get_value())

set_value(100)

print(get_value())


# =============================================================================
# 32. Function Factory
# =============================================================================


def create_multiplier(multiplier: float) -> callable:
    """
    Create a multiplication function.
    """

    def multiply(number: float) -> float:
        """
        Multiply using the enclosing multiplier.
        """
        return number * multiplier

    return multiply


double = create_multiplier(2.0)
triple = create_multiplier(3.0)

print(double(10.0))
print(triple(10.0))


# =============================================================================
# 33. Function Factory With Mutable State
# =============================================================================


def create_running_total() -> callable:
    """
    Create a function that remembers a running total.
    """
    total: float = 0.0

    def add(value: float) -> float:
        """
        Add to the running total.
        """
        nonlocal total

        total += value

        return total

    return add


running_total = create_running_total()

print(running_total(10.0))
print(running_total(5.0))
print(running_total(20.0))


# =============================================================================
# 34. Closure Definition
# =============================================================================
"""
A closure is a function that remembers values from its enclosing scope.

Example:

    def create_multiplier(multiplier: float) -> callable:
        def multiply(number: float) -> float:
            return number * multiplier

        return multiply

The returned multiply function remembers multiplier.

nonlocal becomes useful when that remembered enclosing state must be
modified.
"""


# =============================================================================
# 35. Closure With nonlocal
# =============================================================================


def create_score_tracker() -> callable:
    """
    Create a score tracker using a closure.
    """
    score: int = 0

    def add_points(points: int) -> int:
        """
        Add points to the remembered score.
        """
        nonlocal score

        score += points

        return score

    return add_points


score_tracker = create_score_tracker()

print(score_tracker(10))
print(score_tracker(25))
print(score_tracker(15))


# =============================================================================
# 36. Separate Closure State
# =============================================================================


first_score_tracker = create_score_tracker()
second_score_tracker = create_score_tracker()

print(first_score_tracker(100))
print(second_score_tracker(50))

print(first_score_tracker(20))
print(second_score_tracker(25))


# =============================================================================
# 37. nonlocal Versus global
# =============================================================================
"""
global refers to module/global scope.

nonlocal refers to an enclosing function scope.

Example of global:

    counter: int = 0

    def increment() -> None:
        global counter
        counter += 1

Example of nonlocal:

    def create_counter() -> callable:
        counter: int = 0

        def increment() -> None:
            nonlocal counter
            counter += 1

        return increment

The two keywords solve different problems.
"""


# =============================================================================
# 38. global Example
# =============================================================================


global_counter: int = 0


def increment_global_counter() -> int:
    """
    Modify a global counter.
    """
    global global_counter

    global_counter += 1

    return global_counter


print(increment_global_counter())
print(increment_global_counter())


# =============================================================================
# 39. nonlocal Example
# =============================================================================


def create_nonlocal_counter() -> callable:
    """
    Create a counter using an enclosing variable.
    """
    count: int = 0

    def increment() -> int:
        """
        Modify the enclosing counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


nonlocal_counter = create_nonlocal_counter()

print(nonlocal_counter())
print(nonlocal_counter())


# =============================================================================
# 40. nonlocal Does Not Refer to Global Scope
# =============================================================================
"""
This is invalid:

    value: int = 10

    def outer() -> None:
        def inner() -> None:
            nonlocal value

There is no enclosing function scope containing value.

value exists in global scope.

For global scope, use:

    global value

For an enclosing function scope, use:

    nonlocal value
"""


# =============================================================================
# 41. Nearest Enclosing Scope
# =============================================================================


def demonstrate_nearest_enclosing_scope() -> str:
    """
    Demonstrate that nonlocal selects the nearest enclosing binding.
    """
    value: str = "outer"

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


nearest_scope_result: str = demonstrate_nearest_enclosing_scope()

print(nearest_scope_result)


# =============================================================================
# 42. Multiple Enclosing Scopes
# =============================================================================


def multiple_enclosing_levels() -> tuple[str, str]:
    """
    Demonstrate multiple enclosing scopes.
    """
    outer_value: str = "outer"

    def middle() -> tuple[str, str]:
        """
        Create a middle scope.
        """
        middle_value: str = "middle"

        def inner() -> tuple[str, str]:
            """
            Read both enclosing variables.
            """
            return outer_value, middle_value

        return inner()

    return middle()


multiple_scope_values: tuple[str, str] = multiple_enclosing_levels()

print(multiple_scope_values)


# =============================================================================
# 43. nonlocal Selects the Nearest Binding
# =============================================================================


def nearest_nonlocal_binding() -> str:
    """
    Demonstrate nearest enclosing binding selection.
    """
    value: str = "outer"

    def middle() -> str:
        """
        Define another value with the same name.
        """
        value: str = "middle"

        def inner() -> str:
            """
            Modify the nearest enclosing value.
            """
            nonlocal value

            value = "inner changed"

            return value

        return inner()

    outer_result: str = middle()

    return f"outer={value}; middle={outer_result}"


nearest_binding_result: str = nearest_nonlocal_binding()

print(nearest_binding_result)


# =============================================================================
# 44. nonlocal Does Not Skip to Global
# =============================================================================


global_value: str = "global"


def demonstrate_nonlocal_search() -> str:
    """
    Demonstrate that nonlocal searches enclosing functions.
    """
    local_value: str = "outer"

    def inner() -> str:
        """
        Modify the enclosing local_value.
        """
        nonlocal local_value

        local_value = "changed"

        return local_value

    return inner()


nonlocal_search_result: str = demonstrate_nonlocal_search()

print(global_value)
print(nonlocal_search_result)


# =============================================================================
# 45. Reading Before Rebinding
# =============================================================================


def read_then_modify() -> int:
    """
    Read an enclosing value before modifying it.
    """
    value: int = 10

    def modify() -> int:
        """
        Read and then modify the enclosing value.
        """
        nonlocal value

        old_value: int = value
        value += 5

        return old_value

    return modify()


old_value_result: int = read_then_modify()

print(old_value_result)


# =============================================================================
# 46. Returning the Updated Value
# =============================================================================


def create_incrementer() -> callable:
    """
    Create an incrementing function.
    """
    value: int = 0

    def increment() -> int:
        """
        Increment and return the updated value.
        """
        nonlocal value

        value += 1

        return value

    return increment


incrementer = create_incrementer()

incremented_value_1: int = incrementer()
incremented_value_2: int = incrementer()
incremented_value_3: int = incrementer()

print(incremented_value_1)
print(incremented_value_2)
print(incremented_value_3)


# =============================================================================
# 47. Previous Value and New Value
# =============================================================================


def create_value_updater() -> callable:
    """
    Create an updater that returns old and new values.
    """
    value: int = 0

    def update(amount: int) -> tuple[int, int]:
        """
        Return both the previous and updated values.
        """
        nonlocal value

        previous_value: int = value
        value += amount

        return previous_value, value

    return update


value_updater = create_value_updater()

print(value_updater(10))
print(value_updater(20))
print(value_updater(-5))


# =============================================================================
# 48. nonlocal With Strings
# =============================================================================


def create_name_updater() -> callable:
    """
    Create a function that updates a remembered name.
    """
    name: str = "Guest"

    def update_name(new_name: str) -> str:
        """
        Replace the enclosing name.
        """
        nonlocal name

        name = new_name

        return name

    return update_name


name_updater = create_name_updater()

print(name_updater("Alex"))
print(name_updater("Jordan"))


# =============================================================================
# 49. nonlocal With Floats
# =============================================================================


def create_percentage_tracker() -> callable:
    """
    Create a percentage tracker.
    """
    percentage: float = 0.0

    def update(amount: float) -> float:
        """
        Update the enclosing percentage.
        """
        nonlocal percentage

        percentage += amount

        return percentage

    return update


percentage_tracker = create_percentage_tracker()

print(percentage_tracker(10.0))
print(percentage_tracker(25.5))
print(percentage_tracker(5.0))


# =============================================================================
# 50. nonlocal With Booleans
# =============================================================================


def create_status_controller() -> callable:
    """
    Create a boolean status controller.
    """
    active: bool = False

    def set_active(value: bool) -> bool:
        """
        Update the enclosing status.
        """
        nonlocal active

        active = value

        return active

    return set_active


status_controller = create_status_controller()

print(status_controller(True))
print(status_controller(False))
print(status_controller(True))


# =============================================================================
# 51. nonlocal With Lists
# =============================================================================


def create_number_collection() -> callable:
    """
    Create a collection function.
    """
    numbers: list[int] = []

    def add_number(number: int) -> list[int]:
        """
        Mutate the enclosing list.
        """
        numbers.append(number)

        return numbers.copy()

    return add_number


number_collection = create_number_collection()

print(number_collection(10))
print(number_collection(20))
print(number_collection(30))


# =============================================================================
# 52. Replacing a List With nonlocal
# =============================================================================


def create_collection_replacer() -> callable:
    """
    Create a collection replacement function.
    """
    numbers: list[int] = []

    def replace_numbers(new_numbers: list[int]) -> list[int]:
        """
        Replace the enclosing list.
        """
        nonlocal numbers

        numbers = new_numbers.copy()

        return numbers.copy()

    return replace_numbers


collection_replacer = create_collection_replacer()

print(collection_replacer([1, 2]))
print(collection_replacer([10, 20, 30]))


# =============================================================================
# 53. nonlocal With Dictionaries
# =============================================================================


def create_configuration() -> callable:
    """
    Create a configuration updater.
    """
    configuration: dict[str, str] = {
        "environment": "development",
    }

    def set_environment(environment: str) -> dict[str, str]:
        """
        Replace one configuration value.
        """
        configuration["environment"] = environment

        return configuration.copy()

    return set_environment


configuration_updater = create_configuration()

print(configuration_updater("testing"))
print(configuration_updater("production"))


# =============================================================================
# 54. Rebinding a Dictionary
# =============================================================================


def create_configuration_replacer() -> callable:
    """
    Create a configuration replacement function.
    """
    configuration: dict[str, str] = {}

    def replace(
        new_configuration: dict[str, str],
    ) -> dict[str, str]:
        """
        Replace the enclosing dictionary.
        """
        nonlocal configuration

        configuration = new_configuration.copy()

        return configuration.copy()

    return replace


configuration_replacer = create_configuration_replacer()

print(configuration_replacer({"mode": "development"}))
print(configuration_replacer({"mode": "production"}))


# =============================================================================
# 55. nonlocal With Objects
# =============================================================================


class CounterState:
    """
    Store counter state in an object.
    """

    def __init__(self) -> None:
        """
        Initialize counter state.
        """
        self.value: int = 0


def create_object_counter() -> callable:
    """
    Create a counter using an enclosing object.
    """
    state = CounterState()

    def increment() -> int:
        """
        Mutate the object stored in the enclosing scope.
        """
        state.value += 1

        return state.value

    return increment


object_counter = create_object_counter()

print(object_counter())
print(object_counter())


# =============================================================================
# 56. Object Mutation Does Not Need nonlocal
# =============================================================================
"""
When state is an object and the nested function modifies an attribute:

    state.value += 1

the name state itself is not rebound.

The object is mutated.

Therefore nonlocal is not required.

Compare:

    state.value += 1

with:

    state = CounterState()

The second statement rebinds the name state and therefore requires
nonlocal if state belongs to an enclosing function.
"""


# =============================================================================
# 57. Rebinding an Object Requires nonlocal
# =============================================================================


def create_replaceable_object() -> callable:
    """
    Create a function that can replace an object.
    """
    state = CounterState()

    def replace() -> int:
        """
        Replace the enclosing object.
        """
        nonlocal state

        state = CounterState()
        state.value = 100

        return state.value

    return replace


object_replacer = create_replaceable_object()

print(object_replacer())


# =============================================================================
# 58. nonlocal With Multiple Nested Functions
# =============================================================================


def create_shared_state_functions() -> tuple[callable, callable]:
    """
    Create multiple functions sharing one enclosing variable.
    """
    value: int = 0

    def increment() -> int:
        """
        Increment shared state.
        """
        nonlocal value

        value += 1

        return value

    def decrement() -> int:
        """
        Decrement shared state.
        """
        nonlocal value

        value -= 1

        return value

    return increment, decrement


increment_shared, decrement_shared = create_shared_state_functions()

print(increment_shared())
print(increment_shared())
print(decrement_shared())
print(decrement_shared())


# =============================================================================
# 59. Getter and Setter
# =============================================================================


def create_private_value() -> tuple[callable, callable]:
    """
    Create getter and setter functions.
    """
    value: str = "initial"

    def get() -> str:
        """
        Get the current value.
        """
        return value

    def set_value(new_value: str) -> None:
        """
        Set a new value.
        """
        nonlocal value

        value = new_value

    return get, set_value


get_private_value, set_private_value = create_private_value()

print(get_private_value())

set_private_value("updated")

print(get_private_value())


# =============================================================================
# 60. Closure-Based Configuration
# =============================================================================


def create_logger(prefix: str) -> callable:
    """
    Create a logger function using an enclosing prefix.
    """

    def log(message: str) -> str:
        """
        Create a prefixed log message.
        """
        return f"{prefix}: {message}"

    return log


info_logger = create_logger("INFO")
error_logger = create_logger("ERROR")

print(info_logger("Application started"))
print(error_logger("Application failed"))


# =============================================================================
# 61. Mutable Configuration With nonlocal
# =============================================================================


def create_log_controller() -> callable:
    """
    Create a log controller with mutable configuration.
    """
    prefix: str = "INFO"

    def set_prefix(new_prefix: str) -> str:
        """
        Change the enclosing prefix.
        """
        nonlocal prefix

        prefix = new_prefix

        return prefix

    return set_prefix


log_controller = create_log_controller()

print(log_controller("DEBUG"))
print(log_controller("ERROR"))


# =============================================================================
# 62. Stateful Function
# =============================================================================


def create_visit_tracker() -> callable:
    """
    Create a function that tracks how many times it is called.
    """
    visits: int = 0

    def visit() -> int:
        """
        Record one visit.
        """
        nonlocal visits

        visits += 1

        return visits

    return visit


visit_tracker = create_visit_tracker()

print(visit_tracker())
print(visit_tracker())
print(visit_tracker())


# =============================================================================
# 63. Function Call Counter
# =============================================================================


def create_call_counter() -> callable:
    """
    Create a function that counts calls.
    """
    calls: int = 0

    def wrapped_call() -> int:
        """
        Increment the call count.
        """
        nonlocal calls

        calls += 1

        return calls

    return wrapped_call


call_counter = create_call_counter()

print(call_counter())
print(call_counter())
print(call_counter())


# =============================================================================
# 64. Running Average
# =============================================================================


def create_running_average() -> callable:
    """
    Create a running average calculator.
    """
    count: int = 0
    total: float = 0.0

    def add(value: float) -> float:
        """
        Add a value and return the running average.
        """
        nonlocal count, total

        count += 1
        total += value

        return total / count

    return add


running_average = create_running_average()

print(running_average(10.0))
print(running_average(20.0))
print(running_average(30.0))


# =============================================================================
# 65. Running Minimum
# =============================================================================


def create_running_minimum() -> callable:
    """
    Create a running minimum tracker.
    """
    minimum: float | None = None

    def add(value: float) -> float:
        """
        Update and return the running minimum.
        """
        nonlocal minimum

        if minimum is None or value < minimum:
            minimum = value

        return minimum

    return add


running_minimum = create_running_minimum()

print(running_minimum(50.0))
print(running_minimum(20.0))
print(running_minimum(30.0))


# =============================================================================
# 66. Running Maximum
# =============================================================================


def create_running_maximum() -> callable:
    """
    Create a running maximum tracker.
    """
    maximum: float | None = None

    def add(value: float) -> float:
        """
        Update and return the running maximum.
        """
        nonlocal maximum

        if maximum is None or value > maximum:
            maximum = value

        return maximum

    return add


running_maximum = create_running_maximum()

print(running_maximum(10.0))
print(running_maximum(50.0))
print(running_maximum(30.0))


# =============================================================================
# 67. Stateful ID Generator
# =============================================================================


def create_id_generator() -> callable:
    """
    Create an incremental ID generator.
    """
    current_id: int = 0

    def next_id() -> int:
        """
        Generate the next ID.
        """
        nonlocal current_id

        current_id += 1

        return current_id

    return next_id


next_id = create_id_generator()

print(next_id())
print(next_id())
print(next_id())
print(next_id())


# =============================================================================
# 68. Prefix Generator
# =============================================================================


def create_prefix_generator(prefix: str) -> callable:
    """
    Create a function that generates numbered values.
    """
    number: int = 0

    def generate() -> str:
        """
        Generate the next prefixed value.
        """
        nonlocal number

        number += 1

        return f"{prefix}-{number}"

    return generate


user_id_generator = create_prefix_generator("USER")
order_id_generator = create_prefix_generator("ORDER")

print(user_id_generator())
print(user_id_generator())

print(order_id_generator())
print(order_id_generator())


# =============================================================================
# 69. Simple State Machine
# =============================================================================


def create_state_machine() -> callable:
    """
    Create a simple state machine.
    """
    state: str = "idle"

    def transition(new_state: str) -> str:
        """
        Change the current state.
        """
        nonlocal state

        state = new_state

        return state

    return transition


state_machine = create_state_machine()

print(state_machine("running"))
print(state_machine("paused"))
print(state_machine("completed"))


# =============================================================================
# 70. nonlocal and Decorator-Like State
# =============================================================================


def create_limited_counter(limit: int) -> callable:
    """
    Create a counter limited by a maximum value.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment until the limit is reached.
        """
        nonlocal count

        if count < limit:
            count += 1

        return count

    return increment


limited_counter = create_limited_counter(3)

print(limited_counter())
print(limited_counter())
print(limited_counter())
print(limited_counter())
print(limited_counter())


# =============================================================================
# 71. Callback State
# =============================================================================


def create_event_counter() -> callable:
    """
    Create a callback that counts events.
    """
    event_count: int = 0

    def handle_event(event_name: str) -> str:
        """
        Record an event.
        """
        nonlocal event_count

        event_count += 1

        return f"{event_count}: {event_name}"

    return handle_event


event_handler = create_event_counter()

print(event_handler("start"))
print(event_handler("process"))
print(event_handler("finish"))


# =============================================================================
# 72. nonlocal With a Closure
# =============================================================================


def create_closure_counter() -> callable:
    """
    Create a closure containing mutable state.
    """
    count: int = 0

    def increment() -> int:
        """
        Update the captured count.
        """
        nonlocal count

        count += 1

        return count

    return increment


closure_counter = create_closure_counter()

print(closure_counter())
print(closure_counter())
print(closure_counter())


# =============================================================================
# 73. Closure State Is Preserved
# =============================================================================
"""
When create_closure_counter() returns, its local execution has finished.

However, the returned nested function still references count.

Because the nested function uses count, Python preserves the necessary
enclosing state.

This is one of the important mechanisms behind closures.
"""


# =============================================================================
# 74. Closure Factory With Independent State
# =============================================================================


def create_step_counter(step: int) -> callable:
    """
    Create a counter with a custom step.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment by the enclosing step.
        """
        nonlocal count

        count += step

        return count

    return increment


step_two_counter = create_step_counter(2)
step_five_counter = create_step_counter(5)

print(step_two_counter())
print(step_two_counter())

print(step_five_counter())
print(step_five_counter())


# =============================================================================
# 75. Updating the Enclosing Configuration
# =============================================================================


def create_threshold_checker(
    initial_threshold: int,
) -> tuple[callable, callable]:
    """
    Create threshold getter and setter functions.
    """
    threshold: int = initial_threshold

    def set_threshold(new_threshold: int) -> None:
        """
        Update the threshold.
        """
        nonlocal threshold

        threshold = new_threshold

    def check(value: int) -> bool:
        """
        Check a value against the current threshold.
        """
        return value >= threshold

    return set_threshold, check


set_threshold, check_threshold = create_threshold_checker(100)

print(check_threshold(50))
print(check_threshold(150))

set_threshold(200)

print(check_threshold(150))
print(check_threshold(250))


# =============================================================================
# 76. nonlocal With Optional State
# =============================================================================


def create_optional_value() -> callable:
    """
    Create a function that stores an optional value.
    """
    value: str | None = None

    def set_value(new_value: str | None) -> str | None:
        """
        Update the optional value.
        """
        nonlocal value

        value = new_value

        return value

    return set_value


optional_value = create_optional_value()

print(optional_value("Python"))
print(optional_value(None))


# =============================================================================
# 77. nonlocal and Name Resolution
# =============================================================================
"""
For a nested function, Python commonly searches names using LEGB:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

The nonlocal keyword tells Python that a particular assignment should
target an enclosing function variable instead of creating a local name.
"""


# =============================================================================
# 78. nonlocal and Local Scope
# =============================================================================


def demonstrate_local_scope() -> int:
    """
    Demonstrate that assignment is local by default.
    """
    value: int = 10

    def inner() -> int:
        """
        Create a local variable named value.
        """
        value: int = 20

        return value

    inner_value: int = inner()

    return value + inner_value


local_scope_result: int = demonstrate_local_scope()

print(local_scope_result)


# =============================================================================
# 79. nonlocal and Enclosing Scope
# =============================================================================


def demonstrate_enclosing_scope() -> int:
    """
    Demonstrate nonlocal access to an enclosing variable.
    """
    value: int = 10

    def inner() -> int:
        """
        Modify the enclosing value.
        """
        nonlocal value

        value += 20

        return value

    return inner()


enclosing_scope_result: int = demonstrate_enclosing_scope()

print(enclosing_scope_result)


# =============================================================================
# 80. nonlocal and Global Scope
# =============================================================================


global_message: str = "global"


def read_global_message() -> str:
    """
    Read a global variable.
    """
    return global_message


global_message_result: str = read_global_message()

print(global_message_result)


# =============================================================================
# 81. nonlocal Does Not Replace global
# =============================================================================
"""
Use global when the target is module/global scope.

Use nonlocal when the target is an enclosing function scope.

Incorrect concept:

    nonlocal global_variable

when global_variable exists only at module level.

Correct:

    global global_variable

For a nested function variable:

    nonlocal enclosing_variable
"""


# =============================================================================
# 82. nonlocal and Assignment
# =============================================================================


def assignment_demo() -> int:
    """
    Demonstrate explicit nonlocal assignment.
    """
    value: int = 1

    def update() -> int:
        """
        Assign to the enclosing variable.
        """
        nonlocal value

        value = 2

        return value

    return update()


assignment_demo_result: int = assignment_demo()

print(assignment_demo_result)


# =============================================================================
# 83. nonlocal and +=
# =============================================================================


def increment_demo() -> int:
    """
    Demonstrate augmented assignment with nonlocal.
    """
    value: int = 0

    def increment() -> int:
        """
        Increment the enclosing variable.
        """
        nonlocal value

        value += 1

        return value

    return increment()


increment_demo_result: int = increment_demo()

print(increment_demo_result)


# =============================================================================
# 84. nonlocal and -=
# =============================================================================


def decrement_demo() -> int:
    """
    Demonstrate decrementing an enclosing variable.
    """
    value: int = 10

    def decrement() -> int:
        """
        Decrement the enclosing variable.
        """
        nonlocal value

        value -= 1

        return value

    return decrement()


decrement_demo_result: int = decrement_demo()

print(decrement_demo_result)


# =============================================================================
# 85. nonlocal and *=
# =============================================================================


def multiply_demo() -> int:
    """
    Demonstrate multiplication assignment.
    """
    value: int = 2

    def multiply() -> int:
        """
        Multiply the enclosing value.
        """
        nonlocal value

        value *= 5

        return value

    return multiply()


multiply_demo_result: int = multiply_demo()

print(multiply_demo_result)


# =============================================================================
# 86. nonlocal and String Concatenation
# =============================================================================


def create_text_builder() -> callable:
    """
    Create a text builder.
    """
    text: str = ""

    def append_text(value: str) -> str:
        """
        Append to the enclosing string.
        """
        nonlocal text

        text += value

        return text

    return append_text


text_builder = create_text_builder()

print(text_builder("Hello"))
print(text_builder(" "))
print(text_builder("Python"))


# =============================================================================
# 87. nonlocal and Float Calculation
# =============================================================================


def create_price_tracker() -> callable:
    """
    Create a price tracker.
    """
    price: float = 0.0

    def add_price(amount: float) -> float:
        """
        Add to the enclosing price.
        """
        nonlocal price

        price += amount

        return price

    return add_price


price_tracker = create_price_tracker()

print(price_tracker(100.0))
print(price_tracker(50.0))
print(price_tracker(25.5))


# =============================================================================
# 88. nonlocal and Multiple Nested Functions
# =============================================================================


def create_multi_function_state() -> tuple[callable, callable, callable]:
    """
    Create multiple functions sharing state.
    """
    value: int = 0

    def increment() -> int:
        """
        Increment shared state.
        """
        nonlocal value

        value += 1

        return value

    def decrement() -> int:
        """
        Decrement shared state.
        """
        nonlocal value

        value -= 1

        return value

    def reset() -> int:
        """
        Reset shared state.
        """
        nonlocal value

        value = 0

        return value

    return increment, decrement, reset


increment_value, decrement_value, reset_value = (
    create_multi_function_state()
)

print(increment_value())
print(increment_value())
print(decrement_value())
print(reset_value())


# =============================================================================
# 89. nonlocal With State Validation
# =============================================================================


def create_positive_counter() -> callable:
    """
    Create a counter that cannot become negative.
    """
    count: int = 0

    def update(amount: int) -> int:
        """
        Update the count while preserving the invariant.
        """
        nonlocal count

        new_count: int = count + amount

        if new_count >= 0:
            count = new_count

        return count

    return update


positive_counter = create_positive_counter()

print(positive_counter(10))
print(positive_counter(-5))
print(positive_counter(-10))


# =============================================================================
# 90. nonlocal With State Validation
# =============================================================================


def create_percentage() -> callable:
    """
    Create a percentage state updater.
    """
    percentage: float = 0.0

    def set_percentage(value: float) -> float:
        """
        Set a valid percentage between 0 and 100.
        """
        nonlocal percentage

        if 0.0 <= value <= 100.0:
            percentage = value

        return percentage

    return set_percentage


percentage = create_percentage()

print(percentage(50.0))
print(percentage(150.0))
print(percentage(80.0))


# =============================================================================
# 91. nonlocal With Function Factory
# =============================================================================


def create_discount_calculator(
    discount_percentage: float,
) -> tuple[callable, callable]:
    """
    Create a discount calculator with configurable discount.
    """
    discount: float = discount_percentage

    def set_discount(new_discount: float) -> None:
        """
        Update the enclosing discount.
        """
        nonlocal discount

        discount = new_discount

    def calculate(price: float) -> float:
        """
        Calculate a discounted price.
        """
        return price * (1.0 - discount / 100.0)

    return set_discount, calculate


set_discount, calculate_discount = create_discount_calculator(10.0)

print(calculate_discount(1000.0))

set_discount(20.0)

print(calculate_discount(1000.0))


# =============================================================================
# 92. nonlocal and Callbacks
# =============================================================================


def create_callback_tracker() -> callable:
    """
    Create a callback that tracks invocation count.
    """
    count: int = 0

    def callback(message: str) -> str:
        """
        Process a callback invocation.
        """
        nonlocal count

        count += 1

        return f"Call {count}: {message}"

    return callback


callback = create_callback_tracker()

print(callback("first"))
print(callback("second"))
print(callback("third"))


# =============================================================================
# 93. nonlocal and Private State
# =============================================================================
"""
A closure can provide state that is not directly exposed as a module-level
variable.

Example:

    def create_counter() -> callable:
        count: int = 0

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

The caller receives increment(), not count directly.

The enclosing variable remains part of the closure's state.
"""


# =============================================================================
# 94. nonlocal and Encapsulation
# =============================================================================


def create_secure_counter() -> callable:
    """
    Create a counter whose state is kept inside a closure.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the private counter.
        """
        nonlocal count

        count += 1

        return count

    return increment


secure_counter = create_secure_counter()

print(secure_counter())
print(secure_counter())


# =============================================================================
# 95. nonlocal and Shared State
# =============================================================================


def create_shared_manager() -> tuple[callable, callable]:
    """
    Create two functions sharing one state variable.
    """
    state: str = "idle"

    def set_state(new_state: str) -> None:
        """
        Update shared state.
        """
        nonlocal state

        state = new_state

    def get_state() -> str:
        """
        Read shared state.
        """
        return state

    return set_state, get_state


set_state, get_state = create_shared_manager()

print(get_state())

set_state("running")

print(get_state())

set_state("completed")

print(get_state())


# =============================================================================
# 96. nonlocal and State Transition
# =============================================================================


def create_state_controller() -> callable:
    """
    Create a state transition function.
    """
    state: str = "created"

    def transition(new_state: str) -> str:
        """
        Transition to a new state.
        """
        nonlocal state

        state = new_state

        return state

    return transition


state_controller = create_state_controller()

print(state_controller("started"))
print(state_controller("processing"))
print(state_controller("finished"))


# =============================================================================
# 97. Common Mistake: Forgetting nonlocal
# =============================================================================
"""
Consider:

    def outer() -> callable:
        count: int = 0

        def increment() -> int:
            count += 1
            return count

        return increment

This causes an UnboundLocalError when increment() executes.

Why?

Because assignment to count makes Python treat count as local to
increment().

The expression:

    count += 1

requires reading count before assigning the new value.

But the local count has not been initialized.

The correct version is:

    def increment() -> int:
        nonlocal count
        count += 1
        return count
"""


# =============================================================================
# 98. Correct Version of the Previous Example
# =============================================================================


def create_correct_counter() -> callable:
    """
    Correctly modify an enclosing counter.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the enclosing count.
        """
        nonlocal count

        count += 1

        return count

    return increment


correct_counter = create_correct_counter()

print(correct_counter())
print(correct_counter())


# =============================================================================
# 99. Common Mistake: Using global Instead of nonlocal
# =============================================================================
"""
If a variable belongs to an enclosing function, global is the wrong
keyword.

Example:

    def outer() -> callable:
        value: int = 0

        def inner() -> int:
            global value
            value += 1
            return value

This does not target outer()'s value.

The correct keyword is:

    nonlocal value

when the desired variable belongs to the enclosing function.
"""


# =============================================================================
# 100. Common Mistake: Using nonlocal for a Global
# =============================================================================
"""
If a variable exists only in module/global scope, nonlocal is invalid.

Example:

    value: int = 10

    def function() -> None:
        nonlocal value

There is no enclosing function scope containing value.

Use:

    global value

instead.
"""


# =============================================================================
# 101. Common Mistake: Thinking Mutation Requires nonlocal
# =============================================================================
"""
This does not require nonlocal:

    values.append(10)

because the name values is not rebound.

This requires nonlocal:

    values = [10]

because the name values is rebound to a new object.
"""


# =============================================================================
# 102. Mutation Example
# =============================================================================


def mutation_without_nonlocal() -> list[int]:
    """
    Mutate an enclosing list without nonlocal.
    """
    values: list[int] = []

    def add() -> None:
        """
        Mutate the list.
        """
        values.append(10)

    add()

    return values


mutation_result: list[int] = mutation_without_nonlocal()

print(mutation_result)


# =============================================================================
# 103. Rebinding Example
# =============================================================================


def rebinding_with_nonlocal() -> list[int]:
    """
    Rebind an enclosing list using nonlocal.
    """
    values: list[int] = []

    def replace() -> None:
        """
        Replace the enclosing list.
        """
        nonlocal values

        values = [10, 20, 30]

    replace()

    return values


rebinding_result: list[int] = rebinding_with_nonlocal()

print(rebinding_result)


# =============================================================================
# 104. nonlocal and Closures
# =============================================================================
"""
The combination of nested functions and nonlocal is one of the most
important closure patterns in Python.

General structure:

    def outer():
        state = initial_value

        def inner():
            nonlocal state
            state = new_value

        return inner

The returned function keeps access to state after outer() finishes.
"""


# =============================================================================
# 105. Closure-Based Counter Factory
# =============================================================================


def counter_factory(start: int) -> callable:
    """
    Create a closure-based counter.
    """
    value: int = start

    def next_value() -> int:
        """
        Return the next counter value.
        """
        nonlocal value

        value += 1

        return value

    return next_value


counter_a = counter_factory(0)
counter_b = counter_factory(100)

print(counter_a())
print(counter_a())

print(counter_b())
print(counter_b())


# =============================================================================
# 106. Closure-Based Accumulator Factory
# =============================================================================


def accumulator_factory(start: float) -> callable:
    """
    Create an accumulator starting at a specified value.
    """
    total: float = start

    def add(value: float) -> float:
        """
        Add to the enclosing total.
        """
        nonlocal total

        total += value

        return total

    return add


accumulator_a = accumulator_factory(0.0)
accumulator_b = accumulator_factory(100.0)

print(accumulator_a(10.0))
print(accumulator_a(20.0))

print(accumulator_b(10.0))
print(accumulator_b(20.0))


# =============================================================================
# 107. Closure-Based String Builder
# =============================================================================


def string_builder_factory() -> callable:
    """
    Create a stateful string builder.
    """
    text: str = ""

    def append(value: str) -> str:
        """
        Append text to the enclosing string.
        """
        nonlocal text

        text += value

        return text

    return append


builder = string_builder_factory()

print(builder("Python"))
print(builder(" "))
print(builder("Scope"))


# =============================================================================
# 108. Closure-Based List Builder
# =============================================================================


def list_builder_factory() -> callable:
    """
    Create a stateful list builder.
    """
    values: list[str] = []

    def append(value: str) -> list[str]:
        """
        Append to the enclosing list.
        """
        values.append(value)

        return values.copy()

    return append


list_builder = list_builder_factory()

print(list_builder("Python"))
print(list_builder("Functions"))
print(list_builder("nonlocal"))


# =============================================================================
# 109. Closure-Based Configuration Factory
# =============================================================================


def configuration_factory(
    environment: str,
) -> tuple[callable, callable]:
    """
    Create configurable environment functions.
    """
    current_environment: str = environment

    def set_environment(new_environment: str) -> None:
        """
        Change the current environment.
        """
        nonlocal current_environment

        current_environment = new_environment

    def get_environment() -> str:
        """
        Return the current environment.
        """
        return current_environment

    return set_environment, get_environment


set_environment, get_environment = configuration_factory(
    "development"
)

print(get_environment())

set_environment("testing")

print(get_environment())

set_environment("production")

print(get_environment())


# =============================================================================
# 110. nonlocal and Function Composition
# =============================================================================


def create_pipeline_counter() -> callable:
    """
    Create a stateful pipeline counter.
    """
    processed: int = 0

    def process(value: int) -> int:
        """
        Process a value and track the number of operations.
        """
        nonlocal processed

        processed += 1

        return value * processed

    return process


pipeline_counter = create_pipeline_counter()

print(pipeline_counter(10))
print(pipeline_counter(10))
print(pipeline_counter(10))


# =============================================================================
# 111. nonlocal and Stateful Business Logic
# =============================================================================


def create_invoice_counter() -> callable:
    """
    Create an invoice number generator.
    """
    invoice_number: int = 1000

    def next_invoice_number() -> int:
        """
        Generate the next invoice number.
        """
        nonlocal invoice_number

        invoice_number += 1

        return invoice_number

    return next_invoice_number


next_invoice_number = create_invoice_counter()

print(next_invoice_number())
print(next_invoice_number())
print(next_invoice_number())


# =============================================================================
# 112. nonlocal and Stateful Retry Counter
# =============================================================================


def create_retry_tracker(max_retries: int) -> callable:
    """
    Create a retry tracker.
    """
    retries: int = 0

    def retry() -> bool:
        """
        Attempt another retry if available.
        """
        nonlocal retries

        if retries >= max_retries:
            return False

        retries += 1

        return True

    return retry


retry_tracker = create_retry_tracker(3)

print(retry_tracker())
print(retry_tracker())
print(retry_tracker())
print(retry_tracker())


# =============================================================================
# 113. nonlocal and Toggle State
# =============================================================================


def create_feature_toggle() -> callable:
    """
    Create a feature toggle.
    """
    enabled: bool = False

    def toggle() -> bool:
        """
        Toggle the feature.
        """
        nonlocal enabled

        enabled = not enabled

        return enabled

    return toggle


feature_toggle = create_feature_toggle()

print(feature_toggle())
print(feature_toggle())
print(feature_toggle())


# =============================================================================
# 114. nonlocal and Cached State
# =============================================================================


def create_cached_value() -> callable:
    """
    Create a simple cached-value function.
    """
    cached_value: int | None = None

    def get_value() -> int:
        """
        Initialize and return the cached value.
        """
        nonlocal cached_value

        if cached_value is None:
            cached_value = 100

        return cached_value

    return get_value


cached_value = create_cached_value()

print(cached_value())
print(cached_value())


# =============================================================================
# 115. nonlocal and Lazy Initialization
# =============================================================================


def create_lazy_value() -> callable:
    """
    Create a lazily initialized value.
    """
    value: str | None = None

    def get_value() -> str:
        """
        Initialize the value only when requested.
        """
        nonlocal value

        if value is None:
            value = "Initialized"

        return value

    return get_value


lazy_value = create_lazy_value()

print(lazy_value())
print(lazy_value())


# =============================================================================
# 116. nonlocal and Cache Reset
# =============================================================================


def create_resettable_cache() -> tuple[callable, callable]:
    """
    Create getter and reset functions for a cached value.
    """
    value: str | None = None

    def get_value() -> str:
        """
        Return the cached value.
        """
        nonlocal value

        if value is None:
            value = "Cached"

        return value

    def reset() -> None:
        """
        Clear the cached value.
        """
        nonlocal value

        value = None

    return get_value, reset


get_cached_value, reset_cache = create_resettable_cache()

print(get_cached_value())

reset_cache()

print(get_cached_value())


# =============================================================================
# 117. nonlocal and Closures Versus Classes
# =============================================================================
"""
Closures can store state:

    def create_counter():
        count = 0

        def increment():
            nonlocal count
            count += 1
            return count

        return increment

A class can also store state:

    class Counter:
        def __init__(self):
            self.count = 0

        def increment(self):
            self.count += 1
            return self.count

Both approaches are valid.

Closures are useful when a small amount of private state is needed.

Classes may be clearer when the state and behavior become more complex.
"""


# =============================================================================
# 118. Practical Closure Pattern
# =============================================================================


def create_counter_function() -> callable:
    """
    Create a simple stateful function.
    """
    count: int = 0

    def increment() -> int:
        """
        Increment the stored count.
        """
        nonlocal count

        count += 1

        return count

    return increment


practical_counter = create_counter_function()

print(practical_counter())
print(practical_counter())
print(practical_counter())


# =============================================================================
# 119. Practical Getter/Setter Pattern
# =============================================================================


def create_setting(
    initial_value: str,
) -> tuple[callable, callable]:
    """
    Create a setting with getter and setter functions.
    """
    value: str = initial_value

    def get() -> str:
        """
        Get the setting.
        """
        return value

    def set_value(new_value: str) -> None:
        """
        Update the setting.
        """
        nonlocal value

        value = new_value

    return get, set_value


get_setting, set_setting = create_setting("development")

print(get_setting())

set_setting("production")

print(get_setting())


# =============================================================================
# 120. Practical Accumulator Pattern
# =============================================================================


def create_total() -> callable:
    """
    Create a total accumulator.
    """
    total: float = 0.0

    def add(amount: float) -> float:
        """
        Add an amount to the total.
        """
        nonlocal total

        total += amount

        return total

    return add


total = create_total()

print(total(100.0))
print(total(200.0))
print(total(50.0))


# =============================================================================
# 121. Practical Sequence Generator
# =============================================================================


def create_sequence(
    start: int,
    step: int,
) -> callable:
    """
    Create a sequence generator.
    """
    current: int = start

    def next_value() -> int:
        """
        Return the next value in the sequence.
        """
        nonlocal current

        value: int = current
        current += step

        return value

    return next_value


sequence = create_sequence(10, 5)

print(sequence())
print(sequence())
print(sequence())
print(sequence())


# =============================================================================
# 122. Practical ID Generator
# =============================================================================


def create_identifier_generator(
    prefix: str,
) -> callable:
    """
    Create an identifier generator.
    """
    number: int = 0

    def generate() -> str:
        """
        Generate a unique identifier within this closure.
        """
        nonlocal number

        number += 1

        return f"{prefix}-{number:04d}"

    return generate


user_identifier = create_identifier_generator("USER")
order_identifier = create_identifier_generator("ORDER")

print(user_identifier())
print(user_identifier())

print(order_identifier())
print(order_identifier())


# =============================================================================
# 123. Practical Progress Tracker
# =============================================================================


def create_progress_tracker(
    total: int,
) -> callable:
    """
    Create a progress tracker.
    """
    completed: int = 0

    def update(amount: int = 1) -> float:
        """
        Update progress and return the percentage.
        """
        nonlocal completed

        completed = min(
            completed + amount,
            total,
        )

        if total == 0:
            return 100.0

        return completed / total * 100.0

    return update


progress = create_progress_tracker(10)

print(progress())
print(progress(2))
print(progress(5))
print(progress(10))


# =============================================================================
# 124. Practical Retry Manager
# =============================================================================


def create_retry_manager(
    maximum_attempts: int,
) -> callable:
    """
    Create a retry manager.
    """
    attempts: int = 0

    def attempt() -> bool:
        """
        Record an attempt.
        """
        nonlocal attempts

        if attempts >= maximum_attempts:
            return False

        attempts += 1

        return True

    return attempt


retry_manager = create_retry_manager(3)

print(retry_manager())
print(retry_manager())
print(retry_manager())
print(retry_manager())


# =============================================================================
# 125. Practical Rate Tracker
# =============================================================================


def create_rate_tracker() -> callable:
    """
    Create a simple rate tracker.
    """
    count: int = 0
    total: float = 0.0

    def record(value: float) -> float:
        """
        Record a value and return the average.
        """
        nonlocal count, total

        count += 1
        total += value

        return total / count

    return record


rate_tracker = create_rate_tracker()

print(rate_tracker(10.0))
print(rate_tracker(20.0))
print(rate_tracker(30.0))


# =============================================================================
# 126. Scope Diagram
# =============================================================================
"""
Consider:

    def outer():
        value = 10

        def inner():
            nonlocal value
            value += 1

        return inner

Scope structure:

    GLOBAL
       |
       v
    outer()
       |
       |-- value
       |
       v
    inner()
       |
       |-- nonlocal value
       |
       +---- modifies outer.value

The inner function has local scope.

The outer function provides the enclosing scope.

The global module provides global scope.
"""


# =============================================================================
# 127. LEGB With nonlocal
# =============================================================================
"""
For:

    value = "global"

    def outer():
        value = "enclosing"

        def inner():
            nonlocal value
            value = "changed"

The variable targeted by nonlocal is:

    outer.value

It is not:

    inner.value

and it is not:

    global value
"""


# =============================================================================
# 128. Important Difference Between Reading and Rebinding
# =============================================================================
"""
Reading:

    return value

does not require nonlocal.

Rebinding:

    value = new_value

requires nonlocal if value belongs to an enclosing function.

Augmented assignment:

    value += 1

also requires nonlocal because it performs a read and a write.
"""


# =============================================================================
# 129. nonlocal and +=
# =============================================================================


def demonstrate_augmented_assignment() -> callable:
    """
    Create a function using nonlocal with +=.
    """
    value: int = 0

    def update() -> int:
        """
        Update the enclosing value.
        """
        nonlocal value

        value += 10

        return value

    return update


augmented_assignment = demonstrate_augmented_assignment()

print(augmented_assignment())
print(augmented_assignment())


# =============================================================================
# 130. nonlocal and -=
# =============================================================================


def demonstrate_decrement() -> callable:
    """
    Create a function using nonlocal with -=.
    """
    value: int = 100

    def update() -> int:
        """
        Decrease the enclosing value.
        """
        nonlocal value

        value -= 10

        return value

    return update


decrement = demonstrate_decrement()

print(decrement())
print(decrement())


# =============================================================================
# 131. nonlocal and *=
# =============================================================================


def demonstrate_multiplication() -> callable:
    """
    Create a function using nonlocal with *=.
    """
    value: int = 2

    def update() -> int:
        """
        Multiply the enclosing value.
        """
        nonlocal value

        value *= 2

        return value

    return update


multiplication = demonstrate_multiplication()

print(multiplication())
print(multiplication())
print(multiplication())


# =============================================================================
# 132. nonlocal and String +=
# =============================================================================


def demonstrate_string_update() -> callable:
    """
    Create a function that extends an enclosing string.
    """
    text: str = ""

    def append(value: str) -> str:
        """
        Append to the enclosing string.
        """
        nonlocal text

        text += value

        return text

    return append


append_text = demonstrate_string_update()

print(append_text("A"))
print(append_text("B"))
print(append_text("C"))


# =============================================================================
# 133. nonlocal and State Reset
# =============================================================================


def create_resettable_value() -> tuple[callable, callable]:
    """
    Create getter and reset functions.
    """
    value: int = 100

    def get_value() -> int:
        """
        Read the value.
        """
        return value

    def reset() -> None:
        """
        Reset the value.
        """
        nonlocal value

        value = 100

    return get_value, reset


get_value, reset = create_resettable_value()

print(get_value())

reset()

print(get_value())


# =============================================================================
# 134. nonlocal and Multiple State Operations
# =============================================================================


def create_numeric_state() -> tuple[callable, callable, callable]:
    """
    Create increment, decrement, and reset operations.
    """
    value: int = 0

    def increment() -> int:
        """
        Increment the value.
        """
        nonlocal value

        value += 1

        return value

    def decrement() -> int:
        """
        Decrement the value.
        """
        nonlocal value

        value -= 1

        return value

    def reset() -> int:
        """
        Reset the value.
        """
        nonlocal value

        value = 0

        return value

    return increment, decrement, reset


increment, decrement, reset = create_numeric_state()

print(increment())
print(increment())
print(decrement())
print(reset())


# =============================================================================
# 135. Best Practice: Keep Closure State Small
# =============================================================================
"""
Closures with nonlocal are useful for small amounts of state.

Good example:

    def create_counter():
        count = 0

        def increment():
            nonlocal count
            count += 1
            return count

        return increment

For large and complex state, a class may be easier to understand.

The goal is to make the relationship between state and behavior obvious.
"""


# =============================================================================
# 136. Best Practice: Prefer Explicit Data Flow When Possible
# =============================================================================


def add_values(
    first: int,
    second: int,
) -> int:
    """
    Prefer explicit parameters when persistent state is unnecessary.
    """
    return first + second


explicit_result: int = add_values(
    10,
    20,
)

print(explicit_result)


# =============================================================================
# 137. When nonlocal Is Appropriate
# =============================================================================
"""
nonlocal is especially useful for:

    - counters
    - accumulators
    - closures
    - function factories
    - stateful callbacks
    - configuration closures
    - small private state
    - decorators
    - generators of IDs or sequences
    - maintaining state across function calls
"""


# =============================================================================
# 138. When a Class May Be Better
# =============================================================================
"""
A class may be preferable when:

    - there are many pieces of state
    - there are many operations
    - state needs to be exposed
    - inheritance is useful
    - object identity matters
    - the closure becomes difficult to understand

Example:

    class Counter:
        def __init__(self) -> None:
            self.value: int = 0

        def increment(self) -> int:
            self.value += 1
            return self.value
"""


# =============================================================================
# 139. nonlocal Core Rules
# =============================================================================
"""
Core rules:

1. nonlocal is used inside nested functions.

2. nonlocal refers to an enclosing function scope.

3. nonlocal does not refer to global scope.

4. Reading an enclosing variable does not require nonlocal.

5. Rebinding an enclosing variable requires nonlocal.

6. Augmented assignment such as += also requires nonlocal.

7. Mutation of an enclosing mutable object does not require nonlocal.

8. Rebinding the mutable object itself requires nonlocal.

9. The nearest enclosing binding is selected.

10. Separate closure instances have separate state.

11. nonlocal is commonly used to build stateful closures.

12. nonlocal is useful for small amounts of private state.
"""


# =============================================================================
# 140. Common nonlocal Mistakes
# =============================================================================
"""
Common mistakes include:

    - Forgetting nonlocal before assignment.
    - Using global instead of nonlocal.
    - Using nonlocal for a global variable.
    - Thinking mutation requires nonlocal.
    - Confusing rebinding with mutation.
    - Assuming all nested variables require nonlocal.
    - Forgetting that the nearest enclosing binding is selected.
    - Creating overly complicated closures.
    - Using closures where a class would be clearer.
"""


# =============================================================================
# 141. NameError Versus UnboundLocalError
# =============================================================================
"""
NameError:

    The name cannot be found in the available scopes.

UnboundLocalError:

    Python considers the name local because of an assignment, but the
    local name is read before receiving a value.

Example:

    def outer():
        value = 10

        def inner():
            value += 1
            return value

The assignment makes value local to inner().

The read required by += happens before local value has been initialized.

The correct version is:

    def inner():
        nonlocal value
        value += 1
        return value
"""


# =============================================================================
# 142. Scope and Closure Summary
# =============================================================================
"""
A nested function can access:

    Local
        ↓
    Enclosing
        ↓
    Global
        ↓
    Built-in

If the nested function only reads an enclosing variable:

    nonlocal

is not needed.

If the nested function rebinds the enclosing variable:

    nonlocal

is required.

Example:

    def outer():
        count = 0

        def inner():
            nonlocal count
            count += 1
            return count

        return inner
"""


# =============================================================================
# 143. Complete nonlocal Example
# =============================================================================


def create_application_controller() -> tuple[callable, callable, callable]:
    """
    Create a small stateful application controller.
    """
    status: str = "stopped"
    request_count: int = 0

    def start() -> str:
        """
        Start the application.
        """
        nonlocal status

        status = "running"

        return status

    def request() -> tuple[str, int]:
        """
        Record a request.
        """
        nonlocal request_count

        request_count += 1

        return status, request_count

    def stop() -> str:
        """
        Stop the application.
        """
        nonlocal status

        status = "stopped"

        return status

    return start, request, stop


start_application, make_request, stop_application = (
    create_application_controller()
)

print(start_application())
print(make_request())
print(make_request())
print(stop_application())


# =============================================================================
# 144. Complete Counter Example
# =============================================================================


def create_complete_counter(
    start: int = 0,
    step: int = 1,
) -> tuple[callable, callable, callable]:
    """
    Create a counter with increment, reset, and read operations.
    """
    value: int = start

    def increment() -> int:
        """
        Increment the counter.
        """
        nonlocal value

        value += step

        return value

    def reset() -> int:
        """
        Reset the counter to its starting value.
        """
        nonlocal value

        value = start

        return value

    def get_value() -> int:
        """
        Return the current counter value.
        """
        return value

    return increment, reset, get_value


increment_complete, reset_complete, get_complete = (
    create_complete_counter(
        start=10,
        step=5,
    )
)

print(get_complete())
print(increment_complete())
print(increment_complete())
print(reset_complete())
print(get_complete())


# =============================================================================
# 145. Final Practical Example
# =============================================================================


def create_download_tracker(
    total_files: int,
) -> tuple[callable, callable]:
    """
    Create a simple download-progress tracker.
    """
    completed_files: int = 0

    def complete_file() -> float:
        """
        Mark one file as completed.
        """
        nonlocal completed_files

        if completed_files < total_files:
            completed_files += 1

        if total_files == 0:
            return 100.0

        return (
            completed_files
            / total_files
            * 100.0
        )

    def reset() -> None:
        """
        Reset the tracker.
        """
        nonlocal completed_files

        completed_files = 0

    return complete_file, reset


complete_file, reset_downloads = create_download_tracker(4)

print(complete_file())
print(complete_file())
print(complete_file())
print(complete_file())

reset_downloads()

print(complete_file())


# =============================================================================
# 146. nonlocal Cheat Sheet
# =============================================================================
"""
READ ONLY
---------

def outer():
    value = 10

    def inner():
        return value

No nonlocal required.


REASSIGN ENCLOSING VARIABLE
---------------------------

def outer():
    value = 10

    def inner():
        nonlocal value
        value = 20

    return inner


AUGMENTED ASSIGNMENT
--------------------

def outer():
    value = 10

    def inner():
        nonlocal value
        value += 1

    return inner


MUTATE EXISTING OBJECT
----------------------

def outer():
    values = []

    def inner():
        values.append(10)

    return inner

No nonlocal required because values is not rebound.


REPLACE OBJECT
--------------

def outer():
    values = []

    def inner():
        nonlocal values
        values = [10]

    return inner


GLOBAL VARIABLE
---------------

value = 10

def function():
    global value
    value = 20


ENCLOSING FUNCTION VARIABLE
---------------------------

def outer():
    value = 10

    def inner():
        nonlocal value
        value = 20
"""


# =============================================================================
# 147. Final Scope Model
# =============================================================================
"""
Python name resolution:

    LOCAL
       ↓
    ENCLOSING
       ↓
    GLOBAL
       ↓
    BUILT-IN

The nonlocal keyword changes assignment behavior:

    inner function
          ↓
       nonlocal
          ↓
    enclosing function variable

The global keyword changes assignment behavior:

    function
       ↓
      global
       ↓
    module/global variable
"""


# =============================================================================
# 148. Key Takeaways
# =============================================================================
"""
✓ nonlocal is used inside nested functions.

✓ nonlocal refers to a variable in an enclosing function scope.

✓ nonlocal does not refer to global scope.

✓ Reading an enclosing variable does not require nonlocal.

✓ Rebinding an enclosing variable requires nonlocal.

✓ +=, -=, *=, and similar augmented assignments require nonlocal when
  modifying an enclosing variable.

✓ Mutation of an enclosing list does not require nonlocal.

✓ Rebinding an enclosing list requires nonlocal.

✓ Separate closure instances maintain separate state.

✓ nonlocal is commonly used with counters.

✓ nonlocal is commonly used with accumulators.

✓ nonlocal is commonly used with function factories.

✓ nonlocal is commonly used with closures.

✓ nonlocal is useful for stateful callbacks.

✓ nonlocal can maintain private state inside a closure.

✓ global and nonlocal solve different scope problems.

✓ global refers to module/global scope.

✓ nonlocal refers to an enclosing function scope.

✓ The nearest enclosing binding is selected.

✓ A called function does not inherit the caller's local scope.

✓ Only lexical nesting creates an enclosing scope.

✓ Closures preserve access to required enclosing variables.

✓ For complex state, a class may be clearer than a closure.

Core pattern:

    def outer():
        state = initial_value

        def inner():
            nonlocal state
            state = new_value

        return inner

Core distinction:

    READ
        ↓
    no nonlocal required

    REBIND ENCLOSING NAME
        ↓
    nonlocal required

    MUTATE EXISTING OBJECT
        ↓
    nonlocal usually not required

    REBIND OBJECT NAME
        ↓
    nonlocal required

Core keywords:

    global
        ↓
    module/global scope

    nonlocal
        ↓
    nearest enclosing function scope

LEGB:

    Local
      ↓
    Enclosing
      ↓
    Global
      ↓
    Built-in
"""


# =============================================================================
# End of 12_nonlocal_keyword.py
# =============================================================================