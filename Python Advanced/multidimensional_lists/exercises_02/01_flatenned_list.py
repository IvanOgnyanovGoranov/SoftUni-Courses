string = input().split("|")

final_list = []

for substring in string[::-1]:
    final_list.extend(substring.split())

print(*final_list)
