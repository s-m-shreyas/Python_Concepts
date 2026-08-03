"""
A list in Python is an ordered, 
mutable collection that can store multiple items, 
including mixed data types. 
You can change, add, or remove elements after creating it.
"""

# Below is an example of demo list object.
demo_list: list[str] = ['str1', 'str2', 'str3']
print(demo_list) # returns -> ['str1', 'str2', 'str3']

# functions applicable.
print(dir(demo_list))
"""
['__add__', '__class__', '__class_getitem__',
 '__contains__', '__delattr__', '__delitem__',
   '__dir__', '__doc__', '__eq__', '__format__',
     '__ge__', '__getattribute__', '__getitem__',
       '__getstate__', '__gt__', '__hash__', '__iadd__',
         '__imul__', '__init__', '__init_subclass__',
           '__iter__', '__le__', '__len__', '__lt__',
             '__mul__', '__ne__', '__new__', '__reduce__',
               '__reduce_ex__', '__repr__', '__reversed__',
                 '__rmul__', '__setattr__', '__setitem__',
                   '__sizeof__', '__str__', '__subclasshook__',
                     'append', 'clear', 'copy', 'count',
                       'extend', 'index', 'insert', 'pop',
                         'remove', 'reverse', 'sort']"""

demo_list.reverse()
print(demo_list) # returns -> ['str3', 'str2', 'str1']