import re

sample_text = "The associate phone number is 111-222-3333"
match = re.search("phone", sample_text)

print(match)  # -> finds & returns only the first match
print(match.span())
print(match.start())
print(match.end())


# ----- @TODO Console Output -----

# <re.Match object; span=(14, 19), match='phone'>
# (14, 19)
# 14
# 19
