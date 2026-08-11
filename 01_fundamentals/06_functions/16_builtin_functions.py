# type: ignore
"""
16_builtin_functions.py

Demonstrates commonly used Python built-in functions.

Built-in functions are functions provided directly by Python.
They can be used without importing a module.

This file focuses on commonly used built-ins that naturally
belong with fundamental function concepts.
"""


# ============================================================
# 1. WHAT ARE BUILT-IN FUNCTIONS?
# ============================================================

"""
Python provides a collection of functions that are available
directly in the language.

Examples:

    len()
    type()
    isinstance()
    id()
    range()
    enumerate()
    zip()
    sum()
    min()
    max()
    abs()
    round()
    any()
    all()
    sorted()
    reversed()
    map()
    filter()

No import is required for these functions.
"""


# ============================================================
# 2. len()
# ============================================================

"""
len() returns the number of items in an object.

It commonly works with:

    strings
    lists
    tuples
    sets
    dictionaries
"""

name = "Python"
numbers = [10, 20, 30, 40]

print(len(name))
print(len(numbers))


# ============================================================
# 3. type()
# ============================================================

"""
type() returns the type of an object.
"""

value = 42
message = "Hello"
numbers = [1, 2, 3]

print(type(value))
print(type(message))
print(type(numbers))


# ============================================================
# 4. isinstance()
# ============================================================

"""
isinstance() checks whether an object is an instance of a
specified type.

It returns:

    True
    False
"""

age = 30
name = "Shreyas"

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(age, str))


# ============================================================
# 5. isinstance() WITH MULTIPLE TYPES
# ============================================================

"""
The second argument can also be a tuple of types.

Example:

    isinstance(value, (int, float))
"""

number = 10

print(isinstance(number, (int, float)))
print(isinstance(number, (str, list)))


# ============================================================
# 6. id()
# ============================================================

"""
id() returns an integer identifying an object during its
lifetime.

It can be useful when discussing object identity.

Do not treat the returned value as a permanent identifier
for the object.
"""

value = 100

print(id(value))


# ============================================================
# 7. range()
# ============================================================

"""
range() represents a sequence of integers.

Common forms:

    range(stop)
    range(start, stop)
    range(start, stop, step)

The stop value is excluded.
"""

print(list(range(5)))
print(list(range(2, 6)))
print(list(range(2, 10, 2)))


# ============================================================
# 8. enumerate()
# ============================================================

"""
enumerate() produces pairs containing:

    index
    value

It is commonly used when both the position and the value
are required.
"""

languages = ["Python", "SQL", "Java"]

for index, language in enumerate(languages):
    print(index, language)


# ============================================================
# 9. enumerate() WITH start
# ============================================================

"""
enumerate() accepts an optional start value.
"""

languages = ["Python", "SQL", "Java"]

for position, language in enumerate(languages, start=1):
    print(position, language)


# ============================================================
# 10. zip()
# ============================================================

"""
zip() combines corresponding elements from multiple
iterables.
"""

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name, score)


# ============================================================
# 11. zip() WITH MULTIPLE ITERABLES
# ============================================================

"""
zip() can combine more than two iterables.
"""

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
cities = ["Delhi", "Bengaluru", "Mumbai"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)


# ============================================================
# 12. sum()
# ============================================================

"""
sum() calculates the total of numeric values.
"""

numbers = [10, 20, 30, 40]

total = sum(numbers)

print(total)


# ============================================================
# 13. sum() WITH START VALUE
# ============================================================

"""
sum() accepts an optional starting value.

Syntax:

    sum(iterable, start)
"""

numbers = [10, 20, 30]

total = sum(numbers, 100)

print(total)


# ============================================================
# 14. min()
# ============================================================

"""
min() returns the smallest value.
"""

numbers = [42, 17, 89, 23]

print(min(numbers))


# ============================================================
# 15. max()
# ============================================================

"""
max() returns the largest value.
"""

numbers = [42, 17, 89, 23]

print(max(numbers))


# ============================================================
# 16. min() AND max() WITH MULTIPLE ARGUMENTS
# ============================================================

"""
min() and max() can also receive multiple positional
arguments.
"""

print(min(42, 17, 89, 23))
print(max(42, 17, 89, 23))


# ============================================================
# 17. abs()
# ============================================================

"""
abs() returns the absolute value of a number.
"""

print(abs(-25))
print(abs(25))
print(abs(-7.5))


# ============================================================
# 18. round()
# ============================================================

"""
round() rounds a number.

An optional second argument specifies the number of decimal
places.
"""

print(round(3.14159))
print(round(3.14159, 2))
print(round(12.5678, 1))


# ============================================================
# 19. any()
# ============================================================

"""
any() returns True if at least one element in an iterable
is truthy.

It returns False when all elements are falsy.
"""

values = [False, False, True, False]

print(any(values))

values = [False, False, False]

print(any(values))


# ============================================================
# 20. all()
# ============================================================

"""
all() returns True when every element in an iterable is
truthy.

It returns False when at least one element is falsy.
"""

values = [True, True, True]

print(all(values))

values = [True, False, True]

print(all(values))


# ============================================================
# 21. any() WITH A CONDITION
# ============================================================

"""
any() is commonly combined with a generator expression
to test whether at least one item satisfies a condition.
"""

numbers = [2, 4, 7, 10]

has_odd_number = any(number % 2 != 0 for number in numbers)

print(has_odd_number)


# ============================================================
# 22. all() WITH A CONDITION
# ============================================================

"""
all() can similarly test whether every item satisfies a
condition.
"""

numbers = [2, 4, 6, 8]

contains_only_even = all(number % 2 == 0 for number in numbers)

print(contains_only_even)


# ============================================================
# 23. sorted()
# ============================================================

"""
sorted() returns a new sorted list.

It does not modify the original iterable.
"""

numbers = [40, 10, 30, 20]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)


# ============================================================
# 24. sorted() IN DESCENDING ORDER
# ============================================================

"""
The reverse parameter controls the sorting direction.
"""

numbers = [40, 10, 30, 20]

descending = sorted(numbers, reverse=True)

print(descending)


# ============================================================
# 25. sorted() WITH key
# ============================================================

"""
The key parameter specifies a function used to determine
the sorting value.

Example:

    sort strings according to their length
"""

words = ["Python", "SQL", "Data", "Engineering"]

sorted_words = sorted(words, key=len)

print(sorted_words)


# ============================================================
# 26. reversed()
# ============================================================

"""
reversed() returns an iterator that produces values in
reverse order.
"""

numbers = [10, 20, 30, 40]

for number in reversed(numbers):
    print(number)


# ============================================================
# 27. reversed() VS reverse()
# ============================================================

"""
reversed() is a built-in function.

list.reverse() is a list method.

reversed():

    produces a reverse iterator
    does not modify the original list


list.reverse():

    modifies the list itself
"""

numbers = [10, 20, 30]

reversed_numbers = list(reversed(numbers))

print(numbers)
print(reversed_numbers)

numbers.reverse()

print(numbers)


# ============================================================
# 28. map()
# ============================================================

"""
map() applies a function to every element of an iterable.

Syntax:

    map(function, iterable)

map() returns a map object.
"""

numbers = [1, 2, 3, 4]

doubled = map(lambda number: number * 2, numbers)

print(list(doubled))


# ============================================================
# 29. map() WITH A NAMED FUNCTION
# ============================================================

"""
The function supplied to map() does not have to be a lambda.

It can be a normal function.
"""

def square(number: int) -> int:
    """Return the square of a number."""
    return number * number


numbers = [1, 2, 3, 4]

squared = map(square, numbers)

print(list(squared))


# ============================================================
# 30. filter()
# ============================================================

"""
filter() keeps elements for which the supplied function
returns a truthy value.

Syntax:

    filter(function, iterable)

filter() returns a filter object.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers,
)

print(list(even_numbers))


# ============================================================
# 31. filter() WITH A NAMED FUNCTION
# ============================================================

def is_positive(number: int) -> bool:
    """Return True when number is positive."""
    return number > 0


numbers = [-5, 10, -2, 7, 0]

positive_numbers = filter(is_positive, numbers)

print(list(positive_numbers))


# ============================================================
# 32. sorted(), map(), AND filter() RETURN NEW OBJECTS
# ============================================================

"""
These functions generally do not modify the original
iterable.

For example:

    sorted()
        -> returns a new list

    map()
        -> returns a map object

    filter()
        -> returns a filter object
"""

numbers = [5, 2, 8, 1]

sorted_numbers = sorted(numbers)
doubled_numbers = list(map(lambda number: number * 2, numbers))
positive_numbers = list(
    filter(lambda number: number > 2, numbers)
)

print(numbers)
print(sorted_numbers)
print(doubled_numbers)
print(positive_numbers)


# ============================================================
# 33. BUILT-IN FUNCTIONS CAN BE PASSED AS OBJECTS
# ============================================================

"""
Functions are objects in Python.

Therefore, a built-in function can itself be passed to
another function.

Example:

    sorted(words, key=len)

Here:

    len

is passed as an object.

It is NOT called immediately.

Correct:

    key=len


Not:

    key=len()
"""

words = ["Python", "SQL", "Data"]

print(sorted(words, key=len))


# ============================================================
# 34. BUILT-IN FUNCTIONS AND ITERABLES
# ============================================================

"""
Many built-in functions work naturally with iterables.

Examples:

    len()
    sum()
    min()
    max()
    any()
    all()
    sorted()
    enumerate()
    zip()
    map()
    filter()
"""

numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(any(numbers))
print(all(numbers))
print(sorted(numbers))


# ============================================================
# 35. BUILT-IN FUNCTIONS VS METHODS
# ============================================================

"""
A built-in function is called directly:

    len(numbers)
    sorted(numbers)
    sum(numbers)


A method belongs to an object:

    numbers.append(40)
    numbers.sort()


These are different concepts.

Example:

    sorted(numbers)

returns a new sorted list.

    numbers.sort()

sorts the list in place.
"""

numbers = [30, 10, 20]

sorted_numbers = sorted(numbers)

print(sorted_numbers)

numbers.sort()

print(numbers)


# ============================================================
# 36. BUILT-IN FUNCTIONS VS IMPORTED FUNCTIONS
# ============================================================

"""
Built-in functions require no import.

Example:

    len(numbers)


An external library function generally requires an import.

Example:

    import math

    math.sqrt(25)


Therefore:

    len()
        -> built-in


    math.sqrt()
        -> function provided by the math module
"""


# ============================================================
# 37. BUILT-IN FUNCTIONS CAN BE INSPECTED
# ============================================================

"""
Python provides the built-in namespace through:

    __builtins__

For example:

    print(__builtins__)

However, __builtins__ is an implementation detail whose
exact form can vary by context.

For normal Python code, simply using built-in functions
directly is preferred.
"""


# ============================================================
# 38. COMMON BUILT-IN FUNCTION CATEGORIES
# ============================================================

"""
A useful mental grouping:

Inspection:

    type()
    isinstance()
    id()
    len()


Iteration:

    range()
    enumerate()
    zip()
    reversed()


Aggregation:

    sum()
    min()
    max()
    any()
    all()


Transformation:

    map()
    filter()


Ordering:

    sorted()
    reversed()


Numeric:

    abs()
    round()
"""


# ============================================================
# 39. IMPORTANT DISTINCTION: map() VS COMPREHENSION
# ============================================================

"""
The same transformation can often be expressed using a
comprehension.

Using map():

    numbers = [1, 2, 3]

    doubled = list(
        map(lambda number: number * 2, numbers)
    )


Using a list comprehension:

    doubled = [
        number * 2
        for number in numbers
    ]


Both are valid.

Comprehensions often provide clearer syntax for simple
transformations.

More advanced comparison belongs in the comprehensions
section.
"""


# ============================================================
# 40. IMPORTANT DISTINCTION: filter() VS COMPREHENSION
# ============================================================

"""
Using filter():

    numbers = [1, 2, 3, 4]

    even_numbers = list(
        filter(
            lambda number: number % 2 == 0,
            numbers,
        )
    )


Using a comprehension:

    even_numbers = [
        number
        for number in numbers
        if number % 2 == 0
    ]


Again, both are valid approaches.
"""


# ============================================================
# 41. BUILT-IN FUNCTIONS AND EMPTY ITERABLES
# ============================================================

"""
Some built-in functions have important behavior with empty
iterables.

For example:

    any([])

returns:

    False


while:

    all([])

returns:

    True


This follows their logical definitions:

    any()
        -> "Is at least one item truthy?"


    all()
        -> "Are all items truthy?"
"""


print(any([]))
print(all([]))


# ============================================================
# 42. PRACTICAL EXAMPLE
# ============================================================

"""
Several built-ins can be combined naturally.
"""

scores = [72, 85, 91, 68, 88]

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
passing = all(score >= 40 for score in scores)

print(average)
print(highest)
print(lowest)
print(passing)


# ============================================================
# 43. PRACTICAL EXAMPLE WITH enumerate() AND zip()
# ============================================================

students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for index, (student, score) in enumerate(
    zip(students, scores),
    start=1,
):
    print(index, student, score)


# ============================================================
# 44. KEY TAKEAWAY
# ============================================================

"""
Python provides many built-in functions that can be used
without importing modules.

Important examples covered here:

    len()
    type()
    isinstance()
    id()

    range()
    enumerate()
    zip()

    sum()
    min()
    max()
    abs()
    round()

    any()
    all()

    sorted()
    reversed()

    map()
    filter()


Remember:

    Built-in functions
        ↓
    available directly in Python
        ↓
    no import required


Also remember that built-in functions are different from:

    object methods
    functions from modules
    user-defined functions


The goal is not to memorize every built-in function.

The goal is to recognize commonly used built-ins and
understand when they are appropriate.
"""