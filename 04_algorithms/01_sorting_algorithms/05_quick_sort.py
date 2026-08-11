"""
==============================================================================
Quick Sort (Recursive)
==============================================================================

Description
-----------
Quick Sort is a Divide and Conquer sorting algorithm.

Instead of dividing the array into equal halves like Merge Sort, Quick Sort
selects a Pivot element and partitions the remaining elements around it.

After partitioning:

    Left Partition  <  Pivot  <= Right Partition

The Pivot immediately reaches its final sorted position.

The same process is then recursively applied to both partitions.

Algorithm Flow
--------------

Choose Pivot

↓

Partition

↓

Pivot reaches final position

↓

Recursively Sort Left

↓

Recursively Sort Right

↓

Sorted List

Time Complexity
---------------
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n²)

Space Complexity
----------------
O(log n) recursion stack

Stable
------
No

In-place
--------
No (This implementation creates new lists.)

Advantages
----------
• Very fast average performance.
• Cache friendly.
• Excellent practical performance.

Disadvantages
-------------
Worst-case complexity becomes O(n²) if poor pivots are repeatedly chosen.

Design Note
-----------
Unlike Merge Sort,

Merge Sort performs most of its work while MERGING.

Quick Sort performs most of its work while PARTITIONING.

Once partitioning finishes, the pivot is already in its final sorted position.
"""

def quick_sort(some_list: list[int])->list[int]:

    if len(some_list) <= 1:

        return some_list

    pivot = len(some_list) - 1

    # Boundary separates elements smaller than the pivot.

    boundary: int = 0

    # Partition the list around the pivot.

    for j in range(len(some_list)-1):

        if some_list[j] < some_list[pivot]:
            
            some_list[boundary], \
                some_list[j] = some_list[j], \
                                        some_list[boundary]
            
            boundary+=1
        
    some_list[boundary], \
        some_list[pivot] = some_list[pivot], \
                                    some_list[boundary]

    pivot = boundary

    # Recursively sort both partitions.

    left : list[int] = quick_sort(some_list[:pivot])
    right: list[int] = quick_sort(some_list[pivot+1:])

    # Combine left partition, pivot and right partition.

    return left + [some_list[pivot]] + right


if __name__ == "__main__":

    # Sort the given list of integers using quick sort technique.

    input_list_quicksort_explicit: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

    print(quick_sort(input_list_quicksort_explicit))


"""
==============================================================================
Quick Sort (In-place)
==============================================================================

Description
-----------
Unlike the previous implementation, this version sorts the original list
directly without creating additional lists.

The algorithm repeatedly partitions only the required portion of the array,
identified by the current Low and High indices.

Only one copy of the list exists throughout the entire sorting process.

Time Complexity
---------------
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n²)

Space Complexity
----------------
O(log n)

Stable
------
No

In-place
--------
Yes

Design Note
-----------
The helper parameters 'low' and 'high' define the current sub-array being
partitioned.

No list slicing occurs, making this implementation significantly more memory
efficient than the previous recursive implementation.
"""

def quick_sort_2(some_list: list[int], 
                 low: int=0, 
                 high: int|None=None)-> None:

    # Initialize the upper boundary during the first function call.

    if high is None:

        high = len(some_list)-1

    if low >= high:
        
        return 

    pivot: int = high

    # Boundary separates elements smaller than the pivot.

    boundary: int = low

    # Partition the current sub-array around the pivot.

    for j in range(low, high):

        if some_list[j] < some_list[pivot]:
            
            some_list[boundary], \
                some_list[j] = some_list[j], \
                                        some_list[boundary]
            
            boundary+=1
        
    some_list[boundary], \
        some_list[pivot] = some_list[pivot], \
                                    some_list[boundary]

    pivot = boundary

    # Recursively sort both partitions.

    quick_sort_2(some_list, low, pivot - 1)
    quick_sort_2(some_list, pivot + 1, high)


if __name__ == "__main__":

    # Sort the given list of integers using quick sort technique.

    input_list_quicksort_implicit: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]  

    # returns None, so cannot be stored to any variable or printed.

    quick_sort_2(input_list_quicksort_implicit) 

    print(input_list_quicksort_implicit)


"""
Interview Tip
-------------
Merge Sort performs the major work while merging.

Quick Sort performs the major work while partitioning.
"""
