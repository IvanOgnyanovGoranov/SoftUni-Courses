sequence_of_numbers = input().split(" ")
string = input()
indexes_list = []
message = ""

for index in sequence_of_numbers:
    numbers_sum = 0
    for number in index:
        numbers_sum += int(number)
    indexes_list.append(numbers_sum)

for index in indexes_list:
    while len(string) < index:
        index -= len(string)
    message += string[index]
    string = string[:index] + string[index + 1:]

print(message)

