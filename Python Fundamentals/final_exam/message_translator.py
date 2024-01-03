def is_valid(command):
    is_valid = False
    first_part_is_valid = False
    valid_string = ""
    if ":" in command:
        command = command.split(":")
        actual_command = command[0]
        if actual_command[0] == "!" and actual_command[-1] == "!":
            if len(actual_command) >= 5:
                if actual_command[1].isupper():
                    first_part_is_valid = True
    if first_part_is_valid == True:
        actual_string = command[1]
        if actual_string[0] == "[" and actual_string[-1] == "]":
            if len(actual_string) >= 10:
                is_valid = True
                valid_string += actual_string
    if is_valid == False:
        return "The message is invalid"
    new_string = valid_string[1:]
    new_string = new_string[:-1]
    return is_valid

def translator(valid_command):
    numbers = []
    new_command = valid_command.split(":")
    actual_command = new_command[0]
    actual_string = new_command[1]
    valid_command1 = actual_command[1:]
    valid_command1 = valid_command1[:-1]
    valid_string = actual_string[1:]
    valid_string = valid_string[:-1]

    for letter in valid_string:
        letter = ord(letter)
        numbers.append(letter)
    string_numbers = []
    for num in numbers:
        num = str(num)
        string_numbers.append(num)
    return f"{valid_command1}: {' '.join(string_numbers)}"


count_of_inputs = int(input())
for _ in range(count_of_inputs):
    user_command = input()
    if is_valid(user_command) == True:
        print(translator(user_command))
    else:
        print("The message is invalid")



