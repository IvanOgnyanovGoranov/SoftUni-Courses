N = int(input())

# Initialize an empty matrix to store the values

matrix = [[int(x) for x in input.split(", ")]for _ in range(N)]
primary_sum = 0
opposite_sum = 0

primary_matrix = []
opposite_matrix= []
#opposite diagonal
for i in range(N):
    opposite_sum += matrix[i][N - i - 1]
    opposite_matrix.append(matrix[i][N - i - 1])

primary_diagonal = [matrix[i][i] for i in range(n)]
for i in range(N):
    primary_sum += matrix[i][i]
    primary_matrix.append(matrix[i][i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_matrix)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in opposite_matrix)}. Sum: {opposite_sum}")
