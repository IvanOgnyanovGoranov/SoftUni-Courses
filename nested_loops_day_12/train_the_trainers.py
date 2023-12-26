number_of_judges = int(input())

number_of_projects = 0
project_grade = 0
average_project_grade = 0

while True:
    name_of_project = input()

    average_grade = 0
    loop_number = 0

    if name_of_project == "Finish":
        print(f"Student's final assessment is {average_project_grade / number_of_projects:.2f}.")
        break
    else:
        number_of_projects += 1

    for _ in range(1, number_of_judges + 1):
        grade = float(input())
        average_grade += grade
        loop_number += 1
        if loop_number == number_of_judges:
            project_grade = average_grade / number_of_judges
            print(f"{name_of_project} - {project_grade:.2f}.")
            average_project_grade += project_grade
