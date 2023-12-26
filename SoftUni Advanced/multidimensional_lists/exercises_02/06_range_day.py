def move(direction, steps):
    r = position[0] + (directions[direction][0] * steps)
    c = position[1] + (directions[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return position
    if field[r][c] == "x":
        return position

    return [r, c]

def shoot(direction):
    r = position[0] + directions[direction][0]
    c = position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return[r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
field = []

targets = 0
target_hits = 0
target_hit_positions = []

position = []

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(SIZE):
    field.append(input().split())

    if "A" in field[row]:
        position = [row, field[row].index("A")]

    targets += field[row].count('x')

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        targets_down_pos = shoot(command_info[1])

        if targets_down_pos:
            target_hit_positions.append(targets_down_pos)
            target_hits += 1

        if target_hits == targets:
            print(f"Training completed! All {targets} targets hit.")
            break
else:
    print(f"Training not completed! {targets - target_hits} targets left.")

print(*target_hit_positions, sep="\n")