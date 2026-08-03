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
['__add__', '__class__',
 '__class_getitem__', '__contains__',
   '__delattr__', '__dir__', '__doc__',
     '__eq__', '__format__', '__ge__',
       '__getattribute__', '__getitem__',
         '__getnewargs__', '__getstate__',
           '__gt__', '__hash__', '__init__',
             '__init_subclass__', '__iter__',
               '__le__', '__len__', '__lt__',
                 '__mul__', '__ne__', '__new__',
                   '__reduce__', '__reduce_ex__',
                     '__repr__', '__rmul__', '__setattr__',
                       '__sizeof__', '__str__',
                         '__subclasshook__', 'count', 'index']"""