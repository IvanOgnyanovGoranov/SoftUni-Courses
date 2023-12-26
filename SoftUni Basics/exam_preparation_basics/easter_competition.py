number_of_sweet_breads = int(input())

new_number_one = None
best_result = -1000000000000000000000

for _ in range(number_of_sweet_breads):
    name_of_baker = input()
    baker_total_score = 0

    while True:
        score = input()

        if score == "Stop":
            print(f"{name_of_baker} has {baker_total_score} points.")
            if baker_total_score > best_result:
                new_number_one = name_of_baker
                best_result = baker_total_score
                print(f"{name_of_baker} is the new number 1!")
            break

        baker_total_score += int(score)

print(f"{new_number_one} won competition with {best_result} points!")