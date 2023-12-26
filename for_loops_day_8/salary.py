number_of_tabs = int(input())
salary = float(input())

fine = 0

for _ in range(1, number_of_tabs + 1):
    website = input()
    if website == "Facebook":
        fine += 150
    elif website == "Instagram":
        fine += 100
    elif website == "Reddit":
        fine += 50
    else:
        fine += 0
    if salary - fine <= 0:
        print("You have lost your salary.")
        break
    else:
        continue

if salary - fine > 0:
    print(int(salary - fine))
