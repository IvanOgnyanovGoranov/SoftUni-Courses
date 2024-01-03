N = int(input())

matrix = [input().split() for _ in range(N)]
bunny = []
for row in range(N):
    for col in range(N):
        if matrix[row][col] == "B":
            bunny = [row, col]
            break

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

max_eggs = float('-inf')
max_direction = ""
max_eggs_matrix = []

for direction, move in moves.items():
    eggs = 0
    curr_eggs = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < N and 0 <= col < N:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        curr_eggs.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and curr_eggs:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)