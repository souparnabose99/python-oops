
s = set()
s_2 = set()
s_2.add(1)

s.add(1)
s.add(2)
s.add(3)
print(s)

s.add(3)
print(s)

print(s.intersection(s_2))
print(s.symmetric_difference(s_2))
print(s.isdisjoint(s_2))
print(s.union(s_2))
print(s.difference(s_2))

s.discard(2)
print(s)

# ----- @TODO Console Output -----

# {1, 2, 3}
# {1, 2, 3}
# {1}
# {2, 3}
# False
# {1, 2, 3}
# {2, 3}
# {1, 3}


