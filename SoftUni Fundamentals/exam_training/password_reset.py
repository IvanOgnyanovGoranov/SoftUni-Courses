def take_odd(string):
    """Takes characters at odd indices and concatenates them."""
    new_string = ""
    index_counter = 0
    for letter in string:
        if index_counter % 2 != 0:
            new_string += letter
        index_counter += 1
    return new_string


def cut(string, index_, length_):
    index_ = int(index_)
    length_ = int(length_)
    final_index = index_ + length_
    first_part = string[:index_]
    second_part = string[final_index:]
    new_string = first_part + second_part
    return new_string


def substitute_string(string, substring_, substitute_):
    if substring_ in string:
        new_string = string.replace(substring_, substitute_)
        return new_string


user_string = input()

while True:
    command = input()
    if command == "Done":
        break
    elif command == "TakeOdd":
        user_string = take_odd(user_string)
        print(user_string)
    else:
        command = command.split()
        if command[0] == "Cut":
            action, index, length = command
            user_string = cut(user_string, index, length)
            print(user_string)

        elif command[0] == "Substitute":
            action, substring, substitute = command
            if substring in user_string:
                user_string = substitute_string(user_string, substring, substitute)
                print(user_string)
            else:
                print("Nothing to replace!")


print(f"Your password is: {user_string}")
