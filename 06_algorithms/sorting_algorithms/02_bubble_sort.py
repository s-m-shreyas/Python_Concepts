"""
==============================================================================
Bubble Sort
==============================================================================

Description
-----------
Bubble Sort repeatedly compares adjacent elements and swaps them whenever
they are in the wrong order.

After every complete pass, the largest unsorted element naturally "bubbles"
towards the end of the list.

The algorithm terminates when an entire pass completes without performing
a single swap, indicating that the list is already sorted.

Algorithm Flow
--------------

Compare Adjacent Elements

↓

Swap if Necessary

↓

Complete One Pass

↓

Did Any Swap Occur?

↓

Yes ----------------→ Repeat

↓

No

↓

Sorted

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
• Very simple implementation.
• Detects an already sorted list efficiently.

Disadvantages
-------------
• Inefficient for large datasets.
• Performs many unnecessary comparisons.

Interview Note
--------------
Bubble Sort is one of the few algorithms whose Best Case complexity improves
to O(n) because it can terminate early if no swaps occur.
"""

input_list_bubblesort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

def bubble_sort(some_list: list[int])->None:

    # Just to begin while loop

    swap: bool = True

    # Continue making passes until the list becomes completely sorted.
    
    while swap:

        # Assuming list to be sorted (if it would have not entered the if block, while will exit)
        
        swap = False

        for index_ in range(len(some_list)-1):

            num_1 = some_list[index_]
            num_2 = some_list[index_+1]
            
            if num_1 > num_2:

                # Swap adjacent elements that are out of order.

                some_list[index_], \
                    some_list[index_+1] = some_list[index_+1], \
                                            some_list[index_]
                swap = True


if __name__ == "__main__":
    
    # Sort the given list of integers using bubble sort technique.

    bubble_sort(input_list_bubblesort)

    print(input_list_bubblesort)