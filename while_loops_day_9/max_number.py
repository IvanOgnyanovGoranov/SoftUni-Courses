user_input = input()

max = -100000000000000000000

while user_input != "Stop":
    number = int(user_input)

    if number > max:
        max = number
    user_input = input()

print(max)