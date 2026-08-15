
# Comprehensions

Comprehensions are a concise way to create new collections from existing
iterables.

Python provides comprehensions for:

- Lists
- Sets
- Dictionaries

They can be used for:

- Transformation
- Filtering
- Conditional value selection
- Nested iteration
- Collection construction

The goal of this section is not simply to learn shorter syntax.

The goal is to understand:

- How comprehensions work
- How comprehension syntax maps to traditional loops
- How filtering differs from conditional value selection
- How nested comprehensions execute
- How list, set, and dictionary comprehensions differ
- When comprehensions improve readability
- When traditional loops are better
- How to write maintainable comprehensions


---

# Folder Structure

    02_comprehensions
    ├── 01_list_comprehensions.py
    ├── 02_conditional_list_comprehensions.py
    ├── 03_nested_list_comprehensions.py
    ├── 04_set_comprehensions.py
    ├── 05_dict_comprehensions.py
    ├── 06_conditional_comprehensions.py
    ├── 07_nested_comprehensions.py
    ├── 08_comprehension_vs_loop.py
    ├── 09_comprehension_best_practices.py
    └── README.md


---

# 1. What Is a Comprehension?

A comprehension is a compact syntax for constructing a collection from
an iterable.

Traditional loop:

    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers: list[int] = []

    for number in numbers:
        squared_numbers.append(number**2)

    print(squared_numbers)

Comprehension:

    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

    print(squared_numbers)

Output:

    [1, 4, 9, 16, 25]

A comprehension combines:

    Iteration
        +
    Expression
        +
    Collection construction


---

# 2. Basic List Comprehension

A list comprehension creates a new list.

## Syntax

    [expression for item in iterable]

Example:

    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

    print(squared_numbers)

Output:

    [1, 4, 9, 16, 25]


---

# 3. Understanding the Syntax

Consider:

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

The parts are:

    number**2
        ↑
    expression

    for number in numbers
        ↑          ↑
       item     iterable

Therefore:

    [expression for item in iterable]

means:

    For every item in the iterable:

        1. Evaluate the expression.
        2. Add the resulting value to the new collection.


---

# 4. List Comprehension with Transformation

The expression can transform every item.

    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

    print(squared_numbers)

Output:

    [1, 4, 9, 16, 25]

The original list is not modified.

A new list is created.


---

# 5. String Transformation

    companies: list[str] = [
        "apple",
        "google",
        "microsoft",
    ]

    uppercase_companies: list[str] = [
        company.upper()
        for company in companies
    ]

    print(uppercase_companies)

Output:

    ['APPLE', 'GOOGLE', 'MICROSOFT']


---

# 6. String-Length Pair

A comprehension can construct a new structure for every item.

    companies_string_list: list[str] = [
        "apple",
        "yahoo",
        "google",
        "tech-mahindra",
        "microsoft",
        "x",
        "facebook",
        "instagram",
    ]

    companies_string_list_length_pair: list[dict[str, int]] = [
        {
            company: len(company)
        }
        for company in companies_string_list
    ]

    print(companies_string_list_length_pair)

Output:

    [
        {'apple': 5},
        {'yahoo': 5},
        {'google': 6},
        {'tech-mahindra': 13},
        {'microsoft': 9},
        {'x': 1},
        {'facebook': 8},
        {'instagram': 9}
    ]


---

# 7. Numbered String Pair Using enumerate()

enumerate() can provide both the index and value.

    companies_string_list: list[str] = [
        "apple",
        "yahoo",
        "google",
        "tech-mahindra",
        "microsoft",
        "x",
        "facebook",
        "instagram",
    ]

    numbered_company_string_list: list[dict[int, str]] = [
        {
            index: company
        }
        for index, company in enumerate(
            companies_string_list,
            start=1,
        )
    ]

    print(numbered_company_string_list)

Output:

    [
        {1: 'apple'},
        {2: 'yahoo'},
        {3: 'google'},
        {4: 'tech-mahindra'},
        {5: 'microsoft'},
        {6: 'x'},
        {7: 'facebook'},
        {8: 'instagram'}
    ]


---

# 8. Factorial Using math.factorial()

A comprehension can call functions.

    import math


    factorialize_numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
    ]

    factorialized_numbers: list[int] = [
        math.factorial(number)
        for number in factorialize_numbers
    ]

    print(factorialized_numbers)

Output:

    [1, 2, 6, 24, 120]


---

# 9. Factorial Using eval()

A comprehension can contain a more complex expression.

This example builds a multiplication expression and evaluates it.

    factorialize_numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
    ]

    factorialized_numbers_2: list[int] = [
        eval(
            "*".join(
                [
                    str(num)
                    for num in range(1, number + 1)
                ]
            )
        )
        for number in factorialize_numbers
    ]

    print(factorialized_numbers_2)

Output:

    [1, 2, 6, 24, 120]

Important:

eval() must not be used with untrusted input.

This example is retained because it demonstrates that a comprehension's
expression can itself contain another comprehension and function calls.

For actual factorial calculations, math.factorial() is the appropriate
solution.


---

# 10. Factorial Using Recursive Lambda

The underlying logic can be represented as:

    def worker(f, n, acc):

        if n == 0:
            return acc

        return f(f, n - 1, acc * n)


    def factorial(n):
        return worker(worker, n, 1)

The same idea can be embedded into a comprehension:

    factorialize_numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
    ]

    factorialized_numbers_3: list[int] = [

        (
            lambda f: f(f, number, 1)
        )(
            lambda f, n, acc:
                acc
                if n == 0
                else f(f, n - 1, acc * n)
        )

        for number in factorialize_numbers

    ]

    print(factorialized_numbers_3)

Output:

    [1, 2, 6, 24, 120]

This is primarily a demonstration of expression composition.

It is not recommended as a practical replacement for math.factorial().


---

# 11. Using zip()

zip() allows multiple iterables to be processed together.

    f_names: list[str] = [
        "S.M.",
        "Pranay",
        "Rajeshwari",
    ]

    l_names: list[str] = [
        "Shreyas",
        "Gharde",
        "Khot",
    ]

    full_names: list[str] = [
        f"{f_name} {l_name}"
        for f_name, l_name in zip(f_names, l_names)
    ]

    print(full_names)

Output:

    ['S.M. Shreyas', 'Pranay Gharde', 'Rajeshwari Khot']


---

# 12. Flattening a List

Given:

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

A nested comprehension can flatten it:

    flat_list_3: list[int] = [
        num
        for sublist in matrix
        for num in sublist
    ]

    print(flat_list_3)

Output:

    [1, 2, 3, 4, 5, 6, 7, 8, 10]

The execution order is equivalent to:

    for sublist in matrix:

        for num in sublist:
            ...


---

# 13. Flattening List — Alternative Solutions

## Version 1 — String-Based Approach

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

    flat_list_1: list[int] = [
        int(x)
        for x in str(matrix)
        .strip("[]")
        .replace(" ", "")
        .replace("[", "")
        .replace("]", "")
        .split(",")
    ]

    print(flat_list_1)

This works for the specific structure shown above, but it is not a good
general solution.

It converts structured data into a string and then parses the string again.


---

## Version 2 — extend()

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

    flat_list_2: list[int] = []

    for sub_list in matrix:
        flat_list_2.extend(sub_list)

    print(flat_list_2)

This is clearer than using a comprehension purely for its side effect.

The original practice example used:

    [flat_list_2.extend(sub_list) for sub_list in matrix]

That demonstrates that a comprehension can technically execute a method
for its side effect, but this is not considered good comprehension style.

Prefer the explicit loop.


---

## Version 3 — Clean Comprehension

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

    flat_list_3: list[int] = [
        num
        for sublist in matrix
        for num in sublist
    ]

    print(flat_list_3)

This is the cleanest comprehension-based solution for flattening a
one-level nested list.


---

# 14. Conditional List Comprehension

A comprehension can filter elements using an if condition.

## Syntax

    [expression for item in iterable if condition]

Example:

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    even_numbers: list[int] = [
        number
        for number in numbers
        if number % 2 == 0
    ]

    print(even_numbers)

Output:

    [2, 4, 6]

The trailing if determines whether an item is included.


---

# 15. Filtering Strings

    lang_string_list: list[str] = [
        "Python",
        "Perl",
        "Java",
        "php",
        "C++",
    ]

    P_filtered_string_list: list[str] = [
        string
        for string in lang_string_list
        if string.capitalize().startswith("P")
    ]

    print(P_filtered_string_list)

Output:

    ['Python', 'Perl', 'Php']


---

# 16. Filtering by Type

isinstance() can be used as a filtering condition.

    mixed_values: list[object] = [
        "Shreyas",
        10,
        11.4,
        "Pranay",
        3 + 8j,
        ["xyz"],
    ]

    filtered_names: list[str] = [
        item
        for item in mixed_values
        if isinstance(item, str)
    ]

    print(filtered_names)

Output:

    ['Shreyas', 'Pranay']


---

# 17. Prime Numbers

A comprehension can combine iteration, filtering, and all().

    stop_range: int = 100

    prime_numbers: list[int] = [
        num
        for num in range(2, stop_range + 1)
        if all(
            num % n != 0
            for n in range(2, num)
        )
    ]

    print(prime_numbers)

Output:

    [
        2, 3, 5, 7, 11, 13, 17, 19,
        23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79,
        83, 89, 97
    ]


---

# 18. Filtering and Transformation Together

The expression determines the output.

The condition determines whether the input item is included.

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    squared_even_numbers: list[int] = [
        number**2
        for number in numbers
        if number % 2 == 0
    ]

    print(squared_even_numbers)

Output:

    [4, 16, 36]

Here:

    number**2
        ↓
    determines the output value

while:

    number % 2 == 0
        ↓
    determines whether the item is included.


---

# 19. Multiple Filtering Conditions

Multiple if clauses can be used.

    numbers: list[int] = list(range(1, 21))

    filtered_numbers: list[int] = [
        number
        for number in numbers
        if number > 5
        if number % 2 == 0
    ]

    print(filtered_numbers)

Output:

    [6, 8, 10, 12, 14, 16, 18, 20]

Equivalent logic:

    filtered_numbers: list[int] = []

    for number in numbers:

        if number > 5 and number % 2 == 0:
            filtered_numbers.append(number)


---

# 20. Conditional Value Selection

An if/else expression can select the resulting value.

## Syntax

    [
        value_if_true if condition else value_if_false
        for item in iterable
    ]

Example:

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    number_types: list[str] = [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]

    print(number_types)

Output:

    ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


---

# 21. Filtering vs Conditional Value Selection

This distinction is fundamental.

## Filtering

    [
        number
        for number in numbers
        if number % 2 == 0
    ]

Meaning:

    Include the item only if the condition is True.

Result:

    [2, 4, 6]


## Conditional Value Selection

    [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]

Meaning:

    Every item produces a result,
    but the result depends on the condition.

Result:

    ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


Remember:

    if after the for
        → filtering

    if/else before the for
        → conditional value selection


---

# 22. Can elif Be Used?

elif cannot be used directly inside a comprehension.

This is invalid:

    # Invalid Python

    result = [
        "A"
        if condition_1
        elif condition_2
        else "C"
        for item in items
    ]

A nested conditional expression can technically achieve equivalent logic:

    result = [
        "A"
        if condition_1
        else "B"
        if condition_2
        else "C"
        for item in items
    ]

Conceptually:

    if condition_1:
        "A"

    elif condition_2:
        "B"

    else:
        "C"

However, multiple nested conditional expressions quickly become difficult
to read.

In such cases, use a traditional loop.

    numbers: list[int] = [
        2,
        7,
        12,
        20,
    ]

    number_categories: list[str] = []

    for number in numbers:

        if number > 10:
            number_categories.append("Large")

        elif number > 5:
            number_categories.append("Medium")

        else:
            number_categories.append("Small")

    print(number_categories)

Output:

    ['Small', 'Medium', 'Large', 'Large']


---

# 23. Set Comprehension

Set comprehensions create sets.

## Syntax

    {expression for item in iterable}

Example:

    numbers: list[int] = [
        1,
        2,
        2,
        3,
        3,
        4,
    ]

    unique_squares: set[int] = {
        number**2
        for number in numbers
    }

    print(unique_squares)

Output:

    {1, 4, 9, 16}

Duplicate values are removed because the resulting collection is a set.


---

# 24. Conditional Set Comprehension

    numbers: list[int] = list(range(1, 11))

    even_number_set: set[int] = {
        number
        for number in numbers
        if number % 2 == 0
    }

    print(even_number_set)

Output:

    {2, 4, 6, 8, 10}


---

# 25. Dictionary Comprehension

Dictionary comprehensions create dictionaries.

## Syntax

    {key: value for item in iterable}

Example:

    companies: list[str] = [
        "apple",
        "google",
        "microsoft",
    ]

    company_lengths: dict[str, int] = {
        company: len(company)
        for company in companies
    }

    print(company_lengths)

Output:

    {
        'apple': 5,
        'google': 6,
        'microsoft': 9
    }


---

# 26. Conditional Dictionary Comprehension

    employee_salaries: dict[str, int] = {
        "Alice": 50000,
        "Bob": 75000,
        "Charlie": 60000,
        "David": 90000,
    }

    high_salary_employees: dict[str, int] = {
        employee: salary
        for employee, salary in employee_salaries.items()
        if salary >= 70000
    }

    print(high_salary_employees)

Output:

    {
        'Bob': 75000,
        'David': 90000
    }


---

# 27. Nested Comprehensions

A nested comprehension contains multiple for clauses.

## Syntax

    [
        expression
        for outer_item in outer_iterable
        for inner_item in inner_iterable
    ]

Example:

    numbers: list[int] = [
        1,
        2,
        3,
    ]

    letters: list[str] = [
        "A",
        "B",
        "C",
    ]

    pairs: list[str] = [
        f"{number}{letter}"
        for number in numbers
        for letter in letters
    ]

    print(pairs)

Output:

    [
        '1A', '1B', '1C',
        '2A', '2B', '2C',
        '3A', '3B', '3C'
    ]

Equivalent loops:

    for number in numbers:

        for letter in letters:
            ...


---

# 28. Flattening Nested Lists

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

    flat_list: list[int] = [
        number
        for row in matrix
        for number in row
    ]

    print(flat_list)

Output:

    [1, 2, 3, 4, 5, 6, 7, 8, 10]

Equivalent loops:

    for row in matrix:

        for number in row:
            ...


---

# 29. Nested Transformation

A nested comprehension can preserve the nested structure while
transforming each element.

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10],
    ]

    squared_matrix: list[list[int]] = [
        [
            number**2
            for number in row
        ]
        for row in matrix
    ]

    print(squared_matrix)

Output:

    [
        [1, 4, 9],
        [16, 25, 36],
        [49, 64, 100]
    ]


---

# 30. Cartesian Product

Nested comprehensions can generate every combination of two iterables.

    colors: list[str] = [
        "Red",
        "Green",
        "Blue",
    ]

    sizes: list[str] = [
        "S",
        "M",
        "L",
    ]

    products: list[str] = [
        f"{color}-{size}"
        for color in colors
        for size in sizes
    ]

    print(products)

Output:

    [
        'Red-S', 'Red-M', 'Red-L',
        'Green-S', 'Green-M', 'Green-L',
        'Blue-S', 'Blue-M', 'Blue-L'
    ]


---

# 31. Nested Comprehension with Filtering

Conditions can be added to nested comprehensions.

    numbers: list[int] = [
        1,
        2,
        3,
        4,
    ]

    letters: list[str] = [
        "A",
        "B",
        "C",
        "D",
    ]

    even_number_pairs: list[str] = [
        f"{number}{letter}"
        for number in numbers
        for letter in letters
        if number % 2 == 0
    ]

    print(even_number_pairs)

Output:

    [
        '2A', '2B', '2C', '2D',
        '4A', '4B', '4C', '4D'
    ]


---

# 32. Nested Comprehension with Multiple Conditions

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
    ]

    letters: list[str] = [
        "A",
        "B",
        "C",
    ]

    filtered_pairs: list[str] = [
        f"{number}{letter}"
        for number in numbers
        for letter in letters
        if number % 2 == 0
        if letter != "B"
    ]

    print(filtered_pairs)

Output:

    ['2A', '2C', '4A', '4C']


---

# 33. Nested Set Comprehension

    numbers: list[int] = [
        1,
        2,
        3,
    ]

    letters: list[str] = [
        "A",
        "B",
    ]

    unique_pairs: set[str] = {
        f"{number}{letter}"
        for number in numbers
        for letter in letters
    }

    print(unique_pairs)

The resulting collection is a set.


---

# 34. Nested Dictionary Comprehension

    numbers: list[int] = [
        1,
        2,
        3,
    ]

    number_squares: dict[int, dict[str, int]] = {
        number: {
            "square": number**2,
            "cube": number**3,
        }
        for number in numbers
    }

    print(number_squares)

Output:

    {
        1: {'square': 1, 'cube': 1},
        2: {'square': 4, 'cube': 8},
        3: {'square': 9, 'cube': 27}
    }


---

# 35. Word Frequency — Comprehension Example

This example demonstrates a dictionary comprehension combined with
regular-expression processing.

    import re


    statement: str = (
        "You are most welcome. And honestly, thank you for correcting me "
        "so sharply—that wasn't just a casual catch. In Vedic astrology, "
        "when a person accurately spots an astrological error like that, "
        "it is a clear sign that their 3rd house (intellect and "
        "discernment) and Ketu (intuition) are highly active and "
        "protective. Your dream-self saved that kitten, and your "
        "waking-self just saved yourself from a bad remedy. You are "
        "clearly in tune with your own energy."
    )


    capitalized_clean_words: list[str] = [
        word.capitalize()
        for word in re.findall(
            r"\w+[']?\w+",
            statement,
        )
    ]


    word_count: dict[str, int] = {
        word: capitalized_clean_words.count(word)
        for word in capitalized_clean_words
    }


    print(word_count)

This is a valid comprehension example.

However, there is an important algorithmic consideration:

    list.count()

scans the list every time it is called.

Therefore, the same list may be scanned repeatedly when duplicate words
exist.

The example is useful for demonstrating comprehension syntax, but it is
not the preferred implementation for large-scale frequency counting.


---

# 36. Word Frequency — Alternate Solution

A traditional dictionary-based loop avoids repeatedly scanning the list.

    word_count_2: dict[str, int] = {}

    for word in capitalized_clean_words:

        if word in word_count_2:

            word_count_2[word] += 1

        else:

            word_count_2[word] = 1

    print(word_count_2)


---

# 37. Word Frequency — defaultdict

defaultdict can simplify the counting operation.

    from collections import defaultdict


    word_count_3: defaultdict[str, int] = defaultdict(int)


    for word in capitalized_clean_words:

        word_count_3[word] += 1


    print(word_count_3)

The defaultdict automatically creates a default integer value of 0 for
a missing key.

Therefore:

    word_count_3[word] += 1

works without explicitly checking whether the key already exists.


---

# 38. Comprehension vs Traditional Loop

Comprehension:

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

Traditional loop:

    squared_numbers: list[int] = []

    for number in numbers:

        squared_numbers.append(number**2)

The comprehension is more compact.

The loop is more explicit.

Neither is universally better.

The correct choice depends on readability and complexity.


---

# 39. When a Comprehension Is a Good Choice

A comprehension is generally appropriate when:

- A collection is being created.
- The transformation is simple.
- Filtering is straightforward.
- The expression is easy to understand.
- The resulting code is readable.

Example:

    numbers: list[int] = list(range(1, 11))

    squared_even_numbers: list[int] = [
        number**2
        for number in numbers
        if number % 2 == 0
    ]

    print(squared_even_numbers)

Output:

    [4, 16, 36, 64, 100]


---

# 40. When a Traditional Loop Is Better

Prefer a traditional loop when:

- Multiple processing steps are required.
- Several branches exist.
- Intermediate values need to be inspected.
- Debugging is important.
- Side effects are the purpose of the loop.
- The expression becomes difficult to understand.
- Nesting becomes excessive.
- The algorithm is easier to express procedurally.

Example:

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
    ]

    processed_numbers: list[int] = []

    for number in numbers:

        squared_number: int = number**2

        if squared_number > 10:

            adjusted_number: int = squared_number + 100

            processed_numbers.append(adjusted_number)

    print(processed_numbers)

Output:

    [116, 125]


---

# 41. Multiple Branches

A normal loop is generally clearer when multiple branches are required.

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    classified_numbers: list[str] = []

    for number in numbers:

        if number % 3 == 0:

            classified_numbers.append(
                "Divisible by 3"
            )

        elif number % 2 == 0:

            classified_numbers.append(
                "Even"
            )

        else:

            classified_numbers.append(
                "Other"
            )

    print(classified_numbers)

Output:

    [
        'Other',
        'Even',
        'Divisible by 3',
        'Even',
        'Other',
        'Divisible by 3'
    ]


---

# 42. Side Effects

Comprehensions should primarily be used for collection construction.

Avoid:

    [print(company) for company in companies]

The comprehension creates a list that is not useful.

Prefer:

    for company in companies:

        print(company)

The purpose of the loop is immediately clear.


---

# 43. Readability Over Cleverness

A comprehension should make the code easier to understand.

Good:

    even_numbers: list[int] = [
        number
        for number in numbers
        if number % 2 == 0
    ]

Potentially problematic:

    result = [
        complicated_expression
        for outer_item in outer_items
        for inner_item in inner_items
        if condition_one
        if condition_two
        if another_complex_condition
    ]

Python allows complex comprehensions.

That does not mean complex comprehensions are always good code.

If the comprehension requires significant mental effort to understand,
a normal loop may be the better design.


---

# 44. Avoid Repeated Expensive Work

Concise syntax does not automatically mean an efficient algorithm.

For example:

    word_count: dict[str, int] = {
        word: capitalized_clean_words.count(word)
        for word in capitalized_clean_words
    }

count() scans the list every time it is called.

For large collections, use a counting approach such as:

    from collections import defaultdict


    word_count: defaultdict[str, int] = defaultdict(int)


    for word in capitalized_clean_words:

        word_count[word] += 1

Important principle:

    Concise syntax
        ≠
    Efficient algorithm


---

# 45. Avoid Repeating Complex Expressions

If an expression is complicated or needs to be reused, calculate it
separately.

For example:

    import re


    statement: str = (
        "Python Python SQL Java Python SQL"
    )


    capitalized_clean_words: list[str] = [
        word.capitalize()
        for word in re.findall(
            r"\w+[']?\w+",
            statement,
        )
    ]

The processed collection can then be reused.

This is generally clearer than repeating the same processing expression
inside several comprehensions.


---

# 46. Formatting Long Comprehensions

Long comprehensions should be formatted vertically.

Prefer:

    high_salary_employees: dict[str, int] = {
        employee: salary
        for employee, salary in employee_salaries.items()
        if salary >= 70000
    }

instead of:

    high_salary_employees = {employee: salary for employee, salary in employee_salaries.items() if salary >= 70000}

Vertical formatting makes the structure easier to inspect.


---

# 47. Type Annotations

Comprehensions should maintain accurate type information.

List:

    numbers: list[int] = [1, 2, 3]

    squared_numbers: list[int] = [
        number**2
        for number in numbers
    ]

Set:

    unique_numbers: set[int] = {
        number
        for number in numbers
    }

Dictionary:

    number_squares: dict[int, int] = {
        number: number**2
        for number in numbers
    }

The annotation should describe the resulting collection.


---

# 48. Complexity Considerations

A comprehension does not magically change the algorithmic complexity of
the operation.

For example:

    [
        number**2
        for number in numbers
    ]

performs one transformation for each input element.

If the input contains n elements, this is generally O(n).

A nested comprehension:

    [
        f"{number}{letter}"
        for number in numbers
        for letter in letters
    ]

produces combinations of both collections.

If there are n numbers and m letters, the number of combinations is:

    O(n × m)

Therefore, always consider the underlying loops.

Comprehension syntax is primarily a readability and expression tool, not
an automatic performance optimization.


---

# 49. Comprehension Decision Guide

Use a comprehension when:

    Creating a collection
            +
    Simple transformation/filtering
            +
    Easy to read
            =
    Good comprehension candidate


Use a traditional loop when:

    Multiple steps
            OR
    Multiple branches
            OR
    Complex logic
            OR
    Side effects
            OR
    Difficult debugging
            =
    Prefer a loop


---

# 50. Complete Syntax Reference

## List Comprehension

    [expression for item in iterable]


## Conditional List Comprehension

    [
        expression
        for item in iterable
        if condition
    ]


## Conditional Value Selection

    [
        value_if_true if condition else value_if_false
        for item in iterable
    ]


## Set Comprehension

    {
        expression
        for item in iterable
    }


## Conditional Set Comprehension

    {
        expression
        for item in iterable
        if condition
    }


## Dictionary Comprehension

    {
        key: value
        for item in iterable
    }


## Conditional Dictionary Comprehension

    {
        key: value
        for item in iterable
        if condition
    }


## Nested Comprehension

    [
        expression
        for outer_item in outer_iterable
        for inner_item in inner_iterable
    ]


---

# 51. File-by-File Learning Path

The folder is structured as follows:

    01_list_comprehensions.py

        Basic list comprehension syntax.


    02_conditional_list_comprehensions.py

        Filtering and conditional list construction.


    03_nested_list_comprehensions.py

        Nested iteration and nested list structures.


    04_set_comprehensions.py

        Set comprehension syntax and behavior.


    05_dict_comprehensions.py

        Dictionary comprehension syntax.


    06_conditional_comprehensions.py

        Filtering and conditional value selection across comprehensions.


    07_nested_comprehensions.py

        Nested comprehensions and multi-level iteration.


    08_comprehension_vs_loop.py

        Comparing comprehensions with traditional loops.


    09_comprehension_best_practices.py

        Readability, maintainability, complexity, and practical guidelines.


---

# 52. Important Rules

    1. List comprehensions create lists.

    2. Set comprehensions create sets.

    3. Dictionary comprehensions create dictionaries.

    4. A trailing if filters items.

    5. An if/else before the for selects the resulting value.

    6. elif cannot be used directly inside a comprehension.

    7. Multiple for clauses represent nested loops.

    8. Comprehensions should primarily construct collections.

    9. Avoid using comprehensions only for side effects.

    10. Avoid excessive nesting.

    11. Avoid unnecessarily complicated expressions.

    12. Consider algorithmic complexity.

    13. Use descriptive variable names.

    14. Keep type annotations accurate.

    15. Prefer readability over cleverness.

    16. A traditional loop is sometimes better than a comprehension.


---

# 53. Final Principle

The purpose of learning comprehensions is not to make every loop shorter.

The purpose is to recognize when collection-building logic can be expressed
more clearly and naturally using comprehension syntax.

A good comprehension is:

    Clear
      +
    Readable
      +
    Correct
      +
    Appropriate


The guiding principles are:

    Readability > Cleverness

    Clarity > Brevity

    Correctness > Compactness

    Appropriate algorithm > Forced comprehension


Once these principles become natural, comprehensions become a practical
Python tool rather than merely a compact syntax feature.

