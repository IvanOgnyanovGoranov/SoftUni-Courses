N = int(input())

matrix = [input().split() for _ in range(N)]
alice = []
for row in range(N):
    for col in range(N):
        if matrix[row][col] == "A":
            alice = [row, col]
            break

tea_bags = 0
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


while tea_bags < 10:
    command = input()
    if not command:
        break

    row_move = moves[command][0] + alice[0]
    col_move = moves[command][1] + alice[1]
    matrix[alice[0]][alice[1]] = "*"  # Alice leaving current location
    alice = [row_move, col_move]

    if not (0 <= row_move < N and 0 <= col_move < N):
        break

    elif matrix[row_move][col_move] == "R":
        matrix[row_move][col_move] = "*"
        break
    elif matrix[row_move][col_move] == "*":
        continue
    elif matrix[row_move][col_move] == ".":
        matrix[row_move][col_move] = "*"
    else:
        tea_bags += int(matrix[row_move][col_move])
        matrix[row_move][col_move] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
