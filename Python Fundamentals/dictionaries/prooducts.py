products = {}

while True:
    product = input().split()
    if product[0] == "buy":
        break
    name, price, quantity = product[0], float(product[1]), int(product[2])
    if name not in products.keys():
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

for key, value in products.items():
    value = value[0] * value[1]
    print(f"{key} -> {value:.2f}")

