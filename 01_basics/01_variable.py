import keyword


"""
Variable Identifier Rules:

1 - The varibale name must not be a keyword.
2 - The variable must not start with any digit or number.
3 - The varibale name must not contain any space.
4 - The varibale name must not contain any special character except '_'.
5 - A variable is alphanumeric entity, that too starting with alphabet only.
"""


"""
A varibale name cannot be same as any element in the below list ->
Run the print statement to see the list.
"""
print(keyword.kwlist)

# Valid variable names.

"""
'str' is datatype of the object, that will be store to this variable inside memory.
This method is called type hinting or type annotation.
"""

some_var: str = ''
some_var_2: str = ''
some_var_3, some_var_4 = '', ''
