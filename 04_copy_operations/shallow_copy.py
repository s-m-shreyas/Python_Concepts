# Example:

from typing import cast

list_a: list[int|list[int]] = [1, 2, 3, 4, 5, [1, 2, 3]]
list_b: list[int|list[int]] = list_a.copy()

# Id of both variables will not be same.
print(id(list_a), id(list_b)) # 1550178521664 1550178566336

# changes made to list_b will not be applied to list_a as well.
list_b.append(6)
# [1, 2, 3, 4, 5, [1, 2, 3]] [1, 2, 3, 4, 5, [1, 2, 3], 6]
print(list_a, list_b)

# just to satisfy Mypy
cast(list[int], list_b[5])[0] = 0

"""
But changes made to 
nested list of list_b will affect the 
nested list of list_a
"""
# [1, 2, 3, 4, 5, [0, 2, 3]] [1, 2, 3, 4, 5, [0, 2, 3], 6]
print(list_a, list_b)

