number_of_cars = int(input())
parking_lot = set()
for car in range(number_of_cars):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)

if parking_lot:
    for number in parking_lot:
        print(number)
else:
    print("Parking Lot is Empty")