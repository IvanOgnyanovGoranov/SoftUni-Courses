numbers_list = input().split(", ")
zeros = 0
new_list = []
for number in numbers_list:
    if number == "0":
        zeros += 1
    else:
        new_list.append(int(number))

for zero in range(zeros):
    new_list.append(0)

print(new_list)

