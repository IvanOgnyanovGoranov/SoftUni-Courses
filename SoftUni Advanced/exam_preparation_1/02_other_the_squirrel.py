from collections import deque

SIZE = int(input())
commands = deque(input().split(", "))

field = []
squirrel = []

for row in range(SIZE):
    field.append(list(input()))
    if "s" in field[-1]:
        squirrel = [row, field[row].index("s")]

direction_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hazelnuts_to_collect = 3

while hazelnuts_to_collect and commands:
    current_command = commands.popleft()

    new_row = squirrel[0] + direction_map[current_command][0]
    new_col = squirrel[1] + direction_map[current_command][1]

    if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
        print("The squirrel is out of the field.")
        break

    if field[new_row][new_col] == "h":
        field[squirrel[0]][squirrel[1]] = "*"
        field[new_row][new_col] = "s"
        squirrel = new_row, new_col
        hazelnuts_to_collect -= 1

    elif field[new_row][new_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif field[new_row][new_col] == "*":
        squirrel = new_row, new_col

    if hazelnuts_to_collect == 0:
        print("Good job! You have collected all hazelnuts!")

    if hazelnuts_to_collect > 0 and not commands:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {3 - hazelnuts_to_collect}")
