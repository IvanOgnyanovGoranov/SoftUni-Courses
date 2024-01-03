rows = int(input())
matrix = []

for row in range(rows):
    nested_list = [int(x) for x in input().split(", ")]
    matrix.append(nested_list)

flattened = [num for row in matrix for num in row]
print(flattened)

