from collections import deque

quantity_of_water = int(input())
people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    if command[0] == "refill":
        quantity_of_water += int(command[1])
    else:
        litres_for_client = int(command[0])
        if litres_for_client <= quantity_of_water:
            quantity_of_water -= litres_for_client
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait")
print(f"{quantity_of_water} liters left")