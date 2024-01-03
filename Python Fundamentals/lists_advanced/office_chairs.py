def chairs_left(chairs_and_visitors):
    room_number = 0
    total_chairs = 0
    total_visitors = 0
    for element in chairs_and_visitors:
        room_number += 1
        new_element = element.split(" ")
        chairs = new_element[0]
        number_of_visitors = int(new_element[1])
        total_visitors += number_of_visitors
        number_of_chairs = 0
        for chair in chairs:
            total_chairs += 1
            number_of_chairs += 1
        if number_of_visitors > number_of_chairs:
            print(f"{number_of_visitors - number_of_chairs} more chairs needed in room {room_number}")
    if total_chairs >= total_visitors:
        print( f"Game On, {total_chairs - total_visitors} free chairs left")

number_of_rooms = int(input())
chair_and_visitor_list = []
for room in range(number_of_rooms):
    chair_and_visitor_count = input()
    chair_and_visitor_list.append(chair_and_visitor_count)

chairs_left(chair_and_visitor_list)