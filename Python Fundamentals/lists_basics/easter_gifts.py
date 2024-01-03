names_of_gifts = input().split(" ")

while True:
    user_command = input()
    if user_command == "No Money":
        break
    user_command = user_command.split(" ")
    type_of_command = user_command[0]
    type_of_gift = user_command[1]

    if type_of_command == "Required":
        index = int(user_command[2])
        if 0 <= index < len(names_of_gifts):
            names_of_gifts[index] = type_of_gift
    elif type_of_command == "OutOfStock":
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == type_of_gift:
                names_of_gifts[i] = "None"
    elif type_of_command == "JustInCase":
        names_of_gifts[-1] = type_of_gift
names_of_gifts = [type_of_gift for type_of_gift in names_of_gifts if type_of_gift != "None"]
result = " ".join(names_of_gifts)
print(result)