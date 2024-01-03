user_string = input()

while True:
    command = input().split(" ")
    if command[0] == "Done":
        break
    if command[0] == "Change":
        user_string = user_string.replace(command[1], command[2])
        print(user_string)
    elif command[0] == "Includes":
        includes = False
        if command[1] in user_string:
            includes = True
        print(includes)
    elif command[0] == "End":
        end = False
        string_as_list = user_string.split(" ")
        if command[1] == string_as_list[-1]:
            end = True
        print(end)
    elif command[0] == "Uppercase":
        user_string = user_string.upper()
        print(user_string)
    elif command[0] == "FindIndex":
        for letter in user_string:
            if command[1] == letter:
                i = user_string.index(letter)
                print(i)
                break
    elif command[0] == "Cut":
        first_index = int(command[1])
        last_index = int(command[2])
        user_string = user_string[first_index:]
        new_string = ""
        for i in range(last_index):
            new_string += user_string[i]
        user_string = new_string
        print(user_string)