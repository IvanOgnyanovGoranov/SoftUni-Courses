cities_dict = {}

while True:
    command = input()
    if command == "Sail":
        break
    city, population, gold = command.split("||")
    population, gold = int(population), int(gold)
    if city not in cities_dict:
        cities_dict[city] = [population, gold]
    else:
        cities_dict[city][0] += population
        cities_dict[city][1] += gold

print(cities_dict)
