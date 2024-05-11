import re

sample_text = "The associate phone number is 111-222-3333"
match = re.search("phone", sample_text)

print(match)  # -> finds & returns only the first match
print(match.span())
print(match.start())
print(match.end())

sample_text_2 = "phone 1, phone 2, phone...."
matches = re.findall("phone", sample_text_2)
print(matches)


# ----- @TODO Console Output -----

# <re.Match object; span=(14, 19), match='phone'>
# (14, 19)
# 14
# 19
# ['phone', 'phone', 'phone']
