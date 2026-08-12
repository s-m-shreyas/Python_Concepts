"""
==============================================================================
Selection Sort
==============================================================================

Description
-----------
Selection Sort repeatedly selects the smallest element from the remaining
unsorted portion of the list and places it into the sorted portion.

This implementation builds a separate sorted list rather than sorting
the original list in-place.

Algorithm Flow
--------------
Unsorted List

↓

Find Minimum Element

↓

Append to Sorted List

↓

Remove from Original List

↓

Repeat until Original List becomes Empty

Time Complexity
---------------
Best Case    : O(n²)
Average Case : O(n²)
Worst Case   : O(n²)

Space Complexity
----------------
O(n)

Stable
------
Yes (because equal elements are appended in order)

In-place
--------
No

Use Cases
---------
Useful for understanding the concept of repeatedly selecting the minimum
element, although rarely used in production due to poor performance.
"""

def selection_sort(some_list: list[int])->list[int]:

    sorted_list: list[int] = []

    while some_list:

        # Stores the smallest element found during each iteration.
        smallest_num: int = some_list[0]

        # Search the current minimum element.
        for index_ in range(1, len(some_list)):

            if some_list[index_] <= smallest_num:

                smallest_num = some_list[index_]
                
        # Move the smallest element into the sorted list.
        sorted_list.append(smallest_num)
        some_list.remove(smallest_num)

    return sorted_list


if __name__ == "__main__":

    # Sort the given list of integers using selection sort technique.

    input_list_selectionsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

    print(selection_sort(input_list_selectionsort))