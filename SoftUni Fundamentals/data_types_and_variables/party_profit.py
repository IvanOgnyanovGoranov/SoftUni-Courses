group_size = int(input())
days = int(input())
coins = 0
days_of_adventure = 0

for _ in range(days):
    days_of_adventure += 1
    if days_of_adventure % 10 == 0:
        group_size -= 2
    if days_of_adventure % 15 == 0:
        group_size += 5
    coins = (coins + 50) - (2 * group_size)
    if days_of_adventure % 3 == 0:
        coins = coins - (3 * group_size)
    if days_of_adventure % 5 == 0:
        coins = coins + (20 * group_size)
    if days_of_adventure % 3 == 0 and days_of_adventure % 5 == 0:
            coins = coins - (2 * group_size)
print(f"{group_size} companions received {coins // group_size} coins each.")
