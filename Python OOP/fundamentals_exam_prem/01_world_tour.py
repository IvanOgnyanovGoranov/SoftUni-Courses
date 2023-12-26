def add_stop(stops, index, stop_to_add):
    new_string = stops
    if index < len(stops):
        new_string = stops[:index] + stop_to_add + stops[index:]
    return new_string

def remove_stop(stops, start_index, end_index):
    new_string = stops
    if end_index < len(stops) and start_index >= 0 and start_index < len(stops):
        new_string = stops[:start_index] + stops[end_index + 1:]
    return new_string

def switch_strings(stops, old_str, new_str):
    new_string = stops
    if old_str in stops:
        new_string = stops.replace(old_str, new_str)
    return new_string


stops = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    if command[0] == "Add Stop":
        command, index, stop = command
        stops = add_stop(stops, int(index), stop)
        print(stops)

    elif command[0] == "Remove Stop":
        command, st_index, end_index = command
        stops = remove_stop(stops, int(st_index), int(end_index))
        print(stops)

    elif command[0] == "Switch":
        command, old, new = command
        stops = switch_strings(stops, old, new)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
