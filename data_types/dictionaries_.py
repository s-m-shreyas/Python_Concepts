"""
A dictionary is a mutable mapping that 
stores data as key–value pairs, 
where every key must be unique and hashable, 
while values can be of any type.
"""
sample_dict: dict[str, int] = {} # default
sample_dict_2: dict[str, int] = {'int1': 1, 'int2': 2}
print(sample_dict, sample_dict_2)

# functions applicable.
print(dir(sample_dict))

"""
['clear', 'copy',
 'fromkeys', 'get',
   'items', 'keys',
     'pop', 'popitem',
       'setdefault', 'update',
         'values']"""