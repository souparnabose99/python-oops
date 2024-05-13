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

# ----- @TODO Console Output -----

# 111-222-3333
# 111-222-3333
# 111-222-3333
# 111
# 222
# 3333
