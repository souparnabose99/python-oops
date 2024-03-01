
# args -> arguments, kwargs -> keyword arguments

# args is like a tuple

def calculate(a, b, c, d=0):
    return sum((a, b, c, d)) * 10


def calculate_2(*args): # * sign is the main thing, we can use any other word other than args as well, eg->abcd
    return sum(args) * 10


def calculate_3(*abc): # * sign is the main thing, we can use any other word other than args as well, eg->abcd
    return sum(abc) * 10


# calculate(1, 2, 3, 4, 5)
val = calculate_2(1, 2, 3, 4, 5)
print(val)

val_2 = calculate_3(1, 2, 3, 4, 9)
print(val_2)


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("There are total {} {}".format(args[0], kwargs["val"]))


func(10, 201, 30, val="values", key="keywords")
# func(10, val="123", 20) -> Will throw SyntaxError that Positional argument follows Keyword argument


# ----- @TODO Console Output -----
# Traceback (most recent call last):
#   File "F:\Data-Structures-Algorithms\Data-Structures\Objects-And-Data-Structures\args_and_kwargs.py", line 10, in <module>
#     calculate(1, 2, 3, 4, 5)
# TypeError: calculate() takes from 3 to 4 positional arguments but 5 were given
# 150
# 190
# (10, 201, 30)
# {'val': 'values', 'key': 'keywords'}
# There are total 10 values


