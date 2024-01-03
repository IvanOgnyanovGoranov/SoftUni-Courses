odd_set = set()
even_set = set()

for current_row in range(1, int(input()) + 1):
    sum_of_name = sum([ord(let) for let in input()]) // current_row

    if sum_of_name % 2 == 0:
        even_set.add(sum_of_name)
    else:
        odd_set.add(sum_of_name)
if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep= ", ")
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep= ", ")
else:
    print(*odd_set.difference(even_set), sep= ", ")
