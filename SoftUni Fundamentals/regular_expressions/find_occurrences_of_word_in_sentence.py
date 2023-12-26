import re

sentence = input()
word = input()
regex = fr"\b{word}\b"
matches = re.findall(regex, sentence, re.IGNORECASE)
print(len(matches))