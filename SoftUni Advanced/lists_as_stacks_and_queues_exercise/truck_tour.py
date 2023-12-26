from collections import deque

number_of_petrol_pumps = int(input())
gas_stations = deque()
stops = 0
start_index = 0
for _ in range(number_of_petrol_pumps):
    litres, distance = input().split()
    gas_stations.append([int(litres), int(distance)])

while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += gas_stations[i][0]
        destination = gas_stations[i][1]
        if fuel < destination:
            gas_stations.rotate(-1)
            start_index += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_index)