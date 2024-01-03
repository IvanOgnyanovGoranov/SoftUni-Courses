from collections import deque
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = deque([int(a) for a in x.split(",")] for x in input().split())

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),
              "left_up": (-1, -1), "left_down": (1, -1), "right_up": (-1, 1), "right_down": (1, 1)}

while bombs:
    current_bomb = bombs.popleft()
    bomb_row = current_bomb[0]
    bomb_col = current_bomb[1]
    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    for key, value in directions.items():
        if 0 <= bomb_row + value[0] < n and 0 <= bomb_col + value[1] < n:
            current_explosion = matrix[bomb_row + value[0]][bomb_col + value[1]]
            explosion_row, explosion_col = bomb_row + value[0], bomb_col + value[1]

            if current_explosion > 0:
                matrix[bomb_row + value[0]][bomb_col + value[1]] -= bomb_power
alive_cells = 0
total_sum = 0
for el in matrix:
    for num in el:
        if num > 0:
            alive_cells += 1
            total_sum += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")
[print(*row) for row in matrix]
