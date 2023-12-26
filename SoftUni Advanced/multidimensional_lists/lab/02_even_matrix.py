rows = int(input())
matrix = []


for row in range(rows):
    nested_list = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(nested_list)

print(matrix)