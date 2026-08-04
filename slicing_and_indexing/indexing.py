"""
Indexing is one of the most fundamental concepts in Python.
It allows you to access individual elements of 
an ordered collection using their position.

Python supports indexing on:

Strings
Lists
Tuples
Bytes
Bytearray

Sets and dictionaries do not support indexing because they are not sequence types.
"""

# Examples:

# internally -> 
"""
--------Strings-------

element: 0 -> index: s
element: 1 -> index: o
element: 2 -> index: m
element: 3 -> index: e
element: 4 -> index: _
element: 5 -> index: s
element: 6 -> index: t
element: 7 -> index: r
element: 8 -> index: i
element: 9 -> index: n
element: 10 -> index: g

-----------------------
"""
some_string: str = 'some_string'

# 3rd letter of some_string
some_str_3: str = some_string[2]
# will print 'm'
print(some_str_3)

# internally ->
"""
----------List----------

for item, ind in enumerate(some_list):
    print(f'element: {item} -> index: {ind}')

element: 0 -> index: some_str
element: 1 -> index: 10
element: 2 -> index: 20
element: 3 -> index: my_name
element: 4 -> index: [1, 2]  # this will have its own indexing.

------------------------
"""

some_list: list[str|int|list[int]] = ['some_str', 10, 20, 'my_name', [1, 2]]

# print last element.
print(some_list[len(some_list)-1]) # [1, 2]

"""-----------Similary for tuples as well.------------"""




