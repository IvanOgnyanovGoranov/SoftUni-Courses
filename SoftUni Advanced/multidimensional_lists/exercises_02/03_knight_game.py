def knight_movement(knight_row, knight_col):
    global matrix
    possible_attacks = 0
    if knight_row - 1 >= 0 and knight_col - 2 >= 0:
        if matrix[knight_row - 1][knight_col - 2] == "K":
            possible_attacks += 1
    if knight_row - 2 >= 0 and knight_col - 1 >= 0:
        if matrix[knight_row - 2][knight_col - 1] == "K":
            possible_attacks += 1
    if knight_row + 1 <= N - 1 and knight_col - 2 >= 0:
        if matrix[knight_row + 1][knight_col - 2] == "K":
            possible_attacks += 1
    if knight_row + 2 <= N - 1 and knight_col - 1 >= 0:
        if matrix[knight_row + 2][knight_col - 1] == "K":
            possible_attacks += 1

    if knight_row - 2 >= 0 and knight_col + 1 <= N - 1:
        if matrix[knight_row - 2][knight_col + 1] == "K":
            possible_attacks += 1
    if knight_row - 1 >= 0 and knight_col + 2 <= N - 1:
        if matrix[knight_row - 1][knight_col + 2] == "K":
            possible_attacks += 1
    if knight_row + 2 <= N - 1 and knight_col + 1 <= N - 1:
        if matrix[knight_row + 2][knight_col + 1] == "K":
            possible_attacks += 1
    if knight_row + 1 <= N - 1 and knight_col + 2 <= N - 1:
        if matrix[knight_row + 1][knight_col + 2] == "K":
            possible_attacks += 1
    return possible_attacks

N = int(input())

matrix = [list(input()) for _ in range(N)]
knights_removed = 0

while True:
    most_attacks = 0
    position = []
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == "K":
                attacks = knight_movement(row, col)
                if attacks > most_attacks:
                    most_attacks = attacks
                    position = [row, col]

    if most_attacks > 0:
        row, col = position[0], position[1]
        matrix[row][col] = "0"
        knights_removed += 1
    else:
        break

print(knights_removed)
