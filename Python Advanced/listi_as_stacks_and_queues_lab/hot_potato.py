from collections import deque

kids_names = deque(input().split())

number = int(input()) - 1

while len(kids_names) != 1:
    kids_names.rotate(-number)
    print(f"Removed {kids_names.popleft()}")

print(f"Last is {kids_names.popleft()}")