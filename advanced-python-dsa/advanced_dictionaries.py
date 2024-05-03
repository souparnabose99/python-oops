dict_1 = {"a": 1, "b": 2}

print(dict_1)

print({x: x**2 for x in range(10)})
print({k: v**2 for k, v in zip(["a", "b"], range(2))})

for k in dict_1.keys():
    print(k)

for k in dict_1.values():
    print(k)

print(dict_1.items())

# ----- @TODO Console Output -----

# {'a': 1, 'b': 2}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# {'a': 0, 'b': 1}
# a
# b
# 1
# 2
# dict_items([('a', 1), ('b', 2)])

