rows, columns = [int(x) for x in input().split()]

matrix = [[int(n) for n in input().split()] for _ in range(rows)]

max_sum_matrix = []
max_sum = float('-inf')

for row in range(rows - 2):
    for col in range(columns - 2):
        first_row = matrix[row][col: col + 3]
        second_row = matrix[row + 1][col: col + 3]
        third_row = matrix[row + 2][col: col + 3]
        total_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if total_sum > max_sum:
            max_sum = total_sum
            max_sum_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for i in range(len(max_sum_matrix)):
    print(*max_sum_matrix[i])
