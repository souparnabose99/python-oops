# Sets -> Unordered collection of unique elements

set_1 = set()
set_1.add(1)
print(set_1)

set_1.add(2)
print(set_1)

set_1.add(1)
print(set_1)

list_1 = [11, 11, 22, 33, 55, 66, 55, 44, 77, 33]
print(list_1)
set_2 = set(list_1)
print(set_2)

# Booleans -> Pre-defined True/False value, similar to 0 & 1
# Has placeholder object "None"

bool_1 = True
print(bool_1)
print(3>4)

bool_2 = None # Use None as a placeholder for an object that we don't want to reassign yet
print(bool_2)


# ----- @TODO Console Output -----

# {1}
# {1, 2}
# {1, 2}
# [11, 11, 22, 33, 55, 66, 55, 44, 77, 33]
# {33, 66, 11, 44, 77, 22, 55}
# True
# False
# None

