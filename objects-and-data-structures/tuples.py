
# Tuples -> Similar to lists but immutable, used tyo store data that should not be changed
# Mixing of different data-types is supported, indexing and slicing is similar to lists
# Reassignment of values wont work as tuples are immutable
# Hence tuples are of fixed size and cant grow, to used only when immutability of data is required

tup_1 = (11, 22, 33)
len(tup_1)

tup_2 = ("sample", 67)
print(tup_1)
print(tup_2)
print(tup_1[0])
print(tup_1[-1])

# Tuple Methods:

print(tup_1.index(22)) # To get index of a value
print(tup_1.count(11)) # No of times a value appears


# ----- @TODO Console Output -----

# (11, 22, 33)
# ('sample', 67)
# 11
# 33
# 1
# 1

