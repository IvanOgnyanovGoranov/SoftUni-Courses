matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]


while True:
    line = input()
    if line == "END":
        break

    command, row, col, value = line.split()
    row, col, value = int(row), int(col), int(value)

    if row < 0 or row > len(matrix) -1 or col < 0 or col > len(matrix[row]) -1:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

[print(*row) for row in matrix]
# for row in matrix:
#     print(*row)

