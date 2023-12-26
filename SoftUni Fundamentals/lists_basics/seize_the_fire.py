level_of_fire = input().split("#")
amount_of_water = int(input())

total_effort = 0
total_fire = 0
cells_being_put_out = []
for cell in level_of_fire:
    level_of_fire = cell.split(" = ")
    type_of_fire = level_of_fire[0]
    range_of_fire = int(level_of_fire[1])
    cell_is_valid = False
    if type_of_fire == "High" and range_of_fire >= 81 and range_of_fire <= 125:
        cell_is_valid = True
    elif type_of_fire == "Medium" and range_of_fire >= 51 and range_of_fire <= 80:
        cell_is_valid = True
    elif type_of_fire == "Low" and range_of_fire >= 1 and range_of_fire <= 50:
        cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= range_of_fire:
            amount_of_water -= range_of_fire
            total_effort += range_of_fire * 0.25
            cells_being_put_out.append(range_of_fire)
            total_fire += range_of_fire
        else:
            continue
print("Cells:")
for last_cell in cells_being_put_out:
    print(f" - {last_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")