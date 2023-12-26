import re

n = int(input())

pattern = r"(?:(?:\*([A-Z][a-z]{2,})\*)|(?:@([A-Z][a-z]{2,})@)): \[([a-zA-Z1])\]\|\[([a-zA-Z1])]\|\[([a-zA-Z1])]\|$"

for _ in range(n):
    text = input()

    match = re.search(pattern, text)

    if match:
        tag = match.group(1) if match.group(1) else match.group(2)
        group1 = match.group(3)
        group2 = match.group(4)
        group3 = match.group(5)

        print(f"{tag}: {ord(group1)} {ord(group2)} {ord(group3)}")
    else:
        print("Valid message not found!")

