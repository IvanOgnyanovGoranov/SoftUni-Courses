courses = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course_name, student = command

    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student)

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")