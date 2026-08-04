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
[
  'append', 'clear', 'copy', 'count',
    'extend', 'index', 'insert', 'pop',
      'remove', 'reverse', 'sort']"""

demo_list.reverse()
print(demo_list) # returns -> ['str3', 'str2', 'str1']