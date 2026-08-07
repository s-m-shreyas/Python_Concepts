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


if __name__ == "__main__":

    # Sort the given list of integers using heap sort technique.

    input_list_heapsort: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9] 

    # returns None, so cannot be stored to any variable or printed.

    heap_sort(input_list_heapsort)

    print(input_list_heapsort)