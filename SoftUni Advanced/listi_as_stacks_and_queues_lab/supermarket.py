from collections import deque

customers = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(customers)} people remaining.")
        break
    elif command == "Paid":
        for i in range(len(customers)):
            print(customers.popleft())
    else:
        customers.append(command)

