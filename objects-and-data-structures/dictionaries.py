# Dictionaries -> Mappings(key-value pair) in python, similar to Hash tables in other languages

dict_1 = {"key_1": "123", "key_2": "456"}
dict_2 = {"key_1": 123, "key_2": [11, 22, 33], "key_3": ["A", "B", "C"]}

print(dict_1["key_1"])
print(dict_2["key_2"])
print(dict_2["key_3"][1])

# Note: Dictionary values are mutable and can be updated by re-assigning the key with a different value
# Note: Keys can be created by assignment
dict_2["key_4"] = "abc"
print(dict_2["key_4"].upper())
dict_2["key_4"] = dict_2["key_4"] + "EFG"
print(dict_2["key_4"])
print(dict_2)

# Dictionary Nesting:

dict_3 = {"key1":{"nestkey":{"subnestkey":"value"}}}
print(dict_3["key1"]["nestkey"]["subnestkey"])

# Dictionary Methods:

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

# ----- @TODO Console Output -----

# 123
# [11, 22, 33]
# B
# ABC
# abcEFG
# {'key_1': 123, 'key_2': [11, 22, 33], 'key_3': ['A', 'B', 'C'], 'key_4': 'abcEFG'}
# value
# dict_keys(['key_1', 'key_2'])
# dict_values(['123', '456'])
# dict_items([('key_1', '123'), ('key_2', '456')])


