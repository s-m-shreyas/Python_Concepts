"""
Slicing is advanced version of indexing,
here you can access group or part of any,
collection dtype.

syntax:
dtype[Starting_index : Ending_index: updation]

updation tells the direction we are extracting, i.e
left to right(positive indexing) or
right to left(negative indexing).
and also the sequence, 
eg- 1 means print every element from left to right
    2 means print alternate element (1 skipped) left->right
    3 means print 2 skipped left->right
    .
    .
    .
    n means print n-1 skipped left to right.

    similary for negative indexing.

    -1 means every element right->left
    -2 means alternate element right->left
    -3 means 2 skipped element right->left
    .
    .
    .
    -n means n-1 skipped right->left

Types ->
1 - Positive Starting Indexing. (moving left to right)
2 - Negative Indexing. (moving right to left)
"""


# Positive Indexing Examples

"""
positive indexing will look like:
s=0, o=1, m=2, e=3, ...last_element=len(dtype)-1
"""
some_string: str = 'some_string_example'

# extract first 4 letters, left to right.
some_extd: str = some_string[0:4:1] # dtype[Starting_index : Ending_index + 1: 1]
print(some_extd)

# extract from string onwards.
some_extd_2: str = some_string[5:len(some_string)+1:1]
print(some_extd_2)

# or
some_extd_2_: str = some_string[5::1]
print(some_extd_2_)

# 1 skipped
print(some_extd_2_[0::2])
# 2 skipped
print(some_extd_2_[0::3])


# Negative Indexing Examples

some_str: str = 'some_string_example'

# extract last four letters, from right to left.
"""
negative indexing will look like:
e=-1, l=-2, p=-3, m=-4, ...last_element=len(dtype)
"""
some_str_l4: str = some_str[-1: -4-1: -1] # dtype[Starting_index : Ending_index - 1: -1]
print(some_str_l4)

# 1 skipped
print(some_str_l4[-1: -4-1:-2])
# 2 skipped
print(some_str_l4[-1: -4-1:-3])







