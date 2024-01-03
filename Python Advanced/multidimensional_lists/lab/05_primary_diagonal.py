# rows_and_columns = int(input())
# matrix = []
#
# for row in range(rows_and_columns):
#     column = [int(x) for x in input().split()]
#     matrix.append(column)
#
# sum = 0
# for i in range(rows_and_columns):
#     sum += matrix[i][i]
# print(sum)
# Read the size of the square matrix
N = int(input())

# Initialize an empty matrix to store the values
matrix = []

# Read the matrix values
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)



#opposite diagonal
for i in range(N):
    print(matrix[i][N - i - 1])
