profit_required = float(input())
money_saved = 0

while True:
    name_of_cocktail = input()

    if name_of_cocktail == "Party!":
        print(f"We need {profit_required - money_saved:.2f} leva more.")
        break

    price_of_cocktail = len(name_of_cocktail)
    number_of_cocktails = int(input())
    order_price = price_of_cocktail * number_of_cocktails

    if order_price % 2 != 0:
        order_price = order_price * 0.75

    money_saved += order_price

    if money_saved >= profit_required:
        print("Target acquired.")
        break

print(f"Club income - {money_saved:.2f} leva.")