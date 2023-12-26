import re

regex = r"\b_([a-zA-Z0-9]+)\b"

line = input()
matches = re.findall(regex, line)

print(",".join(matches))