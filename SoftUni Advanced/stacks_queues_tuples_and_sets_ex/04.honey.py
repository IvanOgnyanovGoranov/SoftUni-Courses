from collections import deque

working_bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())

honey_made = 0

while working_bees and nectars:
    nectar = nectars.pop()
    bee = working_bees.popleft()
    symbol = symbols.popleft()
    if nectar == 0 and symbol == "/":
        continue
    if nectar >= bee:
        if symbol == "*":
            result = abs(bee * nectar)
        elif symbol == "+":
            result = abs(bee + nectar)
        elif symbol == "-":
            result = abs(bee - nectar)
        elif symbol == "/":
            result = abs(bee / nectar)
        honey_made += result
    else:
        working_bees.appendleft(bee)
        symbols.appendleft(symbol)

print(f"Total honey made: {honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
