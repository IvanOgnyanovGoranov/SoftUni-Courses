budget = float(input())
price_of_flour_per_kg = float(input())

price_of_eggs_per_pack = price_of_flour_per_kg * 0.75
price_of_milk_per_litre = price_of_flour_per_kg * 1.25
price_of_milk_per_loaf = price_of_milk_per_litre / 4
budget_required_per_loaf = price_of_milk_per_loaf + price_of_eggs_per_pack + price_of_flour_per_kg
colored_eggs_received = 0
number_of_loaves_made = 0

while budget >= budget_required_per_loaf:
    budget -= budget_required_per_loaf
    number_of_loaves_made += 1
    colored_eggs_received += 3
    if number_of_loaves_made % 3 == 0:
        colored_eggs_received = colored_eggs_received - (number_of_loaves_made - 2)

print(f"You made {number_of_loaves_made} loaves of Easter bread! Now you have {colored_eggs_received} eggs and {budget:.2f}BGN left.")