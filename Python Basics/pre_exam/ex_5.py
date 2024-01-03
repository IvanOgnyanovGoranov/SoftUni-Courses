best_player = None
hat_trick = None
most_goals = 0

while True:
    name_of_player = input()

    if name_of_player == "END":
        break

    goals = int(input())

    if goals > most_goals:
        best_player = name_of_player
        most_goals = goals
        if most_goals >= 3:
            hat_trick = name_of_player

    if goals >= 10:
        break

print(f"{best_player} is the best player!")

if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")