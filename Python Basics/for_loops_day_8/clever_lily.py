lilys_age = int(input())
price_of_washing_machine = float(input())
price_per_toy = int(input())

money = 10
toys_money = 0

for age in range(1, lilys_age + 1):
    if age % 2 == 0:
        toys_money += money - 1
        money += 10
    else:
        toys_money += price_per_toy



if toys_money >= price_of_washing_machine:
    print(f"Yes! {toys_money - price_of_washing_machine:.2f}")
else:
    print(f"No! {price_of_washing_machine - toys_money:.2f}")