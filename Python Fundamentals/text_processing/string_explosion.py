user_string = input()
new_string = ""
explosion_leftover = 0
for index in range(len(user_string)):
    if user_string[index] == ">":
        explosion_leftover += int(user_string[index + 1])
        new_string += ">"
    elif explosion_leftover > 0:
        explosion_leftover -= 1
    else:
        new_string += user_string[index]
print(new_string)