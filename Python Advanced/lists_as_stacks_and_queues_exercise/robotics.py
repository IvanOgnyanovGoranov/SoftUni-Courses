from collections import deque

robot_names_and_seconds = input().split(";")
clock = input().split(":")
seconds = int(clock[2])
minutes = int(clock[1])
hours = int(clock[0])

robots = deque()
products = deque()

for i in range(len(robot_names_and_seconds)):
    # Creating the deque of robots with time values
    robot_name, robot_time = robot_names_and_seconds[i].split("-")
    robots.append({"name": robot_name, "time": int(robot_time), "waiting_time": int(robot_time)})

while True:
    # Creating a deque of products.
    product = input()
    if product == "End":
        break
    products.append(product)

# robots_copy = robots

while products:
    if seconds == 59:
        seconds = 0
        if minutes == 59:
            minutes = 0
            if hours == 23:
                hours = 0
            else:
                hours += 1
        else:
            minutes += 1
    else:
        seconds += 1

    robot_found = False
    for robot in robots:
        if robot["time"] == robot["waiting_time"]:
            processed_product = products.popleft()
            print(f"{robot['name']} - {processed_product} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
            robot["waiting_time"] = 0
            robot_found = True
            break
    if not robot_found:
        products.rotate(-1)

    for robot in robots:
        if robot["time"] != robot["waiting_time"]:
            robot["waiting_time"] += 1
