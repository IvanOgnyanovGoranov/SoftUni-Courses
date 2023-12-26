number_of_wagons = [0] * int(input())


while True:
    user_command = input().split()
    if user_command[0] == "End":
        print(number_of_wagons)
        break
    elif user_command[0] == "add":
        number_of_people = int(user_command[1])
        number_of_wagons[-1] += number_of_people
    elif user_command[0] == "insert":
        index = int(user_command[1])
        people = int(user_command[2])
        number_of_wagons[index] += people
    elif user_command[0] == "leave":
        index = int(user_command[1])
        people = int(user_command[2])
        number_of_wagons[index] -= people
print(number_of_wagons)