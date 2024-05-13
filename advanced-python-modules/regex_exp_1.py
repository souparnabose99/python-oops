import re

sample_text = "The associate phone number is 111-222-3333"
match = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", sample_text)
print(match.group())

match_2 = re.search(r"\d{3}-\d{3}-\d{4}", sample_text)
print(match_2.group())

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
new_matches = re.search(phone_pattern, sample_text)
print(new_matches.group())
print(new_matches.group(1))
print(new_matches.group(2))
print(new_matches.group(3))

# Additional Regex

# OR operator
print(re.search(r"sat|hat", "The man sat").group())
print(re.search(r"sat|hat", "The man had a hat").group())

# Wildcard search
print(re.findall(r".at", "The man sat with the hat and then spat"))
print(re.findall(r"..at", "The man sat with the hat and then spat"))
print(re.findall(r"...at", "The man sat with the hat and then spat"))

print(re.findall(r"^\d", "4 is an even number"))
print(re.findall(r"\d$", "Output is 0"))
print(type(re.findall(r"\d$", "Output is 0")[0]))

# ----- @TODO Console Output -----

# 111-222-3333
# 111-222-3333
# 111-222-3333
# 111
# 222
# 3333
# sat
# hat
# ['sat', 'hat', 'pat']
# [' sat', ' hat', 'spat']
# ['n sat', 'e hat', ' spat']
# ['4']
# ['0']
# <class 'str'>
