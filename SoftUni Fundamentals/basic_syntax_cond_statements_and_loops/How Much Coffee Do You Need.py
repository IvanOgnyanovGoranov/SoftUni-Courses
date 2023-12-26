number_of_coffees = 0

while True:
    user_command = input()

    if user_command == "movie" or user_command == "dog" or user_command == "cat" or user_command == "coding":
        number_of_coffees += 1
    elif user_command == "MOVIE" or user_command == "DOG" or user_command == "CAT" or user_command == "CODING":
        number_of_coffees += 2

    if user_command == "END":
        if number_of_coffees <= 5:
            print(number_of_coffees)
            break
        else:
            print("You need extra sleep")
            break