from collections import deque

box_of_clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
racks_used = 0
current_rack = 0

while box_of_clothes:
    piece_of_clothing = box_of_clothes[-1]
    if piece_of_clothing + current_rack > rack_capacity:
        current_rack = piece_of_clothing
        racks_used += 1
    else:
        current_rack += piece_of_clothing
    if len(box_of_clothes) == 1:
        racks_used += 1
    box_of_clothes.pop()

print(racks_used)
