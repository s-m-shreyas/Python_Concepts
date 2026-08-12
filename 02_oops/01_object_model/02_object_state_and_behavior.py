# type: ignore
"""
02_object_state_and_behavior.py

Introduces object state and behavior.

This file focuses on:

    - Object state
    - Object behavior
    - Operations performed on objects
    - Mutable vs immutable state
    - How an object's state can change
    - The relationship between state and behavior

The goal is to understand what "state" and "behavior" mean
before introducing attributes and methods in detail.
"""


# ============================================================
# 1. OBJECT STATE
# ============================================================

"""
Object state represents the data associated with an object
at a particular point in time.

For example, a list currently contains:

    [10, 20, 30]

Those elements are part of the list's current state.
"""

numbers = [10, 20, 30]

print(numbers)


# ============================================================
# 2. OBJECT STATE CAN CHANGE
# ============================================================

"""
Some objects are mutable.

A mutable object's state can change after the object has
been created.

Lists are mutable objects.
"""

numbers = [10, 20, 30]

print("Before:", numbers)

numbers.append(40)

print("After:", numbers)


# ============================================================
# 3. OBJECT BEHAVIOR
# ============================================================

"""
Object behavior refers to the operations an object supports.

For example, a list supports operations such as:

    append()
    remove()
    sort()
    reverse()

These operations allow us to work with the object's state.
"""

numbers = [30, 10, 20]

numbers.sort()

print(numbers)


# ============================================================
# 4. STATE AND BEHAVIOR WORK TOGETHER
# ============================================================

"""
State describes what an object currently contains.

Behavior describes what can be done with that object.

For a list:

    State:
        [30, 10, 20]

    Behavior:
        sort()
        append()
        remove()
        reverse()
"""

numbers = [30, 10, 20]

print("State:", numbers)

numbers.sort()

print("State after behavior:", numbers)


# ============================================================
# 5. DIFFERENT OBJECTS HAVE DIFFERENT STATES
# ============================================================

"""
Two objects of the same type can have different states.

Both objects below are lists, but their contents differ.
"""

first = [10, 20, 30]
second = [100, 200, 300]

print(first)
print(second)


# ============================================================
# 6. SAME TYPE, DIFFERENT STATE
# ============================================================

"""
The objects have the same type:

    list

But their states are different.
"""

first = [10, 20, 30]
second = [100, 200, 300]

print(type(first))
print(type(second))

print(first)
print(second)


# ============================================================
# 7. OBJECT BEHAVIOR DEPENDS ON TYPE
# ============================================================

"""
The type of an object determines which operations it supports.

For example:

    strings support upper()
    lists support append()
    dictionaries support get()

The available behavior therefore depends on the object's type.
"""

message = "python"
numbers = [10, 20, 30]
person = {"name": "Shreyas"}

print(message.upper())
numbers.append(40)
print(numbers)

print(person.get("name"))


# ============================================================
# 8. IMMUTABLE OBJECT STATE
# ============================================================

"""
Some objects are immutable.

Their state cannot be changed after the object is created.

Integers are immutable objects.

An operation such as:

    number + 10

does not modify the original integer object.

Instead, the expression produces a result.
"""

number = 10

result = number + 5

print("Original:", number)
print("Result:", result)


# ============================================================
# 9. IMMUTABLE OBJECTS AND NEW OBJECTS
# ============================================================

"""
With immutable objects, an operation that appears to change
the value actually produces another object.

For example:

    number = 10
    number = number + 5

The original integer object representing 10 is not modified.

The name 'number' is reassigned to the resulting object.
"""

number = 10

print("Before:", number)

number = number + 5

print("After:", number)


# ============================================================
# 10. MUTABLE OBJECTS CAN CHANGE IN PLACE
# ============================================================

"""
Mutable objects can change their state without replacing the
object itself.

Lists are mutable.
"""

numbers = [10, 20, 30]

object_id_before = id(numbers)

numbers.append(40)

object_id_after = id(numbers)

print(numbers)
print(object_id_before == object_id_after)


# ============================================================
# 11. STATE CHANGE VS REASSIGNMENT
# ============================================================

"""
There is an important difference between:

    changing an object's state

and:

    changing what a variable refers to.

With a list:

    numbers.append(40)

changes the existing object's state.

With reassignment:

    numbers = [10, 20, 30, 40]

the variable is made to refer to another object.
"""

numbers = [10, 20, 30]

numbers.append(40)

print("After state change:", numbers)

numbers = [100, 200, 300, 400]

print("After reassignment:", numbers)


# ============================================================
# 12. SHARED OBJECT STATE
# ============================================================

"""
If two variables refer to the same mutable object, both
variables observe changes made to that object's state.
"""

first = [10, 20, 30]
second = first

first.append(40)

print(first)
print(second)


# ============================================================
# 13. STATE IS ASSOCIATED WITH THE OBJECT
# ============================================================

"""
The state belongs conceptually to the object, not to the
variable name.

Here, both names refer to one list object.

Therefore, there is only one list state.
"""

first = [10, 20, 30]
second = first

print(first is second)

second.append(40)

print(first)
print(second)


# ============================================================
# 14. BEHAVIOR DOES NOT ALWAYS CHANGE STATE
# ============================================================

"""
Not every operation changes an object's state.

For example, list operations can simply inspect the object.

len() reads information from the list without modifying it.
"""

numbers = [10, 20, 30]

length = len(numbers)

print("List:", numbers)
print("Length:", length)


# ============================================================
# 15. OPERATIONS CAN PRODUCE NEW OBJECTS
# ============================================================

"""
Some operations produce a new object instead of modifying
the original object.

For example, string methods such as upper() return a new
string because strings are immutable.
"""

message = "python"

result = message.upper()

print("Original:", message)
print("Result:", result)


# ============================================================
# 16. STATE AND BEHAVIOR IN A STRING
# ============================================================

"""
A string object has state represented by its character data.

Its behavior includes operations such as:

    upper()
    lower()
    replace()
    split()

Strings are immutable, so these operations do not modify
the original string.
"""

message = "Python Programming"

print(message.upper())
print(message.lower())
print(message.replace("Python", "Data"))


# ============================================================
# 17. STATE AND BEHAVIOR IN A DICTIONARY
# ============================================================

"""
A dictionary has state represented by its key-value pairs.

It provides behavior such as:

    get()
    keys()
    values()
    update()
"""

person = {
    "name": "Shreyas",
    "role": "Data Engineer",
}

print("State:", person)

person.update({"experience": 1})

print("Updated state:", person)


# ============================================================
# 18. OBJECT BEHAVIOR COMES FROM ITS TYPE
# ============================================================

"""
Different types support different operations.

For example:

    list
        append()

    str
        upper()

    dict
        get()

This is one reason an object's type is important when
understanding its behavior.
"""

numbers = [10, 20]
message = "python"
person = {"name": "Shreyas"}

numbers.append(30)
message = message.upper()
name = person.get("name")

print(numbers)
print(message)
print(name)


# ============================================================
# 19. STATE AND IDENTITY
# ============================================================

"""
Changing the state of a mutable object does not necessarily
change its identity.

The object remains the same object while its state changes.
"""

numbers = [10, 20, 30]

before = id(numbers)

numbers.append(40)

after = id(numbers)

print("State:", numbers)
print("Same identity:", before == after)


# ============================================================
# 20. STATE, BEHAVIOR, AND IDENTITY
# ============================================================

"""
An object can therefore be understood using three related
ideas:

    Identity
        Which particular object is this?

    State
        What data does this object currently contain?

    Behavior
        What operations can this object perform?

Example:

    numbers = [10, 20, 30]

    Identity:
        id(numbers)

    State:
        [10, 20, 30]

    Behavior:
        append()
        remove()
        sort()
        reverse()
"""

numbers = [10, 20, 30]

print("Identity:", id(numbers))
print("State:", numbers)

numbers.append(40)

print("State after behavior:", numbers)


# ============================================================
# 21. WHY THIS MATTERS FOR OOP
# ============================================================

"""
Object-oriented programming organizes programs around
objects.

A useful conceptual model is:

    Object
       |
       +-- Identity
       |
       +-- State
       |
       +-- Behavior

Later, when we create our own classes, we will use:

    attributes
        -> to represent state

    methods
        -> to represent behavior

Those concepts will be introduced separately in the next
files.
"""


# ============================================================
# 22. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. Object state represents the data associated with an object.

2. Object behavior represents operations supported by an object.

3. Objects of the same type can have different states.

4. The object's type determines the operations it supports.

5. Mutable objects can change their state.

6. Immutable objects cannot have their state changed after
   creation.

7. State change and variable reassignment are different concepts.

8. Multiple variables can refer to the same object's state.

9. Some operations modify an object.

10. Some operations inspect an object.

11. Some operations produce a new object.

12. A mutable object's identity can remain the same while its
    state changes.

13. In OOP, state is commonly represented through attributes
    and behavior through methods.

Attributes and methods will be explored explicitly in the
next file.
"""