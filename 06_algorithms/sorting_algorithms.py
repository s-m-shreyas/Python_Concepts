"""
==============================================================================
List Sorting Algorithms
==============================================================================

Overview
--------
Sorting is one of the most fundamental operations in Computer Science.

Different sorting algorithms are designed with different trade-offs between
execution time, memory usage, stability, and implementation complexity.

This module demonstrates multiple sorting algorithms using clean,
well-documented Python implementations suitable for learning, interview
preparation, and long-term reference.

Algorithms Covered
------------------
1. Selection Sort
2. Merge Sort
3. Bubble Sort
4. Insertion Sort
5. Quick Sort (Recursive)
6. Quick Sort (In-place)
7. Heap Sort

Author's Goal
-------------
The implementations in this file intentionally prioritize readability and
understanding over micro-optimizations. Every algorithm is written to explain
its underlying logic while still following clean coding practices.
"""

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


# Sort the given list of integers using selection sort technique.

input_list_selectionsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

print(selection_sort(input_list_selectionsort))

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


# Sort the given list of integers using merge sort technique.

input_list_mergesort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

print(merge_sort(input_list_mergesort))


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


# Sort the given list of integers using bubble sort technique.

bubble_sort(input_list_bubblesort)

print(input_list_bubblesort)


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


# Sort the given list of integers using insertion sort technique.

input_list_insertionsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

insertion_sort(input_list_insertionsort)

print(input_list_insertionsort)


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


# Sort the given list of integers using quick sort technique.

input_list_quicksort_implicit: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]  

# returns None, so cannot be stored to any variable or printed.

quick_sort_2(input_list_quicksort_implicit) 

print(input_list_quicksort_implicit)


"""
==============================================================================
Heap Sort
==============================================================================

Description
-----------
Heap Sort is a comparison-based sorting algorithm built upon the Binary Heap
data structure.

This implementation constructs a Max Heap, where every parent node is greater
than or equal to its children.

Heap Property
-------------
For every parent node:

    Parent >= Left Child
    Parent >= Right Child

Because of this property, the maximum element is always located at the root
(index 0).

Algorithm Overview
------------------

Phase 1 : Build Max Heap

The input list is transformed into a valid Max Heap by repeatedly restoring
the heap property from the last parent node towards the root.

Phase 2 : Sorting

Once the heap is built:

1. Swap the root (largest element) with the last element.
2. Reduce the heap size by one.
3. Restore the heap property.
4. Repeat until only one element remains.

Algorithm Flow
--------------

Original List

↓

Build Max Heap

↓

Largest Element at Root

↓

Swap Root with Last Element

↓

Reduce Heap Size

↓

Restore Heap Property

↓

Repeat

↓

Sorted List

Time Complexity
---------------
Build Heap   : O(n)

Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n log n)

Space Complexity
----------------
O(1)

Stable
------
No

In-place
--------
Yes

Advantages
----------
• Guaranteed O(n log n) worst-case complexity.
• Requires only constant extra memory.
• Suitable when worst-case performance must remain predictable.

Disadvantages
-------------
• Not stable.
• Generally slower than Quick Sort in practice due to poorer cache locality.

Interview Notes
---------------
• Heap construction takes O(n), NOT O(n log n).
• Heap Sort always performs O(n log n), even for nearly sorted data.
• The largest element is always stored at the root of a Max Heap.
• Heapify restores the heap property for exactly one subtree.
• After every extraction, the heap size decreases by one while the sorted
  portion grows from the end of the array.

Design Decision
---------------
The helper function `heapify()` is intentionally nested inside `heap_sort()`.

Reason:
`heapify()` exists solely as an implementation detail of Heap Sort and is not
designed to be called independently. Nesting keeps the public API minimal and
clearly communicates that the helper belongs exclusively to Heap Sort.
"""

def heap_sort(some_list: list[int])->None:

    """
    Heap Sort
    Uses an internal helper function `heapify()`.
    """

    def heapify(some_list: list[int], 
        index_: int, 
        heap_size: int):

        """
        Restores the Max Heap property for the subtree rooted at index_.

        Only the subtree rooted at index_ is examined.

        If either child is larger than the current parent,
        the parent is swapped with the largest child.

        The process then continues recursively until the subtree satisfies
        the Max Heap property.
        """

        # Assuming the current parent is initially the largest node.

        largest: int = index_

        # Compute the indices of both children.

        left_child_index: int = (2 * index_) + 1
        right_child_index: int = (2 * index_) + 2

        # checking to not to be, list out of range

        if left_child_index < heap_size:

            # Compare the left child against the current largest node.

            if some_list[left_child_index] > some_list[largest]:

                largest = left_child_index

        if right_child_index < heap_size:

            # Compare the right child against the current largest node.

            if some_list[right_child_index] > some_list[largest]:

                largest = right_child_index

        # A larger child exists.
        # Move it upward and recursively restore the affected subtree.

        if largest!=index_:

            some_list[largest], \
                some_list[index_] = some_list[index_], \
                                        some_list[largest]
            
            heapify(some_list, largest, heap_size)

    # Entire list initially represents the heap.

    heap_size: int = len(some_list)

    # Last node capable of having children.

    last_parent: int = (heap_size // 2) - 1

    # --------------------------------------------------------------------------
    # Phase 1 : Build the Max Heap
    # --------------------------------------------------------------------------

    for index_ in range(last_parent, -1, -1):

        heapify(some_list, index_, heap_size)

    # --------------------------------------------------------------------------
    # Phase 2 : Repeatedly extract the maximum element
    # --------------------------------------------------------------------------

    while heap_size>1:

        # Move the current maximum to its final sorted position.

        some_list[0], \
            some_list[heap_size-1] = some_list[heap_size-1], \
                                        some_list[0]

        # Exclude the newly sorted element from the heap.

        heap_size -= 1

        # Restore the Max Heap property after extraction.

        heapify(some_list, 0, heap_size)


# Sort the given list of integers using heap sort technique.

input_list_heapsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9] 

# returns None, so cannot be stored to any variable or printed.

heap_sort(input_list_heapsort)

print(input_list_heapsort)


"""
==============================================================================
Algorithm Comparison
==============================================================================

+----------------+-----------+----------+---------+----------+---------------+
| Algorithm      | Best      | Average  | Worst   | Stable   | In-place      |
+----------------+-----------+----------+---------+----------+---------------+
| Selection Sort | O(n²)     | O(n²)    | O(n²)   | Yes*     | No*           |
| Bubble Sort    | O(n)      | O(n²)    | O(n²)   | Yes      | Yes           |
| Insertion Sort | O(n)      | O(n²)    | O(n²)   | Yes      | Yes           |
| Merge Sort     | O(nlogn)  | O(nlogn) | O(nlogn)| Yes      | No            |
| Quick Sort     | O(nlogn)  | O(nlogn) | O(n²)   | No       | Yes           |
| Heap Sort      | O(nlogn)  | O(nlogn) | O(nlogn)| No       | Yes           |
+----------------+-----------+----------+---------+----------+---------------+

*This Selection Sort implementation creates a new list, therefore its
stability and in-place characteristics differ from the classical
Selection Sort algorithm.
"""




