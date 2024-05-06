import time
import timeit

start_time = time.time()

for i in range(10000):
    j = i*2

end_time = time.time()
elapsed_time = end_time - start_time
print("Total time : ", elapsed_time)


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


stmt = """
func_one(1000000)
"""

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

stmt_2 = """
func_two(1000000)
"""

setup_2 = """
def func_two(n):
    return list(map(str, range(n)))
"""

print("Func One : ", timeit.timeit(stmt, setup, number=100))
print("Func Two : ", timeit.timeit(stmt, setup, number=100))

# ----- @TODO Console Output -----

# Total time :  0.004083395004272461
# Func One :  21.913228399999753
# Func Two :  21.315199900000152

