import re
command = input()
total_price = 0
pattern = ">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
bought_furniture = []
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_price += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")