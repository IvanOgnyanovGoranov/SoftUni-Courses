number_of_lines = int(input())
tank_capacity = 255
total_litres = 0

for litres in range(number_of_lines):
    litres = int(input())
    total_litres += litres
    if total_litres > tank_capacity:
        print("Insufficient capacity!")
        total_litres -= litres
        continue
print(total_litres)