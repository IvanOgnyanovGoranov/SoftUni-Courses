bands = {}
first_on_stage = []
total_play_time = 0

while True:
    command = input().split("; ")
    if command[0] == "Start!":
        break

    if command[0] == "Add":
        band = command[1]
        members = command[2].split(", ")

        if band not in bands:
            bands[band] = {'members': [], 'time': 0}
        for member in members:
            if member not in bands[band]["members"]:
                bands[band]["members"].append(member)

    elif command[0] == "Play":
        band_name, time = command[1], int(command[2])
        first_on_stage.append(band_name)
        if band_name not in bands:
            bands[band_name] = {'members': [], 'time': 0}
        bands[band_name]["time"] += time
        total_play_time += time


print(f"Total time: {total_play_time}")
for band, value in bands.items():
    print(f"{band} -> {bands[band]['time']}")

print(first_on_stage[0])
for member in bands[first_on_stage[0]]["members"]:
    print(f"=> {member}")


