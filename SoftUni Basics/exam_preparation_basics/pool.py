from math import ceil

number_of_people = int(input())
entrance_price = float(input()) * number_of_people
price_per_lounge_chair = float(input())
price_per_umbrella = float(input())

umbrella_numbers = ceil(number_of_people / 2)
chair_numbers = ceil(number_of_people * 0.75)

umbrella_total = umbrella_numbers * price_per_umbrella
lounge_chair_total = chair_numbers * price_per_lounge_chair

print(f"{entrance_price + umbrella_total + lounge_chair_total:.2f} lv.")