while True:
    user_input = input()
    if user_input == "SoftUni":
        continue
    elif user_input == "End":
        break

    word = ""
    for element in user_input:
        word += element * 2
    print(word)