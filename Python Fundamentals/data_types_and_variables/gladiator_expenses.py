lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

fight_count = 0
expenses = 0
for i in range(lost_fights_count):
    fight_count += 1
    if fight_count % 2 == 0:
        expenses += helmet_price
    if fight_count % 3 == 0:
        expenses += sword_price
    if fight_count % 6 == 0:
        expenses += shield_price
    if fight_count % 12 == 0:
        expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")