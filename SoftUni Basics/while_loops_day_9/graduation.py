name = input()

average_grade = 0
years_number = 0
failed_years = 0

while True:
    current_grade = float(input())


    if current_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {years_number + 1} grade")
            break
    else:
        average_grade += current_grade
        years_number += 1
        if years_number == 12:
            average_grade = average_grade / 12
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break