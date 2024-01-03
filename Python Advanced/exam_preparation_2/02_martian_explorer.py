SIZE = 6

direction_map = {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
         }

rover = []
field = []
deposits = ["Concrete", "Metal", "Water"]

for row in range(SIZE):
    field.append(input().split())
    if "E" in field[-1]:
        rover = [row, field[row].index("E")]

commands = input().split(", ")

for direction in commands:
    row_move = rover[0] + direction_map[direction][0]
    col_move = rover[1] + direction_map[direction][1]

    if not (0 <= row_move < SIZE and 0 <= col_move < SIZE):
        if row_move < 0:
            row_move = 6 + row_move
        elif row_move >= SIZE:
            row_move = 6 - row_move
        if col_move < 0:
            col_move = 6 + col_move
        elif col_move >= SIZE:
            col_move = 6 - col_move


    if field[row_move][col_move] == "W":
        print(f"Water deposit found at {row_move, col_move}")
        rover = row_move, col_move
        if "Water" in deposits:
            deposits.remove("Water")

    elif field[row_move][col_move] == "M":
        print(f"Metal deposit found at {row_move, col_move}")
        rover = row_move, col_move
        if "Metal" in deposits:
            deposits.remove("Metal")

    elif field[row_move][col_move] == "C":
        print(f"Concrete deposit found at {row_move, col_move}")
        rover = row_move, col_move
        if "Concrete" in deposits:
            deposits.remove("Concrete")

    elif field[row_move][col_move] == "R":
        print(f"Rover got broken at ({row_move}, {col_move})")
        break

    elif field[row_move][col_move] == "-":
        rover = row_move, col_move

if not deposits:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")