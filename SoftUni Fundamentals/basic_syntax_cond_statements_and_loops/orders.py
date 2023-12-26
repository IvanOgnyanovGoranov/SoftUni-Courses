number_of_orders = int(input())

total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed_per_day > 2000 or capsules_needed_per_day < 1:
        continue
    order_price = (days * capsules_needed_per_day) * price_per_capsule
    total_price += order_price
    if order_price == 0:
        continue
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")
