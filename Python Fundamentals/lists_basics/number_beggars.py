money_as_string = input().split(", ")
beggars_count = int(input())
money_as_digits = []

for element in money_as_string:
    money_as_digits.append(int(element))

final_sums = []
start_index = 0

while start_index < beggars_count:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_digits), beggars_count):
        current_beggar_sum += money_as_digits[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)