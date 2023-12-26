results = {}
submissions = {}

while True:
    command = input().split("-")
    if command[0] == "exam finished":
        break
    if command[1] == "banned":
        banned_name = command[0]
        del results[banned_name]
        continue

    name, language, points = command[0], command[1], int(command[2])

    if name not in results.keys():
        results[name] = 0
    if results[name] < points:
        results[name] = points
    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1


print("Results:")
for name, values in results.items():
    print(f"{name} | {values}")
print("Submissions:")
for language, number in submissions.items():
    print(f"{language} - {number}")

