import re

pattern = r'\b[A-Z][a-z]{1,}[ ][A-Z][a-z]{1,}\b'
line = input()
matches = re.findall(pattern, line)

print(" ".join(matches))