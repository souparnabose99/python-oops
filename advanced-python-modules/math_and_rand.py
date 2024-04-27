import math
import random
random.seed(100)

# print(help(math)) -> To explore the module
print(math.floor(4.35))
print(round(4.35))
print(math.ceil(4.35))
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.radians(180))

# Random:
print(random.randint(20, 50))
print(random.choice(list(range(10))))

# Sampling with replacement
print(random.choices(population=list(range(20)), k=5))
# Sampling without replacement
print(random.sample(population=list(range(20)), k=5))

list_1 = list(range(10))
print(list_1)
random.shuffle(list_1)
print(list_1)

# ----- @TODO Console Output -----

# 4
# 4
# 5
# 3.141592653589793
# 2.718281828459045
# inf
# nan
# 1.0
# 2.0
# -0.5440211108893698
# 90.0
# 3.141592653589793

# 24
# 7
# [9, 15, 14, 14, 8]
# [3, 17, 19, 2, 14]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [7, 9, 8, 5, 6, 1, 2, 3, 0, 4]


