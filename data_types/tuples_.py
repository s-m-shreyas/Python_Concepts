"""
Tuples are immutable data type, 
that said it cannot be edited / manipulated, in any way
after creation.
"""


# Below is a demo of creating a boolean type data type.

random_tuple: tuple[()] = () # Default value [whose bool(var_name) is False always]
random_tuple_2: tuple[int, int] = (1, 2) # Non-Defualt value [whose bool(var_name) is True always]

print(random_tuple, random_tuple_2)

# Special case:
tuple_with_1_item: tuple[int] = (1,) # and not (1) -> this will be treated as int.

# Applicable functions. (only 'count', 'index')
print(dir(tuple))

"""
['count', 'index']
"""