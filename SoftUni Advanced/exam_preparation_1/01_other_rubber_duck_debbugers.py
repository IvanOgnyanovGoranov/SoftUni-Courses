from collections import deque

time_to_complete_a_task = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

ducks = {"Darth Vader Ducky": 0,
"Thor Ducky":	0,
"Big Blue Rubber Ducky": 0,
"Small Yellow Rubber Ducky": 0
}
while time_to_complete_a_task and number_of_tasks:
    current_time = time_to_complete_a_task.popleft()
    current_task = number_of_tasks.pop()
    current_value = current_task * current_time

    if 0 <= current_value <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= current_value <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= current_value <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= current_value <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        number_of_tasks.append(current_task - 2)
        time_to_complete_a_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for key, value in ducks.items():
    print(f"{key}: {value}")
