
# args -> arguments, kwargs -> keyword arguments

# args is like a tuple

def calculate(a, b, c, d=0):
    return sum((a, b, c, d)) * 10


def calculate_2(*args):
    return sum(args) * 10


# calculate(1, 2, 3, 4, 5)
val = calculate_2(1, 2, 3, 4, 5)
print(val)


# ----- @TODO Console Output -----
# Traceback (most recent call last):
#   File "F:\Data-Structures-Algorithms\Data-Structures\Objects-And-Data-Structures\args_and_kwargs.py", line 10, in <module>
#     calculate(1, 2, 3, 4, 5)
# TypeError: calculate() takes from 3 to 4 positional arguments but 5 were given
# 150






