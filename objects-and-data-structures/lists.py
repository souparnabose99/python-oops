
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

# List methods:

list_1.append(56) # To append 56 to list_1
list_1.pop() # To pop last element from list_1
list_1.pop(1) # To pop 2nd element from list_1
# Note: pop() will return error if there are no elements in the list
list_1.reverse() # To reverse elements in list_1

list_2 = ["l", "g", "t", "a"]
list_2.sort() # To sort elements in the list, alphabetical order for letters, ascending order for numbers

# Nesting lists: Meaning Data Structure(list) inside another Data Structure
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

final_list = [lst_1, lst_2, lst_3]
print(final_list)
print(final_list[2])
print(final_list[1][2])

# List Comprehension: for quick construction of lists
lst_comp = [ele[1] for ele in final_list]
print(lst_comp)


# ----- @TODO Console Output -----

# 23
# [1.34, 3, 'BG']
# [23, 'ABC', 1.34]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [7, 8, 9]
# 6
# [2, 5, 8]

