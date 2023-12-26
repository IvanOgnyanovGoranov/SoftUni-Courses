import re
bought_furniture = []
money_spent = 0
pattern = r">>([A-Za-z]+)<<([0-9.]+)!([0-9]+)" #">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.search(pattern, command)
    if matches:
        bought_furniture.append(matches.group(1))
        sum = float(matches.group(2)) * int(matches.group(3))
        money_spent += sum

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print (f"Total money spend: {money_spent:.2f}")