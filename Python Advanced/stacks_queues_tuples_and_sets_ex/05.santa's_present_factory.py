from collections import deque

materials = deque(int(x) for x in input().split())
toys_magic_levels = deque(int(x) for x in input().split())

doll_magic_needed = 150
train_magic_needed = 250
bear_magic_needed = 300
bicycle_magic_needed = 400

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents_crafted = {}

while toys_magic_levels and materials:
    magic_level = materials[-1] * toys_magic_levels[0]

    if magic_level in presents:
        new_present = presents[magic_level]
        if new_present not in presents_crafted:
            presents_crafted[new_present] = 0
        presents_crafted[new_present] += 1
        materials.pop()
        toys_magic_levels.popleft()

    elif magic_level < 0:
        materials.append(materials.pop() + toys_magic_levels.popleft())
    elif magic_level > 0:
        toys_magic_levels.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and toys_magic_levels[0] == 0:
        toys_magic_levels.popleft()
        materials.pop()
    elif materials[-1] == 0:
        materials.pop()
    elif toys_magic_levels[0] == 0:
        toys_magic_levels.popleft()



presents_are_crafted = False

if "Doll" in presents_crafted and "Wooden train" in presents_crafted:
    presents_are_crafted = True
if "Teddy bear" in presents_crafted and "Bicycle" in presents_crafted:
    presents_are_crafted = True

if presents_are_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if toys_magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in toys_magic_levels)}")

for key, value in sorted(presents_crafted.items()):
    print(f"{key}: {value}")
