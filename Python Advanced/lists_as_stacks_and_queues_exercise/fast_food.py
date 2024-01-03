from collections import deque

quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())
biggest_order = max(orders)
for index in range(len(orders)):
    current_order = orders[0]
    if quantity_of_food >= current_order:
        quantity_of_food -= current_order
        orders.popleft()

if not orders:
    print(biggest_order)
    print("Orders complete")
else:
    print(biggest_order)
    print(f"Orders left:", end=" ")
    for order in orders:
        print(f"{order}", end=" ")
