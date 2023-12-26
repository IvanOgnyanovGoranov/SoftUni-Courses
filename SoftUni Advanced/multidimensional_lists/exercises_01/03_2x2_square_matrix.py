rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
number_of_squares = 0
for row in range(rows - 1):
    for col in range(columns - 1):
        first_n = matrix[row][col]
        right_side_n = matrix[row][col + 1]
        below_n = matrix[row + 1][col]
        diagonal_n = matrix[row + 1][col + 1]
        if first_n == right_side_n and right_side_n ==  below_n and below_n == diagonal_n:
            number_of_squares += 1

print(number_of_squares)
