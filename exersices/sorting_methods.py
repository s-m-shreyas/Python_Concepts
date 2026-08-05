# List Sorting:


# Selection Sort Method ->

some_list: list[int] = [1, 3, 2, 5, 4]
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

    if len(some_list)<=1:
        return some_list

    mid_pt: int = len(some_list)//2

    left: list[int] = merge_sort(some_list[:mid_pt])
    right: list[int] = merge_sort(some_list[mid_pt:])

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

pass_list: list[int] = [1, 3, 2, 5, 4, 7, 6, 8]
print(merge_sort(pass_list))

# Bubble Sort Method ->

num_list: list[int] = [1, 3, 2, 5, 5, 4, 7, 4, 6, 8, 11, 10, 9]

swap: bool = True

while swap:

    swap = False

    for index_ in range(len(num_list)-1):

        num_1 = num_list[index_]
        num_2 = num_list[index_+1]
        
        if num_1 > num_2:
            print(num_1, num_2)
            num_list[index_], num_list[index_+1] = num_list[index_+1], num_list[index_]
            swap = True

print(num_list)
