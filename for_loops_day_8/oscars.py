actor = input()
academy_score = float(input())
number_of_judges = int(input())

MAX_POINTS = 1250.5

for n in range(number_of_judges):
    judge_name = input()
    judges_points = float(input())

    academy_score += len(judge_name) * judges_points / 2

    if academy_score > MAX_POINTS:
        print(f"Congratulations, {actor} got a nominee for leading role with {academy_score:.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {MAX_POINTS - academy_score:.1f} more!")



