# Map function:

def make_square(num):
    return num ** 2


num_list = [1, 2, 3, 4]

print(map(make_square, num_list))
for item in map(make_square, num_list):
    print(item)

# map will execute the function for us, no need to pass () for functions
print(list(map(make_square, num_list)))

# Filter:


def even_checker(num):
    return num % 2 == 0


num_list_2 = [1, 2, 3, 4, 5, 6]

print(filter(even_checker, num_list_2))
for item in map(even_checker, num_list_2):
    print(item)

print(list(filter(even_checker, num_list_2)))

# Lambda Expressions:

print(list(map(lambda n: n**2, num_list_2)))

# ----- @TODO Console Output -----

# <map object at 0x000001CFCF5C5930>
# 1
# 4
# 9
# 16
# [1, 4, 9, 16]
# <filter object at 0x00000259F9595ED0>
# False
# True
# False
# True
# False
# True
# [2, 4, 6]
# [1, 4, 9, 16, 25, 36]

