number_of_visitors = int(input())

back = 0
chest = 0
legs = 0
abs_exercise = 0
protein_shake = 0
protein_bar = 0

training_people = 0
protein_people = 0

for _ in range(number_of_visitors):
    activity = input()
    if activity == "Back":
        back += 1
        training_people += 1
    elif activity == "Chest":
        chest += 1
        training_people += 1
    elif activity == "Legs":
        legs += 1
        training_people += 1
    elif activity == "Abs":
        abs_exercise += 1
        training_people += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein_people += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein_people += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_exercise} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training_people / number_of_visitors * 100:.2f}% - work out")
print(f"{protein_people / number_of_visitors * 100:.2f}% - protein")