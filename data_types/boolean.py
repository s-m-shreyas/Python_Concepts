"""
Booleans are immutable data type, 
that said it cannot be edited / manipulated, in any way
after creation.
"""


# Below is a demo of creating a boolean type data type.

random_bool: bool = False # Default value [whose bool(var_name) is False always]
random_bool_2: bool = True # Non-Defualt value [whose bool(var_name) is True always]

print(random_bool, random_bool_2)

# False is internally 0 and True is 1
print(int(False), int(True))