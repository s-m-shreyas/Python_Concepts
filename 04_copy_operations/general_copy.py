# Example:

list_a: list[int] = [1, 2, 3, 4, 5]
list_b: list[int] = list_a

# Id of both variables will be same.
print(id(list_a), id(list_b)) # 2263422603840 2263422603840

# changes made to list_b will be applied to list_a as well.
list_b.append(6)
print(list_a)