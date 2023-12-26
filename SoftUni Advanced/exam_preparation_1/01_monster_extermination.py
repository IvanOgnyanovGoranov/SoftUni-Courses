from collections import deque

monsters = deque([int(x) for x in input().split(",")])


monsters_killed = 0

while monsters and soldier_strikes:
    current_monster = monsters.popleft()
    current_strike = soldier_strikes.pop()

    if current_strike >= current_monster:
        monsters_killed += 1
        strike_leftover = current_strike - current_monster
        if soldier_strikes:
            soldier_strikes[-1] += strike_leftover
        else:
            if strike_leftover > 0:
                soldier_strikes.append(strike_leftover)
    else:
        new_monster_value = current_monster - current_strike
        monsters.append(new_monster_value)

if not monsters:
    print("All monsters have been killed!")
if not soldier_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
