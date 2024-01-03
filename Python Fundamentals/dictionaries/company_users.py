employees = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    company, id = command[0], command[1]

    if company not in employees:
        employees[company] = []
    if id in employees[company]:
        continue
    employees[company] += [id]

for company, id in employees.items():
    print(company)
    for element in id:
        print(f"-- {element}")


