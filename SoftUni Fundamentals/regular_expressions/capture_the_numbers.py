import re

user_string = input()
while user_string:
    regex = "\d+"
    matches = re.findall(regex, user_string)
    if matches:
        print(" ".join(matches),end=" ")
    user_string = input()



