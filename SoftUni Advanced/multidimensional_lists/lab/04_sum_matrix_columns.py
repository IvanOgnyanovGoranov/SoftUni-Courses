rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    column = [int(x) for x in input().split()]
    matrix.append(column)

for i in range(columns):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][i]
    print(total_sum)

