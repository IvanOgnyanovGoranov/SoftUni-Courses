while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
   #can be done with len()
    name_length = 0
    for char in name:
        name_length += 1

    if name_length < 5:
        print(f"{name} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{name} goes to Slytherin.")
    elif name_length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name_length > 6:
        print(f"{name} goes to Hufflepuff.")