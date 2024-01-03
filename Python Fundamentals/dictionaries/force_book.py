force_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        command = command.split(" | ")
        force_side, user = command[0], command[1]
        name_in_values = False
        for value in force_dict.values():
            for item in value:
                if user == item:
                    name_in_values = True
        if force_side not in force_dict.keys() and not name_in_values:
            force_dict[force_side] = [user]
        elif force_side in force_dict and not name_in_values:
            force_dict[force_side] += [user]
        elif name_in_values:
            continue

    elif " -> "  in command:
        command = command.split(" -> ")
        user, force_side = command[0], command[1]
        user_exists = False
        target_key = ""
        for key,value in force_dict.items():
            for item in value:
                if item == user:
                    user_exists = True
                    target_key = key
        if user_exists and force_side not in force_dict.keys():
            force_dict[target_key].remove(user)
            force_dict[force_side] = [user]
            print(f"{user} joins the {force_side} side!")
        elif user_exists and force_side in force_dict.keys():
            force_dict[target_key].remove(user)
            force_dict[force_side] += [user]
            print(f"{user} joins the {force_side} side!")
        elif not user_exists and force_side not in force_dict.keys():
            force_dict[force_side] = [user]
            print(f"{user} joins the {force_side} side!")
        elif not user_exists and force_side in force_dict:
            force_dict[force_side] += [user]
            print(f"{user} joins the {force_side} side!")

for k, v in force_dict.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
    for item in v:
        print(f"! {item}")