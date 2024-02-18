from random import shuffle, randint

# Range
list_1 = range(0, 10, 2)
print(list_1)
print(list(list_1))

# Enumerate
str_1 = "abcdef"
for item, letter in enumerate(str_1):
    print(item, "->", letter)

# Zip -> Will zip and cover only till the shortest list if lists are uneven
list_2 = [1, 2, 3, 4]
list_3 = [11, 22, 33]
list_4 = [111, 222, 333]

for item_2 in zip(list_2, list_3, list_4):
    print(item_2)
print(list(zip(list_2, list_3, list_4)))

# Shuffle -> Inplace function as it operates inplace on the list
list_5 = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(list_5)
print(list_5)

print(randint(0, 100))
print(randint(0, 100))

# ----- @TODO Console Output -----

# range(0, 10, 2)
# [0, 2, 4, 6, 8]
# 0 -> a
# 1 -> b
# 2 -> c
# 3 -> d
# 4 -> e
# 5 -> f
# (1, 11, 111)
# (2, 22, 222)
# (3, 33, 333)
# [(1, 11, 111), (2, 22, 222), (3, 33, 333)]
# [5, 4, 6, 3, 2, 8, 7, 1]
# 21
# 24
