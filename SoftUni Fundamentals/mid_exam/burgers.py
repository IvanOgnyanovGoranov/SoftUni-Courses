number_of_cities = int(input())
city_number = 0
total_profit = 0

for city in range(number_of_cities):
    city_number += 1
    profit_per_city = 0
    name_of_city = input()
    income_for_city = float(input())
    expenses_for_city = float(input())
    if city_number % 5 == 0:
        income_for_city *= 0.90
    elif city_number % 3 == 0:
        expenses_for_city *= 1.50
    profit_per_city = income_for_city - expenses_for_city
    total_profit += profit_per_city
    print(f"In {name_of_city} Burger Bus earned {profit_per_city:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

