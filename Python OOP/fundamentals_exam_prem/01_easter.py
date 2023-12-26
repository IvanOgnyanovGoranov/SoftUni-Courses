user_string = input()

while True:
    command = input().split(" ")
    if command[0] == "Easter":
        break

    if command[0] == "Replace":
        current_char, new_char = command[1], command[2]
        if current_char in user_string:
            user_string = user_string.replace(current_char, new_char)
        print(user_string)
    elif command[0] == "Remove":
        substring = command[1]
        user_string = user_string.replace(substring, "")
        print(user_string)

    elif command[0] == "Includes":
        string = command[1]
        if string in user_string:
            print("True")
        else:
            print("False")

    elif command[0] == "Change":
        case = command[1]
        if case == "Upper":
            user_string = user_string.upper()
        else:
            user_string = user_string.lower()
        print(user_string)

    elif command[0] == "Reverse":
        start_index, end_index = int(command[1]), int(command[2])
        if end_index in range(len(user_string)) and start_index >= 0:
            new_string = user_string[start_index:end_index + 1]
            reversed_substring = new_string[::-1]
            print(reversed_substring)
