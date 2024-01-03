def fill_the_box(height, length, width, *args):
    box_capacity = height * length * width
    boxes_left_counter = 0

    for item in args:
        if item == "Finish":
            break
        if box_capacity - item < 0 and box_capacity > 0:
            item = abs(box_capacity - item)
            box_capacity = 0

        box_capacity -= item
        if box_capacity <= 0:
            boxes_left_counter += item

    if box_capacity > 0:
        return f"There is free space in the box. You could put {box_capacity} more cubes."
    return f"No more free space! You have {boxes_left_counter} more cubes."


print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
