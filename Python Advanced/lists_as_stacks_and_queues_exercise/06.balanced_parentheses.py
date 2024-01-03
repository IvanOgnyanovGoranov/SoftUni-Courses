from collections import deque

parenthesis = deque()
line = list(input())

for element in line:
    if element == "(" or element == "{" or element == "[":
        parenthesis.append(element)
    else:
        if not parenthesis:
            parenthesis.append(element)
        if parenthesis[-1] == "(" and element == ")":
            parenthesis.pop()
        elif parenthesis[-1] == "{" and element == "}":
            parenthesis.pop()
        elif parenthesis[-1] == "[" and element == "]":
            parenthesis.pop()

if parenthesis:
    print("NO")
else:
    print("YES")


