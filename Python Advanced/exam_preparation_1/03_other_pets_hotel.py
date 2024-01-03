def accommodate_new_pets(capacity: int, max_weight: float, *args):
    total_pets_accommodated = 0
    pets = {}
    no_capacity = False

    for pet in args:
        type_of_pet = pet[0]
        weight = pet[1]
        if not capacity:
            no_capacity = True
            break
        if weight > max_weight:
            continue
        capacity -= 1
        total_pets_accommodated += 1
        if type_of_pet not in pets.keys():
            pets[type_of_pet] = []
        pets[type_of_pet] += [weight]

    result = ""
    if no_capacity:
        result += f"You did not manage to accommodate all pets!\nAccommodated pets:\n"
        for pet, number in sorted(pets.items()):
            result += f"{pet}: {len(number)}\n"
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n"
        for pet, number in sorted(pets.items()):
            result += f"{pet}: {len(number)}\n"

    return result


print(accommodate_new_pets(
    2,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
