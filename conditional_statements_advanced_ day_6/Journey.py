budget = float(input())
season = input()

price = 0

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        price = budget * 0.30
    else:
        price = budget * 0.70
elif budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        price = budget * 0.40
    else:
        price = budget * 0.80
else:
    price = budget * 0.90
    print("Somewhere in Europe")

if season == "summer":
    if budget > 1000:
        print(f"Hotel - {price:.2f}")
    else:
        print(f"Camp - {price:.2f}")
else:
    print(f"Hotel - {price:.2f}")



