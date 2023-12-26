allowed_bad_grades = int(input())

average_grade = 0
number_of_problems = 0
bad_grades = 0

while True:
    name_of_problem = input()

    if name_of_problem == "Enough":
        print(f"Average score: {average_grade / number_of_problems:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    if grade <= 4:
        bad_grades += 1
    if allowed_bad_grades == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break


    average_grade += grade
    number_of_problems += 1
    last_problem = name_of_problem



