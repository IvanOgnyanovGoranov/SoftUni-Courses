number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

price_of_chicken_menus = number_of_chicken_menus * 10.35
price_of_fish_menus = number_of_fish_menus * 12.40
price_of_vegetarian_menus = number_of_vegetarian_menus * 8.15

total_price_of_menus = price_of_chicken_menus + price_of_fish_menus + price_of_vegetarian_menus
desert_price = total_price_of_menus * 0.20
delivery_price = 2.50

total_order_price = total_price_of_menus + desert_price + delivery_price

print(total_order_price)

