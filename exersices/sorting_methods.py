# List Sorting:


# Selection Sort Method ->

some_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]
sorted_list: list[int] = []
init_: int = 0

while some_list:

    for i, nums in enumerate(some_list):

        if not i == 0:

            if nums <= init_:
                init_ = nums
            
        else:
            init_ = nums

    sorted_list.append(init_)
    some_list.remove(init_)
    init_ = 0


print(sorted_list)


# Merge Sort Method ->

def merge_sort(some_list: list[int])->list[int]:

    # part 1

    if len(some_list)<=1:

        return some_list

    mid_pt: int = len(some_list)//2

    left: list[int] = merge_sort(some_list[:mid_pt])
    right: list[int] = merge_sort(some_list[mid_pt:])

    # part 2

    merged_list: list[int] = []

    left_index: int = 0
    right_index: int = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:

            merged_list.append(left[left_index])
            left_index += 1

        else:

            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list


pass_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]
print(merge_sort(pass_list))



# Bubble Sort Method ->

"""
Compare every adjacent pair. 
If they're in the wrong order, 
swap them. Repeat until no swaps happen.
"""

num_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

swap: bool = True

while swap:

    swap = False

    for index_ in range(len(num_list)-1):

        num_1 = num_list[index_]
        num_2 = num_list[index_+1]
        
        if num_1 > num_2:

            num_list[index_], \
                num_list[index_+1] = num_list[index_+1], \
                                        num_list[index_]
            swap = True


print(num_list)



# Insertion Sort Method.

"""
Take the current element (key), 
move left through the already sorted part, 
keep shifting every element that is greater than key 
one position to the right, 
and when you find the first element that is smaller than 
or equal to key 
(or you reach the beginning), insert key at j + 1.
"""

to_sort_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

for index_ in range(1, len(to_sort_list)):

    key = to_sort_list[index_]
    j = index_-1

    while j>=0 and to_sort_list[j]>key:

        to_sort_list[j+1] = to_sort_list[j]
        j -= 1

    to_sort_list[j+1] = key
    

print(to_sort_list)


# Quick Sort 

def quick_sort(to_quicksort_list: list[int])->list[int]:

    if len(to_quicksort_list) <= 1:

        return to_quicksort_list

    pivot = len(to_quicksort_list) - 1
    
    boundary: int = 0

    for j in range(len(to_quicksort_list)-1):

        if to_quicksort_list[j] < to_quicksort_list[pivot]:
            
            to_quicksort_list[boundary], \
                to_quicksort_list[j] = to_quicksort_list[j], \
                                        to_quicksort_list[boundary]
            
            boundary+=1
        
    to_quicksort_list[boundary], \
        to_quicksort_list[pivot] = to_quicksort_list[pivot], \
                                    to_quicksort_list[boundary]

    pivot = boundary

    left : list[int] = quick_sort(to_quicksort_list[:pivot])
    right: list[int] = quick_sort(to_quicksort_list[pivot+1:])

    return left + [to_quicksort_list[pivot]] + right


to_quicksort_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

print(quick_sort(to_quicksort_list))

"""
The difference is where the work happens:

Merge Sort does the hard work while merging.
Quick Sort does the hard work while partitioning.
"""

# in-place array changing quicksort style.

def quick_sort_2(to_quicksort_list: list[int], 
                 low: int=0, 
                 high: int|None=None)-> None:

    if high is None:

        high = len(to_quicksort2_list)-1

    if low >= high:
        
        return 

    pivot: int = high
    
    boundary: int = low

    for j in range(low, high):

        if to_quicksort_list[j] < to_quicksort_list[pivot]:
            
            to_quicksort_list[boundary], \
                to_quicksort_list[j] = to_quicksort_list[j], \
                                        to_quicksort_list[boundary]
            
            boundary+=1
        
    to_quicksort_list[boundary], \
        to_quicksort_list[pivot] = to_quicksort_list[pivot], \
                                    to_quicksort_list[boundary]

    pivot = boundary

    quick_sort_2(to_quicksort_list, low, pivot - 1)
    quick_sort_2(to_quicksort_list, pivot + 1, high)


to_quicksort2_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]  

# returns None, so cannot be stored to any variable or printed.
quick_sort_2(to_quicksort2_list) 

print(to_quicksort2_list)


# Heap sort technique


    
    
def heap_sort(some_list: list[int])->None:

        def heapify(some_list: list[int], 
            index_: int, 
            heap_size: int):

            largest: int = index_
            left_child_index: int = (2 * index_) + 1
            right_child_index: int = (2 * index_) + 2

            if left_child_index < heap_size:

                if some_list[left_child_index] > some_list[largest]:

                    largest = left_child_index

            if right_child_index < heap_size:

                if some_list[right_child_index] > some_list[largest]:

                    largest = right_child_index

            if largest!=index_:

                some_list[largest], \
                    some_list[index_] = some_list[index_], \
                                            some_list[largest]
                
                heapify(some_list, largest, heap_size)

   
        heap_size: int = len(some_list)
        last_parent: int = (heap_size // 2) - 1

        for index_ in range(last_parent, -1, -1):

            heapify(some_list, index_, heap_size)

        while heap_size>1:

            some_list[0], \
                some_list[heap_size-1] = some_list[heap_size-1], \
                                            some_list[0]
            
            heap_size -= 1
            
            heapify(some_list, 0, heap_size)


heap_sort_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9] 

heap_sort(heap_sort_list)
print(heap_sort_list)










