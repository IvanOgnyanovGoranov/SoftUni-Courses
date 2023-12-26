number_of_students = int(input())

top_students = 0
between_4_5 = 0
between_3_4 = 0
failed = 0
average = 0

for _ in range(number_of_students):
    grade = float(input())
    average += grade
    if grade >= 5:
        top_students += 1
    elif grade >= 4:
        between_4_5 += 1
    elif grade >= 3:
        between_3_4 += 1
    else:
        failed += 1

average = average / number_of_students

print(f"Top students: {(top_students / number_of_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_5 / number_of_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_4 / number_of_students) * 100:.2f}%")
print(f"Fail: {(failed / number_of_students) * 100:.2f}%")
print(f"Average: {average:.2f}")
