type_of_flower = str(input())
number_of_flowers = int(input())
budget = int(input())

ROSES = 5
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.5

price = 0

if type_of_flower == "Roses":
    if number_of_flowers > 80:
        price = (number_of_flowers * ROSES) * 0.90
    else:
        price = number_of_flowers * ROSES
elif type_of_flower == "Dahlias":
    if number_of_flowers > 90:
        price = (number_of_flowers * DAHLIAS) * 0.85
    else:
        price = number_of_flowers * DAHLIAS
elif type_of_flower == "Tulips":
    if number_of_flowers > 80:
        price = (number_of_flowers * TULIPS) * 0.85
    else:
        price = number_of_flowers * TULIPS
elif type_of_flower == "Narcissus":
    if number_of_flowers < 120:
        price = (number_of_flowers * NARCISSUS) * 1.15
    else:
        price = number_of_flowers * NARCISSUS
elif type_of_flower == "Gladiolus":
    if number_of_flowers < 80:
        price = (number_of_flowers * GLADIOLUS) * 1.20
    else:
        price = number_of_flowers * GLADIOLUS
else:
    pass

if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")

