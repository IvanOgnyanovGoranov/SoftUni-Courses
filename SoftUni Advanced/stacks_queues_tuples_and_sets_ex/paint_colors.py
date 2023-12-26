from collections import deque
from math import ceil

substrings = deque(input().split())

all_colors = ["orange", "purple", "green", "yellow", "blue", "red"]
colors_dict = {"orange": ["yellow", "red"], "purple": ["blue", "red"], "green": ["yellow", "blue"]}

colors_list = []

while substrings:
    first_sub = substrings.popleft()
    second_sub = substrings.pop() if substrings else ""
    concatenated_str_one = first_sub + second_sub
    concatenated_str_two = second_sub + first_sub

    if concatenated_str_one in all_colors:
        colors_list.append(concatenated_str_one)
        continue

    if concatenated_str_two in all_colors:
        colors_list.append(concatenated_str_two)
        continue

    first_sub = first_sub[:-1]
    second_sub = second_sub[:-1]
    middle_index = ceil(len(substrings) / 2)
    if second_sub:
        substrings.insert(middle_index, second_sub)
    if first_sub:
        substrings.insert(middle_index, first_sub)


for color in colors_list:
    needed_colors = 0
    if color in colors_dict.keys():
        for value in colors_dict[color]:
            if value in colors_list:
                needed_colors += 1
        if needed_colors != 2:
            colors_list.remove(color)

print(colors_list)

