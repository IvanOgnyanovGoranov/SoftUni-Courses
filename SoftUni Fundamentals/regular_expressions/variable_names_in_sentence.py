import re

line = input()
regex = r"\b_([A-Za-z0-9]+)\b"
match = re.findall(regex, line)
group1, group2 = match.groups
print(",".join(match))
