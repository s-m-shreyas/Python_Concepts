"""
A set is an unordered collection of unique, hashable objects.
"""

# Below is a demo set.
some_set: set[int] = set() # default
# some_set: set[int] = {} -> this is wrong.

some_set_2: set[int] = set({1, 2, 3, 3}) # non-default
# or
# some_set_2: set[int] = {1, 2, 3, 3}

print(some_set, some_set_2)

# functions applicable.
print(dir(some_set))

"""
['add',
    'clear', 'copy',
    'difference', 'difference_update',
        'discard', 'intersection',
        'intersection_update',
            'isdisjoint', 'issubset',
            'issuperset', 'pop',
                'remove', 'symmetric_difference',
                'symmetric_difference_update',
                    'union', 'update']"""
