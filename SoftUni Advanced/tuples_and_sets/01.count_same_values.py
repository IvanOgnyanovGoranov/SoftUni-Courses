numbers = tuple(float(x) for x in input().split())

occ = {}

for number in numbers:
    if number not in occ:
        occ[number] = numbers.count(number)
        print(f"{number} - {numbers.count(number)} times")

