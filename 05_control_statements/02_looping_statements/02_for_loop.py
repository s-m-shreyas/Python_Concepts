"""
A for loop is an iterative control flow statement that
repeatedly executes a block of code by iterating over
each element of an iterable 
(such as a list, tuple, string, set, dictionary, or range) 
until all elements have been processed.

Unlike a while loop, 
a for loop automatically moves to the next element, 
so you usually don't need to manage a counter(updation) manually.
"""

# Ex ->

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

"""
Apple
Banana
Mango

Mechanism ->

fruits
│
├── Apple  → print
├── Banana → print
└── Mango  → print

Python automatically takes one element at a time
from the iterable and assigns it to fruit.


Golden Rule ->

Use 'for'  → When iterating over an iterable or a known sequence.

Use 'while' → When repetition depends on a condition and
the number of iterations is unknown.
"""










    