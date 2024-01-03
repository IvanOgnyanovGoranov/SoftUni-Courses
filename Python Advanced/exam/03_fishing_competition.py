SIZE = int(input())

moves = {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
         }

position = []
area = []
ship_alive = True

for row in range(SIZE):
    area.append(list(input()))
    if "S" in area[-1]:
        position = [row, area[row].index("S")]

fish_collected = 0

while True:
    direction = input()
    if direction == "collect the nets":
        break

    row_move = moves[direction][0] + position[0]
    col_move = moves[direction][1] + position[1]

    if not (0 <= row_move < SIZE and 0 <= col_move < SIZE):
        if row_move < 0:
            row_move = SIZE + row_move
        elif row_move >= SIZE:
            row_move = SIZE - row_move
        if col_move < 0:
            col_move = SIZE + col_move
        elif col_move >= SIZE:
            col_move = SIZE - col_move

    if area[row_move][col_move] == "-":
        area[row_move][col_move] = "S"
        area[position[0]][position[1]] = "-"
        position = row_move, col_move

    elif area[row_move][col_move] == "W":
        area[position[0]][position[1]] = "-"
        ship_alive = False
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row_move},{col_move}]")
        break

    else:
        fish_collected += int(area[row_move][col_move])
        area[row_move][col_move] = "S"
        area[position[0]][position[1]] = "-"
        position = row_move, col_move

if ship_alive:
    if fish_collected >= 20:
        print("Success! You managed to reach the quota!")

    elif fish_collected < 20:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_collected} tons of fish more.")

    if fish_collected > 0:
        print(f"Amount of fish caught: {fish_collected} tons.")

    for row in area:
        print("".join(row))
