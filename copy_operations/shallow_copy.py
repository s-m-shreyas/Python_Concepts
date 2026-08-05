# Example:

from typing import cast

list_c: list[int|list[int]] = [1, 2, 3, 4, 5, [1, 2, 3]]
list_d: list[int|list[int]] = list_c.copy()

# Id of both variables will not be same.
print(id(list_c), id(list_d)) # 1550178521664 1550178566336

# changes made to list_d will not be applied to list_c as well.
list_d.append(6)
# [1, 2, 3, 4, 5, [1, 2, 3]] [1, 2, 3, 4, 5, [1, 2, 3], 6]
print(list_c, list_d)

# just to satisfy Mypy
cast(list[int], list_d[5])[0] = 0

"""
But changes made to 
nested list of list_d will affect the 
nested list of list_c
"""
# [1, 2, 3, 4, 5, [0, 2, 3]] [1, 2, 3, 4, 5, [0, 2, 3], 6]
print(list_c, list_d)

