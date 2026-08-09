"""
==============================================================================
Insertion Sort
==============================================================================

Description
-----------
Insertion Sort builds the final sorted list one element at a time.

At every iteration, the current element (called the key) is removed from the
unsorted portion and inserted into its correct position within the already
sorted portion.

Unlike Bubble Sort, elements are shifted instead of repeatedly swapped.

Algorithm Flow
--------------

Sorted Portion | Unsorted Portion

↓

Pick Current Element (Key)

↓

Shift Larger Elements Right

↓

Insert Key

↓

Repeat

Time Complexity
---------------
Best Case    : O(n)
Average Case : O(n²)
Worst Case   : O(n²)

Space Complexity
----------------
O(1)

Stable
------
Yes

In-place
--------
Yes

Advantages
----------
• Excellent for nearly sorted data.
• Very small memory footprint.
• Simple implementation.

Disadvantages
-------------
• Inefficient for large unsorted datasets.

Interview Note
--------------
Insertion Sort is often used internally by advanced sorting algorithms
(e.g., TimSort) for sorting very small partitions because of its low overhead.
"""

def insertion_sort(some_list: list[int])->None:

    for index_ in range(1, len(some_list)):

        key = some_list[index_]
        j = index_-1

        # Shift every larger element one position to the right.

        while j>=0 and some_list[j]>key:

            some_list[j+1] = some_list[j]
            j -= 1

        # Inserting, the key into its correct sorted position.

        some_list[j+1] = key


if __name__ == "__main__":

    # Sort the given list of integers using insertion sort technique.

    input_list_insertionsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

    insertion_sort(input_list_insertionsort)

    print(input_list_insertionsort)