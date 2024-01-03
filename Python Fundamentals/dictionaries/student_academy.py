academy = {}
input_number = int(input())

for i in range(input_number):
    student = input()
    grade = float(input())

    if student not in academy.keys():
        academy[student] = []
    academy[student] += [grade]

for key, values in academy.items():
    average = 0
    for value in values:
        average += value
    average = average / len(values)
    academy[key] = average

for key in list(academy.keys()):
    if academy[key] < 4.5:
        del academy[key]

for key, value in academy.items():
    print(f"{key} -> {value:.2f}")




