"""
Strings are immutable data type, 
that said it cannot be edited / manipulated, in any way
after creation.
"""


# Below is a demo of creating a string type data type.

random_string: str = "" # Default value [whose bool(var_name) is False always]
random_string_2: str = "non-default" # Non-Defualt value [whose bool(var_name) is True always]

print(bool(random_string), bool(random_string_2))