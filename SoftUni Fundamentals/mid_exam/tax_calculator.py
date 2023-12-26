vehicles = input().split(">>")
total_taxes = 0
for vehicle in vehicles:
    vehicle_element = vehicle.split(" ")
    type_of_vehicle = vehicle_element[0]
    years_of_tax = int(vehicle_element[1])
    km_travelled = int(vehicle_element[2])
    taxes_per_vehicle = 0
    if type_of_vehicle == "family":
        taxes_per_vehicle = (taxes_per_vehicle + 50) - (years_of_tax * 5)
        if km_travelled >= 3000:
            km_taxes = 12 * (km_travelled // 3000)
            taxes_per_vehicle += km_taxes
    elif type_of_vehicle == "heavyDuty":
        taxes_per_vehicle = (taxes_per_vehicle + 80) - (years_of_tax * 8)
        if km_travelled >= 9000:
            km_taxes = 14 * (km_travelled // 9000)
            taxes_per_vehicle += km_taxes
    elif type_of_vehicle == "sports":
        taxes_per_vehicle = (taxes_per_vehicle + 100) - (years_of_tax * 9)
        if km_travelled >= 2000:
            km_taxes = 18 * (km_travelled // 2000)
            taxes_per_vehicle += km_taxes
    else:
        print("Invalid car type.")
        continue
    total_taxes += taxes_per_vehicle
    print(f"A {type_of_vehicle} car will pay {taxes_per_vehicle:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
