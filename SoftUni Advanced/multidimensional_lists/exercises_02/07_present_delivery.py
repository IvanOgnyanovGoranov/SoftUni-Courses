presents = int(input())
SIZE = int(input())

field = []
santa_pos = []
nice_kids_left = 0
kids_received_presents = 0

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(SIZE):
    field.append(input().split())
    if "S" in field[row]:
        santa_pos = [row, field[row].index("S")]
    if "V" in field[row]:
        count = field[row].count("V")
        nice_kids_left += count

# Santa starts going to houses
while presents and nice_kids_left > 0:
    command = input()
    if command == "Christmas morning":
        break

    row_move = moves[command][0] + santa_pos[0]
    col_move = moves[command][1] + santa_pos[1]

    if field[santa_pos[0]][santa_pos[1]] != "C":  # check this line for a mistake(should be row move, col move)
        field[santa_pos[0]][santa_pos[1]] = "-"  # Santa's old position
    santa_pos = [row_move, col_move]  # Santa's new position

    if field[row_move][col_move] == "V":
        nice_kids_left -= 1
        kids_received_presents += 1
        presents -= 1

    elif field[row_move][col_move] == "C":
        for key, value in moves.items():
            row_check = moves[key][0] + row_move
            col_check = moves[key][1] + col_move

            if field[row_check][col_check] == "V" or field[row_check][col_check] == "X":
                presents -= 1
                if field[row_check][col_check] == "V":
                    nice_kids_left -= 1
                    kids_received_presents += 1
            if presents == 0:
                field[row_check][col_check] = "-"
                break
            field[row_check][col_check] = "-"

    if presents == 0:
        print("Santa ran out of presents!")

    field[row_move][col_move] = "S"  # Santa's new position in the matrix

[print(*row) for row in field]
if nice_kids_left == 0:
    print(f"Good job, Santa! {kids_received_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
