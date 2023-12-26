N = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(N)]
primary_diagonal = [matrix[i][i] for i in range(N)]
opposite_diagonal = [matrix[i][-i - 1] for i in range(N)]

sum_difference = abs(sum(primary_diagonal) - sum(opposite_diagonal))

print(sum_difference)
