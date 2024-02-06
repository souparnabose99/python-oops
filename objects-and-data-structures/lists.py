
# What are Lists -> Concept of sequence in python | Mutable | Holds different object types

list_1 = [23, "ABC", 1.34, 3, "BG"]
len(list_1) # Gives length of list

# List indexing & slicing:
print(list_1[0])
print(list_1[2:])
print(list_1[:3])

# Reassign the list to make changes permanent
list_1 + "add" # No change in existing list
list_1 = list_1 + "add" # Item "add" is added to the list due to reassignment
list_1 * 3 # No change in existing list
list_1 = list_1 * 3 # list_1 updated due to reassignment

# ----- @TODO Console Output -----

# 23
# [1.34, 3, 'BG']
# [23, 'ABC', 1.34]

