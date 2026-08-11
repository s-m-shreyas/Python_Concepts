# Type annotation or type hinting ->

"""
The process of specifying the expected data type of variables,
function parameters, return values,
or other objects in Python using special syntax.

It tells humans and type checkers (like Pylance, mypy, or Pyright) 
what type of data is expected.

syntax:
variable_name: data_type = value

Ex->

numbers: list[int] = [1, 2, 3]

numbers
│
└── list containing integers


Ex-> 

matrix: list[list[int]] = [[1,2,3], [4,5,6]]

List
│
├── List
│   ├── int
│   ├── int
│   └── int
│
└── List

Note: Python does not enforce type annotations at runtime.

Benefits ->

Better readability
Better IDE suggestions
Earlier error detection
Easier debugging
Self-documenting code
Easier collaboration
Improves maintainability
"""

# Examples ->

age: int = 29
name: str = "Shreyas"
salary: float = 50000.50
is_active: bool = True

def add(a: int, b: int):
    return a + b
