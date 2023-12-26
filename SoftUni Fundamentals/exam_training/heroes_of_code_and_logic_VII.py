
def cast_spell(hero, mp_needed, spell_name):
    global heroes
    if mp_needed <= heroes[hero]["MP"]:
        heroes[hero]["MP"] -= mp_needed
        return f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!"
    return f"{hero} does not have enough MP to cast {spell_name}!"

def take_damage(hero, damage, attacker):
    global heroes
    heroes[hero]["HP"] -= damage
    if heroes[hero]["HP"] <= 0:
        del heroes[hero]
        return f"{hero} has been killed by {attacker}!"
    return f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!"

# Function to recharge MP
def recharge(hero, mp_amount):
    if heroes[hero]["MP"] + mp_amount > 200:
        mp_recharged = 200 - heroes[hero]["MP"]
        heroes[hero]["MP"] = 200
    else:
        mp_recharged = mp_amount
        heroes[hero]["MP"] += mp_amount
    return f"{hero} recharged for {mp_recharged} MP!"

# Function to heal HP
def heal(hero, hp_amount):
    if heroes[hero]["HP"] + hp_amount > 100:
        hp_recovered = 100 - heroes[hero]["HP"]
        heroes[hero]["HP"] = 100
    else:
        hp_recovered = hp_amount
        heroes[hero]["HP"] += hp_amount
    return f"{hero} healed for {hp_recovered} HP!"

heroes = {}

number_of_heroes = int(input())
for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"HP":int(hit_points), "MP": int(mana_points)}

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    elif command[0] == "CastSpell":
        print(cast_spell(command[1], int(command[2]), command[3]))
    elif command[0] == "TakeDamage":
        print(take_damage(command[1], int(command[2]), command[3]))
    elif command[0] == "Recharge":
        result = recharge(command[1], int(command[2]))
        if result != False:
            print(result)
    elif command[0] == "Heal":
        result = heal(command[1], int(command[2]))
        if result != False:
            print(result)

for name, values in heroes.items():
    print(name)
    for key, value in values.items():
        print(f"  {key}: {value}")