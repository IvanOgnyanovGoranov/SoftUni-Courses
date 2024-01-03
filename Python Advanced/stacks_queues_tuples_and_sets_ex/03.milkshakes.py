from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milk_shakes_prepared = 0

while milk_shakes_prepared < 5 and chocolates and cups_of_milk:
    if chocolates[-1] < 1 and cups_of_milk[0] < 1:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif chocolates[-1] < 1:
        chocolates.pop()
        continue
    elif cups_of_milk[0] < 1:
        cups_of_milk.popleft()
        continue

    if chocolates and cups_of_milk:
        if chocolates[-1] == cups_of_milk[0]:
            cups_of_milk.popleft()
            chocolates.pop()
            milk_shakes_prepared += 1
        else:
            cups_of_milk.rotate(-1)
            chocolates[-1] -= 5

if milk_shakes_prepared == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    new = ", ".join(str(x) for x in chocolates)
    print(f"Chocolate: {new}", sep=" ")
else:
    print("Chocolate: empty")

if cups_of_milk:
    new = ", ".join(str(x) for x in cups_of_milk)
    print(f"Milk: {new}", sep=" ")
else:
    print("Milk: empty")
