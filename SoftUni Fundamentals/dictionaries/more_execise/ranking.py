# contests = {}
# user_contests_scores = []
# best_candidate = ""
# while True:
#     command = input()
#     if command == "end of contests":
#         break
#     contest_name, password = command.split(":")
#     contests[contest_name] = password
#
# while True:
#     command = input()
#     if command == "end of submissions":
#         break
#     contest, password, username, points = command.split("=>")
#     is_valid = False
#     name_exists = False
#     for key, value in contests.items():
#         if key == contest and password == value:
#             is_valid = True
#     for dictionary in user_contests_scores:
#         if username in dictionary.values():
#             name_exists = True
#
#     if is_valid and not name_exists:
#         new_dict = {}
#         new_dict["name"] = username
#         new_dict[contest] = points
#         user_contests_scores.append(new_dict)
#     elif is_valid and name_exists:
#         for dictionary in user_contests_scores:
#             if dictionary["name"] == username:
#                 if contest in dictionary.keys():
#                     if int(points) > int(dictionary[contest]):
#                         dictionary[contest] = points
#                     else:
#                         continue
#                 else:
#                    dictionary[contest] = points
# sorted_dict = sorted(user_contests_scores, key=lambda item: item["name"])
# last_highest_points = 0
# for dict in sorted_dict:
#     total_sum = 0
#     name = dict["name"]
#     for key, value in dict.items():
#         if value.isdigit():
#             total_sum += int(value)
#     if total_sum > last_highest_points:
#         best_candidate = name
#         last_highest_points = total_sum
#
# print(f"Best candidate is {best_candidate} with total {last_highest_points} points.")
# print("Ranking:")
# for dictionary in sorted_dict:
#     new_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
#     print(dictionary["name"])
#     for key, value in new_dict:
#         if value != dictionary["name"]:
#             print(f"#  {key} -> {value}")

#Open AI code:
contests = {}
user_scores = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest_name, password = command.split(":")
    contests[contest_name] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in user_scores:
            user_scores[username] = {}
        if contest not in user_scores[username] or points > user_scores[username][contest]:
            user_scores[username][contest] = points

best_candidate = max(user_scores, key=lambda user: sum(user_scores[user].values()))

print(f"Best candidate is {best_candidate} with total {sum(user_scores[best_candidate].values())} points.")

sorted_users = sorted(user_scores.keys())
for user in sorted_users:
    print(user)
    for contest, points in sorted(user_scores[user].items(), key=lambda item: (-item[1], item[0])):
        print(f"# {contest} -> {points}")