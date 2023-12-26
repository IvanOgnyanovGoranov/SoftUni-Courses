number_of_people = int(input())
capacity_of_elevator = int(input())
courses = 0

if number_of_people > capacity_of_elevator:
    while number_of_people > 0:
        courses += 1
        number_of_people -= capacity_of_elevator
else:
    courses += 1
print(courses)