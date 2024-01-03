import re

pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
line = input()
matches = re.findall(pattern, line)

print(", ".join(matches))