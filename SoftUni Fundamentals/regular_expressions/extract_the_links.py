import re
regex = "(w{3}\.[A-Za-z0-9-\.]+\.[a-z]+)"

line = input()
valid_urls = []
while line:
    matches = re.search(regex, line)
    if matches:
        valid_urls.append(matches.groups(1))
    line = input()

for url in valid_urls:
    print(*url)
