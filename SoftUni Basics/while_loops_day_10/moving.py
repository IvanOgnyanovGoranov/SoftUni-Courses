width = int(input())
length = int(input())
height = int(input())

total_sum_of_boxes = 0
total_space = width * length * height

while total_space >= total_sum_of_boxes:
    boxes = input()

    if boxes == "Done":
        print(f"{total_space - total_sum_of_boxes} Cubic meters left.")
        break

    total_sum_of_boxes += int(boxes)
else:
    print(f"No more free space! You need {total_sum_of_boxes - total_space} Cubic meters more.")