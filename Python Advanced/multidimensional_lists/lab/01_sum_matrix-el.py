rows_and_columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for row in range(rows_and_columns[0]):
    nested_list = [int(x) for x in input().split(", ")]
    matrix.append(nested_list)
    total_sum += sum(nested_list)

print(total_sum)
print(matrix)
