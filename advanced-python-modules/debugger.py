
import pdb

x = 2
y = [1, 2]

pdb.set_trace()  # -> To examine values before an operation as a debugging step

x += y

# ----- @TODO Console Output -----

# > f:\data-structures-algorithms\advanced-python-modules\debugger.py(9)<module>()
# -> x += y
# (Pdb) x
# 2
# (Pdb) y
# [1, 2]
# (Pdb)
# [1, 2]
# (Pdb) --KeyboardInterrupt--

