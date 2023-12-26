def team_lineup(*args):
   teams = {}
   for tup in args:
      if tup[1] not in teams.keys():
         teams[tup[1]] = []
      teams[tup[1]] += [tup[0]]

   result = ""
   sorted_teams = dict(sorted(teams.items(), key=lambda item: (-len(item[1]), item[0])))
   for type, item in sorted_teams.items():
      result += f"{type}:\n"
      result += '\n'.join(f"  -{x}" for x in item)
      result += "\n"

   return result


# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
