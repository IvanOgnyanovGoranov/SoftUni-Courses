longest_intersection = set()

for _ in range(int(input())):
    first_set = set()
    second_set = set()
    first_range, second_range = input().split("-")
    first_number, second_number = [int(x) for x in first_range.split(",")]
    third_number, fourth_number = [int(x) for x in second_range.split(",")]
    for i in range(first_number, second_number + 1):
        i = int(i)
        first_set.add(i)
    for i in range(third_number, fourth_number + 1):
        i = int(i)
        second_set.add(i)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
length = len(longest_intersection)
longest_intersection = ', '.join(map(str, longest_intersection))
print(f"Longest intersection is [{longest_intersection}] with length {length}")


