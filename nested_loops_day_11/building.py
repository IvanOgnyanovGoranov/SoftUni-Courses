floors = int(input())
rooms = int(input())

room_name = ""
room_number = 0

for current_floor in range(floors, 0, -1):
    for ap_num in range(rooms):
        room_number = current_floor * 10 + ap_num
        if current_floor == floors:
            room_name = f"L{room_number}"
        elif current_floor % 2 == 0:
            room_name = f"O{room_number}"
        elif current_floor % 2 != 0:
            room_name = f"A{room_number}"

        print(room_name, end=" ")
    print()

