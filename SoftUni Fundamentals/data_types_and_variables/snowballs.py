number_of_snowballs = int(input())
best_value_snowball = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for i in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > best_value_snowball:
        best_value_snowball = value
        snowball_weight = weight
        snowball_time = time_needed
        snowball_quality = quality
print(f"{snowball_weight} : {snowball_time} = {int(best_value_snowball)} ({snowball_quality})")