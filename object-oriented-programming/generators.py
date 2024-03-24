# Generators

def create_squares(n):
    for i in range(n):
        yield i ** 2


print(create_squares(10))
print(list(create_squares(10)))


def print_val():
    for i in range(5):
        yield i


p = print_val()

print(next(p))
print(next(p))
print(next(p))

# Use of iterator
sample = "abcd"
# print(next(sample)) -> TypeError: 'str' object is not an iterator
s_iter = iter(sample)
print(next(s_iter))
print(next(s_iter))

# ----- @TODO Console Output -----
# <generator object create_squares at 0x0000022911002570>
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 0
# 1
# 2
# a
# b


