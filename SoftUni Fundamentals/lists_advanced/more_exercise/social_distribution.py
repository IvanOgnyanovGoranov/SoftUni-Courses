population = input().split(", ")
minimum_wealth = int(input())
population = [int(x) for x in population]

for index in range(len(population)):
    highest_number_by_index = 0
    for i in range(len(population)):
        if population[i] > highest_number_by_index:
            highest_number_by_index = i
    if population[index] < minimum_wealth:
        if population[highest_number_by_index] - (minimum_wealth - population[index]) >= minimum_wealth:
            population[highest_number_by_index] -= (minimum_wealth - population[index])
            population[index] += (minimum_wealth - population[index])

        elif population[highest_number_by_index] > minimum_wealth:
            population[highest_number_by_index] = population[highest_number_by_index] - (population[highest_number_by_index] - minimum_wealth)
            population[index] += population[highest_number_by_index] - (population[highest_number_by_index] - minimum_wealth)
        else:
            print("No equal distribution possible")
            exit()
    else:
        continue
print(population)
#unsolved 60/100