rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


while True:
    command = input()
    if command == "END":
        break
    line = command.split()
    if len(line) != 5 or line[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in line[1:]]
    if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col2 < columns and 0 <= col1 < columns:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")



