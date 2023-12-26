days_of_stay = int(input())
type_of_accommodation = input()
evaluation = input()

nights = days_of_stay - 1
discounted_price = 0

if type_of_accommodation == "apartment":
    if days_of_stay < 10:
        discounted_price = (25 * nights) * 0.70
    elif 10 <= days_of_stay <= 15:
        discounted_price = (25 * nights) * 0.65
    else:
        discounted_price = (25 * nights) * 0.50
elif type_of_accommodation == "president apartment":
    if days_of_stay < 10:
        discounted_price = (35 * nights) * 0.90
    elif 10 <= days_of_stay <= 15:
        discounted_price = (35 * nights) * 0.85
    else:
        discounted_price = (35 * nights) * 0.80
elif type_of_accommodation == "room for one person":
    discounted_price = nights * 18.0

if evaluation == "positive":
    discounted_price = discounted_price * 1.25
elif evaluation == "negative":
    discounted_price = discounted_price * 0.90

print(f"{discounted_price:.2f}")
