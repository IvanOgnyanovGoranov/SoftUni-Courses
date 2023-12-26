number_of_inputs = int(input())
parking_lot = {}

for number in range(number_of_inputs):
    user_input = input().split()
    if user_input[0] == "unregister":
        if user_input[1] not in parking_lot.keys():
            print(f"ERROR: user {user_input[1]} not found")
            continue
        else:
            print(f"{user_input[1]} unregistered successfully")
            del parking_lot[user_input[1]]
            continue

    command, name, number = user_input
    if name not in parking_lot:
        parking_lot[name] = number
        print(f"{name} registered {number} successfully")
    else:
        print(f"ERROR: already registered with plate number {parking_lot[name]}")

for key, value in parking_lot.items():
    print(f"{key} => {value}")