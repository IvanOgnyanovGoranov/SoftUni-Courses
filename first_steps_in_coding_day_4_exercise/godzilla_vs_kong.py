movie_budget = float(input())
number_of_extras = int(input())
price_of_clothing = float(input())

decor = movie_budget * 0.10

if number_of_extras > 150:
    price_of_clothing *= 0.90

clothing_total = price_of_clothing * number_of_extras
expenses = clothing_total + decor

if expenses > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - expenses:.2f} leva left.")