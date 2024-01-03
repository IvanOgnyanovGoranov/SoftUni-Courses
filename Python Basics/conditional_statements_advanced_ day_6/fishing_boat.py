group_budget = int(input())
season = str(input())
number_of_fishermen = int(input())

price = 0

if season == "Spring":
    if number_of_fishermen <= 6:
        price = 3000 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        price = 3000 * 0.85
    elif number_of_fishermen >= 12:
        price = 3000 * 0.75
    if number_of_fishermen % 2 == 0:
        price = price * 0.95
elif season == "Summer" or season == "Autumn":
    price = 4200
    if number_of_fishermen <= 6:
        price = 4200 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        price = 4200 * 0.85
    elif number_of_fishermen >= 12:
        price = 4200 * 0.75
    if number_of_fishermen % 2 == 0 and season != "Autumn":
        price = price * 0.95
elif season == "Winter":
    if number_of_fishermen <= 6:
        price = 2600 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        price = 2600 * 0.85
    elif number_of_fishermen >= 12:
        price = 2600 * 0.75
    if number_of_fishermen % 2 == 0:
        price = price * 0.95

if group_budget >= price:
    print(f"Yes! You have {group_budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - group_budget:.2f} leva.")






