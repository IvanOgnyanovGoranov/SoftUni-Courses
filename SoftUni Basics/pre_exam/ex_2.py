import math

days_of_absence = int(input())
food_left_in_kg = int(input())
food_needed_deer1 = float(input())
food_needed_deer2 = float(input())
food_needed_deer3 = float(input())

total_food_needed = food_needed_deer3 * days_of_absence + \
                    food_needed_deer2 * days_of_absence + food_needed_deer1 * days_of_absence

if food_left_in_kg >= total_food_needed:
    print(f"{math.floor(food_left_in_kg - total_food_needed)} kilos of food left.")

else:
    print(f"{math.ceil(total_food_needed - food_left_in_kg)} more kilos of food are needed.")