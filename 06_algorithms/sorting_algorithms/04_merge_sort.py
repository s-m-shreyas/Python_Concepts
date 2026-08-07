"""
==============================================================================
Merge Sort
==============================================================================

Description
-----------
Merge Sort follows the Divide and Conquer paradigm.

Instead of sorting the entire list directly, the algorithm repeatedly divides
the list into two smaller halves until every sub-list contains only one
element.

Since a single element is already sorted, neighbouring sub-lists are merged
back together while preserving sorted order.

Unlike Quick Sort, Merge Sort performs most of its work during the merge phase.

Algorithm Flow
--------------

Original List

↓

Recursively Divide

↓

Single Element Lists

↓

Merge Sorted Lists

↓

Completely Sorted List

Time Complexity
---------------
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n log n)

Space Complexity
----------------
O(n)

Stable
------
Yes

In-place
--------
No

Advantages
----------
• Predictable performance
• Stable sorting
• Excellent for Linked Lists
• Suitable for External Sorting

Disadvantages
-------------
Requires additional memory for merging.
"""

def merge_sort(some_list: list[int])->list[int]:

    # -------------------------------------------------------------------------
    # Phase 1 : Divide
    # -------------------------------------------------------------------------

    if len(some_list)<=1:

        return some_list

    mid_pt: int = len(some_list)//2

    left: list[int] = merge_sort(some_list[:mid_pt])
    right: list[int] = merge_sort(some_list[mid_pt:])

    # -------------------------------------------------------------------------
    # Phase 2 : Merge
    # -------------------------------------------------------------------------

    merged_list: list[int] = []

    left_index: int = 0
    right_index: int = 0

    # Merge both sorted halves into a single sorted list.

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:

            merged_list.append(left[left_index])
            left_index += 1

        else:

            merged_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements.

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list


if __name__ == "__main__":
    
    # Sort the given list of integers using merge sort technique.

    input_list_mergesort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

    print(merge_sort(input_list_mergesort))