items_with_prices = input().split("|")
budget = int(input())
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50

profit = 0
new_budget = 0
items_sold = []
for item in items_with_prices:
    items_with_prices = item.split("->")
    type_of_item = items_with_prices[0]
    value_of_item = float(items_with_prices[1])
    if type_of_item == "Clothes" and value_of_item <= clothes_max_price and budget >= value_of_item:
        budget -= value_of_item
        profit += value_of_item * 0.40
        new_budget += value_of_item * 1.40
        items_sold.append(f"{value_of_item * 1.40:.2f}")
    elif type_of_item == "Shoes" and value_of_item <= shoes_max_price and budget >= value_of_item:
        budget -= value_of_item
        profit += value_of_item * 0.40
        new_budget += value_of_item * 1.40
        items_sold.append(f"{value_of_item * 1.40:.2f}")
    elif type_of_item == "Accessories" and value_of_item <= accessories_max_price and budget >= value_of_item:
        budget -= value_of_item
        profit += value_of_item * 0.40
        new_budget += value_of_item * 1.40
        items_sold.append(f"{value_of_item * 1.40:.2f}")
if new_budget + budget >= 150:
    print(*items_sold)
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    print(*items_sold)
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")
