list_of_numbers = input().split()
numbers_to_remove = int(input())
new_list = []
for num in list_of_numbers:
    new_list.append(int(num))

for _ in range(numbers_to_remove):
    previous_number = 887437843873439
    for current_number in new_list:
        if current_number < previous_number:
            previous_number = current_number
    new_list.remove(previous_number)
print(*new_list, sep=', ')


