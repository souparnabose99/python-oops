
from collections import Counter, defaultdict, namedtuple

list_1 = [1,1,1,1,2,2,2,3,3,3,3,3]

print(Counter(list_1))

sample_str = "this is a sample string"
print(Counter(sample_str.split()))

sample_str_2 = "sfnsdvldjdpsfpewpsm"
print(Counter(sample_str_2).most_common())
print(Counter(sample_str_2).most_common(n=3))
print(list(Counter(sample_str_2)))

dict_1 = defaultdict(lambda: 0)  # No KeyError will happen for defaultdict compared to normal dictionary
dict_1["a"] = 1
dict_1["b"] = 2

print(dict_1)
print(dict_1["c"])

tup_1 = namedtuple("tup", ["a", "b", "c"])  # Used where the tuple is very big, hence named references used
tup_2 = tup_1(a=1, b=2, c=3)
print(type(tup_2))
print(tup_2.a)
print(tup_2.b)
print(tup_2[0])


# ----- @TODO Console Output -----

# Counter({3: 5, 1: 4, 2: 3})
# Counter({'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'string': 1})
# [('s', 4), ('d', 3), ('p', 3), ('f', 2), ('n', 1), ('v', 1), ('l', 1), ('j', 1), ('e', 1), ('w', 1), ('m', 1)]
# [('s', 4), ('d', 3), ('p', 3)]
# ['s', 'f', 'n', 'd', 'v', 'l', 'j', 'p', 'e', 'w', 'm']
# defaultdict(<function <lambda> at 0x0000010A51213E20>, {'a': 1, 'b': 2})
# 0
# <class '__main__.tup'>
# 1
# 2




