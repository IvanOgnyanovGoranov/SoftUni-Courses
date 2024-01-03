rows, cols = [int(x) for x in input().split(",")]

moves = {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
         }

mouse = []
cookies = 0
cupboard = []

for row in range(rows):
    cupboard.append(list(input()))
    if "M" in cupboard[-1]:
        mouse = [row, cupboard[row].index("M")]
    if "C" in cupboard[-1]:
        cookies += cupboard[-1].count("C")

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    row_move = moves[command][0] + mouse[0]
    col_move = moves[command][1] + mouse[1]

    if not (0 <= row_move < rows and 0 <= col_move < cols):
        print("No more cheese for tonight!")
        break

    if cupboard[row_move][col_move] == "C":
        cupboard[mouse[0]][mouse[1]] = "*"
        cupboard[row_move][col_move] = "M"
        mouse = row_move, col_move
        cookies -= 1
        if cookies == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard[row_move][col_move] == "T":
        cupboard[mouse[0]][mouse[1]] = "*"
        cupboard[row_move][col_move] = "M"
        mouse = row_move, col_move
        print("Mouse is trapped!")
        break
    elif cupboard[row_move][col_move] == "*":
        cupboard[mouse[0]][mouse[1]] = "*"
        cupboard[row_move][col_move] = "M"
        mouse = row_move, col_move

    elif cupboard[row_move][col_move] == "@":
        continue

for row in cupboard:
    print("".join(row))