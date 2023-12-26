rows, cols = [int(x) for x in input().split()]

field = []
starting_position = []
current_boy_position = []
moves = {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
         }

for row in range(rows):
    field.append(list(input()))
    if "B" in field[-1]:
        starting_position = [row, field[row].index("B")]
        current_boy_position = starting_position

while True:
    command = input()

    row_move = moves[command][0] + current_boy_position[0]
    col_move = moves[command][1] + current_boy_position[1]

    if not (0 <= row_move < rows and 0 <= col_move < cols):
        field[starting_position[0]][starting_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    if field[row_move][col_move] == "*":
        continue

    elif field[row_move][col_move] == "P":
        field[row_move][col_move] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
    elif field[row_move][col_move] == "A":
        field[row_move][col_move] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif field[row_move][col_move] == "-":
        field[row_move][col_move] = "."

    current_boy_position = [row_move, col_move]

for row in field:
    print("".join(row))
