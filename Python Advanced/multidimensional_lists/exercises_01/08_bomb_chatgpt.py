from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = [tuple(map(int, x.split(',')) for x in input().split())]

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (1, -1), (-1, 1), (1, 1)
]

alive_cells = 0
total_sum = 0

for bombs in bomb_coordinates:
    for bomb in bombs:
        bomb_row, bomb_col = bomb
        bomb_power = matrix[bomb_row][bomb_col]

        if bomb_power <= 0:
            continue

        matrix[bomb_row][bomb_col] = 0

        for direction in directions:
            dr, dc = direction
            new_row, new_col = bomb_row + dr, bomb_col + dc

            if 0 <= new_row < n and 0 <= new_col < n:
                cell_value = matrix[new_row][new_col]

                if cell_value > 0:
                    matrix[new_row][new_col] -= bomb_power

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            total_sum += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")

for row in matrix:
    print(*row)