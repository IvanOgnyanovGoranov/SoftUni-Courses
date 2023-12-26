from collections import deque

initial_fuel = deque([int(x) for x in input().split()])
additional_consumption_indexes = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

total_altitudes = 0
reached_altitudes = 0

while initial_fuel and additional_consumption_indexes and fuel_needed:
    current_fuel = initial_fuel[-1]
    current_index = additional_consumption_indexes[0]
    current_fuel_needed = fuel_needed[0]

    fuel_left = current_fuel - current_index

    if fuel_left >= current_fuel_needed:
        reached_altitudes += 1
        total_altitudes += 1
        initial_fuel.pop()
        additional_consumption_indexes.popleft()
        fuel_needed.popleft()
        print(f"John has reached: Altitude {str(total_altitudes)}")
        continue

    elif fuel_left < current_fuel_needed:
        total_altitudes += 1
        print(f"John did not reach: Altitude {str(total_altitudes)}")
        break

altitudes = "Reached altitudes: "
if reached_altitudes:
    number = 0
    for alt in range(reached_altitudes):
        number += 1
        if number > 1:
            altitudes += f", Altitude {str(number)}"
        else:
            altitudes += f"Altitude {str(number)}"

if initial_fuel and reached_altitudes:
    print(f"John failed to reach the top.\n{altitudes}")

elif not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

elif not initial_fuel and reached_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")