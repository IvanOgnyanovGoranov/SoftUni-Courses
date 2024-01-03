from collections import deque
from math import floor

line = deque(input().split())

index = 0

while index < len(line):
    element = line[index]

    if element == "*":
        for _ in range(index - 1):
            line.appendleft(int(line.popleft()) * int(line.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            line.appendleft(int(line.popleft()) / int(line.popleft()))
    elif element == "+":
        for _ in range(index - 1):
            line.appendleft(int(line.popleft()) + int(line.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            line.appendleft(int(line.popleft()) - int(line.popleft()))

    if element in "+-/*":
        del line[1]
        index = 1
    index += 1

print(floor(int(line[0])))
