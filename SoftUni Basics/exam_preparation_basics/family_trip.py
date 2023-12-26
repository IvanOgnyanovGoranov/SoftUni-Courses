PRICE_PER_LITRE = 2.10
TOUR_GUIDE = 100

budget = float(input())
litres_of_fuel = int(input())
day_of_week = input()

total_price = 0

if day_of_week == "Saturday":
    total_price = (litres_of_fuel * PRICE_PER_LITRE + TOUR_GUIDE) * 0.90
elif day_of_week == "Sunday":
    total_price = (litres_of_fuel * PRICE_PER_LITRE + TOUR_GUIDE) * 0.80

if budget >= total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")