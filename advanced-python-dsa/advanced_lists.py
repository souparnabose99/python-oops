
list_1 = [1, 2, 3]
list_2 = [4, 5]

# list_1.append(list_2)
print(list_1)

list_1.extend(list_2)
print(list_1)

list_1.insert(0, 0)
print(list_1)

list_1.pop()
print(list_1)
list_1.pop(0)
print(list_1)

list_1.extend([1, 1])
print(list_1)
list_1.remove(1)
print(list_1)
list_1.reverse()
print(list_1)
list_1.sort()
print(list_1)

# ----- @TODO Console Output -----

# [1, 2, 3]
# [1, 2, 3, [4, 5]]
# [1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 1, 1]
# [2, 3, 4, 1, 1]
# [1, 1, 4, 3, 2]
# [1, 1, 2, 3, 4]
