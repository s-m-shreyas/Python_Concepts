
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

Notes
-----

• Selection Sort is implemented using an auxiliary sorted list for
  educational clarity rather than the classical in-place approach.

• Merge Sort uses recursive list slicing and temporary merged lists,
  requiring O(n) auxiliary space as in the standard implementation.


## Repository Structure

```text
Sorting/
├── README.md
├── __init__.py
├── 01_selection_sort.py
├── 02_bubble_sort.py
├── 03_insertion_sort.py
├── 04_merge_sort.py
├── 05_quick_sort.py
└── 06_heap_sort.py
```

---

## Learning Objectives

This module demonstrates:

- Comparison-based sorting algorithms
- Divide and Conquer
- Recursion
- Binary Heap
- Partitioning
- Time & Space Complexity Analysis
- Stable vs Unstable Sorting
- In-place vs Out-of-place Sorting

---

## Design Philosophy

The objective of this repository is not merely to implement sorting algorithms,
but to understand the underlying logic behind them.

Every implementation is intentionally written with an emphasis on:

- Readability
- Clean code
- Algorithmic thinking
- Production-style documentation
- Interview preparation
- Long-term maintainability

---

## References

- Introduction to Algorithms (CLRS)
- Python Documentation
- GeeksforGeeks