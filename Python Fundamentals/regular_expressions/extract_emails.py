import re

sentence = input()

regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+\b"
matches = re.findall(regex, sentence, re.IGNORECASE)
print("\n".join(matches))