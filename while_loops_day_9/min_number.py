user_input = input()

min = 100000000000000000000

while user_input != "Stop":
    number = int(user_input)

    if number < min:
        min = number
    user_input = input()

print(min)