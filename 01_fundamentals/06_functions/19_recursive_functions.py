# =============================================================================
# 19. Recursive Functions
# =============================================================================
# type: ignore

"""
Python Functions

File:
19_recursive_functions.py

Topic:
Recursive Functions

Overview:

A recursive function is a function that calls itself.

Recursion is useful when a problem can naturally be divided into smaller
versions of the same problem.

A recursive function normally contains two important parts:

1. Base case
2. Recursive case

The base case tells the function when to stop.

The recursive case makes the function call itself with a smaller or simpler
problem.

General structure:

    def recursive_function(value: int) -> int:
        if base_case:
            return result

        return recursive_function(smaller_value)

Without a base case, a recursive function can continue calling itself until
Python raises RecursionError.

Topics covered:

    - What is recursion?
    - Recursive functions
    - Base cases
    - Recursive cases
    - Simple recursion
    - Countdown recursion
    - Count-up recursion
    - Factorial
    - Fibonacci numbers
    - Sum of numbers
    - Product of numbers
    - Power calculation
    - String reversal
    - Palindrome checking
    - Greatest common divisor
    - Recursive multiplication
    - Recursive counting
    - Recursive list processing
    - Recursive maximum
    - Recursive minimum
    - Recursive searching
    - Recursive binary search
    - Nested recursive structures
    - Recursive tree traversal
    - Recursive directory-style traversal
    - Multiple recursive calls
    - Recursion depth
    - RecursionError
    - Recursion versus iteration
    - Advantages of recursion
    - Disadvantages of recursion
    - Tail recursion
    - Python and tail-call optimization
    - Memoization
    - Recursive Fibonacci with memoization
    - Recursive function design
    - Common recursion mistakes
    - Practical recursion rules
"""

# =============================================================================
# 01. What Is Recursion?
# =============================================================================
"""
Recursion means that a function calls itself.

A recursive function solves a problem by reducing it into a smaller version
of the same problem.

Conceptually:

    problem
        |
        v
    smaller problem
        |
        v
    smaller problem
        |
        v
    base case

For example:

    countdown(5)

can become:

    countdown(5)
        -> countdown(4)
            -> countdown(3)
                -> countdown(2)
                    -> countdown(1)
                        -> countdown(0)

At 0, the base case stops the recursion.
"""


# =============================================================================
# 02. Basic Recursive Function
# =============================================================================

def say_hello_recursively(
    count: int,
) -> None:
    """
    Print a message recursively.
    """
    if count <= 0:
        return

    print("Hello")

    say_hello_recursively(
        count - 1,
    )


say_hello_recursively(
    3,
)


# =============================================================================
# 03. Base Case
# =============================================================================
"""
The base case is the condition that stops recursion.

Example:

    if count <= 0:
        return

Without this condition, the function would continue calling itself.

A recursive function should normally have a clearly identifiable base case.
"""


# =============================================================================
# 04. Recursive Case
# =============================================================================

def countdown(
    number: int,
) -> None:
    """
    Count down from number to zero.
    """
    if number <= 0:
        print("Done")
        return

    print(number)

    countdown(
        number - 1,
    )


countdown(
    5,
)


# =============================================================================
# 05. Understanding Countdown
# =============================================================================
"""
Calling:

    countdown(3)

produces:

    countdown(3)
        prints 3
        calls countdown(2)

    countdown(2)
        prints 2
        calls countdown(1)

    countdown(1)
        prints 1
        calls countdown(0)

    countdown(0)
        prints Done
        returns

The recursive call always moves toward the base case.
"""


# =============================================================================
# 06. Count Up Recursively
# =============================================================================

def count_up(
    current: int,
    maximum: int,
) -> None:
    """
    Count upward from current to maximum.
    """
    if current > maximum:
        return

    print(current)

    count_up(
        current + 1,
        maximum,
    )


count_up(
    1,
    5,
)


# =============================================================================
# 07. Countdown With a Return Value
# =============================================================================

def countdown_message(
    number: int,
) -> str:
    """
    Return a message recursively.
    """
    if number <= 0:
        return "Done"

    return f"{number} -> {countdown_message(number - 1)}"


countdown_result: str = countdown_message(
    3,
)

print(
    countdown_result,
)


# =============================================================================
# 08. Factorial
# =============================================================================
"""
Factorial is a classic recursion example.

Mathematically:

    5! = 5 * 4 * 3 * 2 * 1

Therefore:

    5! = 120

The recursive definition is:

    n! = n * (n - 1)!

Base case:

    0! = 1

Recursive case:

    n! = n * factorial(n - 1)
"""


def factorial(
    number: int,
) -> int:
    """
    Calculate factorial recursively.
    """
    if number < 0:
        raise ValueError(
            "Factorial is not defined for negative integers.",
        )

    if number == 0:
        return 1

    return number * factorial(
        number - 1,
    )


factorial_result: int = factorial(
    5,
)

print(
    factorial_result,
)


# =============================================================================
# 09. Factorial Step-by-Step
# =============================================================================
"""
factorial(4)

becomes:

    4 * factorial(3)

then:

    4 * 3 * factorial(2)

then:

    4 * 3 * 2 * factorial(1)

then:

    4 * 3 * 2 * 1 * factorial(0)

then the base case:

    factorial(0) = 1

The calls then return in reverse order:

    1
    1 * 1 = 1
    2 * 1 = 2
    3 * 2 = 6
    4 * 6 = 24
"""


# =============================================================================
# 10. Sum From 1 To N
# =============================================================================

def sum_to(
    number: int,
) -> int:
    """
    Calculate the sum from 1 through number recursively.
    """
    if number <= 0:
        return 0

    return number + sum_to(
        number - 1,
    )


sum_result: int = sum_to(
    5,
)

print(
    sum_result,
)


# =============================================================================
# 11. Sum To N Explanation
# =============================================================================
"""
sum_to(5)

becomes:

    5 + sum_to(4)

then:

    5 + 4 + sum_to(3)

then:

    5 + 4 + 3 + sum_to(2)

then:

    5 + 4 + 3 + 2 + sum_to(1)

then:

    5 + 4 + 3 + 2 + 1 + sum_to(0)

Base case:

    sum_to(0) = 0

Result:

    15
"""


# =============================================================================
# 12. Product From 1 To N
# =============================================================================

def product_to(
    number: int,
) -> int:
    """
    Calculate the product from 1 through number recursively.
    """
    if number <= 0:
        return 1

    return number * product_to(
        number - 1,
    )


product_result: int = product_to(
    5,
)

print(
    product_result,
)


# =============================================================================
# 13. Recursive Power
# =============================================================================

def power(
    base: int,
    exponent: int,
) -> int:
    """
    Calculate base raised to exponent recursively.
    """
    if exponent < 0:
        raise ValueError(
            "This function expects a non-negative exponent.",
        )

    if exponent == 0:
        return 1

    return base * power(
        base,
        exponent - 1,
    )


power_result: int = power(
    2,
    5,
)

print(
    power_result,
)


# =============================================================================
# 14. Power Explanation
# =============================================================================
"""
power(2, 4)

becomes:

    2 * power(2, 3)

then:

    2 * 2 * power(2, 2)

then:

    2 * 2 * 2 * power(2, 1)

then:

    2 * 2 * 2 * 2 * power(2, 0)

Base case:

    power(2, 0) = 1

Result:

    16
"""


# =============================================================================
# 15. Fibonacci Numbers
# =============================================================================
"""
The Fibonacci sequence is:

    0, 1, 1, 2, 3, 5, 8, 13, 21, ...

The recursive definition is:

    fibonacci(0) = 0
    fibonacci(1) = 1

For all larger values:

    fibonacci(n) =
        fibonacci(n - 1) + fibonacci(n - 2)

This is an example of recursion with two recursive calls.
"""


def fibonacci(
    number: int,
) -> int:
    """
    Calculate a Fibonacci number recursively.
    """
    if number < 0:
        raise ValueError(
            "Fibonacci is not defined for negative indexes.",
        )

    if number == 0:
        return 0

    if number == 1:
        return 1

    return (
        fibonacci(number - 1)
        + fibonacci(number - 2)
    )


fibonacci_result: int = fibonacci(
    10,
)

print(
    fibonacci_result,
)


# =============================================================================
# 16. Multiple Recursive Calls
# =============================================================================
"""
Fibonacci demonstrates that a recursive function can call itself more than
once.

For example:

    fibonacci(5)

requires:

    fibonacci(4)
    fibonacci(3)

Then fibonacci(4) requires:

    fibonacci(3)
    fibonacci(2)

This creates a branching recursion tree.

The naive recursive Fibonacci implementation therefore performs many repeated
calculations.
"""


# =============================================================================
# 17. Recursive String Reversal
# =============================================================================

def reverse_string(
    text: str,
) -> str:
    """
    Reverse a string recursively.
    """
    if len(text) <= 1:
        return text

    return (
        reverse_string(text[1:])
        + text[0]
    )


reversed_text: str = reverse_string(
    "Python",
)

print(
    reversed_text,
)


# =============================================================================
# 18. Reverse String Explanation
# =============================================================================
"""
reverse_string("cat")

becomes:

    reverse_string("at") + "c"

then:

    reverse_string("t") + "a" + "c"

then:

    "t" + "a" + "c"

Result:

    "tac"

The base case is a string containing zero or one character.
"""


# =============================================================================
# 19. Palindrome Checking
# =============================================================================
"""
A palindrome reads the same forward and backward.

Examples:

    "level"
    "radar"
    "madam"

A recursive palindrome check can compare the first and last characters.

If they match, the function recursively checks the middle portion.
"""


def is_palindrome(
    text: str,
) -> bool:
    """
    Check whether a string is a palindrome recursively.
    """
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(
        text[1:-1],
    )


palindrome_result: bool = is_palindrome(
    "level",
)

print(
    palindrome_result,
)


# =============================================================================
# 20. Palindrome With Normalized Text
# =============================================================================

def is_normalized_palindrome(
    text: str,
) -> bool:
    """
    Check a normalized string recursively.
    """
    normalized: str = (
        text.lower()
        .replace(" ", "")
    )

    return is_palindrome(
        normalized,
    )


normalized_palindrome: bool = is_normalized_palindrome(
    "Never Odd Or Even",
)

print(
    normalized_palindrome,
)


# =============================================================================
# 21. Recursive String Length
# =============================================================================

def recursive_length(
    text: str,
) -> int:
    """
    Calculate string length recursively.
    """
    if text == "":
        return 0

    return 1 + recursive_length(
        text[1:],
    )


text_length: int = recursive_length(
    "Python",
)

print(
    text_length,
)


# =============================================================================
# 22. Greatest Common Divisor
# =============================================================================
"""
The Euclidean algorithm provides a natural recursive solution for calculating
the greatest common divisor.

The rule is:

    gcd(a, b) = gcd(b, a % b)

The base case is:

    gcd(a, 0) = a
"""


def greatest_common_divisor(
    first: int,
    second: int,
) -> int:
    """
    Calculate the greatest common divisor recursively.
    """
    first = abs(first)
    second = abs(second)

    if second == 0:
        return first

    return greatest_common_divisor(
        second,
        first % second,
    )


gcd_result: int = greatest_common_divisor(
    48,
    18,
)

print(
    gcd_result,
)


# =============================================================================
# 23. Recursive Multiplication
# =============================================================================

def multiply_recursively(
    first: int,
    second: int,
) -> int:
    """
    Multiply two non-negative integers recursively.
    """
    if first < 0 or second < 0:
        raise ValueError(
            "This function expects non-negative integers.",
        )

    if second == 0:
        return 0

    return (
        first
        + multiply_recursively(
            first,
            second - 1,
        )
    )


multiplication_result: int = multiply_recursively(
    6,
    4,
)

print(
    multiplication_result,
)


# =============================================================================
# 24. Recursive Counting
# =============================================================================

def count_occurrences(
    values: list[int],
    target: int,
) -> int:
    """
    Count target occurrences recursively.
    """
    if not values:
        return 0

    current_count: int = (
        1
        if values[0] == target
        else 0
    )

    return (
        current_count
        + count_occurrences(
            values[1:],
            target,
        )
    )


occurrence_count: int = count_occurrences(
    [1, 2, 2, 3, 2],
    2,
)

print(
    occurrence_count,
)


# =============================================================================
# 25. Recursive List Sum
# =============================================================================

def recursive_list_sum(
    values: list[int],
) -> int:
    """
    Calculate the sum of a list recursively.
    """
    if not values:
        return 0

    return (
        values[0]
        + recursive_list_sum(
            values[1:],
        )
    )


list_sum_result: int = recursive_list_sum(
    [10, 20, 30, 40],
)

print(
    list_sum_result,
)


# =============================================================================
# 26. Recursive List Product
# =============================================================================

def recursive_list_product(
    values: list[int],
) -> int:
    """
    Calculate the product of a list recursively.
    """
    if not values:
        return 1

    return (
        values[0]
        * recursive_list_product(
            values[1:],
        )
    )


list_product_result: int = recursive_list_product(
    [2, 3, 4],
)

print(
    list_product_result,
)


# =============================================================================
# 27. Recursive Maximum
# =============================================================================

def recursive_max(
    values: list[int],
) -> int:
    """
    Find the maximum value recursively.
    """
    if not values:
        raise ValueError(
            "Cannot find the maximum of an empty list.",
        )

    if len(values) == 1:
        return values[0]

    remaining_max: int = recursive_max(
        values[1:],
    )

    return (
        values[0]
        if values[0] > remaining_max
        else remaining_max
    )


maximum_result: int = recursive_max(
    [10, 50, 20, 80, 30],
)

print(
    maximum_result,
)


# =============================================================================
# 28. Recursive Minimum
# =============================================================================

def recursive_min(
    values: list[int],
) -> int:
    """
    Find the minimum value recursively.
    """
    if not values:
        raise ValueError(
            "Cannot find the minimum of an empty list.",
        )

    if len(values) == 1:
        return values[0]

    remaining_min: int = recursive_min(
        values[1:],
    )

    return (
        values[0]
        if values[0] < remaining_min
        else remaining_min
    )


minimum_result: int = recursive_min(
    [10, 50, 20, 80, 30],
)

print(
    minimum_result,
)


# =============================================================================
# 29. Recursive List Search
# =============================================================================

def recursive_contains(
    values: list[int],
    target: int,
) -> bool:
    """
    Search for a value recursively.
    """
    if not values:
        return False

    if values[0] == target:
        return True

    return recursive_contains(
        values[1:],
        target,
    )


contains_result: bool = recursive_contains(
    [10, 20, 30, 40],
    30,
)

print(
    contains_result,
)


# =============================================================================
# 30. Recursive Linear Search
# =============================================================================

def recursive_linear_search(
    values: list[int],
    target: int,
    index: int = 0,
) -> int:
    """
    Find target index using recursive linear search.

    Returns:
        The target index, or -1 if the target is not found.
    """
    if index >= len(values):
        return -1

    if values[index] == target:
        return index

    return recursive_linear_search(
        values,
        target,
        index + 1,
    )


search_index: int = recursive_linear_search(
    [10, 20, 30, 40, 50],
    40,
)

print(
    search_index,
)


# =============================================================================
# 31. Recursive Binary Search
# =============================================================================
"""
Binary search requires a sorted list.

The algorithm repeatedly checks the middle element.

If the target is smaller than the middle element, search the left half.

If the target is larger than the middle element, search the right half.

If the target equals the middle element, return the index.

This naturally produces recursive subproblems.
"""


def recursive_binary_search(
    values: list[int],
    target: int,
    low: int,
    high: int,
) -> int:
    """
    Search a sorted list recursively using binary search.
    """
    if low > high:
        return -1

    middle: int = (low + high) // 2

    if values[middle] == target:
        return middle

    if target < values[middle]:
        return recursive_binary_search(
            values,
            target,
            low,
            middle - 1,
        )

    return recursive_binary_search(
        values,
        target,
        middle + 1,
        high,
    )


sorted_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
    60,
]

binary_search_result: int = recursive_binary_search(
    sorted_values,
    40,
    0,
    len(sorted_values) - 1,
)

print(
    binary_search_result,
)


# =============================================================================
# 32. Recursive Binary Search Helper
# =============================================================================

def binary_search(
    values: list[int],
    target: int,
) -> int:
    """
    Public wrapper around recursive binary search.
    """
    if not values:
        return -1

    return recursive_binary_search(
        values,
        target,
        0,
        len(values) - 1,
    )


binary_search_index: int = binary_search(
    sorted_values,
    50,
)

print(
    binary_search_index,
)


# =============================================================================
# 33. Recursive List Flattening
# =============================================================================
"""
Nested lists are a common example where recursion is useful.

A nested structure can contain:

    value
    value
    list
        value
        list
            value

Recursion can process each nested list using the same logic.
"""

from typing import TypeAlias


NestedInteger: TypeAlias = int | list["NestedInteger"]


def flatten(
    values: list[NestedInteger],
) -> list[int]:
    """
    Flatten a nested integer list recursively.
    """
    result: list[int] = []

    for value in values:
        if isinstance(value, int):
            result.append(
                value,
            )
        else:
            result.extend(
                flatten(
                    value,
                ),
            )

    return result


nested_values: list[NestedInteger] = [
    1,
    [
        2,
        3,
    ],
    [
        4,
        [
            5,
            6,
        ],
    ],
]

flattened_values: list[int] = flatten(
    nested_values,
)

print(
    flattened_values,
)


# =============================================================================
# 34. Recursive Nested List Sum
# =============================================================================

def nested_sum(
    values: list[NestedInteger],
) -> int:
    """
    Calculate the sum of nested integers recursively.
    """
    total: int = 0

    for value in values:
        if isinstance(value, int):
            total += value
        else:
            total += nested_sum(
                value,
            )

    return total


nested_sum_result: int = nested_sum(
    nested_values,
)

print(
    nested_sum_result,
)


# =============================================================================
# 35. Recursive Tree Node
# =============================================================================

class TreeNode:
    """
    Represent a node in a binary tree.
    """

    def __init__(
        self,
        value: int,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.value: int = value
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# =============================================================================
# 36. Creating a Tree
# =============================================================================

tree: TreeNode = TreeNode(
    10,
    left=TreeNode(
        5,
        left=TreeNode(2),
        right=TreeNode(7),
    ),
    right=TreeNode(
        15,
        left=TreeNode(12),
        right=TreeNode(20),
    ),
)


# =============================================================================
# 37. Recursive Tree Traversal
# =============================================================================

def inorder_traversal(
    node: TreeNode | None,
) -> list[int]:
    """
    Traverse a binary tree using recursive inorder traversal.
    """
    if node is None:
        return []

    values: list[int] = []

    values.extend(
        inorder_traversal(
            node.left,
        ),
    )

    values.append(
        node.value,
    )

    values.extend(
        inorder_traversal(
            node.right,
        ),
    )

    return values


inorder_values: list[int] = inorder_traversal(
    tree,
)

print(
    inorder_values,
)


# =============================================================================
# 38. Recursive Preorder Traversal
# =============================================================================

def preorder_traversal(
    node: TreeNode | None,
) -> list[int]:
    """
    Traverse a binary tree using recursive preorder traversal.
    """
    if node is None:
        return []

    values: list[int] = [
        node.value,
    ]

    values.extend(
        preorder_traversal(
            node.left,
        ),
    )

    values.extend(
        preorder_traversal(
            node.right,
        ),
    )

    return values


preorder_values: list[int] = preorder_traversal(
    tree,
)

print(
    preorder_values,
)


# =============================================================================
# 39. Recursive Postorder Traversal
# =============================================================================

def postorder_traversal(
    node: TreeNode | None,
) -> list[int]:
    """
    Traverse a binary tree using recursive postorder traversal.
    """
    if node is None:
        return []

    values: list[int] = []

    values.extend(
        postorder_traversal(
            node.left,
        ),
    )

    values.extend(
        postorder_traversal(
            node.right,
        ),
    )

    values.append(
        node.value,
    )

    return values


postorder_values: list[int] = postorder_traversal(
    tree,
)

print(
    postorder_values,
)


# =============================================================================
# 40. Recursive Tree Search
# =============================================================================

def tree_contains(
    node: TreeNode | None,
    target: int,
) -> bool:
    """
    Search a binary tree recursively.
    """
    if node is None:
        return False

    if node.value == target:
        return True

    return (
        tree_contains(
            node.left,
            target,
        )
        or tree_contains(
            node.right,
            target,
        )
    )


tree_search_result: bool = tree_contains(
    tree,
    12,
)

print(
    tree_search_result,
)


# =============================================================================
# 41. Recursive Tree Height
# =============================================================================

def tree_height(
    node: TreeNode | None,
) -> int:
    """
    Calculate the height of a binary tree recursively.
    """
    if node is None:
        return 0

    left_height: int = tree_height(
        node.left,
    )

    right_height: int = tree_height(
        node.right,
    )

    return 1 + max(
        left_height,
        right_height,
    )


tree_height_result: int = tree_height(
    tree,
)

print(
    tree_height_result,
)


# =============================================================================
# 42. Recursive Tree Node Count
# =============================================================================

def count_tree_nodes(
    node: TreeNode | None,
) -> int:
    """
    Count binary tree nodes recursively.
    """
    if node is None:
        return 0

    return (
        1
        + count_tree_nodes(node.left)
        + count_tree_nodes(node.right)
    )


tree_node_count: int = count_tree_nodes(
    tree,
)

print(
    tree_node_count,
)


# =============================================================================
# 43. Multiple Base Cases
# =============================================================================

def fibonacci_with_multiple_base_cases(
    number: int,
) -> int:
    """
    Calculate Fibonacci using two base cases.
    """
    if number < 0:
        raise ValueError(
            "The index cannot be negative.",
        )

    if number == 0:
        return 0

    if number == 1:
        return 1

    return (
        fibonacci_with_multiple_base_cases(
            number - 1,
        )
        + fibonacci_with_multiple_base_cases(
            number - 2,
        )
    )


fibonacci_multiple_base_result: int = (
    fibonacci_with_multiple_base_cases(
        8,
    )
)

print(
    fibonacci_multiple_base_result,
)


# =============================================================================
# 44. Recursion With Accumulated State
# =============================================================================

def recursive_sum_with_index(
    values: list[int],
    index: int = 0,
) -> int:
    """
    Sum a list recursively using an index.
    """
    if index >= len(values):
        return 0

    return (
        values[index]
        + recursive_sum_with_index(
            values,
            index + 1,
        )
    )


indexed_sum_result: int = recursive_sum_with_index(
    [5, 10, 15],
)

print(
    indexed_sum_result,
)


# =============================================================================
# 45. Recursion With an Accumulator
# =============================================================================

def recursive_sum_with_accumulator(
    values: list[int],
    index: int = 0,
    total: int = 0,
) -> int:
    """
    Sum values recursively using an accumulator.
    """
    if index >= len(values):
        return total

    return recursive_sum_with_accumulator(
        values,
        index + 1,
        total + values[index],
    )


accumulator_sum_result: int = recursive_sum_with_accumulator(
    [10, 20, 30],
)

print(
    accumulator_sum_result,
)


# =============================================================================
# 46. Recursion and Call Stack
# =============================================================================
"""
Every active function call occupies a frame on the call stack.

For:

    factorial(4)

the stack conceptually grows like:

    factorial(4)
    factorial(3)
    factorial(2)
    factorial(1)
    factorial(0)

When factorial(0) returns, the stack unwinds:

    factorial(0) returns 1
    factorial(1) returns 1
    factorial(2) returns 2
    factorial(3) returns 6
    factorial(4) returns 24

Therefore recursion consumes call-stack space.
"""


# =============================================================================
# 47. Recursion Depth
# =============================================================================
"""
Python limits recursion depth to prevent unlimited call-stack growth.

A deeply recursive function can eventually raise:

    RecursionError

Example of an unsafe recursive pattern:

    def infinite_recursion() -> None:
        infinite_recursion()

Do not execute an infinite recursive function.

A recursive function should always have a path to its base case.
"""


# =============================================================================
# 48. RecursionError
# =============================================================================

def safe_recursive_function(
    number: int,
) -> int:
    """
    Recursively count down to zero.
    """
    if number <= 0:
        return 0

    return safe_recursive_function(
        number - 1,
    )


safe_recursion_result: int = safe_recursive_function(
    100,
)

print(
    safe_recursion_result,
)

# The function above has a reachable base case and terminates normally.


# =============================================================================
# 49. Recursive Case Must Approach the Base Case
# =============================================================================
"""
Consider:

    def countdown(number: int) -> None:
        if number <= 0:
            return

        countdown(number - 1)

The recursive argument becomes:

    5
    4
    3
    2
    1
    0

It approaches the base case.

A dangerous implementation would be:

    countdown(number + 1)

because the argument moves away from the base case.

The recursive step should make measurable progress toward termination.
"""


# =============================================================================
# 50. Recursion Versus Iteration
# =============================================================================

def factorial_iterative(
    number: int,
) -> int:
    """
    Calculate factorial iteratively.
    """
    if number < 0:
        raise ValueError(
            "Factorial is not defined for negative integers.",
        )

    result: int = 1

    for current in range(
        2,
        number + 1,
    ):
        result *= current

    return result


factorial_iterative_result: int = factorial_iterative(
    5,
)

print(
    factorial_iterative_result,
)


# =============================================================================
# 51. Recursive Versus Iterative Factorial
# =============================================================================

recursive_factorial_result: int = factorial(
    5,
)

iterative_factorial_result: int = factorial_iterative(
    5,
)

print(
    recursive_factorial_result,
)

print(
    iterative_factorial_result,
)

# Both approaches produce the same result.


# =============================================================================
# 52. Recursion Is Not Always Better
# =============================================================================
"""
Recursion can make some algorithms easier to express.

However, recursion is not automatically better than iteration.

For simple repetition, a loop is often easier to understand and more
memory-efficient.

For example:

    for number in range(5):
        print(number)

is usually simpler than recursively printing five numbers.

Recursion becomes especially useful when the problem itself has a recursive
structure.
"""


# =============================================================================
# 53. When Recursion Is Useful
# =============================================================================
"""
Recursion is particularly useful for:

    - tree traversal
    - graph algorithms
    - divide-and-conquer algorithms
    - directory traversal
    - nested data structures
    - parsing nested expressions
    - backtracking
    - combinatorial algorithms
    - mathematical definitions
    - algorithms naturally expressed as smaller subproblems
"""


# =============================================================================
# 54. Advantages of Recursion
# =============================================================================
"""
Advantages:

    1. Can closely match mathematical definitions.

    2. Can make tree algorithms natural to write.

    3. Can simplify nested-data processing.

    4. Can make divide-and-conquer algorithms easier to express.

    5. Can reduce complicated loop state.

    6. Can produce elegant solutions for naturally recursive problems.
"""


# =============================================================================
# 55. Disadvantages of Recursion
# =============================================================================
"""
Disadvantages:

    1. Every recursive call consumes call-stack space.

    2. Deep recursion can raise RecursionError.

    3. Recursive code can be harder to debug.

    4. Poorly designed recursion can perform unnecessary repeated work.

    5. Python does not optimize tail-recursive calls away.

    6. Iterative solutions can sometimes be faster and simpler.
"""


# =============================================================================
# 56. Tail Recursion
# =============================================================================
"""
A tail-recursive function performs its recursive call as its final operation.

Example:

    def countdown(
        number: int,
    ) -> None:
        if number <= 0:
            return

        print(number)
        countdown(number - 1)

The recursive call is the final operation after the print statement.

Some programming languages optimize tail recursion.

Python does not perform general tail-call optimization.

Therefore tail recursion can still consume one stack frame per recursive call.
"""


# =============================================================================
# 57. Tail-Recursive Style Example
# =============================================================================

def factorial_tail_style(
    number: int,
    accumulator: int = 1,
) -> int:
    """
    Calculate factorial using accumulator-based recursion.
    """
    if number < 0:
        raise ValueError(
            "Factorial is not defined for negative integers.",
        )

    if number == 0:
        return accumulator

    return factorial_tail_style(
        number - 1,
        accumulator * number,
    )


tail_factorial_result: int = factorial_tail_style(
    5,
)

print(
    tail_factorial_result,
)


# =============================================================================
# 58. Memoization
# =============================================================================
"""
Memoization stores previously calculated results.

This is particularly useful when recursive calls repeatedly solve the same
subproblem.

Naive Fibonacci recursion repeats many calculations.

For example:

    fibonacci(5)

requires fibonacci(3) more than once.

Memoization allows already-calculated values to be reused.
"""


# =============================================================================
# 59. Fibonacci With Memoization
# =============================================================================

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_memoized(
    number: int,
) -> int:
    """
    Calculate Fibonacci recursively with memoization.
    """
    if number < 0:
        raise ValueError(
            "The index cannot be negative.",
        )

    if number == 0:
        return 0

    if number == 1:
        return 1

    return (
        fibonacci_memoized(number - 1)
        + fibonacci_memoized(number - 2)
    )


memoized_fibonacci_result: int = fibonacci_memoized(
    30,
)

print(
    memoized_fibonacci_result,
)


# =============================================================================
# 60. Why Memoization Helps
# =============================================================================
"""
Without memoization:

    fibonacci(30)

causes many repeated recursive calculations.

With memoization:

    fibonacci_memoized(30)

once a value has been calculated, the result is cached.

Therefore later requests for the same argument can reuse the cached result.

This changes the practical performance dramatically.
"""


# =============================================================================
# 61. Recursive Factorial With a Wrapper
# =============================================================================

def calculate_factorial(
    number: int,
) -> int:
    """
    Public factorial function.
    """
    if number < 0:
        raise ValueError(
            "The number must be non-negative.",
        )

    def calculate(
        current: int,
    ) -> int:
        """
        Perform the recursive calculation.
        """
        if current == 0:
            return 1

        return current * calculate(
            current - 1,
        )

    return calculate(
        number,
    )


wrapped_factorial: int = calculate_factorial(
    6,
)

print(
    wrapped_factorial,
)


# =============================================================================
# 62. Recursive Function Inside Another Function
# =============================================================================
"""
A recursive function does not have to be defined at module scope.

A nested function can also call itself.

Example:

    def outer() -> int:
        def recursive(
            value: int,
        ) -> int:
            if value == 0:
                return 0

            return value + recursive(value - 1)

        return recursive(5)

The recursive function has access to its enclosing scope in addition to
its own local scope.
"""


# =============================================================================
# 63. Nested Recursive Function
# =============================================================================

def nested_recursive_sum(
    number: int,
) -> int:
    """
    Calculate a sum using a nested recursive function.
    """
    if number < 0:
        raise ValueError(
            "The number must be non-negative.",
        )

    def calculate(
        current: int,
    ) -> int:
        """
        Recursively calculate the sum.
        """
        if current == 0:
            return 0

        return current + calculate(
            current - 1,
        )

    return calculate(
        number,
    )


nested_recursive_result: int = nested_recursive_sum(
    5,
)

print(
    nested_recursive_result,
)


# =============================================================================
# 64. Recursive Directory-Style Data
# =============================================================================
"""
Recursive functions are useful for structures that contain themselves.

For example, imagine:

    folder
        file
        folder
            file
            folder
                file

Each folder can contain more folders.

The same processing rule can therefore be applied recursively.
"""


# =============================================================================
# 65. Recursive Nested Dictionary
# =============================================================================

from typing import Any


NestedData: TypeAlias = dict[str, "NestedData | int"]


def sum_nested_dictionary(
    data: NestedData,
) -> int:
    """
    Sum integer values in a recursively nested dictionary.
    """
    total: int = 0

    for value in data.values():
        if isinstance(value, int):
            total += value
        else:
            total += sum_nested_dictionary(
                value,
            )

    return total


nested_dictionary: NestedData = {
    "first": 10,
    "second": {
        "third": 20,
        "fourth": {
            "fifth": 30,
        },
    },
}

nested_dictionary_sum: int = sum_nested_dictionary(
    nested_dictionary,
)

print(
    nested_dictionary_sum,
)


# =============================================================================
# 66. Recursive Backtracking Concept
# =============================================================================
"""
Backtracking is another important use of recursion.

The general idea is:

    1. Choose an option.
    2. Recursively explore the choice.
    3. Undo the choice.
    4. Try another option.

This is useful for:

    - permutations
    - combinations
    - maze solving
    - Sudoku
    - N-Queens
    - constraint problems

The recursion represents the decision tree.
"""


# =============================================================================
# 67. Recursive Permutations
# =============================================================================

def permutations(
    values: list[int],
) -> list[list[int]]:
    """
    Generate permutations recursively.
    """
    if len(values) <= 1:
        return [values.copy()]

    result: list[list[int]] = []

    for index in range(
        len(values),
    ):
        current: int = values[index]

        remaining: list[int] = (
            values[:index]
            + values[index + 1:]
        )

        for permutation in permutations(
            remaining,
        ):
            result.append(
                [current] + permutation,
            )

    return result


permutation_result: list[list[int]] = permutations(
    [1, 2, 3],
)

print(
    permutation_result,
)


# =============================================================================
# 68. Recursive Combination Generation
# =============================================================================

def combinations(
    values: list[int],
    size: int,
) -> list[list[int]]:
    """
    Generate combinations recursively.
    """
    if size == 0:
        return [[]]

    if size > len(values):
        return []

    if not values:
        return []

    first: int = values[0]

    with_first: list[list[int]] = [
        [first] + combination
        for combination in combinations(
            values[1:],
            size - 1,
        )
    ]

    without_first: list[list[int]] = combinations(
        values[1:],
        size,
    )

    return with_first + without_first


combination_result: list[list[int]] = combinations(
    [1, 2, 3, 4],
    2,
)

print(
    combination_result,
)


# =============================================================================
# 69. Recursive Mathematical Definition
# =============================================================================
"""
Many mathematical functions have recursive definitions.

For example, factorial:

    0! = 1
    n! = n * (n - 1)!

This maps almost directly to Python:

    def factorial(number: int) -> int:
        if number == 0:
            return 1

        return number * factorial(number - 1)

This is one reason recursion is often used when teaching algorithms.
"""


# =============================================================================
# 70. Recursive Exponentiation More Efficiently
# =============================================================================
"""
A naive recursive power implementation performs one multiplication per
exponent.

A divide-and-conquer implementation can reduce the number of recursive
levels.

For even exponents:

    x^n = (x^(n / 2))^2

For odd exponents:

    x^n = x * x^(n - 1)
"""


def fast_power(
    base: int,
    exponent: int,
) -> int:
    """
    Calculate a power using recursive exponentiation by squaring.
    """
    if exponent < 0:
        raise ValueError(
            "The exponent must be non-negative.",
        )

    if exponent == 0:
        return 1

    half: int = fast_power(
        base,
        exponent // 2,
    )

    result: int = half * half

    if exponent % 2 == 1:
        result *= base

    return result


fast_power_result: int = fast_power(
    2,
    10,
)

print(
    fast_power_result,
)


# =============================================================================
# 71. Recursive Function Complexity
# =============================================================================
"""
Recursive algorithms can have very different time complexities.

Examples:

    Factorial recursion:
        O(n)

    Recursive sum:
        O(n)

    Binary search:
        O(log n)

    Naive Fibonacci:
        approximately O(2^n)

    Memoized Fibonacci:
        O(n)

The recursive structure itself does not determine performance.

The number of recursive calls and the work performed at each call determine
the complexity.
"""


# =============================================================================
# 72. Avoiding Repeated Work
# =============================================================================
"""
A recursive function should avoid unnecessary repeated work when possible.

Naive Fibonacci:

    fibonacci(n - 1)
    fibonacci(n - 2)

can cause the same values to be calculated many times.

Possible solutions include:

    - memoization
    - dynamic programming
    - iterative algorithms
    - caching
"""


# =============================================================================
# 73. Recursion With Type Annotations
# =============================================================================

def recursive_double(
    number: int,
) -> int:
    """
    Double a number recursively by reducing the problem.
    """
    if number == 0:
        return 0

    if number > 0:
        return 2 + recursive_double(
            number - 1,
        )

    return -2 + recursive_double(
        number + 1,
    )


recursive_double_result: int = recursive_double(
    5,
)

print(
    recursive_double_result,
)


# =============================================================================
# 74. Recursive Function Return Type
# =============================================================================
"""
A recursive function should have a clear return type.

Example:

    def factorial(
        number: int,
    ) -> int:
        ...

The recursive call returns int, so every path through the function should
also return int.

For functions that only perform an action:

    def countdown(
        number: int,
    ) -> None:
        ...

The base case should use:

    return

rather than returning an unrelated value.
"""


# =============================================================================
# 75. Recursive Function With None Return Type
# =============================================================================

def print_numbers(
    number: int,
) -> None:
    """
    Print numbers recursively.
    """
    if number <= 0:
        return

    print(
        number,
    )

    print_numbers(
        number - 1,
    )


print_numbers(
    3,
)


# =============================================================================
# 76. Recursive Function With Boolean Return Type
# =============================================================================

def recursive_even_check(
    number: int,
) -> bool:
    """
    Determine whether a non-negative integer is even recursively.
    """
    if number < 0:
        return recursive_even_check(
            -number,
        )

    if number == 0:
        return True

    if number == 1:
        return False

    return recursive_even_check(
        number - 2,
    )


even_result: bool = recursive_even_check(
    10,
)

print(
    even_result,
)


# =============================================================================
# 77. Recursive Function With String Return Type
# =============================================================================

def repeat_text(
    text: str,
    count: int,
) -> str:
    """
    Repeat text recursively.
    """
    if count <= 0:
        return ""

    return text + repeat_text(
        text,
        count - 1,
    )


repeated_text: str = repeat_text(
    "Hi ",
    3,
)

print(
    repeated_text,
)


# =============================================================================
# 78. Recursive Function With List Return Type
# =============================================================================

def create_numbers(
    number: int,
) -> list[int]:
    """
    Create numbers from 1 through number recursively.
    """
    if number <= 0:
        return []

    result: list[int] = create_numbers(
        number - 1,
    )

    result.append(
        number,
    )

    return result


created_numbers: list[int] = create_numbers(
    5,
)

print(
    created_numbers,
)


# =============================================================================
# 79. Recursive Filtering
# =============================================================================

def recursive_filter_even(
    values: list[int],
) -> list[int]:
    """
    Return even values using recursion.
    """
    if not values:
        return []

    result: list[int] = recursive_filter_even(
        values[1:],
    )

    if values[0] % 2 == 0:
        result.insert(
            0,
            values[0],
        )

    return result


filtered_values: list[int] = recursive_filter_even(
    [1, 2, 3, 4, 5, 6],
)

print(
    filtered_values,
)


# =============================================================================
# 80. Recursive Mapping
# =============================================================================

def recursive_square_values(
    values: list[int],
) -> list[int]:
    """
    Square every value recursively.
    """
    if not values:
        return []

    return [
        values[0] ** 2,
        *recursive_square_values(
            values[1:],
        ),
    ]


recursive_squared_values: list[int] = recursive_square_values(
    [1, 2, 3, 4],
)

print(
    recursive_squared_values,
)


# =============================================================================
# 81. Recursive String Search
# =============================================================================

def recursive_find_character(
    text: str,
    target: str,
    index: int = 0,
) -> int:
    """
    Find a character recursively.

    Returns:
        The first matching index, or -1.
    """
    if index >= len(text):
        return -1

    if text[index] == target:
        return index

    return recursive_find_character(
        text,
        target,
        index + 1,
    )


character_index: int = recursive_find_character(
    "Python",
    "t",
)

print(
    character_index,
)


# =============================================================================
# 82. Recursive String Count
# =============================================================================

def recursive_character_count(
    text: str,
    target: str,
) -> int:
    """
    Count a character recursively.
    """
    if not text:
        return 0

    current_count: int = (
        1
        if text[0] == target
        else 0
    )

    return (
        current_count
        + recursive_character_count(
            text[1:],
            target,
        )
    )


character_count: int = recursive_character_count(
    "banana",
    "a",
)

print(
    character_count,
)


# =============================================================================
# 83. Recursive Decimal Digit Sum
# =============================================================================

def digit_sum(
    number: int,
) -> int:
    """
    Calculate the sum of decimal digits recursively.
    """
    number = abs(number)

    if number < 10:
        return number

    return (
        number % 10
        + digit_sum(
            number // 10,
        )
    )


digit_sum_result: int = digit_sum(
    12345,
)

print(
    digit_sum_result,
)


# =============================================================================
# 84. Recursive Digit Count
# =============================================================================

def digit_count(
    number: int,
) -> int:
    """
    Count decimal digits recursively.
    """
    number = abs(number)

    if number < 10:
        return 1

    return 1 + digit_count(
        number // 10,
    )


number_of_digits: int = digit_count(
    12345,
)

print(
    number_of_digits,
)


# =============================================================================
# 85. Recursive Decimal Reversal
# =============================================================================

def reverse_digits(
    number: int,
    reversed_number: int = 0,
) -> int:
    """
    Reverse decimal digits recursively.
    """
    sign: int = -1 if number < 0 else 1
    remaining: int = abs(number)

    if remaining == 0:
        return sign * reversed_number

    return reverse_digits(
        remaining // 10,
        reversed_number * 10 + remaining % 10,
    )


reversed_number_result: int = reverse_digits(
    12345,
)

print(
    reversed_number_result,
)


# =============================================================================
# 86. Recursive GCD Explanation
# =============================================================================
"""
For:

    gcd(48, 18)

we calculate:

    gcd(48, 18)
        -> gcd(18, 12)
        -> gcd(12, 6)
        -> gcd(6, 0)

The base case is:

    gcd(6, 0) = 6

Therefore:

    gcd(48, 18) = 6
"""


# =============================================================================
# 87. Recursive LCM
# =============================================================================

def least_common_multiple(
    first: int,
    second: int,
) -> int:
    """
    Calculate the least common multiple using recursive GCD.
    """
    if first == 0 or second == 0:
        return 0

    gcd: int = greatest_common_divisor(
        first,
        second,
    )

    return abs(
        first * second
    ) // gcd


lcm_result: int = least_common_multiple(
    12,
    18,
)

print(
    lcm_result,
)


# =============================================================================
# 88. Recursive Factorial With Validation
# =============================================================================

def validated_factorial(
    number: int,
) -> int:
    """
    Calculate factorial with explicit validation.
    """
    if number < 0:
        raise ValueError(
            "number must be greater than or equal to zero.",
        )

    if number == 0:
        return 1

    return number * validated_factorial(
        number - 1,
    )


validated_factorial_result: int = validated_factorial(
    7,
)

print(
    validated_factorial_result,
)


# =============================================================================
# 89. Recursion With Multiple Parameters
# =============================================================================

def recursive_range_sum(
    current: int,
    end: int,
    total: int = 0,
) -> int:
    """
    Sum integers from current through end recursively.
    """
    if current > end:
        return total

    return recursive_range_sum(
        current + 1,
        end,
        total + current,
    )


range_sum_result: int = recursive_range_sum(
    1,
    10,
)

print(
    range_sum_result,
)


# =============================================================================
# 90. Recursive Range Generation
# =============================================================================

def recursive_range(
    start: int,
    end: int,
) -> list[int]:
    """
    Create an inclusive integer range recursively.
    """
    if start > end:
        return []

    return [
        start,
        *recursive_range(
            start + 1,
            end,
        ),
    ]


recursive_range_result: list[int] = recursive_range(
    1,
    5,
)

print(
    recursive_range_result,
)


# =============================================================================
# 91. Recursion and Immutability
# =============================================================================
"""
Recursive functions often work naturally with immutable values.

For example:

    text[1:]

creates a new string.

Integers are also immutable.

This can make recursive transformations easy to reason about.

However, creating many intermediate objects can have a performance cost.

For large lists or strings, index-based recursion can sometimes avoid
unnecessary slicing.
"""


# =============================================================================
# 92. Index-Based Recursive String Reversal
# =============================================================================

def reverse_string_by_index(
    text: str,
    index: int | None = None,
) -> str:
    """
    Reverse a string recursively using indexes.
    """
    if index is None:
        index = len(text) - 1

    if index < 0:
        return ""

    return (
        text[index]
        + reverse_string_by_index(
            text,
            index - 1,
        )
    )


indexed_reversed_text: str = reverse_string_by_index(
    "Python",
)

print(
    indexed_reversed_text,
)


# =============================================================================
# 93. Recursive Tree Value Sum
# =============================================================================

def tree_sum(
    node: TreeNode | None,
) -> int:
    """
    Calculate the sum of all binary tree values recursively.
    """
    if node is None:
        return 0

    return (
        node.value
        + tree_sum(node.left)
        + tree_sum(node.right)
    )


tree_sum_result: int = tree_sum(
    tree,
)

print(
    tree_sum_result,
)


# =============================================================================
# 94. Recursive Tree Maximum
# =============================================================================

def tree_max(
    node: TreeNode | None,
) -> int:
    """
    Find the maximum value in a binary tree recursively.
    """
    if node is None:
        raise ValueError(
            "Cannot find a maximum in an empty tree.",
        )

    values: list[int] = [
        node.value,
    ]

    if node.left is not None:
        values.append(
            tree_max(
                node.left,
            ),
        )

    if node.right is not None:
        values.append(
            tree_max(
                node.right,
            ),
        )

    return max(
        values,
    )


tree_max_result: int = tree_max(
    tree,
)

print(
    tree_max_result,
)


# =============================================================================
# 95. Recursive Tree Minimum
# =============================================================================

def tree_min(
    node: TreeNode | None,
) -> int:
    """
    Find the minimum value in a binary tree recursively.
    """
    if node is None:
        raise ValueError(
            "Cannot find a minimum in an empty tree.",
        )

    values: list[int] = [
        node.value,
    ]

    if node.left is not None:
        values.append(
            tree_min(
                node.left,
            ),
        )

    if node.right is not None:
        values.append(
            tree_min(
                node.right,
            ),
        )

    return min(
        values,
    )


tree_min_result: int = tree_min(
    tree,
)

print(
    tree_min_result,
)


# =============================================================================
# 96. Recursive Algorithm Design
# =============================================================================
"""
When designing a recursive function, ask these questions:

    1. What is the smallest valid input?

    2. What should the function return for that input?

    3. What is the recursive subproblem?

    4. How does the input become smaller?

    5. Does every recursive call move toward the base case?

    6. What happens when the input is empty?

    7. Can the recursive calls repeat the same work?

    8. Would iteration be simpler?

    9. Could recursion depth become too large?

    10. Can memoization improve performance?
"""


# =============================================================================
# 97. Common Mistake: No Base Case
# =============================================================================
"""
Incorrect:

    def bad_recursion(number: int) -> int:
        return number + bad_recursion(number - 1)

There is no stopping condition.

Eventually Python raises:

    RecursionError

Correct:

    def good_recursion(number: int) -> int:
        if number == 0:
            return 0

        return number + good_recursion(number - 1)
"""


# =============================================================================
# 98. Common Mistake: Wrong Direction
# =============================================================================
"""
Incorrect:

    def bad_countdown(number: int) -> None:
        if number <= 0:
            return

        bad_countdown(number + 1)

The function moves:

    5
    6
    7
    8
    ...

It moves away from the base case.

Correct:

    def good_countdown(number: int) -> None:
        if number <= 0:
            return

        good_countdown(number - 1)

The function moves:

    5
    4
    3
    2
    1
    0
"""


# =============================================================================
# 99. Common Mistake: Forgetting Return
# =============================================================================

def correct_recursive_sum(
    number: int,
) -> int:
    """
    Correctly propagate a recursive return value.
    """
    if number <= 0:
        return 0

    return number + correct_recursive_sum(
        number - 1,
    )


correct_sum_result: int = correct_recursive_sum(
    5,
)

print(
    correct_sum_result,
)


# =============================================================================
# 100. Common Mistake: Calling Recursion Without Using Its Result
# =============================================================================
"""
When a recursive calculation produces a value, the recursive result usually
needs to be returned or incorporated into the current result.

For example:

    return number + recursive_sum(number - 1)

is different from:

    recursive_sum(number - 1)

The second form ignores the value returned by the recursive call.
"""


# =============================================================================
# 101. Common Mistake: Too Many Recursive Calls
# =============================================================================
"""
A recursive algorithm can accidentally create an enormous number of calls.

Naive Fibonacci is the classic example:

    fibonacci(n - 1)
    fibonacci(n - 2)

For larger n, the same values are calculated repeatedly.

Use:

    memoization

or:

    an iterative solution

when appropriate.
"""


# =============================================================================
# 102. Recursive Function Testing
# =============================================================================

def testable_factorial(
    number: int,
) -> int:
    """
    Factorial implementation suitable for simple tests.
    """
    if number < 0:
        raise ValueError(
            "number must be non-negative.",
        )

    if number == 0:
        return 1

    return number * testable_factorial(
        number - 1,
    )


assert testable_factorial(0) == 1
assert testable_factorial(1) == 1
assert testable_factorial(5) == 120


# =============================================================================
# 103. Testing Recursive Base Cases
# =============================================================================
"""
The base case should be tested explicitly.

For factorial:

    factorial(0) == 1

For Fibonacci:

    fibonacci(0) == 0
    fibonacci(1) == 1

For recursive list sum:

    recursive_list_sum([]) == 0

Testing the base case helps verify that recursion has a correct termination
condition.
"""


assert recursive_list_sum([]) == 0
assert recursive_list_product([]) == 1
assert recursive_contains([], 10) is False


# =============================================================================
# 104. Testing Recursive Search
# =============================================================================

test_values: list[int] = [
    10,
    20,
    30,
    40,
]

assert recursive_contains(
    test_values,
    30,
) is True

assert recursive_contains(
    test_values,
    99,
) is False

assert recursive_linear_search(
    test_values,
    30,
) == 2

assert recursive_linear_search(
    test_values,
    99,
) == -1


# =============================================================================
# 105. Testing Recursive Tree Functions
# =============================================================================

assert tree_contains(
    tree,
    10,
) is True

assert tree_contains(
    tree,
    999,
) is False

assert count_tree_nodes(
    tree,
) == 7

assert tree_sum(
    tree,
) == 71

assert tree_height(
    tree,
) == 3


# =============================================================================
# 106. Recursion and Side Effects
# =============================================================================
"""
Recursive functions can either:

    - return values
    - perform side effects
    - or do both

Returning values often makes recursive algorithms easier to test.

Example:

    def recursive_sum(
        values: list[int],
    ) -> int:
        ...

The function returns a result rather than modifying global state.
"""


# =============================================================================
# 107. Prefer Local State Over Global State
# =============================================================================

def recursive_total(
    values: list[int],
) -> int:
    """
    Calculate a total using local recursive state.
    """
    if not values:
        return 0

    return values[0] + recursive_total(
        values[1:],
    )


local_state_total: int = recursive_total(
    [1, 2, 3, 4, 5],
)

print(
    local_state_total,
)


# =============================================================================
# 108. Recursive Functions and First-Class Functions
# =============================================================================
"""
Recursive functions are normal Python functions.

They can be:

    - assigned to variables
    - passed as arguments
    - returned from other functions
    - stored in collections
    - used with higher-order functions

Recursion does not create a special function type.

A recursive function is simply a function that refers to itself.
"""


# =============================================================================
# 109. Recursive Function Assigned to Another Name
# =============================================================================

def recursive_factorial_alias(
    number: int,
) -> int:
    """
    Calculate factorial recursively.
    """
    if number == 0:
        return 1

    return number * recursive_factorial_alias(
        number - 1,
    )


factorial_function_reference = recursive_factorial_alias

alias_factorial_result: int = factorial_function_reference(
    5,
)

print(
    alias_factorial_result,
)


# =============================================================================
# 110. Recursive Functions and Higher-Order Functions
# =============================================================================

from collections.abc import Callable


def apply_recursive_function(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Apply a supplied function to a value.
    """
    return function(
        value,
    )


higher_order_recursive_result: int = apply_recursive_function(
    recursive_factorial_alias,
    5,
)

print(
    higher_order_recursive_result,
)


# =============================================================================
# 111. Recursion and Closures
# =============================================================================

def create_recursive_counter(
    starting_value: int,
) -> Callable[[], int]:
    """
    Create a recursive counter function.
    """
    def count(
        current: int,
    ) -> int:
        """
        Recursively count down to zero.
        """
        if current <= 0:
            return 0

        return 1 + count(
            current - 1,
        )

    return lambda: count(
        starting_value,
    )


recursive_counter: Callable[[], int] = create_recursive_counter(
    5,
)

recursive_counter_result: int = recursive_counter()

print(
    recursive_counter_result,
)


# =============================================================================
# 112. Recursive Divide-and-Conquer
# =============================================================================
"""
Divide-and-conquer algorithms typically follow this pattern:

    1. Divide the problem.
    2. Recursively solve each smaller problem.
    3. Combine the results.

Examples include:

    - merge sort
    - quicksort
    - binary search
    - exponentiation by squaring
"""


# =============================================================================
# 113. Recursive Merge Sort
# =============================================================================

def merge(
    left: list[int],
    right: list[int],
) -> list[int]:
    """
    Merge two sorted lists.
    """
    result: list[int] = []

    left_index: int = 0
    right_index: int = 0

    while (
        left_index < len(left)
        and right_index < len(right)
    ):
        if left[left_index] <= right[right_index]:
            result.append(
                left[left_index],
            )
            left_index += 1
        else:
            result.append(
                right[right_index],
            )
            right_index += 1

    result.extend(
        left[left_index:],
    )

    result.extend(
        right[right_index:],
    )

    return result


def recursive_merge_sort(
    values: list[int],
) -> list[int]:
    """
    Sort a list recursively using merge sort.
    """
    if len(values) <= 1:
        return values.copy()

    middle: int = len(values) // 2

    left: list[int] = recursive_merge_sort(
        values[:middle],
    )

    right: list[int] = recursive_merge_sort(
        values[middle:],
    )

    return merge(
        left,
        right,
    )


merge_sort_result: list[int] = recursive_merge_sort(
    [38, 27, 43, 3, 9, 82, 10],
)

print(
    merge_sort_result,
)


# =============================================================================
# 114. Recursive Quicksort
# =============================================================================

def recursive_quicksort(
    values: list[int],
) -> list[int]:
    """
    Sort a list recursively using a simple quicksort implementation.
    """
    if len(values) <= 1:
        return values.copy()

    pivot: int = values[0]

    smaller: list[int] = [
        value
        for value in values[1:]
        if value <= pivot
    ]

    larger: list[int] = [
        value
        for value in values[1:]
        if value > pivot
    ]

    return (
        recursive_quicksort(smaller)
        + [pivot]
        + recursive_quicksort(larger)
    )


quicksort_result: list[int] = recursive_quicksort(
    [5, 2, 8, 1, 9, 3],
)

print(
    quicksort_result,
)


# =============================================================================
# 115. Recursive Problem-Solving Template
# =============================================================================

"""
A general recursive template is:

    def solve(
        problem: ProblemType,
    ) -> ResultType:
        if base_case(problem):
            return base_result(problem)

        smaller_problem: ProblemType = reduce(problem)

        smaller_result: ResultType = solve(
            smaller_problem,
        )

        return combine(
            problem,
            smaller_result,
        )

The exact implementation depends on the problem.

The important structure is:

    BASE CASE
        ↓
    STOP

    RECURSIVE CASE
        ↓
    REDUCE PROBLEM
        ↓
    CALL FUNCTION AGAIN
        ↓
    COMBINE RESULT
"""


# =============================================================================
# 116. Recursion Checklist
# =============================================================================

"""
Before writing a recursive function, verify:

    [ ] Is there a base case?

    [ ] Does the base case return the correct result?

    [ ] Is the recursive case clearly defined?

    [ ] Does every recursive call move toward the base case?

    [ ] Is the recursive result returned or used correctly?

    [ ] Can the recursion become too deep?

    [ ] Are repeated calculations occurring?

    [ ] Would memoization help?

    [ ] Would iteration be simpler?

    [ ] Are the input and output types clearly annotated?
"""


# =============================================================================
# 117. Practical Recursion Rules
# =============================================================================

"""
Rule 1:
    Always define a termination condition.

Rule 2:
    Make measurable progress toward the termination condition.

Rule 3:
    Keep the recursive case simple.

Rule 4:
    Return recursive results when the function calculates a value.

Rule 5:
    Consider recursion depth.

Rule 6:
    Watch for repeated calculations.

Rule 7:
    Use memoization when overlapping subproblems occur.

Rule 8:
    Prefer iteration when recursion provides no meaningful structural
    advantage.

Rule 9:
    Use recursion naturally for recursive data structures.

Rule 10:
    Keep type annotations consistent across all recursive paths.
"""


# =============================================================================
# 118. Complete Simple Recursive Example
# =============================================================================

def calculate_factorial_simple(
    number: int,
) -> int:
    """
    Calculate factorial recursively.
    """
    if number < 0:
        raise ValueError(
            "number must be non-negative.",
        )

    if number == 0:
        return 1

    return number * calculate_factorial_simple(
        number - 1,
    )


simple_factorial_result: int = calculate_factorial_simple(
    5,
)

print(
    f"5! = {simple_factorial_result}",
)


# =============================================================================
# 119. Complete Recursive Search Example
# =============================================================================

def search_value(
    values: list[int],
    target: int,
    index: int = 0,
) -> int:
    """
    Search recursively and return the first matching index.
    """
    if index >= len(values):
        return -1

    if values[index] == target:
        return index

    return search_value(
        values,
        target,
        index + 1,
    )


search_values: list[int] = [
    10,
    20,
    30,
    40,
    50,
]

search_result: int = search_value(
    search_values,
    40,
)

print(
    f"Found at index: {search_result}",
)


# =============================================================================
# 120. Complete Recursive Tree Example
# =============================================================================

def print_tree_inorder(
    node: TreeNode | None,
) -> None:
    """
    Print a binary tree using recursive inorder traversal.
    """
    if node is None:
        return

    print_tree_inorder(
        node.left,
    )

    print(
        node.value,
    )

    print_tree_inorder(
        node.right,
    )


print_tree_inorder(
    tree,
)


# =============================================================================
# Key Takeaways
# =============================================================================
"""
✓ Recursion means a function calls itself.

✓ Every useful recursive function needs a termination condition.

✓ The termination condition is called the base case.

✓ The part that calls the function again is the recursive case.

✓ Every recursive call should move toward the base case.

✓ Factorial is a classic example of recursion.

✓ Fibonacci demonstrates recursion with multiple recursive calls.

✓ Recursive functions can return values.

✓ Recursive functions can also perform side effects.

✓ Every active recursive call consumes call-stack space.

✓ Excessive recursion depth can cause RecursionError.

✓ Python does not perform general tail-call optimization.

✓ Recursion is especially useful for naturally recursive structures.

✓ Trees are commonly processed recursively.

✓ Nested data structures are commonly processed recursively.

✓ Divide-and-conquer algorithms often use recursion.

✓ Binary search can be implemented recursively.

✓ Merge sort can be implemented recursively.

✓ Backtracking algorithms commonly use recursion.

✓ Memoization can prevent repeated recursive calculations.

✓ Naive Fibonacci is an important example of inefficient recursion.

✓ Memoized Fibonacci can be dramatically more efficient.

✓ Recursion does not automatically mean better performance.

✓ Iteration is often preferable for simple repetition.

✓ Recursive functions are normal Python functions.

✓ Recursive functions can be assigned to variables and passed as arguments.

✓ A recursive function can also be nested inside another function.

✓ Recursive functions can use enclosing variables through closures.

✓ Type annotations work normally with recursive functions.

✓ Recursive functions should have consistent return types.

Core model:

    RECURSIVE FUNCTION
            |
            v
       BASE CASE?
        /       \
      YES        NO
       |          |
       v          v
    RETURN    REDUCE PROBLEM
                  |
                  v
             CALL ITSELF
                  |
                  v
             GET RESULT
                  |
                  v
             RETURN RESULT

Example:

    def factorial(
        number: int,
    ) -> int:
        if number == 0:
            return 1

        return number * factorial(
            number - 1,
        )

The most important recursion questions are:

    1. What is the base case?
    2. What is the recursive case?
    3. Does the recursive call get closer to the base case?
    4. What result should be returned?
    5. Could recursion become too deep?
    6. Is repeated work occurring?
    7. Would iteration or memoization be better?

Final mental model:

    PROBLEM
       |
       v
    BASE CASE
       |
       +----> RETURN
       |
       v
    SMALLER PROBLEM
       |
       v
    RECURSIVE CALL
       |
       v
    SMALLER PROBLEM
       |
       v
    ...
       |
       v
    BASE CASE
       |
       v
    UNWIND CALL STACK
       |
       v
    FINAL RESULT
"""


# =============================================================================
# End of 19_recursive_functions.py
# =============================================================================